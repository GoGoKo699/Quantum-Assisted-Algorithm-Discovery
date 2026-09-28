# Claim ledger

## Current checkpoint: resonance-window response bounds, 28 September 2026

[Note 19](exploration/phase_3/RESONANCE_WINDOW_19.md) retains all operator frequencies
inside a chosen band instead of only the exact conserved sector. The Hermitian
static Schur generator K=PLP-PLQ(QLQ)^-1QLP retains finite-frequency and first-order
resonant dynamics. If ||L-L_0||<=e<kappa, the eliminated inverse has scale at least
beta=kappa-e. The approximation theorem needs no minimum nonzero frequency or
gap at the cutoff and does not assume the parity cancellation of Note 18.

A continuous-TV bound compares the full and reduced Lorentzian-broadened spectral
laws using a central analysis window, cross-block coupling and both unbroadened
second moments. Both distributions' outside mass is accounted for. The collective
spin moment is exactly d^2, not the extensive norm-squared bound. A sharper term
uses a damped response-weighted exposure to the eliminated modes. Its acquisition
and numerical errors are not free. Common binning preserves the bound. This is
a sufficient approximation result, not a necessary accuracy test or hardness proof.

At fixed n and fixed cutoff/J, the derived sufficient error tends to zero as
O((|d|/J)^(2/3)) for linewidth c d^2/J with a suitable analysis window. No size-
uniform compression or empirical scaling law is asserted. Internal resonances
are retained rather than discarded on the basis of small spectral weight.

## The quantum resource question remains distinct

A standard block-encoding construction can implement the complementary inverse
and effective-generator products GIVEN controlled band-projector access. Sharp
spectral classification may require its own cutoff-edge margin. The generic
query budget can be worse than direct spectral sampling, and no inverse-d
cancellation from Note 18 is automatically inherited. A smaller operator norm
is not an automatically cheaper block encoding. No gap-independent quantum
algorithm, useful quantum-classical separation, runtime advantage or publication
priority is established. Schur maps, quantum filtering and downfolding are prior work.

The [current work order](work_orders/CURRENT.md) requests one smooth or response-
weighted alternative with a proved output-law error and a complete symbolic
comparison. It does not request another data acquisition or implementation campaign.
Classical effective models, symmetry, recursion and tensor representations remain
competitors; their preprocessing can be reused. Direct quantum samples remain
permitted and the model-first sequence remains in force.

## Executed evidence

The independent NumPy checker ran twice with identical JSON under single-threaded
BLAS; -O/-OO refusals were checked. Three fixed open spin chains of 2/4/6 sites
use full coherence +1 sectors of dimensions 4/56/792, with retained dimensions
2/20/98. Three small block controls retain tiny coupled frequencies and nearly
coincident cutoff-edge levels. These sizes do not establish a scaling law.

The [report](experiments/resonance_window_v1/REPORT.json) records six binned
comparisons, 15 each of Schur/correction/resolvent identities and self-energy
bounds, six moment/exposure bounds and damped integral equations, a wrong-first-
order negative control, and six invalid-input rejections. They are complex128
diagnostics at tolerance 3e-8, not interval certificates. Cancellation-sensitive
resolvent tests use operand-scaled residuals. Continuous guarantees follow from
the proof rather than finite bins or quadrature.

No experimental spectrum, native application, quantum circuit, hardware, model
training, or performance measurement was run. No older scientific verifier was
rerun and no upstream code/data were imported. Primary Feshbach and QSVT methods
and the March 2026 related effective-Hamiltonian paper were inspected at the
scope stated in the note. One Feshbach PDF page was visually checked; other stated
screenshot attempts failed and supplied no figure-derived results. The source
search was bounded, not an exhaustive novelty audit.

## Preserved historical evidence

The preceding ledger and its evidence links remain at the pinned
[pre-window checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/227f041c3431d11e7adaf9b3815fc24ca8ea03a2/STATUS.md).
Notes 15-18 and their source, proofs, diagnostics and reports are unchanged.
Old current/next headings are checkpoint records, not competing work orders.

Climate/dynamics remain open; missing climate records block only their empirical
test. Manthan remains paused, battery/operator routes parked, both classical
spin-offs independent, and Phase-2 Note 27 closed. Manuscript remains on hold.
Prior notes, data, code, licenses and third-party rights are preserved. Only
Quantum-Assisted-Algorithm-Discovery is modified; no contact, paid/unattended work,
release, merge, new repository or administration change occurred.
