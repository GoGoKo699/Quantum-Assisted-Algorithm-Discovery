# Response readout 22: compare the information in the spectrum, not the full operator

29 September 2026. Baseline: `fdc88f1c59d743394001e28edf7b97a5270dba9c`.
Branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Outcome:** the local-block comparison now has both a necessary output-level test
and a constructive classical readout criterion. A rigorously different return
amplitude certifies a spectral error; conversely, finitely many sufficiently
accurate scalar return amplitudes produce a positive bin sampler with a quantified
error. A classical tensor method can acquire those scalars using half-time
evolution. Large operator rank alone is not evidence that the sampled spectrum
is hard. No quantum-classical separation, new primitive, or application speedup
is established. The existing repository remains the appropriate workspace.

The question is still useful direct quantum sampling. The classical reconstruction
below is a competitor, not a requirement to turn quantum output into a program.

## 1. Same model, region, linewidth and output

Use the scalar-coupled high-temperature spin model from Notes 15 and 21, motivated
by the NMR response/inference setting [1,2]. A selected open block of k spins has

$$
H=\sum_{i=1}^k(-1)^i dS_i^z+
 J\sum_{i=1}^{k-1}{\bf S}_i\cdot{\bf S}_{i+1},\qquad
O=\sum_i S_i^+,\quad o=O/\|O\|_F,\quad L=[H,\cdot].
$$

The main regime here is d/J of order one, not a weak-offset expansion. Scalar
parameters are supplied in angular-frequency units. The chain is a structural
model, not a claimed measured compound. The target is the normalized spectral
law mu of L in o, convolved with the SAME Cauchy(gamma) kernel and assigned to the
agreed bins, including overflow. It is not absolute intensity or arbitrary pulse
or finite-temperature response. Physical relaxation beyond this common-linewidth
model needs its own treatment; [6] cannot be transferred without its assumptions.

Let

$$
u(t)=e^{-itL}o,\qquad C(t)=\langle o,u(t)\rangle
=\int e^{-it\omega}\,\mu(d\omega),\qquad s^2=\|Lo\|^2=d^2.
$$

The last equality holds for every such block, including an odd end block with a
nonzero carrier. Do not remove that carrier without restoring its spectral shift.
Note 21's positive window mixture remains valid. If every block sampler has error
at most epsilon_block, the chain error is at most epsilon_loc+epsilon_block by
convexity; mixture weights and endpoint rules remain unchanged.

## 2. A necessary test in the actual output, not operator norm

For two candidate spectral measures mu, nu and their corresponding C_mu,C_nu,

$$
\boxed{d_{\rm TV}(\mu*\ell_\gamma,\nu*\ell_\gamma)
\geq\tfrac12 e^{-\gamma|t|}|C_\mu(t)-C_\nu(t)|.}
$$

Proof: the Fourier transform of ell_gamma is exp(-gamma|t|), and integration
against exp(-it omega), whose modulus is one, is bounded by twice TV. Any single
time is a valid witness. This is elementary characteristic-function duality,
not a new abstract lower-bound technique. A large difference between evolved
operator vectors need NOT give a large difference of these scalar returns.

For fixed bins a continuous-TV witness needs an additional step. Suppose the
interior bins partition [-Omega,Omega] with widths at most Delta. Assign each
interior bin the phase exp(-it times its midpoint), and assign zero to overflow
bins. This is a bounded test on the actual bin labels. If the two broadened laws
have outside masses q_mu and q_nu, then

$$
d_{\rm TV}(\mu_{\rm bins},\nu_{\rm bins})\geq
\tfrac12\left[e^{-\gamma|t|}|C_\mu-C_\nu|
-|t|\Delta-(q_\mu+q_\nu)\right].
$$

The phase error inside each bin is at most |t|Delta/2 per law. The outside error
is at most its probability because the assigned score there is zero. The checker
uses the weaker subtraction 2(q_mu+q_nu) inside the brackets, so its recorded
numbers remain conservative. A negative right side supplies no information.
Coarsening arbitrary bins can erase a continuous-law witness; it is not silently
assumed harmless for a lower bound.

### One nontrivial block, with exact arithmetic

Take k=6, d=J=1, t=2 and gamma=1/4. Compare full H with (i) on-site terms alone
and (ii) the commuting SzSz secular model. These are two specific classical
approximations, NOT all classical methods. Neither is assumed valid at d/J=1.

Integer commutators with 4H give exact rational unbroadened moments. For P=40,
Taylor's theorem for cos supplies an enclosure

$$
\operatorname{Re} C(t)\in\sum_{j=0}^{P-1}
 \frac{(-1)^jt^{2j}m_{2j}}{(2j)!}
 +[-1,1]\frac{t^{2P}m_{2P}}{(2P)!}.
$$

The moment is computed as ||L^j O||_F^2/||O||_F^2. There is no eigenvalue
rounding in this witness. An odd Taylor polynomial bounds exp(-gamma t) from
below. The real-part difference alone suffices to lower-bound the modulus.

| Approximation | Certified continuous-TV lower bound | Certified bin-TV lower bound |
|---|---:|---:|
| On-site terms alone | >0.155595999563 | >0.137241910729 |
| Commuting SzSz | >0.076683654870 | >0.058101380567 |

The bin control uses width 1/100 in [-50,50] and two overflow bins. Cauchy tail
bounds use support enclosures W=13.5, 6 and 8.5 for full, on-site and secular
models, respectively, and pi>3. These are deliberately declared mathematical
resolution choices, NOT experimentally required tolerances or a hard application.
The report rounds rational lower bounds downward. This six-spin system is easy
to solve classically. The result says only that interactions change the requested
output appreciably here: the easiest independent/secular surrogates do not meet
5% TV for the declared bins. It does not imply growing-chain hardness.

## 3. The same clock law has a scalar classical reconstruction

Recall Note 15's geometric clock. Choose tau>0, N>=2, r=exp(-gamma tau), and
normalized clock amplitudes c_j proportional to r^j for 0<=j<N. Put

$$
a_h=\sum_{j=0}^{N-1-h}c_{j+h}c_j
=r^h\frac{1-r^{2(N-h)}}{1-r^{2N}},\qquad 1\leq h<N.
$$

The positive phase density of that finite, dithered quantum measurement is exactly

$$
q_N(\phi)=\frac1{2\pi}\left[1+2\operatorname{Re}
\sum_{h=1}^{N-1}a_h C(h\tau)e^{ih\phi}\right].
$$

Proof: expand the squared clock amplitude for each spectral frequency and average
over mu. Each lag h has clock overlap a_h. This is an equivalent description of
the EXISTING quantum measurement, not a new quantum sampler or a requirement that
the quantum device estimate C separately. Its classical side needs only N-1
complex scalars, not a list of all lines, eigenstates or Pauli strings.

The finite-clock error from the wrapped Cauchy law is at most

$$
\epsilon_{\rm clock}=e^{-\gamma N\tau}/(1-e^{-\gamma N\tau}).
$$

Converting phase to a frequency in [-Omega,Omega), Omega=pi/tau, can be bounded
using the observable's second moment rather than an extensive support bound:

$$
\epsilon_{\rm wrap}\leq
\frac{4s^2}{\Omega^2}+\frac2\pi\arctan\frac{2\gamma}{\Omega}.
$$

Indeed, for X~mu and independent Z~Cauchy(gamma), split |X+Z|>Omega into
|X|>Omega/2 or |Z|>Omega/2. Wrapped and unwrapped values agree otherwise.
This permits small probability outside the principal range; it does not pretend
that every microscopic gap is unaliased. The unwrapped target and overflow bins
are retained. The moment belongs to mu, not the heavy-tailed broadened law.

### Approximate correlations, positivity, and the full error budget

Suppose |Chat_h-C(h tau)|<=e_h, and fix C_0=1 exactly. Substitute Chat into the
Fourier polynomial and integrate it over the actual output-bin preimages. The raw
real bin masses x_b sum to one but may be negative. Define the explicit sampler

$$
\widehat p_b=\frac{\max(x_b,0)}{\sum_c\max(x_c,0)}.
$$

Its output is always a probability distribution. The effect of this repair is
bounded, not assumed negligible. Orthogonality of Fourier modes gives

$$
\|q_N-\widehat q_{\rm raw}\|_{L^1}
\leq \left(2\sum_{h=1}^{N-1}a_h^2e_h^2\right)^{1/2}.
$$

For any real signed bin vector x summing to one and any target probability p,
positive-part normalization satisfies TV(p,repair(x))<=||p-x||_1. To see this,
let z be the negative mass of x. Then ||repair(x)-x||_1=2z, while
2z<=||p-x||_1; triangle inequality proves the claim. Bin integration contracts
L1. Therefore a sufficient complete per-draw bound is

$$
\boxed{\epsilon_{\rm block}\leq
\epsilon_{\rm clock}+\epsilon_{\rm wrap}
+\sqrt{2\sum_{h=1}^{N-1}a_h^2 e_h^2}+\epsilon_{\rm arithmetic}.}
$$

Arithmetic includes bin integration, normalization, finite random-bit sampling
and output representation. If C values have only probabilistic error guarantees,
the failure event must also be charged. No independence between their errors is
needed for the deterministic bound. A bad unvalidated correlation sequence is
not made accurate merely by removing negative bins.

For a uniform e_h<=sigma, a_h<=r^h gives the convenient sufficient readout term
sigma sqrt(2/(exp(2 gamma tau)-1)). Correlation precision thus cannot be held fixed
without checking what happens as gamma decreases. Full-table preprocessing is
not forced on every classical alternative; direct fitting or sample generation
from another representation may do better.

### A concrete sufficient target at d=J

In units J=1, set gamma=1/4, tau=0.1, N=256 and sigma=0.002. Then

| Contribution | Bound |
|---|---:|
| Finite clock | 0.00166433 |
| Unwrapping, using s^2=1 | 0.01418412 |
| Approximate correlations, using actual a_h | 0.01249092 |
| Sum before arithmetic | <0.02834 |

Thus 255 accurately acquired correlations suffice for this per-block bin-sampling
accuracy, for ANY block size in the stated family. The numbers are a conditional
accuracy target, not evidence that a cheap classical method has acquired these
values for large blocks. The numerical diagnostic perturbs exact six-spin values
to check the bound; it is not a tensor-network simulation or timing result.
Note 21's spatial error must still be added for the full-chain mixture.

## 4. Strong classical acquisition uses half-time evolution

Existing finite-temperature tensor methods exploit time translation [3,4]. In
our notation,

$$
C(t)=\langle u(-t/2),u(t/2)\rangle.
$$

Moreover H, L and the initial raising vector are real in the fixed computational
vectorization. Thus u(-s)=u(s)* and

$$
\boxed{C(2s)=u(s)^T u(s).}
$$

The final contraction is BILINEAR, not the conjugated norm (which is always one).
One forward half-time operator trajectory suffices in this real model. This is a
specialization of prior time-splitting methods, not a new doubling algorithm.
A complex-Hamiltonian extension must keep both appropriate trajectories.

If a normalized tensor approximation utilde(s) has vector error delta(s), the
bilinear contraction error is at most 2delta(s). Insert e_h<=2delta(h tau/2) in
the readout certificate. The example above asks for absolute vector error 0.001
only as a SUFFICIENT route to 0.002 correlation error. Scalar contractions may be
accurate with much worse global vector approximations. Conversely, large Schmidt
rank or a failed tensor truncation cannot replace an output-error witness.

For a unitary-step tensor algorithm, errors can be charged by telescoping local
simulation and truncation errors. Normalizing a Schmidt truncation with discarded
squared norm w changes its input unit vector by sqrt(2-2sqrt(1-w))<=sqrt(2w).
Sum such vector errors, together with evolution errors; do not sum the w values
and silently treat that as a global amplitude-error guarantee. This is a sufficient
bookkeeping route, not an optimized tensor implementation or a claim of cheap rank.

If max bond dimension chi is adequate over the half-time interval and Lstep local
update layers are required, one usual fixed-local-dimension upper budget is
O(k Lstep chi^3) for the evolution, plus O(N k chi^3) for scalar contractions and
O(B N) scalar bin integration for B bins. Precomputing a cumulative distribution
uses O(B) storage and gives O(log B) comparisons per later draw. Precision,
certification and random-bit costs remain explicit. Optimal tensor contraction,
restricted-state [6], recursion and direct resolvent [5] methods may improve this
upper bound. Neither chi nor Lstep has been bounded in the hard regime here.

## 5. What the quantum comparison must now beat

For M requested samples from the selected block or templates, compare

$$
C_C=C_{\rm acquire}(k,N,\{e_h\})+O(BN)+M C_{\rm draw},
$$

with Note 15/21's direct local quantum sampling, schematically

$$
C_Q=M[C_{\rm prep}+\widetilde O(1+\alpha_B/\gamma)C_{\rm block}
+C_{\rm clock/readout}],\quad
\alpha_B\leq k|d|+3(k-1)J/2.
$$

C_block denotes actual coefficient-access/block-encoding work, not a free oracle.
No claim of optimality is made for that quantum route. Its relevant distinction is
that it need not classically construct the return amplitudes or their tensor
representation. Its output remains direct samples. The classical setup can be
reused across M; spatial template symmetry and parameter changes must be allocated
consistently. A crossing computed from one classical upper bound does not establish
a best-classical speedup. M and the requested bin/output task are real parameters,
not a free asymptotic afterthought. Shared preprocessing error affects the law of
all draws; a per-draw TV bound is not automatically a joint-TV bound for M draws.

**Decision:** simple interaction-dropping is inadequate in the explicit intermediate
block, but high many-body complexity has not yet been shown necessary for accurate
return amplitudes. The next bounded task is the COST of these response-relevant
scalar contractions, with one controlled operator/tensor or recurrence comparison
in the same d/J~1 regime. Do not add another general output-reconstruction framework,
more six-spin demonstrations, or a molecule/data dependency. A justified compression
would be a classical baseline; an output-sensitive obstruction to one representation
would need to be distinguished from an all-classical lower bound. No third spin-off
or new repository is warranted.

## 6. Execution and attribution

`python experiments/response_readout_v1/verify.py` uses NumPy and the standard library.
It checks one six-spin model, not a size census. Exact Python integers/Fractions
produce moments through order 80 for full, on-site and secular models and rigorous
Taylor enclosures; all reported witness lower bounds are rounded down. Independent
complex128 eigendecomposition checks the scalar result, four half-time identities,
two finite-clock reconstructions, ten direct-kernel/Fourier identities, perturbation
bounds and a negative-probability control. Two rational signed-bin controls check
the repair inequality. Six invalid inputs and -O/-OO execution are rejected.

The final checker ran twice with identical JSON under one BLAS thread. Its source
and report hashes accompany the checkpoint. Floating-point Fourier controls are
not interval certificates; the exact-rational witnesses and general analytic
proofs are distinguished from them. No tensor algorithm, native NMR package,
quantum circuit, experimental spectrum, noise model, performance benchmark or
large-system scaling run occurred. No prior verifier was rerun. No upstream
implementation, data, or weights were imported. Earlier evidence remains intact.

Sources checked 29 September 2026. Primary abstracts/metadata were inspected for
precedent and model scope, not full proof/benchmark reproduction. No PDF was
analyzed or figure digitized in this round. Broad discovery searches also surfaced
unrelated thermal/ground-state examples; they are not used as this chain's baseline.
The general facts (Fourier readout, characteristic-function duality, time splitting
and tensor truncation) are established methods. Priority for this particular
combined certificate has not been audited exhaustively, and no novelty is claimed.

[1] Sels et al., Quantum approximate Bayesian computation for NMR model inference,
Nature Machine Intelligence 2 (2020). Model and inference precedent.
https://arxiv.org/abs/1910.14221

[2] Sels and Demler, Quantum generative model for sampling many-body spectral
functions, Physical Review B 103, 014301 (2021). Direct spectral sampling precedent.
https://arxiv.org/abs/1910.14213

[3] Barthel, Precise evaluation of thermal response functions by optimized density
matrix renormalization group schemes, New J. Phys. 15, 073010 (2013).
https://arxiv.org/abs/1301.2246

[4] Kennes and Karrasch, Extending the range of real time density matrix
renormalization group simulations, Comp. Phys. Comm. 200, 37 (2016).
https://arxiv.org/abs/1404.3704

[5] Savostyanov et al., Exact NMR simulation of protein-size spin systems using
tensor train formalism, Physical Review B 90, 085139 (2014). Model-specific direct
linear-system/tensor comparison; not a guarantee for arbitrary blocks here.
https://arxiv.org/abs/1402.4516

[6] Karabanov et al., On the accuracy of the state space restriction approximation
for spin dynamics simulations, J. Chem. Phys. 135, 084106 (2011). Keep its physical
relaxation assumptions distinct from one common linewidth.
https://arxiv.org/abs/1104.3866

Only Quantum-Assisted-Algorithm-Discovery may be modified. Climate/dynamics remain
open; Manthan is paused; battery/operator routes parked; both classical spin-offs
independent; Phase-2 Note 27 closed. Preserve all proofs, fixtures, rights and the
original license. No contact, paid/unattended work, release, merge or admin change.
