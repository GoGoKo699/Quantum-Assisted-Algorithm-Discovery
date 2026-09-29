# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may be useful outputs. Mathematical models and quantum integration
come before datasets, software and hardware engineering. Essential input, accuracy,
output and validation costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current model: direct sampling of physical emission histories

[Record instrument 25](exploration/phase_3/RECORD_INSTRUMENT_25.md) develops the
monitored-emitter direction from the live [sampling decision 24](exploration/phase_3/SAMPLING_REGIME_DECISION_24.md).
The desired output is a finite-time photon-count record from a specified driven,
dissipative spin model, not an arbitrary internal simulation trajectory. The
Markov reservoir, finite interaction graph, initial state and detector bins are
explicit assumptions. This is not a validated hardware or experimental claim.

The construction interleaves transverse/ZZ rotations and monitored local decay,
retaining the conditional quantum state between emitted outputs. Lifting the
dynamics to counters before approximation gives a whole-record error bound;
matching only an averaged master equation would be insufficient. Detector bin
width and the smaller numerical time step are distinct. Multiple emissions and
saturated count labels are handled without dropping paths or postselection.

For ideal primitives the full record-plus-state half-diamond error is at most
C T h/4, with C an explicit sum of local drive/interaction/decay products.
The method uses n system qubits and one recycled ancilla, with all finite-step,
precision, initialization and repeated-record costs stated. This specializes
established quantum-jump, collision-model and product-formula techniques; no new
generic simulator or useful quantum-classical separation is claimed.

A rational two-emitter calculation certifies a dark-then-bright event discrepancy
above 0.1217 from a population-rate extrapolation in a coherent regime. That small
system is classically easy. Classical conditional pure-state trajectories, tensor,
cluster, renewal and direct observable calculations remain serious competitors.
The [work order](work_orders/CURRENT.md) now asks which conditional many-body
memory actually matters to the requested temporal records and whether it can be
compressed adequately. No new simulation framework or repository is required.

## Executed check

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/record_instrument_v1/verify.py
```

Python 3.10+, NumPy and SciPy. The [report](experiments/record_instrument_v1/REPORT.json)
contains a two-emitter count-resolved matrix calculation, four discretization
controls and a separately exact-rational event witness. The final source ran twice
with identical output; -O/-OO and six invalid inputs were rejected. This is not
hardware, a many-body hardness test, a native trajectory package or a timing study.
No earlier verifier was rerun or historical scientific file changed.

## Retained alternatives and organization

The spectral algorithms in [Note 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md),
[spatial windows 21](exploration/phase_3/POSITIVE_SPATIAL_WINDOWS_21.md),
[response readout 22](exploration/phase_3/RESPONSE_READOUT_22.md) and
[trace acquisition 23](exploration/phase_3/TRACE_ACQUISITION_23.md) remain quantitative
references, not refuted results. The attached local spectral-cache checkpoint is
distinguished from the live Note 24. Climate/dynamics remain open; missing files
block only their empirical check. Manthan is paused; battery/operator routes parked.

Both [Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
remain independent. No third spin-off is being created. Scientific phase 3 uses
`research/prx-quantum-phase2`; `main` is an entry point, not a merged copy of later
research. The [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and charter are subject to the explicit direct-output and model-first extensions.
[STATUS.md](STATUS.md) links current claims and pinned prior ledgers. Phase-2 Note 27
stays closed. The original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin,
and all prior research/third-party rights are preserved. Only this parent is writable.
