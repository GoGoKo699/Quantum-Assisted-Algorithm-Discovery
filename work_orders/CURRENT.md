# Current task: remove artificial cutoff resolution without changing the sampled response

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read [resonance window 19](../exploration/phase_3/RESONANCE_WINDOW_19.md),
[slow-sector sampling 18](../exploration/phase_3/SLOW_SECTOR_SAMPLING_18.md), and
[model comparison 15](../exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md).
Models and quantum integration precede implementation. Direct samples remain
permitted; no learned classical program or quantum-free deployment is required.

## Completed mathematical result and its limit

Keep all unperturbed operator frequencies within [-kappa,kappa] in P, not only
the exact zero sector. For L=L_0+E with ||E||<=e<kappa, the discarded block
B=QLQ has ||B^-1||<=1/(kappa-e). The static Schur generator
K=PLP-PLQ B^-1 QLP is Hermitian and retains first-order resonant couplings.
Its positive spectral law in the original observable, broadened by the SAME
gamma and then binned, approximates the full response under Note 19's continuous
TV bound. Both distributions' tails are included, not silently discarded.

The bound uses a chosen response window, cross-block coupling, and the observable's
unbroadened second moments. Its sharper form weights the retained dynamics by
how much it reaches the eliminated modes. Neither the smallest nonzero frequency
nor a gap at the cutoff is an assumption of the approximation theorem. The even
spin chain has ||L o||=|d|, so the full moment is not an extensive n^2 d^2 estimate.
First-order cancellation and all-size reflection parity purity are unnecessary
for this enlarged model. Near resonances are retained, not declared negligible.

The quantum ACCESS question remains separate. A sharp spectral projector constructed
from L_0 may require a margin at kappa. Standard QSVT inverse operations then depend
on the discarded scale beta=kappa-e. These are different costs. No gap-independent
quantum sampler, useful quantum-classical separation, or practical speedup is
established. The generic product block-encoding upper bound may be worse than
ordinary direct spectral sampling. Note 18's removal of inverse-d powers cannot
be transferred automatically because K now contains finite-frequency and first-
order dynamics. A smaller operator norm is not a free better-normalized block encoding.

## Next bounded mathematical calculation

Investigate one smooth or response-weighted alternative to sharp-band membership,
with the same supplied spin model, collective observable, linewidth and bin law.
Derive the actual positive output law and the error from the transition region.
A smooth filter is not an orthogonal projector: do not substitute it into the
Schur proof unchanged. Initial spectral weight near a cutoff is not by itself
a bound on later coupling through that region. Preserve the small-denominator
warning from Note 17.

Alternatively, an explicitly symmetry-accessible retained space can avoid spectral
classification, but derive its adequacy for this family and charge its access.
Do not assume the full conserved sector or a list of its eigenvectors is free.
The deliverable is a correctness-and-cost statement for one construction, not a
new framework, extra toy census, hardware compilation or experimental campaign.

Compare the complete symbolic budget with Note 15's direct linewidth-matched
sampler AND with a strong classical reduction. Include normalization, filter
accuracy, inverses, coefficient access, state and clock preparation, repeated
samples and output arithmetic. Classical acquisition of an effective model can
be amortized. Failure of one truncation or a large retained dimension is not an
all-classical lower bound. A mathematically valid reduction that offers no cost
improvement should be recorded as such, not expanded indefinitely.

Schur/downfolding, QSVT, and spectral sampling are prior methods. The March 2026
quantum effective-Hamiltonian paper has related complementary-resolvent machinery;
the scoped distinction is our high-temperature operator spectral law versus its
small reference-space eigenproblem, not an established priority claim.

## Executed checks and preserved evidence

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/resonance_window_v1/verify.py`
ran twice with identical JSON; -O/-OO refusal was checked. Three fixed spin chains
(n=2,4,6) and three small block controls give six binned comparisons; 15 each of
Schur, correction and resolvent identities and self-energy bounds; six moment and
dressing-exposure controls; coupled tiny-frequency and cutoff-edge cases; a
wrong-first-order negative control; and six invalid parameter rejections.

These are complex128 diagnostics at tolerance 3e-8, not interval certification,
a growth law, quantum circuit, empirical spectrum or timing. Continuous-TV
statements follow from the written proof. No previous verifier was rerun and
no upstream code or dataset was imported. Primary methods were inspected, including
one successful Feshbach-page screenshot; other stated screenshot attempts failed.

Climate/dynamics remain open; missing climate records block only their empirical
test. Manthan remains paused, battery/operator routes parked, both spin-offs
independent, and Phase-2 Note 27 closed. Preserve earlier notes, proofs, code,
reports, data, licenses and third-party rights. Modify only Quantum-Assisted-
Algorithm-Discovery. No outside contact, paid/unattended work, manuscript revival,
release, merge, new repository or administration change is authorized.
