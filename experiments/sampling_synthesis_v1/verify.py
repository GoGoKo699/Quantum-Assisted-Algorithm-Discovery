#!/usr/bin/env python3
"""Finite contract checks, not Manthan, a SAT solver, or a performance test.

Independently written; Python 3.10+, standard library only. No file writes.
The amplitude calculation is exact ideal-state algebra on three bits only.
It does not compile gates, simulate noise, or implement a resource-efficient oracle.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import product
import json
import sys

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def relation(mask: int, x: int, y: int) -> bool:
    return bool((mask >> (2 * x + y)) & 1)


def check_verification_contract() -> dict:
    accepted = rejected = 0
    # Every relation on two input bits and one output bit, and every X-only map.
    for mask in range(256):
        for candidate in product(range(2), repeat=4):
            direct = all(not any(relation(mask, x, y) for y in range(2))
                         or relation(mask, x, candidate[x]) for x in range(4))
            counterexamples = [(x, y) for x in range(4) for y in range(2)
                               if relation(mask, x, y)
                               and not relation(mask, x, candidate[x])]
            require(direct == (not counterexamples), "Verifier/domain mismatch")
            accepted += direct
            rejected += not direct
    require((accepted, rejected) == (1296, 2800), "Enumeration count mismatch")
    return {"relations": 256, "candidates_per_relation": 16,
            "accepted": accepted, "rejected": rejected}


def step(coefficients: list[F], weights: list[F], good: list[bool]) -> list[F]:
    # State amplitude at j is sqrt(weights[j])*coefficients[j].
    # Mark good states, then reflect around the initially prepared product state.
    marked = [-b if valid else b for b, valid in zip(coefficients, good)]
    mean = sum((w * b for w, b in zip(weights, marked)), F(0))
    return [2 * mean - b for b in marked]


def check_conditioning() -> dict:
    # Joint labels are two X bits and one Y bit; no auxiliary variables exist.
    laws = [[F(1, 8)] * 8,
            [F(1, 4) * (F(9, 10) if j % 2 else F(1, 10)) for j in range(8)]]
    rounds = positive = zero = marginal_checks = 0
    for weights in laws:
        require(sum(weights) == 1 and min(weights) > 0, "Invalid prior")
        for mask in range(1, 256):
            good = [bool((mask >> j) & 1) for j in range(8)]
            mass = sum((w for w, g in zip(weights, good) if g), F(0))
            b = [F(1)] * 8
            for _ in range(4):
                probabilities = [w * c * c for w, c in zip(weights, b)]
                require(sum(probabilities) == 1, "Norm failure")
                success = sum((p for p, g in zip(probabilities, good) if g), F(0))
                rounds += 1
                if success:
                    positive += 1
                    for j in range(8):
                        if good[j]:
                            require(probabilities[j] / success == weights[j] / mass,
                                    "Conditional weighted law changed")
                    for x in range(4):
                        actual = sum((probabilities[2*x+y] for y in range(2)
                                      if good[2*x+y]), F(0)) / success
                        expected = sum((weights[2*x+y] for y in range(2)
                                        if good[2*x+y]), F(0)) / mass
                        require(actual == expected, "Projection failure")
                        marginal_checks += 1
                else:
                    zero += 1  # Overrotation can give zero success; do not hide it.
                b = step(b, weights, good)
    return {"prior_laws": len(laws), "nonempty_relations": 255,
            "round_states": rounds, "positive_success_states": positive,
            "zero_success_states": zero, "input_marginal_checks": marginal_checks}


def check_easy_projection_control() -> dict:
    # F_r(x,y) = AND_i (not x OR y_i); all-one output is a valid constant function.
    # Positive-unate preprocessing must solve this without any training samples.
    cases = 0
    for r in range(1, 9):
        counts = [0, 0]
        for x in range(2):
            for y in product(range(2), repeat=r):
                counts[x] += all((not x) or bit for bit in y)
        require(counts == [2**r, 1], "Multiplicity count")
        require(all(all((not x) or bit for bit in (1,) * r) for x in range(2)),
                "Unate constant witness")
        require(F(counts[1], sum(counts)) == F(1, 2**r+1), "Marginal count")
        cases += 1
    # Analytic illustrative size, not an enumerated or empirically sampled instance.
    with localcontext() as ctx:
        ctx.prec = 40
        unseen = (Decimal(2**20) / Decimal(2**20+1)) ** 10000
    return {"enumerated_sizes": cases, "all_resolved_by_constant_output": True,
            "illustrative_r": 20, "independent_training_samples": 10000,
            "input_one_probability": "1/1048577",
            "probability_input_one_unseen": str(unseen),
            "interpretation": "Deliberately easy diagnostic, not a hard workload."}


def main() -> None:
    report = {"status": "pass",
              "scope": "Finite logical and ideal-amplitude identities only; no native solver or speedup.",
              "verification_contract": check_verification_contract(),
              "weighted_conditioning": check_conditioning(),
              "projection_negative_control": check_easy_projection_control()}
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
