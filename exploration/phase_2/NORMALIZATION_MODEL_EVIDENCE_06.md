# Weigh explanations, not merely executions that fit

26 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.
This is a source-led workload audit and exact finite check, not a new quantum
algorithm, native Pluck benchmark, learned model, or advantage claim.

## 1. A real consumer of probabilities

Pluck's PLDI 2025 artifact contains a synthesis experiment over short stochastic
programs. The source distinguishes evaluating the probability of observed
input/output examples from searching program syntax. The MCMC code evaluates
log likelihood, a grammar prior and a proposal correction. It has temperature,
resource limits and approximate evaluation modes; we do not assert that every
configuration implements an exact untempered posterior.

The artifact README explicitly distinguishes inference/evaluation improvements
from downstream synthesis gains, and reports that the approximate method does
not provide the same additional benefit for the synthesis metric. This is an
author-reported qualitative observation, not a benchmark replicated here.

This suggests an interface to investigate: a classical system proposes compact
executable explanations; quantum processing, where justified, helps compare
their probabilities of the data. The final executable model remains classical.
An LLM is a possible proposer, not an oracle whose parameters become coherently
accessible for free. We have not selected a language-model implementation.

For models j, prior w_j, and independent data examples d_i, write

    L_j = product_i Pr[g_j(R_i)=d_i],
    posterior(j) = w_j L_j / sum_k w_k L_k.

Existence of a successful execution does not determine L_j. A model that can
explain anything with a lucky random choice need not be a good explanation.
This likelihood bottleneck is longstanding; Nori et al. [4] already target it
with classical approximations. This is not a newly identified scientific problem.

## 2. What coherent normalization can do, and what it cannot

For one event E and bounded executable generators, prepare

    sum_j sqrt(w_j) |j> A_j|0>,

where measuring the marked event in A_j has probability ell_j. Conditional on
success, measuring j returns w_j ell_j / sum_k w_k ell_k. Standard amplitude
amplification preserves the relative amplitudes within the successful subspace.
It can raise overall success without printing or separately estimating all
ell_j. The latent registers remain present until measurement; summing their
amplitudes as if histories were the same state would give a different law.

This is ordinary quantum rejection inference [5,6], not our invention.
Preparing a separate normalized successful state for EACH model and retaining
the model's old prior does NOT do the same job: that erases the evidence weights.
The earlier context-freezing counterexample becomes directly relevant to model
comparison. Joint normalization must compare explanations together.

The cost includes prior-state preparation, controlled generator execution,
reversible event evaluation and their inverses. An efficiently enumerable small
candidate list can be explicitly compiled, but arbitrary program interpreters,
large learned models, nontermination, and large data access are not free.
Finite independent observations can be handled by a joint event, but its success
probability is a product and may be a particularly poor representation.

For one Bernoulli probability ell at relative accuracy eta, elementary sampling
costs O(1/(eta^2 ell)); suitable amplitude estimation has O(1/(eta sqrt(ell)))
query scaling, up to confidence/adaptation factors [6,7]. These are not end-to-end
classical lower bounds. Exact summation, symbolic simplification, importance
sampling and domain-specific likelihood formulas may all be faster. Approximate
likelihoods must be used with a justified statistical rule; inserting arbitrary
biased estimates into an exact-MCMC acceptance ratio is not automatically exact.

## 3. The first public calibration is classically easy

We inspected task 000 in the artifact's HMM-Gen dataset. Its supplied generating
program simplifies to four deterministic states 1,2,3,4, with an independent
observation at each position j: output j with probability 4/5; otherwise draw a
nonnegative Geometric(1/5) random number. A separate flip of probability .3 has
the same continuation on both branches and can be removed.

For a four-list y the mathematical kernel therefore has likelihood

    ell(y) = product_(j=1)^4 [(4/5) 1_(y_j=j) + (1/25)(4/5)^(y_j)].

This is for the untruncated geometric law, or a cap strictly above the observed
values. The source supports configurable geometric fuel; we have NOT reproduced
its resource-limited evaluation semantics or runtime. The four transcribed
training outputs have maximum value 11, so caps above 11 give these masses.

The four source training examples are [1,3,0,4], [1,2,11,4], [1,2,3,4], and
[1,2,0,7]. Their likelihoods under this kernel are approximately
.0005564264349696, .001926803131039594, .46010345481201254, and
.000230485124972544. Their product is 1.136955571763615e-10.

Matching all four by generating independent datasets would be extremely rare.
Nevertheless, computing this likelihood uses a short product formula. The small
number is not hardness evidence. The known source program is a calibration, not
an unsupplied discovered algorithm. We do not generalize its easy factorization
to the arbitrary higher-order programs or all HMM-labelled tasks in the suite.

An exact Fraction implementation compares the product with summing all 16
copy/noise branch masks on 2600 checks. The geometric branch is analytically
summed in both methods; this is not a full enumeration of infinite executions.
A two-candidate illustration changes only the copy probability to 1/5 or 4/5.
With an explicitly chosen equal prior the latter receives posterior mass
.985832728188817. This is NOT the upstream grammar prior or full synthesis task.
No upstream solver code is copied or run.

## 4. Evidence relevance is different from execution relevance

The preceding coherent-slice result required an event not to depend on deferred
random bits. That is sufficient for the full conditional-output law, but can
be unnecessarily restrictive when the requested output is only a model label.

If every model's likelihood factorizes as

    Pr(d,z | j) = c(z,d) L_j(d),

with the same positive c for every j, the factor cancels from the posterior on j.
It can matter to exact generated-data matching while being irrelevant to which
model is supported. This is ordinary Bayesian factorization, not a new theorem.
It applies to the stated query only; it does not license ignoring correlations
needed to reconstruct the full posterior over execution traces.

In an exact control, two equally likely models have event probabilities 1/16
and 3/16. The posterior is (1/4,3/4). Appending b observed independent fair bits
common to both models multiplies the evidence probability by 2^(-b) but leaves
that posterior unchanged. An unsimplified amplification over exact complete-data
matches would add a needless factor 2^(b/2) in its query count. At b=80 this is
2^40, despite no added inferential difficulty. Both competitors must cancel the
common factor or otherwise exploit the same irrelevance.

This is not a general efficient algorithm for discovering all cancelable
factors. A factorization can itself be difficult to establish. It sharpens the
selection criterion: retain the information that distinguishes the candidate
explanations, not automatically every variable affecting a raw acceptance bit.

## 5. Positive research question and limits

A promising nonphysical job is quantum-assisted evaluation or comparison of
compact stochastic explanations that are inexpensive to execute once but costly
to assign likelihoods to after classical simplification. A successful model can
then run entirely classically on later inputs. This reconnects to the original
reusable-classical-method objective without requiring quantum execution of the
large model that suggested the candidates.

The missing positive case is not established by the Pluck source audit. We need
a surviving likelihood or conditional-sampling kernel, with a clear consumer
accuracy requirement, strong classical evaluation, and affordable controlled
execution. A solution supplied in the dataset cannot count as our discovery.
A better quantum model comparison on a shortlist does not guarantee that the
outer search supplied adequate models or that the resulting model is correct.

Before building an integration, distinguish tasks: finding any satisfying
program, sampling models in proportion to posterior mass, and predicting future
outputs are not interchangeable. For one useful program or an adequate predictive
model, approximate classical inference can be a legitimate competitor. An exact
posterior requirement must not be introduced solely to obstruct it.

Pluck's lazy compilation, caching, locally informed proposals and incremental
search are baseline capabilities. A generic rejection benchmark or a raw trace
count is not sufficient. The next work should inspect a non-factorizing published
kernel and compare the information it needs, rather than append an isolated
quantum oracle to the easy calibration.

## 6. Work and reproducibility

Read the primary Pluck project/artifact descriptions, pinned source and a dataset
excerpt; checked quantum-inference/amplitude-estimation precedents. The research
repository head was read before work. Native Julia and Rust executables were not
available in this environment and outbound container DNS failed, so the complete
Pluck artifact was NOT installed or executed. No full-paper plot or table is used
as newly measured evidence. No runtime speedup, gate resource or quantum hardware
result is reported.

Ran model_evidence_check.py with exact fractions: 2600 source-kernel comparisons,
4064 full-tape nuisance-factor checks, and one known 32-dimensional Grover
control. Its success rises from 1/8 to 25/32 while its model posterior remains
(1/4,3/4). Per-model normalization incorrectly produces (1/2,1/2). These are
algebraic checks, not an advantage benchmark. No older research verifier rerun.

    python exploration/phase_2/model_evidence_check.py --output /tmp/evidence.json

The Python standard library suffices. Existing files are not overwritten.
The manuscript remains on hold. No outside contact, submission, paid computation
or asynchronous work is authorized by this note.

## Primary sources and exact source pointers

[1] Bowers et al., Stochastic Lazy Knowledge Compilation for Inference in Discrete
Probabilistic Programs, PACMPL 9 PLDI,222 (2025), DOI10.1145/3729325.
https://pldi25.sigplan.org/details/pldi-2025-papers/76/Stochastic-Lazy-Knowledge-Compilation-for-Inference-in-Discrete-Probabilistic-Program
https://pluck-lang.github.io/ . Abstract/project description inspected.

[2] pluck-lang/pluck-artifact README.md, blob
73c16232c95e36ef77d82e5566ad3293b7facdfd; synthesis submodule pins
pluck-lang/PluckArtifact.jl at4258adf926055f4e2415c33025ad04da0b5e312d.
Its data/figure5/out/fuzz-datasets/2024-11-13/04-07-50/dataset.json has blob
8dd1275a589e83d9d2df9e95f5ca0de7f4314782. Only task000's mathematical kernel
and four training lists are transcribed; the full dataset was not executed.

[3] Pinned synthesis implementation pluck-lang/Pluck.jl at
472c32e128f03887daf3cfa14046bb30f44f40af: src/search/mcmc.jl blob
ff5ff1299a0f8e3c257f56b1e510fecab1b78929; src/search/tasks.jl blob
36099fff006a9ba9c612012ed4dbf2ad6e65f6e6; src/language/definitions.jl blob
deda196b687042b230b0fca92bd4128b780c3d10. Source excerpts inspected via GitHub.

[4] Nori et al., Efficient Synthesis of Probabilistic Programs, PLDI2015.
https://www.microsoft.com/en-us/research/publication/efficient-synthesis-of-probabilistic-programs/
Author publication summary read. The reported likelihood approximation speedup
is prior-work evidence, not reproduced data or a bound on our tasks.

[5] Low, Yoder, Chuang, Quantum Inference on Bayesian Networks, PRA89,062315
(2014). https://arxiv.org/abs/1402.7359 . Explicitly compiled quantum inference
prior art, not a lower bound against every classical likelihood method.
[6] Brassard et al., Quantum Amplitude Amplification and Estimation (2000/2002).
https://arxiv.org/abs/quant-ph/0005055 . Established primitive, not new mechanism.
[7] Montanaro, Quantum speedup of Monte Carlo methods (2015; corrected v3 2017).
https://arxiv.org/abs/1504.06987 . General estimator comparison, not a claim that
a randomized simulation baseline is optimal on an explicit structured input.
