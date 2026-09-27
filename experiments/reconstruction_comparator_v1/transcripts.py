"""Exact dyadic transcript conversion and conditional zeta reconstruction.

This does not compute or authenticate a Jacobian cardinality. True input orders,
a reciprocal Weil polynomial, and the declared field hypotheses remain premises.
All transcript values are ordinary classical integers; there is no quantum code.
"""
from __future__ import annotations
from fractions import Fraction
from math import isqrt
from typing import Mapping


def positive(value: int, name: str) -> int:
    if type(value) is not int or value < 1:
        raise ValueError(f'{name} must be a positive integer')
    return value


def indices(h: int) -> tuple[list[int], list[int]]:
    """Return odd anchors O_h and plain-query degrees O_h union 2[1,h]."""
    positive(h, 'h')
    odd = list(range(1, h + 1, 2))
    return odd, sorted(odd + list(range(2, 2 * h + 1, 2)))


def checked(data: Mapping[int, int], required: list[int], label: str) -> dict[int, int]:
    out = dict(data)
    if any(type(key) is not int for key in out) or set(out) != set(required):
        raise ValueError(f'{label} has missing, extra, or invalid keys')
    for value in out.values():
        positive(value, label + ' value')
    return out


def divide(numerator: int, denominator: int) -> int:
    value, remainder = divmod(numerator, denominator)
    if remainder or value < 1:
        raise ValueError('Required cardinality quotient is not a positive integer')
    return value


def plain_from_signed(h: int, anchors: Mapping[int, int],
                      twists: Mapping[int, int]) -> dict[int, int]:
    """Recover every requested K_j by K_(2n)=K_n*T_n, in increasing n."""
    odd, degrees = indices(h)
    values = checked(anchors, odd, 'odd anchors')
    twist = checked(twists, list(range(1, h + 1)), 'twists')
    for n in range(1, h + 1):
        values[2 * n] = values[n] * twist[n]
    return {n: values[n] for n in degrees}


def signed_from_plain(h: int, orders: Mapping[int, int]) -> tuple[dict, dict]:
    """Recover the signed transcript with checked exact integer divisions."""
    odd, degrees = indices(h)
    values = checked(orders, degrees, 'plain orders')
    return ({n: values[n] for n in odd},
            {n: divide(values[2 * n], values[n]) for n in range(1, h + 1)})


def trace(q: int, g: int, n: int, K: int, T: int) -> int:
    """Certified rational logarithm and analytic Weil-tail enclosure.

    An empty or multi-integer enclosure is an error, not a rounded guess. The
    enclosure authenticates no input orders and proves no curve-realizability.
    """
    Q = q ** n
    z = Fraction(T - K, T + K)
    partial = Fraction(0)
    term = z
    # Bound can stop early for z=0; cap is an explicit arithmetic safety limit.
    for j in range(10000):
        partial += Q * term / (2 * j + 1)
        term *= z * z
        numerical = Q * abs(term) / ((2 * j + 3) * (1 - z * z))
        if numerical <= Fraction(1, 12):
            break
    else:
        raise ValueError('Rational logarithm term cap exceeded')
    s = isqrt(Q)
    ceil_sqrt = s + (s * s < Q)
    analytic = Fraction(2 * g * ceil_sqrt, 3 * (Q - 1))
    lower, upper = partial - numerical - analytic, partial + numerical + analytic
    first = -((-lower.numerator) // lower.denominator)
    last = upper.numerator // upper.denominator
    if first != last:
        raise ValueError('Trace interval does not isolate one integer')
    return first


def reconstruct(q: int, g: int, anchors: Mapping[int, int],
                twists: Mapping[int, int]) -> list[int]:
    """Endpoint-completed reconstruction under inherited sufficient hypotheses.

    Genus one uses K_1 alone. Genus two uses K_1,T_1 without a size threshold.
    For g>=3 require odd q>=64g^2. Primality/prime-power recognition is not done:
    q is a supplied field-size parameter, not an authenticated finite field.
    """
    positive(q, 'q'); positive(g, 'genus')
    if q < 3 or q % 2 == 0:
        raise ValueError('Odd field-size parameter at least three required')
    if g == 1:
        K = checked(anchors, [1], 'genus-one order')[1]
        checked(twists, [], 'genus-one twists')
        return [1, K - q - 1, q]
    if g >= 3 and q < 64 * g * g:
        raise ValueError('Inherited sufficient field-size condition not met')
    h = max(1, g - 2)
    K = plain_from_signed(h, anchors, twists)
    powers = [0] + [trace(q, g, n, K[n], twists[n]) for n in range(1, g - 1)]
    coefficients = [1]
    for k in range(1, g - 1):
        numerator = -sum(coefficients[k - i] * powers[i] for i in range(1, k + 1))
        value, rem = divmod(numerator, k)
        if rem:
            raise ValueError('Newton integrality failed')
        coefficients.append(value)
    R_plus = K[1] - sum((1 + q ** (g - i)) * coefficients[i] for i in range(g - 1))
    R_minus = twists[1] - sum((-1) ** i * (1 + q ** (g - i)) * coefficients[i]
                              for i in range(g - 1))
    sign = (-1) ** (g - 1)
    penultimate, rem1 = divmod(R_plus + sign * R_minus, 2 * (q + 1))
    middle, rem2 = divmod(R_plus - sign * R_minus, 2)
    if rem1 or rem2:
        raise ValueError('Endpoint integrality failed')
    coefficients.extend([penultimate, middle])
    coefficients.extend(q ** (g - i) * coefficients[i] for i in range(g - 1, -1, -1))
    return coefficients
