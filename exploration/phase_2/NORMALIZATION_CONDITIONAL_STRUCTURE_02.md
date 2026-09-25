# Reverse conditioning: rarity, retained information, and conditional transport

26 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.
This follows NORMALIZATION_REVERSE_INFERENCE_01.md. It is an exploratory
calculation and small classical validation, not a new quantum advantage,
novelty claim, complete resource estimate, or a change to other workstreams.

## 1. The next distinction: rare need not mean informative

Fix the prior to the classical uniform ensemble of basis preparations in a
D-dimensional invariant sector. Let B be a set of r final basis configurations,
with projector Pi_B. Conditioning on B has probability r/D and gives

    p_U(x | B) = <x| U^dagger Pi_B U |x>/r.

The reverse quantum state is rho_B=U^dagger Pi_B U/r. Its basis probabilities
are the desired preparation-label posterior; this is not an unspecified prior
quantum-state reconstruction. Inverse circuit execution and preparation of
Pi_B/r must be implemented, not assumed because r is known [1].

The simple question now is whether p_U is a useful, nontrivial answer. Rarity
alone does not establish that. With U=I the posterior is uniform on B, with
TV distance 1-r/D from the prior, but trivially sampleable classically. With a
complex Hadamard/Fourier U, every transition has probability 1/D and the
posterior is exactly uniform, at the SAME evidence probability r/D.

A second control makes the point independent of the dynamics. Append s idle
maximally mixed spectator bits and also condition their outputs to zero.
The event probability drops by 2^-s, but the posterior on the original system
is unchanged and the spectator posterior is deterministic. Event rarity can
be increased arbitrarily without making the original inference harder.
These observations invalidate rarity as a stand-alone hardness metric; they
do not invalidate the exact rejection-free reverse sampler.

## 2. A calculated fully scrambled reference case

For a diagnostic only, draw U from the complex Haar measure on the whole
invariant sector. B and the preparation basis are fixed independently of U.
This is not a claim that a particular local circuit is Haar random, that a
Haar unitary is cheaply implemented, or that a time-independent Hamiltonian
mixes uniformly across energies. Random-matrix generation is standard [2].

Let Z_x=<x|U^dagger Pi_B U|x>. For 1<=r<D it is Beta(r,D-r), since the squared
moduli of a complex Haar unit vector form a Dirichlet(1,...,1) vector. Hence

    E p_U(x) = 1/D,
    Var p_U(x) = (D-r)/(r D^2 (D+1)).

For q(x)=1/D, the exact mean chi-squared divergence is

    E chi^2(p_U || q) = (D-r)/(r(D+1)).

Cauchy-Schwarz and Jensen therefore imply

    E_U TV(p_U,q) <= (1/2) sqrt((D-r)/(r(D+1))).

For epsilon>0, Markov applied to TV^2 also gives

    Pr_U[TV(p_U,q)>epsilon] <= (D-r)/(4 r(D+1) epsilon^2).

These are ensemble statements, NOT bounds for every U. U=I is an immediate
counterexample to a universal interpretation. Small TV controls all bounded
classical statistics of the initial basis label, not just one-site means.
Relative errors on arbitrarily rare subevents are a different requirement.

One can integrate the same beta distribution exactly. With a=r/D,

    E_U TV(p_U,q) = a^r (1-a)^(D-r) / [r Beta(r,D-r)].

For r=D both distances vanish. The formula follows by integrating
(D/r) E[(Z_x-r/D)_+]. These are elementary Haar-moment consequences, not
claimed new random-matrix results or a publishable theorem on their own.

For n unconstrained qubits with k fixed measured output bits, D=2^n and
r=2^(n-k), so the displayed upper bound is less than 2^[-(n-k)/2]/2.
The unobserved endpoint degrees of freedom average over many rows. A complicated
coherent state can therefore have an almost uniform classical posterior.

For the earlier combinatorial example of 100 sites, 50 particles, and a fully
occupied 20-site patch:

    D = C(100,50),   r = C(80,30),   p(B) = 8.7930362855e-8.

Forward rejection averages 11,372,635.885 trials. But the Haar-reference mean
TV bound from the uniform sector prior is only 5.3085217086e-12. This is
combinatorics plus a reference-ensemble theorem, NOT a 100-site simulation or a
claim about physical relaxation times. Uniform sampling would already be an
excellent approximate conditional sampler for typical unitaries in this
reference ensemble at ordinary fixed additive/TV tolerance.

## 3. Unitarity has not destroyed the quantum information

rho_B has exactly r eigenvalues 1/r, so S(rho_B)=log r and
D(rho_B || I/D)=log(D/r). This is independent of U. The information need not
remain visible in the chosen preparation basis: dephasing gives the classical
posterior, whose relative entropy from uniform can be much smaller.

Thus there is no conflict between conserved quantum entropy and an almost
uninformative classical retrodiction. The event was informative about a
rotated quantum subspace, but need not distinguish many original basis labels.
Changing the requested measurement could expose other information, but would
change the inference task. We cannot demand a harder measurement solely to
rescue a speedup claim.

## 4. Physical reversal supplies a nontrivial classical comparator

If H is real symmetric in the occupation basis and U(t)=exp(-iHt), then
U(t)^T=U(t). Therefore |U_xy|^2=|U_yx|^2. The retrodictive distribution is also

    p_U(x|B) = (1/r) sum_(y in B) |U_xy|^2,

which is the ordinary forward relaxation of the conditioned endpoint ensemble.
For this specific setup, studying how a dense equilibrium fluctuation was
preceded can be done by preparing the dense patch and studying its relaxation.
This does not hold unchanged for arbitrary time-dependent gate sequences,
magnetic phases, or noninvariant priors. General U requires its actual inverse.
Retrodiction and physical reversal are established topics [1].

Classical competitors can use this same conversion; comparison against forward
rejection is inadequate. Free-fermion/quadratic dynamics, tensor-network
relaxation methods, kinetic approximations, hydrodynamics, and tailored
conditional algorithms remain valid alternatives. Additional energy conservation
and locality can preserve information absent from the full-sector Haar model.
No Haar-design time or classical complexity lower bound is asserted.

## 5. A better physical question: fluctuations beyond mean density

A candidate next observable is the distribution of the number of particles
that entered a patch, conditional on its being full at the final time. For a
k-site patch, define Q_patch(x) from the initial preparation label and

    K_fill = k-Q_patch(x).

Reverse endpoint samples give its complete classical distribution and any
specified moments. This uses only the initial preparation and final event;
it does not assign trajectories to unmeasured intermediate particles.
For real H it equals the particle-loss statistics of the initially full patch.

A worthwhile question could be whether the same mean filling can arise from
independent transfer or from correlated groups. Higher moments may separate
physical descriptions whose mean transport agrees. That motivation has direct
precedent: Gopalakrishnan et al. derive distinct full-counting-statistics behavior
for systems sharing hydrodynamics [3]; Rosenberg et al. measured higher moments
of magnetization transfer on a 46-qubit processor and found departures from the
full KPZ interpretation despite related low-order scaling [4]. These are NOT
our proposed conditioned experiment or proofs of classical hardness. In fact,
[3] derives analytical distributions in particular regimes. The turnstile
protocol [5] is explicitly useful in tensor-network simulations as well as
experiments and belongs in the classical comparison.

The candidate must specify a regime and a bounded statistic that is informative
and that strong classical methods do not already supply adequately. We must not
choose high-order tails with unnecessary precision just to generate difficulty.
No chosen local Hamiltonian, time window, tolerance, or missing-data requirement
has yet earned status as a useful-advantage workload.

## 6. Adjacent prior art is a different conditioning problem

The June 2026 preprint Quantum enhanced rare event discovery and sampling [6]
assumes a state-preparation unitary for a distribution and identifies/samples
outcomes below a probability threshold without a supplied list of rare outcomes.
Its task and coherent input-access model differ from our known endpoint event
under an invariant preparation ensemble. Our identity does not outperform or
replace their theorem. In particular, simple endpoint preparation is not free
for an unknown set of rare states. The paper was inspected for scope, not its
complete lower-bound proof or an empirical performance claim.

## 7. Work actually performed

The NumPy-only reverse_inference_structure_check.py computes:

- Identity versus Fourier controls with D=16,r=4: same evidence 1/4; posterior
  TV distances from the uniform prior 3/4 and zero respectively.
- Idle-spectator controls with 0,2,6 spectator bits: unchanged original marginal.
- 1,280 random complex subspaces (eight D,r settings, 160 each), using Gaussian
  QR isometries. The observed TV averages corroborate the exact beta integral.
  These are finite Monte Carlo observations, not proofs or failure certificates.
- Two 10-site, five-particle open-chain Hamiltonians, one quadratic hopping
  model and one adding nearest/next-nearest density interactions. Both include
  specified on-site fields and are real. The entire 252-dimensional sector is
  diagonalized CLASSICALLY. A three-site full patch has r=21 and p(B)=1/12.
  At six times per model, direct Bayesian conditioning and forward relaxation
  agree within 6.7e-17 TV in the recorded run. Charge-transfer probabilities,
  means, variances, and an example conditional covariance are recorded.
- No 100-site evolution: that example uses only integer binomial arithmetic.

Both small local models have energy conservation and finite-size effects, and
must NOT be presented as tending to the Haar reference. All tests are easy
classical controls. No quantum processor, optimized tensor network, native
rare-event algorithm, or quantum resource compilation was run. Historical
verifiers were not rerun in this pass. Seeded floating-point observations are
not guaranteed byte-identical across platforms.

Reproduce with exclusive output creation:

    OPENBLAS_NUM_THREADS=1 python exploration/phase_2/reverse_inference_structure_check.py \
      --output /tmp/new-reverse-structure-observations.json

## 8. Research decision

Retain the inverse-conditioning mechanism, but stop using rare events or generic
scrambling as stand-alone motivation. The useful target is structured,
interference-sensitive conditional information. The strongest next test is
conditional charge-transfer statistics beyond a mean profile, compared with
classical relaxation and full-counting-statistics methods at the same tolerance.
A positive result must come from meaningful remaining dynamics, not the
rejection factor that both directions of a reversible process can avoid.

The slogan remains simple: normalize by preparing the condition and reversing.
Its payoff depends on what that condition lets us learn. This note does not
convert an exploratory mechanism into a manuscript or establish novelty.

## Primary sources and inspected scope

[1] F. Buscemi and V. Scarani, Fluctuation theorems from Bayesian retrodiction,
Phys. Rev. E 103, 052111 (2021), arXiv:2009.02849.
https://arxiv.org/abs/2009.02849 . Abstract/scope revisited; identities above
are derived explicitly rather than asserted as novel.

[2] F. Mezzadri, How to generate random matrices from the classical compact
groups, Notices AMS 54, 592-604 (2007), arXiv:math-ph/0609050.
https://arxiv.org/abs/math-ph/0609050 . Primary method reference for the standard
Gaussian-QR construction; beta moments and the TV calculation are derived above.

[3] S. Gopalakrishnan, A. Morningstar, R. Vasseur, V. Khemani, Distinct universality
classes of diffusive transport from full counting statistics, Phys. Rev. B 109,
024417 (2024), arXiv:2203.09526.
https://arxiv.org/abs/2203.09526 . Primary abstract inspected; no native model run.

[4] E. Rosenberg et al., Dynamics of magnetization at infinite temperature in a
Heisenberg spin chain, Science 384, 48-53 (2024), arXiv:2306.09333.
https://arxiv.org/html/2306.09333v2 ; DOI 10.1126/science.adi7877.
Primary text/abstract inspected for scope; no raw-data reanalysis. This is not
an endorsement of a universally settled transport classification in all regimes.

[5] R. Samajdar, E. McCulloch, V. Khemani, R. Vasseur, S. Gopalakrishnan,
Quantum Turnstiles for Robust Measurement of Full Counting Statistics,
Phys. Rev. Lett. 133, 240403 (2024).
https://doi.org/10.1103/PhysRevLett.133.240403 . Publisher abstract inspected.

[6] N. Guo et al., Quantum enhanced rare event discovery and sampling,
arXiv:2606.06316v1 (4 June 2026).
https://arxiv.org/html/2606.06316v1 . Problem definition and assumptions inspected;
no claim to reproduce its proof or compare implementations.
