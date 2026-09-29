# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may be useful outputs. Mathematical models and quantum integration
come before datasets, software and hardware engineering. Essential input and
accuracy costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current result: sample finite regions with a collective spectral guarantee

[Positive spatial windows 21](exploration/phase_3/POSITIVE_SPATIAL_WINDOWS_21.md)
constructs a positive mixture of finite-chain responses at the same requested
Lorentzian linewidth. Randomly shifted cuts give overlapping spatial windows;
each window retains its full collective observable, original offsets and physical
ends. The approximation error is bounded in total variation independently of
total chain length, using finite-range locality and collective residual identities.

This is not an average of isolated spin spectra with cross correlations silently
removed. The proof controls the change caused by the cut bonds over all frequencies.
No spectral gap, sharp cutoff, unknown eigenbasis or short-memory assumption is used.
The sufficient region size depends on coupling, linewidth and accuracy and may be
large; it is not a necessary correlation length or a practical hardware estimate.
Locality and spectral-sampling ingredients are prior work, not new primitives.

Both sides benefit. A quantum sampler can select a block classically and operate
on its doubled register, rather than the full chain, while retaining the linewidth
time and all access/precision costs. A classical method can construct the same
block spectra and reuse them. At fixed parameters and resolution this gives a
classical alternative polynomial in total chain length; increasing total spin count
alone is not evidence of advantage. Tensor and restricted-state methods may improve
substantially over dense block diagonalization.

The [work order](work_orders/CURRENT.md) now asks what response-relevant information
is actually required INSIDE a finite region, in a nontrivial alternating-offset
regime, and compares classical acquisition/reuse with local quantum evolution.
No new molecule, large simulation, generic filter or third spin-off is the next step.

## Mathematical checks

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/spatial_windows_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/spatial_windows_v1/REPORT.json)
contains finite 2/4/5/6-spin identities for positive mixtures, collective residuals,
resolvents, moments and negative controls. The final checker ran twice identically;
-O/-OO was rejected. These are floating-point diagnostics, not interval proofs,
experimental spectra, quantum circuits or performance benchmarks. The all-size
continuous-law bound follows from the written argument and a cited locality theorem.
No previous verifier was rerun or historical scientific file changed.

## Retained comparisons and organization

[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) retains
the linewidth-matched quantum clock and classical limits.
[Spectral boundary 16](exploration/phase_3/SPECTRAL_BOUNDARY_16.md) retains the
classical recursion certificate. Notes
[17](exploration/phase_3/EXCHANGE_MEMORY_17.md),
[18](exploration/phase_3/SLOW_SECTOR_SAMPLING_18.md),
[19](exploration/phase_3/RESONANCE_WINDOW_19.md) and
[20](exploration/phase_3/SMOOTH_RESPONSE_COMPRESSION_20.md) retain their distinct
memory, slow-sector, resonance-window and generic-filter conclusions.

Classical probability/climate exploration remains open. Missing climate files
block only the empirical test in [Audit 13](exploration/phase_3/CONTINUATION_INFORMATION_13.md).
Manthan is paused; battery/operator routes are parked. The independent
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
projects own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) are subject to the explicit direct-output
and model-first extensions. `main` is an entry point, not a merged copy of later
work. [STATUS.md](STATUS.md) links current claims and pinned historical ledgers.
Prior evidence, rights notices and the original [MIT license](LICENSE), Copyright
(c) 2026 Ruge Lin, are preserved. Only this parent repository may be modified.
