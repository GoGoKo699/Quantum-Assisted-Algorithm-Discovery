# Change coordinates before declaring the model inseparable

26 September 2026. Phase 2; manuscript remains on hold.
Base read: eabdd319ee52750d0dd72bfe3b573ac0d6997c1b.
This is a condensed exploration record. The expanded proof, exact diagnostic,
model, verifier and receipts are in Quantum_Discovery_Coordinate_Quotient_Scout.zip.
No new quantum primitive, useful hard workload or end-to-end advantage is claimed.

## 1. Change in the proposed output class

The preceding scouts split original variables into additive blocks. A model
can be inseparable in that form while depending on very few combinations of
its inputs. For f(x)=(-1)^(x_1+...+x_n), every nontrivial additive coordinate cut
has uniform-input MSE one. The single parity z=x_1 XOR ... XOR x_n determines
f exactly. This is a trivial classical example, not a speedup witness.

The new candidate is a classical input transformation followed by a smaller
model, rather than a partition of the original labels. Fourier dimension,
parity juntas and linear structures are established concepts [1-3]. Classical
logic synthesis already uses spectral linear input transformations [5].

## 2. Exact reduction

For an explicit deterministic f:{0,1}^n -> [-1,1], under uniform independent
inputs, let W_* be the binary linear span of all labels s with fhat(s)!=0.
If dim W_*=r and M has a basis of W_* as its rows, then

    f(x)=g(Mx),
    f(x+v)=f(x) for every x iff v belongs to W_*^perp.

Addition and matrix operations here are over F_2. Each Fourier character is a
parity of Mx. Equivalently, the orthogonal complement is the translation space
that leaves f unchanged. These are standard Fourier-duality identities.

Compute a right inverse R, MR=I_r, by Gaussian elimination. Then

    g(z)=f(Rz),    f(x)=f(RMx).

One can fill a reduced table with 2^r classical calls and deploy it using r
parities and one lookup. The masks need O(nr) bits; table storage and input
processing are not free. Alternatively, canonicalize inputs and cache only
encountered keys; each new key still needs an f evaluation. Identifying M does
not give the values or a cheap formula for an arbitrary residual g. A full
r-input Boolean table contains 2^r potentially independent bits.

## 3. Approximate projection and a stopping rule

For any proposed W with row matrix M, the best mean-square approximation
using only Mx is P_W f(x)=E[f(X)|MX=Mx]. Parseval gives

    L(W)=E[(f-P_W f)^2]=sum_(s notin W) fhat(s)^2.

The inherited raw signed Fourier sampler returns s with probability fhat(s)^2
and NULL with probability 1-E[f^2]. NULL and zero never count as outside W.
Thus the chance of obtaining a new direction is exactly L(W). We do not
postselect away the failed amplitude flag or assume its normalization known.
Reversible f evaluation, its inverse, amplitude conversion and transforms remain
part of every implemented sampling cost.

An elementary conservative rule starts at W={0}. Put

    h=ceil(log((n+1)/delta)/epsilon).

Add each sampled vector outside W and restart a counter. Stop after h consecutive
inside/NULL records, or at rank n. If the current L(W)>epsilon, that stage stops
incorrectly with probability at most exp(-epsilon*h). At most n+1 stages occur,
so the returned space has L(W)<=epsilon except with probability delta. There
are at most (n+1)h raw trials, or (r+1)h if the actual exact Fourier dimension is
r. This is a simple span-learning certificate, not a new optimal tester.

The algorithm can return all n coordinates. It is not an agnostic minimum-rank
learner: tiny outlying Fourier components can inflate the span. Noise needs a
separate budget. Absence of a sampled direction cannot certify exact invariance;
exact source equivalence would need an algebraic or exhaustive certificate.

For any fixed M there is also a two-evaluation CLASSICAL diagnostic. With X
uniform and V independently uniform in ker M,

    L(W)=(1/2) E[(f(X)-f(X+V))^2].

This follows by expanding the square and using P_W as an orthogonal projection.
For sign f, L(W)=2 Pr[f(X)!=f(X+V)]. Validation is not exclusively quantum.

## 4. An approximate quotient is not automatically a safe cache key

For exact invariance, any representative of a key works. For approximate
invariance, always substituting RMx can be arbitrarily bad relative to L(W).
A rare anomalous representative can be reused for many ordinary inputs.

Choose A uniformly in ker M once and define g_A(z)=f(Rz+A). Then the exact
average-over-sections identity is

    E_A E_X[(f(X)-g_A(MX))^2]=2L(W).

Within a fiber, the original X and randomly selected representative are independent
uniform draws; their squared difference averages to twice the conditional variance.
This is an expectation, not a high-probability deployment guarantee. Fitting
conditional means or independently validating a selected section has a cost.

Control: f is +1 except f(0)=-1 on ten bits. Taking W={0} gives
L=1023/262144, approximately .00390. Always using the zero representative gives
MSE1023/256, approximately3.996. A random representative has mean MSE2L. The
exact Fourier dimension is ten. This example is easy classically and exposes
an invalid use of an average-case certificate, not a hard problem.

## 5. Nonlinear illustration and an explicit classical opponent

On eight input bits, define z_j=parity(m_j AND x) for masks170,204,241, and

    f(x)=(-1)^((z_1 AND z_2) XOR z_3).

All eight original inputs matter. Its four nonzero Fourier coefficients are
c_241=c_91=c_61=1/2 and c_151=-1/2. Each label has Hamming weight five.
Consequently every additive partition with blocks of at most four inputs has
best MSEone. In parity coordinates, a three-bit, eight-entry table reproduces
all256 inputs exactly. Coordinate dependence and interaction order are different.

The diagnostic computes this Fourier law CLASSICALLY and samples it with seed
2026092614. Its first three draws span the true space. The conservative stopping
rule uses140 total draws at epsilon=.05,delta=.01, including137 final confirming
draws. This is not a gate-based quantum sampler or a hardware run.

The source already exposes the three masks, which a classical method may simply
read. A second independent baseline exploits the source's degree-at-most-two
Boolean polynomial: zero, single-bit and two-bit evaluations reconstruct it in
1+8+binom(8,2)=37 classical calls. Its polar form and one kernel constraint recover
the same three-coordinate space. All256 outputs are verified. We do not hide
that cheap classical route or present the sampled masks as a new discovery.

## 6. A relevant new preprint does not settle our application

Gopalan et al. [1] identify small Fourier dimension with a small number of parity
features. Their Theorem1.4 gives an Omega(2^(k/2)) classical query lower bound for
fixed-tolerance testing, including adaptive queries. This is not a lower bound
for every program whose source is supplied. Their reconstruction and implicit
learning algorithms remain classical competitors.

Li and Yang [3] already use Fourier samples and linear equations to find Boolean
linear structures. The span/nullspace mechanism is therefore direct prior art.

Kenny Chen's preprint submitted22 September2026 [4] reports an exponential
quantum/classical query separation for testing Fourier dimensionality and an
improved classical tester. Only its primary arXiv-indexed abstract was retrievable;
full PDF/HTML and direct abstract-page attempts failed. Precise tolerance bounds
and proofs were not audited. It is an important overlapping reference, not a
result reproduced here. The elementary derivations above do not rely on it.

A property tester, a coordinate learner, and a usable compressed evaluator have
different outputs and costs. A 2^r table-construction step may dominate a small
quantum testing cost. Both methods may use symbolic simplification, low-degree
algebra, sparse Fourier learning, decision diagrams, classical spectral methods,
and caching. Neither is obliged to reproduce the other's intermediate records.

## 7. Research decision and actual checks

Keep a candidate with a concrete classical product: a useful input transformation
and residual evaluator. Do not infer usefulness from a small dimension alone.
Transforming inputs can cost more than it saves or destroy locality needed by
other operations. Uniform-input MSE does not establish worst-case correctness,
shifted-input reliability or exact memoization. A classical API is not coherent
access, and independent biased inputs need not remain independent after a parity
transformation. Stochastic programs need an explicit treatment of randomness.

The decisive missing result is a naturally occurring source-aware task where
finding the relevant combinations is genuinely costly classically and makes
later computation sufficiently cheaper. Deliberately concealing a known matrix
inside an artificial oracle does not provide that result. The manuscript remains
on hold; no submission, outside contact or paid computation was initiated.

Actual exact checks:274 bounded functions;5302 function/subspace projection
identities;192864 translated pairs;192864 random-section predictions;2336 exact
quotient outputs;2336 period tests;274 direct-sum/Hadamard-transform comparisons.
The saved illustrative model was replayed on all256 inputs using only its masks
and table. The source-aware37-query classical reconstruction was also verified.

The report and model regenerated byte-for-byte. The supplied predecessor
split_and_fit_check.py was rerun unchanged and reproduced its reference report.
No root/historical verifier or production synthesis tool was run. No physical
quantum circuit or scalable gate resource estimate was produced.

Companion source SHA256:
0d19ddfda9910c8e7b48865322a6c5d30b9b0419848bf3b0174aa0376c42d90e
Exact result SHA256:
1ed4ae8f46e2b6707dcbf894a4d833413a7cd740f40f52ea482ea3c470fddb05
Expanded note SHA256:
c3702226d1ca8be0bbf8b241cb774b80af205f14744b4323481c9660d7b2d840

The companion checkpoint is supplied in the conversation, not represented as
committed source. Run its standard-library verifier with `python verify.py`.
This scoped repository change adds only the present condensed note.

## Sources and inspection scope

[1] Gopalan, O'Donnell, Servedio, Shpilka, Wimmer. Testing Fourier Dimensionality
and Sparsity, SIAM J. Comput.40(4),1075-1100 (2011).
https://doi.org/10.1137/100785429
https://www.cs.columbia.edu/~rocco/Public/4-27-2011-gossw.pdf
Parsed primary text, Definition1.1 and Theorem1.4 inspected. Web screenshot
attempt failed; no table/figure-derived performance claim.

[2] Sanyal. Sub-linear Upper Bounds on Fourier dimension of Boolean Functions
in terms of Fourier sparsity (2014). https://arxiv.org/abs/1407.3500
Primary abstract and first-page scope; Fourier dimension/non-adaptive parity
query relationship. Screenshot attempt failed.

[3] Li and Yang. A quantum algorithm to approximate the linear structures of
Boolean functions. https://doi.org/10.1017/S0960129516000013
https://arxiv.org/abs/1404.0611
Primary abstract and parsed PDF Sections2-4. Screenshot attempt failed. No
cryptographic application is proposed here.

[4] Kenny Chen. Exponential Quantum Advantage in Testing Fourier Dimensionality.
https://arxiv.org/abs/2609.25816
Submitted22 September2026. Primary indexed abstract only; full paper unavailable
in this pass. No claim of independent verification or publication beyond preprint.

[5] Falkowski. Spectral Methods for Boolean and Multiple-Valued Input Logic
Functions, Portland State University doctoral dissertation (1991).
https://pdxscholar.library.pdx.edu/open_access_etds/1152/
https://doi.org/10.15760/etd.1151
Author/institution abstract inspected for established spectral input transformations;
no performance claim transferred from that work.
