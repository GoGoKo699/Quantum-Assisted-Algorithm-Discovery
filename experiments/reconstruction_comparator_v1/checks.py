"""Focused transcript and matched-accounting checks, not a native benchmark."""
from __future__ import annotations
from fractions import Fraction
from math import prod
from pathlib import Path
import json
import sys
from transcripts import indices, plain_from_signed, signed_from_plain, reconstruct

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'translation_cost_v1'))
from cost import schedule


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def poly_product(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def factor_data(q, traces, max_n):
    """Supplied factored Weil controls; not asserted to be curve Jacobians."""
    polynomial = [1]
    all_powers = []
    for t in traces:
        require(t * t <= 4 * q, 'Invalid quadratic Weil control')
        polynomial = poly_product(polynomial, [1, -t, q])
        values = [2, t]
        for _ in range(2, max_n + 1):
            values.append(t * values[-1] - q * values[-2])
        all_powers.append(values)
    K = {n: prod(1 - values[n] + q**n for values in all_powers)
         for n in range(1, max_n + 1)}
    T = {n: prod(1 + values[n] + q**n for values in all_powers)
         for n in range(1, max_n + 1)}
    return polynomial, K, T


def multiply(A, B):
    return [[sum(a*b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def determinant(A):
    """Independent fraction-free determinant with exact-division checks."""
    A = [row[:] for row in A]
    sign, previous = 1, 1
    for k in range(len(A) - 1):
        pivot = next((i for i in range(k, len(A)) if A[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        value = A[k][k]
        for i in range(k + 1, len(A)):
            for j in range(k + 1, len(A)):
                A[i][j], rem = divmod(A[i][j]*value - A[i][k]*A[k][j], previous)
                require(rem == 0, 'Nonexact Bareiss division')
            A[i][k] = 0
        previous = value
    return sign * A[-1][-1]


def companion_orders(polynomial, max_n):
    d = len(polynomial) - 1
    C = [[0] * d for _ in range(d)]
    for i in range(d - 1):
        C[i][i + 1] = 1
    C[-1] = [-value for value in reversed(polynomial[1:])]
    power = [[int(i == j) for j in range(d)] for i in range(d)]
    K, T = {}, {}
    for n in range(1, max_n + 1):
        power = multiply(power, C)
        K[n] = determinant([[int(i == j) - power[i][j] for j in range(d)] for i in range(d)])
        T[n] = determinant([[int(i == j) + power[i][j] for j in range(d)] for i in range(d)])
    return K, T


def rational(value):
    value = Fraction(value)
    return {'numerator': value.numerator, 'denominator': value.denominator}


def run():
    transcript_roundtrips = 0
    for h in range(1, 65):
        odd, degrees = indices(h)
        independent = sorted(set(range(1, h + 1)) | set(range(2, 2*h + 1, 2)))
        require(degrees == independent, 'Wrong pruned direct-query set')
        require(len(degrees) == h + (h+1)//2, 'Query counts differ')
        for policy in (0, 1):
            anchors = {n: 2*n + 3 for n in odd}
            twists = {n: 1 if policy == 0 else n*n + 5 for n in range(1, h + 1)}
            plain = plain_from_signed(h, anchors, twists)
            # Independently walk each dyadic chain, not increasing all n.
            reference = {}
            for r in odd:
                reference[r] = anchors[r]
                n = r
                while n <= h:
                    reference[2*n] = reference[n] * twists[n]
                    n *= 2
            require(plain == reference, 'Dyadic traversal disagrees')
            require(signed_from_plain(h, plain) == (anchors, twists), 'Round trip failed')
            transcript_roundtrips += 1
    reconstructed = []
    determinant_checks = 0
    for g in range(3, 15):
        q = 65537
        h = g - 2
        t = [((i * 173 + g * 29) % 1001) - 500 for i in range(g)]
        P, K, T = factor_data(q, t, 2*h)
        odd, degrees = indices(h)
        anchors = {n: K[n] for n in odd}
        twists = {n: T[n] for n in range(1, h+1)}
        plain = {n: K[n] for n in degrees}
        require(plain_from_signed(h, anchors, twists) == plain, 'Known orders differ')
        require(reconstruct(q, g, anchors, twists) == P, 'Signed reconstruction failed')
        a, t2 = signed_from_plain(h, plain)
        require(reconstruct(q, g, a, t2) == P, 'Pruned direct reconstruction failed')
        reconstructed.append({'g': g, 'q': q, 'calls_each': len(degrees), 'factor_traces': t})
        if g <= 4:
            alternate_K, alternate_T = companion_orders(P, 2*h)
            require(alternate_K == K and alternate_T == T, 'Independent determinant differs')
            determinant_checks += 4*h
    # Inherited genuine curve coefficient example, not a new curve computation.
    P = [1, 4, 10, 20, 25]
    K, T = companion_orders(P, 6)
    require(K[1] == 60 and T[1] == 12 and K[2] == 720, 'Known curve control')
    require(reconstruct(5, 2, {1: K[1]}, {1: T[1]}) == P, 'Genus two endpoints')
    require(all(K[2*n] == K[n]*T[n] for n in (1,2,3)), 'Genuine curve doubling')
    determinant_checks += 12
    require(reconstruct(5, 1, {1: 6}, {}) == [1, 0, 5], 'Genus one special case')
    homogeneous_checks = 0
    for h in range(1, 129):
        odd, degrees = indices(h)
        for k in range(5):
            A = sum(n**k for n in range(1, h+1))
            B = sum(n**k for n in odd)
            direct, signed = sum(n**k for n in degrees), A+B
            require(direct == 2**k*A+B, 'Homogeneous cost identity')
            require(direct - signed == (2**k-1)*A, 'Cost difference identity')
            # Distinct weighted costs are not a query-count improvement.
            require((direct == signed) == (k == 0), 'Flat versus increasing cost')
            homogeneous_checks += 1
    # Arbitrary curve-dependent costs can reverse the preference.
    h = 8
    odd, degrees = indices(h)
    general_cost_direct = len(degrees)   # C_K(n)=1 for every n
    general_cost_signed = len(odd) + 1000*h  # C_T(n)=1000
    require(general_cost_signed > general_cost_direct, 'Cost-asymmetry control')
    malformed = [
        lambda: indices(0), lambda: indices(True),
        lambda: plain_from_signed(2, {1: 2}, {1: 3}),
        lambda: plain_from_signed(1, {True: 2}, {1: 3}),
        lambda: plain_from_signed(1, {1: 2}, {1: 0}),
        lambda: signed_from_plain(1, {1: 2, 2: 3}),
        lambda: signed_from_plain(1, {1: 2, 2: 4, 3: 5}),
        lambda: reconstruct(5, 3, {1: 2}, {1: 2}),
        lambda: reconstruct(4, 2, {1: 2}, {1: 2}),
        lambda: reconstruct(5, 2, {1: 61}, {1: 12}),
    ]
    for call in malformed:
        try:
            call()
        except ValueError:
            pass
        else:
            raise AssertionError('Malformed input accepted')
    g, q, h = 10, 1000003, 8
    odd, degrees = indices(h)
    common = schedule(g, q, degrees)
    signed = schedule(g, q, list(range(1, h+1)) + odd)
    homogeneous = []
    for k in range(5):
        A, B = sum(n**k for n in range(1,h+1)), sum(n**k for n in odd)
        homogeneous.append({'power': k, 'plain': 2**k*A+B, 'signed': A+B,
                            'ratio': rational(Fraction(2**k*A+B, A+B)),
                            'limit': rational(Fraction(2**(k+1)+1, 3))})
    ratios = {name: rational(Fraction(common[name], signed[name])) for name in
              ('full_translations', 'formal_polynomial_term', 'formal_inversion_term')}
    omit = ('rows', 'degrees', 'g', 'q')
    return {
        'schema': 1,
        'scope': 'Transcript equivalence and conditional reconstruction; no new curve, order-finder, circuit or benchmark.',
        'transcript_roundtrips': transcript_roundtrips,
        'supplied_polynomial_reconstructions_each_route': len(reconstructed),
        'polynomial_controls': reconstructed,
        'genus_one_two_controls': 2,
        'independent_determinant_checks': determinant_checks,
        'homogeneous_cost_checks': homogeneous_checks,
        'malformed_controls': len(malformed),
        'cost_asymmetry_control': {'plain': general_cost_direct, 'signed': general_cost_signed},
        'genus_ten': {
            'g': g, 'q': q, 'h': h,
            'plain_degrees': degrees,
            'signed_curve_degrees': odd,
            'signed_twist_degrees': list(range(1,h+1)),
            'plain_common_backend': {k:v for k,v in common.items() if k not in omit},
            'signed_common_backend': {k:v for k,v in signed.items() if k not in omit},
            'formal_ratios_not_speedups': ratios,
            'homogeneous_sensitivity_not_gate_counts': homogeneous,
        },
    }


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
