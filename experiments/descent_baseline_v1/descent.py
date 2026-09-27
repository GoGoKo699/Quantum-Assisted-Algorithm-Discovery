"""Classical task normalization, not a group-order solver or quantum compiler.

K(n) is the original Jacobian order over the degree-n field. T(n) is a FRESH
quadratic twist over that field, not the base twist extended by n. The only
rewrite used here is the established cardinality identity K(2n)=K(n)*T(n).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping

Key = tuple[str, int]


def positive(value: int, label: str) -> int:
    if type(value) is not int or value < 1:
        raise ValueError(f'{label} must be a positive integer')
    return value


@dataclass(frozen=True)
class Plan:
    requests: tuple[int, ...]
    leaves: tuple[Key, ...]
    # (target degree, half degree), in dependency order.
    products: tuple[tuple[int, int], ...]


def normalize(requests: list[int]) -> Plan:
    """Split every even original-curve query and reuse each classical result.

    No optimization/hardness/novelty claim. The caller must justify the twist
    interface and the group-order identity for the actual problem. The plan is
    deterministic even for reordered or duplicated requests.
    """
    if not requests:
        raise ValueError('At least one original-curve request is required')
    for n in requests:
        positive(n, 'extension degree')
    roots = tuple(sorted(set(requests)))
    seen: set[int] = set()
    leaves: set[Key] = set()
    products: list[tuple[int, int]] = []
    # Every dependency degree is smaller. An explicit stack avoids recursion
    # limits for arbitrary (binary encoded) input degrees.
    for root in roots:
        chain = []
        n = root
        while n not in seen and n % 2 == 0:
            chain.append(n)
            n //= 2
        if n not in seen:
            leaves.add(('K', n))
            seen.add(n)
        for n in reversed(chain):
            leaves.add(('T', n // 2))
            products.append((n, n // 2))
            seen.add(n)
    key_order = lambda key: (key[1], key[0])
    return Plan(roots, tuple(sorted(leaves, key=key_order)), tuple(products))


def execute(plan: Plan, supplied: Mapping[Key, int]) -> dict[int, int]:
    """Evaluate supplied order data; no data are discovered or authenticated.

    Refuse false plans, missing/extra leaves, zero, booleans and signed values.
    The validity of the numbers as actual group cardinalities remains a premise.
    """
    if plan != normalize(list(plan.requests)):
        raise ValueError('Not a canonical descent plan')
    if any(type(k) is not tuple or len(k) != 2 or type(k[0]) is not str
           or type(k[1]) is not int for k in supplied):
        raise ValueError('Malformed leaf key')
    if set(supplied) != set(plan.leaves):
        raise ValueError('Incorrect supplied leaf set')
    values = {k: positive(v, 'supplied cardinality') for k, v in supplied.items()}
    for n, half in plan.products:
        values['K', n] = values['K', half] * values['T', half]
    return {n: values['K', n] for n in plan.requests}


def comparison_sets(h: int) -> tuple[list[int], tuple[Key, ...]]:
    """Note 26's pruned direct requests and independent signed leaf definition."""
    positive(h, 'h')
    odd = list(range(1, h + 1, 2))
    direct = sorted(odd + list(range(2, 2 * h + 1, 2)))
    signed = [('K', r) for r in odd] + [('T', n) for n in range(1, h + 1)]
    return direct, tuple(sorted(signed, key=lambda key: (key[1], key[0])))
