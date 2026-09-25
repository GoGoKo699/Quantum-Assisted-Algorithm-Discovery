#!/usr/bin/env python3
"""Exact target-closure probe. Original research code; no quantum execution.

Run in Python without -O. Only the standard library is required.
"""
from __future__ import annotations
import argparse
from collections import deque
from itertools import combinations, product
import json
from pathlib import Path
import random
import sys
import time
from vendor import upstream_dependency as upstream

ROOT = Path(__file__).resolve().parent
Vector = tuple[int, ...]


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def canon(v: Vector, modulus: int | None = None) -> Vector:
    if modulus == 2:
        return tuple(x % 2 for x in v)
    for x in v:
        if x:
            return v if x > 0 else tuple(-y for y in v)
    return v


def combine(a: Vector, b: Vector, sign: int, modulus: int | None) -> tuple[Vector, int, int]:
    raw = tuple(x + sign*y for x, y in zip(a, b))
    h = canon(raw, modulus)
    orientation = 1 if modulus == 2 or h == raw else -1
    return h, orientation, sign*orientation


def closure_rules(options: list[list[dict]], target_count: int) -> tuple[list, dict]:
    """Forward-chain positive Horn rules; no enumeration of subsets/schedules."""
    rules = []
    users = [[] for _ in options]
    for node, choices in enumerate(options):
        for choice in choices:
            mask = choice['requirement']
            require(mask >= 0 and mask < (1 << len(options)), 'invalid prerequisite mask')
            rid = len(rules)
            rules.append((node, choice, mask.bit_count()))
            unseen = mask
            while unseen:
                lowest = unseen & -unseen
                users[lowest.bit_length() - 1].append(rid)
                unseen ^= lowest
    remaining = [rule[2] for rule in rules]
    queue = deque(i for i, count in enumerate(remaining) if count == 0)
    state = 0
    path = []
    processed = 0
    decrements = 0
    goal = (1 << target_count) - 1
    while queue and state & goal != goal:
        rid = queue.popleft()
        processed += 1
        node, rule, _ = rules[rid]
        if state & (1 << node):
            continue
        require(rule['requirement'] & ~state == 0, 'premature rule firing')
        state |= 1 << node
        path.append((node, rule))
        for user in users[node]:
            remaining[user] -= 1
            decrements += 1
            if remaining[user] == 0:
                queue.append(user)
    return path, {'success': state & goal == goal, 'state': state,
                  'node_firings': len(path), 'rules': len(rules),
                  'rule_pops': processed, 'dependency_decrements': decrements}


def validate_rule_path(path, options, target_count):
    if path is None:
        return
    state = 0
    for node, rule in path:
        require(rule in options[node], 'unknown rule')
        require(not state & (1 << node), 'node produced twice')
        require(rule['requirement'] & ~state == 0, 'missing prerequisite')
        state |= 1 << node
    require(state & ((1 << target_count)-1) == (1 << target_count)-1, 'incomplete path')


def closure_equivalence():
    count = 0
    for choices in product(range(16), repeat=3):
        options = []
        for node, pattern in enumerate(choices):
            others = [i for i in range(3) if i != node]
            reqs = [sum((1 << j) for k,j in enumerate(others) if m & (1 << k))
                    for m in range(4)]
            options.append([{'requirement': reqs[i]} for i in range(4) if pattern & (1<<i)])
        for target_count in range(4):
            expected = upstream.reachable_path(options, target_count)
            path, stats = closure_rules(options, target_count)
            require((expected is not None) == stats['success'], 'Horn closure disagreement')
            if stats['success']:
                validate_rule_path(path, options, target_count)
            count += 1
    return {'three_node_rule_systems': 4096, 'goal_comparisons': count}


def expand_source():
    data = json.loads((ROOT/'cn122_source.json').read_text())
    def evaluate(n, fresh, outputs):
        values = upstream.basis(n)
        for form in fresh:
            require(all(0 <= i < len(values) and s in (-1,1) for i,s in form), 'bad source wire')
            values.append(tuple(sum(s*values[i][j] for i,s in form) for j in range(n)))
        return [tuple(sum(s*values[i][j] for i,s in form) for j in range(n)) for form in outputs]
    u = evaluate(9, data['u_fresh'], data['u'])
    v = evaluate(9, data['v_fresh'], data['v'])
    wt = evaluate(23, data['w_fresh'], data['w'])
    w = list(zip(*wt))
    gamma = [wt[3*j+i] for i in range(3) for j in range(3)]
    for a, b, out in product(range(9), repeat=3):
        expected = int(a%3 == b//3 and out//3 == a//3 and out%3 == b%3)
        actual = sum(u[r][a]*v[r][b]*gamma[out][r] for r in range(23))
        require(actual == expected, 'source tensor failed')
    return {'U': u, 'V': v, 'W': [tuple(x) for x in w]}, gamma


class CountingDeque(deque):
    pops = 0
    pushes = 0
    def __init__(self, iterable=()):
        super().__init__(iterable)
        type(self).pushes += len(self)
    def append(self, x):
        type(self).pushes += 1
        super().append(x)
    def popleft(self):
        type(self).pops += 1
        return super().popleft()


def upstream_trial(options, d):
    original = upstream.deque
    CountingDeque.pops = CountingDeque.pushes = 0
    upstream.deque = CountingDeque
    start = time.perf_counter()
    try:
        path = upstream.reachable_path(options, d)
    finally:
        upstream.deque = original
    return path, {'states_popped': CountingDeque.pops, 'states_inserted': CountingDeque.pushes,
                  'seconds': time.perf_counter()-start}


def source_benchmark(rows):
    targets = upstream.unique_targets(rows, 9)
    pure = upstream.dependency_options(targets)
    p, native = upstream_trial(pure, len(targets))
    path, closed = closure_rules(pure, len(targets))
    require(p is None and not closed['success'], 'unexpected direction-floor solution')
    all_candidates = upstream.auxiliary_candidates(targets)
    all_pops = native['states_popped']
    all_inserted = native['states_inserted']
    native_secs = native['seconds']
    all_firings = closed['node_firings']
    closure_secs = 0.0
    tested = 0
    final = None
    for aux, aux_rules in all_candidates.items():
        extra = upstream.options_using_auxiliary(targets, aux)
        options = [p+e for p,e in zip(pure,extra)] + [aux_rules]
        path, stats = upstream_trial(options, len(targets))
        t = time.perf_counter()
        alt_path, alt_stats = closure_rules(options, len(targets))
        closure_secs += time.perf_counter()-t
        require((path is not None) == alt_stats['success'], 'native/closure mismatch')
        all_pops += stats['states_popped']; all_inserted += stats['states_inserted']
        native_secs += stats['seconds']; all_firings += alt_stats['node_firings']
        tested += 1
        if path is not None:
            validate_rule_path(path, options, len(targets))
            validate_rule_path(alt_path, options, len(targets))
            require(len(path) == len(targets)+1 and len(alt_path) == len(path), 'wrong optimum')
            final = {'native_path_length': len(path), 'closure_path_length': len(alt_path),
                     'selected_auxiliary': list(aux)}
            break
    require(final is not None, 'failed to reproduce published upper bound')
    return {'targets': len(targets), 'pure_target_floor_impossible': True,
            'total_enumerated_auxiliary_candidates': len(all_candidates),
            'candidate_tests_until_same_first_success': tested,
            'native_subset_states_popped_including_floor_test': all_pops,
            'native_subset_states_inserted_including_floor_test': all_inserted,
            'closure_node_firings_including_floor_test': all_firings,
            **final}, {'native_reachability_seconds': native_secs,
                       'closure_reachability_seconds_excluding_floor': closure_secs}


def saturate(values: list[Vector], gates: list[dict], targets: set[Vector], modulus=None):
    """Append all constructible target directions, each once. Never delete wires."""
    values = values.copy(); gates = gates.copy()
    seen = set(values)
    i = 0
    pairs = 0
    while i < len(values):
        for j in range(i+1):
            for s in ((1,) if i == j or modulus == 2 else (1,-1)):
                h, si, sj = combine(values[i], values[j], s, modulus)
                pairs += 1
                if h in targets and h not in seen:
                    gates.append({'left': i, 'right': j, 'left_sign': si, 'right_sign': sj,
                                  'kind': 'target'})
                    seen.add(h); values.append(h)
        i += 1
    return values, gates, pairs


def helper_candidates(values: list[Vector], targets: set[Vector], modulus=None):
    seen = set(values) | targets
    candidates = {}
    for i, a in enumerate(values):
        for j in range(i+1):
            for s in ((1,) if i == j or modulus == 2 else (1,-1)):
                h, si, sj = combine(a, values[j], s, modulus)
                if any(h) and h not in seen and h not in candidates:
                    candidates[h] = {'left': i, 'right': j, 'left_sign': si, 'right_sign': sj,
                                     'kind': 'helper'}
    return [(h,candidates[h]) for h in sorted(candidates)]


def synthesize(rows, n, helper_budget, modulus=None):
    require(helper_budget >= 0, 'negative helper budget')
    base = upstream.basis(n)
    targets = {canon(tuple(row),modulus) for row in rows}
    targets = {v for v in targets if any(v)} - set(base)
    stats = {'tree_nodes':0, 'helper_candidates_generated':0, 'pair_operations':0,
             'helper_budget':helper_budget, 'target_directions':len(targets)}
    def dfs(values, gates, depth):
        stats['tree_nodes'] += 1
        values, gates, pairs = saturate(values,gates,targets,modulus)
        stats['pair_operations'] += pairs
        if targets <= set(values):
            return values,gates
        if depth == helper_budget:
            return None
        candidates = helper_candidates(values,targets,modulus)
        stats['helper_candidates_generated'] += len(candidates)
        for h, gate in candidates:
            result = dfs(values+[h],gates+[gate],depth+1)
            if result is not None:
                return result
        return None
    found = dfs(base,[],0)
    if found is None:
        return None, stats
    values, gates = found
    outputs = []
    for row in rows:
        v = canon(tuple(row),modulus)
        if not any(v):
            outputs.append({'slot':None,'sign':0})
        else:
            sign = 1 if modulus == 2 or v == tuple(row) else -1
            outputs.append({'slot':values.index(v),'sign':sign})
    circuit = {'input_count':n,'gates':gates,'outputs':outputs, 'modulus':modulus}
    require(len(gates) <= len(targets)+helper_budget, 'over budget')
    require(replay(circuit) == [tuple(x % 2 for x in row) if modulus == 2 else tuple(row) for row in rows], 'certificate mismatch')
    return circuit, stats


def replay(circuit):
    values = upstream.basis(circuit['input_count'])
    modulus = circuit.get('modulus')
    for gate in circuit['gates']:
        i,j = gate['left'],gate['right']
        require(0 <= i < len(values) and 0 <= j < len(values), 'forward gate reference')
        require(gate['left_sign'] in (-1,1) and gate['right_sign'] in (-1,1), 'invalid gate sign')
        v = tuple(gate['left_sign']*a+gate['right_sign']*b for a,b in zip(values[i],values[j]))
        if modulus == 2: v = tuple(x%2 for x in v)
        values.append(v)
    return [tuple(0 for _ in range(circuit['input_count'])) if o['slot'] is None else
            tuple((o['sign']*x)%2 if modulus == 2 else o['sign']*x for x in values[o['slot']])
            for o in circuit['outputs']]


def transpose_circuit(circuit):
    """Reverse accumulation, counting all binary additions; signs/copies free."""
    require(circuit.get('modulus') is None, 'integer transpose only')
    n = circuit['input_count']; gates = circuit['gates']; m = len(circuit['outputs'])
    adj = [[] for _ in range(n+len(gates))]
    result = {'input_count':m,'gates':[],'outputs':[], 'modulus':None}
    def merge(terms):
        if not terms: return None
        left, sl = terms[0]
        for right,sr in terms[1:]:
            result['gates'].append({'left':left,'right':right,'left_sign':sl,'right_sign':sr,'kind':'transpose'})
            left,sl = m+len(result['gates'])-1,1
        return left,sl
    for out,o in enumerate(circuit['outputs']):
        if o['slot'] is not None:
            adj[o['slot']].append((out,o['sign']))
    for i in reversed(range(n,n+len(gates))):
        value = merge(adj[i])
        if value is None: continue
        wire, sign = value; g = gates[i-n]
        adj[g['left']].append((wire,sign*g['left_sign']))
        adj[g['right']].append((wire,sign*g['right_sign']))
    for terms in adj[:n]:
        value = merge(terms)
        result['outputs'].append({'slot':None,'sign':0} if value is None else {'slot':value[0],'sign':value[1]})
    return result


def unrestricted_states(n, max_gates, modulus=None):
    """Brute-force full addition circuits; used only on tiny independent tests."""
    base = tuple(upstream.basis(n)); layer = {base}; all_layers = [layer]
    for depth in range(max_gates):
        following = set()
        for state in layer:
            for h,_ in helper_candidates(list(state),set(),modulus):
                following.add(tuple(sorted(set(state)|{h})))
        all_layers.append(following); layer = following
    return all_layers


def normal_form_tests():
    # Integer tests include repeated operands/doubling. No coefficient cutoff.
    layers = unrestricted_states(2,3)
    directions = sorted({canon(tuple(v)) for v in product(range(-2,3),repeat=2)
                         if any(v)}-set(upstream.basis(2)))
    count = 0
    for targets in combinations(directions,2):
        truth = any(set(targets) <= set(s) for layer in layers for s in layer)
        circuit,_ = synthesize(targets,2,1)
        require((circuit is not None) == truth,'integer normal form disagrees with full gate search')
        count += 1
    layers2 = unrestricted_states(3,4,2)
    binary_dirs = sorted({tuple(v) for v in product(range(2),repeat=3) if any(v)}-set(upstream.basis(3)))
    binary_count = 0
    for mask in range(1<<len(binary_dirs)):
        targets = [v for i,v in enumerate(binary_dirs) if mask & (1<<i)]
        for k in range(3):
            cap = len(targets)+k
            if cap > 4: continue
            truth = any(set(targets) <= set(s) for layer in layers2[:cap+1] for s in layer)
            circuit,_ = synthesize(targets,3,k,2)
            require((circuit is not None) == truth,'binary normal form disagrees with full gate search')
            binary_count += 1
    return {'integer_two_target_tests':count,'integer_full_search_layer_sizes':[len(x) for x in layers],
            'binary_target_budget_tests':binary_count,'binary_full_search_layer_sizes':[len(x) for x in layers2]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--timing-output', type=Path)
    args = parser.parse_args()
    require(not sys.flags.optimize,'do not use -O or -OO')
    for p in [args.output,args.timing_output]:
        if p: require(not p.exists(),'refusing to overwrite an existing result')
    eq = closure_equivalence()
    maps,gamma = expand_source()
    benchmarks = {}; timings = {}; circuits = {}; searches = {}
    for name,rows in maps.items():
        benchmarks[name],timings[name] = source_benchmark(rows)
        c0,_ = synthesize(rows,9,0)
        require(c0 is None, 'unexpected floor witness')
        c1,stats = synthesize(rows,9,1)
        require(c1 is not None,'eager one-helper search failed')
        circuits[name] = c1; searches[name] = stats
    wt = transpose_circuit(circuits['W'])
    wt['outputs'] = [wt['outputs'][3*j+i] for i in range(3) for j in range(3)]
    require(replay(wt) == gamma,'transposed output incorrect')
    circuits['output'] = wt
    total = len(circuits['U']['gates'])+len(circuits['V']['gates'])+len(wt['gates'])
    require(total == 55,'published additive total not reproduced')
    normal = normal_form_tests()
    result = {'scope':'Classical exact synthesis and model checks; no quantum speedup or new matrix identity.',
              'tensor_integer_equations':729,'rule_equivalence':eq,
              'published_dependency_core_reproduction':benchmarks,
              'eager_helper_search':searches,'normal_form_tests':normal,
              'additions': {'U':len(circuits['U']['gates']),'V':len(circuits['V']['gates']),
                            'W_factor':len(circuits['W']['gates']),'W_output':len(wt['gates']),
                            'total':total}, 'circuits':circuits}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    if args.timing_output:
        args.timing_output.write_text(json.dumps(timings,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'circuits'},indent=2))

if __name__ == '__main__': main()
