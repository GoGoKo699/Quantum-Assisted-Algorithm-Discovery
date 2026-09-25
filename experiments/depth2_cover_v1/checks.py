"""Independent finite validation: enumerate full tiny circuits, not helper sets."""
from __future__ import annotations
from itertools import product
import argparse,hashlib,json
from pathlib import Path
from cover import make_model,exact_cover,minimize_masks,signed_weight
from layered import search
from run_screen import compute,summary,verify_general


def independent_node(a,b,B):
    """Both operands independently shifted; do not call the synthesis operation."""
    possible=set()
    for p,q in product(range(B+1),repeat=2):
        for sign in (-1,1):
            value=abs(a*(2**p)+sign*b*(2**q))
            if not value:continue
            while value%2==0:value//=2
            if value<2**B:possible.add(value)
    return possible


def tiny_check():
    B=4;universe=tuple(range(3,2**B,2))
    options={(a,b):independent_node(a,b,B) for a,b in product((1,)+universe,repeat=2)}
    state_counts={};decisions=[]
    for D in (1,2,3):
        states={((1,0),)};by_budget=[states]
        for g in range(1,4):
            new=set(states) # at most g gates
            for state in states:
                existing=dict(state)
                for (a,da),(b,db) in product(state,repeat=2):
                    depth=1+max(da,db)
                    if depth>D:continue
                    for c in options[a,b]:
                        if existing.get(c,D+1)<=depth:continue
                        modified=dict(existing);modified[c]=depth
                        new.add(tuple(sorted(modified.items())))
            states=new;by_budget.append(states)
        state_counts[str(D)]=[len(s) for s in by_budget]
        for mask in range(1<<len(universe)):
            targets=tuple(t for i,t in enumerate(universe) if mask>>i&1)
            for gates in range(4):
                expected=any(set(targets)<=set(dict(state)) for state in by_budget[gates])
                actual=False if len(targets)>gates else search(targets,B,D,gates-len(targets))['feasible']
                if actual!=expected:raise AssertionError(('tiny circuit mismatch',D,targets,gates))
                decisions.append(int(actual))
    # Independent all-subset check of complete inclusion-minimal portfolios.
    subsets_checked=0
    for target_mask in range(1<<len(universe)):
        targets=tuple(t for i,t in enumerate(universe) if target_mask>>i&1)
        model=make_model(targets,B);answer=exact_cover(model['requirements'])
        successes=[]
        for mask in range(1<<len(model['helpers'])):
            selected={h for i,h in enumerate(model['helpers']) if mask>>i&1}
            first={1}|set(model['mandatory'])|selected
            available=set(first)
            for a,b in product(first,repeat=2):available.update(options[a,b])
            good=set(targets)<=available
            if good:successes.append(mask)
            subsets_checked+=1
        minimal=minimize_masks(successes)
        if tuple(answer['portfolios'])!=minimal:raise AssertionError('Antichain portfolio mismatch.')
    return dict(layered_states_by_budget=state_counts,layered_decisions=len(decisions),
                decision_sha256=hashlib.sha256(bytes(decisions)).hexdigest(),
                target_families=128,helper_subsets_checked=subsets_checked)


def data_test(nodes,coefficients,B,D):
    targets={abs(c)//(abs(c)&-abs(c)) for c in coefficients if c}-{1}
    verify_general(nodes,targets,B,D)
    fundamentals=[1]+[r['value'] for r in nodes];positions={v:i for i,v in enumerate(fundamentals)}
    restore=[]
    for c in sorted(set(coefficients)):
        if c:
            a=abs(c);power=(a&-a).bit_length()-1
            restore.append((positions[a>>power],power,1 if c>0 else -1,c))
    # This evaluates both the network and original signed/even coefficient bank.
    for x in range(-(1<<7),1<<8):
        values=[x]
        for r in nodes:
            num=((values[r['left']]<<r['shift'])+r['sign']*values[r['right']])*r['output_sign']
            den=1<<r['right_shift']
            if num%den:raise AssertionError('Inexact shift.')
            value=num//den
            if value!=r['value']*x:raise AssertionError('Data-level intermediate mismatch.')
            values.append(value)
        for index,power,sgn,c in restore:
            if (values[index]<<power)*sgn!=c*x:raise AssertionError('Original coefficient output mismatch.')
    return 384


def run():
    tiny=tiny_check();screen=compute();certificates=0;input_runs=0
    for bank in screen['banks']:
        for trial in bank['depth_trials']:
            if trial['feasible']:
                input_runs+=data_test(trial['certificate'],bank['coefficients'],bank['B'],trial['depth_bound'])
                certificates+=1
        for trial in bank['count_trials']:
            if trial['feasible']:
                verify_general(trial['certificate'],bank['targets'],bank['B'],trial['nodes'])
        # Independently require the weight lower bound be attained by a certificate.
        depth_bound=max((signed_weight(t)-1).bit_length() for t in bank['targets'])
        if depth_bound!=bank['minimum_depth']:raise AssertionError('Depth bound mismatch.')
    raw=json.dumps(screen,indent=2,sort_keys=True)+'\n'
    return dict(tiny=tiny,screen_sha256=hashlib.sha256(raw.encode()).hexdigest(),
                summary=summary(screen),pareto_certificates=certificates,
                signed_input_runs=input_runs,inputs_per_certificate=384)


if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not use Python -O/-OO.')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():raise SystemExit('Refusing to overwrite evidence.')
    result=run();args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='summary'},indent=2))
