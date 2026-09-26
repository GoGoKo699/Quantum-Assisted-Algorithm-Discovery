# Discover a usable question-and-action policy, not an oracle-valued experiment

26 September 2026. Phase 2; PRX Quantum target; manuscript remains on hold.
Live base read: 5d89bc08e6e66c9267ca31387a4c6f30ab5b657a.
This note is a source-led comparison and exact finite diagnostic. No new quantum
primitive, efficient policy-training algorithm, or useful advantage is claimed.

## 1. A stronger current classical baseline

Action-BED by Rossa, Phillips and Rainforth, first posted on 22 June 2026 [1],
learns an information-gathering policy together with a downstream action policy.
Its objective uses joint forward simulation and task loss rather than explicitly
estimating a posterior for each imagined answer. Its formal policy rearrangement
and its practical parameterized optimization are different claims: neural
training does not certify a global optimum. Its practical gradient construction
requires reparameterizable/differentiable ingredients or suitable likelihood-score
access. The mathematical objective does not itself require differentiability.

This directly strengthens our baseline beyond the previous finite-answer table.
We must not credit a quantum method with removing a nested posterior calculation
that a classical policy-based method can already avoid. The paper also studies
sequential classification from partial image observations, a nonphysical example
of choosing what to reveal and then interpreting it. No training run, quantitative
performance result, or public implementation was reproduced here. The paper is
an explicitly identified preprint, not presented as peer-reviewed validation.

An earlier direct precedent is Hainy et al.'s experimental design through
classification [2]: classify simulated observations by their generating models
and optimize the resulting discrimination performance. DAD [3] already supplies
reusable classical experimental-design policies. These capabilities belong in the
comparison, not only conventional per-observation Bayesian computation.

## 2. Why the experiment and its decoder must be counted together

For equally likely explanations H=0,1, let p_0^e(y),p_1^e(y) be the distributions
of the ACTUALLY REPORTED answer under experiment e. With 0-1 classification utility,

    V*(e) = (1/2) sum_y max(p_0^e(y),p_1^e(y))
          = (1+TV(p_0^e,p_1^e))/2.

This is the standard Bayes-error/variation identity [4], not a new theorem.
The hypothetical optimal decision rule is d*(y)=argmax_h p_h^e(y). Computing the
value of an experiment is not automatically the same task as providing a cheap
rule that achieves that value. If the desired output is an operational decision,
the cost of constructing and applying the decoder is part of the problem.

For an arbitrary deterministic decoder d, its actual value is

    V(e,d) = (1/2) sum_y p_(d(y))^e(y).

With any fixed tie convention for d*, the exact regret is

    V*(e)-V(e,d) = (1/2) sum_(y:d(y)!=d*(y)) |p_1^e(y)-p_0^e(y)|.

Consequently accurate decisions do not require uniformly accurate posterior
probabilities. Mistakes where both explanations have almost identical joint
weight cost little; high-mass strongly discriminating answers matter more.
Conversely, a scalar optimum value is not a deployable decision policy.

Outcome relabeling is a useful easy control. A perfect observation Y=H and
another perfect observation Y=1-H both have V*=1, but applying d(Y)=Y achieves
one and zero respectively. A noisy copy of accuracy 3/4 beats the inverted
observation under that fixed decoder, but not after the decoder is correctly
changed. All of these models are trivially solvable classically. They diagnose
an unfair/incomplete specification, not a quantum application.

## 3. A general forward-rollout formulation

Let alpha map observed histories to the next question, and beta map the final
observed history to the terminal action. Let theta be the hidden situation and
r all simulator randomness. With those two policies fixed, the transcript is

    h_T = Rollout(theta,r;alpha).

The value is a single expectation,

    J(alpha,beta) = E_(theta,r)[u(beta(h_T),theta) - cost(h_T)].

For resource analysis below, take the total payoff to lie in [0,1], or explicitly
rescale a known bounded range. No bound for unbounded utilities is implied.
Optimizing over all allowed measurable policy pairs recovers the corresponding
Bayes-optimal sequential decision problem under the usual existence/measurability
conditions; in our finite controls this is simply enumeration of policy tables.
Restricting policy classes changes the attainable optimum. A trained model's
approximation, optimization error, finite-sample error, and misspecification are
separate issues.

The useful output can therefore be a short executable policy pair: a strategy
for asking and interpreting questions. It can run classically on future cases.
Nothing in the objective requires printing a posterior distribution. This
rearrangement is precisely a direct prior-work obligation from [1]; we do not
claim originality for it or infer cheap global optimization from a single mean.

## 4. The information boundary must survive quantum compilation

During simulated training, theta and r are known internally. A legitimate
policy beta is nevertheless allowed to inspect only the reported history. The
utility routine may use theta to SCORE the decision, but the deployed action
must not depend directly on latent state or unreported simulator randomness.
A coherent evaluation circuit has to preserve this causal/dataflow restriction.

Concrete control: H and R are independent fair bits, and an experiment reports
only Y=H XOR R. Under either H, Y is fair, so V*=1/2. Straightforward coherent
preparations retaining R are

    |psi_0> = (|0,0>+|1,1>)/sqrt(2),
    |psi_1> = (|0,1>+|1,0>)/sqrt(2).

They are orthogonal. Measuring R and Y together identifies H, as does the
classical formula H=R XOR Y. This does NOT mean that the reported Y identifies
H. It means a different observation protocol has been used. Helstrom-style
state discrimination on the retained registers would answer the wrong decision
question. Dephasing/tracing down to the stipulated classical answer gives the
identical distributions again.

This differs from allowing extra COMPUTATION on the same information. A quantum
algorithm may coherently run the entire simulator to estimate a fixed policy's
expected payoff, including latent theta in a reward flag. It must not secretly
change the policy into one with access to hidden truth or turn classical human
answers into coherently supplied states. The toy checks the boundary exactly.

## 5. The classical comparator can couple two complete strategies

Even after fixing the right objective, estimating two strategy values separately
can be wasteful. Given two policies and a valid common source of simulator random
choices z, define their payoffs R0(z),R1(z), and D(z)=R1(z)-R0(z). Then

    E[D] = J1-J0,
    Var(D) = Var(R0)+Var(R1)-2 Cov(R0,R1).

Common random numbers are longstanding classical simulation tools [5]; their
benefit is not universal because the covariance may be negative. An alignment
of random streams that preserves each strategy's marginal execution law must
be supplied. Artificially synchronizing incompatible streams can change the
experiment rather than reduce variance. Classical caching, analytic integration,
learned policies, and source-aware exact solvers remain eligible alternatives.

For binary payoffs, let r=Pr[R0!=R1] and Delta=E[D]. Then

    D in {-1,0,1},    Var(D)=r-Delta^2.

Our explicit 256-scenario control has J0=127/256, J1=129/256, r=1/64 and
Delta=1/128. The variance of a paired difference is 255/16384, versus
16383/32768 from independent payoff evaluations, a ratio 5461/170 (about32.1).
The entire table is known and easy: this is not a measured computational speedup.
A decision tolerance larger than the gap does not justify resolving the winner.

## 6. What coherent computation can legitimately accelerate

An explicit bounded source-level policy rollout can be compiled reversibly:
prepare source randomness, run the question/answer interactions and decision,
compute a bounded reward flag, and uncompute. The policies see only the allowed
history. Simulator arithmetic, data loading, control, workspace, execution length,
and state preparation are all part of its cost. Uniform superposition over a
short pseudorandom seed evaluates that finite seed family, not automatically
the ideal independent-randomness model. A sample-only service or LLM API is not
a coherent circuit specification.

For a fixed policy, ordinary amplitude/mean estimation [6,7] gives the familiar
precision improvement relative to Monte Carlo. It does not by itself find the
policy, prove its optimality, or beat source-aware classical integration. A
useful algorithm must account for how often evaluation is invoked during search
or learning and the error tolerance required by actual decision regret.

Both methods may use the paired comparison in Section5. For binary payoffs put
p+=Pr[D=1], p-=Pr[D=-1]; p++p-=r and Delta=p+-p-. The standard amplitude-estimation
error estimate has terms of order sqrt(p)/M+1/M^2. With a valid known upper bound
r_bar>=r, estimating the two probabilities yields error epsilon in Delta with

    O((sqrt(r_bar)/epsilon + 1/sqrt(epsilon)) log(1/delta))

coherent calls as a conservative high-confidence bound. An adaptive bound needs
its own analysis; r is not assumed known for free. Standard classical Bernstein
sampling of D has the sufficient count

    O((r_bar/epsilon^2 + 1/epsilon) log(1/delta)).

These are standard estimator upper bounds applied to paired payoffs, not new
quantum lower bounds or end-to-end advantages. They explicitly preserve the
classical variance reduction. If C and Q are the full classical/coherent paired
rollout costs, a prospective win must compare C times the classical count with
Q times the quantum count, plus differing setup costs. They are not equivalent
unit-cost oracles. Neither side should demand epsilon much smaller than the
application's acceptable regret merely to display a favorable asymptotic ratio.

Training gradients, policy-class search and accessible useful joint changes
remain separate possible bottlenecks. A faster estimate of one known policy is
not an algorithm that discovers a better policy. A large latent state space or
answer space does not by itself imply that a good policy is hard to find.

## 7. Exact checks and current decision

The standard-library script checks all1225 pairs of four-outcome distributions
with denominator4, enumerating16 decoders per pair. It verifies the Bayes/TV
identity and19600 decision-regret equalities, plus nuisance-output invariance.
It checks128 complete two-step design/action policies against an independent
history-conditioned evaluation, the hidden-randomness information control,
relabeling controls, and the paired-variance example. All comparisons are exact
fractions. The models are intentionally small/easy and do not supply a useful
hard instance. Repeated execution reproduces the JSON bytes.

    python exploration/phase_2/decision_policy_check.py --output /tmp/policy-result.json

Source code of BOSMOS was initially located, but its directory layout did not
match an initial guessed file path; no BOSMOS model was executed. This pass then
prioritized the newly located Action-BED primary paper and classification-design
literature. No native policy-training run, quantum circuit compilation, hardware,
or historical long verifier was run. There is no new benchmark timing claim.

Retain the correlated-uncertainty direction, with a more demanding accepted
output: an executable question-and-action policy whose information access and
end-to-end regret are explicit. Do not turn a scalar Bayes-optimal experiment
value into a usefulness claim while granting the eventual decoder for free.
Next identify a compact policy family with an independently needed joint query
and a documented classical training/comparison bottleneck. The strongest
classical competitor must be allowed to learn the policy directly rather than
reconstruct the posterior. This is not a commitment to a neural architecture,
a new problem category, or a promise of speedup. Manuscript work stays on hold.

## References and inspection scope

[1] T. Rossa, A. Phillips, T. Rainforth, Action-BED: Task-Driven Bayesian
Experimental Design with Singly Intractable Objectives, arXiv:2606.23662v1,
22 June2026. Full HTML Sections3,4,6 and regularity appendix inspected. No
numerical training claims reproduced. https://arxiv.org/html/2606.23662v1

[2] M. Hainy, D. J. Price, O. Restif, C. Drovandi, Optimal Bayesian design for
model discrimination via classification, Statistics and Computing32,25 (2022),
DOI10.1007/s11222-022-10078-2. Publisher method text inspected; no experiment run.
https://link.springer.com/article/10.1007/s11222-022-10078-2

[3] A. Foster et al., Deep Adaptive Design: Amortizing Sequential Bayesian
Experimental Design, ICML2021. Primary proceedings abstract inspected.
https://proceedings.mlr.press/v139/foster21a.html

[4] F. Nielsen, Generalized Bhattacharyya and Chernoff upper bounds on Bayes error
using quasi-arithmetic means, arXiv:1401.4788 (2014). Abstract inspected for
Bayes risk/variation scope; the finite identity above is independently derived.
https://arxiv.org/abs/1401.4788

[5] R. D. Wright, T. E. Ramsay Jr., On the Effectiveness of Common Random Numbers,
Management Science25(7),649-656 (1979), DOI10.1287/mnsc.25.7.649.
Primary abstract explicitly includes counterexamples to universal variance
reduction. https://pubsonline.informs.org/doi/10.1287/mnsc.25.7.649

[6] G. Brassard et al., Quantum Amplitude Amplification and Estimation,
quant-ph/0005055 (2000/2002). Established amplitude-estimation bound; no new
query theorem claimed. https://arxiv.org/abs/quant-ph/0005055

[7] A. Montanaro, Quantum speedup of Monte Carlo methods, arXiv:1504.06987v3
(2017 correction of2015 work). Primary abstract/version checked.
https://arxiv.org/abs/1504.06987
