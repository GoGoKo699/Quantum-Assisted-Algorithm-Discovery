"""Finite checks of task normalization and one nonsplitting elliptic control.

The control enumerates points over F_5 and F_25, not a high-genus Jacobian or
quantum circuit. No group-law implementation or large search library is used.
"""
from __future__ import annotations
from dataclasses import replace
from itertools import combinations
import json
from math import prod
from descent import comparison_sets, execute, normalize


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def fails(action) -> None:
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Malformed data accepted')


def quadratic_orders(n: int) -> tuple[int, int]:
    # Independent root-power recurrence for E: y^2=x^3-x / F_5, trace=-2.
    if n == 1:
        power_sum = -2
    else:
        a, b = 2, -2
        for _ in range(2, n + 1):
            a, b = b, -2 * b - 5 * a
        power_sum = b
    return 1 + 5**n - power_sum, 1 + 5**n + power_sum


def elliptic_control() -> dict:
    # F_25 = F_5[s]/(s^2-2). Irreducible: 2 not among the base-field squares.
    require(2 not in {x*x % 5 for x in range(5)}, 'Invalid quadratic field')
    require((4*(-1)**3) % 5 != 0, 'Singular original curve')
    require(4 % 5 != 0, 'Singular twist')
    field = [(a, b) for a in range(5) for b in range(5)]
    base = [(a, 0) for a in range(5)]
    zero, one, s = (0, 0), (1, 0), (0, 1)

    def add(x, y):
        return ((x[0]+y[0]) % 5, (x[1]+y[1]) % 5)

    def mul(x, y):
        return ((x[0]*y[0]+2*x[1]*y[1]) % 5,
                (x[0]*y[1]+x[1]*y[0]) % 5)

    def power(x, n):
        out = one
        while n:
            if n & 1:
                out = mul(out, x)
            x = mul(x, x)
            n >>= 1
        return out

    def points(elements, A):
        out = {None}  # infinity
        for x in elements:
            rhs = add(mul(mul(x, x), x), mul(A, x))
            for y in elements:
                if mul(y, y) == rhs:
                    out.add((x, y))
        return out

    require(power(s, 5) == (0, 4), 'Frobenius must negate s')
    require(all(power(x, 25) == x for x in field), 'Field Frobenius control')
    E5 = points(base, (4, 0))      # y^2=x^3-x
    twist5 = points(base, (1, 0))  # y^2=x^3-2^2*x=x^3+x
    E25 = points(field, (4, 0))
    twist25 = points(field, (1, 0))
    # Standard twist isomorphism (x,y)->(x/d,y/(d*s)), d=2.
    inv_d = (3, 0)
    inv_ds = power(mul((2, 0), s), 23)
    require(mul(mul((2, 0), s), inv_ds) == one, 'Inverse control')

    def embed(point):
        if point is None:
            return None
        return (mul(point[0], inv_d), mul(point[1], inv_ds))

    embedded = {embed(P) for P in twist5}
    require({embed(P) for P in twist25} == E25, 'Quadratic twist isomorphism failed')
    require(embedded <= E25 and E5 <= E25, 'Embedding failed')
    # In characteristic != 2, [-1](x,y)=(x,-y); hence [2]P=0 iff y=0 or P=O.
    torsion = lambda points: {P for P in points if P is None or P[1] == zero}
    A2, B2, G2 = torsion(E5), torsion(twist5), torsion(E25)
    require(E5 & embedded == A2, 'Wrong natural-subgroup intersection')
    require(len(E5) * len(twist5) == len(E25), 'Cardinality factorization')
    require(len(A2) * len(B2) != len(G2), 'Control must refute group isomorphism')
    require(quadratic_orders(1) == (len(E5), len(twist5)), 'Independent trace recurrence')
    require(quadratic_orders(2)[0] == len(E25), 'Independent extension recurrence')
    return {
        'curve': 'y^2=x^3-x over F_5',
        'twist': 'y^2=x^3+x; nonsquare d=2',
        'extension_model': 'F_5[s]/(s^2-2)',
        'base_order': len(E5), 'twist_order': len(twist5),
        'quadratic_extension_order': len(E25),
        'natural_subgroup_intersection': len(E5 & embedded),
        'two_torsion_extension': len(G2),
        'two_torsion_product': len(A2)*len(B2),
        'sum_subgroup_order_by_intersection_formula': len(E5)*len(twist5)//len(A2),
        'quantum_state_factorization': 'NOT established; the groups are not isomorphic',
    }


def run() -> dict:
    matched, scalar_checks, subset_plans = 0, 0, 0
    for h in range(1, 65):
        direct, signed = comparison_sets(h)
        plan = normalize(direct)
        require(plan.leaves == signed, 'Descent must give the signed query leaves')
        require(len(plan.products) == h, 'Each requested even degree computed once')
        supplied = {key: 1 + 3*key[1] + (key[0] == 'T') for key in signed}
        actual = execute(plan, supplied)
        # Reference expands one dyadic chain algebraically, with no memoized plan.
        for n in direct:
            odd, ancestor = n, []
            while odd % 2 == 0:
                odd //= 2
                ancestor.append(odd)
            expected = supplied['K', odd] * prod(supplied['T', a] for a in ancestor)
            require(actual[n] == expected, 'Wrong scalar product')
            scalar_checks += 1
        require(normalize(list(reversed(direct)) + direct) == plan,
                'Duplicate/reordered roots must not change plan')
        matched += 1
    # Independently sourced formulas for one small fixed E; no larger fields constructed.
    direct, signed = comparison_sets(8)
    orders = {key: quadratic_orders(key[1])[key[0] == 'T'] for key in signed}
    out = execute(normalize(direct), orders)
    require(all(value == quadratic_orders(n)[0] for n, value in out.items()),
            'Curve recurrence disagrees with descent')
    # Every nonempty subset of degrees 1..8 checks sharing beyond the main schedule.
    for r in range(1, 9):
        for roots in combinations(range(1, 9), r):
            plan = normalize(list(roots))
            require(len(plan.products) == len(set(n for n, _ in plan.products)),
                    'A multiplication was duplicated')
            supplied = {key: quadratic_orders(key[1])[key[0] == 'T'] for key in plan.leaves}
            require(execute(plan, supplied) == {n: quadratic_orders(n)[0] for n in roots},
                    'General subset control')
            subset_plans += 1
    plan = normalize([1, 2, 4])
    supplied = {key: 6 for key in plan.leaves}
    malformed = [lambda: normalize([]), lambda: normalize([True]),
                 lambda: normalize([0]), lambda: normalize([-2]),
                 lambda: normalize([1.0]),
                 lambda: execute(plan, {}),
                 lambda: execute(plan, dict(supplied, extra=1)),
                 lambda: execute(plan, {key: 0 for key in plan.leaves}),
                 lambda: execute(plan, {key: True for key in plan.leaves}),
                 lambda: execute(replace(plan, products=tuple(reversed(plan.products))), supplied)]
    for action in malformed:
        fails(action)
    # Base twist extended to degree 2 is trivial; it is not the fresh T(2).
    K2, T2 = quadratic_orders(2)
    require(K2 != T2, 'Fresh-twist negative control is degenerate')
    return {
        'schema': 1,
        'scope': 'Classical task normalization and one finite-field nonsplitting control; no quantum experiment.',
        'matched_h_values': matched, 'scalar_product_checks': scalar_checks,
        'nonempty_request_subsets': subset_plans, 'malformed_controls': len(malformed),
        'genus_ten_plan': {'h': 8, 'original_requests': direct,
                          'common_backend_leaves': [list(x) for x in signed],
                          'leaves_each_route': len(signed), 'max_leaf_degree_each_route': 8,
                          'products_to_materialize_original_requests': 8,
                          'leafwise_backend_ratio': '1 exactly when settings and leaf data agree'},
        'elliptic_control': elliptic_control(),
        'base_twist_not_fresh': {'extended_base_twist_order': K2, 'fresh_twist_order': T2},
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
