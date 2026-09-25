"""Two isospectral 2-state models with different population transfer.

Elementary rotating-frame control, not a model of cyclobutanone, a quantum
hardware run, an advantage benchmark, or a new theorem. All units have hbar=1.
Only NumPy is required. Output is written exclusively to a new file.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
LOW = np.array([0, 1], dtype=complex)


def exp_h(h: np.ndarray, dt: float) -> np.ndarray:
    """Exact exponential for a traceless two-state Hermitian Hamiltonian."""
    r = math.sqrt(max(0.0, float(np.trace(h @ h).real / 2)))
    if r == 0:
        return I.copy()
    return math.cos(r * dt) * I - 1j * math.sin(r * dt) * h / r


def run() -> dict:
    delta = 1.0
    omega = 4.0 / math.sqrt(5.0)
    duration = 2.0 * math.pi / omega
    rotating_frame = delta * Z - (omega / 2.0) * Y
    rotation_end = exp_h((omega / 2.0) * Y, duration)
    exact_u = rotation_end @ exp_h(rotating_frame, duration)
    exact_p = float(abs((exact_u @ LOW)[0])**2)
    stationary_p = float(abs((exp_h(delta * Z, duration) @ LOW)[0])**2)
    spectra_error = 0.0
    for theta in np.linspace(0, 2 * math.pi, 101):
        h = delta * (math.cos(theta) * Z + math.sin(theta) * X)
        spectra_error = max(spectra_error,
                            float(np.max(abs(np.linalg.eigvalsh(h) - [-delta, delta]))))
    controls = []
    for steps in (200, 800, 3200):
        dt = duration / steps
        state = LOW.copy()
        for j in range(steps):
            theta = omega * (j + 0.5) * dt
            h = delta * (math.cos(theta) * Z + math.sin(theta) * X)
            state = exp_h(h, dt) @ state
        p = float(abs(state[0])**2)
        controls.append(dict(steps=steps, transition_probability=p,
                             absolute_probability_error=abs(p - exact_p),
                             normalization_error=abs(float(np.vdot(state, state).real)-1)))
    # Both physical Hamiltonians agree at both endpoints. They are NOT merely
    # different representations of the same time-dependent physical generator.
    final_h = delta * (math.cos(omega*duration)*Z + math.sin(omega*duration)*X)
    endpoint_error = float(np.max(abs(final_h - delta * Z)))
    # A genuine change of basis of the stationary physical model preserves
    # its zero transfer, provided the frame-motion term is retained.
    psi_physical = exp_h(delta * Z, duration) @ LOW
    psi_frame = rotation_end.conj().T @ psi_physical
    gauge_return = float(np.max(abs(rotation_end @ psi_frame - psi_physical)))
    if abs(exact_p - 4/9) > 1e-12 or stationary_p > 1e-12:
        raise AssertionError('Analytic population transfer check failed.')
    if spectra_error > 1e-12 or endpoint_error > 1e-12 or gauge_return > 1e-12:
        raise AssertionError('Spectrum/endpoint/frame control failed.')
    if controls[-1]['absolute_probability_error'] > 1e-6:
        raise AssertionError('Independent midpoint propagation did not converge.')
    if not all(controls[i+1]['absolute_probability_error'] < controls[i]['absolute_probability_error']
               for i in range(len(controls)-1)):
        raise AssertionError('No convergence in specified midpoint sequence.')
    return dict(scope='Elementary isospectral two-state counterexample; no molecular or quantum advantage claim.',
                numpy_version=np.__version__, delta=delta, rotation_rate=omega,
                duration=duration, exact_transfer_stationary=stationary_p,
                exact_transfer_rotating=exact_p, expected_fraction='4/9',
                maximum_spectrum_error=spectra_error, endpoint_error=endpoint_error,
                gauge_return_error=gauge_return, midpoint_checks=controls)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result = run()
    # Exclusive creation ensures previous results cannot be silently overwritten.
    with args.output.open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, indent=2, sort_keys=True))
