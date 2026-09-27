# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The output should run on ordinary
computers and address a need that exists independently of this project.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current application test: battery-interface reaction simulation

The [application case](exploration/phase_3/APPLICATION_CASE_02.md) selects one bounded
feasibility lead: a classical energy/force evaluator for initial electrolyte
chemistry at lithium-metal interfaces, potentially trained on selected quantum
computed electronic references. Later simulations would run classically.
The generic architecture is prior work; neither a new simulator nor an advantage
has been established.

The [latest reference audit](exploration/phase_3/REFERENCE_ACCESS_AUDIT_03.md) found
the authors' August 2026 public geometry/data deposit and corrected the proposed
matched-core model. The published AFQMC/ORCA convention retains lithium 1s
correlation: the neutral Li40+EC calibration has 154 correlated electrons, not
the 74 in the earlier hypothetical lithium-core-frozen model. Electron count,
basis size and quantum resources are distinct quantities.

A public archive listing is available, but the ZIP has not transferred into the
execution environment. No coordinates or Hamiltonian have been processed here.
The [work order](work_orders/CURRENT.md) requires pinning the released inputs and
comparing the same electronic problem before assigning costs. Modern classical
chemistry and energy-only model training must both be permitted; the comparison
cannot rely only on an inaccurate inexpensive functional or on free force labels.

This checkpoint is a source/protocol audit and integer dimension accounting, not
a chemistry, quantum-circuit or performance benchmark. No new verifier was added.
For the earlier published-number arithmetic only:

```sh
python experiments/application_case_v1/verify.py
```

That historical script retains its explicitly hypothetical Li-core convention;
its electron count is not the matched published model. Its sources and outputs
are unchanged and it was not rerun for the latest audit.

## Parked and independent work

The [first phase-3 operator construction](exploration/phase_3/MECHANISM_SCREEN_01.md)
remains parked. Its conditional argument and finite algebra verifier are preserved;
its existence does not establish usefulness or give it priority over applications.

[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects. Their further development belongs there, not as the
default continuation here. Neither replaces the parent's goal.

## Organization and evidence

Scientific phase 3 uses the existing branch `research/prx-quantum-phase2`.
The [canonical project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [parent charter](exploration/phase_2/CHARTER.md) govern the exploration.
The default branch is an entry point, not a merged copy of later research.

[STATUS.md](STATUS.md) distinguishes the current checkpoint from historical claims.
The [source-aware descent comparison](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md)
remains closed; retained reconstruction proofs do not reopen it. Earlier proofs,
experiment sources/results, manifests, notices, and the original [MIT license](LICENSE),
Copyright (c) 2026 Ruge Lin, are unchanged. Root and historical suites were not
rerun for the latest audit. Only the parent repository may be modified here.
