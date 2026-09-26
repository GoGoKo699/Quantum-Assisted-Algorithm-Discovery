"""Exact fairness audit and finite decision-value diagnostics.

Python standard library only. These are mathematical controls, not a native
inference benchmark, compiled quantum algorithm, or demonstrated speedup.
Existing files are never overwritten. No historical evidence is changed.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path


def tv(p: dict, q: dict) -> F:
    return sum((abs(p.get(x, F(0)) - q.get(x, F(0))) for x in p.keys() | q.keys()), F(0)) / 2


def law(values: tuple[int, ...]) -> dict[int, F]:
    return {x: F(n, len(values)) for x, n in Counter(values).items()}


def return_probability(g: tuple[int, ...], h: tuple[int, ...]) -> F:
    """A_g prepares four equiprobable tapes; A_h^dagger undoes h and tapes.

    Output labels 0,1,2 fit in two bits. Compute into output via XOR, then
    apply H tensor H to the two tape bits. This is a full exact statevector
    calculation in sixteen dimensions, not the overlap formula being tested.
    """
    before = [F(0)] * 16
    for z in range(4):
        before[(z << 2) | g[z]] = F(1, 2)
    uncomputed = [F(0)] * 16
    for z in range(4):
        for x in range(4):
            uncomputed[(z << 2) | (x ^ h[z])] += before[(z << 2) | x]
    after = [F(0)] * 16
    for zout, zin, x in product(range(4), range(4), range(4)):
        sign = -1 if (zout & zin).bit_count() % 2 else 1
        after[(zout << 2) | x] += sign * uncomputed[(zin << 2) | x] / 2
    if sum(a * a for a in after) != 1:
        raise AssertionError('Return circuit failed normalization.')
    return after[0] ** 2


def coupling_audit() -> dict:
    generators = list(product(range(3), repeat=4))
    cases = 0
    equal_laws = 0
    equal_law_zero_return = 0
    largest_coupling_slack = F(0)
    for g in generators:
        pg = law(g)
        for h in generators:
            ph = law(h)
            agreement = F(sum(x == y for x, y in zip(g, h)), 4)
            mismatch = 1 - agreement
            distance = tv(pg, ph)
            returned = return_probability(g, h)
            # Independent two-tape Bernoulli experiment exactly simulates the
            # distribution of a phase-free lifted-state return-test bit.
            two_tapes = F(sum(g[z] == h[z] and g[w] == h[w]
                              for z, w in product(range(4), repeat=2)), 16)
            if returned != agreement**2 or returned != two_tapes or distance > mismatch:
                raise AssertionError('Coupling/return correspondence failed.')
            largest_coupling_slack = max(largest_coupling_slack, mismatch-distance)
            cases += 1
            if distance == 0:
                equal_laws += 1
                equal_law_zero_return += int(returned == 0)
    tau, delta = .05, .05
    return dict(
        tape_values=4, output_values=3, distinct_generators=len(generators),
        ordered_generator_pairs=cases, exact_return_circuit_checks=cases,
        classical_two_tape_checks=cases*16,
        equal_output_laws=equal_laws, equal_law_zero_return=equal_law_zero_return,
        largest_slack=str(largest_coupling_slack),
        iid_no_failure_certificate=dict(
            tau=tau, delta=delta,
            classical_paired_runs=math.ceil(math.log(delta)/math.log1p(-tau)),
            return_tests_using_lifted_state_bound=math.ceil(math.log(delta)/(2*math.log1p(-tau))),
            earlier_generic_pure_state_return_tests=math.ceil(math.log(delta)/math.log1p(-tau*tau)),
            scope='One-sided soundness for a fixed candidate, fresh iid validation. Trial counts are not gate or runtime counts.'),
        scope='All ternary-output generators on four equiprobable tapes; phase-free, tape-retaining implementations only.')


def decision_value(joint: list[list[F]], utility: list[list[F]]) -> tuple[F, F, F, F]:
    """Return prior value, posterior form, unnormalized form, policy enumeration."""
    outcomes, hidden, actions = len(joint), len(joint[0]), len(utility)
    if any(len(row) != hidden for row in joint) or any(len(row) != hidden for row in utility):
        raise ValueError('Inconsistent dimensions.')
    if any(p < 0 for row in joint for p in row) or sum(map(sum, joint)) != 1:
        raise ValueError('Expected normalized nonnegative joint probabilities.')
    prior = [sum(joint[y][x] for y in range(outcomes)) for x in range(hidden)]
    baseline = max(sum(prior[x]*utility[a][x] for x in range(hidden)) for a in range(actions))
    posterior_form = F(0)
    for y in range(outcomes):
        mass = sum(joint[y])
        if mass:
            posterior_form += mass * max(sum(joint[y][x]/mass * utility[a][x]
                                             for x in range(hidden)) for a in range(actions))
    joint_form = sum(max(sum(joint[y][x]*utility[a][x] for x in range(hidden))
                         for a in range(actions)) for y in range(outcomes))
    brute = max(sum(joint[y][x] * utility[policy[y]][x]
                    for y in range(outcomes) for x in range(hidden))
                for policy in product(range(actions), repeat=outcomes))
    if posterior_form != joint_form or joint_form != brute or joint_form < baseline:
        raise AssertionError('Posterior cancellation/policy enumeration failed.')
    return baseline, posterior_form, joint_form, brute


def decision_audit() -> dict:
    binary_utility = [[F(int((x & 1) == a)) for x in range(4)] for a in range(2)]
    rational_utility = [[F(1), F(0), F(2,3), F(1,5)],
                        [F(0), F(1), F(1,3), F(4,5)]]
    checks = zero_outcome_cases = 0
    for weights in product(range(3), repeat=8):
        norm = sum(weights)
        if not norm:
            continue
        joint = [[F(weights[4*y+x], norm) for x in range(4)] for y in range(2)]
        zero_outcome_cases += int(any(not sum(row) for row in joint))
        for utility in (binary_utility, rational_utility):
            decision_value(joint, utility)
            checks += 1
    return dict(joint_distributions=3**8-1, utility_tables=2, exact_comparisons=checks,
                deterministic_policies_per_comparison=4, zero_mass_outcome_cases=zero_outcome_cases)


def marginal(joint: dict, positions: tuple[int, ...]) -> dict:
    out = defaultdict(F)
    for state, p in joint.items():
        out[tuple(state[i] for i in positions)] += p
    return dict(out)


def query_synergy() -> dict:
    # H=A XOR B is the binary decision target. An additional independent bit N
    # is irrelevant to that decision. This is invented and classically easy.
    states = list(product(range(2), repeat=4))  # (H,A,B,N)
    true = {s: F(1,8) if s[0] == (s[1] ^ s[2]) else F(0) for s in states}
    independent = {s:F(1,16) for s in states}
    marginal_checks = 0
    for positions in ((0,), (1,), (2,), (3,), (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)):
        if marginal(true, positions) != marginal(independent, positions):
            raise AssertionError('Matching low-order marginals failed.')
        marginal_checks += 1
    utilities = [[F(int(s[0] == a)) for s in states] for a in range(2)]
    query_fns = dict(A=lambda s:(s[1],), B=lambda s:(s[2],),
                     AB=lambda s:(s[1],s[2]), nuisance=lambda s:(s[3],))
    result = {}
    for name, fn in query_fns.items():
        labels = sorted({fn(s) for s in states})
        rows = []
        for model in (true, independent):
            joint = [[model[s] if fn(s) == y else F(0) for s in states] for y in labels]
            base, val, _, _ = decision_value(joint, utilities)
            rows.append(dict(baseline=str(base), value_after=str(val), information_value=str(val-base)))
        result[name] = dict(answers=len(labels), exact_model=rows[0], product_approximation=rows[1])
    # Noisy direct report of H with accuracy 3/4, independent of other bits.
    noisy = [[true[s] * (F(3,4) if s[0] == y else F(1,4)) for s in states] for y in range(2)]
    base, val, _, _ = decision_value(noisy, utilities)
    result['noisy_target'] = dict(answers=2, exact_model=dict(baseline=str(base), value_after=str(val), information_value=str(val-base)))
    # Simple net-utility comparison: illustrative costs in the same [0,1]
    # correctness utility scale, not measured user or experimental preferences.
    cost_pair = F(1,10); cost_noisy = F(1,20)
    if F(result['AB']['exact_model']['value_after']) - cost_pair != F(9,10):
        raise AssertionError('Pair net value changed.')
    return dict(matching_one_and_two_variable_marginals=marginal_checks,
                queries=result, illustrative_net_values=dict(AB='9/10',noisy_target='7/10'),
                scope='Small explicit parity model; exact enumeration is the correct classical solution, not a quantum workload.')


def run() -> dict:
    return dict(scope='Exact source-aware audit and decision-meaning checks. No learned model, native solver, quantum execution, or advantage measurement.',
                coupling=coupling_audit(), decision=decision_audit(), joint_query=query_synergy())


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True, type=Path)
    args = p.parse_args()
    if not __debug__:
        raise SystemExit('Do not run with -O/-OO.')
    if args.output.exists():
        raise SystemExit('Refusing to overwrite prior evidence.')
    report = run()
    with args.output.open('x', encoding='utf-8') as f:
        json.dump(report, f, indent=2, sort_keys=True); f.write('\n')
    print(json.dumps(report, indent=2, sort_keys=True))
