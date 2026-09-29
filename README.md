# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may be useful outputs. Mathematical models and quantum integration
come before datasets, software and hardware engineering. Essential input, output
and accuracy costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current comparison: classical random-state acquisition versus direct quantum samples

[Trace acquisition 23](exploration/phase_3/TRACE_ACQUISITION_23.md) prices an
established classical competitor for the same high-temperature collective spin
spectrum. Random-phase trace estimation gives correlation mean-square error at
most 2/(R 2^k). The existing Fourier readout converts this to a high-probability
bin-sampling guarantee without assuming independent errors at different times.
These are specialized error and cost bounds for prior methods, not a new
quantum advantage or a new general theory of typicality.

The classical producer evolves two ordinary 2^k-entry vectors per probe, not a
4^k-entry operator. It requires no assumed tensor-rank bound or complete eigenbasis.
Each vector still has exponential size and must be propagated to the full required
time; fewer statistical probes do not make this work free. The note keeps random
state generation, propagation precision, normalization, bin readout and reuse
across requested samples in the budget. Cheap random product states cannot simply
be assigned the global-phase variance guarantee.

One ten-spin mathematical control actually acquires the correlations and checks
the resulting finite-clock probabilities against an independent spectral reference.
Its observed bin error is about 0.007. This is not a large-system success guarantee,
application performance result, or a quantum/classical benchmark. The larger-block
probe-count examples in the note are analytical budgets, not executed simulations.

The [current work order](work_orders/CURRENT.md) now asks whether a credible quantum
regime survives this stronger comparator, the half-time tensor route, recursion,
and valid translation reductions at the same resolution and number of draws.
The quantum algorithm need not calculate or output the classical correlation table;
its direct samples remain allowed. A comparison of two upper bounds is not a
proof of advantage. No further generic readout framework or new repository is needed.

## Quantum integration and prior mathematical results

[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) retains
the direct linewidth-matched quantum sampler and analytic classical limits.
[Spatial windows 21](exploration/phase_3/POSITIVE_SPATIAL_WINDOWS_21.md) retains
the positive mixture of finite regions and its collective spectral error bound.
[Response readout 22](exploration/phase_3/RESPONSE_READOUT_22.md) retains exact
output witnesses, scalar reconstruction and half-time tensor identities. The
new full-time pure-state method is a distinct classical tradeoff, not a silent
replacement of those results. Notes 16-20 retain their recursion, memory,
slow-sector, resonance-window and smooth-transformation assumptions and limits.

## Reproduce the executed control

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/trace_acquisition_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/trace_acquisition_v1/REPORT.json)
separates the ten-spin matrix-free calculation, phase-ensemble identity tests and
analytical probe budgets. The final checker ran twice identically; -O/-OO was
rejected. Floating checks are not interval certificates; general guarantees follow
from the proofs. No older verifier was rerun or historical research file changed.
No experimental data or upstream implementation was imported.

## Organization and preserved work

The existing parent repository remains the appropriate workspace. The independent
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
projects own their further development. No third classical spin-off is created.

Climate/dynamics remain open; missing files block only their empirical test in
[Audit 13](exploration/phase_3/CONTINUATION_INFORMATION_13.md). Manthan remains
paused; battery/operator routes remain parked. Scientific phase 3 uses
`research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) are subject to direct-output and
model-first extensions. `main` is an entry point, not a merged copy of later work.
[STATUS.md](STATUS.md) links current claims and pinned historical ledgers.
Phase-2 Note 27 remains closed. All prior evidence, third-party rights and the
original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only Quantum-Assisted-Algorithm-Discovery may be modified in this context.
