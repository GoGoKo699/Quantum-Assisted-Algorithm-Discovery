"""Exact shared-DAG extraction through a structurally shared class boundary.

Independent reference implementation. Costs are exact nonnegative integers.
It does not prove the semantic equalities asserted by an input e-graph.
"""
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from math import inf

@dataclass(frozen=True)
class Node:
    name: str
    cost: int
    children: tuple[str, ...] = ()

class Graph:
    def __init__(self, classes: dict[str, tuple[Node, ...]], roots: tuple[str, ...]):
        self.classes = dict(classes)
        self.roots = tuple(dict.fromkeys(roots))
        names = set()
        for c, nodes in self.classes.items():
            if not isinstance(c, str) or not nodes:
                raise ValueError('Nonempty named classes required.')
            for n in nodes:
                if n.name in names or type(n.cost) is not int or n.cost < 0:
                    raise ValueError('Unique nodes and nonnegative integer costs required.')
                names.add(n.name)
                if any(x not in self.classes for x in n.children):
                    raise ValueError('Unknown child class.')
        if any(r not in self.classes for r in self.roots):
            raise ValueError('Unknown root.')

    def reachable(self):
        seen, todo = set(), list(self.roots)
        while todo:
            c = todo.pop()
            if c in seen:
                continue
            seen.add(c)
            todo.extend(x for n in self.classes[c] for x in n.children)
        return seen

    def restrict_reachable(self):
        return Graph({c:self.classes[c] for c in sorted(self.reachable())}, self.roots)

    def support_acyclic(self):
        active, done = set(), set()
        def visit(c):
            if c in active:
                return False
            if c in done:
                return True
            active.add(c)
            if not all(visit(x) for n in self.classes[c] for x in set(n.children)):
                return False
            active.remove(c); done.add(c)
            return True
        return all(visit(r) for r in self.roots)

    def check(self, choices: dict[str,str]):
        active, done = set(), set()
        def visit(c):
            if c in active:
                raise ValueError('Cyclic selected computation.')
            if c in done:
                return
            if c not in choices:
                raise ValueError('Missing selected representative.')
            n = next((n for n in self.classes[c] if n.name == choices[c]), None)
            if n is None:
                raise ValueError('Representative does not belong to class.')
            active.add(c)
            for x in set(n.children): visit(x)
            active.remove(c); done.add(c)
        for r in self.roots: visit(r)
        used = {c:choices[c] for c in sorted(done)}
        value = sum(next(n.cost for n in self.classes[c] if n.name == used[c]) for c in done)
        return value, used

class SharingCore:
    def __init__(self, graph: Graph):
        self.g = graph.restrict_reachable()
        incoming = {c:set() for c in self.g.classes}
        for c, ns in self.g.classes.items():
            for n in ns:
                for x in set(n.children): incoming[x].add(c)
        self.core = tuple(sorted(set(self.g.roots) | {c for c, p in incoming.items() if len(p) >= 2}))
        self.index = {c:i for i,c in enumerate(self.core)}
        self.required = sum(1 << self.index[c] for c in self.g.roots)
        # A private directed cycle cannot be reachable from a root without
        # making an entry point either a root or a class with >=2 parents.
        active, done = set(), set()
        def private_visit(c):
            if c in self.index or c in done: return
            if c in active: raise AssertionError('Core did not break private cycle.')
            active.add(c)
            for n in self.g.classes[c]:
                for x in set(n.children): private_visit(x)
            active.remove(c); done.add(c)
        for c in self.g.classes: private_visit(c)

    def local(self, mask: int):
        """Costs to construct each new core class from already built core mask.

        A core class is a zero-cost terminal only when its bit is set.
        Representatives of the current class are expanded explicitly.
        """
        witnesses = {}
        @lru_cache(None)
        def private(c):
            if c in self.index:
                return 0 if mask & (1 << self.index[c]) else inf
            val, node = min((n.cost + sum(private(x) for x in set(n.children)), n.name)
                            for n in self.g.classes[c])
            witnesses[c] = node
            return val
        answer = []
        for c in self.core:
            val, node = min((n.cost + sum(private(x) for x in set(n.children)), n.name)
                            for n in self.g.classes[c])
            answer.append(val)
            witnesses[c] = node
        return answer, witnesses

    def solve(self, max_core: int = 22):
        """Subset-DP over core construction orders, valid with cyclic alternatives."""
        s = len(self.core)
        if s > max_core: raise ValueError(f'Core {s} exceeds explicit DP safety cap {max_core}.')
        count = 1 << s
        dp, parent = [inf]*count, [None]*count
        dp[0] = 0
        reachable_states, edges = 0, 0
        for mask in range(count):
            if dp[mask] == inf: continue
            reachable_states += 1
            values, _ = self.local(mask)
            for j, cost in enumerate(values):
                if mask & (1 << j) or cost == inf: continue
                edges += 1; child = mask | (1 << j)
                new = dp[mask] + cost
                if new < dp[child]: dp[child], parent[child] = new, (mask,j)
        final = min((m for m in range(count) if m & self.required == self.required), key=lambda m:(dp[m],m))
        if dp[final] == inf:
            return dict(cost=None, choices=None, core=list(self.core), dp_states=reachable_states, dp_edges=edges)
        trace=[]; m=final
        while m:
            prev,j=parent[m]; trace.append((prev,j));m=prev
        trace.reverse(); choices={}
        def collect(c, ws, at_core=False):
            if c in choices: return
            if c in self.index and not at_core: return
            name=ws[c]; choices[c]=name
            node=next(n for n in self.g.classes[c] if n.name==name)
            for child in set(node.children): collect(child,ws)
        for m,j in trace:
            _,ws=self.local(m);collect(self.core[j],ws,True)
        actual, used=self.g.check(choices)
        if actual != dp[final]: raise AssertionError(('Cost reconstruction discrepancy',actual,dp[final]))
        return dict(cost=actual, choices=used, core=list(self.core), dp_states=reachable_states,
                    dp_edges=edges, trace=[[m,self.core[j]] for m,j in trace])

    def activation_cost(self, activated: set[str]):
        """Exact objective only when the entire reachable support is acyclic.

        Cost can overcharge unused activated classes. Its minimum still equals
        extraction optimum because weights are nonnegative.
        """
        if not self.g.support_acyclic(): raise ValueError('Activation-only formula requires acyclic support.')
        if not set(self.g.roots) <= activated or not activated <= set(self.core):
            raise ValueError('Must activate all roots and only core classes.')
        mask=sum(1 << self.index[c] for c in activated)
        values,_=self.local(mask)
        return sum(values[self.index[c]] for c in activated)

    def solve_acyclic(self):
        if not self.g.support_acyclic(): raise ValueError('Acyclic support required.')
        optional=[c for c in self.core if c not in self.g.roots]
        best=inf; masks=0
        for bits in range(1 << len(optional)):
            a=set(self.g.roots)|{c for i,c in enumerate(optional) if bits & (1<<i)}
            best=min(best,self.activation_cost(a));masks+=1
        return dict(cost=None if best==inf else best, optional_core=len(optional), activation_queries=masks)

def exhaustive(graph: Graph, cap: int = 2000000):
    g=graph.restrict_reachable(); cs=list(g.classes); combinations=1
    for c in cs: combinations *= len(g.classes[c])
    if combinations > cap: raise ValueError('Exhaustive safety cap exceeded.')
    best=inf; best_choices=None; valid=0
    for ns in product(*(g.classes[c] for c in cs)):
        choices={c:n.name for c,n in zip(cs,ns)}
        try: cost,used=g.check(choices)
        except ValueError: continue
        valid+=1
        if cost < best: best,best_choices=cost,used
    return dict(cost=None if best==inf else best, choices=best_choices, assignments=combinations,
                valid_assignments=valid)
