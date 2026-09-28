# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may themselves be useful outputs. Models and possible quantum
integration come before software, datasets and hardware implementation. Essential
input, accuracy and output costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current model-level step: distinguish response time from memory time

[Exchange memory 17](exploration/phase_3/EXCHANGE_MEMORY_17.md) studies the
alternating-offset interacting-spin family from Notes 15-16. The measured collective
mode couples to a known staggered mode. An exact projected-memory representation
expresses the full spectral response through one memory resolvent. This uses
established projection/continued-fraction methods, not a newly invented framework.

The projected generator equals the ordinary doubled spin generator plus two
reflections about easily specified sublattice observable states. That provides
an explicit quantum integration without a supplied projected-eigenbasis oracle.
Preparation, controlled evolution, inverses, coefficient access, precision and
shots still count. A memory-frequency sample is not automatically a physical
response sample; the transformation between the two is stated explicitly.

A conditional finite-window certificate bounds when the memory can be replaced
by a single broadened line. A justified short memory could reduce the maximum
simulation time needed for that approximation. Short memory has NOT been proved
for the growing chain, and reduced circuit depth is not a total-cost advantage.
Finite closed systems recur; fast initial curvature is insufficient evidence.

An exact resolved two-spin limit catches a misleading shortcut: a small memory
contribution can have a large effect when the required linewidth resolves it.
A corrected, equally simple classical two-line model nevertheless succeeds in
that limit. The example is a mathematical control, not a hard workload or an
application claim. The [current work order](work_orders/CURRENT.md) asks whether
low-frequency memory in the many-spin family admits an effective slow-mode
reduction, with all small-gap and resolution assumptions retained.

## Other side of the comparison

[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) supplies
the direct linewidth-matched quantum sampler and exact classical limits.
[Spectral boundary 16](exploration/phase_3/SPECTRAL_BOUNDARY_16.md) supplies a
classical Lanczos-truncation certificate and local-Pauli construction cost.
Neither a failed sufficient bound nor a large operator space proves classical
hardness. Recursion, effective models, tensor networks and direct inference remain
legitimate competitors. Classical preprocessing may be reused across many draws.
The quantum method is not required to learn a classical program first.

## Executed mathematical checks

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/exchange_memory_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/exchange_memory_v1/REPORT.json)
contains small projection/reflection, memory-resolvent, finite-window and dimer
controls. It is not a measured spectrum, large-chain scaling result, compiled
circuit or performance benchmark. The checker passed twice with identical output;
-O/-OO was rejected. Continuous guarantees follow from the written proofs, not
finite numerical bins. No older verifier was rerun; its files remain unchanged.
No experimental data or upstream implementation was imported.

## Open mechanisms and preserved evidence

The [direct-sampling scope](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
and [spectral screen](exploration/phase_3/OPEN_SAMPLING_SCREEN_14.md) retain the
application context. Classical probability evolution remains open. The
[climate contract](exploration/phase_3/HEATWAVE_SAMPLING_CONTRACT_11.md),
[segment construction](exploration/phase_3/SEGMENT_SELECTION_12.md), and
[continuation audit](exploration/phase_3/CONTINUATION_INFORMATION_13.md) remain
available; missing data gate only their specific empirical test.

Manthan [profiling/encoding](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md)
remain paused; [battery](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md)
and [operator](exploration/phase_3/MECHANISM_SCREEN_01.md) candidates remain parked.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) are subject to the direct-output and
model-first extensions. `main` is an entry point, not a merged copy of later work.
[STATUS.md](STATUS.md) links current claims and pinned historical records.
Phase-2 [Note 27](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) stays closed.
The original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, prior research
and third-party rights remain intact. Only this parent repository is writable.
