# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation obtain useful information more effectively
than strong classical alternatives?** Direct samples and model-first analysis
remain authorized. Essential access, accuracy and output costs stay explicit.
See [AGENTS.md](AGENTS.md). Manuscript preparation remains on hold.

**No useful quantum advantage is established. No new repository is needed.**

## Current decision: the source-matched activity test favors a classical contraction

[Classical activity acquisition 29](exploration/phase_3/CLASSICAL_ACTIVITY_ACQUISITION_29.md)
executes the comparison requested by [Claim 28](exploration/phase_3/EMISSION_ACTIVITY_CLAIM_28.md).
For its seven-emitter periodic Ising calibration, a two-mode tilted model was
acquired from the generator, not supplied or fitted to target trajectories.
The ground-start covariance is reproduced with observed errors 3.32e-5, 3.18e-6
and 3.75e-7 for the three declared observation windows. These are finite numerical
diagnostics, not interval certificates or a theorem for growing rings.

Exact translation/reflection reduction first lowers the relevant operator sector
from 16,384 coordinates to 1,300. One sparse factorization and right/left slow-mode
solves acquire the reusable small model. Full invariant-sector exponential action
provides a separate reference. Acquisition and validation are both recorded; no
unknown phase rates, stationary-state preparation, burn-in or photon dataset is
provided free. The small model retains the ground state's slow projection; omitted
fast-transient effects are part of its tested error, not assumed absent.

The reduced matrices compute the requested scalar, not an automatically positive
full photon-record law. Individual moment errors are larger than covariance errors
in this example. Other windows, parameters or larger systems require new validation.
The exact spatial symmetry itself does not establish polynomial scaling in n.

This calibration does not justify quantum resource compilation for the proposed
activity-precision advantage. Amplitude estimation improves generic Monte Carlo,
not deterministic evaluation of an adequate small model. Its quantum construction
remains valid and the broader emitter family is not declared easy. The
[work order](work_orders/CURRENT.md) returns to a bounded positive-mechanism screen,
not another generic estimator or automatic increase in emitter count.

## Executed acquisition and validation

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/activity_acquisition_v1/verify.py
```

Python 3.10+, NumPy and SciPy. The [report](experiments/activity_acquisition_v1/REPORT.json)
records the acquired matrices, three covariance comparisons, symmetry intertwining,
independent propagation, solver-shift and initial-state controls. The final script
ran twice with identical JSON, rejecting -O/-OO and five invalid inputs.
No quantum circuit, laboratory data, large-system study or timing comparison was
performed. No earlier scientific verifier was rerun or historical file changed.

## Preserved work

[Revision 27](exploration/phase_3/STRATEGIC_REVISION_27.md) governs priorities.
[Record instrument 25](exploration/phase_3/RECORD_INSTRUMENT_25.md),
[emission memory 26](exploration/phase_3/EMISSION_MEMORY_26.md), and Claim 28 keep
their original mathematical scopes. Earlier spectral and dynamical results remain
quantitative references, not rejected by this finite calibration. Direct samples
need not become a classical program. No third classical spin-off is being created.

The existing independent projects own their further development. The active parent
branch is `research/prx-quantum-phase2`; `main` remains an entry point, not a merged
copy of later work. [STATUS.md](STATUS.md) links current claims and pinned history.
The [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and charter remain subject to the direct-output and model-first extensions.
Climate/dynamics remain open, Manthan paused, battery/operator routes parked,
and Phase-2 Note 27 closed. Earlier proofs, code, reports, data, the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, and third-party rights remain.
Only Quantum-Assisted-Algorithm-Discovery may be modified in this context.
