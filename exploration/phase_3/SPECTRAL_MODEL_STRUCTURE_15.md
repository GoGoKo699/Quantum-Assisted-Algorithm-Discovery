# Model-first comparison 15: observable structure and a linewidth-matched sampler

28 September 2026. Starting head: `8134a253d94d6fd2218971c41fb54d5be51214fc`.
Working branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Outcome.** The two open model families are compared below. Direct spin-spectral
sampling is selected for the next mathematical analysis, without closing the
classical-dynamics route. A geometric-clock construction explicitly samples a
Lorentzian-broadened spectral law, with truncation and frequency-wrap errors
bounded. Several exact classical limits and resolution-dependent comparison
bounds identify where that quantum construction does NOT establish an advantage.
No useful separation, priority claim, measured spectrum or hardware result is
established. These are model-level deductions, not a new demonstration molecule.

## 1. The model comparison

### Classical probability evolution

Let a smooth, complete flow Phi_t solve xdot=f(x), and let the initial law p0 be
specified and sampleable. On a domain with the appropriate no-flux/decay boundary
conditions, the amplitude generator is

$$
K=-i\left(f\cdot\nabla+\tfrac12\nabla\cdot f\right),\qquad
\psi_t(x)=\psi_0(\Phi_{-t}x)|\det D\Phi_{-t}(x)|^{1/2}.
$$

The unitary flow representation gives |psi_t|^2=(Phi_t)_#p0. This is the existing
Koopman-von Neumann construction [1], not a new linearization. Completeness and
operator-domain conditions matter; absorbing boundaries or stochastic diffusion
are not covered just by writing this deterministic generator.

The SAME output law is obtained classically by drawing x0~p0 and computing
Phi_t(x0). For M independent endpoints, compare symbolically

$$
C_C=M(C_{p_0}+C_{\Phi_t}),\qquad
C_Q=M(C_{\sqrt{p_0}}+C_{K_h}(t,\eta)+C_{\rm output}).
$$

Here h is a declared discretization and its distributional error must be bounded;
eta is simulation error. C_output includes d resolved coordinates if a whole
state is requested. Linearizing a density does not itself beat the trajectory
sampler. Even a linearly unstable flow with Gaussian initial uncertainty has an
explicit Gaussian pushforward and a classical affine sampling construction.
Instability alone is therefore not a quantum opportunity. This says nothing
universal about nonlinear coarse observables or hard initial distributions.

Conditioning on a rare event is another possible mechanism, but has its event-
probability and guided-classical-comparator costs. Notes 11-13 retain that analysis.
No climate archive is needed for this comparison, and none was obtained here.

### Interacting spin spectra

A spectral measurement depends on coherent transition matrix elements, not only
on propagating an ordinary initial-state sample. Its existing quantum entry point
is energy-gap measurement on an observable state [2]. Classical correlation,
restricted-state, tensor-network and direct spectral methods remain legitimate
competitors [5,6]; dense diagonalization is only an upper bound, not their limit.

**Choice for this round:** develop the finite-resolution spectral law. This
exposes quantum interference directly and has a simple justified preparation,
while the required linewidth supplies a mathematical comparison parameter.

## 2. Physically anchored model and output contract

For n homonuclear spin-1/2 sites, take the liquid-state scalar-coupling model [3,4]

$$
H=\sum_i\delta_i S_i^z+\sum_{i<j}J_{ij}\,
 (S_i^xS_j^x+S_i^yS_j^y+S_i^zS_j^z),\qquad S^a=\sigma^a/2.
$$

All coefficients use angular-frequency units; hbar=1. Remove the known mean
carrier so sum_i delta_i=0. Uniform axial rotation shifts the raising-operator
spectrum by that carrier and does not change its shape. The shared input is the
explicit coupling list, offsets, requested linewidth gamma>0, and output bins.
Generating these parameters from electronic chemistry is a separate task.

Take O=sum_i S_i^+, with S^+=S^x+iS^y. This makes the positive raising/lowering
correlation measure explicit, rather than silently treating every pulse signal
as a probability. For eigenpairs of H, define

$$
\mu_H(d\omega)=\frac{\sum_{a,b}|\langle a|O|b\rangle|^2
                    \delta_{E_a-E_b}(d\omega)}{\operatorname{Tr}(O^\dagger O)}.
$$

This is a probability measure and Tr(O^dagger O)=n 2^(n-1). Its characteristic
function is Tr[O^dagger exp(iHt) O exp(-iHt)]/Tr(O^dagger O). The selected target is

$$
p_{H,\gamma}(\omega)=(\mu_H*\ell_\gamma)(\omega),\qquad
\ell_\gamma(x)=\frac{\gamma}{\pi(x^2+\gamma^2)}.
$$

Return its specified frequency-bin labels, including overflow bins, to total-
variation (TV) error 0<epsilon<1. TV controls every bin/event probability, but does
not promise a relative error for arbitrarily weak lines. Full histogram learning,
parameter fitting and repeated queries have separate shot and optimization costs.

The high-temperature spin-response and phenomenological exponential damping that
lead to this Lorentzian model are established NMR approximations [2-4]. They do
not cover arbitrary relaxation, hyperpolarized states, absolute signal strength,
chemical exchange, or signed multi-pulse spectra. Those require different models.
The application anchor is spectrum prediction/fitting from spin parameters [4],
not a claim that every such instance is classically difficult.

## 3. Quantum entry point: match the linewidth instead of measuring unnecessary digits

### Observable preparation

Use fixed computational-basis vectorization

$$
|o\rangle=\operatorname{vec}(O)/\|O\|_F,\qquad
L=H\otimes I-I\otimes H^T.
$$

L has eigenvectors |a>|b*> and energy gaps E_a-E_b. The spectral measure of L in
|o> is exactly mu_H. This extends the Hermitian-observable notation of Note 14
to this non-Hermitian O using O^dagger O, not O^2. The transpose is essential.

Preparation remains simple:

$$
|o\rangle=\frac1{\sqrt n}\sum_j |01\rangle_j
                      \bigotimes_{k\ne j}|\Phi^+\rangle_k.
$$

Prepare a W state in the second members of n pairs, with the first members zero.
On each pair apply a Hadamard to the first bit controlled on the second being
zero, then CNOT from the first to the second. The local map sends |00> to Phi+
and |01> to |01>. Thus no unknown many-body ground state or exponentially rare
postselection is assumed. W-state rotations and finite-precision synthesis cost
resources; this is an elementary preparation identity, not a novelty claim.

### A finite, product-state geometric clock

Let N=2^m, tau>0, r=exp(-gamma tau), and T=N tau. Prepare

$$
|c\rangle=\sqrt{\frac{1-r^2}{1-r^{2N}}}
                  \sum_{j=0}^{N-1}r^j|j\rangle.
$$

This is NOT an arbitrary N-entry state-preparation oracle. Binary expansion of j
factorizes it into m one-qubit states:

$$
|c\rangle=\bigotimes_{k=0}^{m-1}
 \frac{|0\rangle+r^{2^k}|1\rangle}{\sqrt{1+r^{2^{k+1}}}},
$$

with the usual little-endian indexing. Apply controlled exp(-iL j tau). Draw a
classical offset theta uniformly from [0,2pi/N), apply exp(i j theta) to the clock,
and use the positive-phase Fourier transform. On outcome k report phase
phi=2pi k/N+theta, reduced modulo 2pi. For an L-eigenvalue nu, the outcome density
on the phase circle is

$$
q_N(\phi\mid\nu)=\frac{1-r^2}{2\pi(1-r^{2N})}
\frac{|1-r^Ne^{iN(\phi-\nu\tau)}|^2}
     {|1-re^{i(\phi-\nu\tau)}|^2}.
$$

**Derivation:** the conditional discrete amplitude is
N^(-1/2) sum_j c_j exp[ij(2pi k/N+theta-nu tau)]. The offset has density N/(2pi),
which cancels the N from its squared amplitude. A geometric sum gives the formula.
Tracing the system gives the mixture of these kernels over mu_H; different energy
components are orthogonal, so no unaccounted cross terms remain.

The infinite-clock limit is the Poisson kernel

$$
q_\infty(\phi\mid\nu)=\frac{1-r^2}
 {2\pi[1-2r\cos(\phi-\nu\tau)+r^2]}.
$$

Its Fourier coefficients are r^|k| exp(-ik nu tau), so after converting phase to
frequency it is precisely a Cauchy/Lorentzian line of width gamma wrapped with
period 2pi/tau. This is how the target broadening arises; it is not identified
with the standard uniform-clock QPE leakage kernel by assumption.

### Explicit error and time bounds

Writing u=r^N=exp(-gamma T), the ratio q_N/q_infinity differs from one by at most
2u/(1-u). Therefore, uniformly over nu and over the spectral mixture,

$$
d_{\rm TV}(q_N,q_\infty)\leq\min\{1,u/(1-u)\}.
$$

For a known support |nu|<=W, choose output range [-Omega,Omega) with Omega>W and
tau=pi/Omega. Unwrapping into this principal interval adds at most the Cauchy tail

$$
\Pr(|\nu+Z|\geq\Omega)
 \leq\frac2\pi\arctan\frac{\gamma}{\Omega-W}
 \leq\frac{2\gamma}{\pi(\Omega-W)},\quad Z\sim\ell_\gamma.
$$

A sufficient symbolic choice is Omega=W+6gamma/(pi epsilon) and
T>=gamma^(-1) log(1+3/epsilon), rounded UP through N to a power of two. This bounds
truncation and wrapping by epsilon/3 each. Preparation, simulation, finite offset
and arithmetic errors consume the remaining budget. The sum of controlled
Liouvillian evolution times is (N-1)tau<T, with less than a factor-two rounding
increase above the target time (or one minimal clock interval).

Thus the ideal controlled-evolution time to sample the BROADENED law is

$$
T=O\big(\gamma^{-1}\log(1/\epsilon)\big),
$$

not an inverse microscopic level spacing. This is not a gate count or a lower
bound, and not evidence of a speedup over classical correlation methods.
Direct spectral sampling and windowed phase estimation are prior work [2,7,8].
The exponential window, Fourier identities and their use here carry no priority
or optimality claim. A focused search did not establish priority for this exact
product-clock/dither/error composition.

### Finite output and access costs are visible

An actual digital output is a bin label, not an exact continuous real. If the
classical offset is rounded with phase error at most d, the clock-state change
contributes at most (N-1)d in TV. Its ideal phase density is bounded by
q_max=(1+r)/(2pi(1-r)). For K bin boundaries on the phase circle (including the
wrap point), label changes contribute at most 2K d q_max. Therefore a sufficient
finite-offset error budget is [(N-1)+2K q_max]d. A uniform b-bit offset supplies
d<=2pi/(N 2^b). This explicitly avoids claiming continuous-TV accuracy for a
purely discrete output. Further arithmetic/QFT/state errors must also be bounded.

For the explicit Pauli expansion, set
Lambda=(1/2)sum_i |delta_i|+(3/4)sum_edges |J_ij|; W=2Lambda is a sufficient support
bound. Standard Hamiltonian simulation [9] gives controlled-evolution query costs
of order Lambda T plus logarithmic precision terms. For the doubled generator,
forward and conjugate evolution have a constant-factor cost. The term-selection
and coefficient-preparation circuits must be built from the shared input list;
their costs are NOT unit-cost access to a free database. QFT, clock/observable
preparation, repeated shots and any spectral inference are additional costs.

## 4. Strong classical baselines at the SAME linewidth

### Exact sampler in the commuting secular model

For H_z=sum_i delta_i S_i^z+sum_edges J_ij S_i^zS_j^z, the above raising spectrum
has this exact classical sampler: choose i uniformly, draw independent signs
s_j in {-1,+1} for its neighbors, and output

$$
\omega=\delta_i+\tfrac12\sum_{j\ne i}J_{ij}s_j.
$$

Then add a classical Cauchy draw and bin. This follows by summing equally weighted
single-spin-raising transitions in the product eigenbasis. It costs O(deg(i))
after reading the coefficients, rather than enumerating 2^n energies. The secular
model is not automatically accurate for a strongly coupled full Hamiltonian.
Its validity must be assessed at the required linewidth, not presumed.

### A resolution-dependent certificate for deleting couplings

For any self-adjoint A,B and the same unit vector v, let p_A,p_B be their spectral
laws convolved with ell_gamma. The resolvent identity gives

$$
\boxed{d_{\rm TV}(p_A,p_B)\leq\min\{1,\|A-B\|/(2\gamma)\}.}
$$

Proof: write p_A(omega)=-Im<v,(omega+i gamma-A)^(-1)v>/pi. Bound the difference
by ||A-B|| ||R_A^dagger v|| ||R_B v||/pi. Integrating and applying Cauchy-Schwarz
uses integral ||R_A^dagger v||^2 d omega=pi/gamma, and likewise for B. The additional
factor 1/2 is the definition of TV. No commutativity or dimension assumption enters.

For L_H-L_H', its norm is the spectral diameter of H-H'. A deleted isotropic pair
term J Si.Sj has spectral diameter |J|. If J_cut=sum_deleted |J_ij|, then

$$
d_{\rm TV}(p_{H,\gamma},p_{H',\gamma})\leq J_{\rm cut}/(2\gamma).
$$

Suppose a supplied partition cuts the graph into components of size at most k.
For H' with those edges removed, tracelessness of the local raising operators
makes cross-component correlations vanish. Its normalized spectrum is EXACTLY
the mixture of component spectra, with weight n_c/n for a component of n_c spins.
Each small component can be diagonalized classically once and then sampled.
A simple preprocessing upper bound is sum_c O(8^{n_c}); it is not the best possible
classical bound. Finding a favorable partition also counts; an optimal cut oracle
is not granted. If J_cut<=2 gamma epsilon, this construction meets the requested
TV tolerance. The certificate is conservative; failure does not prove hardness.

### Exact symmetry and an observable-specific broadening bound

Isotropic exchange commutes with total raising O. If every centered delta_i=0,
[H,O]=0 for ANY graph and ANY J_ij: the transition law is a point mass at zero.
The spectrum is simply ell_gamma. Large connected spin count can thus coexist
with a trivial collective spectrum. This statement is about uniform homonuclear
detection, not every local observable or heteronuclear/zero-field experiment.

More generally, put sigma_delta^2=(1/n)sum delta_i^2. The first four moments of
UNBROADENED mu_H obey

$$
m_1=0,\quad m_2=\sigma_\delta^2,\quad
m_3=\frac1n\sum_i\delta_i^3,\quad
m_4=\frac1n\sum_i\delta_i^4+
\frac1{2n}\sum_{i<j}J_{ij}^2(\delta_i-\delta_j)^2.
$$

Proof: m_k=<O,L^k O>/||O||_F^2. Exchange annihilates O;
L O=sum_i delta_i Si^+. Next,
L^2 O=sum_i delta_i^2 Si^+ + sum_edges J_ij(delta_i-delta_j)
(Si^+ Sj^z-Si^z Sj^+). Distinct one- and two-site strings are Hilbert-Schmidt
orthogonal. The norm of each pair difference is D/4, versus ||O||_F^2=Dn/2.
This gives the displayed coefficient. Spectral-moment methods are longstanding
magnetic-resonance tools [10,11]; no novelty is assigned to using them here.
These finite moments are NOT moments of the Cauchy-broadened law, which has heavy
tails and does not have an ordinary second or fourth moment.

A useful consequence that already respects the requested linewidth is

$$
\boxed{d_{\rm TV}(p_{H,\gamma},\ell_\gamma)
\leq\min\{1,\frac{3\sqrt3}{8\pi}\frac{\sigma_\delta^2}{\gamma^2}\}.}
$$

For any mean-zero law, Taylor expansion of ell_gamma(x-omega) cancels the linear
term on averaging. The remaining L1 norm is at most (m2/2)||ell_gamma''||_1;
||ell_gamma''||_1=3sqrt(3)/(2pi gamma^2). Divide by two for TV. This is a sufficient
one-line approximation criterion, independent of n and J. It does not say that
small m2 determines a sharp spectrum, or that a large fourth moment proves
classical difficulty or a detectable effect at coarse resolution.

### Two-spin check: weak coupling also depends on linewidth

For two offsets +/-Delta/2 and one J, define R=sqrt(Delta^2+J^2). Exact frequencies
are +/-(R-J)/2 with weight (1+J/R)/4 each and +/-(R+J)/2 with weight (1-J/R)/4 each.
For Delta>|J| the secular frequencies replace R by Delta and have equal weights.
Coupling the four labels, then bounding Cauchy translations, gives

$$
d_{\rm TV}(p_H,p_{H_z})\leq
\frac{|J|}{2R}+\frac{R-\Delta}{2\pi\gamma}.
$$

The first term is the categorical weight difference; the second uses a frequency
shift (R-Delta)/2 and TV(ell_gamma(.),ell_gamma(.-a))<=|a|/(pi gamma).
Thus Delta much larger than |J| is not alone a quantitative accuracy certificate
at arbitrarily fine linewidth. This solvable pair is a structural check, not a
hard instance, a workload, or a many-spin perturbation theorem.

## 5. What remains genuinely open

The working regime is an inhomogeneous interacting spin network whose required
response cannot be approximated by the commuting model, a symmetry-protected line,
or small separated components at the permitted error. Such failure is only an
entry criterion. Restricted-state, Krylov, cluster, tensor-network, learned-library
and direct-inference methods can still succeed [4-6]. A large fourth moment,
large connected component or operator entanglement is not an all-classical lower
bound. Strong-coupling inference is an independently studied NMR issue [12], not
an invention to accommodate this model.

**Next mathematical question:** on one bounded-degree, physically motivated
coupling family, compare observable-specific classical truncation at time
T~gamma^(-1) log(1/epsilon) with the explicit quantum sampler. Bound the error in
the BROADENED spectrum or its declared bins, not the full many-body state at all
times. A useful advance could be a certified classical reduction or a supported
regime where the quantum representation retains an advantage over the strongest
identified reductions. Neither outcome is assumed. Establish the mechanism before
choosing a molecule, downloading a new trace or building a simulator.

The climate mechanism remains open; its data-dependent diagnostic remains separate.
No new repository, manuscript or third classical spin-off follows from this note.

## 6. Executed checks and limits

`python experiments/spectral_structure_v1/verify.py` requires Python 3.10+ and NumPy.
It was run twice with identical JSON, with BLAS restricted to one thread; -O/-OO
refusals were checked. Five fixed models with at most four spins check observable-state preparation, moments,
secular laws, cut and coarse-line bounds. A disconnected example checks the mixture
rule; a complex Hamiltonian detects the incorrect missing transpose. Four two-spin
choices at two linewidths check the exact line formula and applicable weak-coupling
bound. Three finite geometric clocks check product preparation, Fourier output,
dithering normalization and truncation; a uniform-clock negative control fails the
intended kernel match. Six scalar Cauchy-tail checks verify the alias bound.

These are double-precision mathematical diagnostics (tolerance 2e-10), not exact-
arithmetic proofs, experimental spectra, a climate model, a compiled circuit, or a
performance comparison. Continuous-TV claims follow from the proofs, not from
finite bins or quadrature. No source code or datasets were imported. No older
scientific verifier was rerun; existing sources/reports are unchanged.

Checker SHA256: `9d2d308ed2eb832dd450393eba5bb52a501a7fbea4323d70e4a500dd9c0146c8`.
Report SHA256: `ad8717368b826db5461e5082509780a43615286daf146e607ad8fa54f34cc8b9`.

## Primary sources and inspection scope

Sources checked 28 September 2026. This is not an exhaustive novelty audit.
The proofs above specify what is internally derived; sources establish model,
algorithm and comparator precedents, not independent validation of those proofs.
PDF text from [1-3] was read. Web screenshots of the relevant pages failed; no
figure/table-derived numerical data were used. Other entries were inspected through
primary abstracts, publisher text or institutional author records as stated below.

[1] Joseph, Koopman-von Neumann Approach to Quantum Simulation of Nonlinear Classical
Dynamics, PR Research 2, 043102 (2020). Representation and Monte Carlo comparison.
https://arxiv.org/abs/2003.09980

[2] Sels and Demler, Quantum generative model for sampling many-body spectral
functions, PRB 103, 014301 (2021). Algorithm, linewidth and preparation passages.
https://arxiv.org/abs/1910.14213

[3] Sels et al., Quantum approximate Bayesian computation for NMR model inference,
Nature Machine Intelligence 2, 396-402 (2020). Model Eqs. (1)-(4), not benchmark
reproduction. Axes rotated relative to that paper; all pair sums here are i<j.
https://arxiv.org/abs/1910.14221

[4] Dashti et al., Spin System Modeling of NMR Spectra for Applications in
Metabolomics and Small Molecule Screening, Analytical Chemistry 89, 12201 (2017).
Primary abstract, model-input and application passages.
https://doi.org/10.1021/acs.analchem.7b02884

[5] Edwards et al., Quantum mechanical NMR simulation algorithm for protein-size
spin systems, JMR 243, 107 (2014). Classical restricted-space method; abstract.
https://doi.org/10.1016/j.jmr.2014.04.002

[6] Savostyanov et al., Exact NMR simulation of protein-size spin systems using
tensor train formalism, PRB 90, 085139 (2014). Primary abstract/comparison scope.
https://arxiv.org/abs/1402.4516

[7] Sakuma et al., Entanglement-assisted phase-estimation algorithm for calculating
dynamical response functions, PRA 110, 022618 (2024). Primary abstract on kernels.
https://arxiv.org/abs/2404.19554

[8] Patel et al., Optimal Coherent Quantum Phase Estimation Via Tapering,
PRX Quantum 7, 020302 (2026). Published 2 April 2026; publisher/arXiv abstract.
This establishes windowing precedent, not optimality of the exponential clock.
https://doi.org/10.1103/l5y6-6zxv
https://arxiv.org/abs/2403.18927

[9] Low and Chuang, Hamiltonian Simulation by Qubitization, Quantum 3, 163 (2019).
Primary abstract and input-oracle contract; no resource instantiation.
https://quantum-journal.org/papers/q-2019-07-12-163/

[10] Van Vleck, The Dipolar Broadening of Magnetic Resonance Lines in Crystals,
Physical Review 74, 1168 (1948). Primary abstract; spectral-moment precedent only.
https://doi.org/10.1103/PhysRev.74.1168

[11] Kubo and Tomita, A General Theory of Magnetic Resonance Absorption,
JPSJ 9, 888 (1954). Primary abstract on correlations, moments and exchange narrowing.
https://doi.org/10.1143/JPSJ.9.888

[12] Neural net analysis of NMR spectra from strongly-coupled spin systems,
JMR (2024), 107792. Primary abstract: strong-coupling parameter inference and
experimental limitations; not a classical runtime bound.
https://doi.org/10.1016/j.jmr.2024.107792
