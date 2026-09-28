# Resonance window 19: retain small frequencies instead of inverting them

28 September 2026. Baseline: `227f041c3431d11e7adaf9b3815fc24ca8ea03a2`.
Working branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Outcome:** a retained-frequency-band model has a positive spectral law with an
explicit continuous-total-variation (TV) error bound. The approximation needs no
minimum nonzero frequency and no separation between neighboring frequencies at
its cutoff. First-order resonant couplings are retained. However, implementing a
sharp band projector is a separate operation that can require cutoff-edge
resolution. This is NOT a gap-independent quantum algorithm or an established
advantage. We distinguish approximation, inverse conditioning, and projector
access rather than hide a gap in a renamed parameter.

The question remains direct sampling of the high-temperature spin response, not
building another classical spin-off. This checkpoint changes neither the physical
model nor the output resolution. It uses established Schur/downfolding and quantum
filtering ingredients [1-4]; priority for the displayed TV specialization is not
established. No experimental spectrum or hardware timing is claimed.

## 1. The model and the changed reduction

Retain Notes 15-18's uniform even open spin-1/2 chain,

$$
H(d)=J\sum_i\mathbf S_i\cdot\mathbf S_{i+1}
       +d\sum_i(-1)^i S_i^z,\qquad O=\sum_i S_i^+,
$$

with supplied angular-frequency coefficients, hbar=1, and normalized operator
vector o=O/sqrt(n 2^(n-1)). The Liouvillian is L=L_0+E, where L_0=[H(0),.]
and E=d[V,.]. Then L_0 o=0 and ||L o||=|d| exactly; ||E||<=n|d| is a conservative
whole-space bound. The normalized correlation spectrum is convolved with
ell_gamma(omega)=gamma/[pi(omega^2+gamma^2)] and assigned to the shared bins.
The scalar-coupled high-temperature response has the NMR anchor in [1]. This
chain is a structural model family, not a newly validated molecular application.

Note 18 retained only ker L_0. Here choose a cutoff kappa>e, with ||E||<=e, and
retain ALL unperturbed operator frequencies in [-kappa,kappa]:

$$
P=\mathbf1_{[-\kappa,\kappa]}(L_0),\qquad Q=I-P.
$$

This is not the rank-one observable projector of Note 17 or necessarily the
zero-sector projector of Note 18. The low band may be degenerate and may contain
arbitrarily small nonzero frequencies. No reflection/parity-purity assumption is
needed. In particular, PEP is not set to zero.

On the P/Q decomposition put

$$
L=\begin{pmatrix}A&F^\dagger\\F&B\end{pmatrix},\qquad
A=PLP,\quad F=QLP=QEP,\quad B=QLQ|_{Q\mathcal H}.
$$

Since the unperturbed Q frequencies have magnitude greater than kappa,

$$
\|B^{-1}\|\leq\beta^{-1},\qquad \beta=\kappa-e>0.
$$

For example, this follows by the Neumann series for the inverse of QL_0Q+QEQ.
Both signs of the discarded spectrum are allowed. This is distance from zero,
NOT distance between every retained eigenvalue and every discarded eigenvalue.
If Q is empty, the reduction is exact and no inverse is needed.

The proposed Hermitian generator on the retained space is

$$
\boxed{K=A-F^\dagger B^{-1}F.}
$$

It is the static (z=0) Schur model. B includes QEQ; it is not replaced by QL_0Q
without a further error estimate. K keeps both the finite unperturbed frequencies
and the first-order perturbation inside P. Its spectral law in the SAME normalized
o is a positive probability measure. Adding the original Cauchy broadening gives
p_K. This is an approximation to the full physical response, not a memory spectrum
that is being relabeled as the output. There is no claim that K is exactly the
Hamiltonian of a smaller isolated physical spin system.

## 2. A response-level bound with no smallest-spacing parameter

The next statement holds for any finite-dimensional self-adjoint block L above,
unit o in P, and beta>0 satisfying ||B^-1||<=1/beta. Set

$$
c_F=\|F\|,\quad s^2=\|Lo\|^2,\quad s_K^2=\|Ko\|^2.
$$

These are second moments of the UNBROADENED spectral measures. The Cauchy-broadened
laws need not have second moments. The bound

$$
s_K^2\leq s^2\left(1+c_F^2/\beta^2\right)
$$

uses ||Ko||<=||Ao||+(c_F/beta)||Fo|| and ||Ao||^2+||Fo||^2=s^2.
For the spin model s^2=d^2, rather than the extensive estimate n^2 d^2.

For any 0<Omega<beta, let R=sqrt(Omega^2+gamma^2). Then

$$
\boxed{
 d_{\rm TV}(p_L,p_K)\leq\min\left\{1,
 \frac{c_F^2R}{2\gamma\beta(\beta-\Omega)}
 +\frac{2(s^2+s_K^2)}{\Omega^2}
 +\frac2\pi\arctan\frac{2\gamma}{\Omega}\right\}.
}
$$

The first term bounds the in-window difference; the remaining terms account for
BOTH full distributions outside that window. We have not replaced the requested
full spectrum by a conditional central window or renormalized discarded tails.
Common binning and further common probabilistic processing cannot increase TV.
This is a sufficient bound; its failure is neither approximation failure nor
classical hardness. The analysis window Omega can be optimized in the bound
without changing the requested linewidth or output bins.

### Proof: keep the energy dependence until its error is bounded

For z=omega+i gamma define S(z)=P(z-L)^-1P on P and R_K(z)=(z-K)^-1. The exact
Feshbach formula [2] is

$$
S(z)=[z-A-F^\dagger(z-B)^{-1}F]^{-1}.
$$

The discarded-space correction omitted by freezing at zero is

$$
D(z)=F^\dagger[(z-B)^{-1}+B^{-1}]F
=zF^\dagger(z-B)^{-1}B^{-1}F.
$$

Therefore S-R_K=S D R_K. For |omega|<=Omega,

$$
\|D(z)\|\leq\frac{c_F^2|z|}{\beta(\beta-|\omega|)}
\leq\frac{c_F^2 R}{\beta(\beta-\Omega)}.
$$

For any self-adjoint M and unit vector u, spectral integration gives
integral_R ||(omega+i gamma-M)^-1 u||^2 d omega=pi/gamma. Compression cannot
increase the norm, so the same integral is an upper bound for S(z)^dagger o.
Use Cauchy-Schwarz on the quadratic form of S D R_K, then multiply by 1/(2pi)
to convert the integrated resolvent difference to TV. This proves the first term.

For a random variable X with either unbroadened spectral law, and independent
Z~Cauchy(gamma),

$$
\Pr(|X+Z|>\Omega)\leq
4\mathbb E[X^2]/\Omega^2+(2/\pi)\arctan(2\gamma/\Omega).
$$

Half the sum of these two tail bounds gives the remaining terms. No assumption
on memory decay, an invariant perturbed low band, or all-size energy degeneracies
was used. Unlike an eigenvalue-only estimate, this argument covers line weights
and all mass that the reduced model assigns differently.

### A sharper response-weighted variant

Let X=B^-1 F and define the nonnegative quantity

$$
\rho_K=2\gamma\int_0^\infty e^{-2\gamma t}
\|X e^{-itK}o\|^2dt\leq c_F^2/\beta^2.
$$

The first term of the boxed bound can be replaced by

$$
\frac{c_F R\sqrt{\rho_K}}{2\gamma(\beta-\Omega)}.
$$

Indeed, write the quadratic form of S D R_K as the product of F S^dagger o,
(z-B)^-1, and X R_K o. Bound the first factor by c_F||S^dagger o|| and use
Parseval to obtain integral ||X R_K o||^2=pi rho_K/gamma. This yields the displayed
term. The bound follows the retained RESPONSE as it reaches the eliminated modes,
not merely the existence of such modes. The cost of computing rho_K is not free:
classically it requires the retained dynamics and the inverse action X.

If K=U diag(lambda_j) U^dagger, a=U^dagger o, and M=U^dagger X^dagger XU,
then rho_K=sum_jk a_j^* a_k M_jk 2gamma/[2gamma+i(lambda_k-lambda_j)]. The real
value is nonnegative; cancellation and coefficient errors need rigorous control
before treating a floating-point evaluation as a certified numerical bound.

## 3. What changes in the weak-field regime

No parameter g=min{|lambda|:lambda!=0 in spec L_0} occurs. A tiny frequency inside
P remains in K, including its first-order and higher-order influence through B.
It has not been discarded because its unperturbed frequency was small.
Nor do eigenvalues just inside and just outside kappa invalidate the approximation
bound: both are far from the CENTRAL frequencies at which the resolvent was bounded.

For gamma=c d^2/J, fixed n and fixed kappa/J, choose, for sufficiently small
x=|d|/J, Omega/J proportional to x^(2/3). Using c_F<=n|d|, s^2=d^2, and the bound
on s_K, the displayed error is O_{n,kappa/J,c}(x^(2/3)). This statement is about
the sufficient bound, not an observed scaling fit. The constants retain n, and
no thermodynamic or size-independent compression theorem follows. Arbitrarily
close internal resonances are allowed because they are retained.

K is not necessarily d^2 times a fixed generator. Retained nonzero frequencies
and PEP can matter at first order. Consequently Note 18's removal of an inverse-d
power from its quantum query budget does NOT automatically transfer here.
A two-state resonant control with L_0=0 and perturbation d X has lines at +/-d;
dropping its first-order block gives a central-bin discrepancy 0.83269043 at
gamma=0.1d. This elementary control is not a hard physical example or a new result;
it checks why first-order resonances must remain.

## 4. Quantum access: three different gaps must not be conflated

The mathematical reduction replaces the old smallest nonzero frequency by the
chosen discarded-frequency scale beta. It does NOT supply the band projector.

* **Internal small spacings:** arbitrary inside P; not inverted in K.
* **Discarded inverse scale beta:** a lower bound on |spec B|; needed for B^-1.
* **Cutoff-edge margin h:** the distance of |spec L_0| from kappa; can enter the
  cost of approximating a SHARP projector from spectral queries.

QSVT/filtering [3] gives a standard uniform operator-error realization of the sharp
projector with degree O((alpha_0/h) log(1/eta)) when a suitable margin h>0 is
promised, where alpha_0 normalizes the L_0 block encoding. This is a sufficient
construction, not a lower bound against every state-dependent implementation.
If h is tiny or unknown, a constant-cost reflection about P is not justified.
A smooth filter need not resolve h, but it is not an orthogonal P; substituting
one into this proof requires a new transition-band/residual error bound.

Given a valid controlled P operation, extend B to the full register as
B_ext=QLQ+beta P. It is invertible with ||B_ext^-1||<=1/beta. For alpha_L=alpha_0+e,
a conservative LCU normalization is alpha_B=alpha_L+beta. A standard QSVT inverse
uses O((alpha_B/beta) log(1/eta)) B_ext block calls, then restricts both ends with Q.
F=QEP uses the smaller perturbation block, not the entire L block.

The static K can thus be block encoded without enumerating its eigenmodes, with
one conservative normalization

$$
\alpha_K=\alpha_0+e+2e^2/\beta.
$$

Here the factor two allows the usual bounded inverse normalization. A better
operator-norm bound is ||K||<=kappa+e+c_F^2/beta, but that inequality does not by
itself provide a block encoding normalized to this smaller value. Rescaling or
building that encoding has a cost too.

Applying Note 15's geometric-clock sampler to K preserves the desired direct
sample output up to this note's model error and the separate algorithmic error.
A conservative base-block count, with controlled P treated as a counted operation,
is

$$
\widetilde O\left[
 \frac{\alpha_B}{\beta}\left(1+\frac{\alpha_K}{\gamma}\right)\right].
$$

Each such base operation includes its coefficient access, projectors, inverses and
controls. Clock/state preparation, finite output, and M repetitions also count.
The generic bound need not beat the direct sampler's ~1+alpha_L/gamma. This round
removes an unnecessarily global gap from an APPROXIMATION theorem, not from every
resource of an efficient implementation. The unresolved projector/bandwidth costs
are explicit and can erase a putative benefit.

The March 2026 v2 study [4] also uses quantum Schur complements and complementary
resolvents. Its inspected theorems treat a chosen small reference subspace,
eigenvalues and lifted eigenspaces, and retain a distance to the complementary
spectrum. Here the object is a possibly large high-temperature operator band and
a normalized broadened spectral law. This distinguishes tasks; it is not a claim
that this checkpoint outruns that method or establishes publication priority.

## 5. Classical competitor and the next useful question

The same K is a classical downfolding construction. If a compact symmetry-resolved,
Krylov, tensor-network or other representation suffices, it may be built once and
sampled many times. The retained dimension, needed inverse actions and inference
cost must be assessed at the same gamma and output law. Dense eigendecomposition
of the entire operator space is a verification tool here, not the strongest
classical algorithm. Failing this sufficient bound does not establish hardness.

The next bounded task is to replace sharp-band membership with a justified smooth
or response-weighted construction, and compare its ENTIRE symbolic cost to the
direct quantum sampler and a suitable classical reduction. It must preserve
positive spectral probabilities and account for transition-shell couplings; a
small shell's initial weight alone is not sufficient. Alternatively, a symmetry-
accessible retained space could avoid spectral classification, but must be derived
for this model, not supplied as an oracle. No new general solver, molecule search,
large sweep or third spin-off is warranted. The climate/dynamical family remains
open; failure of this particular reduction would not close direct sampling.

## 6. Checks actually run

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/resonance_window_v1/verify.py
```

The independent NumPy checker uses three fixed open chains (n=2,4,6) and three
small block controls. Spin calculations keep the entire coherence +1 operator
sector, which contains o and is invariant under both L_0 and E; they do not keep
only maximum-spin states. Sector dimensions are 4,56,792 and retained dimensions
in the selected cutoffs are 2,20,98. These are finite structural checks, not an
empirical growth law, physical performance claim or recommendation of a compound.

Six binned bound comparisons passed. The two/four-spin and block controls checked
15 each of the Schur, correction and compressed-resolvent identities and the
self-energy norm bound. All six cases checked the response-moment and dressing-
exposure bounds and their damped integral equation. Controls retain genuinely
coupled tiny frequencies and move levels to within 1e-9 of a cutoff while keeping
beta>0.49; this separates the analytic inverse bound from sharp-filter access.
The wrong first-order omission is detected, and six invalid parameter choices
are rejected. Coherence-sector construction preserves collective cross terms.

The final script ran twice with identical JSON; -O/-OO refusals were checked.
Tolerance is 3e-8, complex128. Resolvent difference residuals are scaled to BOTH
large operand resolvents, not to their cancellation-sensitive small difference.
The very narrow numerical line comparisons are diagnostic values, not interval
certificates. Continuous-TV claims follow from the written proof rather than
these finite bins. No experimental spectrum, native application package, quantum
circuit, hardware run, model fitting, or timing benchmark was performed.
No previous scientific verifier was rerun. No upstream code or data was imported.

Checker SHA256: `5564192e7b55c63381a21730c82147670b7be98c4c76ddc34ba82bc45c314b24`.
Report SHA256: `dc6d29b20b7ab5ab7b9075c4b54a6e6c97675cf7aa93c108a17b074233160cd7`.

## Primary sources and inspection scope

Sources checked 28 September 2026; a bounded predecessor check, not an exhaustive
priority audit. No source independently validates the new bound.

[1] Sels et al., Quantum approximate Bayesian computation for NMR model inference,
Nature Machine Intelligence 2 (2020), arXiv:1910.14221. Primary abstract rechecked;
model/normalization conventions inherited explicitly from Notes 15-18.
https://arxiv.org/abs/1910.14221

[2] Dusson, Sigal and Stamm, The Feshbach-Schur map and perturbation theory (2021),
arXiv:2105.02058. Theorem 1.2 and resolvent formulation inspected; PDF page 4
(0-based page 3) visually checked. Schur theory is a prior method.
https://arxiv.org/abs/2105.02058

[3] Gilyen et al., Quantum singular value transformation and beyond (STOC 2019),
arXiv:1806.01838. Theorems 31 and 41 on threshold projectors and pseudoinverses inspected in
primary PDF text; not a new audit of all polynomial synthesis theorems.
https://arxiv.org/abs/1806.01838

[4] Li et al., Quantum Algorithm for Low Energy Effective Hamiltonian and
Quasi-Degenerate Eigenvalue Problem, arXiv:2510.08088v2, 21 March 2026. Inspected
PDF introduction, Theorems 1-2, complementary-distance and reference-access
assumptions. Relevant screenshot attempts failed; no figure/table numbers were
used. No native numerical result reproduced.
https://arxiv.org/abs/2510.08088

[5] Sels and Demler, Quantum generative model for sampling many-body spectral
functions, PRB 103, 014301 (2021), arXiv:1910.14213. Primary abstract rechecked;
direct spectral sampling remains prior work, not this checkpoint's novelty.
https://arxiv.org/abs/1910.14213

Repository reads used the GitHub connection. A direct runtime raw-file transfer
failed on DNS; no checkout or experimental packet was obtained. Historical notes,
code, results, licenses and the two independent spin-offs are unchanged. Only
Quantum-Assisted-Algorithm-Discovery may be modified. No external contact,
paid/unattended work, manuscript revival, release, merge or new repository.
