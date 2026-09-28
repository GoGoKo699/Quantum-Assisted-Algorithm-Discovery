#!/usr/bin/env python3
"""Finite mathematical controls for linewidth-weighted Lanczos truncation.

Independent Python 3.10+/NumPy diagnostic, not a native NMR implementation,
quantum circuit, empirical performance study, or interval-arithmetic certificate.
No file writes. Run without -O/-OO; use one BLAS thread for reproducible replay.
"""
from __future__ import annotations
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")

TOL = 2e-9
P = [np.eye(2, dtype=complex), np.array([[0, 1], [1, 0]], complex),
     np.array([[0, -1j], [1j, 0]], complex), np.diag([1., -1.]).astype(complex)]


def check(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def kron_all(items):
    out = np.array([[1.]], complex)
    for item in items:
        out = np.kron(out, item)
    return out


def pauli_matrix(key):
    return kron_all([P[k] for k in key])


def spin_model(offsets, couplings):
    n = len(offsets)
    check(len(couplings) == n - 1, "open chain edge count")
    terms = {}
    obs = {}
    for i, d in enumerate(offsets):
        s = [0] * n; s[i] = 3
        terms[tuple(s)] = d / 2
        for p, c in [(1, .5), (2, .5j)]:
            s = [0] * n; s[i] = p
            obs[tuple(s)] = c
    for i, j in enumerate(couplings):
        for p in [1, 2, 3]:
            s = [0] * n; s[i] = s[i+1] = p
            terms[tuple(s)] = j / 4
    h = sum(c * pauli_matrix(k) for k, c in terms.items())
    o = sum(c * pauli_matrix(k) for k, c in obs.items())
    return h, o, terms, obs


def product_key(a, b):
    out = []; phase = 1 + 0j
    for x, y in zip(a, b):
        if x == 0: out.append(y)
        elif y == 0: out.append(x)
        elif x == y: out.append(0)
        else:
            out.append(6 - x - y)
            phase *= 1j if (x, y) in [(1, 2), (2, 3), (3, 1)] else -1j
    return tuple(out), phase


def sparse_comm(terms, obs):
    out = {}
    for a, ha in terms.items():
        for b, ob in obs.items():
            k, ab = product_key(a, b)
            _, ba = product_key(b, a)
            out[k] = out.get(k, 0j) + ha * ob * (ab - ba)
    return {k: c for k, c in out.items() if abs(c) > 1e-12}


def lanczos(apply, start, m):
    v = np.asarray(start, complex).reshape(-1)
    v = v / np.linalg.norm(v)
    basis = []; aa = []; bb = []
    for j in range(m):
        basis.append(v.copy())
        w = apply(v)
        a = np.vdot(v, w)
        check(abs(a.imag) < TOL, "Hermitian Lanczos diagonal")
        aa.append(float(a.real))
        w -= a.real * v
        if j: w -= bb[j-1] * basis[j-1]
        # Reorthogonalization affects roundoff, not the exact recurrence.
        for q in basis:
            w -= q * np.vdot(q, w)
        b = float(np.linalg.norm(w))
        bb.append(b)
        if b < 1e-12:
            bb[-1] = 0.
            break
        v = w / b
    q = np.column_stack(basis)
    jmat = np.diag(aa)
    if len(aa) > 1:
        jmat += np.diag(bb[:-1], 1) + np.diag(bb[:-1], -1)
    b = bb[-1]
    r = v if b > 0 else np.zeros_like(basis[0])
    residual = np.column_stack([apply(q[:, j]) for j in range(q.shape[1])]) - q @ jmat
    target = np.zeros_like(residual)
    target[:, -1] = b * r
    check(np.linalg.norm(residual - target) < TOL, "Lanczos residual relation")
    check(np.linalg.norm(q.conj().T @ q - np.eye(len(aa))) < TOL, "basis orthogonality")
    return q, jmat, b, r


def boundary_mass(jmat, gamma):
    if not math.isfinite(gamma) or gamma <= 0:
        raise ValueError("linewidth must be finite and positive")
    lam, u = np.linalg.eigh(jmat)
    c = u[-1] * u[0]
    diff = lam[:, None] - lam[None, :]
    ans = float(np.sum(c[:, None] * c[None, :] *
                       (4 * gamma**2 / (4 * gamma**2 + diff**2))))
    check(-TOL <= ans <= 1 + TOL, "boundary occupation range")
    return min(1., max(0., ans))


def bound(jmat, beta, gamma):
    q = boundary_mass(jmat, gamma)
    linear = beta * math.sqrt(q) / (2 * gamma)
    quadratic = beta**2 * q / (2 * gamma**2)
    return q, min(1., linear, quadratic)


def binned(lam, weight, gamma, edges):
    cdf = .5 + np.arctan((edges[:, None] - lam[None, :]) / gamma) / np.pi
    out = np.diff(cdf @ weight)
    check(abs(out.sum() - 1.) < TOL and out.min() > -TOL, "binned probability law")
    return out


def small_law(a, v):
    lam, u = np.linalg.eigh(a)
    return lam, abs(u.conj().T @ v)**2


def main():
    counts = {"spin_bound_checks": 0, "moment_checks": 0,
              "sparse_support_checks": 0, "resolvent_identity_checks": 0,
              "complex_basis_checks": 0, "analytic_boundary_controls": 0}
    rows = []
    models = [("pair", [-.6, .6], [1.1]),
              ("chain4", [-.9, .4, -.2, .7], [1., .8, 1.2]),
              ("staggered6", [-.7, .7, -.7, .7, -.7, .7], [1., .9, 1.1, .8, 1.2])]
    for name, offsets, couplings in models:
        h, o, terms, obs = spin_model(offsets, couplings)
        d = len(h); n = len(offsets)
        start = o.reshape(-1) / np.linalg.norm(o)
        apply = lambda v: (h @ v.reshape(d, d) - v.reshape(d, d) @ h).reshape(-1)
        energy, u = np.linalg.eigh(h)
        lam = (energy[:, None] - energy[None, :]).reshape(-1)
        weight = (abs(u.conj().T @ o @ u)**2 / np.linalg.norm(o)**2).reshape(-1)
        sparse = obs.copy(); dense = o.copy(); supports = []
        for k in range(5):
            rebuilt = sum((c * pauli_matrix(key) for key, c in sparse.items()), np.zeros_like(o))
            check(np.linalg.norm(rebuilt - dense) < TOL * max(1., np.linalg.norm(dense)), "sparse commutator")
            for key in sparse:
                sites = [i for i, p in enumerate(key) if p]
                check(sites and max(sites) - min(sites) + 1 <= k+1, "connected interval envelope")
            supports.append(len(sparse)); counts["sparse_support_checks"] += 1
            sparse = sparse_comm(terms, sparse)
            dense = h @ dense - dense @ h
        for m in [1, 2, 4, 6]:
            qmat, jmat, beta, r = lanczos(apply, start, m)
            ell, vec = np.linalg.eigh(jmat); w = vec[0]**2
            for k in range(2*len(jmat)):
                exact = float(np.sum(weight * lam**k))
                approx = float(np.sum(w * ell**k))
                check(abs(exact - approx) < 2e-7 * max(1., abs(exact)), "Gauss moment identity")
                counts["moment_checks"] += 1
            for gamma in [.4, 1., 3.]:
                edge = np.r_[-np.inf, np.linspace(lam.min()-5*gamma, lam.max()+5*gamma, 181), np.inf]
                tv = float(np.abs(binned(lam, weight, gamma, edge) - binned(ell, w, gamma, edge)).sum()/2)
                qm, certificate = bound(jmat, beta, gamma)
                check(tv <= certificate + TOL, "binned TV exceeds proven continuous bound")
                for omega in [-1.3, .2, 2.1]:
                    z = omega + 1j * gamma
                    small = np.linalg.inv(z*np.eye(len(jmat))-jmat)
                    # Use the exact energy-gap eigenbasis without building the full Liouvillian.
                    r_e = (u.conj().T @ r.reshape(d,d) @ u).reshape(-1)
                    full = np.sum(weight / (z-lam))
                    tail = np.sum(abs(r_e)**2 / (z-lam))
                    check(abs(full-small[0,0]-beta**2*small[0,-1]**2*tail) < TOL, "quadratic resolvent identity")
                    counts["resolvent_identity_checks"] += 1
                rows.append({"model": name, "m": len(jmat), "gamma": gamma,
                             "boundary_mass": round(qm, 12), "beta": round(beta, 12),
                             "proven_bound_evaluated_float": round(certificate, 12),
                             "finite_bin_TV": round(tv, 12)})
                counts["spin_bound_checks"] += 1
        rows[-1]["nested_commutator_Pauli_counts_k0_to_k4"] = supports
    for a, c, b in [(0.,0.,.7), (-.5,.3,1.2), (1.,-1.,.1)]:
        j = np.array([[a,b],[b,c]])
        for gamma in [.2, 1., 4.]:
            exact = b*b / (2*(gamma*gamma+b*b+(a-c)**2/4))
            check(abs(boundary_mass(j,gamma)-exact) < TOL, "analytic two-mode occupation")
            counts["analytic_boundary_controls"] += 1
    # Complex Hermitian matrices must still give a real Jacobi representation.
    a = np.array([[.2, 1+1j, .1, 0], [1-1j, -.4, .7j, .3],
                  [.1,-.7j,.6,.8],[0,.3,.8,-.2]], complex)
    v = np.array([1., .2j, -.3, .4j]); v /= np.linalg.norm(v)
    phase = np.diag(np.exp(1j*np.array([.1,.7,-.3,1.2])))
    for m in [1,2,3]:
        _, j, b, _ = lanczos(lambda x: a@x, v, m)
        _, jj, bb, _ = lanczos(lambda x: phase@a@phase.conj().T@x, phase@v, m)
        check(np.linalg.norm(j-jj) < TOL and abs(b-bb) < TOL, "complex-basis covariance")
        counts["complex_basis_checks"] += 1
    # The collective signal is not an incoherent mixture of local signals.
    h, o, _, _ = spin_model([0.,0.], [1.])
    check(np.linalg.norm(h@o-o@h) < TOL, "collective symmetry")
    local = np.kron((P[1]+1j*P[2])/2, P[0])
    ee, uu = np.linalg.eigh(h)
    ww = abs(uu.conj().T@local@uu)**2 / np.linalg.norm(local)**2
    gaps = ee[:,None]-ee[None,:]
    local_masses = [float(ww[np.isclose(gaps,x)].sum()) for x in [-1.,0.,1.]]
    check(np.allclose(local_masses,[.25,.5,.25],atol=TOL), "local-mixture negative control")
    # Discarding an unknown residual is not a valid zero-error certificate.
    check(any(r["finite_bin_TV"] > .05 for r in rows if r["m"] == 1), "omitted residual negative control")
    invalid = 0
    for gamma in [0., -1., float("inf"), float("nan")]:
        try: boundary_mass(np.zeros((1,1)), gamma)
        except ValueError: invalid += 1
        else: raise AssertionError("bad linewidth accepted")
    print(json.dumps({"status":"pass", "scope":"Double-precision finite mathematical controls only; no experimental spectrum, compiled quantum circuit or timing benchmark.",
                      "numpy_version":np.__version__, "tolerance":TOL, "counts":counts,
                      "collective_vs_local_negative_control": {"collective_zero_line_mass":1., "local_masses_minus1_0_plus1":local_masses},
                      "invalid_linewidths_rejected":invalid, "rows":rows}, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
