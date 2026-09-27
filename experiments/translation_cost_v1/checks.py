"""Independent checks of arithmetic bounds, not an arithmetic-circuit simulator."""
from fractions import Fraction
from math import comb
import json
from cost import (ceil_log2, sufficient_samples, query, schedule,
                  reduction_degree, precision_digits)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def convolution_tail(m, rank, den):
    # Independent repeated Bernoulli convolution, no binomial formula.
    distribution = [Fraction(1)]
    for _ in range(m):
        nxt = [Fraction(0)] * (len(distribution) + 1)
        for j, prob in enumerate(distribution):
            nxt[j] += prob * Fraction(den - 1, den)
            nxt[j + 1] += prob / den
        distribution = nxt
    return sum(distribution[:rank])


def run():
    log_checks = 0
    for x in range(1, 4097):
        e = ceil_log2(x)
        require(2**e >= x and (e == 0 or 2**(e-1) < x), 'ceiling logarithm')
        log_checks += 1
    tails = 0
    for rank in (1, 2, 4, 8):
        for B in (1, 7, 100):
            for inv in (3, 100):
                for den in (2, 3):
                    m = sufficient_samples(rank, B, inv, den)
                    require(B * inv * convolution_tail(m, rank, den) <= 1, 'tail failed')
                    require(B * inv * convolution_tail(m-1, rank, den) > 1, 'not minimal')
                    tails += 1
    degree_checks = 0
    for g in range(1, 65):
        for d in range(g+1, 2*g+1):
            bound = reduction_degree(g, d)
            require(bound < d, 'reduction must decrease')
            # Check every possible numerator degree f-v^2 against this bound.
            for vd in range(d):
                quotient_degree = max(2*g+1, 2*vd) - d
                require(quotient_degree <= bound, 'degree bound missed a case')
            degree_checks += 1
        d, steps = 2*g, 0
        while d > g:
            d = reduction_degree(g, d)
            steps += 1
        require(steps <= g, 'more than g padded reductions needed')
    precisions = []
    for g in (1, 2, 4, 8, 16, 32, 64):
        for p in (3, 5, 17, 257, 65537, 1000003):
            k = precision_digits(g, p)
            threshold = (1 << (4*g+2)) * p**g
            require(p**(2*k) > threshold and p**(2*(k-1)) <= threshold,
                    'precision strictness/minimality')
            require(p**(2*k) > 4 * comb(2*g, g)**2 * p**g,
                    'coefficient lifting bound')
            precisions.append(dict(g=g, p=p, coefficient_digits=k,
                                   harvey_theorem_1_inequality=p > (2*k-1)*(2*g+1)))
    generic = schedule(10, 1000003, list(range(1, 21)))
    # Note 19: twist orders at all degrees 1..g, original curve at odd degrees.
    twist = schedule(10, 1000003, list(range(1, 11)) + list(range(1, 11, 2)))
    require(generic['full_translations'] == 665651460, 'note 21 generic count')
    require(twist['full_translations'] == 240901313, 'note 21 twist count')
    # The 4,000/8,000-bit coefficient data excludes degree tags and scratch.
    for table in (generic, twist):
        for row in table['rows']:
            require(row['full_translations'] >= row['initial_translations'], 'stages')
            require(row['accumulator_bits'] == 2*table['g']*row['coefficient_bits']+4,
                    'tag accounting')
    failures = 0
    for action in (lambda: ceil_log2(0), lambda: ceil_log2(True),
                   lambda: query(0, 7, 1, 1), lambda: query(1, 2, 1, 1),
                   lambda: schedule(1, 7, []), lambda: reduction_degree(3, 3),
                   lambda: reduction_degree(3, 7), lambda: precision_digits(1, 2)):
        try:
            action()
        except ValueError:
            failures += 1
        else:
            raise AssertionError('invalid input accepted')
    ratios = {}
    for name in ('full_translations', 'formal_polynomial_term', 'formal_inversion_term'):
        ratio = Fraction(generic[name], twist[name])
        ratios[name] = dict(numerator=ratio.numerator, denominator=ratio.denominator)
    return dict(schema=1, scope='Arithmetic audit only; no native point counter or quantum circuit.',
                log_checks=log_checks, independent_sample_bounds=tails,
                reduction_degree_checks=degree_checks, invalid_controls=failures,
                coefficient_precision_checks=precisions, generic_schedule={k: v for k, v in generic.items() if k != "rows"},
                twist_schedule={k: v for k, v in twist.items() if k != "rows"},
                query_rows_checked=35, formal_ratios_not_speedups=ratios)


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, separators=(",", ":")))
