# Fair coupling audit, then ask which information changes a decision

26 September 2026. Phase 2, PRX Quantum target; manuscript remains on hold.
Base read from the live branch: fb56d459776bda4a5e72b36669a2346fd38cd483.
This is an exploratory derivation and exact finite audit, not a new coupling,
value-of-information, mean-estimation, or quantum-advantage theorem. The user's
fair-comparison requirement governs both positive and negative conclusions.

## 1. Source-aware classical counterpart to the last certificate

Let deterministic finite generators g and h use the same normalized classical
random tape law mu. Consider their phase-free, tape-retaining preparations

    |G> = sum_z sqrt(mu(z)) |z>|g(z)>,
    |H> = sum_z sqrt(mu(z)) |z>|h(z)>.

Private reversible workspace has been uncomputed. Put

    c = Pr_z[g(z)=h(z)],   d=1-c.

The exact coherent return probability is F=c^2. A classical algorithm given
the same source can draw z and evaluate BOTH outputs, obtaining an agreement
Bernoulli of mean c. Drawing two independent tapes and reporting success only
when both pairs agree produces a Bernoulli of mean c^2: it simulates the return
bit's complete distribution, without computing either marginal probability.

The classical coupling inequality gives TV(Law(g),Law(h)) <= d=1-c. Hence in
THIS representation the stronger return bound is TV <= 1-sqrt(F), not just
the generic pure-state bound sqrt(1-F) used in the prior scout.

This means the last scout does NOT provide a dimension-dependent advantage
when the target and replacement are supplied ordinary generators with this
lifting. This is a scope-specific classical simulation of the proposed test,
not a dequantization of general quantum state or distribution testing.

For a fixed candidate, m independent paired runs with no disagreement have
false-certification probability at most (1-tau)^m whenever TV>tau. The refined
return test has bound (1-tau)^(2m). At tau=delta=.05, the sufficient counts are
59 paired classical runs versus 30 coherent return tests. The previous generic
1197-return count is overly conservative in this representation. Comparing
59 with 1197 without improving the quantum analysis would itself be unfair.
Trial counts are not runtime comparisons; both evaluation circuits and quantum
preparation/inversion overhead have to be included.

Neither test is complete for all close OUTPUT distributions. The maps z->z and
z->1-z on a fair bit have the same output law and zero agreement under that
coupling. A source-aware relabeling aligns them immediately. A known efficient
measure-preserving relabeling is available to both competitors. Optimizing an
unknown coupling is not free, and an optimal quantum purification alignment is
not supplied by a closeness promise. Arbitrary phases and quantum-generated
states need separate analysis. This does not contradict the earlier sound
one-sided fidelity certificate.

Couplings as quantitative probabilistic-program proofs have direct prior art
[1]. Structure-aware distribution comparison also includes [2], which reduces
relative TV approximation to inference for same-structure Bayesian networks.
No claim is made that all distribution validation is easy.

## 2. A narrower useful output: the value of a question

Rather than certify every possible later query, suppose the consumer must choose
an observation/test/question before taking an action. Freeze the current belief
p(theta), one proposed experiment e, its conditional outcome law l_e(y|theta),
a finite action set A, and utilities 0<=u(a,theta)<=1. Experiment-dependent
cost c_e is expressed in the same utility scale. The current p may already be
a posterior; obtaining it and a sampler for it are NOT free assumptions.

Without more information, best expected utility is

    V0 = max_a sum_theta p(theta) u(a,theta).

If e is performed and the action may depend on its answer y, the value before
paying for the experiment is

    Ve = sum_y p_e(y) max_a E[u(a,theta) | y,e].

Thus net value of information is Ve-V0-c_e. This is standard decision analysis
and expected value of sample information [3], not a newly defined objective.
It can express model-discriminating tests, diagnostic software checks, or
clarifying questions. These are examples of an interface, not established hard
quantum workloads. Information gain about all nuisance parameters is a different
objective from improvement of a specified decision.

For a finite outcome alphabet, multiply out Bayes' rule:

    J_e(a,y) = sum_theta p(theta) l_e(y|theta) u(a,theta),
    Ve = sum_y max_a J_e(a,y).

The posterior denominator cancels against the probability of receiving y.
Zero-probability answers contribute zero. This is an elementary identity, not a
quantum normalization effect. Crucially, it needs no algorithm sampling a
posterior separately for every possible future answer.

If only forward joint samples (theta,Y) are available, J_e(a,y) is still the
mean of 1_(Y=y) u(a,theta). If explicit l_e is cheap, integrating over Y first
is an allowed classical Rao-Blackwell improvement. Hidden-state input, simulator,
scoring and observation encoding costs stay in both comparisons.

This removes inverse-evidence-probability factors caused by unnecessarily
conditioning on rare answers. It does NOT establish that summing over a huge
or continuous answer space is cheap. Only explicitly finite, tractable outcome
sets are assumed here. The bound depends on output coarsening and its impact
on the decision, not on wishful disregard of rare important outcomes.

## 3. Correlations can change which questions are worth asking

A finite diagnostic has fair independent A,B and decision target H=A XOR B.
All three are individually fair; each pair is independent. A fourth independent
bit N is a nuisance variable. The product model on (H,A,B,N) therefore agrees
on EVERY one- and two-variable marginal.

The action is a binary prediction of H, with utility one for a correct guess.
Without observing anything, the value is 1/2. Observing A alone or B alone still
has value 1/2. Observing BOTH has value one under the true model but only 1/2
under the product approximation. Observing N has zero decision benefit. A noisy
direct report of H with accuracy 3/4 has value 3/4.

Thus discarding a relationship can change which test bundle is preferred,
without changing the single-variable or pairwise uncertainties. This is the
consumer-side consequence we needed to identify. It is NOT classical hardness:
XOR and the tiny decision problem are immediate to solve classically.

The example also distinguishes prospective usefulness from post-hoc correlation
fitting. We fix the decision and observation protocol before evaluating which
information helps it. It does not justify inventing a global parity query in
an unrelated application merely to obstruct a classical approximation.

## 4. The strong finite-outcome classical baseline

With K possible answers and L actions, there are L^K deterministic policies
pi:y->a. For each fixed policy,

    E[u(pi(Y),theta)]

is a mean of bounded iid random variables. The best policy value is exactly Ve.
A joint sample bank estimates ALL policies; a union bound gives

    m >= [K log L + log(2/delta)]/(2 epsilon^2)

as a sufficient count for uniform epsilon payoff error, provided the model,
action set and utilities are fixed independently of that bank. The empirical
optimum differs in value by at most epsilon; its selected policy has regret at
most 2 epsilon. This is a statistical upper bound, not an optimality claim.

No exponential policy enumeration is required: maintain empirical J(a,y), then
choose each answer's best action independently. The same sample contributes to
all actions whose utilities can be evaluated, at O(m L) utility-evaluation work
and O(KL) storage in this elementary implementation. Sparse storage is allowed.
Several proposed experiments may share theta samples, but every necessary
response/utility evaluation is charged. This is stronger than nested rejection
and already ignores the number of hidden configurations in its sample count.
Symbolic integration, graphical structure, variance reduction, quasi-Monte Carlo
and learned policies may be better still. Learned planning is allowed to amortize
its setup over future uses, just as a quantum-designed policy would be [6].

## 5. A legitimate quantum route, not a new speedup theorem

For small fixed K,L and an explicit coherent implementation of the forward
simulator and bounded utility, each J(a,y) can be estimated by standard quantum
mean/amplitude estimation [4]. Estimating all KL entries to error epsilon/K
suffices for |Vhat_e-Ve|<=epsilon. A straightforward nonoptimized query bound is

    O_tilde(L K^2 / epsilon)

against repeated calls to those coherent routines. The initial belief sampler,
conditional data generator, reward flag, precision, controlled operations and
uncomputation must be included in gate cost. A prior supplied only as samples
or an LLM API does NOT give coherent access to its preparation. Expensive current
posterior preparation cannot be deleted by the future-answer cancellation.

For fixed K,L this displays the familiar 1/epsilon versus 1/epsilon^2 precision
comparison with Monte Carlo. It is neither an original algorithm nor an
end-to-end separation against every classical algorithm for an explicit program.
The required epsilon comes from acceptable decision regret or a relevant value
gap, not from selecting tiny tolerances to make a crossover appear. If two tests
are nearly tied, returning either may be adequate. If g has an exact formula,
use it. If a learned policy meets the need more cheaply, it wins.

General nonlinear/nested Monte Carlo already has a strong positive quantum
result: Blanchet, Hamoudi, Szegedy and Wang [5] give a quantum-inside-quantum
algorithm with O_tilde(1/epsilon) scaling under their assumptions, compared with
O_tilde(1/epsilon^2) classical multilevel Monte Carlo. We read version 2, not
version 1's different intermediate comparison. Their access model explicitly
requires source for both the outer sampler and the conditional inner sampler,
with bounded moments and a Lipschitz outer function. For a direct Bayesian
formulation the latter may be the difficult posterior routine itself. The
finite-answer joint formula above is a separate elementary way to avoid THAT
particular conditional routine. It does not extend their theorem for free.

This is a quantum COMPUTATIONAL query-count advantage conditional on the declared
routine implementations, not a claim of reducing the amount of real-world data
needed. Actual human responses or physical experiments cannot be queried in
superposition just because their simulators can. Model misspecification and
calibration remain distinct from Monte Carlo accuracy.

## 6. External motivation without declaring an advantage workload

BOSMOS [7] studies adaptive selection between executable cognitive models when
likelihoods are not tractable. Its public paper uses simulated memory retention,
signal-detection and other behavioral tasks, and reports substantially faster
classical model selection than stated alternatives. Its objective and output
metrics are not identical to our bounded-utility formula. This is evidence of
an existing nonphysical consumer and a baseline to inspect, not a matched
runtime result or a claim that its models need quantum computation.

Deep Adaptive Design [6] and its implicit-model extension [8] learn reusable
classical experiment-selection policies. They are particularly important for
fairness: the classical competitor may move work offline and return a reusable
policy, not repeat an expensive inference task at every query. We have not run
BOSMOS, DAD/iDAD, native Pluck or a current numerical decision-design suite.

A possible research question is whether quantum computation can help calculate
which questions or test bundles lead to better decisions, then compile that
knowledge into a classical policy. The policy-reuse stage is hypothetical here;
it does not follow from producing one Ve estimate. No large policy-training
loop or LLM integration is justified by this note alone.

## 7. Exact calculation and decision

The standard-library script checks all 6561 ordered pairs of three-output
functions on four fair tapes. For every pair it independently executes a
16-dimensional exact return circuit, verifies F=c^2 and TV<=1-c, and simulates
the return bit with two independent classical paired executions (104976 tape
pairs). Of 639 equal-output-law pairs, 90 have zero return probability under
that coupling. Those are incompleteness controls, not failures of soundness.

For all 6560 nonzero weight arrays in {0,1,2}^(2x4), with two payoff tables,
posterior-based decision value equals the unnormalized joint formula and full
enumeration of four deterministic policies: 13120 exact comparisons. There are
160 cases with a zero-probability outcome, checked without dividing by zero.
The parity decision diagnostic checks ten one-/two-variable marginals and the
specified test values. All substantive arithmetic uses exact Fraction values;
only illustrative confidence counts use ordinary logarithms.

The executed checks are semantics and fairness diagnostics. They supply no
quantum runtime, no useful hard instance, no learned model, and no measurement
on hardware. The prior large/historical verifiers were not rerun. Reproduce to
a fresh file with

    python exploration/phase_2/coupling_decision_check.py --output /tmp/new-decision-check.json

Retire the ordinary-generator overlap test as a dimension-based advantage
candidate. Keep general quantum distribution-testing questions open, but do not
claim more than the supplied access allows. Next inspect decision-relevant
inference after the source-aware classical reductions above. The prospective
central sentence is: use quantum computation to determine which uncertainty
is worth resolving, rather than to maintain a needlessly complete posterior.
The manuscript stays on hold; no submission, outside contact or paid work.

## Primary sources and inspected scope

[1] Barthe, Gregoire, Hsu, Strub. Coupling proofs are probabilistic product
programs, POPL 2017, arXiv:1607.03455. Primary abstract and quantitative-program
scope inspected. https://arxiv.org/abs/1607.03455

[2] Bhattacharyya et al. Total Variation Distance Meets Probabilistic Inference,
ICML 2024, arXiv:2309.09134v2. Primary abstract, same-structure and small-treewidth
scope inspected; no implementation run. https://arxiv.org/abs/2309.09134

[3] Hironaka, Giles, Goda, Thom. Multilevel Monte Carlo Estimation of the Expected
Value of Sample Information, SIAM/ASA JUQ 2020; arXiv:1909.00549.
Primary abstract and method scope read. https://doi.org/10.1137/19M1284981

[4] Montanaro. Quantum speedup of Monte Carlo methods, Proc. R. Soc. A (2015),
arXiv:1504.06987v3, corrected 2017. Primary abstract and version inspected.
https://arxiv.org/abs/1504.06987

[5] Blanchet, Hamoudi, Szegedy, Wang. Quantum speedup of non-linear Monte Carlo
problems, NeurIPS 2025, arXiv:2502.05094v2 (22 October 2025). Parsed PDF Sections
1-3, especially Assumptions 1-5 and Theorem 3.2; page 5 visually checked through
the web PDF screenshot. Initial versioned screenshot failed; the unversioned
PDF of v2 rendered successfully. No theorem implementation or experiment run.
https://arxiv.org/pdf/2502.05094
https://proceedings.nips.cc/paper_files/paper/2025/hash/1b12cec51490d59484096f178c0f81be-Abstract-Conference.html

[6] Foster, Ivanova, Malik, Rainforth. Deep Adaptive Design: Amortizing Sequential
Bayesian Experimental Design, ICML 2021. Primary proceedings abstract inspected;
no runtime number or native experiment reproduced.
https://proceedings.mlr.press/v139/foster21a.html

[7] Aushev et al. Online Simulator-Based Experimental Design for Cognitive Model
Selection, Computational Brain & Behavior 6, 719-737 (2023), published
21 September 2023. Primary publisher abstract/method prose inspected;
no table/figure digitization or performance measurements reproduced.
https://doi.org/10.1007/s42113-023-00180-7

[8] Ivanova, Foster, Kleinegesse, Gutmann, Rainforth. Implicit Deep Adaptive Design:
Policy-Based Experimental Design without Likelihoods (2021), arXiv:2111.02329.
Primary abstract inspected. https://arxiv.org/abs/2111.02329
