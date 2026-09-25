"""Independent exact and optional-library comparisons; no quantum experiment."""
from __future__ import annotations
import argparse, hashlib, itertools, json, random, sys
from math import inf
from pathlib import Path
from branching import Graph, Node, SharingCore, ComponentBranching, UnsupportedRecurrence
from branching import Edge, arborescence
from core import exhaustive
from public_graph import load_graph, remove_direct_self_dependencies, verify_source

ROOT=Path(__file__).resolve().parent

def direct_fixed(graph, core, active):
    """Independent representative enumeration with all chosen core nodes required."""
    roots=tuple(sorted(active))
    g=Graph(graph.classes,roots)
    classes=sorted(g.reachable())
    best=inf; valid=0; tested=0
    for choices in itertools.product(*(g.classes[c] for c in classes)):
        tested+=1
        assignment={c:n.name for c,n in zip(classes,choices)}
        try:cost,used=g.check(assignment)
        except ValueError:continue
        if (set(used)&set(core))!=set(active):continue
        valid+=1;best=min(best,cost)
    return (None if best==inf else best),tested,valid


def brute_arborescence(n, edges):
    lists=[[e for e in edges if e.v==v and e.u!=v] for v in range(1,n)]
    best=inf; attempts=0
    for picked in itertools.product(*lists):
        attempts+=1
        reached={0}
        for _ in range(n):
            reached|={e.v for e in picked if e.u in reached}
        if len(reached)==n:best=min(best,sum(e.cost for e in picked))
    return (None if best==inf else best),attempts


def random_graph(rng,n,acyclic):
    names=[f'v{i}' for i in range(n)];cs={}
    for i,v in enumerate(names):
        choices=[]
        for j in range(rng.randint(1,3)):
            possible=names[:i] if acyclic else names
            children=tuple(rng.choice(possible) for _ in range(rng.randint(0,3))) if possible else ()
            choices.append(Node(f'{v}n{j}',rng.randrange(9),children))
        cs[v]=tuple(choices)
    roots=tuple(sorted(set([names[-1]]+[rng.choice(names) for _ in range(rng.randrange(3))])))
    return Graph(cs,roots)


def run(with_networkx=False):
    rng=random.Random(202609255)
    summary=dict(graphs=0,admitted=0,rejected=0,cyclic_admitted=0,infeasible_admitted=0,
                 direct_representative_assignments=0,fixed_activation_checks=0,
                 fixed_representative_assignments=0,scale_checks=0)
    digest=hashlib.sha256()
    for n in range(1,8):
        for acyclic in (True,False):
            for trial in range(55):
                g=random_graph(rng,n,acyclic)
                b=ComponentBranching(g); summary['graphs']+=1
                if not b.admitted:
                    summary['rejected']+=1
                    try:b.solve()
                    except UnsupportedRecurrence:pass
                    else:raise AssertionError('Unsupported graph not rejected.')
                    continue
                summary['admitted']+=1
                summary['cyclic_admitted']+=not g.support_acyclic()
                truth=exhaustive(g); found=b.solve()
                summary['direct_representative_assignments']+=truth['assignments']
                if found['cost']!=truth['cost']:
                    raise AssertionError(('Global mismatch',g.classes,g.roots,found,truth))
                summary['infeasible_admitted']+=found['cost'] is None
                digest.update(str(found['cost']).encode()+b'\n')
                optional=[c for c in b.core.core if c not in b.g.roots]
                masks=list(range(1<<len(optional)))
                if len(masks)>12:masks=sorted(set([0,masks[-1],*rng.sample(masks,10)]))
                for mask in masks:
                    active=set(b.g.roots)|{c for j,c in enumerate(optional) if mask>>j&1}
                    expected,tested,_=direct_fixed(b.g,b.core.core,active)
                    observed=b.evaluate(active)
                    summary['fixed_activation_checks']+=1
                    summary['fixed_representative_assignments']+=tested
                    if expected!=observed['charged']:
                        raise AssertionError(('Fixed-set mismatch',expected,observed,g.classes,active))
                if trial%11==0:
                    factor=1000003
                    scaled=Graph({c:tuple(Node(nd.name,nd.cost*factor,nd.children) for nd in ns)
                                  for c,ns in g.classes.items()},g.roots)
                    other=ComponentBranching(scaled);result=other.solve()
                    if not other.admitted or result['cost']!=(None if found['cost'] is None else found['cost']*factor):
                        raise AssertionError('Scale invariance failed.')
                    summary['scale_checks']+=1
    arc_summary=dict(graphs=0,brute_assignments=0,cyclic_contractions=0,networkx_checks=0,networkx_disagreements=[])
    if with_networkx:
        import networkx as nx
    for n in range(2,8):
        for trial in range(80):
            edges=[]
            for u in range(n):
                for v in range(1,n):
                    if u==v or rng.random()>.42:continue
                    for _ in range(1+int(rng.random()<.12)):
                        edges.append(Edge(u,v,rng.randrange(11),len(edges)))
            st={}; answer=arborescence(set(range(n)),0,edges,st)
            got=None if answer is None else sum(e.cost for e in answer)
            if answer is not None:
                expected,tested=brute_arborescence(n,edges)
                if got!=expected:raise AssertionError('Branching differs from brute-force.')
            else:
                expected,tested=brute_arborescence(n,edges)
                if expected is not None:raise AssertionError('False branching infeasibility.')
            arc_summary['graphs']+=1;arc_summary['brute_assignments']+=tested
            arc_summary['cyclic_contractions']+=st.get('contractions',0)
            if with_networkx:
                ng=nx.MultiDiGraph();ng.add_nodes_from(range(n))
                for e in edges:ng.add_edge(e.u,e.v,weight=e.cost)
                try:
                    tree=nx.minimum_spanning_arborescence(ng)
                    native=sum(d['weight'] for _,_,d in tree.edges(data=True))
                except nx.NetworkXException:native=None
                if native!=got:
                    arc_summary['networkx_disagreements'].append(dict(vertices=n,trial=trial,returned=native,exact=got,arcs=[(e.u,e.v,e.cost) for e in edges],witness=[(e.u,e.v,e.cost) for e in answer] if answer is not None else None))
                arc_summary['networkx_checks']+=1
    # A positive-cost recurrent SCC requiring an entry, not circular credit.
    cyc=Graph({'r':(Node('join',0,('a','b')),),
        'a':(Node('a_base',10),Node('a_from_b',1,('b',))),
        'b':(Node('b_base',10),Node('b_from_a',1,('a',)))},('r',))
    c=ComponentBranching(cyc);sol=c.solve()
    if sol['cost']!=11:raise AssertionError('Cycle-entry cost lost.')
    # Conjunctive recurrence cannot be converted to a choice of one parent.
    bad=Graph({'x':(Node('xyANDz',0,('y','z')),Node('xbase',10)),
       'y':(Node('ybase',1),Node('yx',0,('x',))),
       'z':(Node('zbase',1),Node('zx',0,('x',)))},('x','y','z'))
    rejected=ComponentBranching(bad)
    if rejected.admitted or exhaustive(bad)['cost']!=2:raise AssertionError('Conjunctive boundary check.')
    wrong=Graph({'x':(Node('xy',0,('y',)),Node('xz',0,('z',)),Node('xbase',10)),
                'y':bad.classes['y'],'z':bad.classes['z']},bad.roots)
    if ComponentBranching(wrong).solve()['cost']!=1:raise AssertionError('Counterexample changed.')
    # Earlier exponential price-catalog family stays implicit, not materialized.
    sys.path.insert(0,str(ROOT.parent/'price_spectrum_v1'))
    from spectrum import persistent_spectrum
    families=[]
    for n in (4,8,16,32):
        g=persistent_spectrum(n);b=ComponentBranching(g)
        choices=[set(g.roots),set(b.core.core),set(g.roots)|{f'b{i}' for i in range(n) if i%2==0}]
        answers=[]
        for active in choices:
            out=b.evaluate(active)
            expected=3**n-1+len(active-set(g.roots))
            if out['charged']!=expected:raise AssertionError('Independent family formula mismatch.')
            answers.append(dict(activated_optional=len(active-set(g.roots)),cost=out['charged']))
        families.append(dict(n=n,classes=len(g.classes),old_root_price_count=3**n,
            old_conditional_minima=2**n,implicit_table_peak=b.stats['maximum_table_size'],
            activations=answers,optimum=3**n-1,
            scope='Optimum from independent-component formula, not activation enumeration or a hardness claim.'))
    public=[]
    for prune in (False,True):
        g=load_graph()
        if prune:g=remove_direct_self_dependencies(g)
        b=ComponentBranching(g)
        item=dict(direct_self_pruning=prune,classes=len(b.g.classes),nodes=sum(map(len,b.g.classes.values())),
            core=len(b.core.core),mandatory_core=sorted(b.mandatory),component_sizes=sorted(map(len,b.components)),admitted=b.admitted,
            obstructions=b.obstructions)
        if b.admitted:
            solp=b.solve(); exact=exhaustive(remove_direct_self_dependencies(g))
            if solp['cost']!=exact['cost']:raise AssertionError('Public graph mismatch.')
            item.update(cost=solp['cost'],activation_calls=solp['activation_calls'],
                        direct_assignments=exact['assignments'],choices=solp['choices'])
        public.append(item)
    # A different classical parameterization must be kept in the comparator.
    from steiner_baseline import solve_unary
    srng=random.Random(20260925501)
    steiner=dict(graphs=0,representative_assignments=0)
    for n in range(1,9):
        for _ in range(45):
            names=[f'u{i}' for i in range(n)]
            classes={v:tuple(Node(f'{v}_{j}',srng.randrange(10),
                      (srng.choice(names),) if srng.random()<.7 else ())
                      for j in range(srng.randint(1,3))) for v in names}
            roots=tuple(sorted(srng.sample(names,srng.randint(1,min(4,n)))))
            g=Graph(classes,roots)
            expected=exhaustive(g)
            result=solve_unary(g)
            b=ComponentBranching(g)
            if not b.admitted or result['cost']!=expected['cost'] or b.solve()['cost']!=expected['cost']:
                raise AssertionError('Unary/Steiner equivalence failed.')
            steiner['graphs']+=1;steiner['representative_assignments']+=expected['assignments']
    return dict(finite=summary,decision_sha256=digest.hexdigest(),branchings=arc_summary,steiner=steiner,
        library=dict(networkx_version=nx.__version__ if with_networkx else None,
                     scope='Optional exact branching comparator; not a native e-graph extractor.'),
        cycle_example=dict(admitted=c.admitted,optimum=sol['cost'],certificate=sol['choices']),
        conjunctive_counterexample=dict(true_optimum=2,incorrect_OR_relaxation=1,
                                       obstruction=rejected.obstructions),
        implicit_families=families,public_source=verify_source(),public=public,
        claim='Exact specialized classical completion and standard quantum-search corollary. No practical advantage or novelty certification.')


if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not use -O/-OO.')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    p.add_argument('--networkx',action='store_true');a=p.parse_args()
    if a.output.exists():raise SystemExit('Refusing to overwrite evidence.')
    result=run(a.networkx);a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))
