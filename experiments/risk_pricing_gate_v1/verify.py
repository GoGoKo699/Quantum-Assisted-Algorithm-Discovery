#!/usr/bin/env python3
"""Exact risk/pricing-interface controls, not a cloud or quantum workload.

Python 3.10+, standard library only. No network, inputs, file writes or random trials.
The result is an input-model/circuit screen; no pricer or amplitude search is run.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
import json
import sys

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')


def exact_nonnegative(x):
    return isinstance(x, (int, F)) and not isinstance(x, bool) and x >= 0


def validate(means, variances, capacity, risk_squared):
    if (not means or len(means) != len(variances)
        or not all(exact_nonnegative(x) for x in (*means, *variances, capacity, risk_squared))
        or capacity <= 0 or risk_squared <= 0):
        raise ValueError('Use nonempty equal arrays and nonnegative exact coefficients; C,q>0.')


def fits(mean, variance, capacity, q):
    # The first comparison is essential. Squaring alone is not equivalent.
    return mean <= capacity and q*variance <= (capacity-mean)**2


def value(values, bits):
    return sum((a*b for a,b in zip(values,bits)), F(0))


def generator(means, variances, capacity, q):
    validate(means, variances, capacity, q)
    law = {(): (F(1), F(0), F(0))}
    for a,v in zip(means,variances):
        new = {}
        for bits,(prob,A,S) in law.items():
            if fits(A+a,S+v,capacity,q):
                new[bits+(0,)]=(prob/2,A,S)
                new[bits+(1,)]=(prob/2,A+a,S+v)
            else:
                new[bits+(0,)]=(prob,A,S)
        law=new
    return {bits:rec[0] for bits,rec in law.items()}


def main():
    # One illustrative coefficient set, not an acquired master dual or hard instance.
    means=[10,10,1]; variances=[1,4,1]; C=14; q=4
    prices=[F(1,2),F(3,4),F(3,5)]
    validate(means,variances,C,q)
    subsets=list(product((0,1),repeat=3))
    feasible={x for x in subsets if fits(value(means,x),value(variances,x),C,q)}
    law=generator(means,variances,C,q)
    assert set(law)==feasible and sum(law.values())==1
    assert all(p>0 for p in law.values())
    good={x for x in feasible if value(prices,x)>1}
    assert good=={(1,0,1)}
    pgood=sum((law[x] for x in good),F(0))
    assert pgood==F(1,4)
    # The two equal-mean partial solutions are both feasible, but retaining only
    # the larger profit loses the only improving feasible extension.
    assert fits(10,1,C,q) and fits(10,4,C,q) and prices[1]>prices[0]
    assert fits(11,2,C,q) and not fits(11,5,C,q)
    # Pooled risk is different from adding standalone safety buffers.
    assert fits(20,2,23,4)
    assert 2*(10+2)>23  # Individual variance-one, risk-multiplier-two buffers.
    assert not fits(20,2,21,4)  # Means alone would fit.
    # Correlation invalidates the diagonal-variance assumption, not the arithmetic.
    assert not fits(20,2+2*F(1),23,4)
    # Missing the nonnegative-headroom guard can admit an invalid set.
    assert 4*1 <= (10-12)**2 and not fits(12,1,10,4)
    assert fits(10,1,12,4)  # Exact equality is feasible.
    # Positive rounding guards acceptance, not absence of original feasible columns.
    rounded_feasible={x for x in subsets if fits(value([F(a)+F(1,100) for a in means],x),
        value([F(v)+F(1,100) for v in variances],x),C,q)}
    assert rounded_feasible <= feasible
    # Exact certificate used in the published hybrid pricing rule.
    restricted=F(100); old_lower=F(95); threshold=restricted/old_lower
    weak_score=F(103,100); strong_score=F(53,50)
    assert 1 < weak_score < threshold < strong_score
    possible_optima=[strong_score,strong_score+F(1,100),F(6,5)]
    for opt in possible_optima:
        assert restricted/opt <= restricted/strong_score <= old_lower
    # A validated upper bound below threshold itself improves the lower bound;
    # a missing witness is not evidence that this case holds.
    pricing_upper=F(26,25)
    assert 1 < pricing_upper < threshold
    assert restricted/pricing_upper > old_lower
    invalid=[lambda:validate([],[],1,1),lambda:validate([1],[1,2],1,1),
      lambda:validate([-1],[1],1,1),lambda:validate([1],[-1],1,1),
      lambda:validate([1],[1],0,1),lambda:validate([1],[1],1,float('nan'))]
    for fn in invalid:
        try: fn()
        except ValueError: continue
        raise AssertionError('Invalid input accepted')
    print(json.dumps({
      'status':'pass',
      'scope':'Exact small algebra only; no cloud trace, native solver, quantum circuit, runtime or speedup claim.',
      'small_generator':{'means':means,'variances':variances,'capacity':C,'risk_multiplier_squared':q,
        'subset_patterns_checked':len(subsets),'feasible_patterns':len(feasible),
        'probability_sum':str(sum(law.values())),'improving_pattern':list(next(iter(good))),
        'improving_probability':str(pgood),'uniform_feasible_probability':str(F(len(good),len(feasible))),
        'warning':'Illustrative prices, not a restricted-master trajectory or a useful hard case.'},
      'hybrid_threshold':{'restricted_master':str(restricted),'old_lower_bound':str(old_lower),
        'threshold':str(threshold),'positive_but_insufficient_score':str(weak_score),
        'sufficient_witness_score':str(strong_score),'bound_ceiling_from_witness':str(restricted/strong_score),
        'pricing_upper_below_threshold':str(pricing_upper),'improved_lower_bound':str(restricted/pricing_upper)},
      'checked_distinctions':['two resources vs mean-only DP','pooled vs per-item buffer',
        'positive covariance is not diagonal covariance','sign before squaring',
        'safe upward rounding is not absence certification','positive column vs bound-aware threshold'],
      'invalid_inputs_rejected':len(invalid),
      'not_run':['FPTAS/PTAS','non-convex relaxation','piecewise-linear branch-and-cut',
                 'column-generation benchmark','amplitude amplification','any historical scientific suite']
    },indent=2,sort_keys=True))

if __name__=='__main__': main()
