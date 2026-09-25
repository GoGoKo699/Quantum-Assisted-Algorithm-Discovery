"""Exact helper-set synthesis and canonical-parent enumeration.

Integer +/- circuit model; free copies/signs, unlimited storage. No quantum
simulation, SAT claim, or hardware timing. This module is independently written.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations_with_replacement
from collections import Counter
from typing import Iterable

Vector = tuple[int, ...]

def canonical(v: Iterable[int]) -> Vector:
    v = tuple(v)
    s = next((x for x in v if x), 0)
    return tuple(-x for x in v) if s < 0 else v

def add(a: Vector, b: Vector, sign: int = 1) -> Vector:
    return canonical(x + sign*y for x, y in zip(a, b))

@dataclass
class CounterSet:
    closures: int = 0
    pair_tests: int = 0
    parent_tests: int = 0
    proposals: int = 0

class Model:
    def __init__(self, n: int, targets: Iterable[Vector]):
        if n < 1:
            raise ValueError('n must be positive')
        self.n = n
        self.basis = frozenset(tuple(int(i == j) for i in range(n)) for j in range(n))
        ts = [tuple(t) for t in targets]
        if any(len(t) != n for t in ts):
            raise ValueError('target shape mismatch')
        self.targets = frozenset(canonical(t) for t in ts if any(t)) - self.basis
        self.count = CounterSet()

    def closure(self, helpers: frozenset[Vector], witness: bool = False):
        """Do not assume that helpers are available: derive them from basis."""
        self.count.closures += 1
        available = set(self.basis)
        missing = set(self.targets | helpers) - available
        gates = []
        while missing:
            changed = False
            for t in sorted(missing):
                # To obtain a signed representative of t, t = a +/- b,
                # or -t = a +/- b; checking t +/- a up to sign suffices.
                found = None
                for a in sorted(available):
                    for sign in (1, -1):
                        self.count.pair_tests += 1
                        b = canonical(x + sign*y for x,y in zip(t,a))
                        if b in available:
                            # Recover actual parent signs, including output sign.
                            for sa in (1, -1):
                                for sb in (1, -1):
                                    raw = tuple(sa*x + sb*y for x,y in zip(a,b))
                                    if raw == t:
                                        found = (a,b,sa,sb)
                                        break
                                if found: break
                            if found: break
                    if found: break
                if found:
                    available.add(t); missing.remove(t)
                    gates.append((t, *found)); changed = True
            if not changed: break
        return (frozenset(available), gates) if witness else frozenset(available)

    def feasible(self, helpers: frozenset[Vector]) -> bool:
        return helpers <= self.closure(helpers)

    def parent(self, helpers: frozenset[Vector]):
        if not helpers: return None
        for h in sorted(helpers, reverse=True):
            self.count.parent_tests += 1
            candidate = helpers - {h}
            if self.feasible(candidate):
                return candidate
        raise ValueError('helper set is not constructible')

    def candidates(self, helpers: frozenset[Vector], available=None):
        if available is None: available = self.closure(helpers)
        generated = set()
        for a,b in combinations_with_replacement(sorted(available),2):
            for sign in (1,-1):
                h = add(a,b,sign)
                if any(h) and h not in available and h not in self.targets:
                    generated.add(h)
        return sorted(generated)

    def census(self, budget: int, method: str = 'canonical', collect: bool = False):
        """Count the FULL bounded state space, including descendants of goals.

        canonical: no visited-set cache in the traversal (collect is test-only).
        memoized: store all visited helper sets.
        Both enumerate candidate directions, not operand spellings.
        """
        if method not in ('canonical','memoized') or budget < 0:
            raise ValueError('invalid census options')
        self.count = CounterSet()
        seen = set() if method == 'memoized' else None
        collected = set() if collect else None
        by_depth = Counter(); goals = Counter(); stack = [frozenset()]
        first_witness = None
        while stack:
            H = stack.pop()
            if seen is not None:
                if H in seen: continue
                seen.add(H)
            if collected is not None:
                assert H not in collected
                collected.add(H)
            by_depth[len(H)] += 1
            A = self.closure(H)
            assert H <= A
            if self.targets <= A:
                goals[len(H)] += 1
                if first_witness is None or len(H) < len(first_witness): first_witness = H
            if len(H) >= budget: continue
            for h in self.candidates(H,A):
                self.count.proposals += 1
                G = H | {h}
                if method == 'canonical' and self.parent(G) != H: continue
                stack.append(G)
        stats = dict(method=method,budget=budget,vertices=sum(by_depth.values()),
                     by_depth=dict(sorted(by_depth.items())),goals=dict(sorted(goals.items())),
                     **vars(self.count))
        if first_witness is not None:
            A,gates = self.closure(first_witness,True)
            verify_certificate(self.n,self.targets,gates)
            stats['witness'] = {'helpers': sorted(first_witness),'gates':gates,
                                'gate_count':len(gates)}
        return stats,collected

def verify_certificate(n,targets,gates):
    known = {tuple(int(i==j) for i in range(n)) for j in range(n)}
    for t,a,b,sa,sb in gates:
        t,a,b = tuple(t),tuple(a),tuple(b)
        assert a in known and b in known
        assert tuple(sa*x+sb*y for x,y in zip(a,b)) == t
        assert t not in known
        known.add(t)
    assert set(map(tuple,targets)) <= known

if __name__ == '__main__':
    import json,sys,time
    T=[(1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)]
    m=Model(4,T); budget=int(sys.argv[1]) if len(sys.argv)>1 else 2
    method=sys.argv[2] if len(sys.argv)>2 else 'canonical'
    t=time.monotonic();result,_=m.census(budget,method)
    print(json.dumps(result,indent=2));print('elapsed',time.monotonic()-t,file=sys.stderr)
