# Claim ledger

## Current checkpoint: response-level acquisition and readout, 29 September 2026

[Response readout 22](exploration/phase_3/RESPONSE_READOUT_22.md) continues the
same local alternating-offset spin model at d/J of order one. A characteristic-
function witness lower-bounds spectral TV by exp(-gamma|t|)|Delta C(t)|/2.
The finite-bin version includes discretization and overflow terms; arbitrary
coarse binning need not retain a continuous-law discrepancy.

For one six-spin d=J control at t=2/J and gamma=J/4, exact rational moments and
Taylor enclosures reject on-site-only and commuting SzSz responses at 5% TV
for explicitly declared fine bins. Certified conservative bin-TV lower bounds
are 0.137241910729 and 0.058101380567, respectively. The model is classically easy;
this is evidence that these two approximations change the resolved output, not
an application benchmark, all-classical obstruction or scaling theorem.

The finite geometric-clock law can be reconstructed from N-1 scalar correlations.
For errors e_h and clock autocorrelation weights a_h, integrating the estimated
Fourier polynomial and positive-part-normalizing its bin masses incurs TV at most
sqrt(2 sum a_h^2 e_h^2). Clock truncation, moment-controlled frequency wrapping,
input uncertainty and numerical output arithmetic add to that bound. This is an
explicit positive classical sampler with a conditional accuracy guarantee, not
an assumption that the correlations can be computed cheaply or that positivity
repair validates an incorrect signal. Fourier and time-splitting methods are prior
work; no novelty or practical advantage is claimed.

For d=J, gamma=J/4, tau=0.1/J and N=256, correlation errors bounded by 0.002 suffice
for per-block TV below 0.02834 before arithmetic, at any block size in this family.
The numerical control perturbs exact six-spin values; no scalable classical
algorithm was run to acquire those values. Add the spatial error from Note 21
for the full-chain mixture. A per-draw guarantee is not automatically an M-draw
joint guarantee. Classical preparation can be reused across M samples.

The real generator and real initial raising vector give C(2s)=u(s)^T u(s).
This is a bilinear half-time contraction, not u(s)^dagger u(s). A normalized
operator-state error delta gives correlation error at most 2delta, but accurate
scalar contractions do not require accurate reconstruction of every operator
component. Classical half-time tensor, direct resolvent, restricted-state and
recursion routes remain legitimate. Their required ranks and acquisition costs
are unknown in the target growing-block regime. Direct quantum spectral sampling
remains allowed and is not required to learn or output these classical scalars.

The [work order](work_orders/CURRENT.md) requests one response-sensitive acquisition
cost analysis, not more generic readout machinery or another six-spin census.
No useful quantum-classical separation, observed spectral prediction improvement,
compiled quantum circuit, or new repository is established or needed.

## Executed evidence

The new checker ran twice with identical JSON under single-threaded BLAS. Python
integers and Fractions generate moments through order 80 for the full six-spin
model and two surrogates, rigorous cosine/exponential enclosures, conservative
bin witnesses and two exact signed-bin controls. Lower bounds are rounded down.
Complex128 eigendecomposition independently checks the return amplitude; four
half-time identities, ten clock-kernel/Fourier identities, two perturbation-budget
controls and a negative-bin case also pass. Six invalid inputs and -O/-OO execution
were rejected. The [report](experiments/response_readout_v1/REPORT.json) records
values and distinctions between the exact and floating calculations.

Checker SHA256: `6777ad07343c4ee1ade0c90d4255056b2116daaab8a70f4b2e51a269be6b702e`.
Report SHA256: `5d8199805b35d0ed4f970451f302400a2f584f064536d9c321a39de6eaf7c869`.

No tensor-network algorithm, native NMR package, quantum circuit, experimental
spectrum, noise model, timing benchmark or large-system scaling experiment was
run. No prior scientific verifier was rerun, and no upstream data or code was
imported. Primary abstracts and metadata establish cited predecessor scope;
no PDF, figure or experimental table was analyzed this round. The bounded source
screen is not an exhaustive priority audit.

## Preserved evidence

The preceding ledger and its links remain at the pinned
[pre-readout checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/fdc88f1c59d743394001e28edf7b97a5270dba9c/STATUS.md).
Notes 15-21, earlier proofs, code, reports, datasets and rights are unchanged.
Older current/next headings are dated checkpoints, not competing work orders.
Climate/dynamics remain open; Manthan is paused; battery/operator routes parked;
both classical spin-offs independent; Phase-2 Note 27 closed. Manuscript remains
on hold. Only the parent repository is modified; no outside contact, paid or
unattended work, release, branch merge, new repository or administration change.
