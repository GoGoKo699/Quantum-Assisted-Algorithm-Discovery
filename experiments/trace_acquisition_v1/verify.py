#!/usr/bin/env python3
"""Trace-to-spectrum acquisition controls; not a quantum or application benchmark.

Python 3.10+, NumPy. One fixed ten-spin sparse pure-state calculation, exact
finite-probe enumeration on a two-spin identity control, and analytic budgets.
No network, inputs, file writes, or upstream implementation. The general error
and cost statements are proved in TRACE_ACQUISITION_23.md, not inferred here.
"""
from __future__ import annotations
from itertools import product
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


class SpinActions:
    """Matrix-free open isotropic chain and collective raising operator."""
    def __init__(self, k: int, d: float = 1.0, j: float = 1.0):
        if not isinstance(k, int) or k < 1 or not all(map(math.isfinite, (d, j))):
            raise ValueError("Require positive integer k and finite coefficients.")
        self.k, self.dim = k, 1 << k
        states = np.arange(self.dim, dtype=np.int64)
        spins = np.array([1 - 2*((states >> i) & 1) for i in range(k)])
        self.diagonal = 0.5*d*np.sum(((-1.0)**np.arange(k))[:, None]*spins, axis=0)
        self.diagonal += 0.25*j*np.sum(spins[:-1]*spins[1:], axis=0)
        self.exchange = []
        for i in range(k-1):
            source = states[spins[i] != spins[i+1]]
            self.exchange.append((source, source ^ (3 << i), 0.5*j))
        self.raising = []
        for i in range(k):
            source = states[((states >> i) & 1) != 0]
            self.raising.append((source, source ^ (1 << i)))
        self.norm_bound = 0.5*k*abs(d) + 0.75*(k-1)*abs(j)

    def h(self, x: np.ndarray) -> np.ndarray:
        out = self.diagonal[:, None]*x if x.ndim == 2 else self.diagonal*x
        for src, dst, value in self.exchange:
            out[dst] += value*x[src]
        return out

    def o(self, x: np.ndarray) -> np.ndarray:
        out = np.zeros_like(x)
        for src, dst in self.raising:
            out[dst] += x[src]
        return out

    def dense(self) -> tuple[np.ndarray, np.ndarray]:
        # Used only by independent diagnostics, never by the probe producer.
        eye = np.eye(self.dim, dtype=np.complex128)
        return self.h(eye), self.o(eye)


def clock(gamma: float, tau: float, nclock: int) -> np.ndarray:
    if not math.isfinite(gamma) or gamma <= 0 or not math.isfinite(tau) or tau <= 0 or nclock < 2:
        raise ValueError("Invalid clock.")
    h = np.arange(1, nclock)
    return np.exp(-gamma*tau*h)*(-np.expm1(-2*gamma*tau*(nclock-h)))/(-math.expm1(-2*gamma*tau*nclock))


def probe_budget(k: int, a2: float, failure: float, error: float) -> int:
    if k < 1 or a2 < 0 or not math.isfinite(a2) or not 0 < failure < 1 or not error > 0:
        raise ValueError("Invalid acquisition budget.")
    return max(1, math.ceil(4*a2/((1 << k)*failure*error**2)))


def taylor_degree(a: float, tolerance: float) -> tuple[int, float]:
    """Sufficient exponential-series operator remainder, not roundoff control."""
    if not math.isfinite(a) or a < 0 or not 0 < tolerance < 1:
        raise ValueError("Invalid exponential tolerance.")
    if a == 0:
        return 0, 0.0
    q = 0
    while True:
        logbound = a+(q+1)*math.log(a)-math.lgamma(q+2)
        if logbound <= math.log(tolerance):
            return q, math.exp(logbound)
        q += 1


def step(actions: SpinActions, x: np.ndarray, tau: float, q: int) -> np.ndarray:
    term, out = x.copy(), x.copy()
    for degree in range(1, q+1):
        term = (-1j*tau/degree)*actions.h(term)
        out += term
    return out


def acquire(actions: SpinActions, tau: float, nclock: int, probes: int, seed: int,
            vector_tolerance: float = 1e-10):
    """Two ordinary Hilbert-space vectors per probe; no doubled operator state."""
    if probes < 1 or not 0 < vector_tolerance < 1:
        raise ValueError("Invalid probe count or vector tolerance.")
    rng = np.random.Generator(np.random.PCG64(seed))
    phases = (1j)**rng.integers(0, 4, size=(actions.dim, probes))
    r = phases/math.sqrt(actions.dim)
    require(np.max(np.abs(np.sum(abs(r)**2, axis=0)-1)) < 2e-14, "Probe normalization")
    current = np.concatenate((r, actions.o(r)), axis=1)
    q, remainder = taylor_degree(actions.norm_bound*tau, vector_tolerance/(2*nclock))
    values = []
    for _ in range(1, nclock):
        current = step(actions, current, tau, q)
        psi, phi = current[:, :probes], current[:, probes:]
        values.append((2/actions.k)*np.mean(np.sum(actions.o(psi).conj()*phi, axis=0)))
    accumulated = (nclock-1)*remainder*math.exp((nclock-1)*remainder)
    return np.array(values), r, current, q, accumulated


def reference(actions: SpinActions, times: np.ndarray):
    """Small-control reference via magnetization blocks; not the acquisition route."""
    h, o = actions.dense()
    labels = np.array([i.bit_count() for i in range(actions.dim)])
    groups, evals, evecs = [], [], []
    for charge in range(actions.k+1):
        indices = np.flatnonzero(labels == charge)
        vals, vecs = np.linalg.eigh(h[np.ix_(indices, indices)])
        groups.append(indices)
        evals.append(vals)
        evecs.append(vecs)
    result = np.zeros(len(times), dtype=np.complex128)
    norm, second = 0.0, 0.0
    for charge in range(1, actions.k+1):
        transformed = evecs[charge-1].conj().T @ o[np.ix_(groups[charge-1], groups[charge])] @ evecs[charge]
        masses = (abs(transformed)**2).ravel()/(actions.dim*actions.k/2)
        frequencies = (evals[charge-1][:, None]-evals[charge][None, :]).ravel()
        norm += float(np.sum(masses))
        second += float(masses @ (frequencies**2))
        result += np.exp(-1j*np.outer(times, frequencies)) @ masses
    return result, norm, second, (groups, evals, evecs)


def masses(corr: np.ndarray, a: np.ndarray, edges: np.ndarray):
    h = np.arange(1, len(a)+1)
    factor = np.exp(1j*np.outer(edges[1:], h))-np.exp(1j*np.outer(edges[:-1], h))
    raw = np.diff(edges)/(2*math.pi)+np.real(factor @ (a*corr/(1j*math.pi*h)))
    require(abs(np.sum(raw)-1) < 3e-12, "Bin normalization including fixed C(0)=1")
    pos = np.maximum(raw, 0)
    return raw, pos/np.sum(pos)


def probe_identity_control():
    """Enumerate all 4^3 distinct Z4 probes of a D=4 control, up to global phase."""
    actions = SpinActions(2)
    h, o = actions.dense()
    vals, vecs = np.linalg.eigh(h)
    phases = np.array([[1]+list(z) for z in product((1, 1j, -1, -1j), repeat=3)], dtype=complex).T/2
    rows = []
    for time in (0.0, 0.7, 2.0):
        u = (vecs*np.exp(-1j*time*vals)) @ vecs.conj().T
        b = (2/actions.k)*u.conj().T @ o.conj().T @ u @ o
        c = np.trace(b)/actions.dim
        samples = np.sum(phases.conj()*(b @ phases), axis=0)
        variance = np.mean(abs(samples-c)**2)
        formula = (np.sum(abs(b)**2)-np.sum(abs(np.diag(b))**2))/actions.dim**2
        require(abs(np.mean(samples)-c) < 2e-13, "Unbiased phase-trace identity")
        require(abs(variance-formula) < 2e-13, "Exact-enumeration phase variance identity")
        require(formula <= 2/actions.dim+2e-13, "Time-uniform collective variance bound")
        # Same vectors generate different-time estimates; independence across times is false.
        rows.append({"time": time, "enumerated_variance": float(variance), "formula_variance": float(formula)})
    return rows


def product_probe_negative_control():
    k = 4
    actions = SpinActions(k)
    values = []
    for phases in product((1, 1j, -1, -1j), repeat=k):
        # Independent on-site phases are NOT independent phases for all 2^k basis states.
        values.append(0.5+abs(sum(phases))**2/(2*k))
    variance = float(np.mean((np.array(values)-1)**2))
    require(abs(variance-(k-1)/(4*k)) < 1e-14, "Product-phase variance")
    require(variance > 2/actions.dim, "Detect invalid transfer of global-phase variance bound")
    return {"k": k, "product_probe_variance_at_zero": variance,
            "invalid_global_phase_upper_bound": 2/actions.dim,
            "meaning": "An ensemble identity control, not an output error: C(0) is set to one exactly."}


def main():
    controls = probe_identity_control()
    product_control = product_probe_negative_control()
    k, nclock, tau, gamma, rcount, seed = 10, 256, 0.1, 0.25, 8, 230929
    actions = SpinActions(k)
    a = clock(gamma, tau, nclock)
    a2 = float(a @ a)
    acquired, initial, final, degree, evolution_bound = acquire(actions, tau, nclock, rcount, seed)
    times = tau*np.arange(1, nclock)
    exact, norm, m2, sectors = reference(actions, times)
    require(abs(norm-1) < 3e-12 and abs(m2-1) < 5e-12, "Independent response normalization and moment")
    h, o = actions.dense()
    oo = o.conj().T @ o
    require(abs(np.trace(oo).real-actions.dim*k/2) < 1e-10, "Second observable moment")
    require(abs(np.trace(oo @ oo).real-actions.dim*k*k/2) < 1e-9, "Fourth observable moment")
    # Validate this producer's full-time vectors independently at the final time.
    groups, vals, vecs = sectors
    exact_final = np.empty_like(final)
    beginning = np.concatenate((initial, actions.o(initial)), axis=1)
    for indices, v, u in zip(groups, vals, vecs):
        exact_final[indices] = u @ (np.exp(-1j*times[-1]*v)[:, None]*(u.conj().T @ beginning[indices]))
    final_relative = float(np.linalg.norm(final-exact_final)/np.linalg.norm(beginning))
    require(final_relative < max(1e-11, 2*evolution_bound), "Sparse propagation versus independent diagonal reference")
    frequency_edges = np.r_[-np.inf, np.linspace(-50, 50, 10001), np.inf]
    edges = np.clip(tau*frequency_edges, -math.pi, math.pi)
    exact_raw, exact_bins = masses(exact, a, edges)
    require(exact_raw.min() >= -3e-12, "Exact finite-clock positivity")
    raw, estimated_bins = masses(acquired, a, edges)
    weighted = float(np.sqrt(2*np.sum(a*a*abs(acquired-exact)**2)))
    bin_tv = float(np.sum(abs(estimated_bins-exact_bins))/2)
    require(bin_tv <= weighted+3e-12, "Actual output error bounded by weighted scalar acquisition error")
    budgets = [{"block_spins": size, "ordinary_Hilbert_dimension": 1 << size,
                "probes_sufficient_for_readout_0.0125_failure_0.01": probe_budget(size, a2, 0.01, 0.0125)}
               for size in (12, 20, 26)]
    # This is an analytical target, NOT a completed large-block computation.
    ell = 10
    linked_cluster_noise = 2*(ell**2/(1 << (2*ell)) + (ell-1)**2/(1 << (2*(ell-1))))
    require(linked_cluster_noise > 2/(1 << (2*ell)), "Signed boundary cancellation does not have the convex-mixture variance bound")
    invalid = [lambda: SpinActions(0), lambda: SpinActions(2, float("nan")),
               lambda: clock(0, 0.1, 8), lambda: probe_budget(2, 1, 0, 0.1),
               lambda: taylor_degree(-1, 0.01), lambda: acquire(actions, tau, 4, 0, seed)]
    for case in invalid:
        try:
            case()
        except ValueError:
            continue
        raise AssertionError("Invalid input accepted")
    window = math.pi/tau
    clock_bound = math.exp(-gamma*nclock*tau)/(1-math.exp(-gamma*nclock*tau))
    wrap_bound = 4/window**2+2/math.pi*math.atan(2*gamma/window)
    report = {
        "status": "pass",
        "scope": "One ten-spin independent matrix-free pure-state acquisition and small identity controls; no quantum circuit, large-block feasibility, upstream solver, or performance claim.",
        "phase_probe_variance_controls": controls,
        "product_state_negative_control": product_control,
        "sparse_acquisition": {
            "k": k, "d": 1, "J": 1, "dimension": actions.dim,
            "probes": rcount, "rng": "NumPy PCG64", "seed": seed,
            "time_lags": nclock-1, "tau": tau, "max_time": float(times[-1]),
            "output_bins": {"interior_range": [-50, 50], "interior_width": 0.01, "overflow_bins": 2},
            "Taylor_step_degree": degree,
            "matrix_action_calls_on_batch": degree*(nclock-1),
            "simultaneous_vectors_in_control": 2*rcount,
            "ideal_arithmetic_accumulated_operator_error_bound": evolution_bound,
            "relative_vector_error_vs_diagonal_reference": final_relative,
            "max_observed_scalar_error": float(np.max(abs(acquired-exact))),
            "observed_weighted_scalar_error": weighted,
            "observed_finite_clock_bin_TV": bin_tv,
            "negative_raw_bin_mass": float(max(0.0, -np.minimum(raw, 0).sum())),
            "variance_based_expected_readout_error_upper_bound": 2*math.sqrt(a2/(rcount*actions.dim)),
            "warning": "Observed errors are one fixed-seed check, not independent empirical confidence intervals or a full-spectrum performance comparison."
        },
        "analytical_readout_budget": {
            "clock_weight_square_sum": a2, "gamma": gamma, "tau": tau, "N": nclock,
            "target_statistical_readout_error": 0.0125, "failure_probability": 0.01,
            "clock_bound": clock_bound, "wrap_bound": wrap_bound,
            "total_before_deterministic_arithmetic": clock_bound+wrap_bound+0.0125,
            "size_rows": budgets,
            "warning": "None of the size rows is an executed simulation. Each random vector has 2^k entries and must be propagated to the linewidth time."
        },
        "signed_cluster_noise_control": {
            "unit_cells": ell, "independent_two_cluster_one_probe_variance_upper_bound": linked_cluster_noise,
            "scope": "Propagation of probe variance only; no linked-cluster convergence result is asserted."
        },
        "invalid_inputs_rejected": len(invalid),
        "arithmetic": "NumPy complex128; algebraic formulas and operator-error proof are in the note; floating runs are not interval certificates."
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
