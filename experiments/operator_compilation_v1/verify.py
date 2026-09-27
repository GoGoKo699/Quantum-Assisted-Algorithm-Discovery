#!/usr/bin/env python3
"""Exact finite checks of the conditional matrix argument, not a quantum simulator.

Python 3.10+, standard library only. No inputs or stored reports are changed.
The proof and the omitted finite-precision work are described in the linked note.
"""
from fractions import Fraction as F
import json
import sys

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(a, b))


def scale(c, a):
    return tuple(tuple(c * x for x in r) for r in a)


def sub(a, b):
    return add(a, scale(-1, b))


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(r, c)) for c in transpose(b)) for r in a)


def congruence(w, a):
    return mul(mul(w, a), transpose(w))


def matrix(a, b, c, d):
    return ((F(a), F(b)), (F(c), F(d)))


def psd(a):
    """Exact PSD criterion for a real symmetric 2-by-2 matrix."""
    return a[0][1] == a[1][0] and a[0][0] >= 0 and a[1][1] >= 0 and a[0][0] * a[1][1] - a[0][1] ** 2 >= 0


def inverse(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if not det:
        raise ValueError("Singular control matrix")
    return scale(1 / det, ((a[1][1], -a[0][1]), (-a[1][0], a[0][0])))


def quadratic(a, b):
    return mul(mul(transpose(b), a), b)[0][0]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    ident = matrix(1, 0, 0, 1)
    zero = scale(0, ident)
    factors = [matrix(1, 0, 0, 1), matrix(2, 0, 1, 1), matrix(F(1, 2), 0, -2, 3)]
    normalized = [matrix(F(1, 2), 0, 0, F(3, 4)), matrix(F(2, 3), F(1, 6), F(1, 6), F(2, 3)), matrix(F(3, 4), F(1, 8), F(1, 8), F(1, 2))]
    shapes = [zero, ident, scale(-1, ident), matrix(0, 1, 1, 0), matrix(F(1, 2), F(1, 2), F(1, 2), -F(1, 2))]
    rhs = [((F(x),), (F(y),)) for x, y in [(1, 0), (0, 1), (1, 1), (2, -1)]]
    counts = {"congruence_cases": 0, "noncommuting_cases": 0, "final_relative_cases": 0, "rhs_checks": 0, "polarization_checks": 0, "scalar_schedules": 0, "amplitude_bound_checks": 0, "negative_control_checks": 0}
    for w in factors:
        h = congruence(w, ident)
        for m in normalized:
            require(psd(sub(m, scale(F(1, 3), ident))) and psd(sub(ident, m)), "Normalized control outside [I/3,I]")
            g = congruence(w, m)
            require(psd(sub(h, g)), "Control upper bound")
            # Recover the off-diagonal from e_j and (e_1+e_2)/sqrt(2).
            plus_energy = (m[0][0] + 2 * m[0][1] + m[1][1]) / 2
            require(plus_energy - (m[0][0] + m[1][1]) / 2 == m[0][1], "Polarization")
            counts["polarization_checks"] += 1
            for shape in shapes:
                require(psd(sub(ident, shape)) and psd(add(ident, shape)), "Invalid bounded perturbation")
                tau = F(1, 8)
                e = add(m, scale(tau, shape))
                new_h = congruence(w, add(e, scale(tau, ident)))
                require(psd(sub(new_h, g)), "Lost upper bound")
                require(psd(sub(add(g, scale(2 * tau, h)), new_h)), "Contraction failed")
                counts["congruence_cases"] += 1
                counts["noncommuting_cases"] += mul(h, g) != mul(g, h)
                eps = F(1, 10)
                tau_f = eps / 6
                final_h = congruence(w, add(add(m, scale(tau_f, shape)), scale(tau_f, ident)))
                require(psd(sub(final_h, g)) and psd(sub(scale(1 + eps, g), final_h)), "Final relative bound")
                counts["final_relative_cases"] += 1
                for b in rhs:
                    x, y = mul(inverse(g), b), mul(inverse(final_h), b)
                    err = sub(y, x)
                    require(quadratic(g, err) <= (eps / (1 + eps)) ** 2 * quadratic(g, x), "Classical solve bound")
                    counts["rhs_checks"] += 1
            # Omitting the safety shift breaks the invariant for an allowed error.
            bad = congruence(w, sub(m, scale(F(1, 8), ident)))
            require(not psd(sub(bad, g)), "Negative control did not break invariant")
            counts["negative_control_checks"] += 1
    for c0 in [F(1), F(2), F(17), F(1025), F(10**12)]:
        steps, power = 0, 1
        while power < c0:
            power *= 4
            steps += 1
        c = c0
        for _ in range(steps):
            c = 1 + c / 4
        require(c <= F(7, 3) < 3, "Scalar contraction schedule")
        for eps in [F(1, 2), F(1, 10), F(1, 100)]:
            require(1 + (eps / 3) * c <= 1 + eps, "Final scalar envelope")
            counts["scalar_schedules"] += 1
    # pi < 4 yields N*AE_error <= 8*sqrt(N)/T + 16*N/T^2.
    for root_n in [1, 2, 16, 1024]:
        for eta in [F(1, 2), F(1, 10), F(1, 100)]:
            t = 1
            while t < 16 * root_n / eta:
                t *= 2
            bound = F(8 * root_n, t) + F(16 * root_n**2, t**2)
            require(bound <= eta, "Amplitude-estimation sufficient budget")
            counts["amplitude_bound_checks"] += 1
    print(json.dumps({"status": "pass", "arithmetic": "exact rational", "scope": "finite algebra controls only; no amplitude estimation, gate simulation, or input-access implementation", **counts}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
