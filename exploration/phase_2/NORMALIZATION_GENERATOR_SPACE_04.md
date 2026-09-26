# Probability volume: use the generator's choices, not an uninformed output space

26 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.
This is a mechanism audit and an exact interface sketch, not a new quantum
algorithm, trained language model, useful mixing result, or novelty claim.
It follows NORMALIZATION_CLASSICAL_GENERATION_03.md without restricting the
broader search to language models, MCMC, or physical prediction.

## 1. Two consequences of unitarity pull in different directions

The paired-U proposal from the preceding note is symmetric and doubly
stochastic. More generally any measured fixed unitary has both column and row
normalization. Let q(y|x)=|U_yx|^2 and let G be a set of k desired outputs out
of N labels. For a uniformly chosen input outside G,

    Pr(proposal lands in G) = sum_(x notin G,y in G) q(y|x)/(N-k)
                            <= k/(N-k).

The bound holds for every fixed U, including target-dependent circuits, and
for mixtures of them with input-independent mixture weights. It does not
apply unchanged to state-adaptive choices of different circuits. Such choices
need their own valid balance condition. The bound counts proposals, not gates.
It says nothing about a carefully chosen particular starting state.

A stronger obstruction for the previous symmetric-proposal architecture is
visible in a two-level target. Give each label in G weight N-k and every other
label weight k, with 1<=k<N/2. Each region has stationary mass one half. For
symmetric q and the Metropolis rule, its ordinary reversible spectral gap obeys

    gap <= 2 sum_(x in G,y notin G) q(y|x)/(N-k) <= 2k/(N-k).

Proof: use the indicator of G in the Rayleigh quotient. Stationary cross-flow
is sum q/(2(N-k)) and the indicator variance is 1/4. Lazifying cannot improve
this bound. Irreducibility is required for a mixing interpretation; a reducible
chain simply has zero gap. This is a specialized elementary derivation of the
unital-proposal bottleneck studied by Orfi and Sels [1], not a new lower bound
against general quantum computation or every classical/quantum sampler.

The example can be classically trivial when G is known. Its role is to expose
an architectural limitation: high desired probability need not correspond to
large counting volume. A correct target-ratio accept/reject rule cannot by
itself make any symmetric proposal a good concentrator.

## 2. There is no contradiction with amplitude amplification

A uniformly random classical basis input is rho=I/N. Every U leaves it invariant.
The coherent uniform state |+><+| has the same initial basis-measurement
probabilities, but it is a different density operator. Target-dependent
interference can concentrate that pure state. Grover/amplitude amplification
already establishes this [2]. Starting every proposal from the current measured
label is not the same computation as maintaining coherent search across
iterations. No general claim against quantum state preparation or learned
Born distributions follows from Section 1.

A small check uses the SAME three Grover iterations on a 16-label problem.
The coherent input reaches the marked label with probability 0.9613189697;
the uniformly mixed input remains at 1/16. This is a known-mechanism control,
not a proposed algorithm, hardware execution, or application advantage.

## 3. Let a classical generator define probability volume

Instead of treating all possible finished objects as equally sized basis labels,
retain a fixed classical generator g. Write every random choice as part of a
finite uniform tape z in {0,1}^b. Conditional on z and fixed context, the generator
is deterministic and returns x=g(z). Its ACTUAL output distribution is

    p0(x) = |{z:g(z)=x}|/2^b.

No assumption is made that this number can be computed efficiently. Replaying g
must be possible at its declared classical cost. The tape must include all random
choices, a fixed length/termination convention, and any padding. A short PRNG
seed does not inherit the ideal independent-randomness distribution by assertion;
then p0 is the distribution induced by that specific finite generator instead.

Suppose the desired distribution is a reweighting of this reference:

    pi(x) = p0(x) s(x)/Z,   Z=sum_x p0(x)s(x)>0,

where s is a known, finite, nonnegative score. Examples include a likelihood,
a reward multiplier, or an indicator of a global constraint. This specifies a
sampling objective, not a claim that s is truth or that exact sampling is needed
by every application. Support outside p0 cannot be created by this interface.

The target on random tapes is simply

    nu(z) = s(g(z))/(2^b Z).

Summing over the tapes yielding x gives exactly pi(x). The generator's prior
is already present in the number of tapes yielding x; multiplying by p0 AGAIN
would give the wrong output law proportional to p0(x)^2 s(x).

This is a discrete lifted representation of a standard idea, not a new principle.
Primary-sample-space Metropolis light transport [3] performs MCMC over a
renderer's random numbers. Probabilistic-program inference [4] operates over
execution-trace random choices. These are direct classical precedents even
though their application domains differ from language generation.

## 4. A quantum proposal can operate only on this tape

Keep the actual chain state z, not only its output x. Prepare |z>, apply either
a fixed V or V^dagger with equal classical probability, and measure z'. Its
proposal is symmetric. Evaluate x'=g(z') classically and accept with

    min(1, s(x')/s(x)).

Start with s(x)>0 and reject zero-score proposals. Irreducibility and aperiodicity
on the positive support still need establishing (or a suitable mixture with a
full-support classical move). Detailed balance on tapes gives the correct output
marginal above after convergence. The output process need not itself be Markov:
forgetting z and assigning an arbitrary replacement tape can change the chain.

Neither p0 nor the quantum proposal point probabilities are needed. In particular
g is NOT run coherently in this architecture. This is not a free coherent LLM
oracle, an encoder of the model weights into amplitudes, or a claim of rapid
mixing. The quantum subroutine proposes random choices; the classical generator
translates those choices into objects and the classical score evaluates them.

For a block update, fixing the tape outside the block and using the same V for
both directions is safe. Arbitrary current-state-dependent proposal training or
selection is not automatically safe. Different encodings of identical p0 can
induce very different neighborhoods, so p0 alone says little about mixing.
A variable-length or dynamically allocated trace requires further bookkeeping;
it is not implemented by silently applying the fixed-b formula.

## 5. What improves, and what remains unresolved

This interface preserves the structure the classical generator already knows.
A set C can be tiny among all raw strings yet have substantial probability
p0(C); its tape preimage occupies exactly fraction p0(C). Such a reparameterization
can remove an artificial raw-string-volume penalty. Classical methods get the
same improvement; it is not quantum advantage.

It does NOT solve rare conditioning for free. If p0(C) is tiny, its tape preimage
is tiny. The normalization restriction reappears there. Warm-start mixing within
valid tapes is a separate problem from finding the first valid tape. A cheap
score correction also does not imply a cheap transition between relevant modes.

The key unresolved design question is where V obtains useful knowledge of the
tape-to-output map. A generic bit mixer may destroy the coherent revisions we
want. A trained/probabilistic-program-specific circuit may be costly to construct.
The same structure might permit efficient classical block proposals, caching,
learned moves or a direct constraint solver. Incremental classical replay is a
real comparator, not a full-model-recomputation assumption [5].

A bound such as (setup + proposals times circuit/replay/score cost) must count
burn-in, autocorrelation, failed moves, training, finite precision and output
quality. A short output is not a small tape or a small circuit. Nothing here
establishes a bottleneck that interference resolves more cheaply.

Coherent amplification of successful tapes is a different architecture: the
reflection/check must coherently evaluate enough of s composed with g. Classical
scoring at the end of measured proposals does not provide that oracle. Whether
a SMALL sufficient coherent interface exists is a concrete remaining possibility,
not an established trick for avoiding the generator's cost.

## 6. A current prior-art route back to reusable classical outputs

Nakano, Okada and Fujii [6] train a classical generative neural sampler on QAOA
samples, then use its explicitly evaluable density in classical Metropolis
sampling. The eventual chain uses the learned classical proposal, not the exact
quantum proposal with a guessed probability. Published comparisons are to stated
baselines, including uniform proposals, not every strongest classical algorithm.

This is close to the original discovery-and-reuse architecture and must not be
rediscovered as our novelty. Our tape sketch uses a pre-existing classical
generator and proposes changes to its random choices; [6] instead learns a
classical generator from quantum samples. They are different allocations of
work. Neither one by itself supplies an end-to-end advantage for an LLM.

Approximate classical simulation need not reproduce a quantum proposal exactly
to provide equally useful moves; the tensor-network results of Christmann et al.
[7] are a direct warning. No conclusions about all target distributions follow.

## 7. Calculation actually performed

A NumPy-only diagnostic checks the capacity/Rayleigh inequalities for 72 dense
small unitaries; it verifies the exact 2/N gap of the uniform-proposal singleton
example for N=8,16,32,64. No asymptotic runtime evidence follows from this check.
The coherent-versus-mixed 16-label control is described above.

An explicit 16-tape generator produces four abstract objects with multiplicities
(8,4,2,2). Scores (1,3,2,6) give the exact output target

    (2/9, 1/3, 1/9, 1/3).

Multiplying the prior into the tape weight a second time instead gives

    (4/9, 1/3, 1/18, 1/6),

at total variation 2/9 from the target. Exact fractions check these laws. Twelve
arbitrary paired-unitary proposals check stationary tape laws numerically; the
largest residual is 2.78e-17. No useful V, language model, program benchmark,
learned representation, hardware, or quantum runtime advantage was evaluated.

Run to a new path (existing reports are not overwritten):

    OPENBLAS_NUM_THREADS=1 python exploration/phase_2/generator_space_check.py \
      --output /tmp/generator-space-observations.json

Recorded environment: NumPy 2.3.5, seed 2026092604. Floating-point records are
observations, not portable exact fixtures. No historical verifier was rerun.

## 8. Decision

Retain a design question, not a new fixed application: can a classical generator
expose a small space of consequential choices in which an explicit quantum
operation supplies better transitions than strong classical inference?

The shared central insight is that useful probability volume should come from
the model, not from counting arbitrary strings. The remaining quantum question
is information about relations between those choices, not normalization alone.
Do not build an LLM integration merely to demonstrate that the stationary-law
identity holds. Do not claim a novel MCMC principle, automatic quantum speedup,
or a compact coherent generator. Manuscript remains on hold.

## Primary sources and inspection scope

[1] A. Orfi and D. Sels, Bounding the speedup of the quantum-enhanced Markov-chain
Monte Carlo algorithm, PRA 110, 052414 (2024).
https://doi.org/10.1103/PhysRevA.110.052414 ; https://arxiv.org/abs/2403.03087 .
Publisher abstract and HTML v1 mathematical discussion read. The nearby paper
PRA 110, 052434 concerns other mixing barriers; these are not the same paper.

[2] L. Grover, A fast quantum mechanical algorithm for database search (1996),
https://arxiv.org/abs/quant-ph/9605043 ; G. Brassard et al., Quantum Amplitude
Amplification and Estimation (2000), https://arxiv.org/abs/quant-ph/0005055 .
Primary abstract/theorem scope checked; the 16-label calculation is independent.

[3] C. Kelemen et al., A Simple and Robust Mutation Strategy for the Metropolis
Light Transport Algorithm, Computer Graphics Forum 21(3),531-540 (2002).
https://doi.org/10.1111/1467-8659.t01-1-00703 . Publisher abstract inspected;
no renderer was executed. Its random-number-space formulation is prior art.

[4] D. Wingate, A. Stuhlmueller, N. Goodman, Lightweight Implementations of
Probabilistic Programming Languages Via Transformational Compilation (2011).
https://proceedings.mlr.press/v15/wingate11a.html . Primary abstract inspected.

[5] D. Ritchie, A. Stuhlmuller, N. Goodman, C3: Lightweight Incrementalized MCMC
for Probabilistic Programs using Continuations and Callsite Caching (2016).
https://proceedings.mlr.press/v51/ritchie16.html . Primary abstract inspected;
no performance number is transferred to our task and no native run occurred.

[6] Y. Nakano, K. N. Okada, K. Fujii, Neural-Network-Assisted Monte Carlo Sampling
Trained by Quantum Approximate Optimization Algorithm, PRX Quantum 7,010338,
24 February 2026. https://doi.org/10.1103/9nhx-5pym ;
https://arxiv.org/abs/2506.01335 . Published metadata/abstract and HTML v1 method
inspected. No experiment or training-cost comparison reproduced.

[7] J. Christmann et al., From quantum-enhanced to quantum-inspired Monte Carlo,
PRA 111,042615 (2025), https://arxiv.org/html/2411.17821v2 . Primary text checked;
no native solver or plots reproduced. This remains a comparator obligation.
