"""Small exact checks of conditional sampling by inverse unitary evolution.

NumPy-only classical matrix calculations. No quantum execution, useful
advantage, physical application validation, or new theorem is claimed.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np


def embed(gate: np.ndarray, i: int, j: int, n: int) -> np.ndarray:
    dim = 1 << n
    out = np.zeros((dim, dim), dtype=complex)
    mask = (1 << i) | (1 << j)
    for x in range(dim):
        col = 2 * ((x >> i) & 1) + ((x >> j) & 1)
        base = x & ~mask
        for row in range(4):
            y = base | ((row >> 1) << i) | ((row & 1) << j)
            out[y, x] = gate[row, col]
    return out


def conserving_circuit(n: int, layers: int, seed: int):
    rng = np.random.default_rng(seed)
    u = np.eye(1 << n, dtype=complex)
    dephased = np.eye(1 << n)
    gates = 0
    for layer in range(layers):
        for i in range(layer % 2, n - 1, 2):
            a = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
            h = (a + a.conj().T) / 2
            e, v = np.linalg.eigh(h)
            block = (v * np.exp(-1j * e)) @ v.conj().T
            g = np.zeros((4, 4), dtype=complex)
            g[0, 0], g[3, 3] = np.exp(1j * rng.uniform(-np.pi, np.pi, 2))
            g[1:3, 1:3] = block
            full = embed(g, i, i + 1, n)
            u = full @ u
            dephased = (abs(full) ** 2) @ dephased
            gates += 1
    return u, dephased, gates


def tv(a, b):
    return float(np.sum(abs(a - b)) / 2)


def posterior(transition, prior, event):
    likelihood = transition[event, :].sum(axis=0)
    evidence = float(prior @ likelihood)
    if evidence <= 0:
        raise ValueError('Impossible evidence.')
    return prior * likelihood / evidence, evidence


def run():
    n, particles, occupied = 8, 4, 3
    u, dephased, gates = conserving_circuit(n, 8, 20260926)
    transition = abs(u) ** 2
    dim = 1 << n
    charge = np.array([x.bit_count() for x in range(dim)])
    event = np.array([(x & ((1 << occupied) - 1)) == (1 << occupied) - 1
                      for x in range(dim)])
    sector = charge == particles
    prior = sector.astype(float) / sector.sum()
    direct, evidence = posterior(transition, prior, event)
    final = prior * event
    final /= final.sum()
    reverse = transition.T @ final
    check = tv(direct, reverse)
    exact_evidence = math.comb(n - occupied, particles - occupied) / math.comb(n, particles)
    if check > 1e-12 or abs(evidence - exact_evidence) > 1e-12:
        raise AssertionError('Conserved-sector posterior identity failed.')
    independent_coin_posterior, _ = posterior(dephased, prior, event)
    bias = .27
    biased = bias ** charge * (1 - bias) ** (n - charge)
    biased_direct, biased_evidence = posterior(transition, biased, event)
    biased_final = biased * event
    biased_final /= biased_final.sum()
    biased_check = tv(biased_direct, transition.T @ biased_final)
    if biased_check > 1e-12 or abs(biased_evidence - bias ** occupied) > 1e-12:
        raise AssertionError('Stationary nonuniform-prior identity failed.')
    # A further initial restriction is not automatically met by reverse sampling.
    initial = np.zeros(dim)
    initial[85] = 1  # 01010101, four occupied sites.
    _, forward_restricted = posterior(transition, initial, event)
    reverse_accept = float(reverse[85])
    boundary_count = int((sector & event).sum())
    ratio_error = abs(reverse_accept - forward_restricted / boundary_count)
    if ratio_error > 1e-12:
        raise AssertionError('Two-boundary reciprocity failed.')
    # Inference of an external controlled parameter with fresh |0> workspace.
    angles = np.array([.01, .02, .03, .04])
    likelihood = np.sin(angles) ** 2
    controller = np.zeros((8, 8))
    for i, a in enumerate(angles):
        controller[2*i:2*i+2, 2*i:2*i+2] = [[np.cos(a), -np.sin(a)],
                                                           [np.sin(a), np.cos(a)]]
    backward_input = np.zeros(8)
    backward_input[1::2] = .25
    backward = (abs(controller.T) ** 2) @ backward_input
    parameter_before_filter = backward.reshape(4, 2).sum(axis=1)
    accept = float(backward[::2].sum())
    parameter_after_filter = backward[::2] / accept
    desired = likelihood / likelihood.sum()
    if tv(parameter_before_filter, np.full(4, .25)) > 1e-12:
        raise AssertionError('Controlled parameters changed before filtering.')
    if tv(parameter_after_filter, desired) > 1e-12 or abs(accept - likelihood.mean()) > 1e-12:
        raise AssertionError('Workspace filter accounting failed.')
    return dict(
        scope='Classical finite-matrix controls, not a quantum run or advantage benchmark.',
        numpy_version=np.__version__, seed=20260926,
        conserving_example=dict(spins=n, particles=particles, two_site_gates=gates,
            occupied_output_sites=occupied, sector_configurations=int(sector.sum()),
            compatible_endpoints=boundary_count, evidence=evidence,
            exact_evidence_fraction='1/14', reverse_posterior_tv=check,
            unitarity_max_error=float(np.max(abs(u.conj().T @ u - np.eye(dim)))),
            charge_commutator_max_error=float(np.max(abs((charge[:,None]-charge[None,:])*u))),
            per_gate_dephasing_changes_posterior_tv=tv(direct, independent_coin_posterior),
            dephasing_comparison='Different physical model, not strongest classical simulation.'),
        biased_stationary_prior=dict(single_site_occupation=bias, evidence=biased_evidence,
            expected_evidence=bias**occupied, reverse_posterior_tv=biased_check),
        restricted_initial_state=dict(initial_basis_index=85, forward_evidence=forward_restricted,
            reverse_acceptance=reverse_accept, ratio_error=ratio_error,
            expected_ratio='forward_evidence / 5'),
        controlled_parameter=dict(forward_evidence=float(likelihood.mean()),
            reverse_workspace_acceptance=accept,
            parameter_distribution_before_filter=parameter_before_filter.tolist(),
            parameter_distribution_after_filter=parameter_after_filter.tolist(),
            desired_posterior=desired.tolist()),
        large_example_count_only=dict(spins=100,particles=50,occupied_output_sites=20,
            evidence=math.comb(80,30)/math.comb(100,50),
            expected_forward_rejection_trials=math.comb(100,50)/math.comb(80,30),
            scope='Combinatorial calculation only; no 100-spin simulation.'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result = run()
    with args.output.open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, indent=2, sort_keys=True))
