# Smooth response compression 20: remove the cutoff, then count the transformation

28 September 2026. Baseline: `4628eb7a18823bbe3b974c07d11fc671da3ecb9e`.
Branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Decision:** a bounded polynomial of the FULL response generator avoids sharp-band
classification and gives an explicit positive sampling law with a response-weighted
error bound. It is an alternative to Note 19's downfolding, not a smooth projector
substituted into its Schur formula. The generic transform-then-simulate cost does
not improve the leading direct-sampling query scaling. That cancellation is already
recognized in spectral-amplification literature [2]. Do not continue generic cutoff
engineering as though a smaller encoded bandwidth by itself were a speedup.

Direct many-body spectral sampling remains open. No quantum-classical separation,
new primitive, experimental result, or publication-priority claim is established.
The next comparison should exploit physical interaction structure, not add another
generic spectral transformation. No data download or large simulation is needed.

## 1. Preserve the existing physical task

Use the same centered homonuclear spin model and collective raising response [1]:

$$
H=J\sum_{i=1}^{n-1}{\bf S}_i\cdot{\bf S}_{i+1}
+d\sum_{i=1}^n(-1)^iS_i^z,\qquad O=\sum_iS_i^+,
\qquad L=[H,\cdot],\quad o=O/\|O\|_F .
$$

The original response measure is the spectral law $\mu_L$ of self-adjoint $L$ in
$o$. The output is $\mu_L*\ell_\gamma$, subsequently assigned to the agreed bins,
where $\ell_\gamma(x)=\gamma/[\pi(x^2+\gamma^2)]$. Keep the SAME $\gamma$, bins and
total-variation tolerance. This is normalized high-temperature response with a
phenomenological common linewidth, not arbitrary pulse output or absolute intensity.

For even $n$, the exact collective commutator gives

$$
s^2:=\int\omega^2\mu_L(d\omega)=\|Lo\|^2=d^2.
$$

This is a moment of the unbroadened response, not of the Cauchy-broadened law.
The spin model, its input assumptions, state preparation and interpretation are
unchanged from Notes 15-19. For the explicit doubled Pauli encoding one sufficient
normalization is $\alpha=n|d|+3J(n-1)/2\geq\|L\|$ for $J>0$.

## 2. Change frequencies, not their statistical weights

Let $f$ be a bounded real function and set $K=f(L)$. The spectral theorem gives

$$
\mu_K=f_\#\mu_L,\qquad
p_{K,\gamma}(x)=\int\ell_\gamma(x-f(\omega))\,\mu_L(d\omega).
$$

The same eigenvectors carry the SAME probabilities. No positive or negative
spectral contribution is reweighted, and no postselection is required. $K$ need
not itself be a commutator with a smaller physical spin Hamiltonian; it is a
self-adjoint sampling generator on the existing doubled register.

This differs critically from applying $f(L)$ TO THE STATE and renormalizing:
that operation reweights the original law by $|f(\omega)|^2$ and can remove the
dominant zero-frequency line. The checker includes an explicit negative control.
A block encoding is used inside controlled simulation, not measured once and
mistaken for the desired sampling distribution.

Suppose $|f(\omega)-\omega|\leq\delta$ for $|\omega|\leq\kappa$. No restriction on
the frequency map outside the core is needed for the following bound:

$$
\boxed{
d_{\rm TV}(p_{L,\gamma},p_{K,\gamma})
\leq\min\left\{1,\ \mu_L(|\omega|>\kappa)+\frac{\delta}{\pi\gamma}\right\}
\leq\min\left\{1,\ \frac{s^2}{\kappa^2}+\frac{\delta}{\pi\gamma}\right\}.
}
$$

**Proof.** Couple both distributions using the same original spectral label
$\omega$. The TV distance of two equal-width translated Cauchy laws is
$2\arctan(|a-b|/(2\gamma))/\pi$, at most
$\min(1,|a-b|/(\pi\gamma))$. Convexity bounds the mixture difference by the average
of these distances. Split at $\kappa$ and use the second-moment inequality.

All probability mass is retained. The tail term pays for arbitrary relocation of
the original high-frequency mass, not for conditioning it away or declaring it
zero. Common binning cannot increase TV. Accuracy is absolute distributional
accuracy, not relative accuracy for an arbitrarily weak spectral line.

This is an elementary pushforward/coupling specialization, not a new abstract
sampling theorem. Its usefulness here is that $s^2=d^2$ is known without computing
the full spectrum. No global gap or cutoff-edge margin occurs.

### Why the earlier small-memory-weight warning does not invalidate this bound

The present weights are those of the FINAL full-generator spectral measure.
Functions of $L$ preserve these eigenspaces. There is no later coupling that
amplifies a discarded-sector estimate. By contrast, Note 17's small weights
belonged to a MEMORY measure that enters the response through a nonlinear
resolvent expression. Those two measures cannot be interchanged.

Likewise, applying the same formula to $f(L_0)$ while leaving the perturbation
unaccounted for is not justified: $L_0$ and the full $L$ need not share eigenvectors.
We smooth the full response generator, not the old unperturbed band projector.

## 3. An existing bounded-polynomial construction supplies the quantum operation

Assume $0<r=\kappa/\alpha\leq1/2$. The linear-amplification polynomial of Low and
Chuang [2, Theorem 10] supplies an odd real $P$ with

$$
|P(x)|\leq1\quad (|x|\leq1),\qquad
\left|P(x)-\frac{x}{2r}\right|
\leq\vartheta\frac{|x|}{2r}\quad (|x|\leq r),
$$

of degree $q=O(r^{-1}\log(1/\vartheta))$ in its stated small-error range
$\vartheta\leq c r$ for a universal constant $c$. One can reduce the chosen
$\vartheta$ to meet that range. This costs only an additional logarithmic
precision factor; its construction is prior work, not reproduced as a new
polynomial-synthesis algorithm here.

Define

$$
\boxed{K_\kappa=2\kappa P(L/\alpha).}
$$

It is self-adjoint, has norm at most $2\kappa$, and satisfies the previous
certificate with $\delta=\vartheta\kappa$:

$$
d_{\rm TV}(p_{L,\gamma},p_{K_\kappa,\gamma})
\leq\min\{1,d^2/\kappa^2+\vartheta\kappa/(\pi\gamma)\}.
$$

There is no demand to decide whether an eigenvalue is infinitesimally above or
below $\kappa$. The polynomial is defined everywhere; even a frequency exactly
at the chosen core boundary is allowed. No eigenbasis, gap certificate, inverse,
or separately prepared projector is supplied.

For example, allocate half a total error $\epsilon$ to the frequency map. For
$d\ne0$, choose $\kappa=2|d|/\sqrt{\epsilon}$ and
$\vartheta\leq\pi\gamma\epsilon/(4\kappa)$, reduced further if required by [2].
Each term is then at most $\epsilon/4$. The remaining half is for finite-clock,
wrap, digital-bin, preparation, block-encoding and controlled-simulation errors.
This is useful bandwidth compression only when $\kappa\leq\alpha/2$. Otherwise
use the direct construction. At $d=0$, the response is already the known single
line; no quantum computation is needed for this observable.

Standard polynomial eigenvalue transformation [2,3] block-encodes $K_\kappa$
with normalization $2\kappa$, up to an optional fixed-factor convention.
Use Note 15's geometric clock on this generator. In the ideal limit it samples
the positive law just written, with the SAME requested Lorentzian linewidth.
The finite clock, offset and bin errors remain those of Note 15. Do not identify
an arbitrary phase-estimation kernel with the instrument response.

An additional Hermitian implementation error $\xi$ in $K_\kappa$ contributes
at most $\xi/(2\gamma)$ to TV by Note 15's resolvent bound. If the normalized
block error is $\eta$, then $\xi=2\kappa\eta$ and the contribution is at most
$\kappa\eta/\gamma$. State-preparation and actual controlled-circuit errors must
also be budgeted. Coefficient-list access and inverse circuit calls are not free.

## 4. The central cost result: a reduced norm is not a reduced query budget

One call to the compressed block uses

$$
q=\widetilde O(\alpha/\kappa)
$$

calls to the original block. The direct linewidth-matched sampler applied to
$K_\kappa$ uses $\widetilde O(1+\kappa/\gamma)$ compressed-block calls per sample.
Consequently the modular construction has sufficient base-query cost

$$
\boxed{
C_{\rm soft}=\widetilde O\!\left[
\frac{\alpha}{\kappa}\left(1+\frac{\kappa}{\gamma}\right)\right]
=\widetilde O(\alpha/\kappa+\alpha/\gamma).
}
$$

The direct original-generator construction has
$C_{\rm direct}=\widetilde O(1+\alpha/\gamma)$. The apparent bandwidth gain is
therefore cancelled in the leading term by constructing the amplified block.
At $\gamma=c d^2/J$, the generic soft construction still carries
$\widetilde O(\alpha J/(c d^2))$; Note 18's conditional elimination of that
weak-field power has NOT been recovered.

These are sufficient symbolic budgets, not competing runtime measurements or a
universal lower bound on spectral sampling. Low and Chuang already explicitly
identify this absence of simulation gain for generic spectral multiplication
[2, Section 1.1.1]. Its usefulness for other measurement tasks is a different
comparison. We are applying that known warning to this response-weighted task.

### Why a magically cheap uniform transformer does not fix this route

The following is the standard oracle-hybrid argument behind [3, Theorem 73],
restated only to make its scope explicit. Let

$$
U_x=\begin{pmatrix}x&\sqrt{1-x^2}\\\sqrt{1-x^2}&-x\end{pmatrix}.
$$

It block-encodes the scalar $x$, and $\|U_r-U_{-r}\|=2r$. A $q$-query unitary
circuit with oracle-independent intervening operations differs by at most $2qr$
between these two oracles. To output blocks approximating the amplified values
$+1/2$ and $-1/2$ with absolute error $\zeta<1/2$ requires

$$
q\geq(1-2\zeta)/(2r)=\Omega(\alpha/\kappa).
$$

This is a restriction on a GENERIC uniform block transformation. Our explicit
spin parameters are not hidden scalar oracles, and a state-dependent or integrated
spectral sampler need not implement that transformation. It is not an NMR
hardness theorem, a lower bound on all sampling, or a proof that direct evolution
is optimal for this model.

Known spectral amplification near a spectral endpoint and constructions exploiting
additional input structure can do better in their settings [2, Theorem 3].
Our response is near zero in a signed INTERIOR energy-difference spectrum;
a low absolute frequency is not a ground-state energy. Do not transfer an
endpoint theorem by simply renaming the origin.

## 5. Consequence for the research direction

This answers the bounded question: sharp-edge classification is avoidable without
changing the task, but generic smooth bandwidth compression is not the missing
speedup. The construction is not a faster Schur model, and a projector substituted
by a non-idempotent filter in Note 19 remains invalid. Smooth Feshbach maps also
have an established independent literature [4]; their existence is not a supplied
positive response sampler or a cost guarantee.

Do not expand this result into a new filter compiler, an extra algorithmic
framework, or a third classical spin-off. Retain it as a completed comparator.

The next bounded model-level question should exploit the PHYSICAL locality of
the spin model: how large a spatially connected region is needed to reproduce
the collective spectral law at the specified linewidth, including its cross
correlations? Look for a positive overlapping-window/block construction with
controlled error, not an unjustified mixture of independent single-spin spectra
(the latter failed Note 16's exact control). Charge selecting and constructing
the blocks for both sides.

This asks whether the relevant finite-resolution many-body calculation can be
made small classically, or whether direct coherent dynamics avoids constructing
a genuinely expensive response representation. Classical tensor/restricted-state
methods [5,6] and local quantum simulation [7] are the relevant precedents. Their
assumptions must be checked; no locality-based TV bound for this collective
construction has been derived here. Keep the same gamma, approximation scope and
sample count, and do not treat an exponential upper bound as a classical lower
bound. A complete experimental calibration is still not an entry condition.

## 6. Executed checks and scope

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/smooth_response_v1/verify.py`

The independently written NumPy checker ran twice with identical JSON and exit
code zero; -O/-OO refused execution. Three fixed n=2,4,6 spin chains check six
moment identities, six smooth-cap comparisons and three bounded cubic-polynomial
comparisons. Eight boundary-continuity checks, four Cauchy-translation checks,
six invalid-input rejections, and a state-filtering negative control are included.

The C2 cap is a simple scalar analytic control, NOT the efficient amplification
polynomial from [2]. Its smooth-core identity and bounded plateau can be proved
directly. The cubic $P(x)=(3x-x^3)/2$ is a genuine bounded odd polynomial but only
a fixed small control, not a scalable compiler. No general QSVT polynomial was
numerically synthesized and no phase sequence, circuit or timing was executed.

The negative control changes a law with 98% mass at zero by applying the map to
the state; its binned discrepancy is about 0.915. It is explicitly artificial
and only detects the difference between generator transformation and state
postselection. It is not a workload or evidence of useful quantum advantage.

All numerical checks are complex128 at tolerance 3e-10, not interval certificates.
The continuous bounds follow from the proof. No experiment, physical dataset,
native NMR package, quantum hardware or performance study was used. Older
scientific verifiers were not rerun; their files remain unchanged. Both subprocess
runs also emitted an unrelated spreadsheet-runtime startup warning on stderr;
the diagnostic itself completed and produced identical valid reports.

Checker SHA256: `8cfee7c5a3bd48363b73223b3b21806dd0fb2f7b7ad9b215617094af1ee5b6b0`.
Report SHA256: `8cf2bc4d7d0dfc269e27f5afbad6832fef7d7818034e54df03c4f70fea4e7d2c`.

## Primary sources and inspection scope

Checked 28 September 2026. This is a focused predecessor/comparator check, not
an exhaustive priority audit. No cited source independently certifies our
application of its theorem or the new report.

[1] Sels et al., *Quantum approximate Bayesian computation for NMR model inference*,
Nature Machine Intelligence 2 (2020), arXiv:1910.14221. Primary abstract rechecked;
model conventions explicitly inherited from Notes 15-19.
https://arxiv.org/abs/1910.14221

[2] Low and Chuang, *Hamiltonian Simulation by Uniform Spectral Amplification*,
arXiv:1707.05391v1. Section 1.1.1 and Theorems 2-4 and 10 inspected in primary
PDF text; page 4 (zero-based 3) visually checked. The theorem-10 screenshot failed,
but its formula was available as text. No numerical figure was interpreted.
https://arxiv.org/abs/1707.05391

[3] Gilyen et al., *Quantum singular value transformation and beyond*,
arXiv:1806.01838v1 / STOC 2019. Polynomial eigenvalue transformation and Theorem 73
inspected; PDF page 60 (zero-based 59) visually checked.
https://arxiv.org/abs/1806.01838

[4] Bach et al., *Smooth Feshbach map and operator-theoretic renormalization group
methods*, JFA 203 (2003), and Griesemer and Hasler, *On the Smooth Feshbach-Schur
Map*, arXiv:0704.3244. Primary publisher/author-record abstracts only; no claim
that their full hypotheses or a spectral-measure reconstruction were audited.
https://doi.org/10.1016/S0022-1236(03)00057-0
https://arxiv.org/abs/0704.3244

[5] Savostyanov et al., *Exact NMR simulation of protein-size spin systems using
tensor train formalism*, PRB 90, 085139 (2014). Primary abstract and topology scope.
https://arxiv.org/abs/1402.4516

[6] Karabanov et al., *On the accuracy of the state space restriction approximation
for spin dynamics simulations*, JCP 135, 084106 (2011). Primary abstract; relaxation
conditions are not replaced by a common linewidth.
https://arxiv.org/abs/1104.3866

[7] Haah et al., *Quantum algorithm for simulating real time evolution of lattice
Hamiltonians*, FOCS 2018 / SIAM J. Comput., arXiv:1801.03922v4. Primary abstract
on local simulation and its model; no bound transferred to our collective
spectral output without an additional argument.
https://arxiv.org/abs/1801.03922

Only Quantum-Assisted-Algorithm-Discovery may be modified. Climate/dynamics remain
open; Manthan is paused, battery/operator routes parked and the two spin-offs
independent. No outside contact, paid/unattended work, manuscript revival,
release, merge or new repository follows. Earlier research and rights are retained.
