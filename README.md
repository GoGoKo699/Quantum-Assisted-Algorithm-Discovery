# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The output should run on ordinary
computers and address a need that exists independently of this project.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current application test: battery-interface reaction simulation

The [application case](exploration/phase_3/APPLICATION_CASE_02.md) screens accelerator
kernels, weather-model radiation, and reactive molecular simulators. One bounded
feasibility lead is selected: a classical energy/force evaluator for initial
electrolyte decomposition at lithium-metal interfaces, potentially trained on
selected quantum-computed electronic reference values. Later trajectories would
run entirely classically.

The useful workflow is documented, but the quantum advantage is not. This is
learning a reusable classical simulator, not a new symbolic algorithm or a
one-off chemical energy prediction. Quantum-generated training references for
classical potentials are already prior work.

Crucially, a March 2026 paper already supplies strong classical correlated
calculations for this chemistry. The comparison cannot be made only against an
inaccurate inexpensive functional. The [work order](work_orders/CURRENT.md) requires
one matched-input cost-and-accuracy assessment before model training, a large
chemistry campaign, or more general theory.

```sh
python experiments/application_case_v1/verify.py
```

Python 3.10+, standard library only. This replays selected published numbers and
simple sensitivity/electron-accounting calculations. It is not a chemistry,
quantum-circuit, or performance benchmark. No published coordinates or model
weights have been downloaded, and no useful new simulator has been constructed.

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
Copyright (c) 2026 Ruge Lin, are unchanged. Only the new application arithmetic
check was run for this checkpoint; root and historical suites were not rerun.
Only the parent repository may be modified in this project context.
