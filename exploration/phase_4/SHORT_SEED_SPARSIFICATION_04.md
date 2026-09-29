# Short-seed sparsification 04: preserve the graph guarantee, not the random tape

29 September 2026. Baseline: `288eedadc67c283f9fb1cce4b942e8c780eb43ec`.
Branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Outcome:** an internally derived integration of bounded-independence sampling
with both stages of the Apers/de Wolf algorithm reduces its stated additional
coherently accessible working memory to the output scale, while preserving its
asymptotic time up to logarithmic factors. In the usual finite-word input model,

$$
T=\widetilde O(\sqrt{mn}/\epsilon),\qquad
S_{\rm work}=\widetilde O(n/\epsilon^2),
$$

instead of the source's stated working-memory bound
\(\widetilde O(\sqrt{mn}/\epsilon)\). Input storage/access is SEPARATE and remains
required. The direct reversible implementation uses polylogarithmic active quantum
workspace; it does not preserve the source's exact O(log n) active-qubit bound.
This is a theoretical algorithmic refinement, not a QRAM-free method,
compiled circuit, measured speedup, or demonstrated label-learning improvement.
The ingredients are established prior work; priority of this exact integration
and an independent proof audit remain unresolved. No new repository is needed.

The live Note 03, `IMPLICIT_GAUSSIAN_GRAPH_03.md`, selected this short-seed test.
The conversation's plural-filename Note 03 is a distinct local checkpoint. Neither
is overwritten. Gaussian harmonic label propagation remains the application
anchor, with the accuracy/access limits of the live note. The output below is a
universal classical spectral sparsifier, not independent samples from a specified
edge law. It can be reused classically after construction.

## 1. Claim, scope, and what changes

Take a fixed simple connected weighted graph with n vertices and m edges, with
positive finite-represented weights, shared adjacency/weight access, and
\(0<\epsilon<1/2\). Use the original quantum-read/classical-write RAM convention
[1]. Word length and arithmetic must accommodate weights, shortest-path values,
probability rounding and output precision. In the standard polylogarithmic-word
regime and for inverse-polynomial failure probability, the displayed tilde bounds
apply. Otherwise include the actual word and oracle costs explicitly.

The algorithm returns a weighted subgraph H satisfying

$$
(1-\epsilon)L_G\preceq L_H\preceq(1+\epsilon)L_G
$$

with the allocated success probability. It can report failure if a search or
storage cap is exceeded; that event is included in the probability bound. For
\(\epsilon<\sqrt{n/m}\), simply obtaining the full graph is a legitimate fallback;
the interesting sparse regime is the usual one in [1]. Disconnected graphs can be
handled on the Laplacian image, but are not needed for the Gaussian candidate.

The source uses a generic theorem: 2Q-wise independence reproduces the complete
output distribution of a Q-query quantum algorithm supplied a random tape. Its
fast hash data structure then needs storage proportional to Q [1, Section 3.2].
Here we do NOT reproduce that distribution. We prove the required graph property
using logarithmic-order moments, and let the quantum subroutines evaluate the
resulting fixed graph. Doron et al. [2] already establish the bounded-independence
spectral-sampling principle. Our task is its adaptive quantum integration and
complete resource accounting, including the rough stage rather than only the end.

## 2. A moment lemma usable after conditioning on the previous rounds

Let \(A_e=L^{+/2}w_e b_e b_e^T L^{+/2}\), so
\(\sum_e A_e=\Pi\), \(A_e^2=\tau_e A_e\), and
\(\tau_e=w_e b_e^TL^+b_e\) is the edge leverage. Pi projects onto the Laplacian
image. These normalized matrices occur only in the PROOF; their computation is
not an input oracle. For Bernoulli selectors I_e with prescribed probabilities
p_e, set \(Z_e=(I_e/p_e-1)A_e\). Deterministically retained edges have Z_e=0.

Suppose the selectors are K-wise independent, K is even and at least
\(\max(4,2\log n)\), and independent comparison variables obey

$$
\max_e\|Z_e\|\leq\rho,\qquad
\left\|\sum_e\mathbb E Z_e^2\right\|\leq\rho.
$$

Then, for \(0<\theta\leq1\),

$$
\Pr\left(\left\|\sum_e Z_e\right\|>\theta\right)
\leq n\left(\frac{2\sqrt{\mathrm e K\rho}+8\mathrm e K\rho}{\theta}\right)^K.
\tag{1}
$$

**Proof.** Every term in the noncommutative expansion of
\(\operatorname{Tr}(\sum Z_e)^K\) involves at most K distinct selectors. Its
expectation therefore equals the fully independent expectation, exactly as in
[2]. Evenness gives a nonnegative trace and bounds spectral-norm failure by its
expectation divided by theta^K. For the independent sum, first symmetrize with an
independent copy and Jensen's inequality. The differences have symmetric
DISTRIBUTIONS, maximum norm at most 2rho and summed second moment at most 2rho.
Apply the symmetric matrix-moment inequality of [3, Theorem A.1] with parameter
2K, padding the dimension to four when necessary. It gives the bracket in (1).
This explicit symmetrization avoids treating a centered, biased Bernoulli variable
as distributionally symmetric. No commutativity of the edge matrices is assumed.

In particular, \(\rho\leq\theta^2/(256\mathrm e K)\) makes the bracket at most
5/32, hence the failure probability at most \(n4^{-K}\). This conservative
constant is not a suggested implementation tuning.

For the edge COUNT N=sum I_e with mean mu, the same symmetrized scalar moment
argument, applied before taking a trace, gives

$$
\Pr(N>2\mu+32\mathrm e K)\leq2^{-K}. \tag{2}
$$

Indeed the Kth moment norm is at most
\(2\sqrt{\mathrm e K\mu}+8\mathrm e K\), and the threshold deviation
\(\mu+32\mathrm e K\) is at least twice this number. Count caps can therefore
be imposed without the polynomial loss in failure probability of a Markov-only
edge-count argument. These are standard moment methods specialized here, not
new concentration inequalities.

## 3. The first stage: an implicit rough sparsifier with fresh short seeds

The rough approximation has fixed accuracy alpha=1/4, independent of the final
epsilon. Let \(R=\lceil\log_2\max(2,m/n)\rceil\) and
\(\theta=1/(8R)\). Take K to be the next even integer at least

$$
\max\{4,2\log n,\log_2[16(n+1)(R+1)/\delta]\}.
$$

At round j, condition on all earlier seeds and classical subroutine outcomes.
The remaining graph G_j is then fixed. Build a t-bundle of edge-disjoint
\(\ell_s\)-spanners, with \(\ell_s=O(\log n)\), using the existing quantum
spanner algorithm [1, Theorem 13]. Each spanner is constructed after deleting
the preceding spanners in that bundle. Store their union B_j. Take

$$
t=\left\lceil1024\mathrm e K\ell_s/\theta^2\right\rceil.
$$

Only AFTER this graph and bundle are fixed, draw a fresh K-wise independent
selector seed. Keep B_j; keep each other active edge with probability 1/4 and
multiply its weight by four, as in the existing spanner-based construction [4].

Every edge outside the bundle has a path in each of its t spanners, each with
resistance length at most \(\ell_s/w_e\). Sending 1/t units of flow down each
edge-disjoint path proves \(\tau_e\leq\ell_s/t\). Therefore its centered
selection contribution has norm at most \(3\ell_s/t\), and the sum of its
second moments is at most \(3\ell_s/t\) times Pi. The looser choice
\(\rho=4\ell_s/t\) satisfies (1). No actual resistance calculation is needed
in this stage. The energy argument is the standard bundle-spanner mechanism [4].

If the round has M active edges and B protected edges, the selector count has
mean (M-B)/4. Equation (2) gives the next total count at most
\(M/2+B/2+32\mathrm e K\). Each bundle contains at most
\(B_*=\widetilde O(n)\) edges, so after R rounds the support is
\(O(n+B_*+K)=\widetilde O(n)\). The product of the spectral factors lies within
[3/4,5/4], since \(R\theta=1/8\). Both cardinality and accuracy hold except
on the summed conditional failures.

There is no need to materialize the large intermediate edge sets. For a queried
edge, start with its original weight and replay the stored bundles and seeds:
a protected active edge is unchanged; another is multiplied by four or set to
zero. A zero edge cannot reappear. R is logarithmic, all bundles together use
\(\widetilde O(n)\) words, and the original fixed adjacency slots can contain
implicit zero weights as in [1]. Spanner evaluation of a fixed such graph does
not require its entries to have a fully independent generating law.

**Why adaptivity is safe:** the new seed is independent of the entire previous
history, including the bundle just built. Every conditional graph has the same
uniform spectral/count guarantee. Averaging over histories and taking a union
bound proves joint correctness. Conditioning does NOT fix any information about
a future seed. Reusing one seed after conditioning on its survivors is generally
biased; the checker includes an exact two-layer counterexample.

Quantum spanner randomness remains separate. The subroutine succeeds on every
fixed allowed graph. For a small aggregate failure budget, independent executions
can be combined by taking their union: if one is a valid spanner, so is the union.
Reported edges and weights are checked individually and lengths/counts capped.
This adds logarithmic factors, not a new random tape of length sqrt(mn). The
source spanner already uses output-scale memory. No verification of all m edges
or of all pairs of distances is inserted.

Finally enumerate the rough support using repeated quantum search with a declared
\(\widetilde O(n)\) output cap. Any nonzero marked set is fixed once the seeds
and bundles are fixed. Repeated search works for every such set, not only sets
chosen by independent coin flips. Exceeding the cap or a search failure consumes
its allocated failure budget. The rough stage takes \(\widetilde O(\sqrt{mn})\)
time and \(\widetilde O(n)\) working words in the same access model.

## 4. The final stage: resistance probabilities with one more fresh seed

From the explicit constant-accuracy rough graph, build the existing approximate
resistance data structure [1, Section 4; 5]. Using constant-factor error budgets,
scale its estimates to obtain, on its success event,

$$
R_e^G\leq\overline R_e\leq3R_e^G
$$

for every original edge. For example, a 1/4 rough error and 1/4 oracle error imply
that multiplying the raw estimate by 5/3 gives upper ratio at most 25/9. Use this
valid inverse inequality rather than copying an approximate inverse factor with
the wrong direction. The near-linear stored data and its construction are paid.
Repeated independent data structures and median estimates can reduce failure.

Choose \(s=256\mathrm e K/\epsilon^2\) and
\(p_e=\min(1,s w_e\overline R_e)\). Round p_e UP to a grid of width 2^-b, with
\(2^b\geq4n^2\). Call the actual probability p'_e. Draw a new K-wise independent
b-bit hash family, keep e iff its uniform hash word is below \(2^b p'_e\), and
reweight by exactly \(w_e/p'_e\), NOT \(w_e/p_e\).

The graph remains unbiased. For p'_e<1,
\(\tau_e/p'_e\leq1/s\), so (1) applies with rho=1/s and theta=epsilon.
Also

$$
\mu=\sum_e p'_e\leq3s(n-1)+m2^{-b}\leq3s(n-1)+1.
$$

Equation (2) bounds the output by \(\widetilde O(n/\epsilon^2)\) edges with
logarithmic confidence cost. Tiny probabilities can be rounded upward without
claiming closeness to the OLD edge-selection law. Their contribution to the
new output size is bounded; spectral correctness is proved for their actual
probabilities. Heavy edges with p'=1 are deterministic.

Repeated quantum search over the original adjacency slots outputs precisely that
fixed marked set, up to its stated failure probability, in
\(\widetilde O(\sqrt{mn}/\epsilon)\) time. Give each undirected edge one stable
identifier; reject the reverse-oriented slot to avoid duplicate edge sampling.
The probability for an edge must not change between oracle calls or orientations.
For a complete Gaussian graph the canonical pair index is direct arithmetic.
The original general-graph access convention can likewise use vertex-pair IDs
for this simple-graph claim; degree-prefix storage costs O(n).

Equations (1)-(2), fresh-seed conditioning, and union bounds handle both stages.
Allocate the remainder of delta to the spanners, rough enumeration, resistance
structure and final enumeration. Their usual bounded-error routines can be run
with polynomial caps and amplified logarithmically. Returning failure on a cap
is allowed; silently returning a truncated non-sparsifier is not.

## 5. Hash construction and the complete memory bill

For distinct edge IDs embedded in GF(2^b), take

$$
h(e)=a_0+a_1 e+\cdots+a_{K-1}e^{K-1},
$$

with K independent uniform field coefficients. The Vandermonde property gives
K-wise independent uniform outputs. This is the standard polynomial hash family,
not a new pseudorandom generator or cryptographic assumption [1,2]. The quarter
coin uses two designated bits; the final stage uses the integer threshold above.
A standard finite-field construction and its arithmetic are included in setup.
If there are fewer than K distinct queried edges, full independence on that
smaller domain is an equally valid small-instance fallback.

One seed uses Kb bits. R rough seeds plus one final seed use O((R+1)Kb) bits,
polylogarithmic in n and inverse failure probability. Coefficients are ordinary
classical data; Horner evaluation admits reversible schoolbook field arithmetic
with O(Kb^2) gates and O(Kb) scratch bits, followed by uncomputation. This is a
conservative circuit bound, not a compiled circuit or an assertion of exactly
O(log n) active qubits. Coordinate/weight arithmetic adds its own workspace.
No large coherent lookup table is needed just to evaluate these hash functions.

| Resource | Refined requirement, excluding supplied input |
|---|---|
| Sampling seeds | O((R+1)Kb) bits |
| Rough spanners, search structures and rough output | tilde O(n) words |
| Approximate resistance data | tilde O(n) words |
| Final output and enumeration bookkeeping | tilde O(n/epsilon^2) words |
| Reversible hash scratch | O(Kb) bits, plus input/weight arithmetic scratch |
| Total time in the original query/RAM convention | tilde O(sqrt(mn)/epsilon) |

With polylogarithmic weight/word precision this is output-scale additional QRAM.
For longer words multiply the relevant storage by their actual bit length and
retain their arithmetic cost. Intermediate weights gain only O(R) exponent bits.
Round final output weights to allocated RELATIVE precision, or keep their exact
finite rational description; roundoff cannot be discarded because the underlying
weights are small. An eta-relative initial kernel approximation and eta_out-relative
output rounding combine with the spectral epsilon multiplicatively. Those budgets
must fit the requested final accuracy; (1) itself is for the fixed represented graph.

For compact point input add nd times its coordinate word length and all ingestion,
coherent row lookup and reversible kernel evaluation costs. Hash compression does
not remove input QRAM, spanner/resistance RAM, or memory error correction. A serial
lookup architecture can still erase the time advantage. At fixed epsilon on a dense
graph, the additional working-memory scaling improves from roughly n^(3/2) to n,
up to logs; this is not a gate-time or hardware-energy improvement of the same factor.

## 6. Meaning and next decision

The output law changes, but the useful guarantee is unchanged: a reusable classical
graph preserves all quadratic forms on its success event. Later label/energy
queries need not be known in advance. This is closer to the parent's original
objective than producing a richer record for its own sake.

This is an algorithmic memory improvement over the explicitly stated bound in [1],
conditional on the same graph/RAM access. It is not a new classical lower bound,
a claim that bounded independence is novel, or an observed learning advantage.
Ordinary classical sparsification already has output-scale storage in appropriate
models; our comparison is the working memory of the fast QUANTUM construction.
Quantum search supplies its time bound, not the seed itself. The simple broad-kernel
classical construction and geometric/task-specific bypasses from Note 03 remain.
The hard Gaussian bandwidth reduction is not automatically statistically useful.

**Next:** conduct a focused priority and proof audit of this two-stage integration,
then state one complete point-input resource comparison in a useful bandwidth/
prediction regime. Check that independent-moment sampling and all implicit-round
bookkeeping are already known or genuinely add a resource improvement. Do not start
a random-generator library, a large sparsifier benchmark, a QRAM architecture, or a
third spin-off. If the integration is already in the literature, retain it as prior
work and address the remaining application/access question rather than renaming it.
A plausible mathematical refinement merits audit without first asserting novelty
or a universal quantum-classical separation.

## 7. Executed checks and sources

```sh
python experiments/short_seed_sparsification_v1/verify.py
```

The standard-library checker ran twice with identical JSON and rejected -O/-OO
and six invalid inputs. Exact finite checks cover GF(8) arithmetic and four-output
uniformity, threshold probabilities, a noncommuting Laplacian trace-moment identity,
upward rounding/reweighting, and replay of an implicit graph's stored layer choices.
Two negative controls detect seed reuse and choosing a graph after seeing its seed.
An even-parity six-coin law has the same relevant fourth trace moment as independent
coins but a different sixth moment: we explicitly do NOT claim the laws coincide.
These are proof-component checks, not a quantum spanner/sparsifier run or empirical
validation of the asymptotic theorem. No historical scientific verifier was rerun.

Checker SHA256: `d1594e4a573eba09c8681ddada1a226e60927b27c7d9f0ad9967c8a632c22dd4`.
Report SHA256: `fd7e81801c8a9575683146d4db6c67374f8b14e1f0bce122215103e7d9b452ce`.

Primary sources checked 29 September 2026:

[1] Apers and de Wolf, Quantum Speedup for Graph Sparsification, Cut Approximation
and Laplacian Solving, SICOMP 51 (2022), arXiv:1911.07306v4. Algorithms 1-3,
Sections 2-4, Theorems 11/13, and explicit RAM statements inspected as PDF text.
https://arxiv.org/abs/1911.07306

[2] Doron, Murtagh, Vadhan and Zuckerman, Small-Space Spectral Sparsification via
Bounded-Independence Sampling, ACM TOCT 16 (2024). Author-hosted journal PDF and
arXiv:2002.11237v2, Section 3, moment matching and probability rounding. Its
classical deterministic space theorem is not a fast implicit quantum algorithm.
https://salil.seas.harvard.edu/publications/spectral-sparsification-bounded-independence-sampling
https://arxiv.org/abs/2002.11237

[3] Chen, Gittens and Tropp, The Masked Sample Covariance Estimator: An Analysis
via Matrix Concentration Inequalities, Information and Inference 1 (2012),
arXiv:1109.1637v3, Theorem A.1. Distributional symmetry is obtained by an explicit
independent-copy symmetrization above, not confused with matrix self-adjointness.
https://arxiv.org/abs/1109.1637

[4] Koutis and Xu, Simple Parallel and Distributed Algorithms for Spectral Graph
Sparsification, ACM TOPC 3 (2016), arXiv:1402.3851. Bundle-spanner mechanism as
specified and reproduced in [1]; its full independent paper was not separately
reproved here. https://arxiv.org/abs/1402.3851

[5] Spielman and Srivastava, Graph Sparsification by Effective Resistances,
SICOMP 40 (2011), arXiv:0803.0929. Resistance data structure and sampling are used
through the stated toolbox in [1], not newly implemented or independently audited.
https://arxiv.org/abs/0803.0929

Focused searches for quantum sparsification, bounded independence and memory did
not establish publication priority for this exact composition. Search results
included unrelated QAOA and matrix algorithms; absence of a matched result is not
proof of novelty. Requested PDF screenshots failed; no figures or table-derived
performance numbers were used. No dataset, native solver, quantum circuit, hardware
benchmark, external contact, manuscript, release or new repository was produced.
Only Quantum-Assisted-Algorithm-Discovery is modified; prior science and rights stay intact.
