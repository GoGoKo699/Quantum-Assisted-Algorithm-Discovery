#!/usr/bin/env python3
"""Replay published scalar data; NOT chemistry, dynamics, or a quantum benchmark.

Sources (tables visually checked, 2026-09-28):
  Kundu et al., arXiv:2509.14067v1, Table I (PDF page 2).
  Vo et al., arXiv:2603.22139v1, Table II (PDF page 4).
Only selected rounded numerical entries are transcribed. No upstream code/data import.
Python 3.10+, standard library only, no file writes.
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


def corrected_rate(tst: F, kappa: F) -> F:
    if tst < 0 or not 0 <= kappa <= 1:
        raise ValueError("Require nonnegative TST rate and kappa in [0,1].")
    return tst * kappa


def barrier_budget(temperature: float, rate_factor: float) -> float:
    """kcal/mol; exponential sensitivity only, holding the prefactor fixed."""
    if not math.isfinite(temperature) or temperature <= 0:
        raise ValueError("Temperature must be finite and positive.")
    if not math.isfinite(rate_factor) or rate_factor <= 1:
        raise ValueError("Rate factor must be finite and greater than one.")
    # Exact SI k_B and N_A; thermochemical kcal = 4184 J.
    gas_constant = F("1.380649e-23") * F("6.02214076e23") / 4184
    return float(gas_constant) * temperature * math.log(rate_factor)


def main() -> None:
    # These rates concern the molecular LiEC control, NOT the metal surface.
    inputs = {"PBE-D3": (F("2.1e10"), F("0.49")),
              "wB97X-D3": (F("8.3e1"), F("0.94")),
              "DLPNO-CCSD(T)": (F("1.6e2"), F("0.96"))}
    rates = {name: corrected_rate(*values) for name, values in inputs.items()}
    expected = {"PBE-D3": F("10290000000"), "wB97X-D3": F("78.02"),
                "DLPNO-CCSD(T)": F("153.6")}
    require(rates == expected, "Rate arithmetic mismatch")
    weak_ratio = rates["PBE-D3"] / rates["DLPNO-CCSD(T)"]
    hybrid_ratio = rates["DLPNO-CCSD(T)"] / rates["wB97X-D3"]
    require(weak_ratio == F("66992187.5"), "Weak-baseline ratio")
    require(hybrid_ratio == F(7680, 3901), "Hybrid-baseline ratio")
    # Separate STATIC surface barriers, not free energies or rate predictions.
    barriers = {"PBE": F("5.6"), "wB97X-V": F("17.9"),
                "CCSD": F("16.0"), "DLPNO-CCSD(T)": F("15.5"),
                "AFQMC": F("17.4"), "reported_mean": F("16.3")}
    differences = {name: value - barriers["reported_mean"]
                   for name, value in barriers.items() if name != "reported_mean"}
    require(differences["PBE"] == F("-10.7"), "PBE difference")
    require(differences["wB97X-V"] == F("1.6"), "Hybrid difference")
    # The published +/-0.8 is cross-method spread, NOT a certified true-error bound.
    factor2 = barrier_budget(300.0, 2.0)
    factor10 = barrier_budget(300.0, 10.0)
    require(0.4132 < factor2 < 0.4133 and 1.372 < factor10 < 1.373,
            "Energy-to-rate sensitivity")
    require(math.isclose(barrier_budget(600.0, 2.0), 2 * factor2), "T scaling")
    # Proposed neutral Li40 + C3H4O3 calibration, with explicit 1s frozen cores.
    atoms = {"Li": (40, 3, 2), "C": (3, 6, 2), "H": (4, 1, 0), "O": (3, 8, 2)}
    electrons = sum(n * z for n, z, _ in atoms.values())
    correlated = sum(n * (z - core) for n, z, core in atoms.values())
    require(electrons == 166 and correlated == 74, "Electron accounting")
    invalid = [lambda: corrected_rate(F(-1), F(1)),
               lambda: corrected_rate(F(1), F(2)),
               lambda: barrier_budget(0, 2), lambda: barrier_budget(300, 1),
               lambda: barrier_budget(float("nan"), 2),
               lambda: barrier_budget(300, float("inf"))]
    for case in invalid:
        try:
            case()
        except ValueError:
            continue
        raise AssertionError("Invalid-input control was not rejected")
    print(json.dumps({"status": "pass", "scope": "published-data arithmetic only",
                      "molecular_rates_per_second": {k: float(v) for k, v in rates.items()},
                      "molecular_PBE_over_CC_rate_ratio": float(weak_ratio),
                      "molecular_CC_over_hybrid_rate_ratio": float(hybrid_ratio),
                      "surface_barrier_minus_reported_mean_kcal_mol": {k: float(v) for k, v in differences.items()},
                      "fixed_prefactor_300K_factor2_budget_kcal_mol": factor2,
                      "fixed_prefactor_300K_factor10_budget_kcal_mol": factor10,
                      "proposed_Li40_EC_total_electrons": electrons,
                      "proposed_Li40_EC_correlated_electrons": correlated,
                      "invalid_inputs_rejected": len(invalid),
                      "warning": "No calculated ratio is a computational speedup; no electronic or MD calculation was run."},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
