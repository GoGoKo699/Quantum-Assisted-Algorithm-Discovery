# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation obtain useful information more effectively
than strong classical alternatives?** Direct samples are allowed. Mathematical
models and their quantum integration precede implementation; essential access,
accuracy and output costs remain explicit. See [AGENTS.md](AGENTS.md).

**Exploratory: no useful quantum advantage is established. Manuscript on hold.**

## Current conditional claim: estimate temporal emission activity

[Activity claim 28](exploration/phase_3/EMISSION_ACTIVITY_CLAIM_28.md) specializes
the emitter question to a bounded correlation of counts in two successive windows.
The task no longer asks for a complete microscopic history. Two computational
flags exactly encode the needed three Laplace moments as final-state probabilities,
without changing the underlying system dynamics or discarding rare paths.

Standard high-accuracy Lindblad simulation plus amplitude estimation provides
a concrete quantum precision mechanism: inverse-linear rather than generic
inverse-square sampling dependence on additive error. The operation requires a
coherent circuit and its inverse, with purification/workspace retained; it does
not act retrospectively on measured photon data. Two statistic flags are not a
claim of only two extra qubits for the whole simulation. Ordinary first-order
splitting is not silently treated as an exact, cheap channel.

**The comparison remains conditional.** A known adequate small classical tilted
generator evaluates the same statistic cheaply without sampling. Its acquisition,
within-phase corrections and ground-start transient must be counted. Long bins
can favor that classical reduction. The [work order](work_orders/CURRENT.md) now
targets this one classical acquisition question, not another generic proof or a
claim of advantage from the size of the many-body state. The standard primitives
and counting-field machinery are attributed; novelty is not established.

## Reproduce the identity check

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/activity_flags_v1/verify.py
```

Python 3.10+, NumPy and SciPy. The [report](experiments/activity_flags_v1/REPORT.json)
records a single three-emitter flag/tilted-law check and small classical controls.
The checker ran twice identically and rejected -O/-OO. No published metastable
parameter-slice simulation, quantum circuit, large-system run or timing comparison
was performed. This is not evidence of a practical quantum advantage. Historical
scientific verifiers were not rerun and their files remain unchanged.

## Retained work and organization

[Revision 27](exploration/phase_3/STRATEGIC_REVISION_27.md) governs the research
priority. [Record instrument 25](exploration/phase_3/RECORD_INSTRUMENT_25.md) and
[emission memory 26](exploration/phase_3/EMISSION_MEMORY_26.md) preserve the full-record
quantum construction and coherent low-excitation classical comparison. Earlier
spectral and dynamical work remains available, not refuted by the narrower task.
No new repository or third classical spin-off is needed.

The independent [Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
projects own their further development. The active branch is
`research/prx-quantum-phase2`; `main` is an entry point, not a merged research copy.
[STATUS.md](STATUS.md) links current claims and pinned prior ledgers. The
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and charter are subject to the explicit direct-output/model-first extensions.
Climate/dynamics remain open, Manthan paused, battery/operator routes parked,
and Phase-2 Note 27 closed. Prior proofs, data, code and third-party rights remain
intact. The original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, is unchanged.
Only this parent repository is writable in this project context.
