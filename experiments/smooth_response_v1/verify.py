#!/usr/bin/env python3
"""Finite checks of response-weighted spectral compression.

Python 3.10+ and NumPy, no network, no inputs and no file writes.
Not a QSVT phase compiler, NMR package, hardware test or performance benchmark.
Continuous-law statements are proved in SMOOTH_RESPONSE_COMPRESSION_20.md.
"""
from __future__ import annotations
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")

TOL = 3e-10
I = np.eye(2, dtype=complex)
PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def positive(value: float, name: str) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def local(matrix: np.ndarray, site: int, n: int) -> np.ndarray:
    result = np.ones((1, 1), dtype=complex)
    for j in range(n):
        result = np.kron(result, matrix if j == site else I)
    return result


def spin_law(n: int, coupling: float, offset: float):
    if n < 2 or n % 2:
        raise ValueError("The control requires an even chain.")
    sites = [[local(p / 2, j, n) for j in range(n)] for p in PAULI]
    sx, sy, sz = sites
    h = sum(((-1)**j * offset * sz[j] for j in range(n)),
            np.zeros((2**n, 2**n), dtype=complex))
    for j in range(n - 1):
        h += coupling * sum(ops[j] @ ops[j + 1] for ops in sites)
    o = sum((sx[j] + 1j * sy[j] for j in range(n)), np.zeros_like(h))
    e, u = np.linalg.eigh(h)
    amplitudes = u.conj().T @ o @ u
    frequencies = (e[:, None] - e[None, :]).ravel()
    weights = np.abs(amplitudes.ravel())**2 / (n * 2**(n - 1))
    comm = h @ o - o @ h
    require(abs(weights.sum() - 1) < TOL, "spectral normalization")
    require(abs(np.vdot(o, o).real - n * 2**(n - 1)) < TOL,
            "collective raising normalization")
    second = float(np.sum(weights * frequencies**2))
    require(abs(second - offset**2) < TOL, "response second moment")
    require(abs(np.vdot(comm, comm).real / np.vdot(o, o).real - second)
            < TOL, "commutator second moment")
    return frequencies, weights, second


def smooth_cap(values: np.ndarray, cutoff: float) -> np.ndarray:
    """C2 scalar control: identity in the core, plateau at +/-1.5*cutoff.

    This is not the QSVT polynomial from the cited existence theorem.
    On 1<=u<=2 use 1+t-t^3+t^4/2, t=u-1.
    """
    positive(cutoff, "cutoff")
    values = np.asarray(values, dtype=float)
    u = np.abs(values) / cutoff
    t = np.clip(u - 1, 0, 1)
    middle = 1 + t - t**3 + t**4 / 2
    mapped = np.where(u <= 1, u, np.where(u >= 2, 1.5, middle))
    return np.sign(values) * cutoff * mapped


def bin_law(frequencies, weights, gamma: float, edges):
    positive(gamma, "linewidth")
    edges = np.asarray(edges, dtype=float)
    if (len(edges) < 2 or edges[0] != -np.inf or edges[-1] != np.inf
            or not np.all(np.diff(edges) > 0)):
        raise ValueError("Use increasing bins with both infinite endpoints.")
    frequencies = np.asarray(frequencies, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if (frequencies.shape != weights.shape or not np.all(np.isfinite(frequencies))
            or not np.all(np.isfinite(weights)) or np.any(weights < 0)
            or abs(weights.sum() - 1) > TOL):
        raise ValueError("Invalid finite probability law.")
    cdf = (np.arctan((edges[:, None] - frequencies[None, :]) / gamma)
           / math.pi + 0.5)
    probabilities = np.diff(cdf @ weights)
    require(abs(probabilities.sum() - 1) < TOL and probabilities.min() > -TOL,
            "binned probability law")
    return probabilities


def tv(p, q):
    return float(np.sum(np.abs(p - q)) / 2)


def main() -> None:
    counts = {"spin_models": 0, "moment_identities": 0,
              "smooth_cap_comparisons": 0, "bounded_polynomial_comparisons": 0,
              "translation_checks": 0, "edge_continuity_checks": 0,
              "invalid_inputs_rejected": 0}
    rows = []
    edges = np.r_[-np.inf, np.linspace(-2, 2, 801), np.inf]
    for n, j, d, gamma, cutoff in [
            (2, 1., .15, .008, .5),
            (4, 1., .10, .006, .4),
            (6, 1., .12, .010, .5)]:
        lam, w, second = spin_law(n, j, d)
        counts["spin_models"] += 1
        counts["moment_identities"] += 2
        original = bin_law(lam, w, gamma, edges)
        tail = float(w[np.abs(lam) > cutoff].sum())
        require(tail <= second / cutoff**2 + TOL, "moment tail bound")
        for relative_error in (0., .007):
            mapped = (1 - relative_error) * smooth_cap(lam, cutoff)
            inside = np.abs(lam) <= cutoff
            require(np.max(np.abs(mapped[inside] - lam[inside]))
                    <= relative_error * cutoff + TOL, "core identity")
            require(np.max(np.abs(mapped)) <= 1.5 * cutoff + TOL,
                    "bounded spectral range")
            # Eigenvectors and their probabilities are unchanged; only line positions move.
            output = bin_law(mapped, w, gamma, edges)
            discrepancy = tv(original, output)
            coupling_bound = tail + relative_error * cutoff / (math.pi * gamma)
            moment_bound = d**2 / cutoff**2 + relative_error * cutoff / (math.pi * gamma)
            require(discrepancy <= min(1., coupling_bound) + TOL,
                    "tail-plus-core bound")
            require(coupling_bound <= moment_bound + TOL, "moment relaxation")
            rows.append({"n": n, "d": d, "gamma": gamma, "cutoff": cutoff,
                         "core_relative_error": relative_error,
                         "response_tail_mass": tail,
                         "binned_TV_diagnostic": discrepancy,
                         "analytic_moment_bound": min(1., moment_bound)})
            counts["smooth_cap_comparisons"] += 1

        # A genuinely bounded odd polynomial: P(x)=(3x-x^3)/2, |P|<=1 on [-1,1].
        # For r=1/3, relative core error <=1/27. This is only a small analytic control.
        alpha = n * abs(d) + 1.5 * abs(j) * (n - 1)
        k = alpha / 3
        x = lam / alpha
        require(np.max(np.abs(x)) <= 1 + TOL, "base norm bound")
        p = (3*x - x**3) / 2
        mapped = 2*k*p
        inside = np.abs(lam) <= k
        require(np.max(np.abs(mapped[inside] - lam[inside]))
                <= k/27 + TOL, "polynomial core error")
        bound = float(w[~inside].sum()) + k / (27*math.pi*gamma)
        require(tv(original, bin_law(mapped, w, gamma, edges))
                <= min(1., bound) + TOL, "bounded polynomial law")
        counts["bounded_polynomial_comparisons"] += 1

    # The scalar map is continuous at the arbitrary core boundary.
    for k in (.2, .5):
        for edge in (-2*k, -k, k, 2*k):
            delta = 1e-8*k
            a, b = smooth_cap(np.array([edge-delta, edge+delta]), k)
            require(abs(b-a) <= 2.1*delta, "no cutoff jump")
            counts["edge_continuity_checks"] += 1

    for shift, gamma in [(0., .1), (.01, .1), (1., .1), (-2., .4)]:
        exact_tv = 2/math.pi * math.atan(abs(shift)/(2*gamma))
        require(exact_tv <= min(1., abs(shift)/(math.pi*gamma)) + TOL,
                "Lorentzian translation bound")
        counts["translation_checks"] += 1

    # Negative control: applying f(L) to the STATE reweights it by |f|^2.
    lam = np.array([0., -1., 1.])
    w = np.array([.98, .01, .01])
    mapped = smooth_cap(lam, .5)
    correct = bin_law(mapped, w, .03, edges)
    wrong_weights = w * mapped**2
    wrong_weights /= wrong_weights.sum()
    wrong = bin_law(mapped, wrong_weights, .03, edges)
    negative = tv(correct, wrong)
    require(negative > .8, "state-filtering negative control not detected")

    for operation in [
        lambda: smooth_cap(np.array([0.]), 0.),
        lambda: smooth_cap(np.array([0.]), float("nan")),
        lambda: bin_law(lam, w, -1., edges),
        lambda: bin_law(lam, w, .1, [-1., 0., 1.]),
        lambda: bin_law(lam, [1., 1., 1.], .1, edges),
        lambda: spin_law(3, 1., .1),
    ]:
        try:
            operation()
        except ValueError:
            counts["invalid_inputs_rejected"] += 1
        else:
            raise AssertionError("Invalid input accepted.")

    print(json.dumps({
        "status": "pass", "scope": "Fixed small-matrix probability-law controls only; "
        "no general QSVT polynomial construction, circuit, experiment or timing.",
        "tolerance": TOL, "numpy_version": np.__version__, "counts": counts,
        "rows": rows, "wrong_state_filtering_TV": negative,
        "implementation_limit": "The C2 cap is an analytic control, not the "
        "logarithmic-accuracy amplification polynomial. Its existence/cost is cited.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
