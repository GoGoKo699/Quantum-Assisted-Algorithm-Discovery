# Cyclobutanone: isolate the electronic bottleneck without discarding its couplings

25 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.
Additive exploration, not a molecular calculation, new quantum algorithm, or
advantage claim. This follows MICROSCOPIC_BENCHMARK_CYCLOBUTANONE_01.md and does
not replace the collision-record or spectral-record investigations.

## 1. Decision

The next intervention to examine is a reusable *coupled electronic model* in
the region controlling the excited molecule's escape, rather than immediate
full electron-nuclear propagation. This is a testable candidate, not an assertion
that this region alone determines every final product ratio. Nuclear propagation
could still be the dominant irreducible cost after electronic inputs are fixed.

The short statement is: compute the difficult electronic information once,
retain the information needed to move between electronic states, and let the
best adequate classical dynamics method use it. Quantum advantage, if any, must
come from obtaining that information, not from reuse or from choosing a weak
classical propagator.

## 2. What the sources establish

The challenge Perspective [1] identifies a sensitive S2 barrier along a route
from Rydberg to valence character. Static and dynamic electronic correlation,
basis choice and active-space balance affect its description. It recommends
higher-level calculations along the minimum-to-transition-state path, including
CC3 where appropriate, and comparisons of dynamics with common electronic input.
This is evidence for a specific unresolved model question, not classical hardness.

The Janoš et al. prediction [2] has two relaxation routes: ring opening in S2,
and a closed-ring S2/S1 crossing followed by opening in S1. Thus the early escape
problem must not silently replace the final branching problem. The Perspective
also discusses using a common DD-vMCG electronic database for different dynamics
methods, with an explicit warning about trajectories outside its coverage [1].

A wider 2025 benchmark roadmap [3] likewise treats matched electronic inputs,
initialization and observable definitions as necessary for method comparisons.
The controlled comparison below is an implementation of that established agenda,
not a new benchmarking principle. We have not established that nobody has
subsequently completed any particular comparison.

## 3. Why energy curves are not enough: an exact two-state control

Set hbar=1 and Delta>0. On the same prescribed parameter path compare

    H0(t) = Delta Z,
    H1(t) = Delta [cos(omega t) Z + sin(omega t) X].

Both have eigenvalues {-Delta,+Delta} at every time. Choose duration
T=2*pi/omega, so their initial and final Hamiltonians also agree. Start in the
same lower eigenstate, and measure the upper state at the common endpoint.

For H0 the transition probability is zero. Write
R(t)=exp[-i omega t Y/2], so H1(t)=R(t) Delta Z R(t)^dagger. Transforming the
Schroedinger equation, not merely the instantaneous Hamiltonian, gives

    H_rot = Delta Z - (omega/2)Y,
    U1(T)=R(T) exp[-i H_rot T].

Consequently

    P1 = [(omega/2)^2/(Delta^2+(omega/2)^2)]
         * sin^2[T sqrt(Delta^2+(omega/2)^2)].

Taking omega=4 Delta/sqrt(5) gives P1=4/9. Thus identical exact energy curves
and common endpoints allow zero versus 44.4% transfer. This is elementary
rotating-frame physics, not a new result or a cyclobutanone model. It is not
an example of gauge choices producing different physics: H0 and H1 are distinct
physical generators in the same fixed basis. A genuine time-dependent basis
change retains the frame-motion term and leaves physical predictions invariant.

The chemical counterpart is the dependence of transitions on electronic
wavefunctions and their geometric variation, not just their eigenenergies.
Nonadiabatic couplings and their quantum evaluation are established [4]. The
control rejects an inadequate proposed output: a list of accurate energies
cannot alone certify a faithful nonadiabatic dynamical model.

## 4. A concrete reusable classical interface

For geometry samples q_a and k retained orthonormal electronic states at each
sample, define

    V_ij(a)=<phi_i(q_a)|H_el(q_a)|phi_j(q_a)>,
    S_ij(a,b)=<phi_i(q_a)|phi_j(q_b)>.

V is a small coupled electronic matrix. S records the relative electronic
states at neighboring samples, including phases. Magnitudes |S_ij|^2 alone
are not generally enough; interference information cannot be removed by using
an ordinary swap-test magnitude as though it were a complex overlap.

Here is the exact algebraic scope of this interface. For an already discretized
nuclear coordinate basis with kinetic matrix T_ab and parent Hamiltonian
T tensor I + sum_a |a><a| tensor H_el(q_a), project onto |a>|phi_i(q_a)>.
The projected molecular Hamiltonian is

    H_eff[(a,i),(b,j)] = T_ab S_ij(a,b) + delta_ab V_ij(a).

This identity does not assert that the chosen electronic subspace or nuclear
grid approximates the real molecule adequately. It is the matrix of the stated
projection. State truncation, unresolved nuclear modes, quadrature, long-time
coverage and omitted spin sectors require separate convergence checks.

For a nuclear kinetic discretization with sparse fixed stencils, the records
needed for its nonzero links can scale as O(k^2 times number of links). A dense
kinetic matrix can need many more overlaps. Neither a small k nor a short
parameter path proves that the full multidimensional grid is small. A quasi-
diabatic V(q) without its residual derivative couplings is also not automatically
sufficient: a globally strictly diabatic finite basis need not exist.

This use of electronic overlaps has direct prior art in Gu's local diabatic
representation [5]. We do not claim it as a new interface theorem. Arbitrary
local phase/unitary choices are harmless only if all matrices and initial/
observable representations are transformed consistently. One-electron orbital
changes between geometries must also be accounted for when evaluating overlaps.

The practical target could use such records locally, or a validated parametric
coupled Hamiltonian rather than a complete nuclear grid. Which is cheaper and
adequate is an open task-selection question, not a free compression assumption.

## 5. A narrow quantum-mechanism hypothesis

Near a crossing, individual adiabatic eigenstates can change rapidly while a
small group of interacting states can be a more regular object. A candidate
fault-tolerant method would prepare and track that group and measure its coupled
matrix/overlaps, rather than insisting on resolving each nearly degenerate state
individually at every geometry.

This is not a claim that all precision costs disappear. If a relevant k-state
group has a uniform gap to excluded states over the sampled region, one can ask
whether group preparation and tracking costs can depend on that external gap
rather than on the smallest *internal* splitting. Grounded state-preparation
circuits, trial-subspace overlaps, path coverage, matrix-element precision,
nuclear velocity/leakage effects and reconstruction stability must still be
priced. An external electronic gap alone does not guarantee accurate projected
nuclear dynamics. No such resource theorem or favorable cyclobutanone gap has
been established in this note.

Importantly, this direction is not new at the slogan level. Illésová et al. [6]
examine state-average orbital-optimized VQE as a route to a quasi-diabatic block
without subsequent adiabatic-to-diabatic transformation. Their paper studies
formaldimine, distinguishes block diagonalization from eigenstate resolution,
and explains residual orbital/basis issues. It does not supply a tested scalable
fault-tolerant advantage for cyclobutanone. Simply applying this prior method or
renaming a variational output would not be our PRX Quantum contribution.

Likewise, an exact solution of a small chosen active-space Hamiltonian cannot
recover electronic correlation from orbitals excluded from that Hamiltonian.
The active-space and external-correlation treatment must be adequate before
attributing physical significance to quantum numerical precision.

## 6. The discriminating comparison

First freeze a physical preparation, a common region of nuclear configurations,
and the observables: early S2 population decay, transient electronic transfer,
and later product populations are separate quantities. Do not fit the target
experimental lifetimes or yields into the model and then call recovery prediction.

Build two internally consistent electronic descriptions on that region, each
including energies and the required couplings/overlaps. Compare at least a
trajectory-based propagation and a systematically converged wavepacket method
on each description with matched physical preparation. A 2-by-2 comparison can
separate sensitivity to input physics from sensitivity to propagation, while
also displaying their interaction. It is not legitimate to swap only the energy
curves while silently retaining incompatible couplings.

For an initial affordable study, inspect the published minimum, transition-state,
and both crossing-region geometries rather than pretending to fit a global
27-dimensional surface. A converged local electronic benchmark can address the
escape barrier, but not alone determine final yields. A small geometry list is
not guaranteed sufficient; its adequacy must be tested and the region enlarged
if wavepackets/trajectories leave it. Preparation and experimental signal modeling
remain common obligations, not things either competitor gets for free.

The decision rule is practical: if a stronger classical electronic treatment
settles the required prediction at affordable cost, there is no quantum workload
here. If classical propagation is adequate given a genuinely expensive electronic
input, target that input. If competing propagators disagree on a well-converged
common model, investigate dynamics separately. Do not assume a quantum machine
must simulate the full molecule just because the full wavefunction is large.

## 7. Work actually done

Read the challenge Perspective, original-prediction abstract/institution record,
classical local-diabatization paper metadata/abstract, benchmark roadmap, and
quantum coupling/quasi-diabatization papers (the latter full HTML).
Attempted PDF retrieval of the Perspective failed; no PDF table or plotted
value is used as new evidence. No chemistry package, electronic integral build,
active-space convergence calculation, molecular trajectory, or quantum circuit
was run. No performance, novelty, or classical-hardness conclusion follows.

Ran the NumPy-only isospectral_dynamics_check.py. The exact rotating-frame
transition is 4/9, stationary transfer zero. Independent midpoint propagation
converges through 200,800,3200 steps, with final probability discrepancy
2.78e-7. Spectra and common endpoints agree to floating-point precision. The
script tests a genuine basis-change control and creates reports exclusively;
it does not overwrite prior evidence. Results are floating-point observations,
not a portable byte-identical benchmark. Historical verifiers were not rerun.

## Sources

[1] J. Janoš et al., Perspective on a challenge: predicting the photochemistry
of cyclobutanone (2026), Sections 2.2 and 2.3, especially their proposed tests.
https://arxiv.org/html/2604.12749v2 ; DOI 10.1063/5.0338792.

[2] J. Janoš et al., Predicting the photodynamics of cyclobutanone triggered by
a laser pulse at 200 nm and its MeV-UED signals (2024), JCP160,144305.
https://arxiv.org/abs/2402.05801 ; DOI 10.1063/5.0203105.

[3] L. L. E. Cigrang et al., Roadmap for Molecular Benchmarks in Nonadiabatic
Dynamics, JPCA129,7023-7050 (2025). DOI 10.1021/acs.jpca.5c02171.
Publisher abstract/introduction and summary inspected, not native execution.

[4] S. Tamiya, S. Koh, Y. O. Nakagawa, Calculating nonadiabatic couplings and
Berry's phase by variational quantum eigensolvers, PRResearch3,023244 (2021).
https://arxiv.org/abs/2003.01706 ; DOI 10.1103/PhysRevResearch.3.023244.

[5] B. Gu, A Discrete-Variable Local Diabatic Representation of Conical
Intersection Dynamics (2023). DOI 10.1021/acs.jctc.3c00560;
https://arxiv.org/abs/2304.04369. Published abstract and arXiv metadata inspected.

[6] S. Illésová, M. Beseda, S. Yalouz, B. Lasorne, B. Senjean,
Transformation-free generation of a quasi-diabatic representation from the
state-average orbital-optimized variational quantum eigensolver, JCTC21,
5457-5480 (2025). https://arxiv.org/html/2502.18194 ;
DOI 10.1021/acs.jctc.5c00327. Full HTML conceptual discussion inspected.
