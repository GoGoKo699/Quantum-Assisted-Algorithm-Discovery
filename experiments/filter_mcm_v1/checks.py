"""Independent finite checks and certificate audit. Outputs contain no timings."""
import itertools,json,sys
from pathlib import Path
from mcm_smt import odd,instance,certificate
from shift_closure import close,options
from depth_probe import validate,layers
ROOT=Path(__file__).resolve().parent

def independent_extensions(state,B):
    # Two independently shifted signed operands; normalize only exact powers of two.
    answer=set()
    for a,b in itertools.product(state,repeat=2):
        for p,q in itertools.product(range(B+1),repeat=2):
            for sign in (-1,1):
                value=abs((a<<p)+sign*(b<<q))
                if not value:continue
                while not value%2:value//=2
                if value<(1<<B):answer.add(value)
    return answer

def tiny(solver=False):
    B=4;levels=[{frozenset({1})}]
    for k in range(2):
        levels.append({s|{v} for s in levels[-1] for v in independent_extensions(s,B)})
    universe=list(range(3,1<<B,2));calls=0;statuses={'sat':0,'unsat':0}
    from hashlib import sha256
    outcome=[]
    if solver:from smt_native import solve
    for mask in range(1<<len(universe)):
        ts=[t for i,t in enumerate(universe) if (mask>>i)&1]
        for k in range(3):
            expected=any(set(ts)<=state for state in levels[k])
            outcome.append(int(expected))
            if solver:
                result=solve(instance(ts,k,B),2000);calls+=1
                if result['status']=='unknown':raise AssertionError('Tiny SMT query returned unknown.')
                if (result['status']=='sat')!=expected:raise AssertionError((ts,k,result))
                statuses[result['status']]+=1
                if expected:validate(certificate(result['model'],k,ts,B),ts,B)
    return dict(states_by_budget=[len(x) for x in levels],target_sets=128,decisions=384,
                answer_sha256=sha256(bytes(outcome)).hexdigest(),solver_queries=calls,
                solver_statuses=statuses if solver else None)

def audit(solver=False):
    data=json.loads((ROOT/'published_coefficients.json').read_text()); bank_results=[]
    for case in data['cases']:
        ts=[x for row in case['matrix'] for x in row];B=max(abs(x).bit_length() for x in ts)+1
        rows,missing=close(ts,B)
        validate(rows,[r['value'] for r in rows],B)
        bank_results.append(dict(name=case['name'],B=B,nontrivial_odd_targets=sorted(set(map(odd,ts))-{0,1}),
                                 target_closure_certificate=rows,missing=missing))
    obs=json.loads((ROOT/'cases_observations.json').read_text());sat=0
    for record in obs:
        if record['status']=='sat':
            ts=sorted(set(map(odd,record['targets']))-{0,1})
            rows=record['certificate']
            if len(rows)!=record['k']:raise AssertionError('Stored node count differs.')
            validate(rows,ts,record['B']);sat+=1
    result=json.loads((ROOT/'depth_results.json').read_text());ts=result['targets']
    # For a 12-operation circuit all operation outputs must be the 12 targets.
    # Every first-layer target is <= 65. For s>=1 odd operands give odd output,
    # so no right division: 2**s*a <= 303+65=368 and s<=8. At s=0 the
    # normalized magnitude is <=65, excluding 303. Thus this finite check
    # excludes depth 2 even without the empirical B=10 coefficient bound.
    first={1}|(set(ts)&independent_extensions({1},10))
    if first!={1,5,7,31,63,65}:raise AssertionError('Unexpected first layer.')
    if any(c==303 for a,b in itertools.product(first,repeat=2) for c,*_ in options(a,b,10)):
        raise AssertionError('The depth-two lower-bound obstruction disappeared.')
    # Direct 303 construction with the helper, independently of schedule generation.
    if 15*16+63!=303:raise AssertionError('Witness error.')
    for key in ('target_only_certificate','one_helper_certificate'):
        validate(result[key],ts,10)
    return dict(tiny_model=tiny(solver),banks=bank_results,stored_sat_certificates_checked=sat,
                depth_obstruction=dict(target=303,first_layer=sorted(first),maximum_shift_to_check=8),
                scope='Exact algebra and small-model decisions, not a current best-solver or hardware benchmark.')

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--solver',action='store_true');p.add_argument('--output',required=True)
    args=p.parse_args()
    if not __debug__:raise SystemExit('Do not use -O/-OO.')
    if Path(args.output).exists():raise SystemExit('Refusing to overwrite output.')
    r=audit(args.solver);Path(args.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='banks'},indent=2))
