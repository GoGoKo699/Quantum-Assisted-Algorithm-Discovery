"""Exact schedule arithmetic; no curve, point counter or quantum circuit is run."""
from __future__ import annotations
from functools import lru_cache
from math import comb, isqrt


def positive(x: int, name: str) -> int:
    if type(x) is not int or x < 1:
        raise ValueError(f'{name} must be a positive integer')
    return x


def ceil_log2(x: int) -> int:
    positive(x, 'log argument')
    return (x - 1).bit_length()


@lru_cache(None)
def sufficient_samples(rank: int, B: int, failure_inverse: int, denominator: int) -> int:
    """Minimum m for B Pr[Bin(m,1/denominator)<rank] <= 1/failure_inverse."""
    for x in (rank, B, failure_inverse, denominator):
        positive(x, 'sample-bound parameter')
    if denominator < 2:
        raise ValueError('denominator must be at least two')
    m = rank
    while True:
        numerator = sum(comb(m, j) * (denominator - 1) ** (m - j)
                        for j in range(rank))
        if B * failure_inverse * numerator <= denominator ** m:
            return m
        m += 1


def query(g: int, q: int, n: int, calls: int) -> dict:
    """Note 21's full-backend upper envelope for one genus-g field q^n call.

    q is an integer size parameter, not certified prime here. Characteristic,
    curve, sampler and reconstruction premises must be justified separately.
    """
    for x, name in ((g, 'genus'), (q, 'q'), (n, 'extension'), (calls, 'calls')):
        positive(x, name)
    if q < 3:
        raise ValueError('odd-characteristic size parameter must be >= 3')
    Q = q ** n
    root = isqrt(Q)
    root += root * root < Q
    U = (root + 1) ** (2 * g)
    B = ceil_log2(U)
    inv_eta = 100 * calls
    m = sufficient_samples(2 * g, B, inv_eta, 3)
    s = sufficient_samples(2 * g, B, inv_eta, 2)
    c = ceil_log2(m * B * inv_eta)
    a = 2 * B + ceil_log2(2 * m * c * inv_eta) + 4
    b = B + ceil_log2(2 * m * s * inv_eta) + 4
    initial = m * c * a
    full = initial + max(0, s - c) * m * b
    # For the q=p family: n prime-field coefficients per extension element.
    h = n * ceil_log2(q)
    W = 2 * g * h + ceil_log2(g + 1)
    return dict(n=n, B=B, m=m, s=s, c=c, a=a, b=b,
                initial_translations=initial, full_translations=full,
                coefficient_bits=h, accumulator_bits=W)


def schedule(g: int, q: int, degrees: list[int]) -> dict:
    """Aggregate exact count and two *formal* arithmetic envelope monomials.

    These monomials have no fitted multiplicative constants and are NOT gates,
    times, or a quantum/classical comparison. They weight full translations by
    g^3 (n ceil(log2 q))^2 and g (n ceil(log2 q))^3 respectively.
    """
    if not degrees:
        raise ValueError('nonempty declared schedule required')
    rows = [query(g, q, n, len(degrees)) for n in degrees]
    return dict(g=g, q=q, degrees=degrees, calls=len(rows), rows=rows,
                full_translations=sum(r['full_translations'] for r in rows),
                initial_translations=sum(r['initial_translations'] for r in rows),
                formal_polynomial_term=sum(r['full_translations'] * g**3 *
                                           r['coefficient_bits']**2 for r in rows),
                formal_inversion_term=sum(r['full_translations'] * g *
                                          r['coefficient_bits']**3 for r in rows),
                max_accumulator_bits=max(r['accumulator_bits'] for r in rows))


def reduction_degree(g: int, d: int) -> int:
    """Worst possible degree after a valid non-final Cantor reduction."""
    positive(g, 'genus')
    if type(d) is not int or not g < d <= 2 * g:
        raise ValueError('degree must be in (g,2g]')
    return max(2 * g + 1 - d, d - 2)


def precision_digits(g: int, p: int) -> int:
    """Sufficient residue precision from |a_i| <= 2^(2g) p^(g/2), i<=g.

    This verifies coefficient lifting only. Any native Frobenius implementation
    must additionally satisfy its own working-precision theorem.
    """
    positive(g, 'genus')
    positive(p, 'prime-size parameter')
    if p < 3:
        raise ValueError('p must be >= 3')
    k = 1
    while p ** (2 * k) <= (1 << (4 * g + 2)) * p ** g:
        k += 1
    return k
