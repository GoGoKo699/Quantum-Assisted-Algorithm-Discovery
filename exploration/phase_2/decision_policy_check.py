"""Exact small controls for actionable information and simulator-only information.

No native experimental-design package, policy training, quantum hardware, or
quantum performance comparison. Standard-library fractions; no random tests.
All output files are created exclusively, not overwritten.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def compositions(total: int, length: int):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest


def tv(p, q):
    return sum((abs(a-b) for a,b in zip(p,q)), F(0))/2


def policy_value(p0, p1, policy):
    return sum((p0[y] if a == 0 else p1[y] for y,a in enumerate(policy)), F(0))/2


def binary_audit():
    distributions = [tuple(F(c,4) for c in counts) for counts in compositions(4,4)]
    policies = list(product((0,1), repeat=4))
    pairs = regrets = 0
    for p0 in distributions:
        for p1 in distributions:
            values = [policy_value(p0,p1,d) for d in policies]
            optimum = (1+tv(p0,p1))/2
            require(max(values) == optimum, 'Bayes/TV identity failed')
            bayes = tuple(int(p1[y] > p0[y]) for y in range(4))
            require(policy_value(p0,p1,bayes) == optimum, 'Bayes policy failed')
            for d,v in zip(policies,values):
                loss = sum((abs(p0[y]-p1[y]) for y in range(4) if d[y] != bayes[y]),F(0))/2
                require(optimum-v == loss, 'Weighted decision regret failed')
                regrets += 1
            # Append one independent nuisance bit; optimal value is unchanged.
            pp0 = tuple(p/2 for p in p0 for _ in range(2))
            pp1 = tuple(p/2 for p in p1 for _ in range(2))
            require(tv(pp0,pp1)==tv(p0,p1),'Independent answer augmentation failed')
            pairs += 1
    return dict(output_alphabet=4,probability_denominator=4,conditional_laws=len(distributions),
                model_pairs=pairs,policies_per_pair=len(policies),regret_checks=regrets,
                scope='Complete small rational family, not all probability models.')


def information_boundary():
    # H and R are fair; only Y=H XOR R is visible in the first experiment.
    # Global table is generated from an explicit four-tape process.
    joint = {(h,r,h^r):F(1,4) for h,r in product((0,1),repeat=2)}
    visible = [[sum((mass for (h,r,y),mass in joint.items() if h==hh and y==yy),F(0))
                for yy in range(2)] for hh in range(2)]
    p0,p1 = [tuple(2*x for x in row) for row in visible]
    value_visible=max(policy_value(p0,p1,d) for d in product((0,1),repeat=2))
    value_revealed=max(sum((mass*int(d[2*r+y]==h) for (h,r,y),mass in joint.items()),F(0))
                       for d in product((0,1),repeat=4))
    # Direct reversible generator preparations retain the random tape R.
    # Store rational basis probabilities instead of irrational 1/sqrt(2).
    support0={(r,r) for r in (0,1)}
    support1={(r,1^r) for r in (0,1)}
    overlap=F(len(support0 & support1),2)
    require(value_visible==F(1,2) and value_revealed==1 and overlap==0,'Information control failed')
    return dict(visible_answer='Y = H XOR R; R is not reported',
                visible_conditional_laws=[list(map(str,p0)),list(map(str,p1))],
                optimum_from_Y=str(value_visible),optimum_if_R_is_also_revealed=str(value_revealed),
                retained_randomness_state_overlap=str(overlap),
                scope='Revealing R changes the observation protocol. Orthogonal purifications do not make Y informative.')


def policy_compatibility():
    # Two observations, same Bayes value; exchanging outcome labels exchanges
    # the required decoder. A weak noisy channel is useful with the wrong fixed
    # decoder for the deterministic channel, illustrating the missing cost.
    channels={
        'copy': ((F(1),F(0)),(F(0),F(1))),
        'invert': ((F(0),F(1)),(F(1),F(0))),
        'noisy_copy': ((F(3,4),F(1,4)),(F(1,4),F(3,4)))
    }
    decoders={'return_y':(0,1),'return_not_y':(1,0),'always_zero':(0,0)}
    rows={name:{dname:str(policy_value(*ch,d)) for dname,d in decoders.items()} for name,ch in channels.items()}
    require(rows['invert']['return_y']=='0' and rows['invert']['return_not_y']=='1','Relabel control failed')
    return dict(values=rows,scope='Elementary classical decoder suffices; no learning hardness claimed.')


def sequential_policy_check():
    # Unknown H=(H0,H1). First exact observation is chosen coordinate H_b;
    # the next coordinate can depend on the first reported answer. A two-bit
    # target action predicts H0 XOR H1. We enumerate complete deterministic
    # design/action pairs and verify the posterior and forward-policy values.
    scenarios=list(product((0,1),repeat=2))
    count=0; max_value=F(0)
    for first in (0,1):
        for second in product((0,1),repeat=2):
            for decoder in product((0,1),repeat=4):
                forward=F(0); weighted_by_history={}
                for h in scenarios:
                    y0=h[first]; chosen=second[y0]; y1=h[chosen]
                    hist=(y0,y1)
                    payoff=int(decoder[2*y0+y1]==(h[0]^h[1]))
                    forward+=F(payoff,4)
                    weighted_by_history.setdefault(hist,[]).append((F(1,4),payoff))
                posterior=F(0)
                for entries in weighted_by_history.values():
                    prob=sum((p for p,_ in entries),F(0))
                    posterior+=prob*sum((p*reward/prob for p,reward in entries),F(0))
                require(forward==posterior,'Sequential policy expectation mismatch')
                count+=1; max_value=max(max_value,forward)
    require(max_value==1,'Complete two-bit observation policy failed')
    return dict(design_action_pairs=count,exact_forward_posterior_agreements=count,best_value=str(max_value),
                scope='Finite policy verification, not an adaptive-design benchmark.')


def paired_evaluation():
    # Two known policies evaluated on the same 256 possible simulated scenarios.
    # On four they disagree; on the other 252 their binary payoffs coincide.
    old=[0,0,0,1]+[0]*126+[1]*126
    new=[1,1,1,0]+[0]*126+[1]*126
    mean=lambda x:sum((F(v) for v in x),F(0))/len(x)
    variance=lambda x:mean([F(v)**2 for v in x])-mean(x)**2
    diff=[b-a for a,b in zip(old,new)]
    r=F(sum(a!=b for a,b in zip(old,new)),len(old))
    gap=mean(diff)
    vp=variance(diff); vi=variance(old)+variance(new)
    require(vp==r-gap**2 and gap==F(1,128),'Paired variance formula failed')
    return dict(scenarios=256,old_value=str(mean(old)),new_value=str(mean(new)),
                decision_value_gap=str(gap),payoff_disagreement_probability=str(r),
                paired_variance=str(vp),independent_variance=str(vi),variance_ratio=str(vi/vp),
                scope='Known finite table, exactly solvable. Variances are not measured runtime improvements.')


def run():
    return dict(scope='Exact decision-policy semantics and fair-information controls only; no quantum advantage.',
                binary=binary_audit(),accessible_information=information_boundary(),
                compatible_policy=policy_compatibility(),sequential=sequential_policy_check(),
                paired_comparison=paired_evaluation())


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise SystemExit('Refusing to overwrite existing evidence.')
    report=run()
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(report,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps(report,indent=2,sort_keys=True))
