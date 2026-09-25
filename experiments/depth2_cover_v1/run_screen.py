"""Regenerate the complete 11-bank count/depth screen and exact certificates."""
import argparse,hashlib,json,time
from pathlib import Path
from cover import odd,signed_weight,solve_bank,make_model,make_certificate,exact_cover
from layered import search,closure
ROOT=Path(__file__).resolve().parent
def banks():
    data=json.loads((ROOT/'banks.json').read_text())
    if len(data['banks'])!=11:raise AssertionError('Unexpected bank count.')
    for bank in data['banks']:
        coefficients=bank['coefficients'];B=bank['B']
        if coefficients!=sorted(set(coefficients)):raise AssertionError('Noncanonical coefficient list.')
        if B!=max(abs(c).bit_length() for c in coefficients)+1:raise AssertionError('Changed coefficient-bound rule.')
        yield bank['name'],coefficients,B


def verify_general(nodes,targets,B,D):
    values=[1];depths=[0]
    for index,row in enumerate(nodes,1):
        a,b,s,sgn,t,osign=(row['left'],row['right'],row['shift'],row['sign'],row['right_shift'],row['output_sign'])
        if not(0<=a<index and 0<=b<index and 0<=s<=B and 0<=t<=B):raise AssertionError('Malformed operation.')
        if sgn not in (-1,1) or osign not in (-1,1):raise AssertionError('Malformed sign.')
        raw=((values[a]<<s)+sgn*values[b])*osign
        c=row['value']
        if not(0<c<1<<B and c%2 and raw==c*(1<<t)):raise AssertionError('Incorrect exact operation.')
        values.append(c);depths.append(1+max(depths[a],depths[b]))
    if not set(targets)<=set(values) or max(depths)>D:raise AssertionError('Output/depth violation.')
    return max(depths)


def compute():
    results=[]
    for name,coeffs,B in banks():
        targets=sorted({odd(c) for c in coeffs}-{0,1});d=len(targets)
        weights={str(c):signed_weight(c) for c in targets}
        minimum_depth=(max(weights.values(),default=1)-1).bit_length()
        # A g-operation DAG never requires depth above g. Thus D=d+k
        # gives a complete at-most-(d+k)-operation search in this model.
        count_trials=[]
        for k in range(7):
            trial=search(coeffs,B,d+k,k);count_trials.append(trial)
            if trial['feasible']:break
        else:raise RuntimeError('Screen budget exhausted; not an impossibility result.')
        min_nodes=trial['nodes'];min_helpers=min_nodes-d
        depth_two=solve_bank(coeffs,B)
        depth_trials=[]
        for D in range(minimum_depth,min_nodes+1):
            if D==2:
                trial=dict(depth_bound=D,method='two-layer antichain',feasible=depth_two['status']=='feasible')
                if trial['feasible']:
                    trial.update(nodes=depth_two['minimum_operations'],helpers=depth_two['minimum_portfolios'][0],
                                 certificate=depth_two['certificate'])
                depth_trials.append(trial)
            else:
                attempts=[]
                for k in range(7):
                    candidate=search(coeffs,B,D,k);attempts.append(candidate)
                    if candidate['feasible']:break
                else:raise RuntimeError('Depth-constrained screen budget exhausted.')
                trial=dict(depth_bound=D,method='layered helper search',feasible=True,nodes=candidate['nodes'],
                           helpers=candidate['helpers'],certificate=candidate['certificate'],trials=attempts)
                depth_trials.append(trial)
            if trial['feasible'] and trial['nodes']==min_nodes:break
        points=[]
        for trial in depth_trials:
            if not trial['feasible']:continue
            verify_general(trial['certificate'],targets,B,trial['depth_bound'])
            if not points or trial['nodes']<points[-1][0]:points.append([trial['nodes'],trial['depth_bound']])
        # Every reported minimum depth attains the independent signed-weight bound.
        if not points or points[0][1]!=minimum_depth:raise AssertionError('Depth lower bound not attained.')
        results.append(dict(name=name,B=B,coefficients=coeffs,targets=targets,signed_weights=weights,
                            minimum_depth=minimum_depth,minimum_operations=min_nodes,
                            count_trials=count_trials,depth_two=depth_two,depth_trials=depth_trials,
                            pareto_points=sorted(points)))
    return dict(schema=1,scope='Bounded positive-odd shift-add model; no mapped hardware or quantum advantage.',banks=results)


def summary(result):
    return [dict(name=r['name'],B=r['B'],outputs=len(r['targets']),pareto=r['pareto_points'],
                 minimum_depth=r['minimum_depth'],minimum_operations=r['minimum_operations'],
                 two_layer_status=r['depth_two']['status'],
                 largest_cover_frontier=max(r['depth_two']['frontier_sizes']),
                 cover_unions=r['depth_two']['union_operations']) for r in result['banks']]


if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not run with Python -O/-OO.')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():raise SystemExit('Refusing to overwrite output.')
    start=time.perf_counter();result=compute();elapsed=time.perf_counter()-start
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary(result),indent=2));print(f'Observed computation time: {elapsed:.6f} s (not a reproducibility fixture).')
