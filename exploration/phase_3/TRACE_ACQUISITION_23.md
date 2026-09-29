# Trace acquisition 23: price scalar spectral information with classical typicality

29 September 2026. Baseline: `389f9d81014be10fa3a0b6d0c8c44fd91ea39e01`.
Branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Outcome:** an established classical random-vector method closes one missing
acquisition budget in Note 22. For the specified collective high-temperature
response, its mean-square correlation error is at most 2/(R 2^k), at every time,
for R independent global random-phase probes. Combining this with the existing
readout bound gives an explicit high-probability spectral sampler. The algorithm
propagates two ordinary 2^k-component vectors per probe, not a 4^k-component
operator, and does not require a bound on tensor bond dimension. Propagation is
still costly; this is not a polynomial-in-k classical algorithm or a demonstrated
quantum advantage. Random-phase trace estimation and dynamical typicality are
prior work [1-3], not a new discovery here.

One ten-spin matrix-free control actually acquires the 255 scalar correlations
and checks the resulting finite-clock bin law. It is an independent mathematical
implementation, not an upstream NMR run, large-system feasibility study, or
performance comparison. Direct quantum samples remain the alternative; they do
not have to become a classical program. No new repository or spin-off is needed.

## 1. Same block, observable, linewidth, and consumer

For a k-spin open block retain

$$
H=\sum_{i=1}^k(-1)^i dS_i^z+
J\sum_{i=1}^{k-1}{\bf S}_i\cdot{\bf S}_{i+1},
\qquad O=\sum_i S_i^+,\qquad D=2^k.
$$

The block coefficients are supplied classical inputs, with d/J of order one in
the comparison. The model is the same high-temperature scalar-coupled response
anchored in [4]; it is not an arbitrary signed pulse signal, a finite-temperature
state, a model of every real molecule, or a new experimental prediction. Any
additional physical relaxation must be included under its own assumptions.

With U(t)=exp(-itH), cyclicity of the trace gives

$$
C(t)=\frac{\operatorname{Tr}[O^\dagger U(t)O U(t)^\dagger]}{Dk/2}
=\frac1D\operatorname{Tr}B(t),\qquad
B(t)=\frac2k U(t)^\dagger O^\dagger U(t)O.
$$

C is the characteristic function of the same normalized positive raising-response
spectral measure used in Notes 15-22. It need not be real. Convolve that measure
with Cauchy(gamma) and return the original prescribed bin labels, including
overflow, at the allocated TV accuracy. The uniform detector normalization Dk/2
is known exactly; no random estimate of it is necessary. C(0)=1 is imposed exactly.

The spatial-window rule of Note 21 remains available to both sides. The present
bounds concern a selected block, not a proof that a chosen small block already
represents an arbitrarily long chain. Its spatial error is a separate term.

## 2. A time-uniform variance bound for the actual observable

Draw independent phases z_x uniformly from {1,i,-1,-i}, one for EACH of the D
computational-basis labels, and define the normalized vector

$$
|r\rangle=D^{-1/2}\sum_{x=0}^{D-1}z_x|x\rangle.
$$

This is a global random-phase vector, not a tensor product of k random one-spin
vectors. Classical generation and storage take O(D) entries; it is not granted
as a cheap quantum state-preparation oracle.

The random trace estimate is

$$
\widehat C_r(t)=\langle r|B(t)|r\rangle.
$$

Since E[z_x]=E[z_x^2]=0 and E[|z_x|^2]=E[|z_x|^4]=1, direct phase averaging yields

$$
\mathbb E\widehat C_r(t)=C(t),\qquad
\mathbb E|\widehat C_r(t)-C(t)|^2
=\frac1{D^2}\sum_{x\ne y}|B(t)_{xy}|^2.
$$

This standard random-phase trace identity applies to non-Hermitian B as well as
Hermitian matrices [1]. Discrete fourth-root phases satisfy the same fourth-order
conditions needed here as the continuous phases in that reference. No energy
basis is supplied and no thermalization assumption is used.

For the collective raising observable,

$$
\operatorname{Tr}(O^\dagger O)=\frac{Dk}{2},\qquad
\operatorname{Tr}[(O^\dagger O)^2]=\frac{Dk^2}{2}.
$$

To verify the fourth trace, write O^dagger O as the sum of k occupation
projectors and ordered two-site raising/lowering terms. The normalized trace of
the square of the projector sum is (k^2+k)/4; the paired off-diagonal terms
contribute k(k-1)/4. Cross terms vanish. The sum is k^2/2.

Set M=OO^dagger. Hilbert-Schmidt Cauchy-Schwarz gives

$$
\|B(t)\|_F^2=\frac4{k^2}\operatorname{Tr}[U(t)^\dagger M U(t)M]
\leq\frac4{k^2}\operatorname{Tr}(M^2)=2D.
$$

For an average of R independent probe vectors, therefore,

$$
\boxed{\mathbb E|\widehat C_R(t)-C(t)|^2\leq\frac{2}{RD}.}
$$

This is uniform in t and independent of spectral gaps, interaction strength,
operator entanglement, and whether the dynamics is integrable. The dynamics still
has to be computed accurately. The proof is a specialization of established
random-vector typicality to our normalized observable, not a new typicality theory.

The SAME probe batch may be reused at every requested time. The resulting errors
are generally correlated; they are not independent trajectory samples. The next
bound requires no independence across times.

### Two important non-substitutions

Do not divide the estimator by the probe's own random O^dagger O expectation.
That changes it to a ratio estimator and invalidates the unbiased calculation
above. Use the known k/2 normalization and set the known zero-lag value to one.

Do not replace the global phases by independent one-spin phases and retain the
same variance promise. For the product of equatorial one-spin states with phases
z_i, the zero-time normalized trace estimate is

$$
\frac12+\frac{|\sum_{i=1}^k z_i|^2}{2k},
\qquad \operatorname{Var}=\frac{k-1}{4k}.
$$

That tends to 1/4, not to zero as 2^-k. This is an ensemble counterexample, not an
output-error claim: C(0) is known and fixed in the actual algorithm. It shows why
cheap product-state preparation is not equivalent to global typicality. The
existing quantum observable-state sampler requires neither type of random probe.

## 3. Turn the variance into a guarantee for the full spectral readout

Use the clock variables of Note 22, not a new reconstruction model:

$$
a_h=e^{-\gamma\tau h}
\frac{1-e^{-2\gamma\tau(N-h)}}{1-e^{-2\gamma\tau N}},
\qquad A_2=\sum_{h=1}^{N-1}a_h^2
\leq\frac1{e^{2\gamma\tau}-1}.
$$

Substitute the acquired Chat_h into the existing Fourier bin calculation. Keep
C_0=1, integrate over actual bin preimages, and apply the positive-part
normalization whose error was proved in Note 22. Conditional on a batch of probes,
its error from the exact finite-clock bin law is bounded by

$$
E_R=\sqrt{2\sum_{h=1}^{N-1}a_h^2|\widehat C_R(h\tau)-C(h\tau)|^2}.
$$

Time correlations do not obstruct the following calculation: expectation of a
sum is a sum of expectations, so

$$
\mathbb E E_R^2\leq\frac{4A_2}{RD},\qquad
\mathbb E E_R\leq2\sqrt{\frac{A_2}{RD}}.
$$

For 0<beta<1 and statistical readout allocation epsilon_stat>0, Markov's inequality
on E_R^2 supplies

$$
\boxed{R\geq\max\left\{1,
\left\lceil\frac{4A_2}{2^k\,\beta\,\epsilon_{\rm stat}^2}\right\rceil\right\}}
$$

as a sufficient probe budget for E_R<=epsilon_stat with probability at least
1-beta. This avoids pretending that all lag estimates are independent and avoids
a separate union bound for every time point. It is conservative; concentration
or variance-aware choices may improve it. No optimality is claimed.

Deterministic correlation errors e_h,num add by the weighted triangle inequality:
E_num=sqrt(2 sum a_h^2 e_h,num^2). On the stated success event the per-draw physical
bin error is at most

$$
\epsilon_{\rm clock}+\epsilon_{\rm wrap}+\epsilon_{\rm stat}
+E_{\rm num}+\epsilon_{\rm bin/random\ arithmetic}.
$$

Here epsilon_clock=exp(-gamma N tau)/(1-exp(-gamma N tau)). With Omega=pi/tau,
Note 22's bound epsilon_wrap<=4d^2/Omega^2+(2/pi)atan(2gamma/Omega) is retained.
No spectral tails are deleted or a finite clock called an exact physical line.
For the full-chain mixture, add the allocated spatial error from Note 21.

The probability statement concerns the ONCE acquired classical sampling table.
Given that table, repeated draws are independent from its approximate law.
Unconditionally they share table error. A per-draw TV bound is not automatically
a joint M-draw TV bound; a safe bound is beta+M epsilon_conditional, capped at one.
For adaptive parameter fitting, independent new probes or an appropriate uniform
failure budget are needed. A theorem for a fixed Hamiltonian does not certify
an arbitrary adaptively selected collection of fits.

### A numerical accuracy budget, not a runtime claim

Keep Note 22's d=J, gamma=J/4, tau=0.1/J, N=256. Then A_2 is about 19.502864.
Take epsilon_stat=0.0125 and beta=0.01. Sufficient probe counts are:

| Block spins k | Entries per ordinary state vector | Sufficient R |
|---|---:|---:|
| 12 | 4,096 | 12,190 |
| 20 | 1,048,576 | 48 |
| 26 | 67,108,864 | 1 |

These rows are evaluations of the bound, NOT executed simulations, minimum
necessary counts, evidence of adequate spatial-window size, or hardware estimates.
The first two nonstatistical terms total about 0.015848433; adding epsilon_stat
gives 0.028348433 before deterministic arithmetic and any spatial approximation.

The number of statistical probes can decrease as the Hilbert space grows. Each
probe, however, contains 2^k amplitudes and requires full-time propagation. A single
probe at k=26 does not mean a single cheap scalar operation or a single quantum shot.

## 4. An explicit acquisition algorithm, with no unknown tensor-rank assumption

For each probe form and evolve two ordinary Hilbert-space vectors:

$$
|\psi_r(t)\rangle=U(t)|r\rangle,\qquad
|\phi_r(t)\rangle=U(t)O|r\rangle.
$$

Then compute

$$
\widehat C_r(t)=\frac2k
\langle\psi_r(t)|O^\dagger|\phi_r(t)\rangle.
$$

This is the standard two-vector dynamical-typicality architecture [2,3], here with
a known infinite-temperature normalization and a non-Hermitian raising observable.
The producer never stores an evolved 4^k-entry operator or diagonalizes H.
The local spin Hamiltonian and O act on a vector in O(k2^k) arithmetic operations;
bit-indexing can generate the sparse action without storing a dense Hamiltonian.
Probe initialization costs O(2^k) random phases and vector entries. Working vectors
can be processed sequentially, using O(2^k+N+B) words plus local indexing/workspace,
where B is the number of output bins. Storing an explicit sparse matrix instead
may take O(k2^k) words; no dense operator is necessary in either case.

Unlike Note 22's operator-vector half-time contraction, this simple two-pure-state
implementation evolves to the full largest lag T=(N-1)tau. It is a different
tradeoff: smaller state representation, not an asserted combination of all
advantages of both methods. Tensor implementations, symmetry blocks, optimized
Krylov/Chebyshev propagators, and shared-parameter reuse remain available too.

### One conservative arithmetic budget

Let W>=||H||, for example W=k|d|/2+3(k-1)|J|/4. Approximate a step U(tau) by
its degree-q exponential Taylor polynomial. A sufficient exact-arithmetic
operator error is

$$
\eta_{\rm step}\leq e^{W\tau}\frac{(W\tau)^{q+1}}{(q+1)!}.
$$

For r<=N-1 repeated steps, telescoping gives
||U_tilde^r-U^r|| <= r eta_step exp(r eta_step). Thus eta_step<=delta_U/(2N),
0<delta_U<=1, suffices for error <=delta_U at every lag. One may choose
q=O(W tau+log(N/delta_U)); this is an upper-bound construction, not an optimized
integrator or a bound on floating-point roundoff.

Using ||O||<=k and the two propagated vectors, the per-lag scalar error from
||U_tilde(t)-U(t)||<=delta_U is at most

$$
\frac2k\|O\|^2(2\delta_U+\delta_U^2)\leq6k\delta_U.
$$

Therefore E_num<=6k delta_U sqrt(2A_2). Coefficient errors, roundoff, bin integration,
normalization and random-bit generation still need budgets; an ideal Taylor
remainder is not an interval certificate for the code.

For R probes, a sufficient arithmetic upper bound is

$$
\boxed{C_{\rm acquire}=O\big(R\,N\,k\,2^k(q+1)\big).}
$$

The required N-1 contractions are included. Substituting the probe budget gives

$$
C_{\rm acquire}=O\left[
Nk(q+1)\left(2^k+\frac{A_2}{\beta\epsilon_{\rm stat}^2}\right)\right],
$$

up to an absolute numerical factor and the stated precision costs. At finite
precision this is arithmetic, not a gate, memory-bandwidth, power, or wall-clock
estimate. With B bins, add O(BN) readout preprocessing and the costs of M later
classical draws. More efficient methods may improve any of these upper bounds.

This removes the previously unspecified C_acquire for ONE serious classical
competitor. It does not show that the competitor is optimal or that 2^k work is
necessary. Conversely, a quantum spectral sampler's polynomial-sized register
does not establish a useful total-cost separation against all classical routes.

## 5. What the translation/linked-cluster screen did and did not establish

The source search found an existing combination of dynamical typicality and
numerical linked clusters [3]. In one dimension the truncated bulk correlation
is a difference of the two largest extensive cluster contributions. This is a
strong comparator, not a new idea to claim. For a two-spin unit cell, write
X_m=m C_(2m); its formal linked-cluster partial sum is X_m-X_(m-1). This is not
identical to the finite block law requested here without an additional tail or
finite-size error argument.

Cancellation of physical boundary terms need not cancel statistical noise. With
independent R-probe calculations of both clusters, the variance of that difference
is bounded by

$$
\frac2R\left[\frac{m^2}{4^m}+\frac{(m-1)^2}{4^{m-1}}\right].
$$

Its signed coefficients cannot be assigned the convex-mixture error bound of
Note 21. Shared probes could alter covariance, but their coupling and accuracy
need an explicit analysis. Nor does a signed extrapolation automatically define
a positive spectral sampler. Its possible use through Note 22 remains legitimate
once all errors are controlled. No linked-cluster convergence theorem for this
alternating-field response was established in this round. Do not substitute
large-system results for a different observable or Hamiltonian.

The completed calculation therefore prices the pure-state acquisition component
first, rather than adding a speculative linked-cluster or tensor-rank theorem.

## 6. One actually executed acquisition control

The checker independently implements the two-vector producer at k=10, d=J=1,
tau=0.1, N=256, and R=8 fixed pseudorandom Z4 probes (NumPy PCG64 seed 230929).
It uses 16 vectors in parallel for this control; the analytical memory bound can
instead process probes sequentially. The degree-16 step polynomial requires
4,080 batched Hamiltonian actions through time 25.5. This is an operation count,
not a runtime result or a full statistical feasibility run.

The producer does not use an eigenbasis. For validation only, a separate exact-
sector diagonalization of this small model supplies reference correlations and
reference finite-clock probabilities. The original fine-bin contract is retained:
width 0.01 over [-50,50], plus two overflow bins. The wrapped-clock calculation
uses the appropriate bin preimages, with zero clock mass outside its principal
range. Its comparison to the UNWRAPPED target still needs the stated wrap error.

The fixed-seed control has maximum scalar error about 0.026568, weighted scalar
error 0.057745, and bin TV about 0.006989 against the exact finite-clock law.
The output error is smaller than the sufficient weighted bound and does not
require every lag to meet the earlier 0.002 uniform target. This is one numerical
control, not an empirical confidence interval or a scaling law. R=8 at k=10 does
NOT meet the 99%-success budget in Section 3; do not label it such. The relative
propagated-vector discrepancy against the independent diagonal reference is about
2.6e-14. Floating reference data do not independently certify a continuous-TV claim.

Other checks exhaust all 64 global-phase classes for a two-spin variance identity
at three times, verify the collective fourth trace, and exhaust 256 four-spin
product-phase choices for the invalid-ensemble control. These are distinct tests
of the derivation, not additional demonstration workloads. Six invalid inputs and
-O/-OO execution are rejected.

## 7. Decision and next discriminating comparison

Random phase trace acquisition is a mandatory classical comparator. The bottleneck
cannot be justified merely by a 4^k operator representation or the number of
individually required correlations. On the other hand, the exponential number of
amplitudes in a pure-state propagation remains charged, and an actual tensor or
symmetry reduction can improve it. No all-classical lower bound is obtained.

Compare, at the SAME resolved output and requested number of samples, the minimum
of the justified classical routes: typicality with full-time pure-state propagation,
half-time operator tensors, certified recursion, exact easy limits, and any valid
translation reduction. The direct quantum route does not need to construct the
classical correlation table; its local-block state/clock preparation, controlled
Hamiltonian evolution, parameter access and repeated shots remain priced in
Notes 15 and 21. Large classical setup is reusable. A crossing of two nonoptimal
upper bounds is not proof of quantum advantage.

**Next bounded task:** decide whether this model family exposes a credible
resolution/sample-count regime AFTER this stronger comparator. Make one explicit
symbolic comparison, including typicality and the possibility of classical trace
or tensor compression. Do not keep adding general-purpose classical readout
certificates. A response-sensitive obstruction or an economical classical
construction is informative, but do not call ordinary operator entanglement a
hardness proof. If no structural reason survives, broaden the mechanism comparison
rather than manufacture a difficult molecule or another small-size benchmark.
No new repository, manuscript or classical spin-off follows from this checkpoint.

## 8. Reproduction, scope, and sources

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/trace_acquisition_v1/verify.py
```

Python 3.10+ and NumPy. The final checker ran twice with identical JSON. It writes
no files and imports no upstream implementation. All dynamic checks use complex128;
no interval or full roundoff certificate is claimed. General probability and
arithmetic bounds follow from the written proof, not the sampled batch.

Checker SHA256: `debcd383b7d12d4d4de89beda35281cf2e272b9bc9a28037a8d8ffa9bfe92254`.
Report SHA256: `f8705f0d0f1ec177ffc0c4c7efdfa036071bbf71f6998da429849c4d11e7e31e`.

No quantum circuit, hardware, native NMR package, experimental spectrum, physical
relaxation simulation, large-block run, performance benchmark, or scientific
advantage was established. No prior verifier was rerun; historical sources,
proofs, reports, data and third-party rights remain unchanged.

Primary sources checked 29 September 2026. This is a bounded predecessor screen,
not an exhaustive novelty audit. PDF text of [1-3] was read for the trace identities,
two-vector method, and linked-cluster comparison. Three requested PDF-page
screenshots failed; no figure/table number is used as a new numerical benchmark.
The NMR and direct-quantum sources were checked at primary abstract/model-scope
level. The variance-to-readout specialization is internally derived; its building
blocks are standard, and no publication-priority claim is made.

[1] T. Iitaka and T. Ebisuzaki, Random phase vector for calculating the trace of a
large matrix (2004), arXiv:cond-mat/0401202v2, especially Eqs. (16) and (22).
https://arxiv.org/abs/cond-mat/0401202

[2] R. Steinigeweg, J. Gemmer and W. Brenig, Spin-current autocorrelations from
single pure-state propagation, PRL 112, 120601 (2014), arXiv:1312.5319. This is
CLASSICAL simulation of quantum response, not a quantum-computer algorithm.
https://arxiv.org/abs/1312.5319

[3] J. Richter and R. Steinigeweg, Combining Dynamical Quantum Typicality and
Numerical Linked Cluster Expansions, PRB 99, 094419 (2019), arXiv:1901.02909.
Sections III.B-C, two-state estimator and Eq. (10) inspected. Their current observable
and model are not silently identified with our collective raising spectrum.
https://arxiv.org/abs/1901.02909

[4] D. Sels et al., Quantum approximate Bayesian computation for NMR model inference,
Nature Machine Intelligence 2, 396-402 (2020), arXiv:1910.14221.
https://arxiv.org/abs/1910.14221

[5] D. Sels and E. Demler, Quantum generative model for sampling many-body spectral
functions, PRB 103, 014301 (2021), arXiv:1910.14213. Direct spectral sampling precedent.
https://arxiv.org/abs/1910.14213

Climate/dynamics remain open; Manthan stays paused; battery/operator routes remain
parked; both classical spin-offs independent; Phase-2 Note 27 closed. Only the
parent Quantum-Assisted-Algorithm-Discovery repository may be modified. No outside
contact, paid/unattended work, submission, release, merge, or administration change.
