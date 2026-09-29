# Claim ledger

## Current checkpoint: positive spatial-window response, 29 September 2026

[Note 21](exploration/phase_3/POSITIVE_SPATIAL_WINDOWS_21.md) gives a positive
finite-window sampler for the high-temperature collective raising response of
a bounded nearest-neighbor spin chain at the original Lorentzian linewidth.
Shifted block partitions retain short end blocks and original local frequency
carriers. For each partition the disconnected spectrum is exactly the mixture
of complete block spectra with weights |block|/n. Averaging partitions produces
overlapping windows, not negative inclusion-exclusion weights or postselection.

Let a=2+log(C)/mu+2/(exp(mu)-1)^2 and b=v/mu for a uniform LR envelope.
With X_ell=9 sum J_i^2(a+b/(2 gamma))/(n ell gamma^2), the full continuous-law
TV error is at most min(1,X_ell,sqrt(X_ell/2)), also after common binning. The
proof uses HS-orthogonality of distinct cut residuals, a vanishing first
resolvent term, and a single-site locality bound with a separate collective
norm argument. It does not assume that all physical cross correlations vanish.
No spectral gap, sharp projector, parity-purity or memory-decay promise is used.

A sufficient size O(epsilon_loc^-1[(J_*/gamma)^2+(J_*/gamma)^3]) is independent
of n but may be large. It is not a necessary size or an empirical correlation
length. Uniform offsets have an exact one-line response and need no such bound.
The theorem is for a normalized infinite-temperature trace and common linewidth,
not arbitrary finite-temperature, pulse, long-range or dissipative models.
Locality, resolvent and spectral-sampling methods are prior ingredients; priority
for this particular collective positive-mixture specialization is unassessed.

## The computational implication is shared, not a separation

The classically selected block requires at most 2ell quantum system qubits plus
ancillas, with the existing linewidth-time evolution and preparation/access costs.
The same mixture is available classically through block diagonalization or stronger
methods. Explicit preprocessing is polynomial in total n at fixed linewidth,
local parameters and accuracy, with exponential dependence on the sufficient
block size in the simple dense upper bound. It can be reused across samples.
Uniform alternating chains require only O(ell) distinct block templates.

Neither that dense upper bound nor the sufficient block size is a lower bound on
classical computation. No useful quantum-classical separation, NMR prediction
improvement, compiled circuit or runtime advantage has been established. The
[work order](work_orders/CURRENT.md) directs the next comparison to necessary
response complexity inside finite regions, not another generic transformation
or an increase in total chain length. Direct samples and model-first scope remain.

## Executed scope

The final NumPy checker ran twice with identical JSON under one BLAS thread.
-O/-OO and six invalid inputs were rejected. Four fixed chains (2,4,6 and a
nonuniform 5-site control with a negative coupling) check 33 partitions, 99 block-
mixture bin identities, 90 cut-residual orthogonality identities, 66 vanishing
first-order and 66 second-resolvent identities, 99 residual envelopes and 42 binned
bounds. Fourth moments, uniform-field exact limits and two invalid simplifications
are checked. Some sufficient bounds saturate at one. The
[report](experiments/spatial_windows_v1/REPORT.json) records all values and counts.

These are complex128 mathematical diagnostics at tolerance 4e-9, not interval
certificates, experimental spectra, a native NMR run, a compiled quantum circuit,
or performance data. Continuous and all-size claims follow from the proof, not
finite cases or quadrature. No prior suite was rerun; no upstream implementation
or experimental dataset was imported. A primary LR theorem page was visually
checked; a separate overview screenshot failed and supplied no figure data.
The source search was bounded, not an exhaustive priority audit.

## Preserved evidence

The preceding ledger and its links are pinned at the
[pre-window checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/dfecc43cccda4843a209a9a55f5dc8547850c0ad/STATUS.md).
Notes 15-20, all earlier proofs, code, reports, datasets and rights remain unchanged.
Older current/next headings are dated checkpoints, not concurrent work orders.
Climate/dynamics remain open; Manthan is paused; battery/operator routes parked;
both spin-offs independent and Phase-2 Note 27 closed. Manuscript preparation
remains on hold. Only this parent repository is modified; no outside contact,
paid/unattended work, release, merge or new repository is part of this checkpoint.
