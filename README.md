# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may be useful outputs. Mathematical models and quantum integration
come before data, software and hardware engineering. Essential input, accuracy,
output and validation costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current decision: fair reuse, then examine physical measurement records

[Sampling regime 24](exploration/phase_3/SAMPLING_REGIME_DECISION_24.md) completes
the present spectral cost comparison without declaring an advantage or a general
impossibility. Typicality, half-time tensors, recursion, effective reductions and
small-block diagonalization remain legitimate classical alternatives. The available
bounds do not yet identify a response-required regime where quantum sampling wins.
The one-dimensional spectral construction is retained as a quantitative reference;
further generic spectral certificates are not the default task.

The comparison also permits a quantum producer to learn a reusable classical
output table. Direct quantum sampling does not forbid caching. However, resampling
such a table does not create fresh statistical information. The note states a
standard table-learning budget and an exact event-frequency variance calculation.
The same distinction between per-draw approximation and joint statistical quality
applies to classical and quantum-produced tables.

The new bounded model check concerns time-resolved emission records from a driven,
dissipative interacting-spin system. The useful output is a physical measurement
history, potentially supporting waiting-time and bright/dark-interval statistics,
not an arbitrary internal simulation trajectory. This model and quantum-jump
methods have primary-literature precedents; neither is a new architecture here.

The [work order](work_orders/CURRENT.md) requires a record-level discretization
bound and a strong classical comparison. An instrument includes both the recorded
outcome and the conditional remaining state. Approximating only the averaged
master equation does not ensure the correct detector record. A two-emitter
control demonstrates this distinction but is not a hard or useful new instance.
No full driven-system trajectory algorithm or quantum advantage was demonstrated.

## Evidence in this checkpoint

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/sampling_regime_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/sampling_regime_v1/REPORT.json)
contains analytical resolution/probe budgets, an exact rational cache-variance
control, and a finite Kraus-instrument identity check. The 20/26/32-spin rows are
not executed simulations. The final checker ran twice identically and rejected
-O/-OO and six invalid inputs. No many-body propagation, tensor benchmark,
experimental record, quantum circuit or performance measurement occurred.
No previous scientific verifier was rerun; its evidence remains at its own checkpoint.

## Retained mechanisms and organization

[Trace acquisition 23](exploration/phase_3/TRACE_ACQUISITION_23.md),
[response readout 22](exploration/phase_3/RESPONSE_READOUT_22.md),
[spatial windows 21](exploration/phase_3/POSITIVE_SPATIAL_WINDOWS_21.md) and
[model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) retain the
spectral algorithms, proofs, classical comparisons and executed controls.
Their conclusions are not refuted by the new direction. Classical probability/
climate exploration remains open; missing files block only its empirical test.
Manthan remains paused and battery/operator routes parked. Phase-2 Note 27 stays closed.

Both [Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
remain independent projects. No new repository or third classical spin-off is needed.
Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) are subject to the direct-output and
model-first extensions. `main` remains an entry point, not a merged copy of later
work. [STATUS.md](STATUS.md) links current claims and pinned prior ledgers.
Prior research, third-party rights and the original [MIT license](LICENSE),
Copyright (c) 2026 Ruge Lin, are preserved. Only this parent repository is writable.
