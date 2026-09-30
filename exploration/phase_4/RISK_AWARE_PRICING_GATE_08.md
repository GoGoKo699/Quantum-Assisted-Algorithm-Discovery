# Risk-aware pricing 08: a source-grounded extension, with a stronger target

30 September 2026. Baseline: `070cfc441903f91fa0ad375539ecf68d6ab1890a`.
Working branch: `research/prx-quantum-phase2`. No assumed QRAM; manuscript on hold.

**Decision:** stop enlarging the ordinary fixed-capacity workload. Retain one
DIFFERENT, independently motivated packing model for a bounded test: allocate
uncertain cloud workloads subject to a declared overload-risk constraint. The
quantum candidate is a coherent, feasible-pattern finder targeted at a published
hybrid-pricing threshold, not simply any score above one. Existing classical
bounds and approximation algorithms must run first. No useful quantum advantage,
new algorithmic primitive, production deployment, or publication priority is shown.

The source gate from Note 07 is met at the level of application motivation and a
published solver bottleneck, not at the level of a verified quantum benefit. The
root model and circuit below are new specifications; they are NOT consequences of
the old single-capacity recurrence or its benchmark. No new repository is needed.

## 1. Why consider uncertainty rather than an artificial larger integer capacity?

Cohen et al. [1] study cloud overcommitment: requested resources can exceed typical
use, but packing jobs too tightly increases overload risk. Their classical model
and workload-based study motivate pooling uncertain demands. We select OFFLINE
allocation/repacking of a supplied batch, not immediate online admission, real-time
service control, or a promised operational cost saving. Data estimation, scheduling
latency, migration restrictions and model validation would all count in deployment.

A source screen also considered conflict packing and crew pairing [7,8]. Both have
independent applications and strong specialized classical algorithms. They are
alternatives, not constraints appended to make our old knapsack difficult, and no
quantum route for them is selected here. Plain one-dimensional pricing remains a
hardware-admissible reference without a demonstrated useful residual regime.

In the risk-pooling model, each job has nonnegative mean a_i and uncertainty weight
b_i. A pattern x is admissible when

$$
A(x)+\sqrt{q S(x)}\leq C,\qquad
A(x)=\sum_i a_i x_i,\quad S(x)=\sum_i b_i x_i,\quad x_i\in\{0,1\}.
$$

C is server capacity, and q>0 specifies the risk buffer. All inputs are classical.
For independent Gaussian demands, b_i is variance and
q=[Phi^{-1}(1-delta)]^2 for delta<1/2 gives an exact single-server chance constraint.
For demands with given means and a diagonal covariance matrix, taking
q=(1-delta)/delta gives a sufficient one-sided moment bound. For example delta=.05
makes q=19 exactly. These are different distributional promises. Neither an
estimated mean nor a Gaussian label establishes them for actual workloads [1].
Bounded-support formulations can instead use the source's Hoeffding construction;
they are not automatically equivalent to the original chance constraint.

The target controls one modeled server-load snapshot. It does not by itself bound
all servers jointly or overload at any time in a long observation horizon. Positive
cross-job covariance, changing demand, and estimation uncertainty need accounting.
We do not add independence simply because it favors a quantum construction. Both
classical and quantum methods use the SAME validated coefficient model.

The master minimizes the number of servers covering the jobs, with admissible
patterns as columns. Its nonnegative dual prices pi_i yield score v(x)=sum pi_i x_i.
The returned pattern is classically stored and validated. A root pattern finder
is not an integer allocation or a full branch-and-price solver. Equal MEANS alone
do not permit Note 07's equal-size aggregation: all model-relevant job attributes
and constraints must agree before jobs are interchangeable.

## 2. What the published bottleneck establishes, and what it does not

Xu et al. [2] solve this model with tailored piecewise-linear branch-and-cut pricing
and a bound-aware heuristic/exact hybrid. Their public experiments use generated
cloud-inspired instances; the earlier industrial workload is confidential. We have
not obtained or replayed it. The source table reports the following DW-Hybrid
statistics, aggregated with its stated shifted-geometric-mean procedure:

| Jobs in the source family | Reported pricing-time share | Reported final relative dual gap |
|---:|---:|---:|
| 100 | 96% | 2.0% |
| 400 | 73% | 11.8% |
| 1000 | 8% | 34.2% |

These are SOURCE-REPORTED metrics, not our timings, lower bounds, or quantum
forecasts. They motivate the medium family rather than blind size growth. The
percentages cover all pricing activity, not specifically calls a quantum finder
could replace, and include the source's complete branch-and-price run. A root-only
circuit must not claim to accelerate that whole share. SGM percentages cannot be
plugged into an average-runtime speedup formula as though they described one run.

## 3. A useful finder needs the right threshold

The source hybrid strategy uses more than negative reduced cost [2, Proposition
4.1]. Let z_R be the exactly solved restricted-master objective, and L>0 a valid
current lower bound on the full master. If a feasible pattern has score v>1 and

$$
v\geq\theta:=z_R/L,
$$

then even the exact pricing optimum V* cannot improve the current Farley bound:

$$
V^*\geq v\quad\Longrightarrow\quad z_R/V^*\leq z_R/v\leq L.
$$

The pattern is eligible to add, and that exact pricing call can be skipped FOR THIS
bound update. This is an existing hybrid-pricing rule, not our theorem. It does
not certify global optimality, no remaining columns, or that a different column
would not produce faster master convergence. The numerical interface must validate
z_R and L; bounds and interval arithmetic can replace exact master data as needed.

This changes the marked set for our proposed generator to

$$
\mathcal M=\{x: A(x)+\sqrt{qS(x)}\leq C,\ v(x)>1,\ v(x)\geq z_R/L\}.
$$

Both acceptance tests are required: if z_R/L=1, a score of exactly one is not an
improving column. With L=0 the rule cannot be used; obtain a valid positive lower
bound classically or retain a different explicitly justified finder contract.

For example z_R=100 and L=95 give theta=20/19. A column scoring 1.03 has negative
reduced cost but does not meet this bypass threshold.
A feasible score 1.06 does. These are illustrative exact numbers, not a sampled
cloud dual vector. The distinction must survive actual solver traces.

Let ell be the best feasible score already found classically and U a validated
upper bound on V*. If ell meets the marked threshold, quantum work is unnecessary.
If U<theta, no pattern can supply this particular bypass; indeed z_R/U>L may
already improve the bound. If U<=1, no strict improving column exists. Thus only
unresolved cases with ell<theta<=U (plus the strict score test) can motivate this
quantum call. Existing positive columns, adequate integer bounds, and direct
allocation algorithms remain valid ways to finish the task without it.

This also addresses the concern that difficult pricing merely proves absence:
a sufficiently strong POSITIVE witness can, under the source's rule, remove one
need for tighter certification. Whether such witnesses exist and are costly to
find in the calls responsible for the published runtime remains UNTESTED.

## 4. The risk test needs no sampling oracle or square-root circuit

For A,S>=0 and q>0, feasibility is equivalent to

$$
\boxed{A\leq C\quad\text{and}\quad q S\leq(C-A)^2.}
$$

The first inequality is essential: squaring a negative headroom would accept some
invalid patterns. Clear denominators exactly, or use conservatively rounded input
intervals. Then the test needs integer addition, comparison and multiplication,
not sampling demand scenarios, arbitrary amplitude encoding, or a nonlinear-oracle
assumption. q=19 is one exact rational risk convention; a normal quantile instead
needs an explicitly priced approximation/calibration policy. The quantum device
optimizes a deterministic reformulation; it does not generate or observe cloud demand.

Extend the feasible-prefix circuit of Note 06 as follows. Store the running A,S;
for each classically ordered job, reversibly compute the proposed new pair and
both inequalities. Controlled on feasibility, branch the zero selection bit with
a Hadamard. Uncompute the entire prospective test while the running pair is
unchanged; then conditionally add the job's a_i and b_i. Nonnegative coefficients
make feasibility downward closed, so every feasible pattern has a path and no
infeasible pattern is produced. The induced distribution is nonuniform and ordered,
just as in Note 06. Score accumulation marks the new threshold; all work is inverted
for amplitude amplification. This is a specialization of prior tree-generation
and reversible-arithmetic constructions, not a new quantum primitive [6].

Every job coefficient is used sequentially at a fixed circuit location. No quantum
address reads a point table, a DP frontier, the master, or a changing column pool.
These remain classical. A whole deterministic gate list can be recompiled when
prices or thresholds change, and that cost is retained.

If w covers the cleared-denominator means, variances, q, capacity and all relevant
sums, products need O(w) additional bits (e.g. 2w or 3w, not w-bit wraparound).
Schoolbook reversible products and comparisons give a sufficient O(w^2) logical
gate cost per job; ripple-carry score work adds O(b) per job, where b includes the score and cleared rational
threshold bit lengths.
A simple implementation has O(n+w+b) logical qubits with reusable arithmetic
workspace and O(n(w^2+b)+w+b) gates per prepare/mark/reflection cycle. Include
input reading, common-denominator bit growth, classical model estimation, price
updates, gate synthesis, validation, and output. A loose line-routing realization
adds O(n+w+b) swaps/gate overhead; no connectivity or physical clock ratio is free.

For marked mass p_theta>0 the standard conditional amplitude-amplification count
is O(1/sqrt(p_theta)); a sufficient logical-gate bound is therefore

$$
\widetilde O\big([n(w^2+b)+w+b]/\sqrt{p_\theta}\big),
$$

before the above setup, routing and physical overhead. Neither p_theta nor the
classical cost to estimate it is supplied free. Comparing with 1/p_theta classical
replays is not a comparison with the best optimizer. A bounded failed search proves
nothing about existence; keep a capped attempt and the original fallback. This
root predicate excludes branch-specific together/apart restrictions unless they
are explicitly added and costed in a successor. No full circuit or gate count was
compiled here.

Safe upward rounding can preserve acceptance safety while deleting near-boundary
feasible patterns. It therefore does not license a no-column certificate or an
unchanged optimum. Model risk, numerical error, quantum failure and optimization
quality remain separate requirements.

## 5. Why the previous one-counter DP does not transfer automatically

A single "best score at each used mean" is insufficient. Consider a partial
pattern with (mean,variance,score)=(10,1,1/2), another with (10,4,3/4), and a later
job with (1,1,3/5). For C=14,q=4 both partial patterns fit. Only the lower-variance
one can accept the later job, producing an improving score 11/10. Keeping only the
higher score at mean 10 discards that completion. This three-job counterexample
is easy classically; it refutes one transferred recurrence, not classical algorithms.

A DP tracking both integer mean and variance, dominance labels, special ratios,
and other formulations remain competitors. For genuinely integer coefficients,
feasible S<=C^2/q gives a pseudopolynomial two-counter bound; saying C=72 physical
cores does not by itself determine its integer grid after precision scaling.
If b_i is proportional to a_i, total variance is a function of total mean and the
constraint reduces to a scalar capacity rule again. A large or continuous-looking
coefficient table alone is not a quantum opportunity.

Pooling itself is meaningful: two jobs of mean 10 and variance 1 with q=4 fit C=23
jointly, while adding their standalone safety buffers gives 24. Means-only packing
can be unsafe, while per-job buffering can lose a feasible allocation. Perfectly
positive correlation would change the combined variance from 2 to 4 and invalidate
that pooled allocation. The problem being optimized must match the data assumptions.

## 6. The classical and quantum prior art has strengthened since the source benchmark

Goyal and Ravi [3] give a chance-feasible PTAS for the Gaussian form. It is not the
ordinary knapsack FPTAS, but fixed-profit-margin problems still have a polynomial
classical approximation route in their stated setting; practical cost and safety
are separate from that asymptotic statement. Ryu and Park [4] supply additional
robust/pseudopolynomial approaches under their coefficient assumptions.

Crucially, Kim and Lee [5] give a polynomial method for a stronger non-convex
continuous relaxation and a 1/2-approximation, with stated O(n^3 log n) complexity.
Their bounds and practical rounding methods are direct competitors for ell,U
above. Their experiments use generated standalone objectives, not our proposed
cloud master duals; we do not transfer their reported times or assume failure.
The next comparison must include these later bounds, not only the 2023 baseline.

Quantum chance-constrained knapsack is also NOT new. Bordelon et al. [9], revised
16 June 2026, study a variational quantum/classical method for insurance-motivated
instances; its latest abstract says solution quality is comparable to the tested
classical schemes. This is not a proved gate-model speedup or a validation of our
pricing role. Our exact feasible-prefix/threshold test has different guarantees,
but composing existing ingredients is not publication novelty by itself. We do not
copy its broader distribution-family claims; our Gaussian/moment assumptions above
are explicit and separately justified.

## 7. Decision and bounded next task

Park ordinary deterministic one-dimensional root pricing as the default test path,
retaining Notes 06-07 and their exact result. Select a SOURCE-MOTIVATED, conditional
risk-aware hypothesis for one diagnostic: can strong feasible columns remove
expensive exact pricing calls in the existing hybrid optimizer after its heuristic,
parametric/non-convex bounds, and approximation/gap checks?

Use the published CloudMedium family as the scope anchor, not larger CloudLarge
by default. Start with one declared risk convention and its genuine root-pricing
calls. Obtain current duals, z_R,L, feasible lower score ell and safe upper score U;
classify threshold witnesses rather than simply score>1 columns. Retain calls that
contribute to the useful solver gap, not only a hard objective supplied in isolation.
Do not claim that the entire published pricing percentage belongs to such calls.
No confidential production data are needed for this model test, and generated
benchmarks must remain labelled generated.

A cheap classical method supplying the witness or required gap ends the quantum
call. Only a material residue warrants measuring or bounding p_theta and comparing
fully charged quantum work to the avoided classical fallback. Independent output
quality and total master progress matter; the witness rule alone does not prove
which columns converge fastest. A missing solver/data input blocks that experiment,
not model analysis or honest closure. No new cloud framework, large census, quantum
compiler, added covariance structure, or higher precision chosen just to defeat a
baseline is requested. If this criterion fails, broaden mechanisms rather than
keep making the same problem more elaborate.

## 8. Executed evidence and inspection limits

```sh
python experiments/risk_pricing_gate_v1/verify.py
```

The new standard-library check ran twice with identical JSON, and -O/-OO plus six
invalid inputs were rejected. Exact Fraction tests cover all eight subsets of the
three-job control, the feasible generator, pooled risk and correlation, the sign
guard, conservative rounding, and the published hybrid-bound logic. Its prices
and z_R,L examples are illustrative, not acquired workload data. No native pricer,
cloud model fit, approximation solver, stochastic simulation, quantum circuit,
amplitude search, or timing benchmark was run. No old scientific suite was rerun.

Primary PDFs and HTML were inspected. PDF screenshot requests for the model,
workload table, hybrid rule, and relaxation failed; the source table values were
cross-checked against the primary published HTML table, but not visually validated.
No plot was digitized. A runtime PDF download also failed on DNS; no source data or
code were imported. This is a bounded source/model check, not a complete novelty,
industrial-safety, or independent proof audit.

### Primary references, checked 30 September 2026

[1] Cohen, Keller, Mirrokni and Zadimoghaddam, *Overcommitment in Cloud Services:
Bin Packing with Chance Constraints*, Management Science 65 (2019), 3255-3271.
Application abstract and model Sections 2-3 inspected; no deployment claim adopted.
https://doi.org/10.1287/mnsc.2018.3091
https://arxiv.org/abs/1705.09335

[2] Xu, D'Ambrosio, Haddad-Vanier and Traversi, *Branch and price for submodular bin
packing*, EURO Journal on Computational Optimization 11 (2023), 100074.
Model, Proposition 4.1/Algorithm 2, Table 2 and experiment definitions inspected.
https://doi.org/10.1016/j.ejco.2023.100074
https://arxiv.org/abs/2204.00320

[3] Goyal and Ravi, *A PTAS for the chance-constrained knapsack problem with random
item sizes*, Operations Research Letters 38 (2010), 161-164. Primary abstract/model.
https://doi.org/10.1016/j.orl.2010.01.003

[4] Ryu and Park, *Robust solutions for stochastic and distributionally robust
chance-constrained binary knapsack problems* (2021). Primary abstract only.
https://arxiv.org/abs/2105.11875

[5] Kim and Lee, *Non-convex relaxation and 1/2-approximation algorithm for the
chance-constrained binary knapsack problem* (2024). Primary HTML and theorem text
inspected; full correctness and experimental results not independently reproduced.
https://arxiv.org/abs/2403.06686

[6] Wilkening et al., *A quantum algorithm for solving 0-1 Knapsack problems*,
npj Quantum Information 11,146 (2025). Generator precedent retained from Note 06;
new risk predicate supplied here, not the published deterministic benchmark.
https://doi.org/10.1038/s41534-025-01097-8

[7] Sadykov and Vanderbeck, *Bin Packing with Conflicts: A Generic Branch-and-Price
Algorithm*, INFORMS J. Computing 25 (2013). Primary abstract, alternate screen only.
https://doi.org/10.1287/ijoc.1120.0499

[8] Parmentier and Meunier, *Aircraft routing and crew pairing: updated algorithms
at Air France* (2017). Primary abstract, alternative and classical counterweight.
https://arxiv.org/abs/1706.06901

[9] Bordelon et al., *A Quantum Approach to Stochastic Optimization in Insurance
Underwriting*, arXiv:2605.01169v2, 16 June 2026. Latest abstract and methods inspected;
not a reproduced benchmark or evidence of the proposed cloud-pricing advantage.
https://arxiv.org/abs/2605.01169v2

Only Quantum-Assisted-Algorithm-Discovery may be modified. Preserve prior science,
licenses, the no-QRAM boundary, and independent spin-offs. No new repository,
manuscript, merge, release, external contact, or paid/unattended work is authorized.
