# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation obtain useful information more effectively
than strong classical alternatives?** Direct samples and model-first exploration
are allowed; a learned classical program is optional. Essential access, accuracy,
output and validation costs remain explicit. See [AGENTS.md](AGENTS.md).

**No useful quantum advantage is established. Manuscript preparation is on hold.**

## Current checkpoint: activity claim closed, evidence preserved

[Closeout 30](exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md) completes the
repository handoff for the two-window emission-covariance proposal. That proposal
is **not selected for further quantum-advantage development on the present evidence**.
The classical acquisition thought potentially costly was performed at the specified
seven-emitter parameter point, and a small tilted contraction reproduced the chosen
statistic closely. Generic Monte Carlo precision is therefore not an adequate sole
classical baseline for this example.

This is not a proof that all emitter systems are easy, a full-record accuracy
claim, or a measured quantum runtime disadvantage. The quantum flag/instrument
constructions remain conditional references. No replacement application or new
research task is started in this wrap-up, and no new repository is needed.

## Read the completed comparison

| Evidence | Contents |
|---|---|
| [Acquisition 29](exploration/phase_3/CLASSICAL_ACTIVITY_ACQUISITION_29.md) | Model acquired from the supplied generator; windows 1, 4, 16; [code](experiments/activity_acquisition_v1/verify.py) and [report](experiments/activity_acquisition_v1/REPORT.json) |
| [Cross-check 29B](exploration/phase_3/CLASSICAL_ACTIVITY_CROSSCHECK_29B.md) | Separate calculation at windows 1, 5, 20; extra tilted-mode refinement; [code](experiments/activity_acquisition_crosscheck_v1/verify.py) and [report](experiments/activity_acquisition_crosscheck_v1/REPORT.json) |
| [Closeout decision](exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md) | What is established, what is not, and the conditions for reopening |
| [Import/replay manifest](provenance/activity_closeout_30.json) | Hashes of the previously local 29B payload and the maintenance replay |

Both evidence sets concern one periodic seven-emitter calibration, with ground
initialization and no supplied phase rates or fitted photon data. Their observation
windows are different and must not be relabeled. Results are finite floating-point
diagnostics, not interval proofs, all-size tractability or experimental validation.
The closeout retains the original numerical files rather than rewriting history.

## Reproduce cross-check 29B

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/activity_acquisition_crosscheck_v1/verify.py
```

Python 3.10+, NumPy and SciPy. The unchanged checker was replayed once during
closeout and reproduced its archived report byte-for-byte; its invalid-input
controls passed and -O/-OO invocations refused execution. Other historical
scientific verifiers were not rerun. This maintenance replay is not new research,
a quantum circuit, a larger-system study or a performance comparison.

## Continuation and preserved work

The [current work order](work_orders/CURRENT.md) records the closed checkpoint;
it no longer requests the completed acquisition. A subsequent continuation starts
from [Revision 27](exploration/phase_3/STRATEGIC_REVISION_27.md), not by automatically
increasing emitter count, tightening accuracy or extending the last certificate.
The parent exploration remains open. Supporting results are not a substitute for
a useful quantum contribution.

[Claim 28](exploration/phase_3/EMISSION_ACTIVITY_CLAIM_28.md),
[record instrument 25](exploration/phase_3/RECORD_INSTRUMENT_25.md),
[emission memory 26](exploration/phase_3/EMISSION_MEMORY_26.md), and earlier spectral
and dynamical studies keep their original scopes. Climate/dynamics remain open
alternatives, Manthan paused, and battery/operator routes parked. The two
independent classical spin-offs own their further development. No third spin-off
is created, and Phase-2 Note 27 remains closed.

The active research branch is `research/prx-quantum-phase2`. `main` is a public
entry point, not a merged copy of the research. [STATUS.md](STATUS.md) links current
claims and pinned history; the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
records branch roles and the direct-output/model-first scope. Earlier proofs,
code, reports, data, third-party rights and the original [MIT license](LICENSE),
Copyright (c) 2026 Ruge Lin, are preserved. Only this parent repository is writable.
