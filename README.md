# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may be useful outputs. Mathematical models and quantum integration
precede datasets, software and hardware engineering. Essential input, accuracy,
output and validation costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current result: quantify the conditional memory left between photons

[Emission memory 26](exploration/phase_3/EMISSION_MEMORY_26.md) studies the same
monitored interacting-emitter model. A coherent classical approximation keeps at
most q simultaneous excitations, not at most q photons over the observation.
A factorial-moment envelope and a count-lifted residual bound control the entire
site/time-binned record and final state. The approximation retains coherences,
interactions within the retained sector and repeated emissions.

For fixed collective drive parameter lambda=n Omega^2/kappa^2, dimensionless
horizon and accuracy, a finite q gives a polynomial classical sampler in n.
This is not a fixed-local-drive thermodynamic claim: lambda grows with n when
Omega/kappa is fixed. A failed sufficient bound is not evidence of hardness.
The proof specializes existing residual/trajectory methods; no generic novelty
or practical advantage is claimed.

At q=1 each photon truly resets the whole approximate system. The uniform open
chain then has an exact three-amplitude renewal description including waiting
times and detector labels. It is not a global-blockade assumption about the full
model. At comparable drive and decay, a four-site check shows that this simple
renewal law and a two-excitation law differ from the requested record. That system
is classically easy; neither discrepancy establishes many-body difficulty.

The [current work order](work_orders/CURRENT.md) now tests a stronger classical
possibility: phase-level or hidden-state dynamics for non-dilute emission records.
Existing Ising-model metastability work already describes classical switching in
some regimes. Its averaged-state reduction is not automatically an accurate
site-resolved detector instrument. The comparison must identify useful record
information and price acquisition of the adequate model, not just count amplitudes.
No new repository, spin-off or simulation framework is needed.

## Quantum integration and verification

[Record instrument 25](exploration/phase_3/RECORD_INSTRUMENT_25.md) retains the direct
quantum construction: local coherent evolution and monitored decay, preserving the
conditional quantum state between outputs. Its whole-record discretization,
precision and repeated-history costs still count. The classical reduction is a
competitor, not a requirement to convert quantum samples into a classical program.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/emission_memory_v1/verify.py
```

Python 3.10+, NumPy and SciPy. The [report](experiments/emission_memory_v1/REPORT.json)
contains one four-site model at two drives, excitation-cutoff comparisons and
reduced-space renewal controls. The final checker ran twice with identical JSON;
-O/-OO and six invalid inputs were rejected. These are floating-point diagnostics,
not interval certificates, measured photon histories, quantum circuits or timings.
The all-size statements follow from the written proof. No old verifier was rerun.

## Preserved mechanisms and organization

The [live sampling decision 24](exploration/phase_3/SAMPLING_REGIME_DECISION_24.md)
sets the record direction and retains the distinct attached spectral-cache note.
Earlier spectral algorithms, response/locality proofs and classical comparisons
remain quantitative references, not refuted results. Climate/dynamics remain open;
missing files block only their empirical test. Manthan is paused, battery/operator
routes parked, and Phase-2 Note 27 remains closed.

[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects owning their further development. Scientific phase 3
uses `research/prx-quantum-phase2`; `main` is an entry point, not a merged copy of
later work. The [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and charter are subject to the explicit direct-output/model-first extensions.
[STATUS.md](STATUS.md) links current claims and pinned prior ledgers. The original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, and prior evidence and
third-party rights are preserved. Only this parent repository is writable.
