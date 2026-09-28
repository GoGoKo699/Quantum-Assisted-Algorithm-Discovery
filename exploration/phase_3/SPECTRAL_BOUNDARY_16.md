# Spectral boundary 16: how far must the observable spread before linewidth matters?

28 September 2026. Read baseline: `4d601cb7d0d58f552da40784e1f333edf6bf1d78`,
branch `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Outcome:** specialize established Lanczos/resolvent error machinery to the
actual Lorentzian-broadened sampling law. The resulting certificate depends on
one residual and propagation inside the retained observable space, not on the
unknown discarded spectrum. For a nearest-neighbor spin chain, the required
recursion data have an explicit local-Pauli construction. This identifies the
mathematical comparison parameter; it does not establish quantum advantage,
publication priority, or a new NMR algorithm.

The live repository's [model comparison 15](SPECTRAL_MODEL_STRUCTURE_15.md) is the
baseline: collective **raising** response and its linewidth-matched geometric
clock. The separate local `MODEL_FIRST_SPECTRAL_15.md` checkpoint discussed in
chat uses a Hermitian collective-X convention and a different sufficient clock
budget. It was read but is not silently substituted for, merged into, or used to
overwrite the live note. The present result applies to any normalized operator
vector, and is instantiated in the live note's raising convention.

## 1. One model family and the same useful output

Use the high-temperature scalar-coupled spin model motivated in Notes 14-15 and
[1,2]. For the complexity accounting, restrict to an open nearest-neighbor chain:

$$
H=\sum_{i=1}^n\delta_i S_i^z+
\sum_{i=1}^{n-1}J_i\,\mathbf S_i\cdot\mathbf S_{i+1},
\qquad O=\sum_i S_i^+.
$$

Coefficients are explicit real inputs in angular-frequency units, with
$|J_i|\leq J_*$ and $|\delta_i|\leq\Delta_*$ after removing the mean carrier.
This is a structural subfamily of the supplied spin model, not a claim that an
arbitrary measured molecule has only nearest-neighbor couplings. Neglected bonds
must be budgeted, for example by Note 15's cut bound. High-temperature response,
uniform detection weights, and the phenomenological linewidth are retained
assumptions, not a model of arbitrary pulse experiments or relaxation.

With $o=O/\|O\|_F$ and $L=[H,\cdot]$, the desired probability law is the spectral
measure of the self-adjoint operator $L$ in $o$, convolved with

$$
\ell_\gamma(\omega)=\frac{\gamma}{\pi(\omega^2+\gamma^2)}.
$$

Return the agreed frequency-bin labels within TV tolerance $\epsilon$, including
any needed overflow bins. This is normalized spectral shape, not absolute
intensity or a relative guarantee for arbitrarily weak lines. The coefficient
input, linewidth, bins and quality requirement are shared by both competitors.
No experimental trace or software installation is a prerequisite to this analysis.

## 2. The observable defines its own one-dimensional chain

Starting with $v_1=o$, exact Lanczos recursion for the self-adjoint $L$ gives
orthonormal operator vectors $v_j$, real $a_j$, and nonnegative $b_j$ such that

$$
Lv_j=b_{j-1}v_{j-1}+a_jv_j+b_jv_{j+1},\qquad b_0=0.
$$

Let $V_m=(v_1,\ldots,v_m)$ and let $T_m$ be the real symmetric tridiagonal matrix
with diagonal $a_1,\ldots,a_m$ and off-diagonal $b_1,\ldots,b_{m-1}$. Then

$$
LV_m=V_mT_m+b_mv_{m+1}e_m^T.
$$

If $b_m=0$, the retained space is invariant and its spectral law is exact. Otherwise
$b_m$ is the computed residual norm; setting it to zero without justification
would erase the very quantity that controls the truncation error.

This operator recursion, continued-fraction spectral representation, and Lanczos
quadrature are prior methods [3,4]. It is not a newly discovered reduction. It is
also not free: computing the coefficients requires constructing or otherwise
accessing the recursively generated operators. A short tridiagonal matrix need
not be cheap to discover from the original spin Hamiltonian.

Diagonalize only $T_m=U\operatorname{diag}(\lambda_j)U^T$. Its positive approximation
is the mixture of Cauchy lines at $\lambda_j$, with weights $U_{1j}^2$:

$$
p_{m,\gamma}(\omega)=\sum_{j=1}^m U_{1j}^2\ell_\gamma(\omega-\lambda_j).
$$

This is an explicit classical sampler after preprocessing, not a possibly negative
polynomial reconstruction. It is the **classical comparator**, not a requirement
that the quantum method first learn a classical model. Direct quantum samples
remain the permitted output.

## 3. A linewidth-weighted boundary certificate

Define a dimensionless number using only the small retained matrix:

$$
q_m(\gamma)=2\gamma\int_0^\infty e^{-2\gamma t}
\left|e_m^T e^{-itT_m}e_1\right|^2dt,\qquad 0\leq q_m\leq1.
$$

Interpretation: sample a time from an exponential law of rate $2\gamma$ and ask
for the probability that the retained observable-space evolution is at its last
basis vector. This is an interpretation of the integral, not a required extra
sampling algorithm or a physical relaxation model. The index labels generated
operator combinations, not a literal spin position or a fixed correlation order.

**Certificate (exact arithmetic, any finite-dimensional self-adjoint $L$):**

$$
\boxed{
 d_{\rm TV}(p_{H,\gamma},p_{m,\gamma})
 \leq \min\left\{1,
 \frac{b_m\sqrt{q_m(\gamma)}}{2\gamma},
 \frac{b_m^2 q_m(\gamma)}{2\gamma^2}\right\}.
}
$$

The entire discarded spectrum is unrestricted. The same bound holds after common
binning or further common probabilistic postprocessing. It is sufficient, not
necessary; its failure does not demonstrate an inaccurate approximation or
classical hardness. Neither the bound nor the actual approximation error is
claimed monotone with the number of Lanczos steps.

The quadratic term is a Lorentzian-TV specialization of the residual-square
quadratic-form mechanism in [4, Section 6]. Boundary insensitivity of recursive
spectral calculations is older still [3]. The contribution of this checkpoint is
making the comparison explicit for our output, not inventing Lanczos error theory.
Priority for this exact integrated formulation has not been established.

### Proof

Put $P=V_mV_m^\dagger$, $r=v_{m+1}$, $w=v_m$, and
$L_0=PLP+(I-P)L(I-P)$. Exact recursion and self-adjointness imply

$$
D=L-L_0=b_m(|r\rangle\langle w|+|w\rangle\langle r|).
$$

For $z=\omega+i\gamma$, write $R=(z-L)^{-1}$ and $R_0=(z-L_0)^{-1}$. The
second resolvent identity, used twice, is

$$
R-R_0=R_0DR_0+R_0DRDR_0.
$$

The first term has zero quadratic form in $v_1$, since $D$ crosses the retained
boundary. Since $(z-T_m)^{-1}$ is symmetric (not Hermitian), writing
$s_m(z)=e_m^T(z-T_m)^{-1}e_1$ gives the exact scalar identity

$$
\langle v_1,Rv_1\rangle-e_1^T(z-T_m)^{-1}e_1
=b_m^2s_m(z)^2\langle r,Rr\rangle.
$$

The square here is not an absolute square; absolute values are taken only when
bounding. Self-adjointness gives $\|R\|\leq1/\gamma$. The spectral density is
$-\operatorname{Im}\langle v_1,Rv_1\rangle/\pi$, and Parseval gives

$$
\int_{\mathbb R}|s_m(\omega+i\gamma)|^2d\omega
=2\pi\int_0^\infty e^{-2\gamma t}|(e^{-itT_m})_{m1}|^2dt
=\frac\pi\gamma q_m.
$$

Integrating the scalar bound and dividing by $2\pi$ proves the quadratic term.
For the linear term use $R-R_0=RDR_0$ instead, followed by Cauchy-Schwarz and
$\int\|R^\dagger v_1\|^2d\omega=\pi/\gamma$. The case $b_m=0$ is exact closure.
No diagonalization of the full $L$ or bound on its extensive norm is required.

### Evaluate the certificate without propagating the large system

If $c_j=U_{mj}U_{1j}$, then

$$
q_m=\sum_{j,k}c_jc_k\,
\frac{4\gamma^2}{4\gamma^2+(\lambda_j-\lambda_k)^2}.
$$

This uses one $m$-dimensional eigendecomposition and $O(m^2)$ scalar operations.
Cancellation in this formula and the computation of $a_j,b_j$ need controlled
roundoff for a numerical certificate. The present proof assumes exact recursion;
the diagnostic uses floating point and is not an interval certificate. Finite-
precision recurrence defects and sampling arithmetic need their own error budget;
existing Lanczos finite-precision theory [4] is relevant, not silently assumed away.

## 4. A closed parameterized check, not a new demonstration molecule

For a two-dimensional retained matrix
$T_2=\left(\begin{smallmatrix}a_1&b_1\\b_1&a_2\end{smallmatrix}\right)$,

$$
q_2=\frac{b_1^2}{2[\gamma^2+b_1^2+(a_1-a_2)^2/4]}.
$$

For any even chain with alternating offsets $\delta_i=(-1)^i d$, $d\ne0$, the
first recursion data follow from Note 15's exact moments:

$$
a_1=a_2=0,\quad b_1=|d|,\quad b_2^2=\frac2n\sum_iJ_i^2.
$$

The retained law is exactly the equally weighted pair of Lorentzian lines at
$\pm d$. Hence the certificate gives the all-size sufficient condition

$$
 d_{\rm TV}\!\left(p_{H,\gamma},
 \tfrac12\ell_\gamma(\cdot-d)+\tfrac12\ell_\gamma(\cdot+d)\right)
 \leq \min\left\{1,
 \frac{d^2\sum_iJ_i^2}{2n\gamma^2(\gamma^2+d^2)}\right\}.
$$

The separately available linear certificate and Note 15's one-line bound can
also be used; choose the strongest justified bound, not the most favorable
comparison story. This illustrates an easy-resolution regime uniform in chain
length for bounded couplings. It does NOT say every linewidth is easy, nor that
intermediate $d/J$ must be hard. No measured compound or claimed performance gain
is represented by this example.

## 5. Collective cross terms cannot be replaced by local averages

The normalized correlation of $\sum_i S_i^+$ contains terms
$\operatorname{Tr}[(S_i^+)^\dagger S_j^+(t)]$ for $i\ne j$. At later times these
need not vanish. Our starting vector is the complete collective observable, so
all such terms are retained throughout the recursion.

An exact two-spin negative control is decisive: at zero offsets and nonzero $J$,
the collective law is $\delta_0$. The normalized single-site law, and therefore
the average of the two single-site laws, is

$$
\tfrac12\delta_0+\tfrac14\delta_{J}+\tfrac14\delta_{-J}.
$$

Thus replacing the collective spectrum by a mixture of site spectra changes the
answer, even in this elementary limit. This is a check against an invalid locality
shortcut, not a new physical prediction. The disconnected-component mixture in
Note 15 remains valid; it is a different factorization.

## 6. What building the classical approximation costs

For the open nearest-neighbor chain, any Pauli string in $L^kO$ has support
contained in an interval of length at most $k+1$. Proof: initially every term
occupies one site. A nonzero commutator with a one-site field or adjacent bond
must intersect its support and can extend the enclosing interval by at most one.
Cancellations can leave holes, so connected *nonidentity support* is not assumed.
Linear combinations of earlier Krylov vectors preserve the enclosing-interval bound.

Through the residual at step $m$, the number of possible nonidentity strings is
bounded by

$$
3n+\sum_{\ell=2}^{\min(n,m+1)}9(n-\ell+1)4^{\ell-2}
\leq 3n4^m.
$$

Local term indexing and compact interval strings therefore give a conservative
arithmetic-operation construction cost

$$
C_{\rm rec}=O(n\,\operatorname{poly}(m)4^m),
$$

with comparable string storage (and an additional polynomial factor if all
vectors are retained for reorthogonalization). The finite diagnostic is not an
optimized implementation of this upper bound. Coefficient bit length, conditioning
and numerical certification are additional costs. This is an upper bound for one
classical method, not its lower bound or a bound on all tensor-network methods.

Once the recursion and small eigendecomposition are obtained, ordinary categorical
and Cauchy sampling suffice. For $M$ requested samples, compare

$$
C_C=C_{\rm rec}(n,m)+O(m^3)+M C_{\rm classical\ draw}
$$

against the direct quantum route in Note 15,

$$
C_Q=M[C_{\rm observable/clock\ prep}+C_{\rm controlled\ evolution}(n,T,\epsilon)
+C_{\rm readout}],\qquad T=O(\gamma^{-1}\log(1/\epsilon)).
$$

The last expression is not a hardware time estimate: explicit coefficient access,
Hamiltonian simulation accuracy and output precision count. Neither side is
compared with an unnecessary complete line list. Classical preprocessing can be
amortized over all requested samples; quantum state preparation must be repeated.

Define a **certificate depth** as the first affordable $m$ for which the proven
bound meets the allocated error. This depends on the observable, parameters,
linewidth and tolerance. It is not an intrinsic classical-complexity measure.
If it stays bounded as $n$ grows, this classical method already avoids exponential
spin-count scaling. If it grows, other reductions may still succeed.

The possible quantum benefit is avoiding explicit classical construction of
response-relevant operator combinations while retaining them coherently. That
benefit survives only if the required spectrum really depends on them and all
adequate classical alternatives are charged fairly. Large operator growth or
Lanczos coefficients are not classical lower bounds. The operator-growth
hypothesis [6] is a hypothesis in its stated regimes, not a theorem for these
collective alternating-field chains.

## 7. Keep physical relaxation distinct from the chosen linewidth model

Karabanov et al. [5] analyze state-space restriction using a hierarchy of spin
correlations and explicit assumptions on relaxation. Their discussion supports
classical compression when those assumptions apply and identifies exceptions.
It is a serious predecessor/comparator, not evidence that our criterion is the
first such idea. They use order-dependent relaxation and additional approximations;
we must not replace those by a single Lorentzian convolution and transfer every
bound unchanged. Conversely, real relaxation that suppresses difficult correlations
must not be omitted merely to favor the quantum side. At this stage our conclusion
is for the explicitly stated Hamiltonian-plus-common-linewidth model.

## 8. Decision and next mathematical question

The present result makes the model-level test computable before reconstructing
all microscopic transitions. It does not establish a useful separation. Do not
spin the classical certificate off or make it the new project objective.

**Next:** analyze, for the alternating-offset nearest-neighbor family, whether
observable-space transport reaches growing correlation support on the linewidth
time scale, and whether symmetry, exchange narrowing, a secular approximation,
or a tensor-network representation can still avoid explicitly representing it.
Use the exact uniform-field and resolved two-spin limits as controls. Derive
parameter-dependent statements before requesting a molecule or a large simulation.
A failure of this particular certificate is not permission to claim hardness.
The direct quantum sampler need not learn the classical recursion coefficients.

## 9. Executed checks and source limits

Run with Python 3.10+ and NumPy, without optimization flags:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/spectral_boundary_v1/verify.py
```

The final checker ran twice with identical JSON; -O/-OO refusal was checked.
Three fixed spin models (2, 4 and 6 sites) check 36 binned spectral comparisons,
74 Gauss-moment identities, 15 sparse/dense commutator and support comparisons,
and 108 quadratic resolvent identities. Nine analytic two-mode boundary formulas,
three complex-basis covariance checks, the collective/local-mixture and omitted-
residual negative controls, and four invalid linewidths also pass.

These are double-precision mathematical diagnostics, tolerance 2e-9, not exact-
arithmetic or interval certification, experimentally fitted spectra, quantum
hardware or timing comparisons. The continuous-TV theorem follows from the proof,
not the finite bins. The tested models diagnose formulas; they are not performance
workloads. No old verifier was rerun; old code/reports and the local checkpoint
15 are unchanged. No source data or upstream implementation was imported.

Checker SHA256: `ac047915a477741754ee0182e2bb11e8229e2c17fd97b401e16d2e94f715187c`.
Report SHA256: `36a73a8bd64a4092be01b03e2477611d8c3476f2116e0a89e6e35438aae2da29`.

Primary sources checked 28 September 2026; no exhaustive priority audit:

[1] Sels et al., Quantum approximate Bayesian computation for NMR model inference,
Nature Machine Intelligence 2 (2020). Primary abstract/model context rechecked;
Notes 14-15 contain the earlier model inspection. https://arxiv.org/abs/1910.14221

[2] Sels and Demler, Quantum generative model for sampling many-body spectral
functions, PRB 103, 014301 (2021). Primary abstract rechecked; direct quantum sampler
precedent, not a new result here. https://arxiv.org/abs/1910.14213

[3] Haydock and Te, Accuracy of the recursion method, PRB 49, 10845 (1994).
Publisher indexed abstract inspected; boundary-insensitivity and spectral-error
precedent. Full text was not available. https://doi.org/10.1103/PhysRevB.49.10845

[4] Chen, Greenbaum, Musco and Musco, Error bounds for Lanczos-based matrix function
approximation, SIAM J. Matrix Anal. Appl. 43, 787-811 (2022), arXiv:2106.09806v2.
Lanczos relation, Lemma 2.2 and Section 6's residual-square quadratic-form identity
inspected from PDF text. This directly precedes the certificate's proof method.
https://arxiv.org/abs/2106.09806

[5] Karabanov et al., On the accuracy of the state space restriction approximation
for spin dynamics simulations, arXiv:1104.3866. Sections 2-4, especially relaxation
assumptions, correlation hierarchy and scope, inspected from PDF text. Numerical
plots were not used for new claims. https://arxiv.org/abs/1104.3866

[6] Parker et al., A Universal Operator Growth Hypothesis, PRX 9, 041017 (2019).
Primary abstract inspected; growth hypothesis is not a proof of algorithmic
hardness or a result for every observable. https://arxiv.org/abs/1812.08657

HTML retrieval failed for [4-6]; PDF text was used for [4,5]. Four web screenshot
attempts on the relevant methods pages failed; no plot/table values were extracted
or inferred. Priorities and unseen finite-precision details remain unassessed.
Only Quantum-Assisted-Algorithm-Discovery may be modified. Climate exploration
remains open, Manthan paused, battery/operator candidates parked, the two spin-offs
independent, and earlier closed comparisons unchanged. No new repository, external
contact, paid/unattended work, manuscript revival, release or merge is authorized.
