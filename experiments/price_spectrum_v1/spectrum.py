"""Finite local-price alphabets for exact cyclic e-graph extraction.

The compiler is output-sensitive, NOT promised polynomial in the input graph.
Explicit limits abort rather than dropping prices. No QRAM or quantum execution.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product
from math import inf, prod
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'budget_grounding_v1'))
from budget import Graph, Node, SharingCore, Grounding


class SpectrumLimit(RuntimeError):
    """Compiling this instance exceeds its declared work/space budget."""


class PriceSpectrum:
    def __init__(self, graph: Graph, threshold: int, max_prices: int = 200000,
                 max_pairs: int = 5000000, propagate: bool = False):
        if type(threshold) is not int or threshold < 0:
            raise ValueError('A nonnegative integer threshold is required.')
        if max_prices < 1 or max_pairs < 1:
            raise ValueError('Positive explicit compilation limits required.')
        self.grounding = Grounding(graph)
        self.core = self.grounding.core
        self.K = threshold
        self.mandatory = mandatory_classes(self.core.g)
        full = (1 << len(self.core.core))-1
        self.lower = tuple(self.core.local(full ^ (1 << j))[0][j]
                           if c in self.mandatory else 0
                           for j,c in enumerate(self.core.core))
        self.infeasible_lower = any(x == inf for x in self.lower) or sum(self.lower) > threshold
        self.fixed = {}
        if propagate and not self.infeasible_lower:
            grounded = self.grounding.close(self.lower, witness=False)['mask']
            self.fixed = {j:self.lower[j] for j in range(len(self.lower)) if (grounded >> j)&1}
        self.stats = dict(pair_sums=0, stored_private_prices=0,
                          stored_core_prices=0, peak_set=0)

        def check_size(prices):
            self.stats['peak_set'] = max(self.stats['peak_set'], len(prices))
            if len(prices) > max_prices:
                raise SpectrumLimit('Price-set cap exceeded; no answer asserted.')

        def node_prices(node):
            values = {node.cost} if node.cost <= threshold else set()
            for child in sorted(set(node.children)):
                rhs = private(child)
                combined = set()
                for a in sorted(values):
                    for b in sorted(rhs):
                        self.stats['pair_sums'] += 1
                        if self.stats['pair_sums'] > max_pairs:
                            raise SpectrumLimit('Pair-sum cap exceeded; no answer asserted.')
                        if a + b <= threshold:
                            combined.add(a+b)
                            check_size(combined)
                values = combined
                if not values:
                    break
            return values

        @lru_cache(None)
        def private(c):
            if c in self.core.index:
                return frozenset({0})  # Price only; availability checked by grounding.
            prices = set()
            for node in self.core.g.classes[c]:
                prices.update(node_prices(node))
                check_size(prices)
            self.stats['stored_private_prices'] += len(prices)
            return frozenset(prices)

        raw = []
        for j,c in enumerate(self.core.core):
            if j in self.fixed:
                raw.append((self.fixed[j],))
                continue
            prices = set()
            for node in self.core.g.classes[c]:
                prices.update(node_prices(node))
                check_size(prices)
            self.stats['stored_core_prices'] += len(prices)
            raw.append(tuple(sorted(prices)))
        self.prices = tuple(raw)
        # 0 represents a zero cap, not availability or an unconditional purchase.
        self.raw_alphabets = tuple(tuple(sorted({0, *p})) for p in self.prices)
        all_mask = (1 << len(raw))-1
        domains = []
        for j, c in enumerate(self.core.core):
            lower = self.core.local(all_mask ^ (1 << j))[0][j]
            keep = {p for p in self.prices[j] if p >= lower}
            if c not in (self.mandatory if propagate else self.core.g.roots):
                keep.add(0)
            domains.append((self.fixed[j],) if j in self.fixed else tuple(sorted(keep)))
        self.alphabets = tuple(domains)
        self.cartesian_size = 0 if self.infeasible_lower else prod(map(len, self.alphabets))

    def snap(self, caps):
        """Round down; with forced caps this preserves final grounding, not each round."""
        if len(caps) != len(self.prices) or any(type(x) is not int or x < 0 for x in caps):
            raise ValueError('Nonnegative integer cap per core required.')
        if any(x > self.K for x in caps):
            raise ValueError('The truncated alphabet covers only caps <= K.')
        if self.fixed and any(b < lo for b,lo in zip(caps,self.lower)):
            raise ValueError('Forced-grounding reduction requires caps above mandatory lower prices.')
        return tuple(self.fixed[j] if j in self.fixed else max(p for p in ps if p <= b)
                     for j,(ps,b) in enumerate(zip(self.raw_alphabets,caps)))

    def decode(self, rank: int):
        if type(rank) is not int or not 0 <= rank < self.cartesian_size:
            raise ValueError('Rank outside the exact mixed-radix domain.')
        digits = [0]*len(self.alphabets)
        for i in range(len(digits)-1, -1, -1):
            rank, digit = divmod(rank, len(self.alphabets[i]))
            digits[i] = self.alphabets[i][digit]
        return tuple(digits)

    def encode(self, caps):
        if len(caps) != len(self.alphabets):
            raise ValueError('Wrong tuple length.')
        rank = 0
        for choices, x in zip(self.alphabets, caps):
            rank = rank*len(choices)+choices.index(x)
        return rank

    def decision(self, safety_cap: int = 1000000):
        if self.cartesian_size > safety_cap:
            raise SpectrumLimit('Decision enumeration safety cap; not infeasibility.')
        for rank in range(self.cartesian_size):
            caps = self.decode(rank)
            if sum(caps) > self.K:
                continue
            out = self.grounding.close(caps)
            if out['success']:
                return dict(out, caps=list(caps), rank=rank)
        return dict(success=False)

    def cost_histogram(self, state_limit: int = 1000000):
        """Optional sparse sum DP for domain statistics, NOT free preprocessing."""
        hist = {0: 1}
        total_states = 1
        for values in self.alphabets:
            nxt = {}
            for old, count in hist.items():
                for value in values:
                    if old+value <= self.K:
                        nxt[old+value] = nxt.get(old+value, 0)+count
            if len(nxt) > state_limit:
                raise SpectrumLimit('Sparse histogram cap exceeded.')
            hist = nxt
            total_states += len(hist)
        return dict(admissible_vectors=sum(hist.values()),
                    distinct_final_sums=len(hist), dp_states=total_states)


def scaled(graph, factor):
    if type(factor) is not int or factor < 1:
        raise ValueError('Positive integer scale required.')
    return Graph({c:tuple(Node(n.name, n.cost*factor, n.children) for n in ns)
                  for c,ns in graph.classes.items()}, graph.roots)


def exponential_spectrum(n: int, binary_weights: bool = True):
    """Linear-size easy family whose root can have 2**n distinct local prices.

    Core S_i is a required root costing one. A private root child is either
    an independent paid construction or a zero-cost use of S_i. All S_i
    must be built, so the global optimum is n by cardinality and a witness.
    This is a structural counterexample, not a difficult application family.
    """
    if n < 1:
        raise ValueError('Positive n required.')
    cs = {}
    for i in range(n):
        cs[f's{i}'] = (Node(f'input{i}', 1),)
        cs[f'p{i}'] = (Node(f'paid{i}', (1 << i) if binary_weights else 1),
                      Node(f'use{i}', 0, (f's{i}',)))
    cs['root'] = (Node('join', 0, tuple(f'p{i}' for i in range(n))),)
    return Graph(cs, tuple(['root']+[f's{i}' for i in range(n)]))


def mandatory_classes(graph):
    """Safe least-fixed-point mandatory-class analysis, including cyclic support.

    Every finite implementation of c uses every member of must[c]. This is
    a lower approximation, not promised the strongest dominator analysis.
    """
    must = {c:{c} for c in graph.classes}
    while True:
        changed = False
        for c, nodes in graph.classes.items():
            alternatives = [set().union(*(must[x] for x in set(n.children)))
                            for n in nodes]
            common = set.intersection(*alternatives) if alternatives else set()
            new = must[c] | common
            if new != must[c]:
                must[c] = new
                changed = True
        if not changed:
            return set().union(*(must[r] for r in graph.roots))


def persistent_spectrum(n: int):
    """Independent two-use components; mandatory grounding does not simplify them.

    Root needs p_i and q_i. Each costs 3**i directly, or can use shared b_i
    for free; b_i costs 2*3**i+1. Direct construction is optimal componentwise.
    Root local spectra contain 3**n sums and 2**n distinct conditional minima.
    This is an easy structural family demonstrating compilation cost, not hardness.
    """
    if n < 1:
        raise ValueError('Positive n required.')
    cs = {}
    for i in range(n):
        w = 3**i
        cs[f'b{i}'] = (Node(f'b{i}',2*w+1),)
        for prefix in ('p','q'):
            name=f'{prefix}{i}'
            cs[name]=(Node(name+'paid',w),Node(name+'use',0,(f'b{i}',)))
    cs['root']=(Node('join',0,tuple(f'{p}{i}' for i in range(n) for p in ('p','q'))),)
    return Graph(cs,('root',))
