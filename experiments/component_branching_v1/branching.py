"""Exact SCC-local arborescence completion for single-recurrent-boundary graphs.

Original adapter/reduction; the minimum-arborescence algorithm is standard
Chu--Liu/Edmonds cycle contraction, not a new algorithm. Exact integer costs.
No local price catalogs, numerical-budget enumeration, QRAM or quantum run.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from math import inf
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'sharing_core_v1'))
from core import Graph, Node, SharingCore


class UnsupportedRecurrence(ValueError):
    """The graph fails this sufficient condition, not necessarily infeasible."""


@dataclass(frozen=True)
class Edge:
    u: int
    v: int
    cost: int
    label: int
    payload: object = None
    previous: object = None


def arborescence(vertices, root, edges, stats=None):
    """Return an optimum root-spanning out-arborescence, or None.

    One cycle is contracted per recursive call; every contracted edge stores
    its immediate precursor. Worst case polynomial O(V E), with integer
    arithmetic and polynomial space. Parallel edges and zero costs permitted.
    """
    vertices = set(vertices)
    if root not in vertices:
        raise ValueError('Root must be a vertex.')
    if any(e.u not in vertices or e.v not in vertices or type(e.cost) is not int for e in edges):
        raise ValueError('Invalid endpoints or noninteger cost.')
    if stats is not None:
        stats['calls'] = stats.get('calls',0)+1
        stats['edge_scans'] = stats.get('edge_scans',0)+len(edges)
    incoming = {}
    for e in edges:
        if e.u == e.v or e.v == root:
            continue
        if e.v not in incoming or (e.cost,e.label)<(incoming[e.v].cost,incoming[e.v].label):
            incoming[e.v] = e
    if any(v not in incoming for v in vertices-{root}):
        return None
    done={root}; cycle=None
    for start in sorted(vertices):
        if start in done: continue
        trail=[]; place={}; u=start
        while u not in done and u not in place:
            place[u]=len(trail);trail.append(u);u=incoming[u].u
        if u in place:
            cycle=set(trail[place[u]:]);break
        done.update(trail)
    if cycle is None:
        return [incoming[v] for v in sorted(vertices-{root})]
    if stats is not None:
        stats['contractions']=stats.get('contractions',0)+1
    new=max(vertices)+1
    reduced=[]
    for e in edges:
        u=new if e.u in cycle else e.u
        v=new if e.v in cycle else e.v
        if u==v or v==root: continue
        cost=e.cost-(incoming[e.v].cost if e.v in cycle else 0)
        reduced.append(Edge(u,v,cost,e.label,None,e))
    selected=arborescence((vertices-cycle)|{new},root,reduced,stats)
    if selected is None:return None
    lifted=[e.previous for e in selected]
    enters=[e for e in lifted if e.u not in cycle and e.v in cycle]
    if len(enters)!=1:raise AssertionError('Contracted component needs one entering edge.')
    broken=enters[0].v
    return lifted+[incoming[v] for v in sorted(cycle-{broken})]


def strongly_connected(adj):
    """Tarjan SCCs, in dependency-first order for source->dependency edges."""
    number={};low={};stack=[];active=set();parts=[]
    def visit(v):
        number[v]=low[v]=len(number);stack.append(v);active.add(v)
        for w in sorted(adj[v]):
            if w not in number:
                visit(w);low[v]=min(low[v],low[w])
            elif w in active:low[v]=min(low[v],number[w])
        if low[v]==number[v]:
            part=[]
            while True:
                w=stack.pop();active.remove(w);part.append(w)
                if w==v:break
            parts.append(tuple(sorted(part)))
    for v in sorted(adj):
        if v not in number:visit(v)
    return tuple(parts)


def mandatory_classes(graph):
    """Sound monotone mandatory analysis; not claimed complete or novel."""
    must={c:{c} for c in graph.classes}
    while True:
        changed=False
        for c, nodes in graph.classes.items():
            alternatives=[set().union(*(must[x] for x in set(n.children))) for n in nodes]
            common=set.intersection(*alternatives) if alternatives else set()
            new=must[c]|common
            if new!=must[c]:must[c]=new;changed=True
        if not changed:return set().union(*(must[r] for r in graph.roots))


MANY=object()


def join_label(a,b):
    if a is MANY or b is MANY:return MANY
    if a is None:return b
    if b is None:return a
    return a if a==b else MANY


class ComponentBranching:
    """Private compilation plus exact recurrent-component branching.

    An admissible local implementation may depend on arbitrarily many core
    classes outside its SCC, but at most ONE distinct other core class inside
    it. Local self-dependence is impossible in an extraction and is discarded.
    Recognition is conservative with respect to global usefulness, but exact
    for existence of such a self-free local construction.
    """
    def __init__(self, graph: Graph):
        self.core=SharingCore(graph);self.g=self.core.g
        self.stats={}
        @lru_cache(None)
        def boundaries(c):
            if c in self.core.index:return frozenset({c})
            return frozenset(x for node in self.g.classes[c] for ch in set(node.children)
                             for x in boundaries(ch))
        self.adj={v:set(x for node in self.g.classes[v] for ch in set(node.children)
                        for x in boundaries(ch)) for v in self.core.core}
        self.components=strongly_connected(self.adj)
        self.which={v:i for i,part in enumerate(self.components) for v in part}
        self.obstructions=[]
        all_active=set(self.core.core)
        for v in self.core.core:
            table=self.local_table(v,all_active)
            if MANY in table:
                self.obstructions.append(dict(core=v,component=list(self.components[self.which[v]]),
                                              witness=table[MANY][1]))
        self.admitted=not self.obstructions
        self.mandatory=set(self.core.core)&mandatory_classes(self.g)

    def local_table(self, v, active):
        """Min-plus DP with labels empty / one recurrent class / two-or-more.

        Each state retains only one minimum, not every attainable price.
        The MANY state is only a recognition sentinel, never an arborescence arc.
        Externally activated core dependencies cost zero here, but their own
        construction is charged in the separate component objective.
        """
        block=set(self.components[self.which[v]])
        def best_put(table,label,item):
            self.stats['label_relaxations']=self.stats.get('label_relaxations',0)+1
            old=table.get(label)
            if old is None or (item[0],tuple(sorted(item[1].items())))<(old[0],tuple(sorted(old[1].items()))):
                table[label]=item
        @lru_cache(None)
        def value(c):
            if c in self.core.index:
                if c==v or c not in active:return {}
                return {c if c in block else None:(0,{})}
            return expand(c)
        def expand(c):
            answer={}
            for node in self.g.classes[c]:
                tab={None:(node.cost,{c:node.name})}
                for ch in sorted(set(node.children)):
                    nxt={}
                    for a,(ca,wa) in tab.items():
                        for b,(cb,wb) in value(ch).items():
                            if any(k in wa and wa[k]!=val for k,val in wb.items()):
                                raise AssertionError('Private ownership lemma violated.')
                            best_put(nxt,join_label(a,b),(ca+cb,wa|wb))
                    tab=nxt
                for label,item in tab.items():best_put(answer,label,item)
            self.stats['maximum_table_size']=max(self.stats.get('maximum_table_size',0),len(answer))
            return answer
        return expand(v)

    def evaluate(self, active):
        """Minimum cost of constructing ALL activated core results, or None.

        The returned reachable-root certificate may cost less if activation
        contained unused classes; minimizing the charged cost is exact.
        """
        if not self.admitted:
            raise UnsupportedRecurrence('At least one local construction needs two recurrent boundaries.')
        active=set(active)
        if not set(self.g.roots)<=active or not active<=set(self.core.core):
            raise ValueError('Activate all roots and only core classes.')
        choices={}; charged=0; per=[]
        for component in self.components:
            selected=sorted(active&set(component))
            if not selected:continue
            ids={v:i+1 for i,v in enumerate(selected)}
            edges=[]
            for v in selected:
                table=self.local_table(v,active)
                if MANY in table:raise AssertionError('Recognition failed.')
                for dep,(cost,ws) in table.items():
                    if dep is None or dep in ids:
                        edges.append(Edge(0 if dep is None else ids[dep],ids[v],cost,len(edges),ws))
            stats={}; solution=arborescence(set(ids.values())|{0},0,edges,stats)
            per.append(dict(vertices=len(selected),arcs=len(edges),stats=stats))
            if solution is None:
                return dict(cost=None,charged=None,choices=None,components=per)
            for edge in solution:
                for c,node in edge.payload.items():
                    if c in choices and choices[c]!=node:raise AssertionError('Overlapping local pieces.')
                    choices[c]=node
                charged+=edge.cost
        expanded=Graph(self.g.classes,tuple(sorted(active)))
        all_cost,_=expanded.check(choices)
        if all_cost!=charged:raise AssertionError('Active-set reconstruction mismatch.')
        cost,used=self.g.check(choices)
        if cost>charged:raise AssertionError('Nonnegative pruning increased cost.')
        return dict(cost=cost,charged=charged,choices=used,all_choices=choices,components=per)

    def solve(self, max_optional=18):
        if not self.admitted:raise UnsupportedRecurrence('Graph outside stated structural promise.')
        optional=[x for x in self.core.core if x not in self.mandatory]
        if len(optional)>max_optional:raise ValueError('Enumeration safety cap, not infeasibility.')
        best=None;calls=0
        for mask in range(1<<len(optional)):
            active=self.mandatory|{x for i,x in enumerate(optional) if mask>>i&1}
            out=self.evaluate(active);calls+=1
            if out['charged'] is not None and (best is None or out['charged']<best['charged']):best=out
        if best is None:best=dict(cost=None,charged=None,choices=None)
        if best['cost']!=best['charged']:raise AssertionError('Optimum activation contains removable cost.')
        return dict(best,optional=len(optional),activation_calls=calls)
