# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may themselves be useful outputs; they need not be converted into
a classical program. Models and possible quantum integration are examined before
software, datasets and hardware implementation. Essential access and accuracy
costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current model-level result: sample the spectrum at the required linewidth

[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) compares
classical probability evolution with direct interacting-spin spectral sampling.
The latter supplies the next bounded mathematical task; the dynamics route remains
open. The model is an established high-temperature nuclear-spin response with
explicit offsets, isotropic couplings and a specified Lorentzian linewidth.

A geometric quantum clock, controlled energy-gap evolution and a dithered Fourier
measurement give a linewidth-matched sampling law. The note bounds finite-clock,
frequency-wrap and digital-offset errors. Controlled evolution time scales as
O(log(1/epsilon)/gamma), where gamma is linewidth and epsilon is distributional
accuracy, not inverse microscopic level spacing. This is a symbolic construction,
not a gate/runtime estimate, optimality statement or new quantum-advantage claim.
Direct spectral sampling and windowed phase estimation have established precedents.

The same note supplies classical comparisons at that linewidth: an exact sampler
for the commuting model, a symmetry-protected single line, a coarse-line error
bound, and a coupling-cut certificate for reducing the problem to small components.
Failing these sufficient reductions does not establish classical hardness. The
interesting parameter is the observable complexity that survives the requested
resolution, not spin count alone.

The [current work order](work_orders/CURRENT.md) asks for an observable-specific
classical truncation/error analysis on one justified coupling family, compared
with the explicit quantum sampler. No molecule selection, data transfer, package
installation, large simulation or full circuit compilation is the next step.

## Executed mathematical checks

```sh
python experiments/spectral_structure_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/spectral_structure_v1/REPORT.json)
records fixed small-matrix, observable-preparation, spectral-moment, classical-law,
Fourier-kernel and negative controls. It is not a measured NMR spectrum, native
application benchmark or quantum hardware test. The final checker passed twice
with identical output; -O/-OO was rejected. Earlier scientific verifiers were
not rerun, and their sources and reports are unchanged. No upstream code or data
was imported. The research note distinguishes analytic proofs from finite checks.

## Other mechanisms and preserved evidence

The [direct-sampling scope](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
and [earlier spectral screen](exploration/phase_3/OPEN_SAMPLING_SCREEN_14.md)
remain the application and algorithmic context. The
[climate contract](exploration/phase_3/HEATWAVE_SAMPLING_CONTRACT_11.md),
[segment construction](exploration/phase_3/SEGMENT_SELECTION_12.md), and
[continuation-information audit](exploration/phase_3/CONTINUATION_INFORMATION_13.md)
remain available. Their pending data-specific test does not block model analysis.
No climate data were acquired or analyzed in this checkpoint.

Manthan [profiling and encoding](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md)
remain paused. The [battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md)
and [operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
Both [Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) retain their historical objectives;
Note 10 explicitly permits direct samples and the current work order sets the
model-first sequence. `main` is an entry point, not a merged copy of later work.
[STATUS.md](STATUS.md) states current claims and links pinned historical records.
Phase-2 [Note 27](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) stays closed.
Old research, notices and the original [MIT license](LICENSE), Copyright (c) 2026
Ruge Lin, are preserved. Only the parent repository may be modified here.
