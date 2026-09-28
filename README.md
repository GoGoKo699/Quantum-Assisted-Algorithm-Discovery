# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may themselves be useful outputs. Models and possible quantum
integration come before software, datasets and hardware implementation. Essential
input, accuracy and output costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current mathematical result: sample the slow response without assuming short memory

[Slow-sector sampling 18](exploration/phase_3/SLOW_SECTOR_SAMPLING_18.md) identifies
the second-order response of the alternating-offset spin family. Under an explicit
first-order cancellation and a nonzero-frequency gap condition, a reduced generator
retains the resolved spectral structure. An invariant-graph argument bounds the
continuous total-variation error, including changes in the measured observable's
state and weights. This does not assume fast memory decay or replace the spectrum
by one line.

The generator is a product of the conserved-sector projector, perturbation and
signed inverse of the exchange generator. Standard quantum singular value
transformation can construct those operations from explicit block encodings,
without enumerating a classical eigenbasis. Spectral measurement and rescaling
then give direct samples of the effective response. At linewidth proportional
to d^2/J, the stated query budget has no inverse power of d, but retains important
size and inverse-gap factors. This compares with a straightforward direct quantum
construction, not the best classical algorithm. It is not a compiled circuit,
practical speedup, generic fast forwarding or a priority claim.

A matching classical second-order representation is also explicit. Its coefficients
must be acquired, but that work can be amortized across many samples. The solved
maximum-spin sector illustrates the reduction and contributes a shrinking fraction
of the full high-temperature response; it cannot stand in for that response.
Reflection symmetry alone does not prove the required cancellation in the presence
of opposite-parity degeneracy. No all-size nondegeneracy theorem is established.

The [current work order](work_orders/CURRENT.md) asks whether a justified treatment
of response-relevant near resonances can avoid a global minimum-gap penalty.
An analytic upper bound already shows that the global gap cannot be assumed
size-independent. Neither its smallness nor a failed approximation proves
classical hardness. No data download, molecule selection or large simulation
is the next step.

## Retained quantum and classical alternatives

[Exchange memory 17](exploration/phase_3/EXCHANGE_MEMORY_17.md) gives an exact
rank-two quantum implementation of projected memory, its conditional one-line
certificate and a resolved two-spin warning. The new slow-sector route does not
require a memory-decay hypothesis or convert a memory sample into a response
sample through an unproved map.

[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) retains
the direct linewidth-matched quantum sampler and exact classical limits.
[Spectral boundary 16](exploration/phase_3/SPECTRAL_BOUNDARY_16.md) retains the
classical Lanczos-truncation certificate. Recursion, effective models, tensor
networks and direct inference remain legitimate competitors. The quantum method
is not required to learn a classical program first.

## Executed mathematical checks

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/slow_sector_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/slow_sector_v1/REPORT.json) contains
fixed 2/4/6/8-spin symmetry and effective-generator controls, finite-bin comparisons,
small invariant-graph controls and path-Laplacian identities. It is not a measured
spectrum, arbitrary-size theorem, interval certificate, QSVT circuit or timing
benchmark. The final checker ran twice with identical output; -O/-OO was rejected.
Continuous guarantees follow from the written proofs. No older verifier was rerun
and no upstream implementation, experimental spectrum or climate data was imported.

## Open mechanisms and preserved evidence

The [direct-sampling scope](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
and [spectral screen](exploration/phase_3/OPEN_SAMPLING_SCREEN_14.md) retain the
application context. Classical probability evolution remains open. The
[climate contract](exploration/phase_3/HEATWAVE_SAMPLING_CONTRACT_11.md),
[segment construction](exploration/phase_3/SEGMENT_SELECTION_12.md), and
[continuation audit](exploration/phase_3/CONTINUATION_INFORMATION_13.md) remain
available; missing data gate only their empirical test.

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
