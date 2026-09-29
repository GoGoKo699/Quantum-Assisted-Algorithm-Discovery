#!/usr/bin/env python3
"""Sampling-regime arithmetic and instrument controls, not a speedup benchmark.

Python 3.10+, NumPy. No files, network, model training, or random trials.
The cache identity is checked with exact Fractions; Kraus controls use complex128.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import ceil, comb, exp, expm1, factorial, isfinite, log, sqrt
import json
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def bank_size(bins, epsilon, beta):
    if isinstance(bins, bool) or not isinstance(bins, int) or bins < 2:
        raise ValueError("At least two declared output bins are required.")
    if not all(isfinite(x) and 0 < x < 1 for x in (epsilon, beta)):
        raise ValueError("Require epsilon,beta in (0,1).")
    # E TV <= sqrt((B-1)/R)/2 and one-sided bounded differences.
    return ceil(((sqrt(bins - 1) + sqrt(2 * log(1 / beta))) / (2 * epsilon)) ** 2)


def reuse_variance(p, original_draws, replay_draws):
    if not 0 <= p <= 1 or original_draws < 1 or replay_draws < 1:
        raise ValueError("Invalid probability or positive sample counts.")
    r, m = original_draws, replay_draws
    return p * (1-p) * F(r + m - 1, r * m)


def exact_cache_control():
    p, r, m = F(1, 3), 4, 5
    second, mean = F(0), F(0)
    # Integrate over the binomially distributed empirical bank, then its replay.
    for a in range(r + 1):
        pa = comb(r, a) * p**a * (1-p)**(r-a)
        theta = F(a, r)
        for b in range(m + 1):
            probability = pa * comb(m, b) * theta**b * (1-theta)**(m-b)
            x = F(b, m)
            mean += probability*x
            second += probability*x*x
    variance = second-mean*mean
    require(mean == p and variance == reuse_variance(p, r, m), "Cache variance identity")
    return {"bank_draws": r, "replay_draws": m, "event_probability": str(p),
            "exact_mean": str(mean), "exact_replay_variance": str(variance),
            "fresh_draw_variance": str(p*(1-p)/m),
            "effective_independent_draws_for_this_mean": str(F(r*m,r+m-1))}


def spectral_budget():
    tau, beta, eps_stat, eps_num = 0.1, 0.01, 0.0125, 0.005
    rows = []
    for gamma, count in ((0.5, 128), (0.25, 256), (0.125, 512)):
        h = np.arange(1, count)
        a = np.exp(-gamma*tau*h) * (-np.expm1(-2*gamma*tau*(count-h))) / (-expm1(-2*gamma*tau*count))
        a2 = float(a @ a)
        sizes = []
        for k in (20, 26, 32):
            dimension = 1 << k
            probes = max(1, ceil(4*a2/(dimension*beta*eps_stat**2)))
            require(4*a2/(probes*dimension) <= beta*eps_stat**2*(1+1e-13), "Probe budget")
            w = k/2 + 3*(k-1)/4  # d=J=1, sufficient ||H|| bound.
            delta_u = eps_num/(6*k*sqrt(2*a2))
            q = 0
            while exp(w*tau)*(w*tau)**(q+1)/factorial(q+1) > delta_u/(2*count):
                q += 1
            sizes.append({"spins": k, "vector_entries": dimension, "probes": probes,
                          "sufficient_Taylor_degree": q,
                          "individual_vector_H_actions": 2*probes*(count-1)*q,
                          "term_entry_work_proxy": 2*probes*(count-1)*q*k*dimension,
                          "direct_quantum_normalization": 2*w})
        rows.append({"gamma_over_J": gamma, "tau_times_J": tau, "clock_length": count,
                     "clock_tail_bound": exp(-gamma*tau*count)/(1-exp(-gamma*tau*count)),
                     "full_time_times_J": (count-1)*tau,
                     "half_time_times_J": (count-1)*tau/2,
                     "A2": a2, "typicality_rows": sizes})
    return rows


def detector_control():
    p = 0.25
    a0 = np.diag([1., sqrt(1-p)]).astype(complex)
    a1 = np.array([[0., sqrt(p)], [0., 0.]], dtype=complex)
    local = [np.kron(a0,a0), np.kron(a0,a1), np.kron(a1,a0), np.kron(a1,a1)]
    mixed = [local[0], (local[1]+local[2])/sqrt(2), (local[1]-local[2])/sqrt(2), local[3]]
    channel = lambda ks: sum(np.kron(k.conj(),k) for k in ks)
    require(np.linalg.norm(channel(local)-channel(mixed)) < 2e-14, "Same unlabelled channel")
    for ks in (local, mixed):
        require(np.linalg.norm(sum(k.conj().T@k for k in ks)-np.eye(4)) < 2e-14, "Kraus completeness")
    psi = np.array([0,1,1,0], dtype=complex)/sqrt(2)
    probabilities = lambda ks: np.array([np.vdot(k@psi,k@psi).real for k in ks])
    pl, pm = probabilities(local), probabilities(mixed)
    tv = float(np.abs(pl-pm).sum()/2)
    require(abs(tv-p/2) < 2e-14, "Different detector records")
    require(abs(pl[1]+pl[2]-pm[1]-pm[2]) < 2e-14, "Coarsening can erase witness")
    return {"decay_probability": p, "local_detector_probabilities": pl.tolist(),
            "mixed_detector_probabilities": pm.tolist(), "labelled_record_TV": tv,
            "unlabelled_channel_Frobenius_difference": float(np.linalg.norm(channel(local)-channel(mixed))),
            "warning": "Exact finite amplitude-damping instrument control; no driven many-body trajectory or continuum-limit test."}


def main():
    control = exact_cache_control()
    bank = bank_size(10002, 0.02, 0.01)
    require((sqrt(10001)+sqrt(2*log(100)))/(2*sqrt(bank)) <= 0.02, "Histogram guarantee")
    bad = [lambda: bank_size(1,.1,.1), lambda: bank_size(2,0,.1),
           lambda: bank_size(2,.1,1), lambda: bank_size(2,float('nan'),.1),
           lambda: reuse_variance(F(2),2,2), lambda: reuse_variance(F(1,2),0,2)]
    for fn in bad:
        try:
            fn()
        except ValueError:
            continue
        raise AssertionError("Invalid argument accepted")
    print(json.dumps({"status":"pass", "scope":"Analytical budgets, exact cache variance, and finite detector control only; no physical performance data.",
          "cache_control":control,
          "cache_budget":{"bins":10002,"bank_error":0.02,"failure_probability":0.01,
                          "sufficient_independent_original_draws":bank,
                          "warning":"A worst-case sufficient budget, not a necessary size or free independent replay."},
          "large_replay_example":{"original_draws":10000,"replay_draws":1000000,
                                  "effective_draws_for_event_mean":float(F(10000*1000000,10000+1000000-1))},
          "spectral_resolution_budgets":spectral_budget(),
          "detector_instrument_control":detector_control(), "invalid_inputs_rejected":len(bad),
          "not_executed":"20/26/32-spin propagation, tensor contraction, quantum circuit, driven-dissipative simulation or timing."},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
