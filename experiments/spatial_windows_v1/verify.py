#!/usr/bin/env python3
"""Finite checks for positive spatial-window spectral sampling.

Python 3.10+, NumPy, single BLAS thread recommended. No network or file writes.
This is not NMR data, interval certification, quantum hardware or a timing study.
The continuous-TV and all-size claims are proved in POSITIVE_SPATIAL_WINDOWS_21.md.
"""
from __future__ import annotations
from collections import Counter
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")

TOL = 4e-9
S = [np.array([[0, 1], [1, 0]], complex)/2,
     np.array([[0, -1j], [1j, 0]], complex)/2,
     np.diag([0.5, -0.5]).astype(complex)]
RAISE = S[0] + 1j*S[1]
COUNTS: Counter[str] = Counter()


def check(name: str, value: float | complex, expected: float | complex = 0.0,
          scale: float = 1.0) -> None:
    if abs(value-expected) > TOL*max(1.0, scale):
        raise AssertionError(f"{name}: {value!r} != {expected!r}")
    COUNTS[name] += 1


def require(name: str, ok: bool) -> None:
    if not ok:
        raise AssertionError(name)
    COUNTS[name] += 1


def site(n: int, i: int, op: np.ndarray) -> np.ndarray:
    out = np.ones((1, 1), complex)
    for k in range(n):
        out = np.kron(out, op if k == i else np.eye(2))
    return out


def model(offsets: list[float], bonds: list[float]):
    n = len(offsets)
    if n < 1 or len(bonds) != n-1 or not np.isfinite(offsets+bonds).all():
        raise ValueError("Invalid chain specification")
    spins = [[site(n, i, s) for s in S] for i in range(n)]
    h = sum(offsets[i]*spins[i][2] for i in range(n))
    edge_ops = [bonds[i]*sum(spins[i][a]@spins[i+1][a] for a in range(3))
                for i in range(n-1)]
    h = h + sum(edge_ops, np.zeros_like(h))
    o = sum(site(n, i, RAISE) for i in range(n))/math.sqrt(n/2)
    return h, o, edge_ops


def inner(a: np.ndarray, b: np.ndarray) -> complex:
    return np.vdot(a, b)/len(a)


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a@b-b@a


def partition(n: int, ell: int, shift: int):
    if n < 1 or ell < 1 or not 0 <= shift < ell:
        raise ValueError("Invalid partition")
    cuts = [b for b in range(1, n) if b % ell == shift]
    ends = [0] + cuts + [n]
    return cuts, list(zip(ends[:-1], ends[1:]))


class Spectral:
    def __init__(self, h: np.ndarray):
        self.e, self.u = np.linalg.eigh(h)
        self.gaps = self.e[:, None]-self.e[None, :]

    def act(self, x: np.ndarray, t: float | None = None,
            z: complex | None = None) -> np.ndarray:
        if (t is None) == (z is None):
            raise ValueError("Supply one of time or resolvent argument")
        a = self.u.conj().T@x@self.u
        factor = np.exp(-1j*t*self.gaps) if t is not None else 1/(z-self.gaps)
        return self.u@(a*factor)@self.u.conj().T

    def law(self, o: np.ndarray):
        a = self.u.conj().T@o@self.u
        weights = (np.abs(a)**2/len(o)).ravel()
        check("normalized_spectral_law", weights.sum(), 1)
        return self.gaps.ravel(), weights


def bins(law, gamma: float, edges: np.ndarray) -> np.ndarray:
    if not np.isfinite(gamma) or gamma <= 0:
        raise ValueError("Linewidth must be finite and positive")
    freq, weights = law
    cdf = np.arctan((edges[:, None]-freq[None, :])/gamma)/math.pi + 0.5
    return np.diff(cdf@weights)


def main() -> None:
    rows = []
    edges = np.array([-np.inf, -6, -1.2, -.4, 0, .4, 1.2, 6, np.inf])
    a0 = 2 + math.log(2) + 2/math.expm1(1)**2
    models = [([-.35, .35], [1.0]),
              ([-.5, .5, -.5, .5], [1., .7, 1.]),
              ([-.4, .4, -.4, .4, -.4, .4], [1., .8, 1.1, .9, 1.]),
              ([-.7, .2, .4, -.1, .9], [.6, -1., .8, .5])]
    for offsets, bonds in models:
        n = len(offsets)
        h, o, edge_ops = model(offsets, bonds)
        full = Spectral(h)
        full_law = full.law(o)
        jstar = max(abs(x) for x in bonds)
        velocity = 4.5*math.e*jstar
        cache = {}
        for ell in sorted({1, min(2, n), min(3, n), min(4, n)}):
            mixed = {g: np.zeros(len(edges)-1) for g in [.35, 2., 8.]}
            mean_s2 = 0.0
            fourth = 0.0
            for shift in range(ell):
                cuts, blocks = partition(n, ell, shift)
                require("block_partition", sum(r-l for l, r in blocks) == n
                        and max(r-l for l, r in blocks) <= ell)
                s2 = sum(bonds[b-1]**2 for b in cuts)
                mean_s2 += s2/ell
                removed = sum((edge_ops[b-1] for b in cuts), np.zeros_like(h))
                sliced = Spectral(h-removed)
                sliced_law = sliced.law(o)
                fourth += float(sliced_law[1]@(sliced_law[0]**4))/ell
                for gamma in mixed:
                    from_blocks = np.zeros(len(edges)-1)
                    for left, right in blocks:
                        key = (left, right)
                        if key not in cache:
                            hb, ob, _ = model(offsets[left:right], bonds[left:right-1])
                            cache[key] = Spectral(hb).law(ob)
                        from_blocks += (right-left)/n*bins(cache[key], gamma, edges)
                    direct = bins(sliced_law, gamma, edges)
                    check("positive_block_mixture_identity", np.max(abs(direct-from_blocks)))
                    require("positive_normalized_bins", from_blocks.min() >= -TOL
                            and abs(from_blocks.sum()-1) < TOL)
                    mixed[gamma] += from_blocks/ell
                # Probe the two ingredients that avoid an extensive collective error.
                for t in [0., .2, .9]:
                    evolved = sliced.act(o, t=t)*math.sqrt(n/2)
                    residuals = [comm(edge_ops[b-1], evolved) for b in cuts]
                    for i in range(len(residuals)):
                        for j in range(i):
                            check("distinct_cut_residual_orthogonality",
                                  inner(residuals[i], residuals[j]))
                    residual = comm(removed, evolved/math.sqrt(n/2))
                    require("boundary_residual_envelope", inner(residual, residual).real
                            <= 18*s2/n*(a0+velocity*t) + TOL)
                for z in [.25+.7j, -.8+1.2j]:
                    r0 = lambda x: sliced.act(x, z=z)
                    r = lambda x: full.act(x, z=z)
                    d = lambda x: comm(removed, x)
                    first = inner(o, r0(d(r0(o))))
                    check("first_resolvent_term_vanishes", first)
                    second = inner(o, r0(d(r(d(r0(o))))))
                    lhs = inner(o, r(o)-r0(o))
                    check("second_resolvent_identity", lhs, second,
                          max(abs(lhs), abs(second)))
            check("averaged_cut_strength", mean_s2, sum(x*x for x in bonds)/ell)
            if n % 2 == 0 and all(abs(x-((-1)**(i+1))*abs(offsets[0])) < 1e-12
                                    for i, x in enumerate(offsets)):
                dfield = abs(offsets[0])
                expected = dfield**4 + 2*dfield**2/n*(1-1/ell)*sum(x*x for x in bonds)
                check("averaged_fourth_moment", fourth, expected)
            for gamma, pmix in mixed.items():
                pfull = bins(full_law, gamma, edges)
                tv = float(abs(pfull-pmix).sum()/2)
                x = 9*sum(j*j for j in bonds)/(n*ell*gamma**2)*(a0+velocity/(2*gamma))
                bound = min(1., x, math.sqrt(x/2))
                require("binned_TV_bound_diagnostic", tv <= bound + TOL)
                rows.append({"n": n, "block_limit": ell, "gamma": gamma,
                             "binned_TV": tv, "analytic_bound": bound})
    # Collective two-spin response is not the average of coupled local responses.
    h, o, _ = model([0., 0.], [1.])
    sp = Spectral(h)
    collective = bins(sp.law(o), .1, edges)
    local = site(2, 0, RAISE)*math.sqrt(2)
    local_p = bins(sp.law(local), .1, edges)
    local_error = float(abs(collective-local_p).sum()/2)
    require("local_spectrum_substitution_detected", local_error > .1)
    # Every disconnected isotropic block preserves the uniform-field line.
    for n in [2, 4, 6]:
        h, o, _ = model([.37]*n, [1.]*(n-1))
        law = Spectral(h).law(o)
        target = bins((np.array([.37]), np.array([1.])), .2, edges)
        check("uniform_field_exact_control", np.max(abs(bins(law, .2, edges)-target)))
    # Do not remove each block's own carrier without adding it back.
    single = bins((np.array([-.7, .7]), np.array([.5, .5])), .2, edges)
    centered = bins((np.array([0.]), np.array([1.])), .2, edges)
    carrier_error = float(abs(single-centered).sum()/2)
    require("lost_block_carrier_detected", carrier_error > .1)
    invalid = [lambda: partition(0, 2, 0), lambda: partition(4, 0, 0),
               lambda: partition(4, 2, 2), lambda: model([0., 0.], []),
               lambda: bins((np.array([0.]), np.array([1.])), 0., edges),
               lambda: bins((np.array([0.]), np.array([1.])), float('nan'), edges)]
    for case in invalid:
        try:
            case()
        except ValueError:
            COUNTS["invalid_inputs_rejected"] += 1
        else:
            raise AssertionError("Invalid control accepted")
    print(json.dumps({"status": "pass", "scope": "Finite complex128 identities; no experimental data, native NMR solver, compiled circuit or performance claim.",
                      "tolerance": TOL, "numpy_version": np.__version__,
                      "counts": dict(sorted(COUNTS.items())), "rows": rows,
                      "local_substitution_bin_TV": local_error,
                      "block_carrier_bin_TV": carrier_error,
                      "constants": {"C_LR": 2, "mu": 1, "v_over_Jstar": 4.5*math.e, "a0": a0}},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
