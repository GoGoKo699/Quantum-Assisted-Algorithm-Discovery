#!/usr/bin/env python3
"""Exact controls for short-seed spectral sampling, not a quantum implementation.

Python 3.10+, standard library only. No randomness trials, files, network,
spanner-performance run or claim of an application speedup.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json
import sys

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')
COUNTS: Counter[str] = Counter()


def require(ok: bool, label: str) -> None:
    if not ok:
        raise AssertionError(label)
    COUNTS[label] += 1


def gf_mul(a: int, b: int) -> int:
    """GF(8), polynomial basis modulo x^3+x+1, coefficients encoded as bits."""
    if not 0 <= a < 8 or not 0 <= b < 8:
        raise ValueError('Field values must be in 0..7.')
    out = 0
    for _ in range(3):
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11
    return out


def field_eval(coeffs: tuple[int, ...], x: int) -> int:
    if not coeffs or not 0 <= x < 8 or any(not 0 <= c < 8 for c in coeffs):
        raise ValueError('Invalid polynomial or field address.')
    ans = 0
    for c in reversed(coeffs):
        ans = gf_mul(ans, x) ^ c
    return ans


def round_up(p: F, bits: int) -> F:
    if not 0 < p <= 1 or not isinstance(bits, int) or isinstance(bits, bool) or bits < 1:
        raise ValueError('Use probability in (0,1] and a positive bit count.')
    scale = 1 << bits
    a = (p.numerator * scale + p.denominator - 1) // p.denominator
    return F(a, scale)


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def trace_power(a, power):
    n = len(a)
    acc = [[int(i == j) for j in range(n)] for i in range(n)]
    for _ in range(power):
        acc = matmul(acc, a)
    return sum(acc[i][i] for i in range(n))


def field_controls():
    # Independent algebraic field checks precede polynomial-distribution checks.
    for a in range(1, 8):
        require(sum(gf_mul(a,b) == 1 for b in range(1,8)) == 1, 'unique_field_inverse')
    for a,b,c in product(range(8),repeat=3):
        require(gf_mul(a,b ^ c) == gf_mul(a,b) ^ gf_mul(a,c), 'field_distributivity')
    seeds = list(product(range(8), repeat=4))
    for addresses in ((0,1,2,3), (1,3,5,7), (2,4,6,7)):
        histogram = Counter(tuple(field_eval(s,x) for x in addresses) for s in seeds)
        require(len(histogram) == 8**4 and set(histogram.values()) == {1}, 'four_output_bijection')
    addresses = (1,3,5,7)
    thresholds = (1,3,5,8)
    distribution = Counter(tuple(int(field_eval(s,x) < a) for x,a in zip(addresses,thresholds)) for s in seeds)
    for bits in product((0,1),repeat=4):
        expected = 1
        for bit,a in zip(bits,thresholds):
            expected *= a if bit else 8-a
        require(distribution[bits] == expected, 'thresholded_joint_probabilities')
    return {'field': 'GF(8), modulus x^3+x+1', 'coefficients':4,
            'seed_bits':12, 'seeds_exhausted':len(seeds),
            'scope':'Tiny exact field identities only; no scalable field compiler or quantum oracle.'}


def noncommutative_controls():
    edges = list(combinations(range(4),2))
    rows = list(product((0,1),repeat=6))
    even = [b for b in rows if sum(b)%2 == 0]
    # Even parity on six bits is five-wise, but not fully independent.
    for chosen in combinations(range(6),4):
        marginal = Counter(tuple(b[i] for i in chosen) for b in even)
        require(len(marginal) == 16 and set(marginal.values()) == {2}, 'four_bit_parity_marginal')
    result = {}
    for degree in (2,4,6):
        numerators = []
        for family in (rows,even):
            total = 0
            for bits in family:
                a = [[0]*4 for _ in range(4)]
                for (u,v),bit in zip(edges,bits):
                    sign=2*bit-1
                    a[u][u]+=sign;a[v][v]+=sign;a[u][v]-=sign;a[v][u]-=sign
                # K4: normalized Laplacian error is (2 L_sample-L_K4)/4.
                total += trace_power(a,degree)
            numerators.append(F(total,len(family)*4**degree))
        result[str(degree)] = {'independent':str(numerators[0]), 'even_parity':str(numerators[1])}
        require((numerators[0] == numerators[1]) == (degree <= 4), 'low_moment_not_full_law')
    return result


def rounding_and_adaptation():
    rounded=[]
    for p in (F(1,1000),F(2,7),F(1,2),F(1)):
        pp=round_up(p,5);a=int(pp*32)
        require(p <= pp < p+F(1,32) or pp == p, 'upward_probability_rounding')
        expectation=sum((F(1,pp) if h<a else F(0)) for h in range(32))/32
        require(expectation == 1, 'rounded_probability_reweight_unbiased')
        rounded.append({'requested':str(p),'actual':str(pp),'threshold':a})
    independent=sum(F(4*x*y,4) for x,y in product((0,1),repeat=2))
    reused=sum(F(4*x*x,2) for x in (0,1))
    require(independent == 1 and reused == 2, 'fresh_layer_seed_essential')
    # An arbitrary graph chosen after seeing the next seed is not conditionable as fixed.
    good=sum(F((1-x)*2*y,4) for x,y in product((0,1),repeat=2))
    bad=sum(F((1-x)*2*x,2) for x in (0,1))
    require(good == F(1,2) and bad == 0, 'lookahead_graph_bias_detected')
    return {'rounded_rows':rounded,'two_layer_expected_weight':str(independent),
            'reused_seed_expected_weight':str(reused),
            'fresh_graph_then_seed_expectation':str(good),'seed_then_graph_bias':str(bad)}


def implicit_replay():
    # Deterministic artificial layer transcript: checks replay, not spectral quality.
    weights={e:F(e+1,7) for e in range(7)}
    states=[weights.copy()];packs=[];seeds=[]
    for j in range(3):
        alive=[e for e,w in weights.items() if w]
        pack=set(alive[:min(1,len(alive))])
        seed=(j+1,2*j%8,3,4)
        packs.append(pack);seeds.append(seed)
        for edge,w in list(weights.items()):
            if w and edge not in pack:
                weights[edge]=4*w if field_eval(seed,edge)<2 else F(0)
        states.append(weights.copy())
    for last in range(4):
        for edge,initial in states[0].items():
            current=initial
            for pack,seed in zip(packs[:last],seeds[:last]):
                if current and edge not in pack:
                    current=4*current if field_eval(seed,edge)<2 else F(0)
            require(current==states[last][edge], 'implicit_weight_replay')
    require(any(v==0 for v in weights.values()), 'replay_contains_deletion')
    return {'layers':3,'addresses':7,'scope':'Membership/reweighting algebra, not a spanner constructor.'}


def main():
    field=field_controls();moment=noncommutative_controls()
    adaptive=rounding_and_adaptation();replay=implicit_replay()
    # Constants after explicit symmetrization of the independent comparison sum.
    for theta in (F(1,100),F(1,4),F(1,2),F(1)):
        require(theta/8+theta*theta/32 <= 5*theta/32 < theta/4, 'spectral_moment_constant')
    # Put x=sqrt(mu/(e*k)); the count threshold leaves (x-2)^2+12.
    for x in (F(0),F(1,4),F(1),F(4),F(100)):
        require(x*x+32-2*(2*x+8) == (x-2)**2+12 > 0, 'scalar_count_constant_control')
    # Independent exact electrical-energy control: 3 disjoint length-2 paths.
    require(F(1,1+F(3,2)) <= F(2,3), 'parallel_path_leverage_bound')
    invalid=[lambda:gf_mul(8,1),lambda:gf_mul(-1,0),lambda:field_eval((),1),
             lambda:field_eval((1,2),8),lambda:round_up(F(0),3),lambda:round_up(F(1,2),0)]
    for action in invalid:
        try: action()
        except ValueError: COUNTS['invalid_inputs_rejected']+=1
        else: raise AssertionError('Invalid argument accepted')
    print(json.dumps({'status':'pass','arithmetic':'Exact integers and Fractions; standard library.',
        'counts':dict(sorted(COUNTS.items())),'field_control':field,'trace_moments':moment,
        'rounding_and_adaptivity':adaptive,'implicit_oracle_control':replay,
        'not_executed':['quantum search','quantum spanner routine','large sparsifier',
                        'QRAM circuit','classification benchmark','historical verifier'],
        'scope':'Finite proof-component controls. General correctness and resource bounds are in the note; no empirical speedup or priority claim.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
