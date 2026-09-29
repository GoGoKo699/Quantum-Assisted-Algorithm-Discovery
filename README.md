# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

Direct samples may be useful outputs. Mathematical models and quantum integration
come before datasets, software and hardware engineering. Essential input and
accuracy costs remain explicit. See [AGENTS.md](AGENTS.md).

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current comparison: what information does the spectrum actually require?

[Response readout 22](exploration/phase_3/RESPONSE_READOUT_22.md) compares the same
local-block spectral task at the output level. A difference in scalar return
amplitudes certifies a spectral difference. Exact rational controls show that
independent-spin and commuting approximations miss a declared resolved six-spin
response. That small system is classically easy; the result establishes the
importance of interactions there, not quantum advantage or growing-chain hardness.

Conversely, finitely many sufficiently accurate scalar correlations yield a
classical bin sampler with a proved error budget. The Fourier reconstruction is
matched to the existing geometric quantum clock. Any negative approximate bin
weights are repaired with their effect bounded, rather than silently ignored.
Clock truncation, observable-weighted wrapping, correlation errors and arithmetic
are all charged. A small final spectrum does not mean it is cheap to acquire.

Strong classical tensor methods can use half-time evolution to calculate these
correlations. For the real spin generator the required contraction is bilinear,
not the conserved operator norm. The [work order](work_orders/CURRENT.md) now asks
what it costs to acquire the response-relevant scalars as resolution increases.
Large Schmidt rank, full-state complexity or failure of one truncation does not
by itself establish a difficult sampled spectrum. The quantum route need not
construct the scalars classically; it may still return direct spectral samples.

At d=J and linewidth J/4, one explicit conditional target is 255 correlations
within 0.002, sufficient for per-block TV below 0.02834 before arithmetic. No cheap
large-block method has been demonstrated to meet that target. No native tensor
simulation, experimental spectrum or quantum performance result is claimed.

## Local quantum integration remains available

[Positive spatial windows 21](exploration/phase_3/POSITIVE_SPATIAL_WINDOWS_21.md)
retains its positive mixture of finite regions, with a collective spectral error
bound independent of total chain length at fixed local parameters and linewidth.
Both classical and quantum methods may use it. Quantum system-register size is
at most twice the selected block size; linewidth time, coefficient access and
repeated-shot costs remain. The sufficient block size is not a hardness bound.
Its spatial error must be added to the new per-block readout error.

[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) supplies
the direct linewidth-matched quantum sampler and analytic classical limits.
[Spectral boundary 16](exploration/phase_3/SPECTRAL_BOUNDARY_16.md) retains the
recursion certificate. Notes 17-20 preserve their distinct memory, slow-sector,
resonance-window and generic-filter conclusions. The new scalar reconstruction is
a classical competitor, not a renewed classical-program requirement.

## Mathematical checks

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/response_readout_v1/verify.py
```

Python 3.10+ and NumPy. The [report](experiments/response_readout_v1/REPORT.json)
separates exact rational moment/Taylor witnesses from complex128 readout controls.
The final checker ran twice with identical output; -O/-OO was rejected. These are
not hardware, native NMR or tensor benchmarks. General output guarantees follow
from the proof, not finite numerical plots. No older verifier was rerun or old
scientific file changed. No source dataset or upstream implementation was imported.

## Organization and preserved work

The existing parent repository is the appropriate workspace; no new repository
or third classical spin-off is needed. Both
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
remain independent projects owning their further development.

Climate/dynamics remain open; missing files block only the empirical test in
[Audit 13](exploration/phase_3/CONTINUATION_INFORMATION_13.md). Manthan remains
paused and battery/operator routes parked. Scientific phase 3 uses
`research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) are subject to the explicit direct-output
and model-first extensions. `main` is an entry point, not a merged copy of later
work. [STATUS.md](STATUS.md) links claims and pinned historical ledgers.
Phase-2 Note 27 remains closed. Prior evidence, notices and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only Quantum-Assisted-Algorithm-Discovery may be modified in this context.
