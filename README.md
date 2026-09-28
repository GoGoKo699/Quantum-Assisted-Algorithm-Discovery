# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may themselves be useful outputs. Models and possible quantum
integration come before software, datasets and hardware implementation. Essential
input, accuracy and output costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current result: retain near resonances, eliminate only the faster sector

[Resonance window 19](exploration/phase_3/RESONANCE_WINDOW_19.md) extends the
slow-response analysis to an entire band of low operator frequencies. A Hermitian
static Schur generator retains their finite-frequency and first-order couplings.
A continuous-total-variation bound controls the resulting Lorentzian-broadened
spectral law, including its tails. It does not require a minimum nonzero frequency,
a separation between neighboring frequencies at the cutoff, or the earlier parity-
cancellation condition. A response-weighted refinement follows the retained
observable's coupling to eliminated modes rather than counting those modes.

This is a model-reduction result, NOT a gap-independent quantum algorithm.
The inverse on the discarded sector is conditioned by the chosen cutoff, but a
sharp projector onto the retained band can itself be expensive to implement.
The note separates internal spacings, discarded inverse conditioning, and cutoff-
edge resolution. Standard QSVT and downfolding are prior methods, and the generic
construction need not beat the direct linewidth-matched sampler. The same reduced
model is a classical comparator whose preparation can be reused across samples.

The [current work order](work_orders/CURRENT.md) asks whether a justified smooth or
response-weighted construction can avoid artificial cutoff resolution while
preserving positive spectral probabilities. Its complete symbolic cost must be
compared with direct quantum sampling and adequate classical methods. No molecule,
new dataset, native solver, large sweep or additional spin-off is the next step.

## Reproduce the bounded mathematical check

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/resonance_window_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/resonance_window_v1/REPORT.json)
records three fixed small spin chains and three block controls, Schur/resolvent
identities, moment and response-weighted bounds, and negative controls. The final
checker ran twice with identical output; -O/-OO was rejected. These are floating-
point diagnostics, not interval certificates, experimental spectra, quantum
hardware, scaling measurements or timing comparisons. Continuous claims follow
from the written proof. No older scientific verifier was rerun or file changed.
No upstream code or experimental data was imported.

## Retained quantum and classical alternatives

[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) retains
the direct linewidth-matched quantum sampler and exact classical limits.
[Spectral boundary 16](exploration/phase_3/SPECTRAL_BOUNDARY_16.md) retains the
classical Lanczos certificate. [Exchange memory 17](exploration/phase_3/EXCHANGE_MEMORY_17.md)
and [slow-sector sampling 18](exploration/phase_3/SLOW_SECTOR_SAMPLING_18.md) retain
the projected-memory and isolated-zero-sector constructions with their assumptions.
Their bounds are not silently transferred to the enlarged resonance window.
Classical recursion, effective models, tensor networks and direct inference remain
legitimate competitors. Direct samples do not have to become a classical program.

Classical probability/climate exploration remains open. Its missing packet gates
only the empirical test in [Audit 13](exploration/phase_3/CONTINUATION_INFORMATION_13.md).
Manthan remains paused, battery/operator routes remain parked, and
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
remain independent projects owning their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) are subject to the explicit direct-output
and model-first extensions. `main` remains an entry point, not a merged copy of
later work. [STATUS.md](STATUS.md) records claims and pinned historical ledgers.
Phase-2 Note 27 remains closed. Prior research, notices and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only this parent repository may be modified in the project context.
