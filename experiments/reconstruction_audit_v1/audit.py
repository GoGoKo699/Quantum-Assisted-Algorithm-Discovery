"""Independent arithmetic checks for Note 28; not an external peer review.

The main adversarial fixture is an irreducible degree-64 2-Weil polynomial.
Its membership in that class, irreducibility, and all supplied resultants are
checked without SymPy. Only q, g and integer counts reach the inherited decoder.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
DEPENDENCY = HERE.parent / 'all_field_reconstruction_v1' / 'reconstruct.py'
spec = importlib.util.spec_from_file_location('audited_reconstruction', DEPENDENCY)
subject = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = subject
spec.loader.exec_module(subject)


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def mod(a, b, p):
    a = [x % p for x in a]
    while a and a[-1] == 0: a.pop()
    while len(a) >= len(b):
        t = a[-1] * pow(b[-1], -1, p) % p
        shift = len(a) - len(b)
        for j, c in enumerate(b): a[j + shift] = (a[j + shift] - t * c) % p
        while a and a[-1] == 0: a.pop()
    return a


def gcd_poly(a, b, p):
    while b: a, b = b, mod(a, b, p)
    if not a: return []
    return [x * pow(a[-1], -1, p) % p for x in a]


def powmod(a, e, f, p):
    out = [1]
    while e:
        if e & 1: out = mod(mul(out, a), f, p)
        e >>= 1
        if e: a = mod(mul(a, a), f, p)
    return out


def determinant(a):
    """Fraction-free elimination, checking every exact division."""
    a = [row[:] for row in a]
    previous, sign, divisions = 1, 1, 0
    for k in range(len(a) - 1):
        r = next((r for r in range(k, len(a)) if a[r][k]), None)
        if r is None: return 0, divisions
        if r != k: a[k], a[r] = a[r], a[k]; sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                a[i][j], rem = divmod(a[i][j] * pivot - a[i][k] * a[k][j], previous)
                check(rem == 0, 'nonexact Bareiss division')
                divisions += 1
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1], divisions


def input_resultant(coefficients, n):
    """det(chi(S_n)), S_n a cyclic shift. Not the generating Sylvester routine.

    coefficients are low-to-high for P(T); chi(X)=X^(2g)P(1/X).
    Product chi(zeta) over n-th roots equals K_n because deg chi is even.
    """
    reduced = [0] * n
    for i, c in enumerate(reversed(coefficients)): reduced[i % n] += c
    return determinant([[reduced[(i - j) % n] for j in range(n)] for i in range(n)])


def digest(data):
    return hashlib.sha256(json.dumps(data, separators=(',', ':')).encode()).hexdigest()


def run():
    fixture = json.loads((HERE / 'CONTROL.json').read_text())
    diag = fixture['diagonal']; g = len(diag); q = fixture['q']; ell = fixture['prime']
    check((g, q, ell) == (32, 2, 7), 'unexpected fixture contract')
    fprev, f = [1], [-diag[0], 1]
    for a in diag[1:]: fprev, f = f, add(mul([-a, 1], f), [-x for x in fprev])
    check(f == fixture['real_weil_coefficients_low'], 'tridiagonal characteristic polynomial')
    # Leading principal minors prove +/- (11/4)I-A are positive definite.
    # Hence all roots of f lie strictly in (-11/4,11/4) inside (-2sqrt(2),2sqrt(2)).
    principal_minors = []
    for sign in (-1, 1):
        last, current = Q(1), Q(11, 4) - sign * diag[0]
        check(current > 0, 'first principal minor')
        for a in diag[1:]:
            last, current = current, (Q(11, 4) - sign * a) * current - last
            check(current > 0, 'nonpositive principal minor')
        principal_minors.append([current.numerator, current.denominator])
    check(Q(11, 4)**2 < 4*q, 'spectral margin')
    # Rabin criterion for degree 32: the sole prime dividing 32 is 2.
    fm = [v % ell for v in f]; z = [0, 1]; at16 = None
    for j in range(1, 33):
        z = powmod(z, ell, fm, ell)
        if j == 16: at16 = z[:]
    check(z == [0, 1], 'Frobenius^32 congruence')
    check(gcd_poly(fm, mod(add(at16, [0, -1]), fm, ell), ell) == [1],
          'Frobenius^16 gcd: real polynomial reducible')
    # P(T)=T^g f(T^-1+qT). Irreducible f with totally real roots and
    # t^2-4q<0 yields an irreducible degree-2g characteristic polynomial.
    P = [0] * (2*g + 1)
    for j, a in enumerate(f):
        for k in range(j + 1): P[g - j + 2*k] += a * comb(j, k) * q**k
    check(P == fixture['numerator_coefficients_low'], 'Weil transform')
    check(P[0] == 1 and P[-1] == q**g, 'normalization')
    check(all(P[2*g - i] == q**(g - i)*P[i] for i in range(g + 1)), 'reciprocity')
    required = sorted(set(range(1, g-1)) | set(range(2, 2*g-3, 2)))
    check(required == subject.query_indices(g), 'unexpected order set')
    K, divisions = {}, 0
    for n in required:
        actual, steps = input_resultant(P, n); divisions += steps
        check(actual > 0, 'nonpositive resultant')
        K[n] = actual
    check(digest(sorted(K.items())) == fixture['sympy_orders_sha256'],
          'circulant resultants disagree with the separately generated SymPy fingerprint')
    found, report = subject.reconstruct(q, g, K)
    check(found == P, 'decoder on irreducible input')
    exact_powers = [2*g]
    for n in range(1, g-1):
        exact_powers.append(-n*P[n] - sum(P[i]*exact_powers[n-i] for i in range(1, n)))
    check(report['powers'] == exact_powers, 'independent full-polynomial Newton recurrence')
    # Inspect actual rational logs and unnormalized truncation residues directly.
    h = g-2; tolerance = Q(1, 24*h*q**h)
    logs = {n: subject.log_enclosure(K[n], q**(g*n), tolerance)[0] for n in K}
    normal_errors = []
    q_bound_bits = 2*g + 2*g*h*max(1, (q-1).bit_length()) + 1
    check(max(v.bit_length() for v in K.values()) <= q_bound_bits, 'input-bit bound')
    term_cap = (192*g*h*q**h - 1).bit_length() + 1
    for row in report['log_rows']:
        check(-4*g <= row['binary_shift'] <= 2*g, 'promised binary shift bound')
        check(max(row['mantissa_terms'], row['log2_terms']) <= term_cap, 'term cap')
    for n in range(1, h+1):
        k = max(2, h//n)
        A = -Q(q**n, n)*sum((Q(subject.mobius(i), i)*logs[n*i].centre for i in range(1, k+1)), Q(0))
        error = abs(A - Q(exact_powers[n], n))
        check(error < subject.tail_bound(g, n) + Q(1, 24), 'actual normalized error')
        normal_errors.append(error)
    # Maximal legal centre shifts test the stated numerical budget, not float accuracy.
    original_log = subject.log_enclosure
    for policy in range(4):
        def displaced(num, den, tol, policy=policy):
            box, metadata = original_log(num, den, tol)
            sign = (1 if policy == 0 else -1 if policy == 1 else
                    (-1)**(num.bit_length() if policy == 2 else den.bit_length()))
            shift = sign*(tol-box.radius)
            return subject.Interval(box.centre+shift, tol), metadata
        subject.log_enclosure = displaced
        try: check(subject.reconstruct(q, g, K)[0] == P, 'permitted log error changed output')
        finally: subject.log_enclosure = original_log
    # Decoder acceptance is not order authentication: a one-unit change in K_60
    # remains below the analytic/numerical tolerance and need not change the output.
    corrupted = dict(K); corrupted[max(K)] += 1
    accepted = subject.reconstruct(q, g, corrupted)[0]
    check(accepted == P, 'authentication-boundary fixture changed')
    check(input_resultant(accepted, max(K))[0] != corrupted[max(K)], 'corruption not demonstrated')
    # Independent checking of a precisely stated endpoint promise (not all algebraic claims).
    Rp = K[1]-sum((1+q**(g-i))*P[i] for i in range(g-1))
    Rm = (K[2]//K[1])-sum((-1)**i*(1+q**(g-i))*P[i] for i in range(g-1))
    check(Rp == (q+1)*P[g-1]+P[g], 'endpoint plus')
    check((-1)**(g-1)*Rm == (q+1)*P[g-1]-P[g], 'endpoint minus')
    return {
        'schema': 1,
        'scope': 'Internal proof rederivation and independently generated exact controls; not external peer review.',
        'theorem_threshold_unchanged': 32,
        'q': q, 'g': g, 'irreducible_real_degree': g, 'irreducible_weil_degree': 2*g,
        'irreducibility_modulus': ell, 'positive_principal_minors_checked': 2*g,
        'final_principal_minors': principal_minors,
        'circulant_resultants_checked': len(K), 'exact_Bareiss_divisions': divisions,
        'reconstructed_coefficients': len(P), 'independent_power_sums': len(exact_powers)-1,
        'legal_numerical_displacement_runs': 4,
        'one_corrupted_count_accepted_by_decoder': True,
        'same_corruption_detected_by_resultant_replay': True,
        'max_input_bits': max(v.bit_length() for v in K.values()), 'proved_input_bit_cap': q_bound_bits,
        'max_log_terms': max(max(r['mantissa_terms'], r['log2_terms']) for r in report['log_rows']),
        'proved_log_term_cap': term_cap,
        'polynomial_sha256': digest(P),
        'known_curve_or_abelian_realization': 'not asserted',
        'quantum_or_native_curve_computation': 'not executed'
    }


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
