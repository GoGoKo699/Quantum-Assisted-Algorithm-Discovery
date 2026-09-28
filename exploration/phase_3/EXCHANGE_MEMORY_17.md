# Exchange memory 17: separate spectral linewidth from memory time

28 September 2026. Read baseline: `c6bc4ca6f069bd1f0a7fb94c578d45b17b7b3b4b`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Outcome:** the alternating-offset family admits an exact projected-memory
representation with an explicitly implementable rank-two quantum correction.
A conditional, finite-linewidth certificate specifies when that memory may be
replaced by one Lorentzian line. A resolved two-spin limit shows why fast exchange
alone does not justify the replacement, and supplies a corrected classical
surrogate. No fast-memory theorem for a growing chain, quantum advantage, new
physical prediction, or publication priority is established.

The purpose is to identify a possible shorter-time quantum integration, not to
create another classical spin-off or require a learned classical program. Direct
spectral sampling from Note 15 remains a valid alternative. The model and requested
output are unchanged; no experimental data or package installation is needed.

## 1. Same model, different mathematical question

Use an even open chain, initially with uniform J>0:

$$
H(d)=H_J+dV,\qquad H_J=J\sum_{i=1}^{n-1}\mathbf S_i\cdot\mathbf S_{i+1},
\qquad V=\sum_i(-1)^iS_i^z,\qquad O=\sum_iS_i^+.
$$

Reflection-symmetric bonds J_i=J_(n-i) may replace J where stated. The exact
projection identities also hold without that reflection symmetry. Coefficients
are angular frequencies, hbar=1. The output is the high-temperature raising-
correlation probability law convolved with ell_gamma, then assigned to the agreed
bins at TV tolerance epsilon. It is not an arbitrary pulse signal, absolute
intensity, or a first-principles chemical calculation. The finite-range family is
a structural subfamily of the justified NMR model in Notes 14-15 [1].

Exchange narrowing and memory-function analysis are established magnetic-resonance
ideas [2,3]. In particular, a Lorentzian is not a theorem from a large exchange
constant alone: the literature explicitly distinguishes short memory from slow
hydrodynamic tails and finite-system resonances [3]. Its anisotropic electron-spin
examples are precedents for the issue, not a validated linewidth formula for our
alternating-offset nuclear-spin family.

Here the question is whether the long resolved response can be determined from
shorter projected dynamics. A representation identity by itself supplies no cost
advantage; this note makes its implementation and remaining assumptions explicit.

## 2. The measured mode couples to one known staggered mode

Work in operator Hilbert space with Frobenius inner product, and let

$$
o=\frac{\sum_iS_i^+}{\sqrt{n2^{n-1}}},\qquad
v=\frac{\sum_i(-1)^iS_i^+}{\sqrt{n2^{n-1}}},\qquad L_d=[H(d),\cdot].
$$

For even n, o and v are orthonormal. Isotropic exchange commutes with O, so

$$
L_do=dv,\qquad P=|o\rangle\langle o|,\quad Q=I-P.
$$

The generator of the orthogonal, or projected-memory, dynamics is

$$
\boxed{B_d=QL_dQ=L_d-d(|o\rangle\langle v|+|v\rangle\langle o|).}
$$

This is an exact identity on the full operator space. It follows by expanding
QL_dQ and using PL_dP=0 and self-adjointness. B_d is self-adjoint and annihilates
o. This is an orthogonal high-temperature projection, not a general nonorthogonal
open-system projection whose generator might be non-Hermitian.

Define, for Im z>0,

$$
F_d(z)=\langle v,(z-B_d)^{-1}v\rangle,\qquad
G_d(z)=\langle o,(z-L_d)^{-1}o\rangle.
$$

Schur complementation of the o/Q blocks gives the exact relation

$$
\boxed{G_d(z)=\frac1{z-d^2F_d(z)}.}
$$

Both functions have nonpositive imaginary part in the upper half-plane. F_d is
the Stieltjes transform of a normalized positive memory spectral measure nu_d.
The desired physical spectrum remains

$$
p_{d,\gamma}(\omega)=-\frac1\pi\operatorname{Im}G_d(\omega+i\gamma).
$$

The memory spectrum is NOT itself this physical output. There is no claimed
one-draw classical map taking an arbitrary memory-frequency sample to a correct
response sample. Continued fractions, projection, and this Schur mechanism are
prior mathematical machinery [2], not a new reduction in principle.

In time-domain form put K_d(t)=<v,exp(-itB_d)v> and C_d(t)=<o,exp(-itL_d)o>.
Eliminating the orthogonal component gives

$$
\dot C_d(t)=-d^2\int_0^t K_d(t-s)C_d(s)\,ds,\qquad C_d(0)=1,
\qquad F_d(z)=-i\int_0^\infty e^{izt}K_d(t)dt.
$$

The rest of the CLOSED spin system supplies this memory; no new physical bath,
noise process, or relaxation assumption has been added. The damped integral exists
for Im z>0 even if finite-system correlations never decay.

For reflection-symmetric bonds, reflection followed by a global pi spin rotation
about x commutes with H and exchanges O with O^dagger. Hence the physical law is
even. The resolvent identity then gives an even nu_d and real K_d(t). In particular

$$
\kappa_\gamma=-\operatorname{Im}F_d(i\gamma)
 =\int_0^\infty e^{-\gamma t}K_d(t)dt\geq0.
$$

Further exact data: [V,v]=o, so B_d v=[H_J,v]. Consequently
||B_d v||^2=2 sum_i J_i^2/n, independent of d. Fast initial memory curvature is
therefore present even when the later memory is not short. Low moments do not
by themselves bound the long-time tail.

## 3. A quantum operation for the projected dynamics, without a projected oracle

Use the doubled computational-basis vectorization of Notes 14-15. Then
L_d=H(d) tensor I-I tensor H(d)^T acts on 2n qubits.
Let u_+=(o+v)/sqrt(2) and u_-=(o-v)/sqrt(2). They are the normalized collective
raising operators on the two sublattices. Their states use the same one-excitation
and Bell-pair preparation as Note 15, now restricted to n/2 sites. Preparing v
instead of o only changes known alternating phases in that construction.

With reflections R_+=I-2|u_+><u_+| and R_-=I-2|u_-><u_-|,

$$
\boxed{B_d=L_d+\frac d2(R_+-R_-).}
$$

Each reflection is U_+/- (I-2|0><0|) U_+/-^dagger for a known state-preparation
circuit. Thus it is not access to an exponentially supplied projector or an
unknown many-body eigenstate. The projections are nonlocal on the doubled
register, but have this explicit polynomial-size circuit construction.

Equivalently, the removed rank-two coupling has eigenvalues +/-d on u_+,u_-;
its exponential is two known rank-one phase operations. Product formulas or
linear-combination/block-encoding simulation can combine it with L_d [4]. For
Lambda=(1/2)sum|delta_i|+(3/4)sum|J_i|, a Pauli-plus-reflection LCU normalization
is at most 2 Lambda+|d|. This is a normalization budget, NOT a constant-cost
oracle or gate estimate. Coefficient selection, state preparation/inverses,
controlled operations, precision, and simulation error still count.

K_d(t) can consequently be estimated with a Hadamard test on exp(-itB_d), or the
broadened memory measure can be sampled with Note 15's clock. Neither operation
has been run on hardware. The same reduction is available classically; a quantum
benefit requires the needed projected dynamics to be expensive classically.
A smaller maximum coherent time need not imply fewer total gates or shots.

## 4. When is replacing the memory by one number justified?

Fix a nonnegative proposed value kappa, including its estimation uncertainty.
Replacing F_d(omega+i gamma) by -i kappa gives a valid normalized Cauchy line

$$
\ell_\Gamma(\omega),\qquad \Gamma=\gamma+d^2\kappa.
$$

This replacement is a proposed approximation, not an assumption hidden in the
model. To test it, supply a bound valid on a frequency window:

$$
\sup_{|\omega|\leq\Omega}|F_d(\omega+i\gamma)+i\kappa|\leq\Delta,
\qquad r=\frac{d^2\Delta}{\Gamma}<1.
$$

Then the following sufficient continuous-TV bound holds:

$$
\boxed{
 d_{\rm TV}(p_{d,\gamma},\ell_\Gamma)
 \leq\min\left\{1,
 \frac{r}{\pi(1-r)}\arctan\frac\Omega\Gamma
 +\frac{2d^2}{\Omega^2}
 +\frac1\pi\arctan\frac{2\gamma}{\Omega}
 +\frac1\pi\arctan\frac\Gamma\Omega\right\}.
}
$$

This also bounds common binning. If r>=1, the displayed nontrivial certificate
is unavailable; no conclusion of hardness or actual failure follows. The bound
is conservative, and a supplied uniform memory error is not obtained merely by
checking a finite frequency grid.

**Proof.** In the window, put g0=(omega+i Gamma)^(-1). The Schur identity yields

$$
|G_d-g0|\leq\frac{d^2\Delta}{(1-r)(\omega^2+\Gamma^2)}.
$$

Integrating the density difference with its TV factor 1/(2 pi) gives the first
term. The UNBROADENED physical law has second moment d^2 because L_d o=dv.
If X has that law and Z is independent Cauchy(gamma), then

$$
\Pr(|X+Z|>\Omega)\leq4d^2/\Omega^2+
 (2/\pi)\arctan(2\gamma/\Omega).
$$

This uses the union |X|>Omega/2 or |Z|>Omega/2 and the second-moment inequality.
The reference Cauchy(Gamma) tail is (2/pi)arctan(Gamma/Omega). Half the sum of
the two tails supplies the remaining terms. No finite moment of a Cauchy law
is asserted. This is an internally derived error specialization; publication
priority for it has not been established.

### Make the memory assumption and scalar acquisition cost visible

For kappa=kappa_gamma, define

$$
M_1(\gamma)=\int_0^\infty t e^{-\gamma t}|K_d(t)|dt.
$$

Since |exp(i omega t)-1|<=|omega|t, Delta<=Omega M_1(gamma). If kappa is estimated
with error at most e_kappa, use Delta<=Omega M_1(gamma)+e_kappa instead. The generic
bound M_1<=1/gamma^2 is always true but may be unhelpful. Short-memory compression
needs a substantially better justified bound, not just a large J or fast curvature.

A possible bounded-time acquisition of kappa uses times t in [0,T_m] with density
exp(-gamma t)/A_T, where A_T=(1-exp(-gamma T_m))/gamma. A Hadamard-test outcome
X in {-1,+1}, with mean Re K_d(t), makes A_T X an unbiased estimator of the
truncated integral. Hoeffding gives sufficient independent shot count

$$
N_{\rm shot}\geq\frac{2A_T^2}{a^2}\log\frac2\zeta
$$

for statistical error at most a with failure at most zeta. Include the tail
R_gamma(T_m)=integral_(T_m)^infinity exp(-gamma t)|K_d(t)|dt, circuit bias,
quadrature/clock precision, and state preparation in e_kappa. Clipping an estimate
to nonnegative values cannot increase its error relative to kappa_gamma.

Without a better tail estimate, R_gamma(T_m)<=exp(-gamma T_m)/gamma simply restores
the usual linewidth time scale. A known short tail can permit T_m much less than
1/gamma, but that condition is NOT established here for the growing chain.
Closed finite systems recur: an all-time exponential decay law cannot be imposed
on them without a justified continuum/relaxation limit and a finite-size remainder.

This optional quantum-memory-assisted line approximation must also beat classical
memory-function, tensor-network, recursion and direct-correlation calculations.
Projection-free auxiliary-kernel methods are established alternatives [5]. Both
sides may reuse acquired response information for many samples. No claim that
maximum circuit depth alone determines cost is made.

## 5. A resolved limit: a small memory contribution can be essential

The exact two-spin member has offsets +/-d and coupling J>0. Its collective
observable recursion closes as the four-site Jacobi chain with off-diagonals
(d,J,d). The projected-memory transform is

$$
F_d(z)=\frac{z^2-d^2}{z(z^2-J^2-d^2)}
=\frac{d^2}{J^2+d^2}\frac1z+
 \frac{J^2}{J^2+d^2}\frac{z}{z^2-J^2-d^2}.
$$

Thus

$$
K_d(t)=\frac{d^2+J^2\cos(t\sqrt{J^2+d^2})}{J^2+d^2}.
$$

The memory has a zero-frequency mass d^2/(J^2+d^2), tending to zero as d/J tends
to zero. Replacing it by its d=0 value F_0(z)=z/(z^2-J^2) removes that mass.
Nevertheless, the resulting output can remain wrong by order one at a resolved
narrow linewidth. A perturbation that is small at a fixed frequency need not be
uniformly small in the shrinking frequency window controlling the signal.

Write R=sqrt(J^2+4d^2). The exact physical frequencies are +/-s and +/-h, where
s=(R-J)/2, h=(R+J)/2. Each low line has mass (1+J/R)/4 and each high line has
mass (1-J/R)/4. In contrast, substituting F_0 gives a line at zero of mass
J^2/(J^2+d^2), plus lines at +/-sqrt(J^2+d^2) sharing the remainder.

For gamma=c d^2/J with fixed c>0, rescale frequency by d^2/J. The exact broadened
law tends to 1/2 ell_c(. -1)+1/2 ell_c(. +1), whereas the F_0 approximation tends
to ell_c. In the central bin [-1/2,1/2] their mass difference tends to

$$
\frac{3\arctan(1/(2c))-\arctan(3/(2c))}{\pi}.
$$

At c=0.1 this is about 0.83269043. This is an exact limiting BIN discrepancy,
and hence a lower bound on TV; it is not a measured NMR error or a lower bound
on classical algorithms. Here gamma AND the bins shrink with d^2/J. At fixed
gamma>0 the discrepancy vanishes; there is no contradictory fixed-resolution
claim and no justification for arbitrarily demanding this precision in an application.

### Keep the strong classical repair

The two-spin example is classically easy even at that narrow resolution. Keep the
second-order shifted pair instead of dropping the small memory contribution:

$$
\widetilde p=\tfrac12\ell_\gamma(. -d^2/J)+
             \tfrac12\ell_\gamma(. +d^2/J).
$$

The total satellite mass is at most d^2/J^2. Also s(s+J)=d^2 implies
|s-d^2/J|=s^2/J<=d^4/J^3. Coupling line labels and using the Cauchy translation
bound gives the continuous result

$$
 d_{\rm TV}(p_{d,\gamma},\widetilde p)
 \leq\min\{1,d^2/J^2+d^4/(\pi\gamma J^3)\}.
$$

It tends to zero even for gamma=c d^2/J. The control therefore rejects a naive
memory replacement, NOT classical resummation or a secular/effective-model method
in general. It also explains why neither long response time nor a failed
low-order truncation alone proves quantum difficulty.

## 6. What this adds to the open quantum question

Three quantities must be kept separate: the duration of the resolved response,
the decay of its projected memory, and the classical complexity of obtaining that
memory or an equally useful effective response. The first can be long while the
second is short; the third is not determined by either duration alone.

The exact rank-two construction exposes a quantum entry point into the second
quantity without acquiring a classical Lanczos chain or projected eigenspace first.
The window certificate converts a justified memory estimate into the SAME physical
output guarantee. The two-spin control demonstrates why the memory's low-frequency
weight cannot simply be dropped on the basis of its small total mass.

**Next bounded derivation:** for the uniform even chain (with the two-spin limit
retained as a control), analyze low-frequency projected memory beyond the first
moments. Determine whether symmetry/effective slow modes or a controlled memory
approximation supplies a compact response at gamma relative to d^2/J, and identify
which residual correlations remain necessary. In particular, distinguish a finite-
chain zero-frequency contribution from a smooth thermodynamic memory density.
Do not assume decay from a finite trace or assume integrability supplies every
finite-resolution answer for free. One concrete first test is the overlap of the staggered mode with the conserved
operator sector of L_0=[H_J,.], followed by the first nonvanishing effective
coupling within that sector. Any inverse small-gap or system-size dependence of
this reduction must be retained. No large numerical sweep is the next task.

If the low-frequency effect closes in a small effective description, that is a
classical comparator that must be retained. If it requires nontrivial many-body
projected dynamics, compare its best classical representations with the explicit
quantum route at the same output quality. Neither outcome is asserted now.
Strong classical methods can infer useful spectra without direct real-time
simulation to every linewidth time; complex-time Krylov work supplies another
predecessor to consider within its documented model scope [6]. No all-classical
lower bound follows from failure of one representation.

## 7. Checks, sources, and limitations

The independent NumPy diagnostic is
`python experiments/exchange_memory_v1/verify.py`. With one BLAS thread it passed
twice with identical output; -O/-OO refusals were checked. Three fixed two/four-spin
systems check projection/reflection identities, 45 Schur identities, memory
symmetry, finite-window envelopes, three binned error controls, and 18 truncated-
memory identities. Four d/J choices check 24 dimer identities, the resolved-limit
counterexample and the corrected two-line bound. Five invalid inputs are rejected.

These are complex128 checks at tolerance 3e-10, not rigorous interval numerics,
compiled circuits, large-chain evidence, experimental spectra, or performance
measurements. The continuous bounds and limiting statements follow from the
written proofs, not a finite grid. The checker makes no short-memory inference
from its matrices. No old scientific verifier was rerun, no source data or
upstream implementation was imported, and no physical or quantum simulation
benchmark occurred.

Checker SHA256: `b5da26c42a33cd7cd158676a3056597b3e1360924a2e7a086016a879b49a338a`.
Report SHA256: `3c8257eacaf57e8f170b262d04e210bde79f2abdb08d04cb68eaf8b1cc9cbc8f`.

Primary sources inspected 28 September 2026; the search is focused, not exhaustive:

[1] Sels et al., *Quantum approximate Bayesian computation for NMR model inference*,
Nature Machine Intelligence 2, 396-402 (2020), arXiv:1910.14221. Model and response
scope already audited in Notes 14-16; no new application result asserted.
https://arxiv.org/abs/1910.14221

[2] Mori, *A Continued-Fraction Representation of the Time-Correlation Functions*,
Progress of Theoretical Physics 34, 399-416 (1965). Primary abstract and formalism
scope inspected. Projection/continued-fraction precedence, not validation of our
specific error bound. https://doi.org/10.1143/PTP.34.399

[3] El Shawish, Cepas and Miyashita, *Electron spin resonance in S=1/2 antiferromagnets
at high temperature*, PRB 81, 224421 (2010), arXiv:1004.0839v1. Introduction and
Section III, particularly the projected-memory and Markov assumptions, read from
the primary PDF. Page-3 screenshot failed; no graph or table was digitized and no
figure-derived numerical result is used. Its anisotropy models are not our field
model. https://arxiv.org/abs/1004.0839

[4] Low and Chuang, *Hamiltonian Simulation by Qubitization*, Quantum 3, 163 (2019).
Publisher input-oracle/LCU contract inspected. No new simulation primitive or
constant-cost coefficient oracle is claimed.
https://quantum-journal.org/papers/q-2019-07-12-163/

[5] Montoya-Castillo and Reichman, *Approximate but Accurate Quantum Dynamics from
the Mori Formalism: I. Nonequilibrium Dynamics*, JCP 144, 184104 (2016),
arXiv:1603.01903. Primary abstract: projected dynamics can be replaced with
ordinary auxiliary kernels in that formalism. It is a classical-method precedent,
not a proved efficient solution for the present family.
https://arxiv.org/abs/1603.01903

[6] Paeckel, *Spectral decomposition and high-accuracy Greens functions: Overcoming
the Nyquist-Shannon limit via complex-time Krylov expansion*, arXiv:2411.09680.
Primary abstract only; its method and model examples were not independently
benchmarked or generalized here. https://arxiv.org/abs/2411.09680

[7] Sels and Demler, *Quantum generative model for sampling many-body spectral
functions*, PRB 103, 014301 (2021), arXiv:1910.14213. Primary abstract and earlier
repository analysis: direct spectral-sampling precedent.
https://arxiv.org/abs/1910.14213

Keyword searches for quantum projected-memory algorithms produced substantial
irrelevant material (including unrelated authors named Mori). That is not an
exhaustive novelty audit. No priority or practical advantage is claimed for the
rank-two composition or the conditional certificate.

Only the parent repository is modified. Direct sampling and model-first scope
remain. Climate/dynamics remain open; Manthan is paused, battery/operator routes
parked, the two classical spin-offs independent, and Phase-2 Note 27 closed.
Preserve old evidence, licenses and rights. No outside contact, paid/unattended
work, manuscript, release, branch merge, new repository or administration change.
