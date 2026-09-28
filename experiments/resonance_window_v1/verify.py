#!/usr/bin/env python3
"""Finite checks of a resonance-window spectral bound; not a speedup benchmark.

Python 3.10+, NumPy. No network, input files, or file writes. Complex128 checks
support, but do not replace, the analytic continuous-TV proof in Note 19.
"""
from __future__ import annotations
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O/-OO.")
TOL = 3e-8
COUNTS: dict[str, int] = {}


def require(ok: bool, name: str) -> None:
    if not ok:
        raise AssertionError(name)
    COUNTS[name] = COUNTS.get(name, 0) + 1


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, 2)) if a.size else 0.0


def close(a: np.ndarray, b: np.ndarray, name: str) -> None:
    require(opnorm(np.atleast_2d(a - b)) <= TOL * max(1.0, opnorm(np.atleast_2d(b))), name)


def lines(a: np.ndarray, v: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    lam, u = np.linalg.eigh(a)
    w = np.abs(u.conj().T @ v) ** 2
    require(abs(float(w.sum()) - 1) < TOL, "normalized_spectral_law")
    return lam, w


def binmass(law: tuple[np.ndarray, np.ndarray], gamma: float, edges: np.ndarray) -> np.ndarray:
    lam, w = law
    cdf = np.arctan((edges[:, None] - lam[None, :]) / gamma) / np.pi + 0.5
    mass = np.diff(cdf @ w)
    require(float(mass.min()) >= -TOL and abs(float(mass.sum()) - 1) < TOL, "normalized_binned_law")
    return mass


def certificate(cross: float, beta: float, gamma: float, window: float,
                s2: float, k2: float, exposure: float | None = None) -> tuple[float, float, float]:
    vals = (cross, beta, gamma, window, s2, k2)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("All parameters must be finite")
    if cross < 0 or beta <= 0 or gamma <= 0 or not 0 < window < beta or s2 < 0 or k2 < 0:
        raise ValueError("Invalid nonnegative norms or positive beta/gamma/window")
    residual = cross**2 * math.hypot(window, gamma) / (beta * (beta - window))
    central = residual / (2 * gamma)
    if exposure is not None:
        if not math.isfinite(exposure) or exposure < 0:
            raise ValueError("Exposure must be finite and nonnegative")
        central = min(central, cross * math.hypot(window, gamma) * math.sqrt(exposure) / (2 * gamma * (beta-window)))
    tails = 2 * (s2 + k2) / window**2 + 2 / np.pi * math.atan(2 * gamma / window)
    return min(1.0, central + tails), central, tails


def analyze(l0: np.ndarray, perturb: np.ndarray, obs: np.ndarray,
            cutoff: float, gamma: float, name: str, do_resolvents: bool = True) -> dict:
    close(l0, l0.conj().T, "hermitian_input")
    close(perturb, perturb.conj().T, "hermitian_input")
    close(l0 @ obs, np.zeros_like(obs), "conserved_start")
    ev, u = np.linalg.eigh(l0)
    low = np.abs(ev) <= cutoff
    order = np.r_[np.flatnonzero(low), np.flatnonzero(~low)]
    u, ev = u[:, order], ev[order]
    m = int(low.sum())
    require(0 < m < len(ev), "nontrivial_partition")
    e = opnorm(perturb)
    beta = cutoff - e
    require(beta > 0, "valid_far_gap_promise")
    h = np.diag(ev) + u.conj().T @ perturb @ u
    v = u.conj().T @ obs
    close(v[m:], np.zeros_like(v[m:]), "observable_in_retained_space")
    vp = v[:m]
    a, f, b = h[:m, :m], h[m:, :m], h[m:, m:]
    gap = float(np.min(np.abs(np.linalg.eigvalsh(b))))
    require(gap + TOL >= beta, "far_inverse_bound")
    binvf = np.linalg.solve(b, f)
    k = a - f.conj().T @ binvf
    close(k, k.conj().T, "hermitian_static_schur")
    c = opnorm(f)
    s2 = float(np.linalg.norm(h @ v)**2)
    k2 = float(np.linalg.norm(k @ vp)**2)
    require(k2 <= s2 * (1 + (c / beta)**2) + TOL * max(s2, k2, 1e-30), "response_moment_bound")
    lamk, uk = np.linalg.eigh(k)
    zeta = uk.conj().T @ vp
    gram = uk.conj().T @ (binvf.conj().T @ binvf) @ uk
    frequencies = lamk[None, :] - lamk[:, None]
    exposure_complex = np.sum(zeta.conj()[:, None] * zeta[None, :] * gram * (2*gamma)/(2*gamma+1j*frequencies))
    require(abs(exposure_complex.imag) < TOL * max(abs(exposure_complex.real), 1e-30), "real_dressing_exposure")
    exposure = float(exposure_complex.real)
    require(0 <= exposure <= (1+TOL) * (c/beta)**2 + 1e-30, "dressing_exposure_bound")
    # Independent Sylvester/Lyapunov identity for the damped time integral.
    filt_gram = gram * (2*gamma)/(2*gamma+1j*frequencies)
    close(2*gamma*filt_gram + 1j*frequencies*filt_gram, 2*gamma*gram, "dressing_integral_equation")
    # Optimize only the sufficient certificate, not the computed spectral discrepancy.
    candidates = np.geomspace(beta * 1e-6, beta * 0.85, 240)
    selected = min(((*certificate(c, beta, gamma, float(w), s2, k2, exposure), float(w)) for w in candidates), key=lambda r: r[1] + r[2])
    bound, central, tails, window = selected
    law, klaw = lines(h, v), lines(k, vp)
    shifts = gamma * np.array([-10, -2, -1, -0.5, 0, 0.5, 1, 2, 10])
    finite = np.r_[(law[0][:, None] + shifts).ravel(), (klaw[0][:, None] + shifts).ravel(), -window, window]
    edges = np.r_[-np.inf, np.unique(finite), np.inf]
    tv = float(np.abs(binmass(law, gamma, edges) - binmass(klaw, gamma, edges)).sum() / 2)
    require(tv <= bound + TOL, "binned_bound_diagnostic")
    if do_resolvents:
        for omega in [-window, 0.0, window]:
            z = omega + 1j * gamma
            rb = np.linalg.inv(z * np.eye(len(b)) - b)
            sigma_delta = f.conj().T @ (rb @ (z * binvf))
            close(sigma_delta, f.conj().T @ rb @ f + f.conj().T @ binvf, "self_energy_remainder_identity")
            rp = np.linalg.inv(z * np.eye(m) - a - f.conj().T @ rb @ f)
            rk = np.linalg.inv(z * np.eye(m) - k)
            full = np.linalg.inv(z * np.eye(len(h)) - h)[:m, :m]
            close(rp, full, "feshbach_resolvent_identity")
            # Test the product form with a scale that includes both resolvents:
            # direct subtraction loses digits when gamma is very small.
            defect = (rp - rk) - rp @ sigma_delta @ rk
            require(opnorm(defect) <= TOL * max(1.0, opnorm(rp), opnorm(rk)), "compressed_resolvent_difference")
            require(opnorm(sigma_delta) <= (1 + TOL) * c*c*abs(z)/(beta*(beta-abs(omega))) + 1e-30, "self_energy_norm_bound")
    nonzero = np.abs(ev[np.abs(ev) > 1e-13])
    return {"name": name, "dimension": len(ev), "retained_dimension": m,
            "cutoff": cutoff, "perturbation_norm": e, "linewidth": gamma,
            "diagnostic_min_nonzero_frequency": float(nonzero.min()),
            "diagnostic_edge_distance": float(np.min(np.abs(np.abs(ev) - cutoff))),
            "certified_far_lower_bound": beta, "selected_window": window,
            "bound": bound, "central_bound": central, "tail_bound": tails,
            "dressing_exposure": exposure, "dressing_exposure_upper_bound": (c/beta)**2,
            "binned_TV_diagnostic": tv}


def spin_chain(n: int, d: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    z = np.diag([0.5, -0.5]).astype(complex)
    plus = np.array([[0, 1], [0, 0]], dtype=complex)
    def embed(a, j):
        out = np.array([[1]], dtype=complex)
        for site in range(n):
            out = np.kron(out, a if site == j else np.eye(2))
        return out
    sz = [embed(z, j) for j in range(n)]
    sp = [embed(plus, j) for j in range(n)]
    dim = 2**n
    h0 = np.zeros((dim, dim), dtype=complex)
    for j in range(n-1):
        h0 += sz[j] @ sz[j+1] + (sp[j] @ sp[j+1].conj().T + sp[j].conj().T @ sp[j+1]) / 2
    fld = sum((-1)**j * sz[j] for j in range(n))
    o = sum(sp) / math.sqrt(n * 2**(n-1))
    # Coherence +1 is invariant under both commutators; no magnetization blocks are discarded.
    mags = np.diag(sum(sz)).real
    pairs = [(a, b) for a in range(dim) for b in range(dim) if abs(mags[a]-mags[b]-1) < 1e-12]
    a, b = np.array(pairs).T
    l0 = h0[a[:, None], a[None, :]] * (b[:, None] == b[None, :]) - (a[:, None] == a[None, :]) * h0[b[None, :], b[:, None]]
    dg = np.diag(fld).real
    perturb = np.diag(d * (dg[a] - dg[b]))
    obs = o[a, b]
    return l0, perturb, obs


def main() -> None:
    rows = []
    for n, cutoff, d in [(2, 0.5, 0.001), (4, 0.6, 0.0001), (6, 0.2, 0.0002)]:
        l0, e, obs = spin_chain(n, d)
        require(abs(float(np.linalg.norm(e @ obs)**2) - d*d) < TOL * d*d, "spin_second_moment")
        rows.append(analyze(l0, e, obs, cutoff, d*d, f"open_uniform_chain_n{n}", n <= 4))
    # Coupled arbitrarily small frequencies and near-cutoff levels, not an application model.
    for tiny, edge in [(1e-3, 1e-3), (1e-8, 1e-3), (1e-8, 1e-9)]:
        diag = np.array([0, tiny, 0.5-edge, 0.5+edge, -1.0, 1.4])
        raw = np.array([[0,1,.2,.3,.4,-.2], [1,.3,.4,-.2,.3,.1], [.2,.4,-.1,.6,.2,.2], [.3,-.2,.6,.2,.5,-.3], [.4,.3,.2,.5,-.4,.2], [-.2,.1,.2,-.3,.2,.1]])
        e = raw * (0.0001 / opnorm(raw))
        rows.append(analyze(np.diag(diag), e, np.eye(6)[:, 0], 0.5, 1e-8, f"boundary_and_resonance_control_{tiny}_{edge}"))
    # Dropping a resonant first-order block or its normalization is NOT licensed.
    d = 0.01
    h = np.array([[0., d], [d, 0.]])
    law = lines(h, np.array([1.,0.]))
    gamma = 0.1*d
    edges = np.array([-np.inf, -d/2, d/2, np.inf])
    exact = binmass(law, gamma, edges)
    wrong = binmass((np.array([0.]), np.array([1.])), gamma, edges)
    bad_tv = float(np.abs(exact-wrong).sum()/2)
    require(bad_tv > 0.8, "discarded_resonance_negative_control")
    # No-gap-at-boundary geometry is permitted by the proof, not by a sharp-filter oracle for free.
    require(rows[-1]["diagnostic_edge_distance"] < 2e-9 and rows[-1]["certified_far_lower_bound"] > .49, "edge_and_inverse_gaps_are_distinct")
    invalid = [(0,.5,0,.1,1,1), (0,.5,.1,.5,1,1), (0,.5,.1,0,1,1), (-1,.5,.1,.1,1,1), (0,.5,.1,.1,-1,1), (0,float('nan'),.1,.1,1,1)]
    for args in invalid:
        try:
            certificate(*args)
        except ValueError:
            require(True, "invalid_parameters_rejected")
        else:
            raise AssertionError("Invalid parameter accepted")
    print(json.dumps({"status": "pass", "scope": "Finite complex128 identities and binned controls, not interval certificates, hardware, full classical comparisons, or scaling measurements.", "numpy_version": np.__version__, "tolerance": TOL, "counts": COUNTS, "rows": rows, "discarded_resonance_bin_TV": bad_tv}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
