"""Exact subgroup counting and interval stopping; diagnostic, not a quantum solver.

The group is supplied only by identity/add/neg/equal operations. No ambient
cardinality, coordinate decoder, sampler, or generation promise is consulted.
The caller separately supplies a rigorously valid upper bound on ambient size.
Primality uses deterministic trial division here, not a production proof system.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import isqrt, lcm, prod
from typing import Any, Callable, Sequence


class InvalidData(ValueError):
    """Malformed data or a failed exact order/consistency check."""


class BudgetExceeded(RuntimeError):
    """Declared completion budget exceeded: no cardinality conclusion."""


@dataclass(frozen=True)
class Group:
    zero: Any
    add: Callable[[Any, Any], Any]
    neg: Callable[[Any], Any]
    equal: Callable[[Any, Any], bool]


def natural(x: int, name: str, minimum: int = 1) -> int:
    if type(x) is not int or x < minimum:
        raise InvalidData(f'{name} must be an integer >= {minimum}')
    return x


def scale(group: Group, n: int, x: Any) -> Any:
    """Binary repeated addition; negative multipliers allowed."""
    if n < 0:
        return scale(group, -n, group.neg(x))
    out = group.zero
    while n:
        if n & 1:
            out = group.add(out, x)
        n >>= 1
        if n:
            x = group.add(x, x)
    return out


def prime(p: int) -> bool:
    """Exact but not polynomial-bit-time primality test; costs are not hidden."""
    natural(p, 'prime factor', 2)
    return all(p % d for d in range(2, isqrt(p) + 1))


def validate_order(group: Group, x: Any, order: int,
                   factors: Sequence[tuple[int, int]]) -> dict[int, int]:
    natural(order, 'order')
    clean: dict[int, int] = {}
    for p, e in factors:
        natural(e, 'factor multiplicity')
        if p in clean or not prime(p):
            raise InvalidData('Repeated or composite prime factor')
        clean[p] = e
    if prod(p ** e for p, e in clean.items()) != order:
        raise InvalidData('Incomplete order factorization')
    if not group.equal(scale(group, order, x), group.zero):
        raise InvalidData('Order does not annihilate the supplied element')
    if any(group.equal(scale(group, order // p, x), group.zero) for p in clean):
        raise InvalidData('Order is not minimal')
    return clean


def interval_multiple(divisor: int, lower: int, upper: int) -> dict:
    """Arithmetic only. Caller must establish divisor | ambient cardinality."""
    natural(divisor, 'divisor')
    natural(lower, 'lower bound')
    natural(upper, 'upper bound')
    if lower > upper:
        raise InvalidData('Reversed interval')
    first, last = (lower + divisor - 1) // divisor, upper // divisor
    if first > last:
        return {'status': 'inconsistent', 'first_multiplier': first,
                'last_multiplier': last}
    if first == last:
        return {'status': 'accepted', 'cardinality': first * divisor,
                'multiplier': first}
    return {'status': 'inconclusive', 'first_multiplier': first,
            'last_multiplier': last}


def subgroup_order(group: Group, generators: Sequence[Any],
                   orders: Sequence[int],
                   factorizations: Sequence[Sequence[tuple[int, int]]],
                   upper: int, cap: int = 64) -> dict:
    """Count H=<generators>, NOT G. Requires only |G|<=upper and valid group ops.

    E=exp(H) follows from checked exact generator orders. Note 23's bounded
    completion is applied to H itself. Large prime parts are cyclic by the upper
    bound; the remaining small-prime quotient is counted with exact membership.
    No assertion is made that H generates the ambient group.
    """
    natural(upper, 'upper bound')
    natural(cap, 'cofactor cap')
    if len(generators) != len(orders) or len(orders) != len(factorizations):
        raise InvalidData('Generator/order/factorization lengths disagree')
    if any(type(r) is not int or not 1 <= r <= upper for r in orders):
        raise InvalidData('Order outside the supplied bound')
    all_factors = [validate_order(group, x, r, f)
                   for x, r, f in zip(generators, orders, factorizations)]
    exponent = lcm(*orders)
    if exponent > upper:
        raise InvalidData('Subgroup exponent exceeds the ambient upper bound')
    # Empty lists and lists consisting of identities generate the trivial group.
    if exponent == 1:
        return {'subgroup_order': 1, 'exponent': 1, 'cofactor_bound': upper,
                'cosets': 1, 'membership_tests': 0, 'skipped_primes': [],
                'digit_table_entries': 0}
    bound = upper // exponent
    if bound > cap:
        raise BudgetExceeded(f'C={bound} exceeds cap={cap}')
    factors: dict[int, int] = {}
    for entry in all_factors:
        for p, e in entry.items():
            factors[p] = max(e, factors.get(p, 0))
    small = {p: e for p, e in sorted(factors.items()) if p <= bound}
    smooth = prod(p ** e for p, e in small.items())
    large = exponent // smooth
    anchor = group.zero
    for p, e in small.items():
        i = next(i for i, entry in enumerate(all_factors) if entry.get(p) == e)
        anchor = group.add(anchor, scale(group, exponent // (p ** e), generators[i]))
    validate_order(group, anchor, smooth, list(small.items()))
    projected = [scale(group, large, x) for x in generators]
    prepared = []
    for p, e in small.items():
        projection = smooth // (p ** e)
        a = scale(group, projection, anchor)
        top = scale(group, p ** (e - 1), a)
        table = [scale(group, j, top) for j in range(p)]
        prepared.append((p, e, projection, a, table))
    membership_tests = 0

    def member(x: Any) -> bool:
        nonlocal membership_tests
        membership_tests += 1
        if not group.equal(scale(group, smooth, x), group.zero):
            return False
        for p, e, projection, a, table in prepared:
            residual = scale(group, projection, x)
            digit_base = a
            for j in range(e):
                target = scale(group, p ** (e - 1 - j), residual)
                digit = next((d for d, value in enumerate(table)
                              if group.equal(target, value)), None)
                if digit is None:
                    return False
                residual = group.add(residual, group.neg(scale(group, digit, digit_base)))
                digit_base = scale(group, p, digit_base)
            if not group.equal(residual, group.zero):
                return False
        return True

    # All representatives stay in H_s by construction. Pairwise distinct cosets,
    # and closure under the supplied generators when the frontier is exhausted,
    # prove that exactly these cosets comprise H_s/<anchor>.
    representatives = [group.zero]
    position = 0
    while position < len(representatives):
        current = representatives[position]
        for generator in projected:
            candidate = group.add(current, generator)
            if not any(member(group.add(candidate, group.neg(r)))
                       for r in representatives):
                if len(representatives) >= bound:
                    raise InvalidData('Quotient contradicts the ambient upper bound')
                representatives.append(candidate)
        position += 1
    return {'subgroup_order': exponent * len(representatives), 'exponent': exponent,
            'cofactor_bound': bound, 'cosets': len(representatives),
            'membership_tests': membership_tests,
            'skipped_primes': sorted(p for p in factors if p > bound),
            'digit_table_entries': sum(p for p in small)}


def count_or_inconclusive(group: Group, generators: Sequence[Any],
                          orders: Sequence[int],
                          factorizations: Sequence[Sequence[tuple[int, int]]],
                          lower: int, upper: int, cap: int = 64) -> dict:
    """Early E-divisor test, bounded H completion, then a new ambient test.

    A sampling/generation promise is never an input. A budget return is UNKNOWN,
    not infeasibility. Invalid algebra/input is an exception, not a timeout.
    """
    natural(lower, 'lower bound')
    natural(upper, 'upper bound')
    natural(cap, 'cofactor cap')
    if lower > upper:
        raise InvalidData('Reversed interval')
    if len(generators) != len(orders) or len(orders) != len(factorizations):
        raise InvalidData('Generator/order/factorization lengths disagree')
    for x, r, factors in zip(generators, orders, factorizations):
        validate_order(group, x, r, factors)
    exponent = lcm(*orders)
    early = interval_multiple(exponent, lower, upper)
    if early['status'] != 'inconclusive':
        return dict(early, route='order-divisor', divisor=exponent)
    try:
        count = subgroup_order(group, generators, orders, factorizations, upper, cap)
    except BudgetExceeded as error:
        return {'status': 'inconclusive', 'route': 'completion-budget',
                'reason': str(error), 'divisor': exponent}
    final = interval_multiple(count['subgroup_order'], lower, upper)
    return dict(final, route='subgroup-divisor', divisor=count['subgroup_order'],
                completion=count)
