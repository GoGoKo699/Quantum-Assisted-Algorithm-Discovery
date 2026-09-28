# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may themselves be useful outputs. Mathematical models and possible
quantum integration come before software, datasets and hardware implementation.
Essential input, accuracy and output costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current conclusion: smooth spectral compression is valid, but not a free speedup

[Smooth response 20](exploration/phase_3/SMOOTH_RESPONSE_COMPRESSION_20.md) avoids
sharp spectral-band classification by applying a bounded polynomial to the full
response generator. The construction preserves spectral probabilities, approximately
retains the relevant frequencies, and pays explicitly for changes to the high-
frequency tail. A simple total-variation bound uses the collective response's
known second moment and the same Lorentzian linewidth and output bins.

No smallest spectral spacing or cutoff-edge gap is required. This is a positive
spectral law, not a postselected filtered state or a smooth function silently
substituted for an orthogonal projector in the preceding Schur argument.

The complete generic cost does not improve the leading direct-sampling query
scaling: the reduction in encoded bandwidth is offset by the cost per transformed
block call. This limitation is already recognized in spectral-amplification
literature. It is not an impossibility theorem for the spin model, structured
encodings or other quantum sampling methods. The result is a completed comparison,
not a reason to build another filter compiler or classical spin-off.

The [current work order](work_orders/CURRENT.md) returns to the physical interaction
structure: how much spatially connected information is needed for the collective
response at the requested linewidth? The next test is a positive finite-window
construction with controlled cross-correlation and boundary errors, then a matched
classical/local-quantum comparison. No such locality guarantee is claimed yet.

## Reproduce the mathematical controls

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/smooth_response_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/smooth_response_v1/REPORT.json)
contains fixed 2/4/6-spin checks of spectral weights, moments and bounded maps,
plus negative and invalid-input controls. The efficient general amplification
polynomial is a cited prior construction, not numerically synthesized here.
The checker ran twice with identical JSON; -O/-OO was rejected. These are
floating-point mathematical diagnostics, not experimental spectra, circuits,
performance tests or interval certificates. No older verifier was rerun.

## Retained alternatives and organization

[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) retains
the direct linewidth-matched quantum sampler and classical limits.
[Spectral boundary 16](exploration/phase_3/SPECTRAL_BOUNDARY_16.md) retains the
classical observable-recursion certificate.
[Exchange memory 17](exploration/phase_3/EXCHANGE_MEMORY_17.md),
[slow-sector sampling 18](exploration/phase_3/SLOW_SECTOR_SAMPLING_18.md), and
[resonance window 19](exploration/phase_3/RESONANCE_WINDOW_19.md) retain their
distinct approximations and access assumptions. Their conclusions are not
silently transferred to the new frequency map.

Classical probability/climate exploration remains open. Missing climate files
block only the empirical test in [Audit 13](exploration/phase_3/CONTINUATION_INFORMATION_13.md).
Manthan remains paused; battery/operator routes remain parked.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
remain independent projects owning their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) are subject to the direct-output and
model-first extensions. `main` is an entry point, not a merged copy of later work.
[STATUS.md](STATUS.md) records current claims and pinned historical ledgers.
Earlier notes, data, code, reports, third-party notices and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only this parent repository may be modified in the project context.
