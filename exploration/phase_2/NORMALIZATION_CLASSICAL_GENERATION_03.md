# Beyond physical simulation: quantum moves, classical probability models

26 September 2026. Phase 2; PRX Quantum target; manuscript remains on hold.
Author direction: keep the exploration open beyond physical prediction. Language
models illustrate probabilistic computation; they do not define its exclusive scope.

This is an exploratory mechanism note, not a new algorithm or an advantage claim.
It preserves the earlier reverse-conditioning and physics investigations. The
immediate architecture here uses a quantum proposal during sampling; it is NOT
already a one-time quantum discovery followed by entirely classical execution.
That departure from the reusable-artifact route is explicit.

## 1. A classical model can be normalized and still be difficult to condition

For fixed-length strings, an autoregressive model has

    P(x_1,...,x_L | c) = product_t P(x_t | c,x_<t).

Each next-token distribution is normalized; no sum over all complete strings is
needed for ordinary forward generation. Unitarity is not needed to accomplish
that normalization. A different task is drawing complete strings according to

    pi(x) = W(x)/Z,   W(x)=P(x|c) exp(beta R(x)) 1_C(x),
    Z = sum_x W(x),

where R scores a complete string and C is a specified constraint. Beta, R, C,
length/termination and the candidate domain must all be fixed explicitly.
This distribution models a sampling objective; it is not automatically a model
of truth, correctness, or human preference. R and C evaluations have costs.

For a prefix s and constraint event C, let h(s)=Pr_P(C | prefix s). Exact
conditioned generation uses

    P(a | s,C) = P(a|s) h(sa)/h(s).

Checking that some completion is possible is not the same as calculating h.
For a two-token toy with equally likely first tokens A,B and final-validity
probabilities .99,.01, exact conditioning makes A/B probabilities .99/.01.
Masking only impossible continuations leaves .5/.5. This is the distinction
studied in grammar-aligned decoding [1], not a new claim about language models.
GeLaTo [2] and TRACE [3] already exploit tractable probabilistic models to guide
constrained generation. They are legitimate competitors, not methods to exclude.
If approximate biased generation meets the actual requirement, it also competes.

## 2. The prior physical restriction is unnecessary for a proposal mechanism

The preceding reverse-posterior construction required an invariant initial
ensemble. Here the desired target pi can be any nonnegative finite weight model
with a positive total weight. The quantum system need not have pi as an
invariant state: a classical acceptance step imposes the target.

Fix a unitary U on the candidate-label register. Given current x, prepare |x>,
choose U or U^dagger with equal CLASSICAL probability, apply it, and measure y.
The resulting proposal is

    q(y|x) = ( |U_yx|^2 + |U_xy|^2 )/2 = q(x|y).

Unitarity normalizes q. The forward/inverse pairing makes it symmetric. Those
are different properties: a unitary alone only makes the measured kernel doubly
stochastic, not symmetric. This is elementary additive reversibilization, not a
claimed new primitive. It uses one circuit execution per proposal, not both.

For x with W(x)>0, accept y with

    a(x,y)=min(1,W(y)/W(x)),

and otherwise keep x. Reject W(y)=0 proposals. For x!=y,

    pi(x) q(y|x) a(x,y) = q(y|x) min(W(x),W(y))/Z,

which is symmetric in x,y. Thus pi is stationary. No proposal probability and
no target partition function Z needs to be evaluated. Ordinary classical MCMC
already avoids Z; the added opportunity is an efficiently generated quantum
proposal whose point probabilities might be expensive to calculate.

Stationarity does NOT mean an exact independent target sample after one step.
Convergence requires irreducibility and aperiodicity on the positive support;
one can add holding probability and a full-support classical proposal, with
all its cost and potentially bad mixing retained. Hard constraints may split
local neighborhoods or make almost every broad proposal invalid. None of this
is cured by normalization. Exact identities presume ideal implemented circuits
and exact weights; floating-point scores and hardware errors require additional
analysis. No blanket noise robustness is asserted.

The basic use of quantum proposals plus classical Metropolis acceptance is
already the subject of Layden et al. [4]. We do not claim this direction as new.
The paired-U derivation above is a generic algebraic variant, not a completed
prior-art priority audit. Quantum MCMC does not have to represent a physical
system just because its proposals can be described with Hamiltonians.

## 3. A possible nonphysical interface: the language model stays classical

Use a classical model to evaluate W on complete candidate strings or programs.
Let the quantum circuit propose coordinated edits. The circuit may depend on the
fixed prompt, target specification and previously trained parameters, but the
same U must be used for both directions of each proposal relation.

This interface does not require the entire language-model inference to occur in
quantum superposition. It does not grant free coherent access to billions of
model weights. HOWEVER, finding a useful U may itself require costly training
or model queries. Avoiding coherent model evaluation is not a guarantee that an
independently cheap proposal circuit exists.

A safe block version conditions U on the coordinates OUTSIDE the chosen block,
which are identical for x and y. Choose blocks with fixed state-independent
probabilities (or probabilities that are demonstrably identical for the pair).
Then each block kernel has the same symmetry and the same acceptance proof.
Whole-string scoring remains necessary: editing a middle token can change the
likelihood of later tokens. Block choice, vocabulary restriction, reversible
encoding, invalid strings, precision, and classical/quantum communication are
not free. A small block need not cross the relevant global bottleneck.

Choosing a DIFFERENT U_x based on each current full candidate x is not generally
safe. Even if every U_x is its own inverse, q_x(y) need not equal q_y(x). The
script constructs a directed three-cycle from three individually symmetric
swaps. Restore a valid Hastings ratio or derive another stationarity condition
before using state-dependent guidance. Likewise, arbitrary garbage discarded
from an ancillary register can destroy the effective kernel's symmetry. The
simple theorem assumes U on candidate space, or clean ancillas returned to their
fixed state. No postselected renormalization is hidden in the proposal.

Coarse-grained quantum MCMC already studies smaller processors [5]. Our block
observation is not a new small-hardware advantage or a transferable resource
estimate from that paper's examples.

## 4. What would count as the useful quantum contribution?

Not avoiding the target normalizer; classical Metropolis already does that.
Not hard quantum sampling alone; a difficult proposal distribution can be poor
for the target. Not replacing a transformer layer with a circuit. Not faster
mixing than an intentionally weak one-token baseline.

A promising mechanism would move BETWEEN regions of useful candidates using
interference-rich updates, with better end-to-end mixing or time-to-quality
than classical blocked moves, sequential Monte Carlo, tractable surrogate
conditioning, learned proposals, tempering, and problem-specific solvers.
A classical method need not reproduce the quantum proposal; a different,
approximately simulated proposal may work just as well.

This is a substantial objection, not hypothetical: Christmann et al. [6] find
that truncated tensor-network proposal simulations can retain favorable scaling
on their tested spin-glass cases. Orfi and Sels [7] identify limits to mixing and
show that sufficiently ergodic long-time quenches do not supply an advantage in
their analyzed regime. Their conclusions are not universal impossibility
results for every quantum proposal or target distribution.

The real comparison includes preprocessing/training, all classical scoring,
quantum circuit preparation and execution, failed proposals, burn-in,
autocorrelation, parallel resources and the application's required accuracy.
If drawing one useful solution is the real task, do not charge classical methods
for obtaining an unnecessarily exact target distribution or proving optimality.
Acceptance rate alone cannot certify good mixing; a chain can accept moves
within one region forever. Transition probability between relevant regions, or
a matched output-distribution criterion, is the meaningful quantity to test.

## 5. Checks actually performed

normalized_proposal_check.py is a small NumPy algebra diagnostic. It does not
run or train a language model, synthesize a useful quantum circuit, measure
mixing times, or execute quantum hardware.

48 dense random unitaries in dimensions 2,4,8 were tested on 96 nonuniform target
weight vectors, half with zero-weight constraints. Forward/inverse proposals
are symmetric and normalized. Maximum detailed-balance residual was
5.55e-17; maximum stationarity residual 1.11e-16. These are floating-point checks,
not a proof of physical sampler convergence or superiority.

A three-cycle permutation is a unitary but not a symmetric proposal. With target
weights (1,2,4), incorrectly using only W(y)/W(x) yields stationary law
(1/6,1/6,2/3), not (1/7,2/7,4/7). Equal forward/inverse mixing restores the target.
The three-label example can be embedded in a four-label space with a rejected
invalid label; it is used only as an algebraic negative control. Three
state-dependent symmetric swaps reproduce the same invalid directed cycle.

The two-token example is checked exactly using rational arithmetic: local
masking and exact global conditioning differ by total variation .49.

Reproduce to a new file:

    OPENBLAS_NUM_THREADS=1 python exploration/phase_2/normalized_proposal_check.py \
      --output /tmp/new-normalized-proposal-observations.json

The run used NumPy 2.3.5, seed 20260926. Floating-point observations are not
portable byte-identical expectations. The algebra checks are the only new
numerical work. No earlier long benchmark or historical verifier was rerun.

## 6. Next direction, without declaring a new project prematurely

The broadly useful question is whether a quantum device can efficiently propose
coordinated changes to a classical object while a classical model supplies its
weights. Language, program generation and Bayesian inference are possible
consumers. The unitary is an algorithmic tool, not necessarily a model of nature.

The next decisive question is how to construct informative proposals whose
inter-region transitions survive strong classical alternatives and whose cost
is smaller than the computational effort saved. A genuine mechanism must be
identified before claiming a language-model benefit. Do not benchmark random
circuits against single-coordinate updates and present the difference as the
answer. Learning phases or mixing schedules is an additional problem, not a
free ability attributed to unitarity.

Keep this as a candidate alongside the earlier normalization ideas. Manuscript
preparation remains on hold. No global quantum advantage, new MCMC technique,
training result, LLM performance improvement, external contact, paid computation,
or background task has been established or authorized.

## Primary sources checked

[1] K. Park et al., Grammar-Aligned Decoding (2024), arXiv:2405.21047v2.
https://arxiv.org/html/2405.21047v2 . Equations 2-3 and convergence discussion.
[2] H. Zhang et al., Tractable Control for Autoregressive Language Generation,
ICML 2023. https://proceedings.mlr.press/v202/zhang23g.html . Abstract and method scope.
[3] G. Y. Weng et al., TRACE Back from the Future: A Probabilistic Reasoning
Approach to Controllable Language Generation (2025).
https://arxiv.org/abs/2504.18535 . Abstract-level comparison; not executed.
[4] D. Layden et al., Quantum-enhanced Markov chain Monte Carlo, Nature 619,
282-287 (2023). https://doi.org/10.1038/s41586-023-06095-4 ;
https://arxiv.org/abs/2203.12497 . Published result and abstract inspected;
proposal/acceptance equations also checked directly in [6]. No benchmark reproduced.
[5] S. Ferguson and P. Wallden, Quantum-enhanced Markov chain Monte Carlo for
systems larger than a quantum computer, Phys. Rev. Research 7, 013231 (2025).
https://doi.org/10.1103/PhysRevResearch.7.013231 . Method/scope checked, not executed.
[6] J. Christmann et al., From quantum-enhanced to quantum-inspired Monte Carlo,
Phys. Rev. A 111, 042615 (2025). https://arxiv.org/html/2411.17821v2 ;
https://doi.org/10.1103/PhysRevA.111.042615 . Full HTML method/limitations inspected;
no native benchmark or figure/table measurement reproduced.
[7] A. Orfi and D. Sels, Barriers to efficient mixing of quantum-enhanced Markov
chains, Phys. Rev. A 110, 052434 (2024).
https://doi.org/10.1103/PhysRevA.110.052434 . Primary abstract inspected for exact scope.
