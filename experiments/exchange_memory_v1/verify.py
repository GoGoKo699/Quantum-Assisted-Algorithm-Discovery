#!/usr/bin/env python3
"""Finite checks of the exchange-memory derivation; not a physical benchmark.

Python 3.10+ and NumPy, complex128. No input files, network calls, or file writes.
No general short-memory assumption is inferred from these finite systems.
"""
from __future__ import annotations
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")

TOL = 3e-10


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def close(a, b, message: str) -> None:
    require(bool(np.allclose(a, b, atol=TOL, rtol=TOL)), message)


def embed(a: np.ndarray, site: int, n: int) -> np.ndarray:
    out = np.ones((1, 1), complex)
    for j in range(n):
        out = np.kron(out, a if j == site else np.eye(2))
    return out


def system(n: int, d: float, bonds: list[float]):
    require(n >= 2 and n % 2 == 0 and len(bonds) == n - 1, "Invalid chain")
    sx = np.array([[0, 1], [1, 0]], complex) / 2
    sy = np.array([[0, -1j], [1j, 0]], complex) / 2
    sz = np.diag([.5, -.5]).astype(complex)
    spins = [[embed(a, j, n) for j in range(n)] for a in (sx, sy, sz)]
    raising = [spins[0][j] + 1j * spins[1][j] for j in range(n)]
    obs = sum(raising)
    alt = sum((-1)**j * raising[j] for j in range(n))
    h = d * sum((-1)**j * spins[2][j] for j in range(n))
    for j, coupling in enumerate(bonds):
        h += coupling * sum(s[j] @ s[j + 1] for s in spins)
    size = 2**n
    liouvillian = np.kron(h, np.eye(size)) - np.kron(np.eye(size), h.T)
    scale = math.sqrt(n * size / 2)
    return liouvillian, obs.reshape(-1) / scale, alt.reshape(-1) / scale


def law(matrix: np.ndarray, vector: np.ndarray):
    values, vectors = np.linalg.eigh(matrix)
    weights = np.abs(vectors.conj().T @ vector)**2
    close(weights.sum(), 1, "Probability normalization")
    return values, weights


def transform(values, weights, z: complex) -> complex:
    return complex(np.sum(weights / (z - values)))


def bin_law(values, weights, edges, gamma: float):
    require(gamma > 0, "Positive linewidth required")
    cdf = np.sum(weights[:, None] * (.5 + np.arctan(
        (np.asarray(edges)[None, :] - values[:, None]) / gamma) / np.pi), axis=0)
    return np.diff(cdf)


def memory_certificate(d: float, gamma: float, window: float,
                       kappa: float, delta: float) -> float:
    vals = (d, gamma, window, kappa, delta)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("Parameters must be finite")
    if d < 0 or gamma <= 0 or window <= 0 or kappa < 0 or delta < 0:
        raise ValueError("Invalid sign or zero scale")
    width = gamma + d*d*kappa
    ratio = d*d*delta / width
    if ratio >= 1:
        return 1.0
    middle = ratio * math.atan(window / width) / (math.pi * (1 - ratio))
    tail = 2*d*d/window**2 + (math.atan(2*gamma/window)
                             + math.atan(width/window)) / math.pi
    return min(1.0, middle + tail)


def jacobi(offdiagonal: list[float]) -> np.ndarray:
    result = np.zeros((len(offdiagonal) + 1,) * 2)
    for j, value in enumerate(offdiagonal):
        result[j, j+1] = result[j+1, j] = value
    return result


def main() -> None:
    counts = {"spin_resolvent_checks": 0, "memory_symmetry_checks": 0,
              "projected_generator_checks": 0, "reflection_checks": 0,
              "window_envelope_checks": 0, "binned_certificate_checks": 0,
              "truncated_memory_checks": 0, "dimer_identity_checks": 0}
    rows = []
    for n, d, bonds in [(2, .2, [1.0]), (4, .3, [1., 1., 1.]),
                        (4, .15, [1., .7, 1.])]:
        liouv, o, v = system(n, d, bonds)
        ident = np.eye(liouv.shape[0])
        q = ident - np.outer(o, o.conj())
        link = d * (np.outer(o, v.conj()) + np.outer(v, o.conj()))
        bath = liouv - link
        close(np.vdot(o, v), 0, "Alternating mode orthogonality")
        close(liouv @ o, d*v, "Exact collective-to-staggered link")
        close(bath, q @ liouv @ q, "Projected generator")
        close(bath @ o, 0, "Collective mode decoupled")
        close(np.vdot(bath @ v, bath @ v), 2*sum(x*x for x in bonds)/n,
              "First memory moment")
        counts["projected_generator_checks"] += 5
        plus, minus = (o+v)/math.sqrt(2), (o-v)/math.sqrt(2)
        rp = ident - 2*np.outer(plus, plus.conj())
        rm = ident - 2*np.outer(minus, minus.conj())
        close(bath, liouv + d*(rp-rm)/2, "Two reflection representation")
        close(rp @ rp, ident, "First reflection")
        close(rm @ rm, ident, "Second reflection")
        counts["reflection_checks"] += 3
        ev, wt = law(liouv, o)
        bv, bw = law(bath, v)
        close(np.dot(wt, ev), 0, "Unbroadened first moment")
        close(np.dot(wt, ev**2), d*d, "Unbroadened second moment")
        for gamma in [.15, .6, 1.2]:
            for frequency in [-1.3, -.2, 0., .2, 1.3]:
                z = complex(frequency, gamma)
                f = transform(bv, bw, z)
                close(transform(ev, wt, z), 1/(z-d*d*f), "Schur identity")
                close(transform(bv, bw, complex(-frequency, gamma)),
                      -f.conjugate(), "Even memory spectrum")
                counts["spin_resolvent_checks"] += 1
                counts["memory_symmetry_checks"] += 1
            kappa = -transform(bv, bw, 1j*gamma).imag
            for time in [.25, 2.0]:
                integrated = np.sum(bw * (1-np.exp(-(gamma+1j*bv)*time))
                                    / (gamma+1j*bv)).real
                require(abs(integrated-kappa) <= math.exp(-gamma*time)/gamma + TOL,
                        "Truncated damped memory bound")
                counts["truncated_memory_checks"] += 1
        gamma, window = .6, 3.
        kappa = -transform(bv, bw, 1j*gamma).imag
        distance = np.maximum(np.abs(bv)-window, 0.)
        # A rigorous analytic envelope for these finite input matrices, not
        # a supremum inferred from the evaluation grid below.
        delta = float(window*np.sum(bw/(np.hypot(bv, gamma)
                                        * np.hypot(distance, gamma))))
        for frequency in np.linspace(-window, window, 51):
            require(abs(transform(bv, bw, complex(frequency, gamma))+1j*kappa)
                    <= delta+TOL, "Window envelope")
            counts["window_envelope_checks"] += 1
        bound = memory_certificate(d, gamma, window, kappa, delta)
        edges = np.r_[-np.inf, np.linspace(-10, 10, 2001), np.inf]
        p = bin_law(ev, wt, edges, gamma)
        approx = bin_law(np.array([0.]), np.array([1.]), edges, gamma+d*d*kappa)
        tv = float(np.sum(np.abs(p-approx))/2)
        require(tv <= bound+TOL, "Finite-bin consistency with written certificate")
        counts["binned_certificate_checks"] += 1
        rows.append({"n": n, "d": d, "gamma": gamma, "window": window,
                     "bound": bound, "binned_TV_diagnostic": tv})

    dimer_rows = []
    c = .1
    for d in [.2, .1, .05, .01]:
        full, root = jacobi([d, 1., d]), np.array([1., 0., 0., 0.])
        vals, probs = law(full, root)
        # Check the closed chain against the actual two-spin Liouvillian.
        liouv, o, v = system(2, d, [1.])
        le, lw = law(liouv, o)
        for z in [.2+.1j, -.4+.3j, 1j*d*d]:
            f = (z*z-d*d)/(z*(z*z-1-d*d))
            close(transform(vals, probs, z), 1/(z-d*d*f), "Dimer memory formula")
            close(transform(le, lw, z), transform(vals, probs, z), "Dimer realization")
            counts["dimer_identity_checks"] += 2
        scale, gamma = d*d, c*d*d
        edges = [-np.inf, -scale/2, scale/2, np.inf]
        exact_bins = bin_law(vals, probs, edges, gamma)
        frozen_vals, frozen_probs = law(jacobi([d, 1.]), np.array([1., 0., 0.]))
        frozen_bins = bin_law(frozen_vals, frozen_probs, edges, gamma)
        resummed = bin_law(np.array([-scale, scale]), np.array([.5, .5]), edges, gamma)
        resummed_bound = d*d + d**4/(np.pi*gamma)
        require(np.max(np.abs(exact_bins-resummed)) <= resummed_bound+TOL,
                "Dimer resummed approximation")
        dimer_rows.append({"d_over_J": d, "gamma_over_d2_J": c,
                           "memory_zero_pole_mass": d*d/(1+d*d),
                           "central_bin_error_dropped_memory_perturbation":
                               float(abs(exact_bins[1]-frozen_bins[1])),
                           "resummed_TV_bound": resummed_bound})
    limiting_error = (3*math.atan(5)-math.atan(15))/math.pi
    require(abs(dimer_rows[-1]["central_bin_error_dropped_memory_perturbation"]
                - limiting_error) < .0002, "Resolved asymptotic control")
    bad = [(1, 0, 2, 1, 1), (1, 1, 0, 1, 1), (1, 1, 2, -1, 1),
           (1, 1, 2, 1, -1), (float("nan"), 1, 2, 1, 1)]
    for args in bad:
        try:
            memory_certificate(*args)
        except ValueError:
            continue
        raise AssertionError("Invalid certificate inputs accepted")
    print(json.dumps({"status": "pass", "scope": "Finite complex128 identities and bin checks only; no established short-memory regime, quantum run, or speedup.",
                      "tolerance": TOL, "counts": counts, "certificate_controls": rows,
                      "dimer_controls": dimer_rows,
                      "limiting_bin_error": limiting_error,
                      "invalid_inputs_rejected": len(bad)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
