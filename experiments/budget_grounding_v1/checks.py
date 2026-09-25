"""Independent finite checks for grounded-budget certificates.

Exhaustive comparisons are only on the finite explicitly enumerated instances.
Random structural graphs are not claims about semantic rewrite correctness.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, random, sys
from pathlib import Path
from math import comb, log2
from budget import Graph, Node, SharingCore, Grounding, exhaustive, allocations, unrank, rank_allocation
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'sharing_core_v1'))
import importlib.util
_spec=importlib.util.spec_from_file_location("previous_checks",Path(__file__).resolve().parents[1]/"sharing_core_v1"/"checks.py")
_previous=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_previous)
random_graph=_previous.random_graph


def all_local_vectors(g: Graph, core_order: tuple[str, ...]) -> tuple[list[tuple[int, ...]], int]:
    """Direct representative enumeration and owner accounting; no local-cost DP."""
    g=g.restrict_reachable()
    boundary=set(core_order)
    parents={c:set() for c in g.classes}
    for p, ns in g.classes.items():
        for n in ns:
            for c in n.children: parents[c].add(p)
    def owner(c):
        visited=set()
        while c not in boundary:
            if c in visited or len(parents[c]) != 1: raise AssertionError('Private owner error.')
            visited.add(c);c=next(iter(parents[c]))
        return c
    index={c:i for i,c in enumerate(core_order)}
    cs=sorted(g.classes)
    vectors=set();count=0
    for ns in itertools.product(*(g.classes[c] for c in cs)):
        count+=1
        chosen=dict(zip(cs,ns))
        try:cost,used=g.check({c:n.name for c,n in chosen.items()})
        except ValueError:continue
        local=[0]*len(core_order)
        for c in used: local[index[owner(c)]] += chosen[c].cost
        if sum(local)!=cost:raise AssertionError('Independent local partition mismatch.')
        vectors.add(tuple(local))
    return sorted(vectors),count


def run():
    h=hashlib.sha256();rng=random.Random(202609251)
    graphs=cyclic=infeasible=assignments=capchecks=budgetdecisions=accepted=0
    # 400 graphs, all allocations with total <= 4 on each graph.
    for n in range(1,6):
        for mode in (True,False):
            for _ in range(40):
                g=random_graph(rng,n,mode)
                # Include zero costs but keep the exhaustive cap range informative.
                g=Graph({c:tuple(Node(x.name,x.cost%4,x.children) for x in ns) for c,ns in g.classes.items()},g.roots)
                oracle=Grounding(g);s=len(oracle.core.core)
                vectors,nassign=all_local_vectors(g,oracle.core.core)
                dp=oracle.core.solve();brute=exhaustive(g)
                if dp['cost']!=brute['cost']:raise AssertionError('Historical DP discrepancy.')
                true_opt=min(map(sum,vectors),default=None)
                if true_opt!=brute['cost']:raise AssertionError('Owner cost optimum.')
                hits=[]
                for b in allocations(s,4):
                    expected=any(all(x<=y for x,y in zip(v,b)) for v in vectors)
                    result=oracle.close(b)
                    if result['success']!=expected:raise AssertionError(('cap failure',g,b,result,vectors))
                    if expected:
                        accepted+=1;hits.append(sum(b))
                        if result['cost']>sum(b):raise AssertionError('Overspent certificate.')
                    capchecks+=1;h.update(bytes([expected]))
                for k in range(5):
                    got=any(t<=k for t in hits)
                    if got != (true_opt is not None and true_opt<=k):raise AssertionError('Threshold decision.')
                    budgetdecisions+=1
                if dp['cost'] is not None:
                    b=oracle.caps_from_dp(dp);r=oracle.close(b)
                    if not r['success'] or r['cost']!=dp['cost']:raise AssertionError('Witness conversion.')
                graphs+=1;assignments+=nassign
                cyclic+=not g.support_acyclic();infeasible+=not vectors
    # Independently exercise all 2100 previously seeded graphs and their exact optima.
    witness_checks=0;rr=random.Random(20260925)
    for n in range(1,8):
        for mode in (True,False):
            for _ in range(150):
                g=random_graph(rr,n,mode);o=Grounding(g);dp=o.core.solve()
                if dp['cost'] is not None:
                    b=o.caps_from_dp(dp);r=o.close(b)
                    if not r['success'] or r['cost']!=dp['cost']:raise AssertionError('Larger witness conversion.')
                    witness_checks+=1
    ranks=0
    for s in range(7):
        for k in range(11):
            vectors=list(allocations(s,k))
            if len(vectors)!=comb(k+s,s):raise AssertionError('Composition count.')
            for j,b in enumerate(vectors):
                if unrank(s,k,j)!=b or rank_allocation(b,k)!=j:raise AssertionError('Rank mismatch.')
                ranks+=1
    big_tests=[]
    for s,k in [(12,10**6),(20,10**30),(3,2**256)]:
        m=comb(k+s,s)
        for rank in [0,1,m//2,m-1]:
            b=unrank(s,k,rank)
            if rank_allocation(b,k)!=rank:raise AssertionError('Binary-encoded large threshold test.')
        big_tests.append({'core':s,'threshold_bits':k.bit_length(),'rank_bits':(m-1).bit_length(),'checked_ranks':4})
    cycles=_previous.cyclic();c=Grounding(cycles)
    zero=c.close((0,)*len(c.core.core))
    repaired=c.decision(10)
    if zero['success'] or repaired['cost']!=10:raise AssertionError('Zero-cost cycle guard.')
    pure=Graph({'a':(Node('a',0,('b',)),),'b':(Node('b',0,('a',)),)},('a',))
    if Grounding(pure).close((1000,)*len(SharingCore(pure).core))['success']:
        raise AssertionError('Ungrounded pure cycle admitted.')
    # Public source calibration: transfer only an independently verified witness;
    # do NOT attempt the enormous budget enumeration.
    from public_graph import load_graph, remove_direct_self_dependencies, verify_source
    pg=remove_direct_self_dependencies(load_graph());po=Grounding(pg);ps=po.core.solve()
    caps=po.caps_from_dp(ps);pr=po.close(caps)
    if pr['cost']!=1205:raise AssertionError('Public reconstruction.')
    counter=[]
    for s,k in [(20,2),(40,10),(80,20),(40,40),(40,80),(len(caps),1205)]:
        m=comb(k+s,s)
        counter.append({'s':s,'K':k,'allocations':m,'log2_allocations':round(log2(m),6),
                        'log2_sqrt_allocations':round(log2(m)/2,6),
                        'note':'Search-domain counts, not lower bounds or runtime estimates.'})
    return {
        'finite_cap_checks':{'graphs':graphs,'cyclic_graphs':cyclic,'infeasible_graphs':infeasible,
          'exhaustive_assignments':assignments,'cap_vectors':capchecks,'accepted_cap_vectors':accepted,
          'threshold_decisions':budgetdecisions,'decisions_sha256':h.hexdigest()},
        'previous_graph_witness_transfer':{'graphs':2100,'feasible_witnesses_verified':witness_checks},
        'ranking':{'exhaustive_rank_roundtrips':ranks,'large_binary_thresholds':big_tests},
        'cycles':{'zero_caps_accepted':zero['success'],'grounded_optimum':repaired,'ungrounded_cycle_rejected':True},
        'public_calibration':{'source':verify_source(),'core':list(po.core.core),'budget_vector':list(caps),
          'sum_caps':sum(caps),'cost':pr['cost'],'grounding_rounds':pr['rounds'],'choices':pr['choices'],
          'allocation_count':comb(1205+len(caps),len(caps)),
          'scope':'Witness reconstruction only; allocation enumeration not run; not a hard workload.'},
        'domain_counts':counter,
        'claims_not_established':['novelty','best_classical_separation','large_native_benchmark','useful_quantum_advantage','compiled_physical_resources']
    }

if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not use -O or -OO.')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():raise SystemExit('Output exists; refusing overwrite.')
    report=run();args.output.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['finite_cap_checks','previous_graph_witness_transfer','ranking']},indent=2))
