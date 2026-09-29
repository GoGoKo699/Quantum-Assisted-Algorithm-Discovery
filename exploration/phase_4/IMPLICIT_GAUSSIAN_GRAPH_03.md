# Implicit Gaussian graph 03: a real reuse task and a priced quantum-access bottleneck

29 September 2026. Baseline: `e7af3ecdaf0393cc9f279f1267429fba8073dcc0`.
Branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Decision:** retain Gaussian similarity-graph sparsification as an in-scope
candidate, not a demonstrated new advantage. It has a useful classical output,
an established quantum construction, and a genuine conditional worst-case
classical obstacle. Its broad-kernel regime is already inexpensive classically,
and the quantum memory/access assumptions are material. The most concrete next
hypothesis is to reduce the random-oracle working memory of the existing quantum
algorithm by proving only sparsifier correctness, rather than preserving its
entire fully independent output distribution. Bounded-independence sparsification
is prior work; its integration with the adaptive quantum construction is NOT
proved here. No new repository or spin-off is needed.

## 1. A reusable mathematical object for a documented learning workflow

Input n points x_i in R^d, represented by b-bit coordinates, and a supplied
bandwidth sigma. The complete undirected similarity graph has no self-loops and

$$
w_{ij}=\exp[-\|x_i-x_j\|^2/(2\sigma^2)],\qquad
L=\sum_{i<j}w_{ij}(e_i-e_j)(e_i-e_j)^T.
$$

The compact input is the point table and bandwidth, not an n-by-n edge matrix.
Gaussian weights and harmonic label propagation are independently established
in semi-supervised learning [1]. With known labels on a nonempty boundary, the
remaining real-valued predictions minimize f^T L f subject to those labels.
This can be useful for repeated label sets/tasks on the same data geometry.
The bandwidth and the validity of graph smoothness as a learning assumption are
not solved by sparsification. In particular, a graph energy guarantee is not a
measured improvement in classifier accuracy.

The reusable output contract is a classical graph H with approximately
n/epsilon^2 edges (up to logarithms) such that, with stated success probability,

$$
(1-\epsilon)L\preceq L_H\preceq(1+\epsilon)L.
$$

Its guarantee is simultaneous for every vector, so later classical queries need
not be known when H is constructed. A success event for this deterministic graph
property is not a collection of independent per-query sampling guarantees.
The number of later uses and their costs must be matched on both sides. A single
known downstream statistic may have a cheaper direct solution; do not force that
competitor to construct an unnecessarily universal graph.

### What the graph guarantee says about harmonic predictions

Let f and g minimize the two quadratic forms with the same fixed boundary labels,
and set e=g-f. Then e vanishes on the boundary, e^T L f=0 and e^T L_H g=0.
The spectral sandwich implies

$$
(1-\epsilon)\|e\|_L^2
\leq |e^T(L_H-L)f|
\leq\epsilon\|e\|_L\|f\|_L,
\qquad
\boxed{\|g-f\|_L\leq\frac{\epsilon}{1-\epsilon}\|f\|_L.}
$$

The cross-term inequality uses the operator norm of the relative perturbation
on the space orthogonal to the constant vector. This is a standard variational
consequence, not a new algorithm. Coordinate error or thresholded classification
needs a grounded eigenvalue/margin argument; it is not supplied for free.

## 2. Implement the input oracle, rather than assume a dense quantum table

For zero-based i and k in {0,...,n-2}, the k-th neighbor in the complete graph is
j=k+1[k>=i]. Its degree is n-1. Computing the weight needs two point-row lookups,
a squared distance and an exponential at the declared accuracy. The adjacency
index itself is simple reversible arithmetic. No weighted-row amplitude state,
row-sum normalization, or unknown eigenbasis is supplied.

Apers and de Wolf [2] give a quantum algorithm returning the required classical
sparsifier in time O-tilde(sqrt(mn)/epsilon) in their adjacency-list and quantum-
read/classical-write RAM model, for epsilon at least sqrt(n/m). For this complete
graph m=n(n-1)/2, the ideal-word time is O-tilde(n^(3/2)/epsilon). It is an existing
algorithm, not this project's result. Logarithms hide graph size, representation
precision and success-probability overhead, not arbitrary lookup circuits.

Their resource statement also includes O-tilde(sqrt(mn)/epsilon) bits of
coherently accessible working memory, besides input access. O(log n) active qubits
is therefore NOT total physical memory. For compact point input, add nd b data
bits and their ingestion and coherent-interface cost. One explicit budget is

$$
C_Q=C_{\rm ingest}+C_{\rm memory\ setup}
+\widetilde O(n^{3/2}/\epsilon)
   (T_{\rm edge}^Q+T_{\rm working\ lookup}+T_{\rm word})+C_{\rm output},
$$

where T_edge^Q includes both point-row lookups and reversible arithmetic.
Actual input/working query counts need not all attain this common upper envelope.
Preparing an arbitrary point table takes at least reading that input; neither
loading nor maintaining it is free. The output itself contains approximately
n/epsilon^2 weighted edges with their finite-bit representation.

A conventional sequential multiplexer is one implementation with work linear in
table size per lookup; substituting it can erase the advertised query saving.
That is an implementation example, not a lower bound against all coherent-memory
architectures. A fast RAM interface is a substantive resource assumption, not an
impossibility. The source itself flags the fault-tolerant memory issue [2, Sec.2.1].
No circuit, QRAM architecture, wall-clock comparison, or hardware resource count
has been implemented here.

### Finite precision is a graph property, not merely a kernel-value error

If every stored weight obeys (1-eta)w_e<=wtilde_e<=(1+eta)w_e, then the same PSD
sandwich holds for the Laplacians because each edge contributes a positive matrix.
An epsilon sparsifier of Ltilde has distortion at most eta+epsilon+eta epsilon
relative to L. Allocate both errors to the requested final tolerance.

For Gaussian exponent range [0,R], fixed-point absolute error eta exp(-R) suffices,
requiring O(R+log(1/eta)) fractional bits. This is a sufficient accuracy budget,
not a claim that all applications require the same smallest weight. Truncating
small weights requires an output-error argument, not a small maximum entry error.
A floating exponent representation changes the arithmetic model and must be priced.

## 3. A concrete classical shortcut: the broad-kernel regime

Suppose a cheap certified bound gives tau<=w_ij<=1 with tau>0. A bound from the
input coordinate range may be used; do not spend n^2 work computing an exact
minimum unless that work is charged. On 1-perp, L>=n tau I. Effective resistance
R_e=b_e^T L^+ b_e therefore gives leverage

$$
\ell_e=w_eR_e\leq\frac{2}{n\tau},\qquad \sum_e\ell_e=n-1.
$$

Choose S edges uniformly with replacement and weight each selected copy by
m w_e/S. The resulting Laplacian is unbiased. After conjugation by L^+/2, one
sample has operator norm at most (n-1)/tau and expectation the identity on 1-perp.
The usual matrix Chernoff inequality [5] gives failure at most

$$
2(n-1)\exp[-S\epsilon^2\tau/(3(n-1))],\quad 0<\epsilon<1.
$$

Thus S=O(n log(n/delta)/(tau epsilon^2)) edge evaluations suffice. If this is larger
than the whole graph, enumeration plus a standard classical sparsifier is another
option. If its output is too large for the final edge budget, classically
resparsify this already smaller graph, allocating a second approximation error.
That resparsification is standard and costs near-linear time in its input size
for fixed accuracy; output edge reweighting and duplicate handling are charged.

In particular, constant tau gives a near-linear classical construction at fixed
accuracy, without materializing n^2 weights. The quantum n^(3/2) upper bound is
not compelling there. Comparing these two stated upper bounds only, uniform
sampling is already competitive when tau is roughly at least 1/(epsilon sqrt(n)),
up to logarithms and access/arithmetic differences. This is not a hardness
threshold or a claim of optimal classical complexity.

Stronger geometric/kernel algorithms are also available [3,4]. Their guarantees
depend on dimension, kernel regularity, dynamic range and density-estimation
costs. A very small global tau only makes the simple bound unhelpful; a clustered
or otherwise structured graph may still be easy. No blanket quadratic classical
cost is assigned to implicit Gaussian input.

## 4. There is nevertheless a conditional hard corner with compact input

Alman et al. [3] give geometric-graph hardness results, including steep Gaussian
kernels, by reducing closest-pair questions to approximating graph cuts. This is
not merely the observation that a dense graph contains n^2 entries. The following
finite-bit restatement exposes the relevant parameter; it is the prior reduction
idea, not claimed as a new hardness theorem.

Take bichromatic binary points A,B with n total points in dimension d=O(log n).
Let p=ceil(log_2(16n^2)), r=2^-p and w_ij=r^(||x_i-x_j||^2). These are exact dyadic
Gaussian weights. Equivalently the inverse bandwidth is chosen so that the
Gaussian base is r; no exact representation of the irrational constant log 2 is
required when the integer-distance kernel is specified by its dyadic base.

For the cut separating A and B and any integer threshold k:

$$
\begin{array}{ll}
\min_{a\in A,b\in B}\|a-b\|^2\leq k
&\Longrightarrow C(A,B)\geq r^k,\\
\min_{a\in A,b\in B}\|a-b\|^2\geq k+1
&\Longrightarrow C(A,B)\leq |A||B|r^{k+1}\leq r^k/64.
\end{array}
$$

A 1/3-relative cut approximation distinguishes these cases at r^k/2. A spectral
sparsifier gives that cut approximation. One acquired graph supports all thresholds;
read its cross-cut sum and recover the closest integer distance. Its input is
O(n log n) bits and each weight needs at most p d+1=O(log^2 n) fixed-point bits.
The obstruction is not an exponentially long precision input.

Known fine-grained closest-pair hardness [3,6] therefore supplies a conditional
near-quadratic worst-case classical barrier for the universal artifact at constant
accuracy. When the putative construction is randomized, the hypothesis must
exclude bounded-error randomized closest-pair algorithms as well; do not treat a
deterministic-only hardness assumption as sufficient. Under that matching
hypothesis and the fast coherent-memory model, the published quantum upper bound
supplies a meaningful conditional complexity contrast for this graph family.
This is not an unconditional classical lower bound or a newly proved separation.

The APPLICATION qualification is equally important: bandwidth chosen by this
reduction need not be a statistically appropriate bandwidth for the real learning
problem. In this corner min weight can be n^-O(log n), despite polylogarithmic
bit length. Preserving every quadratic direction is stronger than one label
prediction. We have not shown that the hard instances or their tiny connecting
weights are required by a useful data task. The theorem cannot be relabeled an
observed classifier, preprocessing or laboratory advantage.

A separate five-point control shows why absolute entry pruning is not a universal
substitute. Four outer points are labelled 0,0,1,1; a midpoint has harmonic value
1/2. Deleting just its left connections makes its value 1 while the deleted
Laplacian's trace tends to zero with separation. This is a sensitivity example,
not a demand that a real isolated point be classified at arbitrary confidence.
An abstention rule, prior, or weaker output can legitimately change the task.

## 5. A specific algorithmic opening: correctness may require less randomness

The memory audit finds a more discriminating next step than choosing a bigger
point cloud. The published quantum algorithm repeatedly sparsifies an implicit
graph and later samples by approximate effective resistances. It uses a generic
simulation of a long random string: a q-query quantum algorithm has the identical
output law when that string is replaced by a 2q-wise independent one. The compact,
fast-query data structure for that many-way independence is the source of
O-tilde(q) extra coherent working bits [2, Sec.3.2 and Corollary 1].

Our output contract is NOT that exact randomized output law. It asks for any
sparse graph satisfying the spectral inequalities with the promised probability.
There is no requirement that all retained edges have the same full joint law as
independent Bernoulli decisions.

Doron, Murtagh, Vadhan and Zuckerman [7] already prove that bounded-independence
effective-resistance sampling suffices for spectral approximation. At logarithmic
independence their sparsity matches the usual near-linear-edge guarantee. This
is a classical result and does not itself implement the quantum algorithm; its
small-space deterministic construction does not claim a fast solution to the
implicit Gaussian problem. However, it supplies a serious potential replacement
for the generic random-oracle emulation.

**Hypothesis to audit next:** use short, reversibly evaluable random seeds and
prove sparsifier correctness directly, potentially reducing the extra coherent
randomness memory without paying for the old output-law guarantee. Grover search
can enumerate a fixed marked set; it does not intrinsically require that every
edge decision be mutually independent. The distributional certificate for the
marked set, not an indistinguishability claim for every quantum query algorithm,
is the relevant condition.

This is NOT yet a new small-memory algorithm. It must cover BOTH the constant-
accuracy recursive/spanner stage and the final resistance-sampling stage. Changing
only the final stage leaves the first stage's memory requirement. Each fresh
random seed must be independent of the graph and spanners fixed before it; quantum
subroutine failure, adaptive rounds, edge-count tails, finite probability precision
and reversible evaluation cost all require proof. Data-coordinate access, spanner
membership and resistance data structures remain charged even if random-bit memory
shrinks. Input QRAM is not eliminated by a shorter seed.

The next deliverable is that bounded integration/provenance test, not a general
pseudorandomness framework or an assertion of practical speedup. If this memory
replacement is already known, inapplicable, or costs the same elsewhere, record
that promptly. Any surviving new result must then be tied back to a useful
bandwidth/data regime and a matched complete resource comparison. A reduced
memory upper bound alone does not establish deployment or classifier benefit.

## 6. Evidence, provenance, and scope

The new standard-library checker uses exact Fractions. It verifies complete-graph
adjacency arithmetic, one four-point Gaussian graph's resistances and harmonic
perturbation, the uniform-sampling expectation, relative-error composition, a
finite dyadic closest-pair reduction control, and the five-point pruning warning.
It rejects six invalid inputs and execution under -O/-OO. Its finite examples are
identity controls, not a sparsifier implementation, hardness test, dataset study
or quantum-performance benchmark. General bounds follow from the written
arguments and attributed theorems. No matrix-concentration experiment, bounded-
independence algorithm, quantum circuit, QROM/QRAM implementation, or historical
scientific verifier was run.

The first checker draft perturbed the square graph symmetrically and triggered
its intended nonzero-change assertion; the final check perturbs one edge instead.
The reported final version ran twice with identical output. No prior scientific
file was modified to accommodate the check. The saved report preserves exact
rational values and distinguishes proofs from unexecuted algorithms.

Checker SHA256: `d0417617cb3e511bfb8847ba119950d00cfdc26c320133bb7a4c687922b6b148`.
Report SHA256: `53c5cc5d651862cfdabdc6cf4f4649eb46c18f27155ed6341cdc903ad28093b3`.

Primary sources checked 29 September 2026 (focused screen, not exhaustive priority
review):

[1] Zhu, Ghahramani and Lafferty, Semi-Supervised Learning Using Gaussian Fields
and Harmonic Functions (ICML 2003). Section 2, Gaussian weights, harmonic objective
and application context inspected; PDF page 2 visually checked.
https://mlg.eng.cam.ac.uk/zoubin/papers/zgl.pdf

[2] Apers and de Wolf, Quantum Speedup for Graph Sparsification, Cut Approximation
and Laplacian Solving (SICOMP 2022), arXiv:1911.07306v4 (2023). Theorems 1/11,
adjacency/RAM access, random-string emulation, and staged algorithms inspected.
Screenshots failed; no plotted or table performance data inferred.
https://arxiv.org/abs/1911.07306

[3] Alman, Chu, Schild and Song, Algorithms and Hardness for Linear Algebra on
Geometric Graphs, arXiv:2011.02466 (2020). Model, high-dimensional algorithms,
Gaussian closest-pair cut reduction and conditional assumptions inspected in PDF
text. Screenshots failed; no graph/table benchmark used.
https://arxiv.org/abs/2011.02466

[4] Bakshi et al., Sub-quadratic Algorithms for Kernel Matrices via Kernel Density
Estimation, arXiv:2212.00642 (2022). Kernel access, tau lower bound and spectral-
sparsification section inspected; no universal tau-free running time claimed.
https://arxiv.org/abs/2212.00642

[5] Tropp, User-Friendly Tail Bounds for Sums of Random Matrices, Foundations of
Computational Mathematics 12 (2012), arXiv:1004.4389. Standard matrix Chernoff
input to the elementary broad-kernel comparator; not a new concentration theorem.
https://arxiv.org/abs/1004.4389

[6] Rubinstein, Hardness of Approximate Nearest Neighbor Search (STOC 2018),
arXiv:1803.00904. Closest-pair assumptions and binary dimension inspected; PDF
page 3 visually checked. No unconditional or mismatched-randomness lower bound.
https://arxiv.org/abs/1803.00904

[7] Doron, Murtagh, Vadhan and Zuckerman, Small-Space Spectral Sparsification via
Bounded-Independence Sampling, TOCT 16(2), Article 7 (2024); arXiv:2002.11237v2.
Theorems 1.2/1.3 and techniques read in primary PDF; author publication page checked
for the journal title. PDF screenshot failed. The quantum integration above has
not been proved or attributed as their result.
https://arxiv.org/abs/2002.11237
https://doi.org/10.1145/3637034

Only Quantum-Assisted-Algorithm-Discovery is modified. Sensing remains a separate-
input reference, stopping-power a reserve, and the emitter covariance closed.
The handover, phase-3 archive, both classical spin-offs, LICENSE and all earlier
source/results remain intact. No manuscript, new repository, external contact,
paid/unattended work, merge, release or administration change follows.
