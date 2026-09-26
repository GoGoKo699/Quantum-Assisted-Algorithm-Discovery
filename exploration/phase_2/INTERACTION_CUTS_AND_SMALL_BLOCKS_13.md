# A sampled cut problem, and the classical advantage of small components

26 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.
Live branch base: f90d584da989f4c224847f1e9749ec811dd40460.
This is an exploratory algorithm/comparison audit. The quantum sampling,
hypergraph reduction, concentration and coefficient-estimation ingredients are
established. Their combination below is not claimed novel or advantageous over
the best classical method. No useful difficult workload is established.

## 1. A direct predecessor changes the baseline

Bogdanov and Wang, Learning and Testing Variable Partitions, ITCS 2020 [1],
already connect additive L2 variable decomposition with cuts of a hypergraph
whose hyperedges carry squared Efron-Stein/Fourier-component weights. Their
Proposition 18 gives the partition-loss identity used in the preceding scout.
Their paper also develops a classical approximate minimum-cut-oracle approach,
using noisy evaluations and symmetric submodular optimization. It is motivated
by decomposing control variables in reinforcement learning, not by quantum
computing. The prior scout's list of sensitivity/surrogate references missed
this more direct problem-and-algorithm predecessor.

For real f with L4 norm at most one, their Theorem 2 finds a nontrivial two-way
partition with squared-L2 loss at most optimum plus epsilon in
O(n^5 log(n/gamma)/epsilon^2) time in their evaluation model. This is a published
upper bound, NOT a lower bound against classical learning. Our bounded-value
assumption |f|<=1 implies that moment condition but is stronger. No factor-n^4
end-to-end advantage follows by juxtaposing their upper bound with a quantum
query count. Their native algorithm was not executed, and the strongest
subsequent classical complexity is not certified by this literature search.

The positive question is whether an explicit sampled hypergraph can replace a
noisy cut oracle in a useful regime, with all quantum acquisition costs charged.

## 2. Exact quantum interface inherited from scout 12

The supplied input is a deterministic finite-precision program
f:{0,1}^n -> [-1,1], with independent uniform bits and n>=2. Write c_S for its
Walsh coefficients. A raw signed-value-to-amplitude Fourier trial has

    Pr(flag=1, label=S)=c_S^2,
    Pr(NULL)=1-E[f^2].

This is an ideal-law statement. Reversible f evaluation and its inverse,
amplitude rotation accuracy, input preparation and Hadamards belong in the
implemented trial cost C_spectral. Boolean Fourier sampling is prior work [3].
A sample-only API is not a coherent evaluator. A coherent evaluator here can
be compiled only when the program and its required data access are supplied.

For a nonempty proper cut A of the variables, the best approximation of the
form g(x_A)+h(x_Ac) has mean-square loss

    L(A)=sum_(S intersects both A and Ac) c_S^2.

NULL, empty and singleton outcomes never cross a cut. Keep them in the RAW
trial denominator; deleting them and renormalizing would change L.

## 3. Complete two-way partition algorithm

Draw m independent raw records. Treat every observed nontrivial set S as a
hyperedge, with integer weight equal to its occurrence count. Aggregate repeated
sets. The empirical cut objective is

    L_hat(A)=number of records crossing A / m.

Every realized objective is exactly a nonnegative hypergraph cut function.
In particular it is symmetric and submodular, regardless of finite-sample
fluctuations. This is more structure than an arbitrary collection of independent
noisy answers to cut queries; it is not a proof that no classical procedure can
construct an equally useful structured record.

There are M=2^(n-1)-1 nontrivial unoriented cuts. Hoeffding and a union bound give

    Pr(sup_A |L_hat(A)-L(A)|>a) <= 2M exp(-2ma^2).

If A_hat minimizes the empirical cut exactly, then

    L(A_hat) <= min_A L(A)+2a.

Consequently m>=ceil(2 epsilon^(-2) log(2M/delta)) suffices for excess MSE at
most epsilon with probability at least 1-delta. This is
O((n+log(1/delta))/epsilon^2) raw trials, not an exponential partition search.
It is an upper bound, not an optimal sample-complexity assertion.

If each implemented trial is iid from a law within TV tau of the ideal record
law, the true-loss bound becomes optimum+2a+2tau. An empirical optimization
error gamma adds gamma. Correlated device errors need a different argument.
No accuracy claim about the actual quantum implementation is supplied here.

### Classical optimization after sampling

Use the classical hypergraph-to-directed-network reduction [2]. For each
hyperedge e of weight w_e, introduce a_e,b_e, with arcs

    v -> a_e (large capacity), for v in e;
    a_e -> b_e (capacity w_e);
    b_e -> v (large capacity), for v in e.

Choose the large integer capacity as 1+sum_e w_e. A separating cut must pay
w_e exactly when e has vertices on both sides. A noncrossing edge can place
both auxiliary vertices on the same side without paying. All purely finite
cuts have weight at most sum_e w_e, so the large arcs are never part of an
optimal constrained terminal cut.

Fix original source 0, compute its minimum cut to each other original vertex,
and retain the cheapest. Some terminal is across any nontrivial cut, proving
that n-1 terminal flow problems suffice for the global hypergraph minimum cut.
With at most m observed hyperedges, the network has at most n+2m vertices and
O(nm) arcs. Counts have O(log(m+1)) bits. This is a polynomial postprocessing
algorithm, not a claim that this elementary reduction is the fastest approach.

The full accounting is

    setup + m*C_spectral + T_cut(n,m) + fitting + validation.

The output of this stage is a variable bipartition, NOT two already trained
component functions. Quantum register/workspace costs depend on the explicit
evaluator. The classical record requires O(mn) bits. No QRAM, amplitude table,
or precomputed complete hypergraph is granted for free.

### Why arbitrary noisy cut estimates are not interchangeable

A shared classical four-corner trial is an unbiased estimator of L(A), but
one realization need not itself be submodular. In three bits, let the table of
f at indices 0,...,7 be (1,-1,1,1,1,1,-1,1), and take endpoints 000,111.
The value [f(000)+f(111)-f(A)-f(Ac)]^2/4 at masks 0,...,7 is

    (0,4,0,0,0,0,4,0).

At A=010, B=100, the submodular inequality fails: the left side is zero and
the right side is four. The EXPECTATION is still the correct cut objective.
This diagnostic explains one possible benefit of a common structured record.
It is not a classical lower bound; different estimators, optimizers or sketches
must remain competitors.

## 4. A near-best cut does not automatically yield a useful simplification

The cheapest nontrivial cut can isolate an irrelevant variable and leave the
remaining n-1 variables together. That is a valid answer to the two-way cut
task, but may not appreciably reduce evaluation or fitting costs. A balance,
block-size, cost or multiple-component requirement is a DIFFERENT optimization
constraint. The unconstrained mincut proof does not carry over automatically.
Greedily repeating optimal two-way cuts need not solve the constrained global
partition problem. We have not made that claim or tested it as an algorithm.

Likewise a low cut weight is a statement about average squared error under the
specified product input law, not worst-case correctness, causal independence,
or behavior under a shifted distribution. A genuinely useful target needs a
reason the resulting components are substantially cheaper to construct/use.

## 5. Strong source-aware classical response for genuinely small components

Suppose every retained block has at most b inputs, with 1<=b<=n. Then only
Walsh terms of order at most b can occur inside any block. Put

    N_b=sum_(j=0)^b binom(n,j),
    D_b=1+floor(n/b)*(2^b-1)+(2^(n mod b)-1).

N_b is the number of potentially relevant coefficients. D_b is an upper bound
on the number retained by any admissible partition (the bound is attained by
using as many full b-sized blocks as possible). It is a property of the output
class, NOT an assumption that the supplied f has a sparse spectrum.

Draw ONE bank X_1,...,X_m of uniform classical inputs and evaluate f once at
each. Reuse each value for every coefficient of order at most b:

    c_tilde_S = mean_t f(X_t) chi_S(X_t).

Since each summand lies in [-1,1], simultaneously

    max_(|S|<=b) |c_tilde_S-c_S| <= eta

with probability at least 1-delta whenever

    m >= 2 eta^(-2) log(2 N_b/delta).

Computing and storing these estimates costs real arithmetic: a straightforward
implementation uses O(m N_b b) work, aside from f evaluation. This is polynomial
for fixed b and can be impractical for large b. The values are not acquired
with a separate model query for every coefficient or proposed partition.

### The same bank supports selection AND fitting

For partition P let K(P) be its retained Walsh indices, including the constant,
and let W(P)=sum_(S in K(P)) c_S^2. Parseval and |f|<=1 imply W(P)<=1.
The uniform coefficient event yields

    |sum_(S in K(P)) c_tilde_S^2 - W(P)|
      <= 2 sqrt(D_b)*eta + D_b*eta^2

for EVERY admissible P. To verify this, apply Cauchy-Schwarz to twice the
inner product of the true coefficients and their errors, then add the squared
error norm. No union over the exponentially many partitions is needed here.

Choose a partition P_hat whose estimated retained energy is within gamma of
its maximum; construct g_hat using the same estimated signed coefficients.
Orthogonality separates discarded true terms from retained fitting errors:

    E[(f-g_hat)^2]
      <= min_admissible_P L(P)
         +4 sqrt(D_b)*eta +3 D_b*eta^2 +gamma.

This holds on the same simultaneous event even though the partition was chosen
from the data. A separate fitting bank is unnecessary for THIS bound. With
eta=epsilon/(8 sqrt(D_b)) and 0<epsilon<=1, the excess is below epsilon+gamma,
using at most the sufficient count

    m >= 128 D_b epsilon^(-2) log(2 N_b/delta).

These constants are conservative; this is an elementary learner, not the best
classical guarantee. The optimizing step still needs an algorithm. For general
block constraints it may be expensive. An oracle optimizer is not supplied
implicitly to either method.

### Two-input blocks have a polynomial classical optimizer

For b=2 every partition consists of singletons and disjoint pairs. The retained
energy is

    c_empty^2 + sum_i c_i^2 + sum_({i,j} in matching) c_{ij}^2.

The first two terms do not depend on the matching. Maximizing the third is
ordinary maximum-weight matching, with edge weight c_{ij}^2. Replace the true
coefficients by estimates to solve the empirical problem. Polynomial classical
weighted-matching methods are established [5]; the companion diagnostic uses
only a small subset DP to check the reduction, not a production matching solver.

Now D_2=1+n+floor(n/2), N_2=1+n+binom(n,2). One labeled bank with
O(n epsilon^(-2) log(n/delta)) model evaluations gives selection and fitting
within the stated MSE excess. Its arithmetic/postprocessing differs from the
quantum route and is not free. But its model-evaluation count already matches
the leading n/epsilon^2 scale of our uniform-cut-record guarantee, up to logs.
Thus an alleged advantage based on classical methods needing to test every
pairing independently would be artificial. This is not a proof against every
quantum precision or postprocessing advantage.

All terms of order at least three are discarded by EVERY pair partition.
An exponentially rich collection of such terms therefore does not make choosing
the best pairing harder. If that unavoidable tail is large, no pair-component
model is good; if small, the useful output itself carries exploitable structure.
More generally, an adequate bounded-block approximation is Fourier-sparse even
when f is not. Classical learning of functions approximable by sparse Fourier
representations has direct longstanding precedent [4]. We cannot dismiss it
merely because our sampler does not assume sparsity of the original f.

## 6. What was actually implemented and checked

The standard-library diagnostic uses exact fractions and integer maxflow:

- 304 bounded small functions: all 256 three-bit Boolean sign functions plus
  48 seeded bounded rational tables, with 2832 independent projection/cut checks.
- All 2048 unweighted four-vertex hypergraphs (edges of sizes 2,3,4), comparing
  the flow reduction with complete cut enumeration.
- 48 direct classical shared-bank fitting cases and 1392 candidate small-block
  partitions. Maximum-weight pairing agrees with exhaustive retained-energy
  optimization; actual prediction error agrees with projection plus fitting error.
- The non-submodular four-corner realization above, checked exactly.
- The preceding six-variable illustrative spectrum: 4096 RAW trials sampled
  CLASSICALLY from its explicitly known law. Counts of sets 3,12,21,48 are
  311,327,101,329; NULL count is 3028. Empirical global mincut selects mask 3,
  with true loss 1/49, equal to the enumerated optimum. The empirical loss is
  101/4096. No gate-based Fourier sampling or hidden-source discovery occurred.

The last toy also admits the earlier best pair partition {0,1},{2,3},{4,5}.
The structure is visible in its supplied expression; it is not a favorable
application benchmark. The 48 random-table controls do not assume a sparse
spectrum, but they remain deliberately small and exhaustively solvable.

Both executions of the new diagnostic reproduce results.json byte-for-byte.
Source SHA256: ab40ff1cb4f37cc55a1df2ff1d7c7c6122d743384e46fd1ed7cc62de04c3df2b.
Results SHA256: 56ceddf9f084ad16012bf1ad970dd73bc26df1082dc28ccfefdeef07595fc4a7.
The supplied preceding interaction_record_check.py was rerun unchanged. Its
report matches the supplied report at SHA256
0dd3dc33201a1a15050e1944c463d7b13f4fe1fb4b8a576cadb9bc3dc15dedaa.
No root/historical verifier, native Bogdanov-Wang learner, SPEX/Sobol-TT system,
large simulator, production matching solver, quantum compiler or hardware ran.

    python split_and_fit_check.py --output /tmp/new-split-fit.json

The companion files are provided in the conversation checkpoint; only this
note is intended for the scoped research-branch addition. No old files or
reference outputs are overwritten.

## 7. Research decision

Keep the positive mechanism: acquire an interaction-sensitive combinatorial
instance quantumly, then exploit classical optimization. The two-way variant
now has a complete inference-to-partition route rather than an unpriced search
over partitions. Quantum acquisition and classical postprocessing are distinct.

But require the consequence: a useful fitted model, or an independently useful
partitioning decision. Small-group convenience can make classical discovery
cheap too. Large components can make fitting/deployment dominate. A published
classical upper bound or a Fourier-sampling black-box lower bound alone does not
establish a source-aware end-to-end advantage for this task. No new-result or
publication-readiness claim is made. The manuscript stays on hold.

The next decisive investigation should locate a setting where the partition
itself enables a useful computational decomposition, without merely requiring
small arbitrary truth-table blocks, and where existing classical cut estimation,
surrogate learning and source analysis are genuinely costly. Do not revive a
weak classical oracle or enlarge a toy to manufacture the claimed gap.

## Primary sources and inspection scope

[1] A. Bogdanov, B. Wang, Learning and Testing Variable Partitions, ITCS 2020,
37:1-37:22, DOI 10.4230/LIPIcs.ITCS.2020.37. Official abstract and parsed paper
were inspected, especially Theorem 2, Proposition 18 and the cut-oracle discussion.
The expanded arXiv version is 2003.12990. PDF screenshot attempts on both arXiv
and Dagstuhl failed; no figure/table measurements or visual inspection is claimed.
https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2020.37
https://arxiv.org/abs/2003.12990

[2] E. L. Lawler, Cutsets and partitions of hypergraphs, Networks 3(3),275-285
(1973), DOI 10.1002/net.3230030306. Primary publisher abstract inspected;
network construction and correctness above were independently derived/checked.
https://onlinelibrary.wiley.com/doi/abs/10.1002/net.3230030306

[3] H. Li, L. Yang, A quantum algorithm for approximating the influences of
Boolean functions and its applications, Quantum Information Processing 14,
1787-1797 (2015), arXiv:1409.1416. Primary abstract and earlier scout inspected.
The bounded signed-value flag interface is derived in scout 12, not attributed
as a new theorem to this source or to the current work.
https://arxiv.org/abs/1409.1416

[4] E. Kushilevitz, Y. Mansour, Learning Decision Trees Using the Fourier
Spectrum, SIAM J. Comput.22(6),1331-1348 (1993), DOI 10.1137/0222080. Publisher
abstract includes polynomial-sparse approximants and membership queries. It is
prior art, not a native implementation or an asserted optimal rate for our class.
https://epubs.siam.org/doi/10.1137/0222080

[5] Maximum-weight matching is a standard classical optimization primitive.
The current experiments use the explicitly described small exhaustive/subset
solver only; no library complexity or timing result is transferred to this run.
