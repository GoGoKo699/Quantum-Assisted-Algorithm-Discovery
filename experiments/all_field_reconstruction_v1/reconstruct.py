"""Ordinary-count reconstruction for g>=32 and all integer q>=2.

The theorem assumes a supplied reciprocal integral Weil polynomial of degree 2g
and TRUE cyclic resultants. This module neither computes/authenticates group
orders nor certifies that arbitrary returned integers belong to a curve.
No source equation, twist oracle, known polynomial or factorization is an input.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Mapping


@dataclass(frozen=True)
class Interval:
    centre: Fraction
    radius: Fraction


class InvalidData(ValueError):
    """Malformed input or failed arithmetic consistency/rounding test."""


def integer(x: int, name: str, minimum: int) -> int:
    if type(x) is not int or x < minimum:
        raise InvalidData(f'{name} must be an integer >= {minimum}')
    return x


def query_indices(g: int) -> list[int]:
    integer(g, 'genus', 32)
    h = g - 2
    return sorted(set(range(1, h + 1)) | set(range(2, 2 * h + 1, 2)))


def mobius(n: int) -> int:
    integer(n, 'Mobius argument', 1)
    value, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    return -value if n > 1 else value


def tail_bound(g: int, n: int) -> Fraction:
    """Uniform-in-q bound for the error in S_n/n, NOT in S_n."""
    integer(g, 'genus', 32)
    integer(n, 'trace index', 1)
    h = g - 2
    if n > h:
        raise InvalidData('trace index exceeds g-2')
    k = max(2, h // n)
    t = Fraction(5, 7) ** n  # 1/sqrt(q) <= 1/sqrt(2) < 5/7.
    return Fraction(2 * g * k, n * (k + 1)) * t ** (k - 1) / (1 - t)


@lru_cache(maxsize=256)
def short_log(x: Fraction, tolerance: Fraction) -> tuple[Interval, int]:
    """2*atanh((x-1)/(x+1)) with a rational enclosure and |z|<=1/3."""
    if not 1 <= x <= 2 or tolerance <= 0:
        raise InvalidData('short-log domain or tolerance')
    z = (x - 1) / (x + 1)
    value, term = Fraction(0), z
    j = 0
    while True:
        value += 2 * term / (2 * j + 1)
        term *= z * z
        j += 1
        remainder = 2 * abs(term) / ((2 * j + 1) * (1 - z * z))
        if remainder <= tolerance:
            return Interval(value, remainder), j


def log_enclosure(num: int, den: int, tolerance: Fraction) -> tuple[Interval, dict]:
    """Range-reduced log(num/den); avoids a near-unit atanh argument at small q."""
    integer(num, 'log numerator', 1)
    integer(den, 'log denominator', 1)
    if tolerance <= 0:
        raise InvalidData('positive log tolerance required')
    e = num.bit_length() - den.bit_length()
    x = Fraction(num, den)
    mantissa = x / (1 << e) if e >= 0 else x * (1 << (-e))
    if mantissa < 1:
        e -= 1
        mantissa *= 2
    if not 1 <= mantissa < 2:
        raise InvalidData('binary log range reduction failed')
    reduced, terms = short_log(mantissa, tolerance / 2)
    unit, unit_terms = short_log(Fraction(2), tolerance / (2 * max(1, abs(e))))
    result = Interval(reduced.centre + e * unit.centre,
                      reduced.radius + abs(e) * unit.radius)
    if result.radius > tolerance:
        raise InvalidData('log enclosure exceeded its allowance')
    return result, dict(binary_shift=e, mantissa_terms=terms, log2_terms=unit_terms)


def unique_integer(interval: Interval) -> int:
    if interval.radius < 0:
        raise InvalidData('negative radius')
    lo = interval.centre - interval.radius
    hi = interval.centre + interval.radius
    first = -((-lo.numerator) // lo.denominator)
    last = hi.numerator // hi.denominator
    if first != last:
        raise InvalidData('interval does not contain exactly one integer')
    return first


def reconstruct(q: int, g: int, supplied_orders: Mapping[int, int]) -> tuple[list[int], dict]:
    """Recover all coefficients, conditional on the mathematical input promise.

    A malformed input can pass the consistency checks. Acceptance is NOT a
    certificate that the supplied orders or the resulting polynomial are real.
    """
    integer(q, 'field-size parameter', 2)
    required = query_indices(g)
    data = dict(supplied_orders)
    if any(type(n) is not int for n in data) or set(data) != set(required):
        raise InvalidData('order keys differ from the declared query set')
    for value in data.values():
        integer(value, 'supplied cardinality', 1)
    h = g - 2
    log_tolerance = Fraction(1, 24 * q ** h * h)
    logs, log_rows = {}, []
    for j in required:
        logs[j], details = log_enclosure(data[j], q ** (g * j), log_tolerance)
        log_rows.append(dict(index=j, **details))
    mu = [0] + [mobius(i) for i in range(1, h + 1)]
    coefficients, powers, rows = [1], [2 * g], []
    for n in range(1, h + 1):
        k = max(2, h // n)
        centre, error = Fraction(0), Fraction(0)
        for i in range(1, k + 1):
            weight = Fraction(-q ** n * mu[i], n * i)
            value = logs[n * i]
            centre += weight * value.centre
            error += abs(weight) * value.radius
        analytic = tail_bound(g, n)
        if analytic >= Fraction(1, 3) or error > Fraction(1, 24):
            raise InvalidData('proved analytic/numerical envelope violated')
        known_sum = sum(coefficients[n-i] * powers[i] for i in range(1, n))
        # Newton determines S_n modulo n: round the coefficient, not S_n.
        interval = Interval(-centre - Fraction(known_sum, n), analytic + error)
        coefficient = unique_integer(interval)
        coefficients.append(coefficient)
        powers.append(-n * coefficient - known_sum)
        rows.append(dict(n=n, cutoff=k,
                         analytic_numerator=analytic.numerator,
                         analytic_denominator=analytic.denominator))
    T1, remainder = divmod(data[2], data[1])
    if remainder or T1 <= 0:
        raise InvalidData('K_2/K_1 is not a positive integer')
    R_plus = data[1] - sum((1 + q ** (g-i)) * coefficients[i] for i in range(g-1))
    R_minus = T1 - sum((-1)**i * (1 + q ** (g-i)) * coefficients[i]
                      for i in range(g-1))
    penultimate, r1 = divmod(R_plus + (-1)**(g-1) * R_minus, 2 * (q + 1))
    middle, r2 = divmod(R_plus - (-1)**(g-1) * R_minus, 2)
    if r1 or r2:
        raise InvalidData('endpoint integrality failed')
    coefficients.extend((penultimate, middle))
    coefficients.extend(q ** (g-i) * coefficients[i] for i in range(g-1, -1, -1))
    return coefficients, dict(query_count=len(required), max_degree=max(required),
                              log_rows=log_rows, trace_rows=rows, powers=powers)
