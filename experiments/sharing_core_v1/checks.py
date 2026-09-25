"""Finite corroboration, real-source greedy calibration, and theorem guard tests."""
import argparse, hashlib, itertools, json, random, time
from pathlib import Path
from types import SimpleNamespace
from core import Graph, Node, SharingCore, exhaustive
from public_graph import load_graph, verify_source, remove_direct_self_dependencies
from vendor.greedy_core import FasterGreedyDagExtractor

def run_greedy(g):
    ids={c:i for i,c in enumerate(g.classes)}; rev={v:k for k,v in ids.items()}
    ns={}; costs={}; names={}
    for c,nodes in g.classes.items():
        for n in nodes:
            i=len(ns); names[i]=n.name; costs[i]=n.cost
            ns[i]=SimpleNamespace(belong_eclass_id=ids[c], eclass_id=[ids[x] for x in n.children])
    result,_=FasterGreedyDagExtractor().extract(costs, ns)
    selected={rev[c]:names[n] for c,n in result.choices.items()}
    cost, used=g.check(selected)
    return {'cost':cost,'choices':used}

def coupled():
    return Graph({'a':(Node('a',0),),'b':(Node('b',0),),
      'h':(Node('xor',5,('a','b')),),
      'u':(Node('u_direct',4,('a','b')),Node('u_shared',1,('h','a'))),
      'v':(Node('v_direct',4,('a','b')),Node('v_shared',1,('h','b')))},('u','v'))

def cyclic():
    return Graph({'r':(Node('rAB',0,('A','B')),),
                  'A':(Node('AfromB',0,('B',)),Node('Aleaf',10)),
                  'B':(Node('BfromA',0,('A',)),Node('Bleaf',10))},('r',))

def random_graph(rng,n,acyclic):
    classes={}
    for i in range(n):
        ns=[]
        for j in range(rng.randint(1,3)):
            choices=list(range(i)) if acyclic else list(range(n))
            children=tuple(str(rng.choice(choices)) for _ in range(rng.randint(0,2))) if choices else ()
            ns.append(Node(f'{i}:{j}',rng.randrange(7),children))
        classes[str(i)]=tuple(ns)
    roots=tuple(dict.fromkeys([str(n-1),str(rng.randrange(n))]))
    return Graph(classes,roots)

def main(outdir):
    rng=random.Random(20260925)
    cases=0; assignments=0; has_cycles=0; infeasible=0; acyclic_cases=0
    dp_states=0; maxcore=0; checks_digest=hashlib.sha256()
    for n in range(1,8):
        for mode in (True,False):
            for _ in range(150):
                g=random_graph(rng,n,mode); core=SharingCore(g)
                exact=exhaustive(g); reduced=core.solve()
                if reduced['cost']!=exact['cost']:
                    raise AssertionError(('DP vs brute mismatch',g.classes,g.roots,reduced,exact))
                ac=g.support_acyclic()
                if ac:
                    act=core.solve_acyclic()
                    if act['cost']!=exact['cost']:raise AssertionError('Activation mismatch')
                    acyclic_cases+=1
                else: has_cycles+=1
                cases+=1; assignments+=exact['assignments'];infeasible+=exact['cost'] is None
                dp_states+=reduced['dp_states'];maxcore=max(maxcore,len(core.core))
                checks_digest.update(json.dumps([n,mode,g.roots,reduced['cost'],core.core],sort_keys=True).encode())
    c=coupled(); cs=SharingCore(c)
    if cs.solve()['cost'] != 7 or exhaustive(c)['cost'] != 7: raise AssertionError('Coupling check')
    cg=run_greedy(c)
    cy=cyclic(); cycore=SharingCore(cy)
    good=cycore.solve()['cost']; bad=sum(cycore.local((1<<len(cycore.core))-1)[0])
    if (good,bad)!=(10,0):raise AssertionError('Cycle guard example changed')
    try:cycore.solve_acyclic()
    except ValueError:pass
    else:raise AssertionError('Cyclic activation accepted')
    source=verify_source(); public=load_graph(); pruned=remove_direct_self_dependencies(public)
    observations=[]
    t=time.perf_counter(); pg=run_greedy(public);observations.append({'name':'upstream_greedy_core_original_graph','seconds':time.perf_counter()-t})
    t=time.perf_counter(); pr=SharingCore(pruned).solve();observations.append({'name':'sharing_core_DP_pruned_graph','seconds':time.perf_counter()-t})
    t=time.perf_counter(); pe=exhaustive(pruned);observations.append({'name':'exhaustive_pruned_graph','seconds':time.perf_counter()-t})
    pa=SharingCore(pruned).solve_acyclic()
    if len(set([pg['cost'],pr['cost'],pe['cost'],pa['cost']])) !=1:raise AssertionError('Public costs mismatch')
    report={'random_structural_tests':{'graphs':cases,'brute_force_assignments':assignments,
             'acyclic_graphs':acyclic_cases,'cyclic_graphs':has_cycles,'infeasible_graphs':infeasible,
             'DP_states':dp_states,'largest_core':maxcore,'outcome_sha256':checks_digest.hexdigest()},
       'coupled_toy':{'exact':cs.solve()['cost'],'upstream_greedy_core':cg['cost'],
                      'scope':'Illustrative weights; not a real performance improvement.'},
       'cycle_obstruction':{'correct_optimum':good,'invalid_activation_value':bad},
       'public_calibration':{'source':source,'nodes':sum(map(len,public.classes.values())),
          'classes':len(public.classes),'reachable_classes_before_pruning':len(public.reachable()),
          'pruned_nodes':sum(map(len,pruned.classes.values())),'pruned_classes':len(pruned.classes),
          'pruned_support_acyclic':pruned.support_acyclic(),'core':pr['core'],'optional_core':pa['optional_core'],
          'exhaustive_assignments_after_pruning':pe['assignments'],'DP_states':pr['dp_states'],
          'greedy_cost_scaled1000':pg['cost'],'exact_cost_scaled1000':pr['cost'],
          'exact_choices':pr['choices'],'greedy_choices':pg['choices'],
          'scope':'Original source greedy core with a separate input adapter; not full optimized SmoothE, e-boost or a hard case.'},
       'claims_not_established':['novelty','useful_quantum_advantage','physical_speedup','large_native_extractor_comparison']}
    outdir.mkdir(parents=True,exist_ok=False)
    (outdir/'results.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    (outdir/'observations.json').write_text(json.dumps(observations,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not use -O/-OO.')
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();main(a.output_dir)
