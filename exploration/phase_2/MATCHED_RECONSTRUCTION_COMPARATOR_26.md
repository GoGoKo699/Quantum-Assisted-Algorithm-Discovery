# Same number of counts; different extension-field costs

27 September 2026. Base: `8daa8ae16458acd25155179ad2ab35a97f600b40` on
`research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision from the direct comparison:** the twist method does not need fewer
cardinality calls than an equally pruned, endpoint-completed base-change method.
Their exact count data are interconvertible. What survives is a one-for-one
replacement of degree-2n base-change counts by degree-n fresh-twist counts.
This separates a genuine representation/cost change from an unfair call-count
comparison with the longer consecutive schedule.

This is a proof and comparator correction, not a new quantum primitive, a claim
that the precise pruning appears verbatim in a predecessor, or a demonstrated
useful quantum advantage. The new [diagnostic](../../experiments/reconstruction_comparator_v1/README.md)
executes both reconstructions on supplied polynomial controls and checks the
matched cost accounting. It is not another native point-counting benchmark.

## 1. Common mathematical contract

Let P(T)=product_i(1-alpha_i T) be the degree-2g numerator for the same curve over
F_q, with reciprocal Weil roots and integer coefficients. Put

$$
K_n=\prod_i(1-\alpha_i^n),\qquad T_n=\prod_i(1+\alpha_i^n).
$$

The standard identity is K_(2n)=K_n T_n. For the odd-characteristic hyperelliptic
implementation, T_n is the cardinality of a fresh nontrivial quadratic twist over
F_(q^n). The algebraic quotient K_(2n)/K_n does not require physically constructing
that twist. For general curves the algebra below still holds, but no new general
curve-arithmetic or point-sampling implementation is being supplied.

Use the same sufficient large-field regime as the retained pipeline, q>=64g^2.
The conditional reconstruction only needs true cardinalities and the inherited
Weil/rounding hypotheses. Genus two uses endpoint equations without this size
condition; genus one needs only K_1. Sampling, certification and the group
backend have their own costs and failure guarantees.

For g>=2 set h=max(1,g-2), and let O_h be the odd integers in [1,h]. Compare:

$$
\mathcal S_h=\{K_r:r\in O_h\}\cup\{T_n:1\le n\le h\},
$$

$$
\mathcal D_h=\{K_r:r\in O_h\}\cup\{K_{2n}:1\le n\le h\}.
$$

The second is an ordinary base-change-only comparator. Its degree set is also
[1,h] union {2,4,...,2h}. Both transcripts require exactly h+ceil(h/2) calls.
These are sufficient schedules, not minimum-query theorems. Do not treat the
unknown Weil polynomial's count data as freely independent information to infer
an unrestricted lower bound.

## 2. Exact transcript equivalence

From D_h, each K_n for n<=h is already present: odd n is an anchor and even n
is among the queried even degrees. Recover T_n=K_(2n)/K_n by exact division.

Conversely, start with the odd anchors in S_h and process n=1,...,h. When n is
even, K_n was produced at step n/2; when n is odd, it was supplied. Form
K_(2n)=K_n T_n. This recovers all of D_h without additional group queries.

Equivalently, every odd r starts a dyadic chain r,2r,4r,... . The plain transcript
supplies its consecutive vertex values; the signed transcript supplies its first
value and consecutive ratios. Both descriptions have the same number of integer
entries. This explains why the apparent count advantage vanishes under matched
pruning. The size of an entry is O(gn log q), so the transformations have polynomial
bit cost. Their actual arithmetic costs must be charged, not called zero.

For true curve orders, every division is exact. A failed divisibility check rejects
an inconsistent transcript. Successful divisions do not authenticate the original
orders or prove that arbitrary positive input numbers belong to a real curve.
The implementation retains this boundary.

## 3. Both transcripts recover the same polynomial

For Q=q^n and S_n=sum_i alpha_i^n, the inherited statistic can be written either as

$$
A_n=\frac Q2\log\frac{T_n}{K_n}
   =\frac Q2\log\frac{K_{2n}}{K_n^2}.
$$

Subtracting the two normalized logarithms is precisely the two-term Mobius
combination from Kedlaya's reconstruction [1], not a new cancellation principle.
Its expansion and the Weil bound give

$$
A_n=S_n+\sum_{j\ge3,\ j\ {\rm odd}}\frac{S_{nj}}{jQ^{j-1}},\qquad
|A_n-S_n|\le\frac{2g\sqrt Q}{3(Q-1)}.
$$

The retained rational logarithm enclosure, with numerical error <=1/12, isolates
S_n in the stated large-field regime. Compute n=1,...,g-2 and obtain
c_0=1,c_1,...,c_(g-2) by Newton identities. Both transcripts provide K_1 and T_1.
For g>=2 write

$$
R_+=K_1-\sum_{i=0}^{g-2}(1+q^{g-i})c_i,\qquad
R_-=T_1-\sum_{i=0}^{g-2}(-1)^i(1+q^{g-i})c_i.
$$

With s=(-1)^(g-1), the remaining coefficients are

$$
c_{g-1}=\frac{R_++sR_-}{2(q+1)},\qquad
c_g=\frac{R_+-sR_-}{2}.
$$

Reciprocity fills the upper half. For genus one, c_1=K_1-q-1. The endpoint step is
the same one retained in the previous assessment, now explicitly given to the
plain comparator. It specializes to the familiar low-genus curve/twist approach
of Sutherland [2]; no priority is asserted for those low-genus identities.

Thus pruning the base-change schedule also reduces its calls below the older
consecutive schedule in this large-field setting. This is a consequence of the
same cancellation and endpoint algebra, not a benefit exclusive to physical
twist access. The previous complete quantum zeta capability remains prior work.

## 4. The exact surviving cost difference

Let C_K(n) and C_T(n) be costs under one fixed accounting convention for obtaining
accepted individual orders of the original curve and fresh twist, respectively.
Let B_D and B_S account for shared setup and remaining processing on each route.
For a decomposable workflow the difference is exactly

$$
C_D-C_S=(B_D-B_S)+\sum_{n=1}^h\bigl(C_K(2n)-C_T(n)\bigr).
$$

The odd-anchor costs cancel. This is the precise surviving research hypothesis:
can the cheaper fields compensate for all twist/setup/certification costs in a
consequential implementation? Equal genus does not imply equal actual solver
cost on the original curve and its twist. Shared preprocessing and cross-call
batching must be represented in B or another correct nonadditive model.
A classical point counter can bypass all these group-order queries.

For sensitivity only, impose C_K(n)=C_T(n)=w(n) and equal B. Then

$$
C_D=\sum_{n=1}^h w(2n)+\sum_{r\in O_h}w(r),\qquad
C_S=\sum_{n=1}^h w(n)+\sum_{r\in O_h}w(r).
$$

Constant w gives exactly no saving. Increasing w favors the signed schedule
within this assumed model. With w(n)=n^k for fixed k>=0, set A=sum_(n=1)^h n^k
and B=sum_(r in O_h) r^k. The ratio is (2^k A+B)/(A+B), approaching

$$
\frac{2^{k+1}+1}{3}\quad\text{as }h\to\infty.
$$

It is a constant, not an improved asymptotic exponent. For the cubic and quartic
terms in Note 25's translation envelope, the respective limits are 17/3 and 11.
Logarithmic factors, numerical constants and complete workflow costs still matter.
These formal ratios are neither gate counts nor quantum/classical speedups.

## 5. Genus-ten comparison, without giving the comparator obsolete choices

Use the same illustrative size parameter q=1000003 and genus g=10, hence h=8.
There is no newly chosen large curve or native execution in this illustration.

| Schedule | Calls | Maximum extension degree | Sum of degrees |
|---|---:|---:|---:|
| Historical consecutive degree range 1..20 | 20 | 20 | 210 |
| Endpoint-completed, pruned plain comparator D_8 | 12 | 16 | 88 |
| Endpoint-completed signed schedule S_8 | 12 | 8 | 52 |

D_8 requests degrees 1,2,3,4,5,6,7,8,10,12,14,16. S_8 requests original-curve
degrees 1,3,5,7 and fresh-twist degrees 1,2,3,4,5,6,7,8. Relative to a fair plain
comparator, the count stays 12 while the largest field degree changes 16 to 8.

The unchanged Note 21/25 backend, with the same 12-call error allocation, gives:

| Quantity | Pruned plain | Signed | Meaning |
|---|---:|---:|---|
| Full-backend controlled translations | 265458395 | 152818614 | Upper-envelope operation accounting, not emitted gates |
| Initial-order-stage translations | 134867595 | 76629054 | Does not include completion/retries/fallback |
| Peak single-accumulator data bits | 6404 | 3204 | Includes degree tag; excludes other data and arithmetic workspace |

The first ratio is about 1.737, not the comparison with the historical 20-call
route. Weighting the two formal arithmetic monomials separately gives ratios
about 6.272 and 12.512. Unknown constants prevent combining those into a physical
number. Both routes have the same asymptotic genus powers under this envelope.
A smaller upper bound does not establish that an implementation is optimal.

## 6. Direct predecessor and originality assessment

Kedlaya [1, Sections 8-9] supplies normalized-log reconstruction and discusses the
2g-query question for cyclic resultants. The two-term combination is already
present in that machinery. His stated consecutive schedule is not itself an
optimized comparator for our restricted large-field setting.

Sutherland [2, Section 4.1, Lemma 4] supplies direct low-genus endpoint/twist
precedents. These support, rather than refute, the smaller-field implementation
idea; they prevent us from presenting it as a wholly new mechanism.

Hillar-Levine [3] concerns generic cyclic-resultant determination and polynomial
recurrences. Its generic statements are not minimum-query claims for integral
reciprocal Weil polynomials or for a source-aware algorithm. The recent
Roy-Saxena-Venkatesh preprint [4, Lemma 2.10] restates the consecutive reconstruction
as an ingredient. Its use of that schedule does not prove that our pruning is
new; an absence of an identical displayed schedule is not a priority certificate.

The result here is a necessary comparator theorem: the same algebra lowers the
query count on BOTH sides, and twist access changes representation costs. It
does not resolve the global minimum-query problem, establish a lower bound on
classical point counting, or prove a new useful quantum capability. A standalone
publication claim for the present call-count saving is not supported.

## 7. Executed checks and stopping decision

The new diagnostic verifies 128 exact transcript round trips against independently
traversed dyadic chains; runs both reconstructions on 12 supplied factored Weil
polynomials; checks 24 individual orders through companion determinants; retains
the inherited genus-one and genus-two controls; and verifies 640 homogeneous
cost identities plus ten malformed-input controls. A deliberate unequal-cost
control reverses the signed/plain preference, guarding against an unconditional
cost claim. These are targeted correctness checks for the comparison, not
application-scale discovery evidence. No new curve or group cardinality is found.

The existing translation-cost and subgroup-stopping verifiers passed unchanged
from the mounted checkpoint. The new report is independently regenerated by its
verifier. A full Git checkout failed because the container could not resolve
GitHub; the live branch was read and updated through the GitHub connection.
The root historical verifier, 164-curve suite, native point counters and quantum
circuits were not run. Historical experiment bytes and LICENSE are unchanged.

Retain this cost-placement refinement inside Quantum-Assisted-Algorithm-Discovery.
It has not become an independently justified spinoff. Stop schedule-only iterations
whose proposed contribution is fewer calls than an unpruned old schedule. A further
zeta implementation step needs one predeclared consequential resource/capability
claim, using D_h as an eligible baseline and allowing methods that bypass it.
Otherwise retain this as supporting research while pursuing the broader compact-
input quantum-discovery objective. Do not automatically start a general arithmetic
compiler or manufacture a difficult curve family. Manuscript stays on hold.

Primary links, inspection scope, and dependency hashes are in
[SOURCES.md](../../experiments/reconstruction_comparator_v1/SOURCES.md).
