"""Independent finite enumeration and selected large-integer execution controls."""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from itertools import product
from math import prod
import json
from subgroup import (Group, InvalidData, BudgetExceeded, count_or_inconclusive,
                      subgroup_order, validate_order, interval_multiple)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class Element:
    """Opaque to the algorithm; only the test adapter reads the tuple."""
    coordinates: tuple[int, ...]


class ProductFixture:
    def __init__(self, moduli):
        self.moduli = tuple(moduli)
        self.size = prod(moduli)
        self.calls = Counter()
        self.zero = Element((0,) * len(moduli))
        self.api = Group(self.zero, self.add, self.neg, self.equal)

    def element(self, coordinates):
        return Element(tuple(x % n for x, n in zip(coordinates, self.moduli)))

    def add(self, x, y):
        self.calls['addition'] += 1
        return Element(tuple((a + b) % n for a, b, n in
                             zip(x.coordinates, y.coordinates, self.moduli)))

    def neg(self, x):
        self.calls['negation'] += 1
        return Element(tuple(-a % n for a, n in zip(x.coordinates, self.moduli)))

    def equal(self, x, y):
        self.calls['equality'] += 1
        return x == y

    def basis(self):
        return [self.element(int(i == j) for i in range(len(self.moduli)))
                for j in range(len(self.moduli))]

    def elements(self):
        return [Element(x) for x in product(*(range(n) for n in self.moduli))]

    def enumerate_generated(self, generators):
        """Reference: enumerate actual elements, with no order or coset algorithm."""
        seen = {self.zero}
        frontier = [self.zero]
        while frontier:
            a = frontier.pop()
            for b in generators:
                c = Element(tuple((x + y) % n for x, y, n in
                                  zip(a.coordinates, b.coordinates, self.moduli)))
                if c not in seen:
                    seen.add(c)
                    frontier.append(c)
        return seen

    def enumerate_order(self, x):
        a = self.zero.coordinates
        for order in range(1, self.size + 1):
            a = tuple((u + v) % n for u, v, n in
                      zip(a, x.coordinates, self.moduli))
            if not any(a):
                return order
        raise AssertionError('Fixture failed to find an order')


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def expect_error(exception, call):
    try:
        call()
    except exception:
        return
    raise AssertionError(f'Expected {exception.__name__}')


def run():
    families = [(), (2,), (3,), (4,), (6,), (2, 2), (2, 3),
                (2, 4), (3, 3), (2, 2, 2), (4, 4)]
    counters = Counter()
    for moduli in families:
        fixture = ProductFixture(moduli)
        elements = fixture.elements()
        lists = [xs for k in range(3) for xs in product(elements, repeat=k)]
        # Add a full basis to exercise rank-three generation; duplicates retained
        # only when the list is not already among the complete length-0..2 census.
        basis = tuple(fixture.basis())
        if len(basis) > 2:
            lists.append(basis)
        for generators in lists:
            true_subgroup = len(fixture.enumerate_generated(generators))
            orders = [fixture.enumerate_order(x) for x in generators]
            factors = [factor(r) for r in orders]
            counters['generating_lists'] += 1
            counters['proper_subgroup_lists'] += true_subgroup < fixture.size
            for upper in (fixture.size, fixture.size + 1, 2 * fixture.size + 1):
                counted = subgroup_order(fixture.api, generators, orders, factors, upper, 128)
                require(counted['subgroup_order'] == true_subgroup, 'Incorrect subgroup order')
                counters['subgroup_completions'] += 1
            intervals = [(1, 2 * fixture.size + 1), (1, fixture.size),
                         (max(1, fixture.size - 1), fixture.size + 1),
                         (max(1, fixture.size - fixture.size // 4),
                          fixture.size + fixture.size // 4),
                         (fixture.size, fixture.size)]
            for lower, upper in intervals:
                result = count_or_inconclusive(fixture.api, generators, orders, factors,
                                               lower, upper, 128)
                # Independent reference lists all multiples; no imported interval rule.
                candidates = [n for n in range(lower, upper + 1)
                              if n % true_subgroup == 0]
                accepted = len(candidates) == 1
                require((result['status'] == 'accepted') == accepted, 'Wrong acceptance')
                if accepted:
                    require(result['cardinality'] == fixture.size, 'Wrong ambient order')
                    counters['accepted'] += 1
                    counters['accepted_proper_subgroup'] += true_subgroup < fixture.size
                    counters['accepted_after_subgroup_completion'] += result['route'] == 'subgroup-divisor'
                else:
                    counters['inconclusive'] += 1
                counters['ambient_interval_checks'] += 1
            # Deliberately double each exact positive order; must reject minimality.
            for x, order in zip(generators, orders):
                expect_error(InvalidData,
                             lambda: validate_order(fixture.api, x, 2 * order, factor(2 * order)))
                counters['nonminimal_orders_rejected'] += 1

    cube = ProductFixture((2, 2, 2))
    generators = cube.basis()[:2]
    small_examples = {}
    for name, lower, upper in [('proper_subgroup_certifies_eight', 6, 10),
                               ('same_samples_wide_interval', 4, 12)]:
        small_examples[name] = count_or_inconclusive(cube.api, generators, [2, 2],
                                                    [[(2, 1)], [(2, 1)]], lower, upper)
    require(small_examples['proper_subgroup_certifies_eight']['cardinality'] == 8,
            'Missing proper-subgroup example')
    require(small_examples['same_samples_wide_interval']['status'] == 'inconclusive',
            'Wide interval was incorrectly accepted')

    huge_examples = []
    for e in (20, 40, 80):
        exponent = 101 * (1 << e)
        fixture = ProductFixture((exponent, 4, 2, 3))
        # Last independent factor is intentionally unsampled. These are supplied
        # algebraic controls, not purportedly hard discovery inputs.
        gens = fixture.basis()[:3]
        lower, upper = fixture.size - 2 * exponent, fixture.size + 2 * exponent
        result = count_or_inconclusive(fixture.api, gens, [exponent, 4, 2],
                                      [[(2, e), (101, 1)], [(2, 2)], [(2, 1)]], lower, upper)
        require(result['status'] == 'accepted' and result['cardinality'] == fixture.size,
                'Large control failed')
        require(result['completion']['cosets'] == 8 and result['multiplier'] == 3,
                'Large control did not count the intended proper subgroup')
        require(result['completion']['skipped_primes'] == [101], 'Large prime not skipped')
        huge_examples.append(dict(e=e, ambient_size=fixture.size, result=result,
                                  group_calls=dict(sorted(fixture.calls.items()))))

    malformed = ProductFixture((4,))
    x = malformed.basis()[0]
    cases = [(4, [(4, 1)]), (4, [(2, 1)]), (4, [(2, 1), (2, 1)]),
             (4, [(2, 0)]), (0, []), (3, [(3, 1)]), (True, []), (4, [(True, 2)])]
    for order, factors in cases:
        expect_error(InvalidData, lambda: validate_order(malformed.api, x, order, factors))
    large_rank = ProductFixture((2,) * 10)
    budget = count_or_inconclusive(large_rank.api, large_rank.basis(), [2] * 10,
                                  [[(2, 1)]] * 10, 1000, 1040, 64)
    require(budget['route'] == 'completion-budget', 'Missing budget fallback')
    expect_error(BudgetExceeded, lambda: subgroup_order(large_rank.api, large_rank.basis(),
                 [2] * 10, [[(2, 1)]] * 10, 1040, 64))
    # Missing generator and order metadata, reversed bounds, and bad cap.
    expect_error(InvalidData, lambda: count_or_inconclusive(cube.api, generators, [2],
                 [[(2, 1)]], 6, 10))
    expect_error(InvalidData, lambda: interval_multiple(2, 10, 6))
    expect_error(InvalidData, lambda: count_or_inconclusive(cube.api, [], [], [], 1, 10, 0))
    # The strict sufficient condition uses M > width, not M >= width.
    require(interval_multiple(2, 2, 4)['status'] == 'inconclusive', 'Endpoint boundary')
    require(interval_multiple(4, 9, 11)['status'] == 'inconsistent', 'Impossible divisor')
    return {'schema': 1, 'family_count': len(families), 'census': dict(sorted(counters.items())),
            'examples': small_examples, 'large_controls': huge_examples,
            'budget_control': budget, 'malformed_order_controls': len(cases),
            'scope': 'Exact supplied-group controls; no curve or quantum sampler, no native benchmark.'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
