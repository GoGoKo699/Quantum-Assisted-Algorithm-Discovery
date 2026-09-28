#!/usr/bin/env python3
"""Exact finite-law controls for joint parent/continuation selection.

Independent standard-library diagnostic; not a climate model, circuit compiler,
particle-filter benchmark, or implementation of an upstream method. No file writes.
Run with Python 3.10+ without -O/-OO. See SEGMENT_SELECTION_12.md for scope.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import asin, comb, floor, pi, sin, sqrt
import json
import sys

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def normalize(values: tuple[F, ...]) -> tuple[F, ...]:
    if not values or any(v < 0 for v in values) or sum(values) <= 0:
        raise ValueError("A law needs nonnegative weights and positive total mass.")
    total = sum(values)
    return tuple(v / total for v in values)


def joint(mu: tuple[F, ...], kernels: tuple[tuple[F, ...], ...],
          scores: tuple[tuple[F, ...], ...]) -> tuple[F, tuple[F, ...]]:
    if sum(mu) != 1 or any(v < 0 for v in mu):
        raise ValueError("Invalid parent law.")
    if len(mu) != len(kernels) or len(mu) != len(scores):
        raise ValueError("Parent/kernel/score dimensions differ.")
    raw = []
    for w, row, score in zip(mu, kernels, scores):
        if not row or len(row) != len(score) or sum(row) != 1 or any(v < 0 for v in row):
            raise ValueError("Invalid continuation law or dimensions.")
        if any(g < 0 or g > 1 for g in score):
            raise ValueError("Scores must be in [0,1].")
        raw.extend(w * p * g for p, g in zip(row, score))
    alpha = sum(raw)
    return alpha, normalize(tuple(raw))


def tv(p: tuple[F, ...], q: tuple[F, ...]) -> F:
    require(len(p) == len(q), "TV dimensions")
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def amplified_conditioned(mu, kernels, scores, counts) -> None:
    # Exact dyadic score flag: an independent uniform two-bit register u<4*g.
    p0, marked, output = [], [], []
    for i in range(2):
        for r in range(2):
            threshold = 4 * scores[i][r]
            require(threshold.denominator == 1, "Non-dyadic test score")
            for u in range(4):
                p0.append(mu[i] * kernels[i][r] / 4)
                marked.append(u < threshold)
                output.append(2 * i + r)
    # amplitude[z]=sqrt(p0[z])*coefficient[z]; rational recurrence avoids roots.
    coefficient = [F(1)] * len(p0)
    alpha = sum(p for p, flag in zip(p0, marked) if flag)
    if not alpha:
        counts["empty_selection_laws"] += 1
        return
    _, target = joint(mu, kernels, scores)
    counts["nonempty_selection_laws"] += 1
    for _ in range(4):
        require(sum(p * c * c for p, c in zip(p0, coefficient)) == 1, "Norm")
        success = sum(p * c * c for p, c, flag in zip(p0, coefficient, marked) if flag)
        counts["round_states"] += 1
        if success:
            obtained = [F(0)] * 4
            for p, c, flag, key in zip(p0, coefficient, marked, output):
                if flag:
                    obtained[key] += p * c * c / success
            require(tuple(obtained) == target, "Joint conditional distribution")
            counts["successful_conditional_laws"] += 1
        else:
            counts["zero_success_round_states"] += 1
        reflected = [-c if flag else c for c, flag in zip(coefficient, marked)]
        mean = sum(p * c for p, c in zip(p0, reflected))
        coefficient = [2 * mean - c for c in reflected]


def path_control() -> dict:
    mu = (F(1, 3), F(2, 3))
    k1 = ((F(1, 4), F(3, 4)), (F(1, 2), F(1, 2)))
    g1 = ((F(1, 4), F(1)), (F(1, 2), F(3, 4)))
    k2 = ((F(1, 4), F(3, 4)), (F(3, 4), F(1, 4)),
          (F(1, 2), F(1, 2)), (F(1, 4), F(3, 4)))
    g2 = ((F(1), F(1, 4)), (F(1, 2), F(3, 4)),
          (F(1, 4), F(1)), (F(3, 4), F(1, 2)))
    c1, eta1 = joint(mu, k1, g1)
    c2, eta2 = joint(eta1, k2, g2)
    base, weight, event = [], [], []
    for h, r, s in product(range(2), repeat=3):
        j = 2 * h + r
        base.append(mu[h] * k1[h][r] * k2[j][s])
        weight.append(g1[h][r] * g2[j][s])
        event.append(r + s >= 1)
    direct = normalize(tuple(p * g for p, g in zip(base, weight)))
    require(eta2 == direct, "Sequential potential recursion")
    desired = normalize(tuple(p if e else F(0) for p, e in zip(base, event)))
    corrected = normalize(tuple(p / g if e else F(0) for p, g, e in zip(eta2, weight, event)))
    naive = normalize(tuple(p if e else F(0) for p, e in zip(eta2, event)))
    require(corrected == desired, "Terminal inverse-guide correction")
    require(tv(naive, desired) > 0, "Missing-correction negative control")
    event_mass = sum(p for p, e in zip(base, event) if e)
    require(c1 * c2 * sum(p / g for p, g, e in zip(eta2, weight, event) if e) == event_mass,
            "Probability needs the normalizers")
    return {"paths": 8, "event_mass": str(event_mass),
            "uncorrected_tail_TV": str(tv(naive, desired)), "corrected_tail_TV": "0"}


def independent_pilot_control() -> dict:
    """Enumerate a two-stage, one-particle algorithm, including pilot randomness."""
    mu = (F(1, 3), F(2, 3))
    k1 = ((F(1, 4), F(3, 4)), (F(1, 2), F(1, 2)))
    g1 = ((F(1, 4), F(1)), (F(1, 2), F(3, 4)))
    k2 = ((F(1, 4), F(3, 4)), (F(3, 4), F(1, 4)),
          (F(1, 2), F(1, 2)), (F(1, 4), F(3, 4)))
    g2 = ((F(1), F(1, 4)), (F(1, 2), F(3, 4)),
          (F(1, 4), F(1)), (F(3, 4), F(1, 2)))
    desired = {(h, r, s): mu[h] * k1[h][r] * k2[2*h+r][s]
               for h, r, s in product(range(2), repeat=3)}
    recovered = {path: F(0) for path in desired}
    tilted_wrong = {path: F(0) for path in desired}
    histories = 0
    for h, pilot1, r, pilot2, s in product(range(2), repeat=5):
        a1 = sum(p*g for p, g in zip(k1[h], g1[h]))
        j = 2*h+r
        a2 = sum(p*g for p, g in zip(k2[j], g2[j]))
        # Two independent ordinary pilot scores, one per stage; accepted children
        # have the exact quantum/rejection conditional law. This is enumeration,
        # not an implementation of either accepted-child generator.
        prob = (mu[h] * k1[h][pilot1] * k1[h][r] * g1[h][r] / a1
                * k2[j][pilot2] * k2[j][s] * g2[j][s] / a2)
        zhat = g1[h][pilot1] * g2[j][pilot2]
        inverse_path_guide = 1 / (g1[h][r] * g2[j][s])
        recovered[h, r, s] += prob * zhat * inverse_path_guide
        tilted_wrong[h, r, s] += prob * inverse_path_guide
        histories += 1
    require(recovered == desired, "Independent pilots must recover every base path mass")
    require(normalize(tuple(tilted_wrong.values())) != tuple(desired.values()),
            "Omitting random normalizers must fail this finite-pool control")
    return {"extended_random_histories": histories, "base_path_mass_checks": len(desired),
            "recovered_total_mass": str(sum(recovered.values())),
            "normalizer_omission_detected": True,
            "scope": "Unnormalized expectations only; a finite self-normalized ratio is not unbiased."}


def main() -> None:
    counts = {"nonempty_selection_laws": 0, "empty_selection_laws": 0,
              "round_states": 0, "successful_conditional_laws": 0, "zero_success_round_states": 0}
    priors = ((F(1, 2), F(1, 2)), (F(1, 3), F(2, 3)))
    rows = ((F(1), F(0)), (F(1, 4), F(3, 4)), (F(1, 2), F(1, 2)))
    for mu, k0, k1 in product(priors, rows, rows):
        for flat in product((F(0), F(1, 4), F(1)), repeat=4):
            amplified_conditioned(mu, (k0, k1), (flat[:2], flat[2:]), counts)
    require(counts["zero_success_round_states"] > 0, "Overshoot not exercised")
    # For these two histories, event probabilities are 1/4 and 3/4.
    mu = (F(1, 2), F(1, 2))
    kernels = ((F(3, 4), F(1, 4)), (F(1, 4), F(3, 4)))
    scores = ((F(0), F(1)), (F(0), F(1)))
    alpha, law = joint(mu, kernels, scores)
    naive = (F(0), F(1, 2), F(0), F(1, 2))
    require(law == (F(0), F(1, 4), F(0), F(3, 4)), "Ancestor weighting")
    require(tv(law, naive) == F(1, 4), "Parent-first bias")
    # A finite random pool is not the exact base law, even with perfect local draws.
    pools = {}
    for n in (1, 2, 4, 8):
        expectation = sum(F(comb(n, k), 2**n) * F(3 * k, n + 2 * k) for k in range(n + 1))
        pools[str(n)] = str(expectation)
        require(expectation < F(3, 4), "Finite-pool bias control")
    require(pools["1"] == "1/2" and pools["2"] == "5/8", "Finite-pool exact controls")
    # Purely rescaling a guide changes rejection difficulty but not its target law.
    scaled_scores = tuple(tuple(g / 100 for g in row) for row in scores)
    a_scaled, law_scaled = joint(mu, kernels, scaled_scores)
    require(law_scaled == law and a_scaled == alpha / 100, "Envelope scaling")
    # Deterministic continuations can all be cached once by a classical competitor.
    a_det, det_law = joint((F(1, 4), F(3, 4)), ((F(1),), (F(1),)),
                          ((F(1, 4),), (F(1),)))
    require(det_law == normalize((F(1, 16), F(3, 4))), "Cached deterministic law")
    # Amplified success frequencies are not original normalizers.
    require(F(1, 4) * (3 - 4 * F(1, 4))**2 == 1, "One-round normalization trap")
    cost = []
    for a in (F(1, 4), F(1, 16), F(1, 100)):
        theta = asin(sqrt(float(a)))
        rounds = floor(pi / (4 * theta))
        success = sin((2 * rounds + 1) * theta)**2
        calls = (2 * rounds + 1) / success
        cost.append({"assumed_local_acceptance": str(a), "rounds": rounds,
                     "forward_or_inverse_calls_per_child": calls,
                     "unit_coherent_cost_plus_one_replay": calls + 1,
                     "rho_ceiling_against_same_law_rejection": (1 / float(a) - 1) / calls})
    bad = [lambda: joint((F(1),), ((F(1),),), ((F(2),),)),
           lambda: joint((F(1),), ((F(1),),), ((F(0),),)),
           lambda: joint((F(1, 2),), ((F(1),),), ((F(1),),)),
           lambda: joint((F(1),), ((F(-1), F(2)),), ((F(1), F(1)),)),
           lambda: joint((F(1),), ((F(1),),), ((F(1), F(1)),))]
    for case in bad:
        try:
            case()
        except ValueError:
            continue
        raise AssertionError("Invalid-input control was accepted")
    print(json.dumps({"status": "pass", "scope": "Artificial finite laws only; no climate or gate simulation.",
                      "joint_selection": counts, "parent_first_TV": "1/4",
                      "finite_pool_expected_high_parent_mass": pools,
                      "true_high_parent_mass": "3/4", "two_segment_path_control": path_control(),
                      "independent_pilot_control": independent_pilot_control(),
                      "guide_rescaling_target_unchanged": True, "deterministic_cache_law_checked": True,
                      "normalizer_trap": {"original_mass": "1/4", "one_round_success": "1"},
                      "cost_sensitivity": cost,
                      "cost_assumptions": "Known local mass; first-peak schedule; replay costs one ordinary segment; no setup, lookup, mark, precision or validation overhead. Not a climate timing estimate.",
                      "hard_score_pilot_examples": [{"local_acceptance": str(a), "target_conditional_relative_sd": "1/10",
                          "minimum_independent_pilots": int((1-a) / (a * F(1, 100)))}
                          for a in (F(1,4), F(1,16), F(1,100))],
                      "invalid_inputs_rejected": len(bad)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
