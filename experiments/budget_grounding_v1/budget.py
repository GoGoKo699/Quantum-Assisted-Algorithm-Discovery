"""Exact budget-grounded shared-DAG extraction, including cyclic alternatives.

Independent successor to sharing_core_v1. No quantum runtime is measured.
Costs and budgets are exact nonnegative integers. No helpers are assumed free.
"""
from __future__ import annotations
import sys
from pathlib import Path
from math import comb, inf
from typing import Iterator
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'sharing_core_v1'))
from core import Graph, Node, SharingCore, exhaustive


def allocations(parts: int, total: int) -> Iterator[tuple[int, ...]]:
    """Weak compositions with sum <= total, in lexicographic order."""
    if parts < 0 or total < 0: raise ValueError('Nonnegative parameters required.')
    if parts == 0:
        yield ()
    else:
        for first in range(total + 1):
            for rest in allocations(parts - 1, total - first):
                yield (first,) + rest


def unrank(parts: int, total: int, rank: int) -> tuple[int, ...]:
    """Unrank without iterating over the numeric value of total.

    Uses binomial prefix counts and binary search, polynomial in parts and
    log(total+1); integer arithmetic is exact. Invalid padding labels rejected.
    """
    if parts < 0 or total < 0 or rank < 0 or rank >= comb(total + parts, parts):
        raise ValueError('Invalid allocation rank.')
    answer = []
    for p in range(parts, 0, -1):
        full = comb(total + p, p)
        def before(x: int) -> int:
            return full - comb(total - x + p, p)
        lo, hi = 0, total + 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if before(mid) <= rank: lo = mid
            else: hi = mid
        answer.append(lo)
        rank -= before(lo)
        total -= lo
    if rank != 0: raise AssertionError('Unranking remainder.')
    return tuple(answer)


def rank_allocation(budgets: tuple[int, ...], total: int) -> int:
    if total < 0 or any(type(x) is not int or x < 0 for x in budgets) or sum(budgets) > total:
        raise ValueError('Invalid budget vector.')
    rank = 0
    for i, x in enumerate(budgets):
        p = len(budgets) - i
        rank += comb(total + p, p) - comb(total - x + p, p)
        total -= x
    return rank


class Grounding:
    def __init__(self, graph: Graph):
        self.core = SharingCore(graph)
        self.g = self.core.g

    def close(self, budgets: tuple[int, ...], witness: bool = True) -> dict:
        """Synchronous monotone rounds; costs are tested against local caps.

        A zero cap does not mean 'already constructed'. It only permits pieces
        which can actually be constructed for zero cost from the prior round.
        """
        s = len(self.core.core)
        if len(budgets) != s or any(type(x) is not int or x < 0 for x in budgets):
            raise ValueError('One nonnegative integer cap per core class required.')
        mask, events, rounds = 0, [], []
        for _ in range(s):
            costs, ws = self.core.local(mask)
            new = [j for j in range(s) if not (mask >> j) & 1 and costs[j] <= budgets[j]]
            if not new: break
            rounds.append([self.core.core[j] for j in new])
            if witness:
                events.extend((j, costs[j], dict(ws)) for j in new)
            mask |= sum(1 << j for j in new)
        success = mask & self.core.required == self.core.required
        result = {'success': success, 'mask': mask, 'rounds': rounds}
        if not witness or not success: return result
        choices: dict[str, str] = {}
        charged = 0
        def collect(c: str, ws: dict[str, str], boundary: bool = False) -> None:
            if c in choices: return
            if c in self.core.index and not boundary: return
            name = ws[c]
            choices[c] = name
            n = next(n for n in self.g.classes[c] if n.name == name)
            for child in sorted(set(n.children)): collect(child, ws)
        for j, price, ws in events:
            charged += price
            collect(self.core.core[j], ws, True)
        actual, used = self.g.check(choices)
        if not actual <= charged <= sum(budgets):
            raise AssertionError(('Budget accounting', actual, charged, budgets))
        result.update(cost=actual, all_constructed_cost=charged, choices=used)
        return result

    def decision(self, total: int, safety_cap: int = 1000000) -> dict:
        size = comb(total + len(self.core.core), len(self.core.core))
        if size > safety_cap: raise ValueError(f'{size} allocations exceed safety cap.')
        for i, b in enumerate(allocations(len(self.core.core), total)):
            got = self.close(b)
            if got['success']:
                return dict(got, allocations_checked=i+1, allocation_space=size, budgets=list(b))
        return dict(success=False, allocations_checked=size, allocation_space=size)

    def caps_from_dp(self, optimum: dict) -> tuple[int, ...]:
        """Convert an independent subset-DP witness into local caps."""
        if optimum['cost'] is None: raise ValueError('Feasible DP witness required.')
        b = [0] * len(self.core.core)
        for mask, name in optimum['trace']:
            j = self.core.index[name]
            b[j] = self.core.local(mask)[0][j]
        if sum(b) != optimum['cost']: raise AssertionError('DP decomposition cost.')
        return tuple(b)
