#!/usr/bin/env python3
"""Exact controls for circuit-native bin-packing pricing.

Python 3.10+, standard library only. This is finite algebra, not an industrial
pricing run, a decomposed quantum circuit, or a speed benchmark. No file writes.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
import json
import sys

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')


def valid(weights, profits, capacity):
    if (not isinstance(capacity, int) or isinstance(capacity, bool) or capacity <= 0
        or not weights or len(weights) != len(profits)):
        raise ValueError('Positive integer capacity and equal nonempty arrays required.')
    if any(not isinstance(a, int) or isinstance(a, bool) or a <= 0 for a in weights):
        raise ValueError('Positive integer item sizes required.')
    if any(not isinstance(p, (int,F)) or isinstance(p,bool) or p < 0 for p in profits):
        raise ValueError('Nonnegative exact profits required.')


def all_feasible(weights, capacity):
    return [x for x in product((0,1), repeat=len(weights))
            if sum(a*b for a,b in zip(weights,x)) <= capacity]


def value(profits, x):
    return sum((p*b for p,b in zip(profits,x)), F(0))


def tree_law(weights, capacity):
    """The fair feasible-prefix generator's exact probabilities, not uniform leaves."""
    states = {((), capacity): F(1)}
    for a in weights:
        new = {}
        for (prefix,remaining),prob in states.items():
            if a <= remaining:
                new[(prefix+(0,), remaining)] = prob/2
                new[(prefix+(1,), remaining-a)] = prob/2
            else:
                new[(prefix+(0,), remaining)] = prob
        states = new
    return {x:p for (x,_),p in states.items()}


def fractional_bound(weights, profits, capacity):
    """A classical fractional knapsack bound, with exact break multiplier."""
    order=sorted(range(len(weights)),key=lambda i:(-F(profits[i])/weights[i],i))
    remaining=F(capacity); frac=[F(0)]*len(weights); lam=F(0)
    for i in order:
        if remaining <= 0:
            # The previously selected item's multiplier is a valid minimizer.
            break
        frac[i]=min(F(1),remaining/weights[i]); remaining-=frac[i]*weights[i]
        lam=F(profits[i])/weights[i]
        if frac[i] < 1: break
    if sum(weights) <= capacity: lam=F(0)
    upper=lam*capacity+sum((max(F(0),p-lam*a) for a,p in zip(weights,profits)),F(0))
    assert upper == value(profits,frac)
    return upper,lam,frac


def core(weights,profits,capacity,threshold):
    upper,lam,frac=fractional_bound(weights,profits,capacity)
    if upper <= threshold: return upper,lam,{},True
    gap=upper-threshold
    fixed={i:int(p-lam*a > 0) for i,(a,p) in enumerate(zip(weights,profits))
           if abs(p-lam*a)>gap}
    return upper,lam,fixed,False


def main():
    # Three finite logic controls. None is proposed as a difficult workload.
    jobs=[([6,5,4,3,2,1,7,8],list(map(F,['.9','.3','.25','.2','.15','.05','.01','.01'])),10,F(1)),
          ([4,4,3],list(map(F,['.4','.4','.25'])),7,F(1)),
          ([2,3,4],list(map(F,['.3','.4','.5'])),10,F(1))]
    rows=[]; identities=0; core_checks=0
    for weights,profits,capacity,threshold in jobs:
        valid(weights,profits,capacity)
        feasible=all_feasible(weights,capacity); law=tree_law(weights,capacity)
        assert set(law)==set(feasible) and sum(law.values())==1
        upper,lam,fixed,excluded=core(weights,profits,capacity,threshold)
        good=[x for x in feasible if value(profits,x)>threshold]
        assert not excluded or not good
        for x in feasible:
            residual=lam*(capacity-sum(a*b for a,b in zip(weights,x)))
            residual+=sum((max(F(0),p-lam*a)*(1-b)+max(F(0),lam*a-p)*b
                           for a,p,b in zip(weights,profits,x)),F(0))
            assert upper-value(profits,x)==residual and residual>=0
            identities+=1
        for x in good:
            assert all(x[i]==b for i,b in fixed.items()); core_checks+=1
        pgood=sum((law[x] for x in good),F(0))
        maxval=max(value(profits,x) for x in feasible)
        pbest=sum((law[x] for x in feasible if value(profits,x)==maxval),F(0))
        # Correct marked mass is generally not number marked / number feasible.
        rows.append({'items':len(weights),'capacity':capacity,'threshold':str(threshold),
          'feasible_patterns':len(feasible),'fractional_upper_bound':str(upper),
          'certified_fixed_bits':{str(i):b for i,b in fixed.items()},
          'improving_patterns':len(good),'improving_probability':str(pgood),
          'uniform_feasible_probability':str(F(len(good),len(feasible))),
          'best_pattern_probability':str(pbest),'best_value':str(maxval),
          'classical_bound_proves_no_improvement':excluded})
    # Restrict the generator AFTER ordinary fixing; no access table is required.
    weights,profits,capacity,tau=jobs[0]
    U,lam,fixed,_=core(weights,profits,capacity,tau)
    rest=[i for i in range(len(weights)) if i not in fixed]
    cap=capacity-sum(weights[i]*b for i,b in fixed.items())
    forcedval=sum((profits[i]*b for i,b in fixed.items()),F(0))
    short=tree_law([weights[i] for i in rest],cap)
    pcore=sum((p for x,p in short.items() if forcedval+value([profits[i] for i in rest],x)>tau),F(0))
    assert pcore>0
    assert rows[0]['improving_probability'] != rows[0]['uniform_feasible_probability']
    # No-amplification state is NOT uniformly distributed over its feasible outputs.
    tiny=tree_law([2,2],2)
    assert tiny=={(0,0):F(1,4),(0,1):F(1,4),(1,0):F(1,2)}
    # Counter overflow can falsely reject the very pattern that should be marked.
    vals=[3,3]; denominator=4; selected=(1,1)
    assert value(vals,selected)>denominator and int(value(vals,selected))%4<=denominator
    # A tighter acceptance margin changes the task and cannot certify no improvement.
    at_one=sum((p for x,p in tiny.items() if value([F(21,20),F(21,20)],x)>1),F(0))
    at_margin=sum((p for x,p in tiny.items() if value([F(21,20),F(21,20)],x)>F(11,10)),F(0))
    assert at_one>0 and at_margin==0
    # An approximation guarantee with a real improvement margin suffices classically.
    # This checks its algebra, not an implementation of an FPTAS.
    margin_checks=[]
    for eta in (F(1,100),F(1,10),F(1,2)):
        zeta=eta/(2*(1+eta))
        lower=(1-zeta)*(1+eta)
        assert lower==1+eta/2 and lower>1
        margin_checks.append({'improvement_margin':str(eta),'relative_approximation_error':str(zeta),
                              'guaranteed_return_score':str(lower)})
    # Scaling the dual with ANY valid pricing upper bound gives full feasibility.
    scaled_checks=0
    for weights,profits,capacity,tau in jobs:
        upper,_,_=fractional_bound(weights,profits,capacity)
        alpha=max(F(1),upper)
        for x in all_feasible(weights,capacity):
            assert value(profits,x)/alpha<=1
            scaled_checks+=1
    # Fractional upper bound and a feasible output are distinct certificates.
    bad=[lambda:valid([],[],1),lambda:valid([0],[F(1)],2),
         lambda:valid([1],[F(-1)],2),lambda:valid([1],[F(1)],0),
         lambda:valid([1,2],[F(1)],3),lambda:valid([1],[float('nan')],2)]
    for test in bad:
        try:test()
        except ValueError:continue
        raise AssertionError('Invalid input accepted.')
    print(json.dumps({'status':'pass','scope':'Exact finite arithmetic only; no real pricing workload, quantum circuit compilation, amplitude amplification, or runtime comparison.',
      'jobs':rows,'reduced_cost_identities_checked':identities,'improving_columns_preserved_checks':core_checks,
      'core_control':{'free_items':len(rest),'residual_capacity':cap,'probability_of_improvement':str(pcore)},
      'negative_controls':['feasible generator is not uniform','profit register cannot wrap','margin failure is not no-column certificate'],
      'approximation_margin_controls':margin_checks,'scaled_dual_constraints_checked':scaled_checks,
      'invalid_inputs_rejected':len(bad),'external_code_or_data_used':False},indent=2,sort_keys=True))

if __name__=='__main__':main()
