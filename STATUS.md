# Claim ledger

## Current checkpoint: bounded activity estimation, 29 September 2026

[Claim 28](exploration/phase_3/EMISSION_ACTIVITY_CLAIM_28.md) specifies one candidate
quantum benefit after the strategic revision: estimate a bounded correlation of
photon counts in successive finite windows. This explicitly narrows the earlier
full-record output. It is not a complete count-distribution, switching-rate,
stationary phase or fine-record solution. The bounded transform is chosen here;
its numerical tolerance is not asserted to be an experimental standard.

For counts K1,K2, s=u/(n kappa Delta) and u=1, the target is
G=E exp(-s(K1+K2))-E exp(-sK1) E exp(-sK2). An exact absorbing-flag embedding
retains the three needed Laplace moments as probabilities. The original system
marginal is unchanged. Intensity and Jensen bounds give Z1,Z2>=exp(-u) and
Z12>=exp(-2u); these do NOT bound G away from zero. Independent coherent emitters
can have nonzero G, so this is not an entanglement or hardness witness.

Known high-accuracy Lindblad algorithms plus standard amplitude estimation give
~O(1/epsilon) coherent simulator/inverse calls at additive error epsilon, with
explicit channel bias and failure budgets. One sufficient local-input gate bound
is ~O((n+edges)(1+Gamma T)/epsilon), Gamma=n|Omega|/2+edges|V|/4+n kappa,
with accuracy logarithms, coefficient access and coherent workspace charged.
It is not a compiled resource count or an improved simulation primitive. Retaining
only two flags does not mean that environmental simulation ancillas can be erased
before inversion. The method cannot accelerate already measured laboratory data.

This improves generic sampling precision, not every classical method. Direct
tilted propagation and a supplied adequate small phase generator can compute the
same statistic without Monte Carlo. Their acquisition, within-phase corrections,
initial transient and validation must be costed. The bound ||Ls-L||<=u/Delta makes
long windows a small tilted perturbation and can favor the classical reduction;
it is not an all-size metastability theorem. No useful quantum-classical separation,
new physical prediction or publication novelty is established.

The [work order](work_orders/CURRENT.md) asks for the matched acquisition/validation
cost of that one tilted observable. The source anchor is the periodic Ising family,
including V/kappa=250,Omega/kappa=50 in Rose et al.'s finite-size study; this is not
silently transferred to the earlier open/equal-scale examples. Ground initialization,
finite horizon and physical observation scale remain explicit. A cheap adequate
classical tilted description ends this claim's priority; no generic flag framework
or another small-model census is the next task.

## Executed evidence and limitations

The new checker ran twice with identical JSON and rejected -O/-OO and six invalid
inputs. One three-emitter periodic Omega=V=kappa=1,Delta=u=1 control compares the
flag generator against independent tilted contractions, preserves the physical
marginal, and verifies jump completeness and normalized probabilities. An exact
Fraction control distinguishes absorption from parity. Independent coherent
emitters and an illustrative supplied two-state classical model are positive
bypass controls, not approximations claimed adequate for the interacting target.

Checker SHA256: `67685e9d3d5ccde748aa2d27ae7b13300ca6a883912c191b05b2f9bb860d0d0c`.
Report SHA256: `2b7d3394d731e0ccdf10e5a7931d9a961568373b40a0eb2ac4e8b60e627e7b44`.
The [report](experiments/activity_flags_v1/REPORT.json) uses rounded complex128
diagnostics, not interval certification. General claims follow from the equations
and cited algorithms, not extrapolation of that control. No amplitude estimation,
channel-simulation circuit, published metastable-slice calculation, large system,
experimental data or performance benchmark was executed. No earlier verifier
was rerun and no upstream code/data imported.

Primary model, metastability, amplitude-estimation and high-accuracy simulation
sources were inspected to the scope stated in the note. One model PDF page was
visually checked; other requested screenshots failed, and no graph was digitized.
This is a bounded source check, not a complete novelty or proof audit.

## Preserved evidence

The preceding ledger and evidence links remain pinned at the
[pre-claim checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/0fcf4d7c979003bc2d2508dfb3cde1c4cf4657af/STATUS.md).
All earlier proofs, code, reports, licenses and rights are unchanged. Other
mechanisms remain available; the two spin-offs remain independent. Manuscript
preparation is on hold. No new repository, contact, paid/unattended work, release,
merge or administration change is part of this checkpoint. Only the parent is writable.
