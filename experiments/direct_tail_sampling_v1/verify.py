#!/usr/bin/env python3
"""Check the tail-sampling accounting, not a climate or quantum simulation.

Python 3.10+, standard library only. No inputs, network calls, or file writes.
All laws in the checks are explicitly artificial arithmetic controls. The
cost table is an optimistic known-probability sensitivity, not a forecast.
"""
from fractions import Fraction as F
import json
import math
import sys

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def normalized(xs: list[F]) -> list[F]:
    if not xs or any(x < 0 for x in xs) or sum(xs) <= 0:
        raise ValueError("Need a nonnegative vector with positive mass.")
    return [x / sum(xs) for x in xs]


def condition(p: list[F], event: list[bool]) -> list[F]:
    if len(p) != len(event):
        raise ValueError("Law and event lengths differ.")
    return normalized([x if hit else F(0) for x, hit in zip(p, event)])


def tv(p: list[F], q: list[F]) -> F:
    if len(p) != len(q) or sum(p) != 1 or sum(q) != 1:
        raise ValueError("Need probability laws on the same finite space.")
    return sum(abs(x - y) for x, y in zip(p, q)) / 2


def amplifier_cost(p: float) -> dict:
    """First-peak known-p Grover schedule; A and A^-1 counted equally.

    Excludes marking/reflections/validation, assumes deterministic replay costs
    one classical trajectory, and charges a new preparation for every attempt.
    This is not an optimal schedule or an unknown-p algorithm.
    """
    if not math.isfinite(p) or not 0 < p <= 0.5:
        raise ValueError("Require finite 0 < p <= 1/2.")
    theta = math.asin(math.sqrt(p))
    j = max(0, int(math.floor(math.pi / (4 * theta))))
    success = math.sin((2 * j + 1) * theta) ** 2
    calls = (2 * j + 1) / success
    # Illustrative: one coherent A/A^-1 call costs one classical path, then replay.
    unit_cost = calls + 1
    return {
        "p_assumed": p, "rounds": j, "success_per_attempt": success,
        "A_or_inverse_calls_per_accepted_sample": calls,
        "equal_call_cost_plus_replay": unit_cost,
        "speed_ratio_vs_rejection_at_equal_call_cost": 1 / (p * unit_cost),
        "max_coherent_call_cost_over_classical_path": {
            str(g): max(0.0, (1 / (p * g) - 1) / calls) for g in (1, 10, 100)
        },
    }


def main() -> None:
    scores = [0, 1, 2, 3]
    priors = [normalized([F(4), F(2), F(1), F(1)]),
              normalized([F(1), F(1), F(2), F(4)])]
    cases = 0
    for p in priors:
        for base in (2, 3):
            weights = [F(base) ** a for a in scores]
            z = sum(x * w for x, w in zip(p, weights))
            tilted = [x * w / z for x, w in zip(p, weights)]
            for cutoff in (1, 2, 3):
                event = [a >= cutoff for a in scores]
                event_mass = sum(x for x, hit in zip(p, event) if hit)
                accept = [F(base) ** (cutoff - a) if hit else F(0)
                          for a, hit in zip(scores, event)]
                require(all(0 <= x <= 1 for x in accept), "Acceptance out of range")
                raw = [x * a for x, a in zip(tilted, accept)]
                require(normalized(raw) == condition(p, event), "Wrong corrected law")
                alpha = sum(raw)
                require(alpha == F(base) ** cutoff * event_mass / z, "Wrong success mass")
                first_filter = z / F(base) ** max(scores)
                require(first_filter * alpha == event_mass * F(base) ** (cutoff - max(scores)),
                        "Nested preparation accounting failed")
                require(first_filter * alpha <= event_mass, "Artificial nested gain")
                cases += 1
    # Deliberately wrong shortcut: tilt and condition, omitting reweighting.
    p = priors[0]
    tilted = normalized([x * F(2) ** a for x, a in zip(p, scores)])
    event = [False, False, True, True]
    naive_error = tv(condition(p, event), condition(tilted, event))
    require(naive_error == F(1, 6), "Negative control changed")
    # Worst-case conditioning amplification; both input laws have the same event mass.
    a = [F(999, 1000), F(1, 2000), F(1, 2000)]
    b = [F(999, 1000), F(51, 100000), F(49, 100000)]
    e = [False, True, True]
    require(tv(a, b) == F(1, 100000), "Raw TV control")
    require(tv(condition(a, e), condition(b, e)) == F(1, 100), "Conditional TV control")
    # Rarity of a detailed label is not invariant under appending unused random bits.
    p2 = [F(3, 4), F(1, 4)]
    expanded = [x / 16 for x in p2 for _ in range(16)]
    require(all(x < F(1, 10) for x in expanded), "Refined-label rarity control")
    require(sum(expanded[16:]) == p2[1], "Appending labels changed event mass")
    rows = [amplifier_cost(p) for p in (0.01, 0.001, 0.0001)]
    require(rows[0]["speed_ratio_vs_rejection_at_equal_call_cost"] < 7, "Cost control")
    require(rows[1]["speed_ratio_vs_rejection_at_equal_call_cost"] < 21, "Cost control")
    rejected = 0
    for p_bad in (0.0, -0.1, 1.0, float("nan"), float("inf")):
        try:
            amplifier_cost(p_bad)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError("Invalid probability accepted")
    print(json.dumps({
        "status": "pass",
        "scope": "Artificial finite-law controls and analytic cost sensitivities only; no climate data or simulator run.",
        "tilt_correction_and_nested_cost_cases": cases,
        "naive_tilt_conditional_TV_negative_control": str(naive_error),
        "conditioning_error_control": {"raw_TV": str(tv(a, b)), "event_mass": "1/1000", "conditional_TV": "1/100"},
        "invalid_probabilities_rejected": rejected,
        "cost_table_assumptions": "Known p, first-peak schedule; no reflection/marking/validation/tuning overhead; rho=1 for displayed speed; g=1,10,100 are hypothetical quality-matched classical gains, NOT measured gains.",
        "cost_sensitivity": rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
