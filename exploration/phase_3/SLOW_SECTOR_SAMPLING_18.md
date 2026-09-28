# Slow-sector sampling 18: resolve weak-field structure without assuming short memory

28 September 2026. Starting head: `7da0ca4a8f2f87a5283280f5a8541b17af97b521`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Outcome:** a conditional slow-sector reduction gives a positive spectral sampler
and an explicit continuous-TV error bound. Quantum block encoding can implement
the second-order generator without first enumerating its classical eigenmodes.
At linewidth proportional to the weak-field splitting, its stated query budget
has no inverse weak-field power, but has important inverse-gap and size costs.
This is a comparison with a straightforward direct quantum construction, NOT a
separation from the best classical method. Effective Hamiltonians and quantum
inverse/filtering methods are prior work. No priority or practical advantage is
claimed. No short-memory or arbitrary-size spectral-nondegeneracy theorem is claimed.

## 1. Keep the physical model and output fixed

Use the same even open chain as [Note 17](EXCHANGE_MEMORY_17.md), in angular-frequency
units with hbar=1:

$$
H(d)=H_0+dV,\quad H_0=J\sum_{i=1}^{n-1}\mathbf S_i\cdot\mathbf S_{i+1},
\quad V=\sum_i(-1)^iS_i^z,\quad O=\sum_iS_i^+.
$$

Here J>0, S=sigma/2, o=O/sqrt(n 2^(n-1)), and L_d=[H(d),.]. The target remains
the high-temperature normalized spectral measure in o, convolved with Cauchy
half-width gamma, then assigned to agreed bins. Scalar-coupled spin response has
an independent NMR model/inference motivation [1,2]. The chain is a structural
subfamily, not a newly selected molecule or an experimentally validated workload.
Parameters are supplied; their chemical inference is another problem.

This note studies resolved weak-field structure, including gamma=c d^2/J with
fixed c>0. This is a mathematical resolution regime, not a claim that every
experiment needs such a narrow line. At fixed coarse gamma, earlier simple-line
bounds may already solve the task. All competitors use the same gamma and bins.
Direct spectral samples remain allowed. A classical program is not the output
requirement. The new route supplements direct sampling and memory sampling; it
does not impose short memory or add a bath to the closed spin model.

## 2. Which zero-frequency modes can the alternating field couple?

Let P_E be the spectral projectors of H_0. The orthogonal projector onto the
ENTIRE conserved operator sector is

$$
\Pi X=\sum_E P_E X P_E,\qquad L_0=[H_0,.],\quad D=[V,.].
$$

This Pi is not Note 17's rank-one projector |o><o|. The sector contains all
operators acting inside degenerate energy eigenspaces, not only total spin.
Since O commutes with H_0, Pi o=o. For V_0=sum_E P_E V P_E,

$$
\Pi D\Pi X=[V_0,\Pi X],\qquad \Pi v=[V_0,o],\qquad v=Do.
$$

Thus absence of overlap with the single conserved total-spin mode is insufficient.
The full first-order operator Pi D Pi must be checked or explicitly assumed zero.

For even n, spatial reversal R commutes with H_0 and changes V to -V. If each
energy eigenspace has a single reflection parity, then P_E V P_E=0 and

$$
\Pi D\Pi=0,\qquad \Pi v=0.
$$

**Qualification:** reflection symmetry alone does not prove this. Opposite-parity
states at exactly the same energy can have nonzero matrix elements of V. We have
not proved parity purity for all even uniform chains. Numerical checks at n=2,4,6,8
verify it for those sizes only. A separate degenerate control detects this caveat.
The reduction below assumes Pi D Pi=0; parity purity is one sufficient condition,
not an extra conclusion. If it fails, retain the first-order slow operator rather
than applying a purely second-order model.

## 3. The effective slow generator and its classical meaning

Let L_0^+ be the inverse on nonzero operator frequencies and zero on ker L_0.
Under Pi D Pi=0, define

$$
\boxed{A=-\Pi D L_0^+D\Pi.}
$$

The physical slow generator to second order is d^2 A. A is self-adjoint, acts on
the conserved sector, and can have a nontrivial positive spectral measure in o.
No assumption that its spectrum is one Lorentzian has been made.

This is standard degenerate perturbation/Schrieffer-Wolff structure [3], now applied
to the operator generator and the specified response. It is not a new perturbation
formalism. Here is a useful explicit classical interpretation. Define

$$
H_2=\sum_E\sum_{F\ne E}\frac{P_E V P_F V P_E}{E-F}.
$$

For every X in the conserved sector,

$$
AX=[H_2,X].
$$

To check this, write [V,X]_(EF)=V_(EF)X_F-X_E V_(EF), divide off-diagonal blocks by
E-F, commute with V again, and keep the diagonal energy blocks. The terms involving
X_F cancel. The minus sign in A leaves [H_2,X_E]. This derivation does not require
computing the eigenbasis in the proposed quantum implementation.

If each energy eigenspace is a single irreducible total-spin multiplet, rotational
covariance further implies

$$
(H_2)_E=a_E I+\beta_E(S^z_{\rm tot})^2.
$$

Reason: V is the zero component of a vector operator; its two identical components
with rotationally scalar intermediate resolvents yield only rank-zero and rank-two
tensors. Axial symmetry selects component zero. On one irreducible multiplet this
is a scalar plus a quadratic function of magnetization. If an energy contains
multiple irreducible copies, matrix-valued coefficients and mixing must be kept.
No single-multiplet condition is asserted for all chain sizes.

When the condition holds, the classical second-order spectrum consists of lines

$$
\omega_{E,M}=d^2\beta_E(2M+1),\qquad
w_{E,M}=\frac{S(S+1)-M(M+1)}{n2^{n-1}},\quad M=-S,\ldots,S-1.
$$

Its weights sum to one after summing all multiplets. Add the SAME Cauchy broadening
and bin to get a positive classical comparator. Acquiring all beta_E, or sampling
their relevant distribution by another classical method, is not free. Conversely,
a large number of labels does not prove that every classical algorithm must list them.

## 4. A finite-dimensional response guarantee with explicit constants

The following lemma is derived here to state exactly what the reduction promises.
It is a conservative specialization of established effective-subspace methods [3].
It concerns an isolated zero sector, including an interior spectral sector; no
ground-state assumption is used.

Let L_0,D be finite-dimensional self-adjoint operators, Pi its zero-sector
projector, Pi D Pi=0, and o a unit vector in that sector. Suppose

$$
|\lambda|\geq g>0\quad(\lambda\in\operatorname{spec}(L_0)\setminus\{0\}),
\qquad \|D\|\leq v_*,\qquad e=|d|v_*,\quad x=e/g\leq1/8.
$$

Let p_full be the Cauchy(gamma)-broadened spectral law of L_0+dD in o, and p_eff
that of d^2 A in the SAME o. Then

$$
\boxed{
 d_{\rm TV}(p_{\rm full},p_{\rm eff})
 \leq\min\left\{1,\frac{2e}{g}+\frac{2e^3}{g^2\gamma}\right\}.
}
$$

The same bound covers common bins or other common probabilistic postprocessing.
Its failure is not a hardness statement. Numerics do not certify g, degeneracies
or coefficient errors; those require separate justified bounds for a claimed
application. The lemma's assumptions are not inferred from a few tested sizes.

### Proof by an invariant graph

In the Pi/complement decomposition write

$$
L_0+dD=\begin{pmatrix}0&F^\dagger\\F&B+dC\end{pmatrix},
\quad F=d(1-\Pi)D\Pi,\quad B=(1-\Pi)L_0(1-\Pi).
$$

Here ||F||,||dC||<=e and ||B^(-1)||<=1/g, whether B has one or both signs.
Put K=B+dC. On the ball ||X||<=2x the map

$$
X\longmapsto-K^{-1}F+K^{-1}XF^\dagger X
$$

maps the ball into itself and has Lipschitz constant at most 4x^2/(1-x)<1.
Indeed the image norm is at most x(1+4x^2)/(1-x)<=2x. Its fixed point therefore
satisfies KX+F=XF^dagger X and

$$
\|X+B^{-1}F\|\leq\frac{x^2(1+4x)}{1-x}\leq2x^2.
$$

Let N=(I+X^dagger X)^(-1/2) and W=[I;X]N. W is an isometry onto an invariant
subspace. Its exact self-adjoint effective generator is

$$
L_{\rm eff}=W^\dagger(L_0+dD)W=N^{-1}F^\dagger XN.
$$

Since d^2 A=-F^dagger B^(-1)F, the preceding estimates, ||N||<=1,
||N^(-1)||<=sqrt(1+4x^2), and ||N-I||,||N^(-1)-I||<=2x^2 give

$$
\|L_{\rm eff}-d^2 A\|\leq
[2\sqrt{1+4x^2}+4x]e^3/g^2\leq4e^3/g^2.
$$

Moreover $\langle o,Wo\rangle=\langle o,No\rangle\geq(1+4x^2)^{-1/2}$. The trace distance of the pure states o
and Wo is therefore at most 2x. Any spectral measurement, followed by the same
broadening, differs by at most that amount. The spectral law in Wo is the law of
L_eff in o. Finally Note 15's resolvent argument gives TV at most ||L_eff-d^2 A||/
(2 gamma) between their broadened laws. Combining these bounds proves the claim.
The bound includes state dressing and weight leakage; it is not only an eigenvalue
error estimate. It does not assume decay, time averaging, or a smooth memory density.

### Resolved weak-field limit

For this spin model v_*=n is a valid bound, since ||V||=n/2. At gamma=c d^2/J,

$$
d_{\rm TV}\leq\min\{1,2n|d|/g+2Jn^3|d|/(c g^2)\}.
$$

For fixed n and a fixed nonzero gap g this vanishes as d tends to zero, even
though the requested linewidth shrinks as d^2. The bound is conservative and
not uniform in growing n. It is not the statement that all large chains have a
small effective description. At fixed gamma the simpler bounds of Notes 15-16
may be preferable. State, spectral, and digital arithmetic errors must be budgeted
in addition to this model-reduction error.

## 5. A direct quantum sampler of the effective response

The spectral measure of A in o is not a memory-frequency distribution. Multiplying
a sample from that measure, broadened by gamma/d^2, by d^2 gives exactly p_eff.
This avoids the nonlinear memory-to-response conversion in Note 17. For d=0,
the original response is exactly the known single line and this route is unnecessary.

The formal projectors and inverse in A must not be granted as free oracles.
In the doubled-register representation, L_0=H_0 tensor I-I tensor H_0^T and
D=V tensor I-I tensor V^T have explicit local Pauli lists. Valid LCU normalizations
are alpha_0=3J(n-1)/2 and alpha_D=n. Suppose a certified gap lower bound g is
available; obtaining/certifying it is an additional input obligation.

Using standard quantum singular value transformation [4], build:

* a polynomial approximation of the zero-sector projector Pi, separated from
  the nonzero spectrum by the specified gap;
* a block encoding of (g/2)L_0^+, including the sign of nonzero frequencies;
* products with D/n to block encode A/alpha_A, alpha_A=2n^2/g.

Each effective-block call uses O((alpha_0/g) log(1/eta)) base L_0 block calls and
O(1) D block calls, with eta controlling block error. One can use identical
Hermitian polynomial filters on both sides to keep the encoded approximation
Hermitian. The inverse and projector act on the doubled system; no full list of
H_0 eigenstates, classical slow-mode matrix, or ground-state postselection is
supplied. State o already lies in the zero sector. Ancillas, coefficient-list
access, product construction and inverses still count.

Use Note 15's linewidth-matched clock for the effective generator. Suppressing
logarithmic precision/clock factors, a sufficient base-block query budget is

$$
N_0=\widetilde O\left[
 \frac{\alpha_0}{g}\left(1+\frac{n^2d^2}{g\gamma}\right)\right],
\qquad
N_D=\widetilde O\left(1+\frac{n^2d^2}{g\gamma}\right).
$$

Here tilde hides logarithms in accuracy, spectral ranges and condition numbers,
not unknown state preparation. A base-block query itself is not a gate or time
unit: total gates include N_0 times the L_0 SELECT/PREPARE cost and N_D times the
D cost, plus observable/clock preparation and readout per sample. For M samples,
repeated quantum preparation is paid M times. Classical preprocessing can be
reused by the competing effective-spectrum construction.

At gamma=c d^2/J, the displayed bound becomes

$$
N_0=\widetilde O\left[\frac{\alpha_0}{g}
 (1+n^2J/(c g))\right].
$$

There is no inverse power of d. Compare with the straightforward direct
linewidth-matched simulation budget ~alpha_0 J/(c d^2) in the weak-field regime.
This exposes a possible algorithmic improvement over that DIRECT QUANTUM
implementation, not over every quantum algorithm and not over the best classical
method. Output rescaling and input precision still require bits depending on d.
It is not generic fast forwarding: it uses a restricted initial observable sector,
a gap promise, a perturbative approximation and a compatible error budget.

A sufficient operator error xi in the compiled A adds at most d^2 xi/(2 gamma)
to the broadened-law TV. Thus xi<=2 gamma epsilon_alg/d^2 is adequate for an
allocated operator-error budget epsilon_alg. At the resolved scaling this required
absolute accuracy for A has no inverse power of d. Clock, state-preparation,
simulation, coefficient, gap-certification and digital-bin errors remain separate.
The construction is at the ideal block-encoding level, not a compiled circuit.

Quantum effective-Hamiltonian constructions are themselves prior work. Kowalski
and Bauman [5] and Li et al. [6] supply related downfolding and complementary-
resolvent/QSVT precedents. The latter's current primary version is v2, March 2026;
its stated task is a small reference-subspace eigenproblem, not this entire
high-temperature conserved-operator sector. We have not completed a priority or
complexity comparison with it. Do not claim novelty from the displayed composition.

## 6. A fully solved sector, and why it is not the whole answer

The maximum-spin multiplet S=n/2 is unique for J>0 and lies at the top exchange
energy E_max=J(n-1)/4. For all even n its second-order block is exactly

$$
(H_2)_{S=n/2}=\frac{S^2I-(S^z_{\rm tot})^2}{J(n-1)}.
$$

Derivation: in the one-spin-down sector E_max-H_0=(J/2)L_path, where L_path is
the path graph Laplacian. The staggered vector epsilon_i=(-1)^i has zero sum.
Its inverse quadratic form is epsilon^T L_path^+ epsilon=n/2: the unique edge
flows have alternating cumulative sums -1,0,-1,0,..., and energy is their squared
sum. The M=S-1 second-order energy is therefore 1/J. Rotational covariance gives
the factor (S^2-M^2)/(n-1) for other magnetizations, proving the expression.

This yields a simple, correctly shifted line family, but its fraction of the
full high-temperature collective spectral weight is only

$$
w_{\max}=\frac{(n+1)(n+2)}{3\,2^n}.
$$

This follows by summing S(S+1)-M(M+1) and dividing by n2^(n-1). For n=2 it is the
whole spectrum and reproduces Note 17's shifted pair. As n grows its fraction
vanishes. It would be wrong to solve this convenient sector and relabel it the
full NMR response. Other multiplets remain necessary for the original contract.

The same one-magnon calculation also supplies a warning independent of numerical
extrapolation. The smallest nonzero operator frequency obeys

$$
g_n\leq J[1-\cos(\pi/n)]=O(J/n^2).
$$

This is an UPPER bound, not a usable lower-bound promise for the quantum inverse.
Other energy differences may be much smaller. The first fixed-size controls give
minimum nonzero differences/J of about 1, 0.292893, 0.0348921 and 0.000479582 for
n=2,4,6,8. These are floating-point observations, not a proved scaling law or
certified eigenvalue enclosures. A generic minimum-gap implementation may lose
its benefit as the chain grows. Symmetry-restricted or response-weighted treatment
of near resonances is a possible improvement to analyze, not something assumed free.

## 7. Next decision

The next bounded mathematical question is whether the global inverse-gap cost can
be replaced by a justified treatment of only the near resonances that actually
couple to the collective response. Derive the error for retaining such resonances
in the slow block, or regularizing the inverse with an explicit response-weighted
remainder. Do not discard small denominators merely because their total spectral
weight appears small; Note 17 demonstrates why that can fail at resolved linewidth.

Compare with classical symmetry-resolved effective coefficients, recursion,
restricted operators, tensor networks and projection-free methods. The easy
maximum-spin calculation is a control, not an application or a lower bound for
other sectors. Failure of a global gap certificate is not a no-go theorem for
direct quantum dynamics, which does not need that inverse. Keep the earlier direct
sampler and climate/distribution mechanisms open. No third spin-off or data/native
implementation campaign follows from this checkpoint.

## 8. Executed checks and source scope

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/slow_sector_v1/verify.py`
uses Python 3.10+ and NumPy. Its final version passed twice with identical JSON;
-O/-OO refusals were checked. Four fixed chains, n=2,4,6,8, test reflection,
zero-sector overlap, the effective-commutator identity, 98 energy-block parity
and quadratic-multiplet controls, and the maximum-spin formula/weight. Four
2/4-spin binned spectra satisfy the conservative bound. Four small abstract block
systems test the invariant-graph identities and remainder bounds. Six path
Laplacians check the closed quadratic form. Degenerate/mixed-parity, broken-
reflection and omitted-first-order negative controls and four invalid linewidths
are retained. These are complex128 diagnostics at tolerance 3e-9, not interval
proofs, arbitrary-size parity results, quantum hardware, experimental spectra,
performance measurements or a compiled QSVT implementation. The first draft had a
NumPy boolean-negation error, fixed before the reported successful runs.

The continuous bound follows from the proof, not finite bins. No new physical
relaxation assumption was made. No upstream implementation, experimental spectrum
or climate data was imported. Historical scientific suites were not rerun; all
prior research files and both independent spin-offs remain unchanged.

Executed checker SHA256: `220a502692b2a64668594dfdffc4c882e07664fbb2941d7a454acd5a7fb8e59d`.
Report SHA256: `470b2f1a5fb6f6ffe6fbacf7db298ce1dfd6e42ec759e29ab741f5d1cf454f05`.

Primary sources checked 28 September 2026; search is focused, not exhaustive:

[1] Sels et al., Quantum approximate Bayesian computation for NMR model inference,
Nature Machine Intelligence 2 (2020), arXiv:1910.14221v2. Primary abstract/model
context rechecked; no experimental benchmark reproduced.
https://arxiv.org/abs/1910.14221

[2] Sels and Demler, Quantum generative model for sampling many-body spectral
functions, PRB 103, 014301 (2021). Primary abstract and inherited Note 15 contract.
https://arxiv.org/abs/1910.14213

[3] Bravyi, DiVincenzo and Loss, Schrieffer-Wolff transformation for quantum
many-body systems, Annals of Physics 326 (2011). Primary PDF Section 3.1 and scope
of the general spectral-subspace construction inspected; its ground-energy/local
results are NOT imported as high-temperature response guarantees. PDF screenshot
attempt failed. The explicit graph and TV proof above supplies the used constants.
https://arxiv.org/abs/1105.0675

[4] Gilyen, Su, Low and Wiebe, Quantum singular value transformation and beyond,
STOC 2019; arXiv:1806.01838v1. Theorems 31/41, product block encoding and simulation
sections inspected. Page 38 (zero-based 37) was visually checked for inverse
normalization and gap dependence. No QSVT phase sequence was generated or run.
https://arxiv.org/abs/1806.01838

[5] Kowalski and Bauman, Fock-Space Schrieffer-Wolff Transformation: Classically-
Assisted Rank-Reduced Quantum Phase Estimation Algorithm, Applied Sciences 13, 539
(2023). Primary indexed abstract inspected; a direct publisher fetch was rate
limited. This is a predecessor, not a validated advantage for the present model.
https://doi.org/10.3390/app13010539

[6] Li et al., Quantum Algorithm for Low Energy Effective Hamiltonian and Quasi-
Degenerate Eigenvalue Problem, arXiv:2510.08088v2 (21 March 2026). Primary abstract
and version metadata inspected; full HTML fetch failed. Differently worded search
summaries were not used as the source of the current title or a cost theorem.
https://arxiv.org/abs/2510.08088v2

Only Quantum-Assisted-Algorithm-Discovery is writable. Manuscript remains on hold;
no contact, paid/unattended computation, release, merge or new repository follows.
