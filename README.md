# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may be useful outputs. Mathematical models and quantum integration
precede datasets, software and hardware engineering. Essential input, accuracy,
output and validation costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current decision: establish the useful quantum opportunity before extending the machinery

[Strategic revision 27](exploration/phase_3/STRATEGIC_REVISION_27.md) reassesses the
accumulated work. We have explicit quantum sampling constructions, controlled
classical reductions, and tests of output accuracy. We have not yet identified a
consequential regime where quantum computation improves the complete cost.
Another available error bound is therefore not the default next task.

The monitored-emitter model remains a candidate for ONE bounded regime-selection
study. The [work order](work_orders/CURRENT.md) requires a physically motivated
counting observable, the strongest matched classical description including its
acquisition cost, and a specific quantum operation that could improve the result.
A conditional hypothesis can justify exploration; a universal classical lower
bound, hardware demonstration or new dataset is not required. A large quantum
state or failure of one weak approximation is not sufficient either.

The classical baseline is stronger than an averaged-state comparison. Existing
metastability theory explicitly treats coarse continuous-measurement records and
within-phase fluctuations. Its assumptions must be matched to the finite-time,
ground-start task; it is not automatically valid for every microscopic record.
Neither cheap sampling from supplied phase rates nor expensive full-state
propagation establishes the cost of acquiring the adequate classical model.

The next deliverable is one claim sheet and its decisive test, not another generic
trajectory, filtering or reconstruction framework. The full record-plus-final-
state bounds remain useful certificates, not a requirement that every scientific
consumer needs that much output. Any narrower useful task must be declared.
No new repository or third classical spin-off is needed.

## Retained emitter results

[Record instrument 25](exploration/phase_3/RECORD_INSTRUMENT_25.md) specifies direct
quantum sampling through local coherent evolution and monitored decay. It retains
the conditional state between outputs and bounds whole-record discretization error.
It is an explicit use of established simulation methods, not an advantage claim.

[Emission memory 26](exploration/phase_3/EMISSION_MEMORY_26.md) gives a coherent
classical few-excitation approximation with a record-level error bound. The cutoff
limits simultaneous excitations, not cumulative photons. At fixed collective
drive n Omega^2/kappa^2 it supplies a controlled polynomial-in-n regime; that is
not fixed-local-drive thermodynamic tractability. The q=1 uniform-chain model has
an exact three-amplitude renewal description. Its failure in one non-dilute small
control is not all-classical hardness.

The historical checker remains available:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/emission_memory_v1/verify.py
```

Python 3.10+, NumPy and SciPy. Its [report](experiments/emission_memory_v1/REPORT.json)
records the earlier finite controls. It was NOT rerun for this documentation-only
revision. No new simulation, timing result, experimental validation or independent
full-proof audit is claimed. The supplied latest archive and note were checked
for integrity; that is not scientific revalidation.

## Preserved mechanisms and organization

The [sampling decision 24](exploration/phase_3/SAMPLING_REGIME_DECISION_24.md)
retains the spectral cost comparison and the explicitly distinct attached local
cache analysis. Earlier spectral algorithms, response/locality proofs and classical
comparisons remain quantitative references. Climate/dynamics remain open; missing
files block only their empirical test. Manthan is paused; battery/operator routes
remain parked; Phase-2 Note 27 stays closed. Old next steps are dated records,
not parallel active tasks.

[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects owning their further development. Scientific phase 3
uses `research/prx-quantum-phase2`; `main` is an entry point, not a merged copy of
later work. The [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and charter are subject to the explicit direct-output/model-first extensions.
[STATUS.md](STATUS.md) links current claims and pinned prior ledgers. The original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, and all earlier research,
source data and third-party rights are preserved. Only this parent is writable.
