#!/usr/bin/env python3
"""Output-level spectral controls, not a tensor-network or quantum benchmark.

Python 3.10+, NumPy. Exact rational witnesses and separate complex128 controls.
No network, inputs, or file writes. See RESPONSE_READOUT_22.md for the proofs.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def spin_data(n: int, kind: str):
    """Integer 4H and collective raising O, d=J=1, open even chain."""
    if n < 2 or n % 2 or kind not in {"full", "free", "secular"}:
        raise ValueError("Require an even n>=2 and a declared model.")
    size = 1 << n
    h = [dict() for _ in range(size)]
    for x in range(size):
        z = [1 - 2 * ((x >> i) & 1) for i in range(n)]
        diagonal = sum(2 * (-1)**i * z[i] for i in range(n))
        if kind != "free":
            diagonal += sum(z[i] * z[i+1] for i in range(n-1))
        h[x][x] = diagonal
        if kind == "full":
            for i in range(n-1):
                if z[i] != z[i+1]:
                    h[x][x ^ (3 << i)] = 2
    o = {(x ^ (1 << i), x): 1 for x in range(size)
         for i in range(n) if x & (1 << i)}
    return h, o


def commutator(h, u):
    """Exact integer [4H,u], using the symmetry of real h."""
    out = {}
    for (a, b), v in u.items():
        for c, x in h[a].items():
            out[c, b] = out.get((c, b), 0) + x*v
        for c, x in h[b].items():
            out[a, c] = out.get((a, c), 0) - x*v
    return {key: value for key, value in out.items() if value}


def even_moments(n: int, kind: str, order: int):
    h, o = spin_data(n, kind)
    norm = sum(v*v for v in o.values())
    u = o
    moments = [F(1)]
    for j in range(1, order+1):
        u = commutator(h, u)
        moments.append(F(sum(v*v for v in u.values()), norm * 16**j))
    return moments


def cosine_interval(moments, t: F):
    """Re C(t) with a spectral-moment Taylor remainder; all arithmetic exact."""
    order = len(moments)-1
    center = sum((-1)**j * moments[j] * t**(2*j) / math.factorial(2*j)
                 for j in range(order))
    error = moments[order] * t**(2*order) / math.factorial(2*order)
    return center-error, center+error


def exp_lower(x: F):
    if x < 0:
        raise ValueError("Require x>=0.")
    # Odd Taylor degree: the Lagrange remainder of exp(-x) is positive.
    return sum((-x)**j / math.factorial(j) for j in range(42))


def floor_fraction(x: F, digits: int = 12):
    scale = 10**digits
    return F(x.numerator * scale // x.denominator, scale)


def outward_interval(pair, digits: int = 12):
    lo, hi = pair
    return [str(floor_fraction(lo, digits)), str(-floor_fraction(-hi, digits))]


def spectral_data(n: int, kind: str):
    hs, os = spin_data(n, kind)
    size = len(hs)
    h = np.zeros((size, size))
    o = np.zeros((size, size))
    for a, row in enumerate(hs):
        for b, value in row.items():
            h[a, b] = value / 4
    for (a, b), value in os.items():
        o[a, b] = value
    eigenvalues, vectors = np.linalg.eigh(h)
    ov = vectors.T @ o @ vectors
    ov = ov / np.linalg.norm(ov)
    gaps = eigenvalues[:, None]-eigenvalues[None, :]
    weights = np.abs(ov)**2
    return gaps.ravel(), weights.ravel(), ov, gaps


def clock_weights(gamma: float, tau: float, count: int):
    if not math.isfinite(gamma) or gamma <= 0 or tau <= 0 or count < 2:
        raise ValueError("Invalid clock parameters.")
    r = math.exp(-gamma*tau)
    c = r**np.arange(count, dtype=float)
    c /= np.linalg.norm(c)
    lag = np.arange(1, count)
    a = r**lag * (-np.expm1(-2*gamma*tau*(count-lag))) / (-math.expm1(-2*gamma*tau*count))
    require(np.max(np.abs(a - np.array([c[:-k] @ c[k:] for k in lag]))) < 3e-13,
            "Clock autocorrelation weights")
    return c, a


def bin_masses(correlations, lag_weights, edges):
    """Integrate the finite Fourier polynomial, not midpoint quadrature."""
    k = np.arange(1, len(correlations)+1)
    differences = np.exp(1j*np.outer(edges[1:], k))-np.exp(1j*np.outer(edges[:-1], k))
    return np.diff(edges)/(2*math.pi) + np.real(differences @ (lag_weights*correlations/(1j*math.pi*k)))


def repair_bins(raw):
    if not np.isfinite(raw).all() or abs(float(np.sum(raw))-1) > 1e-10:
        raise ValueError("Expected finite, real masses summing to one.")
    positive = np.maximum(raw, 0)
    total = float(np.sum(positive))
    if total <= 0:
        raise ValueError("No positive mass.")
    return positive/total


def main():
    # One fixed nontrivial block, not a size sweep or experimental requirement.
    n, time, gamma = 6, F(2), F(1, 4)
    moments = {kind: even_moments(n, kind, 40) for kind in ("full", "free", "secular")}
    intervals = {kind: cosine_interval(m, time) for kind, m in moments.items()}
    for lo, hi in intervals.values():
        require(hi-lo < F(1, 10**20), "Taylor enclosure too wide")
    require(moments["full"][1] == 1, "Exact second moment")
    require(moments["full"][2] == F(8, 3), "Exact fourth moment")
    witnesses = {}
    omega, binwidth = F(50), F(1, 100)
    support = {"full": F(27, 2), "free": F(6), "secular": F(17, 2)}
    for kind in ("free", "secular"):
        gap = max(F(0), intervals["full"][0]-intervals[kind][1], intervals[kind][0]-intervals["full"][1])
        lower = exp_lower(gamma*time) * gap / 2
        # pi>3 and arctan(x)<=x give valid Cauchy tail upper bounds.
        tails = sum(2*gamma/(3*(omega-support[k])) for k in ("full", kind))
        binned_lower = lower-time*binwidth/2-tails
        require(lower > F(3, 40) and binned_lower > F(1, 20), "Resolved surrogate witness")
        witnesses[kind] = {"continuous_TV_lower": str(floor_fraction(lower)),
                           "declared_bin_TV_lower": str(floor_fraction(binned_lower)),
                           "correlation_interval": outward_interval(intervals[kind])}
    # Separate numerical identities on this same block.
    frequencies, probabilities, operator, gapmatrix = spectral_data(n, "full")
    require(abs(probabilities.sum()-1) < 2e-12, "Positive normalized spectral weights")
    cf = lambda t: np.sum(probabilities*np.exp(-1j*frequencies*t))
    lo, hi = intervals["full"]
    require(abs(cf(float(time)).real - float((lo+hi)/2)) < 3e-12, "Independent moment/spectral check")
    half_checks = 0
    for t in (0.0, 0.5, 2.0, 7.0):
        left = operator*np.exp(1j*gapmatrix*t/2)
        right = operator*np.exp(-1j*gapmatrix*t/2)
        require(abs(np.vdot(left, right)-cf(t)) < 2e-12, "Half-time overlap")
        half_checks += 1
    rows = []
    for linewidth in (0.25, 0.5):
        tau, count = 0.1, 256
        c, a = clock_weights(linewidth, tau, count)
        times = tau*np.arange(1, count)
        corr = np.array([cf(t) for t in times])
        edges = np.linspace(-math.pi, math.pi, 129)
        exact = bin_masses(corr, a, edges)
        require(exact.min() > -2e-12 and abs(exact.sum()-1) < 2e-12, "Finite clock bins")
        errors = 0.002*np.exp(1j*np.arange(1, count)*0.37)
        raw = bin_masses(corr+errors, a, edges)
        repaired = repair_bins(raw)
        readout_bound = math.sqrt(2*np.sum(a*a*np.abs(errors)**2))
        bintv = np.sum(np.abs(repaired-exact))/2
        require(bintv <= readout_bound+2e-12, "Output reconstruction error bound")
        # Independently evaluate the positive clock-mixture density at fixed phases.
        phases = np.array([-2.1, -0.7, 0, 0.9, 2.4])
        j = np.arange(count)
        for phase in phases:
            direct = np.sum(probabilities*np.abs(np.exp(1j*np.outer(phase-frequencies*tau, j)) @ c)**2)/(2*math.pi)
            fourier = (1+2*np.real(np.sum(a*corr*np.exp(1j*np.arange(1, count)*phase))))/(2*math.pi)
            require(abs(direct-fourier) < 3e-12, "Positive kernel/Fourier identity")
        trunc = math.exp(-linewidth*count*tau)/(1-math.exp(-linewidth*count*tau))
        omega_f = math.pi/tau
        wrap = 4/omega_f**2+2/math.pi*math.atan(2*linewidth/omega_f)
        rows.append({"gamma": linewidth, "N": count, "tau": tau,
                     "lag_count": count-1, "max_half_time": (count-1)*tau/2,
                     "per_lag_absolute_error": 0.002,
                     "finite_clock_bin_TV_diagnostic": float(bintv),
                     "readout_TV_bound": float(readout_bound),
                     "clock_tail_bound": trunc, "moment_wrap_bound": wrap,
                     "complete_per_draw_bound_before_arithmetic": float(readout_bound+trunc+wrap),
                     "caveat": "Perturbations test the conditional certificate; no tensor algorithm acquired them."})
    # A deliberately nonphysical estimated correlation can make raw bins negative.
    edges = np.linspace(-math.pi, math.pi, 65)
    _, a = clock_weights(0.25, 0.1, 8)
    raw = bin_masses(np.array([3.0]+[0.0]*6), a, edges)
    require(raw.min() < -0.01, "Missing negative-probability control")
    repaired = repair_bins(raw)
    uniform = np.diff(edges)/(2*math.pi)
    require(np.all(repaired >= 0) and abs(repaired.sum()-1) < 1e-12, "Positivity repair")
    require(np.sum(abs(repaired-uniform))/2 <= np.sum(abs(raw-uniform)), "Repair contraction bound")
    # Exactly normalized signed-bin controls, independent of floating arithmetic.
    repair_exact = 0
    target = [F(1,4), F(1,2), F(1,4)]
    for rawq in ([F(-1,10), F(6,10), F(5,10)], [F(2), F(-1), F(0)]):
        positive = [max(F(0), q) for q in rawq]
        total = sum(positive)
        normalized = [q/total for q in positive]
        require(sum(abs(p-q) for p,q in zip(target,normalized))/2 <=
                sum(abs(p-q) for p,q in zip(target,rawq)), "Exact repair inequality")
        repair_exact += 1
    invalid = [lambda: spin_data(3,"full"), lambda: spin_data(2,"bad"),
               lambda: clock_weights(0,0.1,8), lambda: clock_weights(1,-1,8),
               lambda: clock_weights(1,1,1), lambda: repair_bins(np.array([0.2,0.3]))]
    for action in invalid:
        try:
            action()
        except ValueError:
            continue
        raise AssertionError("Invalid input accepted")
    print(json.dumps({"status": "pass", "scope": "One six-spin exact-rational witness and separate complex128 readout identities; no tensor, quantum, experimental, or performance run.",
                      "n": n, "d": 1, "J": 1, "witness_time": str(time), "witness_gamma": str(gamma),
                      "cosine_taylor_degree": 78, "remainder_moment_order": 80,
                      "full_correlation_interval": outward_interval(intervals['full']),
                      "bin_contract": {"interior_range": [-50,50], "uniform_width": "1/100", "interior_bins": 10000, "overflow_bins": 2},
                      "witnesses": witnesses, "half_time_checks": half_checks, "exact_repair_checks": repair_exact,
                      "negative_raw_bin_detected": True, "invalid_inputs_rejected": len(invalid), "readout_controls": rows}, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
