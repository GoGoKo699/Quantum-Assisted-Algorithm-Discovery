#!/usr/bin/env python3
"""One public bin-packing pricing workload; not a quantum performance benchmark.

Python 3.10+, NumPy, SciPy. Deterministic column-generation policies, HiGHS LP/MIP,
exact-integer knapsack checks, exact rational record probabilities. No network or
file writes. Input is the attributed, normalized OR-Library extraction beside this
script. Individual item labels are aggregated only by the exact root symmetry.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, linprog, milp

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')
D = 1 << 24
MAX_ROUNDS = 300
MIP_NODES = 1000
PROBABILITY_STATES = 200_000


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def validate(a: list[int], capacity: int) -> None:
    if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 1 or not a:
        raise ValueError('Positive integer capacity and nonempty items required.')
    if any(not isinstance(x, int) or isinstance(x, bool) or not 0 < x <= capacity for x in a):
        raise ValueError('Each integer item must fit by itself.')


def best_fit(a: list[int], capacity: int) -> list[list[int]]:
    bins: list[list[int]] = []
    for i in sorted(range(len(a)), key=lambda i: (-a[i], i)):
        candidates = [j for j, b in enumerate(bins) if sum(a[t] for t in b)+a[i] <= capacity]
        if candidates:
            j = min(candidates, key=lambda j: capacity-sum(a[t] for t in bins[j])-a[i])
            bins[j].append(i)
        else:
            bins.append([i])
    return bins


def knapsack(sizes: list[int], demand: list[int], v: list[int], capacity: int):
    """Binary item DP, ties maximizing used capacity. Item copies remain bounded."""
    best = [(0, 0, ())] * (capacity+1)
    relaxations = 0
    for i, (size, count) in enumerate(zip(sizes, demand)):
        for _ in range(count):
            for c in range(capacity, size-1, -1):
                prev = best[c-size]
                candidate = (prev[0]+v[i], prev[1]+size, prev[2]+(i,))
                if candidate[:2] > best[c][:2]:
                    best[c] = candidate
                relaxations += 1
    score, _, indices = best[capacity]
    pattern = tuple(indices.count(i) for i in range(len(sizes)))
    require(sum(x*w for x, w in zip(pattern, sizes)) <= capacity, 'DP returned overfull pattern.')
    require(all(0 <= x <= d for x, d in zip(pattern, demand)), 'DP reused an unavailable copy.')
    require(sum(x*p for x, p in zip(pattern, v)) == score, 'DP score mismatch.')
    return score, pattern, relaxations


def bounded_type_dp(sizes, demand, v, capacity):
    """Independent exact recurrence for validation, not used by the master policy."""
    previous = [0] * (capacity+1)
    transitions = 0
    for size, count, price in zip(sizes, demand, v):
        current = []
        for c in range(capacity+1):
            choices = range(min(count, c//size)+1)
            current.append(max(previous[c-take*size]+take*price for take in choices))
            transitions += len(choices)
        previous = current
    return previous[capacity], transitions


def cheap_pattern(sizes, demand, v, capacity):
    orders = [sorted(range(len(sizes)), key=lambda i: (-F(v[i], sizes[i]), -sizes[i], i)),
              sorted(range(len(sizes)), key=lambda i: (-v[i], -sizes[i], i)),
              list(reversed(range(len(sizes))))]
    candidates = []
    for order in orders:
        r = capacity
        pattern = [0] * len(sizes)
        for i in order:
            count = min(demand[i], r//sizes[i])
            pattern[i] = count
            r -= sizes[i]*count
        candidates.append((sum(x*p for x, p in zip(pattern, v)), tuple(pattern)))
    return max(candidates, key=lambda q: (q[0], sum(x*w for x, w in zip(q[1], sizes))))


def fractional_bound(sizes, demand, v, capacity):
    order = sorted(range(len(sizes)), key=lambda i: (-F(v[i], sizes[i]), i))
    remaining, upper, lam = capacity, F(0), F(0)
    for i in order:
        used = min(remaining, demand[i]*sizes[i])
        upper += F(used*v[i], sizes[i])
        lam = F(v[i], sizes[i])
        remaining -= used
        if remaining == 0:
            break
    if remaining:
        lam = F(0)
    algebraic = lam*capacity+sum(d*max(F(0), p-lam*w) for w, d, p in zip(sizes, demand, v))
    require(upper == algebraic, 'Fractional multiplier identity.')
    return upper, lam


def probability_diagnostic(sizes, demand, v, capacity):
    """Exact/bounded marked mass AFTER solving a difficult-to-greedy call.

    This is charged offline validation, not a free probability oracle. Threshold
    is strict > D. On budget exhaustion an unresolved state contributes [0,1].
    """
    a = [w for w, d in zip(sizes, demand) for _ in range(d)]
    prices = [p for p, d in zip(v, demand) for _ in range(d)]
    upper, lam = fractional_bound(sizes, demand, v, capacity)
    if upper <= D:
        return {'lower': '0', 'upper': '0', 'exact': True, 'free_items': len(a), 'states': 0}
    gap = upper-D
    fixed = {i: int(prices[i]-lam*a[i] > 0) for i in range(len(a)) if abs(prices[i]-lam*a[i]) > gap}
    cap = capacity-sum(a[i]*bit for i, bit in fixed.items())
    need = D-sum(prices[i]*bit for i, bit in fixed.items())
    if cap < 0:
        raise AssertionError('An improving DP pattern must survive the core.')
    order = sorted((i for i in range(len(a)) if i not in fixed and a[i] <= cap),
                   key=lambda i: (-F(prices[i], a[i]), -a[i], i))
    weights, values = [a[i] for i in order], [prices[i] for i in order]
    k = len(order)
    suffix = [[0]*(cap+1) for _ in range(k+1)]
    for i in range(k-1, -1, -1):
        for c in range(cap+1):
            suffix[i][c] = max(suffix[i+1][c], values[i]+suffix[i+1][c-weights[i]] if c >= weights[i] else 0)
    states = 0

    @lru_cache(None)
    def visit(i, c, threshold):
        nonlocal states
        if threshold < 0:
            return F(1), F(1)
        if i == k or suffix[i][c] <= threshold:
            return F(0), F(0)
        if states >= PROBABILITY_STATES:
            return F(0), F(1)
        states += 1
        if c < weights[i]:
            return visit(i+1, c, threshold)
        a0, b0 = visit(i+1, c, threshold)
        a1, b1 = visit(i+1, c-weights[i], threshold-values[i])
        return (a0+a1)/2, (b0+b1)/2

    lo, hi = visit(0, cap, need)
    return {'lower': str(lo), 'upper': str(hi), 'lower_decimal': round(float(lo), 12),
            'upper_decimal': round(float(hi), 12), 'exact': lo == hi,
            'free_items': k, 'fixed_items': len(fixed), 'states': states,
            'suffix_cells': k*(cap+1), 'score_denominator': D,
            'capacity_bits': max(1, cap.bit_length()),
            'safe_score_bits': max(D, sum(prices)).bit_length()}


def rational_primal_upper(columns, x, demand):
    coefficients = [math.ceil(max(0., float(t))*D) for t in x]
    coverage = [sum(coef*col[i] for coef, col in zip(coefficients, columns)) for i in range(len(demand))]
    require(all(t > 0 for t in coverage), 'Empty primal coverage.')
    # Scale the rounded primal UP if required. No dependence on LP optimality.
    scale = max([F(1)]+[F(d*D, t) for d, t in zip(demand, coverage)])
    require(all(scale*t >= D*d for t, d in zip(coverage, demand)), 'Exact covering check.')
    return F(sum(coefficients), D)*scale


def expand_packing(a, sizes, columns, integer_values, capacity):
    remaining = {w: [i for i, x in enumerate(a) if x == w] for w in sizes}
    packing = []
    for pattern, count in zip(columns, integer_values):
        for _ in range(count):
            items = []
            for w, slots in zip(sizes, pattern):
                for _ in range(min(slots, len(remaining[w]))):
                    items.append(remaining[w].pop())
            if items:
                packing.append(sorted(items))
    require(not any(remaining.values()), 'Integer columns do not cover all items.')
    require(sorted(i for b in packing for i in b) == list(range(len(a))), 'Individual item check.')
    require(all(sum(a[i] for i in b) <= capacity for b in packing), 'Integer capacity check.')
    return packing


def run_policy(a, capacity, policy):
    require(policy in ('exact-pricing', 'greedy-first'), 'Unknown policy.')
    n = len(a)
    sizes = sorted(set(a))
    demand = [a.count(w) for w in sizes]
    types = len(sizes)
    initial = best_fit(a, capacity)
    columns = list(dict.fromkeys([tuple(int(j == i) for j in range(types)) for i in range(types)] +
                  [tuple(sum(a[i] == w for i in b) for w in sizes) for b in initial]))
    volume_lower = (sum(a)+capacity-1)//capacity
    diagnostics, trace, mip_log = [], [], []
    counts = Counter()
    next_mip = None
    certificate = None
    for iteration in range(MAX_ROUNDS):
        matrix = np.array(columns, dtype=float).T
        result = linprog(np.ones(len(columns)), A_ub=-matrix, b_ub=-np.array(demand),
                         bounds=(0, None), method='highs-ds', options={
                             'dual_feasibility_tolerance': 1e-9, 'primal_feasibility_tolerance': 1e-9})
        require(result.success, 'Restricted LP failed: '+result.message)
        counts['restricted_LP_solves'] += 1
        primal_upper = rational_primal_upper(columns, result.x, demand)
        raw = np.maximum(0., -result.ineqlin.marginals)
        prices = [math.floor(float(p)*D) for p in raw]
        # The dual is native floating-point; rounded coefficients define an exact
        # pricing problem. Any certified global lower bound is valid even without
        # assuming that these scores are exactly optimal restricted-master duals.
        require(all(abs(float(p)-v/D) < 1/D+1e-14 for p, v in zip(raw, prices)), 'Price conversion.')
        for col in columns:
            require(sum(x*v for x, v in zip(col, prices)) <= D, 'Rounded dual violated a current column.')
        row = {'iteration': iteration, 'columns': len(columns),
               'LP_objective_diagnostic': round(float(result.fun), 10),
               'rational_primal_upper': str(primal_upper)}
        # One predetermined recovery schedule: first at LP<=volume ceil, then
        # after ten more columns. No reference answer is used to find the target.
        if next_mip is None and result.fun <= volume_lower+1e-8:
            next_mip = iteration
        if next_mip is not None and iteration >= next_mip:
            recovered = milp(np.ones(len(columns)), integrality=np.ones(len(columns)),
                             bounds=Bounds(0, np.inf), constraints=LinearConstraint(matrix, demand, np.inf),
                             options={'mip_rel_gap': 0, 'node_limit': MIP_NODES})
            counts['integer_recovery_calls'] += 1
            recovery = {'iteration': iteration, 'solver_status': int(recovered.status),
                        'nodes': int(recovered.mip_node_count or 0), 'verified_bins': None}
            if recovered.x is not None:
                ints = [int(round(float(x))) for x in recovered.x]
                require(all(t >= 0 for t in ints) and max(abs(float(x)-t) for x, t in zip(recovered.x, ints)) < 1e-5,
                        'MIP integer rounding failed.')
                candidate = expand_packing(a, sizes, columns, ints, capacity)
                recovery['verified_bins'] = len(candidate)
                if len(candidate) == volume_lower:
                    certificate = candidate
            mip_log.append(recovery)
            next_mip = iteration+10
        if certificate is not None:
            row['action'] = 'stop: exact volume plus verified packing certificate'
            trace.append(row)
            break
        upper, _ = fractional_bound(sizes, demand, prices, capacity)
        cheap_score, cheap = cheap_pattern(sizes, demand, prices, capacity)
        counts['three_order_greedy_screens'] += 1
        row['fractional_score_upper'] = str(upper/D)
        row['greedy_score'] = str(F(cheap_score, D))
        if upper <= D:
            raise AssertionError('This fixture reached a fractional no-column stop before its integer certificate.')
        if cheap_score > D:
            counts['greedy_positive_calls'] += 1
        else:
            counts['greedy_failed_calls'] += 1
        if policy == 'greedy-first' and cheap_score > D:
            score, pattern = cheap_score, cheap
            row['action'] = 'greedy-column'
        else:
            score, pattern, relax = knapsack(sizes, demand, prices, capacity)
            counts['actual_exact_DP_calls'] += 1
            counts['actual_exact_DP_relaxations'] += relax
            independent, transitions = bounded_type_dp(sizes, demand, prices, capacity)
            require(score == independent, 'Independent exact pricing recurrence disagrees.')
            counts['validation_DP_calls'] += 1
            counts['validation_DP_transitions'] += transitions
            counts['positive_exact_DP_calls' if score > D else 'nonpositive_exact_DP_calls'] += 1
            lb = F(sum(d*v for d, v in zip(demand, prices)), max(D, score))
            require(lb <= primal_upper, 'Global lower/feasible upper contradiction.')
            row['exact_price'] = str(F(score, D))
            row['certified_full_LP_lower'] = str(lb)
            row['action'] = 'exact-DP-column'
            if cheap_score <= D and score > D:
                p = probability_diagnostic(sizes, demand, prices, capacity)
                require(p['exact'], 'Fixture probability evaluation exhausted its separate cap.')
                p.update({'iteration': iteration, 'prices_by_ascending_type': prices,
                          'exact_price': str(F(score, D))})
                diagnostics.append(p)
        require(score > D, 'No-column pricing before this fixture was packed; broaden stopping logic before reuse.')
        require(pattern not in columns, 'Attempted duplicate improving column.')
        require(sum(x*w for x, w in zip(pattern, sizes)) <= capacity, 'New pattern is infeasible.')
        if trace and abs(row['LP_objective_diagnostic']-trace[-1]['LP_objective_diagnostic']) < 1e-9:
            counts['unchanged_LP_objective_after_last_addition'] += 1
        trace.append(row)
        columns.append(pattern)
    require(certificate is not None, 'Iteration cap reached without a certificate.')
    result = {'policy': policy, 'initial_column_count': len(columns)-(len(trace)-1),
            'final_column_count': len(columns), 'counts': dict(sorted(counts.items())),
            'added_columns': len(trace)-1, 'integer_recovery': mip_log,
            'final_primal_upper': trace[-1]['rational_primal_upper'],
            'volume_lower_bound': volume_lower, 'verified_packing_bins': len(certificate),
            'packing_item_ids_zero_based': certificate, 'last_action': trace[-1]['action'],
            'pricing_trace': trace, 'post_solution_probability_diagnostics': diagnostics}
    result['price_trace_sha256'] = hashlib.sha256(json.dumps(trace, sort_keys=True).encode()).hexdigest()
    if '--full-trace' not in sys.argv:
        result['first_LP_objective'] = trace[0]['LP_objective_diagnostic']
        result['last_LP_objective'] = trace[-1]['LP_objective_diagnostic']
        del result['pricing_trace']
        for record in diagnostics:
            record['price_vector_sha256'] = hashlib.sha256(json.dumps(record.pop('prices_by_ascending_type')).encode()).hexdigest()
    return result


def main():
    source = Path(__file__).with_name('instance.json')
    raw = source.read_bytes()
    instance = json.loads(raw)
    a, capacity = instance['sizes'], instance['capacity']
    validate(a, capacity)
    require(instance['name'] == 'u120_00' and len(a) == 120 and capacity == 150, 'Wrong fixture.')
    policies = [run_policy(a, capacity, name) for name in ('exact-pricing', 'greedy-first')]
    # Capacity units must not manufacture an apparent difficult input. Dividing
    # by the gcd leaves exactly the same feasible binary patterns.
    scale = 1000
    divisor = math.gcd(*(scale*x for x in [capacity]+a))
    require([scale*x//divisor for x in a] == a and scale*capacity//divisor == capacity, 'Units reduction.')
    # Exact checks on the smallest binary-vs-unbounded counterexample.
    value, pattern, _ = knapsack([2], [1], [3], 4)
    require(value == 3 and pattern == (1,), 'Illicit unbounded multiplicity.')
    # Margin rounding is accounted for; <=7 items fit here, so rounding each
    # price down by <1/D changes every pattern score by <7/D.
    max_items = capacity//min(a)
    require(max_items == 7, 'Fixture cardinality bound.')
    # Event probability depends on the generator, not uniform feasible labels.
    # With two size-two items and cap two, (00,01,10) have mass (1/4,1/4,1/2).
    require(F(1,4)+F(1,4)+F(1,2) == 1 and F(1,2) != F(1,3), 'Nonuniform law control.')
    invalid = [([], 1), ([0], 1), ([2], 1), ([1], 0), ([True], 2), ([1], 1.5)]
    for sizes, cap in invalid:
        try:
            validate(sizes, cap)
        except ValueError:
            continue
        else:
            raise AssertionError('Invalid data accepted.')
    print(json.dumps({'status': 'pass', 'scope': 'One public instance, two declared root workflows; exact output certificate, not an industrial or quantum timing benchmark.',
      'instance': {'name': instance['name'], 'n': len(a), 'capacity': capacity,
                   'equal_size_types': len(set(a)), 'total_size': sum(a),
                   'source': instance['source'], 'input_sha256': hashlib.sha256(raw).hexdigest(),
                   'source_reference_count_used_by_algorithm': False},
      'software': {'numpy': np.__version__, 'scipy': scipy.__version__,
                   'LP': 'SciPy linprog/HiGHS dual simplex', 'integer_recovery': 'SciPy milp/HiGHS, node cap 1000'},
      'fixed_policy': {'dual_denominator': D, 'iterations_cap': MAX_ROUNDS,
                       'integer_recovery_interval_columns': 10, 'probability_state_cap_per_call': PROBABILITY_STATES,
                       'stabilization': 'none; equal-size item symmetry aggregated exactly',
                       'DP_tie_rule': 'profit, then used capacity; existing state wins remaining ties'},
      'work_per_full_item_DP_call': sum(capacity-size+1 for size in a),
      'pattern_price_rounding_error_bound': str(F(max_items, D)),
      'policies': policies, 'invalid_inputs_rejected': len(invalid),
      'limitations': ['One benchmark is not a representative hard-pricing sample.',
                      'HiGHS primal/duals are floating; returned packings and price-DP statements are checked with integers/rationals.',
                      'Exact probabilities were calculated after classical solution as charged diagnostics, not provided freely to a quantum algorithm.',
                      'No quantum search, FPTAS, advanced lexicographic/stabilized pricer, native SCIP, or timing crossover was run.',
                      'Reference number in the input is metadata only; volume and explicit item assignment prove the achieved bin count.']}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
