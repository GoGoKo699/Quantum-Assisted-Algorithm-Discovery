"""Small classical check of a spectral record for weak probe-pulse responses.

This is a 4-spin algebra/sampling sanity check, NOT a quantum execution, a
classical-hardness benchmark, or an independently motivated material model.
Requires NumPy. Fixed-seed floating-point results may vary slightly by platform.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def pauli(n: int, labels: dict[int, np.ndarray]) -> np.ndarray:
    out = np.ones((1, 1), dtype=complex)
    for j in range(n):
        out = np.kron(out, labels.get(j, I))
    return out


def make_model() -> tuple[np.ndarray, np.ndarray]:
    n = 4
    h = np.zeros((2**n, 2**n), dtype=complex)
    for i, j, a in [(0, 1, .83), (1, 3, 1.07), (3, 2, .91), (2, 0, 1.13)]:
        h += a * pauli(n, {i: Z, j: Z})
    for i in range(n):
        h += (.61 + .09*i) * pauli(n, {i: X})
        h += (.17 - .04*i) * pauli(n, {i: Z})
        h += (.08 + .025*i) * pauli(n, {i: Y})  # H is not real.
    return h, pauli(n, {0: Z})


def bin_features(omega: np.ndarray, duration: float, bins: int) -> np.ndarray:
    dt = duration / bins
    centers = (np.arange(bins) + .5) * dt
    # Integral over each bin, divided by bin width. np.sinc(x)=sin(pi*x)/(pi*x).
    return np.exp(1j * omega[:, None] * centers) * np.sinc(omega[:, None] * dt/(2*np.pi))


def pulse_values(gram: np.ndarray, signs: np.ndarray) -> np.ndarray:
    alpha = signs / signs.shape[1]  # Integral of |u| is exactly one.
    return np.einsum('bi,ij,bj->b', alpha, gram, alpha, optimize=True).real


def probe_probability(h: np.ndarray, b: np.ndarray, pulse: np.ndarray,
                      duration: float, coupling: float) -> float:
    d = len(h)
    u = np.eye(2*d, dtype=complex)
    for sign in pulse:
        total_h = np.kron(I, h) + coupling * float(sign)/duration * np.kron(X, b)
        vals, vecs = np.linalg.eigh(total_h)
        step = (vecs*np.exp(-1j*vals*duration/len(pulse))) @ vecs.conj().T
        u = step @ u
    k10 = u[d:, :d]  # Probe begins in |0>; bath is I/d.
    return float(np.vdot(k10, k10).real / d)


def run() -> dict:
    h, b = make_model()
    d = len(h)
    e, v = np.linalg.eigh(h)
    be = v.conj().T @ b @ v
    omega = (e[:, None] - e[None, :]).ravel()
    weights = (np.abs(be)**2/d).ravel()
    weights /= weights.sum()
    # Explicit transpose-sensitive vectorization identity.
    liouvillian = np.kron(h, np.eye(d)) - np.kron(np.eye(d), h.T)
    vec_b = b.ravel()/np.sqrt(d)
    action_error = float(np.linalg.norm(liouvillian @ vec_b - ((h@b-b@h)/np.sqrt(d)).ravel()))
    correlations = []
    for t in (.0, .1, .6, 2.4):
        u = (v*np.exp(-1j*e*t)) @ v.conj().T
        trace_c = np.trace(u.conj().T@b@u@b)/d
        spectral_c = weights @ np.exp(1j*omega*t)
        correlations.append(float(abs(trace_c-spectral_c)))
    duration, bins = 8.0, 12
    signs = 1-2*((np.arange(2**bins)[:, None] >> np.arange(bins)) & 1)
    f = bin_features(omega, duration, bins)
    gram = f.conj().T @ (weights[:, None]*f)
    exact = pulse_values(gram, signs)
    best = int(exact.argmax())
    rng = np.random.default_rng(20260925)
    indices = rng.choice(len(weights), size=8192, p=weights)
    grid = np.linspace(-duration, duration, 4097)
    exponentials = np.exp(1j*omega[:, None]*grid)
    exact_c = weights @ exponentials
    records = []
    for m in (128, 1024, 8192):
        empirical = np.bincount(indices[:m], minlength=len(weights))/m
        estimate_gram = f.conj().T @ (empirical[:, None]*f)
        estimate = pulse_values(estimate_gram, signs)
        chosen = int(estimate.argmax())
        delta = float(np.max(np.abs(estimate_gram-gram)))
        pulse_error = float(np.max(np.abs(estimate-exact)))
        if pulse_error > delta + 1e-11:
            raise AssertionError('All-pulse entrywise bound failed.')
        if estimate.min() < -1e-11:
            raise AssertionError('The empirical quadratic response is not positive.')
        regret = float(exact[best]-exact[chosen])
        if regret > 2*delta + 1e-11:
            raise AssertionError('Selection bound failed.')
        records.append(dict(samples=m, gram_entrywise_bound=delta,
            tested_pulses=2**bins, worst_tested_pulse_error=pulse_error,
            correlation_error_on_grid=float(np.max(np.abs(empirical@exponentials-exact_c))),
            best_exact_response=float(exact[best]), selected_true_response=float(exact[chosen]),
            selection_regret=regret, chosen_signs=signs[chosen].tolist()))
    # Effects of finite spectral resolution, separated from Monte Carlo error.
    step=.002
    rounded=np.round(omega/step)*step
    error_round=float(np.max(np.abs(weights@np.exp(1j*rounded[:, None]*grid)-exact_c)))
    if error_round > step*duration/2 + 1e-11:
        raise AssertionError('Frequency perturbation bound failed.')
    weak=[]
    for pulse_id in sorted({0, best, int(rng.integers(len(signs)))}):
        for g in (.05, .1, .25):
            actual=probe_probability(h,b,signs[pulse_id],duration,g)
            second=g*g*float(exact[pulse_id])
            bound=float(np.sinh(g)**2-g*g)
            if abs(actual-second) > bound+1e-10:
                raise AssertionError('Dyson weak-probe bound failed.')
            weak.append(dict(pulse_id=pulse_id,coupling_area=g,
                full_probe_transition_probability=actual,quadratic_prediction=second,
                discrepancy=abs(actual-second),dyson_upper_bound=bound))
    if action_error>1e-11 or max(correlations)>1e-11:
        raise AssertionError('Spectral identity failed.')
    return dict(scope='Small classical floating-point sanity checks only; no quantum execution or advantage.',
        bath_spins=4, bath_dimension=d, duration=duration, pulse_bins=bins,
        numpy_version=np.__version__, seed=20260925, liouvillian_action_error=action_error,
        max_trace_spectral_identity_error=max(correlations),
        spectral_support_radius=float(np.max(np.abs(omega))),records=records,
        rounding=dict(frequency_step=step,grid_discrepancy=error_round,
                      all_time_upper_bound=step*duration/2),weak_probe_checks=weak)


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args=parser.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite an existing report.')
    report=run()
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps(report, indent=2))
