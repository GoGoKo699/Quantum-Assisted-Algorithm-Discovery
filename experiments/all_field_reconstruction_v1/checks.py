"""Targeted independent controls for the all-field reconstruction theorem.

Examples are supplied Weil polynomials, not newly counted Jacobians or a claim
that these polynomials are realized by curves. Full proofs are in Note 28.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd
from decimal import Decimal, localcontext
import hashlib
import json
from reconstruct import (Interval, InvalidData, query_indices, tail_bound,
                         mobius, reconstruct, log_enclosure, unique_integer)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def expect_error(call):
    try:
        call()
    except InvalidData:
        return
    raise AssertionError('Expected rejection')


def multiply_polynomials(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def make_control(q, traces, blocks, maximum):
    """Build quadratic and cyclotomic-shaped Weil factors by integer formulas.

    Quadratic factors are 1-t*T+q*T^2 with t^2<=4q.
    A block of size a is 1+q^a*T^(2a), all inverse roots of magnitude sqrt(q).
    Resultants are computed factorwise; the decoder is not given these factors.
    """
    P = [1]
    K = {n: 1 for n in range(1, maximum+1)}
    powers = [0] * (maximum+1)
    for t in traces:
        require(t*t <= 4*q, 'Not a quadratic Weil factor')
        P = multiply_polynomials(P, [1, -t, q])
        s = [2, t]
        for n in range(2, maximum+1):
            s.append(t*s[-1]-q*s[-2])
        for n in K:
            K[n] *= 1-s[n]+q**n
            powers[n] += s[n]
    for a in blocks:
        factor = [1] + [0]*(2*a-1) + [q**a]
        P = multiply_polynomials(P, factor)
        for n in K:
            d = gcd(2*a, n)
            K[n] *= (1-(-q**a)**(n//d))**d
            if n % (2*a) == 0:
                powers[n] += 2*a*(-q**a)**(n//(2*a))
    g = len(P)//2
    require(len(P) == 2*g+1 and P[-1] == q**g, 'Degree or leading term')
    require(all(P[2*g-i] == q**(g-i)*P[i] for i in range(g+1)), 'Reciprocity')
    require(all(x > 0 for x in K.values()), 'Nonpositive resultant')
    # Independent full polynomial Newton recurrence versus factor traces.
    for n in range(1, min(maximum, 2*g)+1):
        require(powers[n] + sum(P[i]*powers[n-i] for i in range(1,n)) + n*P[n] == 0,
                'Full-polynomial Newton check disagrees with factor power sums')
    return P, K, powers


def matrix_product(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def determinant(A):
    A = [r[:] for r in A]
    previous, sign = 1, 1
    for k in range(len(A)-1):
        pivot = next((i for i in range(k,len(A)) if A[i][k]),None)
        if pivot is None:
            return 0
        if pivot != k:
            A[pivot],A[k] = A[k],A[pivot]
            sign = -sign
        value = A[k][k]
        for i in range(k+1,len(A)):
            for j in range(k+1,len(A)):
                A[i][j],r = divmod(A[i][j]*value-A[i][k]*A[k][j],previous)
                require(r == 0, 'Nonexact determinant elimination')
            A[i][k] = 0
        previous = value
    return sign*A[-1][-1]


def companion_orders(P, maximum):
    d = len(P)-1
    C = [[0]*d for _ in range(d)]
    for i in range(d-1):
        C[i][i+1] = 1
    C[-1] = [-c for c in reversed(P[1:])]
    A = [[int(i==j) for j in range(d)] for i in range(d)]
    result = {}
    for n in range(1,maximum+1):
        A = matrix_product(A,C)
        result[n] = determinant([[int(i==j)-A[i][j] for j in range(d)] for i in range(d)])
    return result


def encoded_hash(value):
    return hashlib.sha256(json.dumps(value,separators=(',',':')).encode()).hexdigest()


def run():
    rho = F(5,7)
    anchors = [F(64,15)*rho**10/(1-rho**10),
               F(64,5)*rho**15/(1-rho**5),224*rho**20]
    require(all(b<F(1,3) for b in anchors), 'Uniform tail anchors')
    parameter_checks = 0
    for g in range(32,97):
        h = g-2
        degrees = query_indices(g)
        require(len(degrees)==h+(h+1)//2 and max(degrees)==2*h, 'Count or degree')
        for n in range(1,h+1):
            k = max(2,h//n)
            require(all(n*i in degrees for i in range(1,k+1)), 'Hidden oracle query')
            require(tail_bound(g,n)<F(1,3), 'Uniform tail bound')
            parameter_checks += 1
    # Independently count squarefree divisor subsets to verify Mobius values.
    mobius_checks = 0
    for n in range(1,129):
        divisors = [d for d in range(1,n+1) if n%d==0]
        require(sum(mobius(d) for d in divisors)==int(n==1), 'Mobius inversion')
        mobius_checks += 1
    # Distinct supplied-control families include the smallest supported genus,
    # characteristic-two-size parameters, higher-degree factors and repeated roots.
    definitions = [
        (2, [1]*32, []),
        (2, [], [32]),
        (2, [((3*i)%5)-2 for i in range(33)], []),
        (3, [-3,0,1,2]*8, []),
        (4, [4]*32, []),
        (5, [((7*i)%9)-4 for i in range(16)], [16]),
        (2, [0,1,-1,2,-2,1,0,-1]*2, [32]),
    ]
    control_rows = []
    total_coefficients = total_traces = 0
    for q,traces,blocks in definitions:
        g = len(traces)+sum(blocks)
        degrees = query_indices(g)
        P,K,S = make_control(q,traces,blocks,max(degrees))
        requested = {n:K[n] for n in degrees}
        found,receipt = reconstruct(q,g,requested)
        require(found == P, 'Reconstructed polynomial differs')
        require(receipt['powers'][1:] == S[1:g-1], 'Recovered power sums differ')
        total_coefficients += len(P)
        total_traces += g-2
        control_rows.append(dict(q=q,g=g,traces=traces,blocks=blocks,
                                 queries=receipt['query_count'],maximum_degree=max(degrees),
                                 recovered_coefficients_sha256=encoded_hash(found),
                                 input_orders_sha256=encoded_hash(requested),
                                 largest_order_bits=max(K[n].bit_length() for n in degrees),
                                 largest_log_series=max(max(r['mantissa_terms'],r['log2_terms'])
                                                        for r in receipt['log_rows'])))
    # The independent determinant check is deliberately small and is NOT a
    # genus-32 native counter: it checks the separate resultant-construction oracle.
    determinant_checks = 0
    for q,traces,blocks in [(2,[1,-2],[]),(3,[],[3]),(5,[2],[2])]:
        P,K,_=make_control(q,traces,blocks,12)
        require(companion_orders(P,12)==K,'Companion/factor resultant disagreement')
        determinant_checks += 12
    log_checks = 0
    shifts = []
    for num,den in [(1,1),(1,2),(2,1),(3,7),(7,3),(1,2**4096),(2**4096,1)]:
        interval,meta=log_enclosure(num,den,F(1,2**64))
        # Secondary numerical check only; the enclosure guarantee is the series
        # proof. Decimal precision is far finer than the requested enclosure.
        with localcontext() as context:
            context.prec=160
            actual=(Decimal(num)/Decimal(den)).ln()
            centre=Decimal(interval.centre.numerator)/Decimal(interval.centre.denominator)
            radius=Decimal(interval.radius.numerator)/Decimal(interval.radius.denominator)
            require(abs(actual-centre)<=radius+Decimal('1e-140'), 'Decimal log spot check')
        inverse,_=log_enclosure(den,num,F(1,2**64))
        require(abs(interval.centre+inverse.centre)<=interval.radius+inverse.radius,
                'Exact log inversion enclosures disagree')
        log_checks += 1
        shifts.append(meta)
    # Congruence-aware rounding: error<1/2 in S_n/n need not bound S_n by 1/2.
    require(unique_integer(Interval(F(7,3),F(1,3))) == 2, 'Coefficient lattice control')
    failures=[lambda:query_indices(31),lambda:query_indices(True),
              lambda:tail_bound(32,31),lambda:log_enclosure(0,1,F(1,10)),
              lambda:log_enclosure(1,1,F(0)),lambda:unique_integer(Interval(F(1,2),F(1,2))),
              lambda:reconstruct(1,32,{}),lambda:reconstruct(2,32,{}),
              lambda:reconstruct(2,32,{n:0 for n in query_indices(32)}),
              lambda:reconstruct(2,32,{n:1 for n in query_indices(32)}),
              lambda:reconstruct(2,32,{**{n:1 for n in query_indices(32)},100:1})]
    for failure in failures:
        expect_error(failure)
    return dict(schema=1,scope='Supplied-polynomial reconstruction, not a curve/Jacobian/quantum run.',
                uniform_anchor_bounds=[{'numerator':v.numerator,'denominator':v.denominator} for v in anchors],
                finite_parameter_checks=parameter_checks,mobius_checks=mobius_checks,
                reconstructed_controls=control_rows,total_recovered_coefficients=total_coefficients,
                total_recovered_traces=total_traces,independent_determinant_checks=determinant_checks,
                logarithm_spot_checks=log_checks,logarithm_range_reductions=shifts,
                malformed_controls=len(failures),congruence_rounding_controls=1)


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
