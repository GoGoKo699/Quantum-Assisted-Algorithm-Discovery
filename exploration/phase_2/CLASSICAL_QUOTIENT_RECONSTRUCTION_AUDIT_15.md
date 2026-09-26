# Learn the coordinates and residual evaluator together

26 September 2026. Phase 2; PRX Quantum target; manuscript remains on hold.
Live base: 01f63cf940961dd1608d3595e484638bade63ca3.
This is a condensed comparator audit, not a new sparse-Fourier algorithm,
production benchmark, or useful quantum-advantage claim.

## 1. What changed

The preceding scout separated quantum coordinate discovery from construction
of a reduced truth table. A stronger classical competitor can obtain both in
the same calculation. Under an exact Fourier-dimension promise r<=k, a random
restriction and its single-bit-shifted copies reconstruct the coordinate masks
and the complete residual evaluator using O(n*2^k) ordinary function evaluations
at fixed confidence. Restriction/hash-and-shift decoding is established classical
machinery [1-3], not an innovation claimed by this project.

An arbitrary Boolean residual on r bits has 2^r table entries. Thus a fast test
for low dimension does not automatically supply an exponentially faster complete
classical replacement. Polynomial improvements in other parameters, useful
coordinate maps without full tables, and succinct residual programs remain open.
This is not a general no-go theorem for quantum-assisted model reduction.

## 2. Explicit classical construction

Let f:F_2^n -> [-1,1] have exact finite-precision values, represented by B-bit
integer numerators and a known common scale. Both competitors receive its source
and may inspect/simplify it. The reference algorithm uses only chosen-input
ordinary evaluations. Let W span its nonzero Fourier labels, with dim W=r<=k.
Choose an n-by-t matrix A with independent uniform binary columns, where

    t = k + ceil(log_2(1/delta)).

If t>=n, evaluate the full n-input truth table once and use its Walsh transform,
rather than doing n+1 redundant full-domain scans. Otherwise set

    h_0(u)=f(Au),              u in F_2^t,
    h_i(u)=f(Au+e_i),          i=1,...,n.

For any nonzero s in W, Pr[A^T s=0]=2^(-t). Union bounding over W gives

    Pr[A^T is not injective on W] <= (2^r-1)*2^(-t) < delta.

On the injective event there is no collision among active Fourier labels:

    hat(h_0)(a) = sum_(s:A^T s=a) hat(f)(s),
    hat(h_i)(a) = sum_(s:A^T s=a) (-1)^(s_i) hat(f)(s).

Each nonzero restricted coefficient therefore represents exactly one original
coefficient. Its sign change in h_i reveals the original label's i-th bit.
Select a basis a_1,...,a_r of the restricted Fourier support and recover the
corresponding original labels s_1,...,s_r. Their rows define M'.

The initial restricted values also supply the residual table G:

    G(a_1.u,...,a_r.u) = h_0(u),
    f(x)=G(M'x).

All reduced keys are covered. No additional 2^r source calls are needed to fill
G. Different recovered bases give equivalent exact representations.

The implementation computes exact integer Walsh transforms, compares c and -c
only for nonzero c, checks decoded-mask projections, and checks every already
queried shifted-slice value. These checks are not an unconditional equivalence
certificate on unqueried inputs. A failed random restriction can pass them.
The exact rank promise and the probabilistic capture event are essential.

The direct costs are (n+1)*2^t requested function values, with repeated inputs
cached, and O((n+1)*t*2^t) transform arithmetic plus binary linear algebra and
input construction. A full statement is

    (n+1)*2^t*C_f + 2^t*poly(n,t,B),

where C_f is actual classical evaluator cost. The saved model has O(nr+B*2^r)
bits. Working memory is exponential in k in this reference implementation.
No original-input polynomial-workspace claim is made. At fixed confidence and
a tight k=r, the total cost is 2^r times polynomial factors, not 2^n.

This is an exact promised-input result. Approximate low dimension, noisy outputs,
unknown suitable k, general real arithmetic, and source-equivalence certification
require separate analysis. The exact identity, when correctly recovered, holds
for every x and hence any deployment distribution; its approximate predecessor's
uniform-input MSE guarantee should not be confused with that statement.

## 3. Direct prior art and a stronger generic comparator

Gopalan et al. [1] give exact proper learning and low-dimensional reconstruction
results in addition to property testing. Cheraghchi and Indyk [2] give general
sparse Walsh recovery, with roughly linear dependence on sparsity in the
randomized version up to factors polynomial in logarithmic ambient dimension.
For exact sparsity its approximation guarantee becomes exact reconstruction.
Here the sparsity is at most 2^r. These methods already prevent an assumption
that classical recovery requires examining all 2^n inputs.

Spencer, Bharti and Gorshkov [3] explicitly state the shifted-folding identity
and coordinate-bit sign decoding in their 2026 Pauli-decomposition preprint.
Their matrix problem and full algorithm are different. The present function
algorithm specializes standard tools to a low-dimensional span and has its own
short capture proof; it is not an execution or improvement of their matrix
algorithm. The independently written reference code imports no upstream solver.

The recent Fourier-dimensionality testing preprint from the previous scout was
again not retrievable in full. No new result here relies on its indexed abstract,
and its testing claims are not treated as complete evaluator-construction claims.

## 4. The table and the structure are different outputs

A low-dimensionality tester, a coordinate learner, and a deployed evaluator solve
different tasks. For fixed known coordinates an arbitrary r-bit Boolean table
contains 2^r independent bits. Writing that table entails its output length.
In the oracle model, recovering all entries also recovers their parity, giving
a linear-in-table-size quantum query lower bound by the polynomial method [5].
Oracle interrogation [4] essentially matches that scale up to a constant, not
poly(r) queries. These are not lower bounds for a residual promised to have a
compact formula, or for an application requiring only some table entries.

Lazy memoization avoids constructing unused entries but does not determine an
unseen key. Both sides can use caching and exploit actual key recurrence. The
same coordinate map may be worthwhile without a table if it reorganizes an
existing solver; that requires an explicit downstream benefit, not a free
residual-evaluation oracle. A succinct residual should be represented by its
actual program, not deliberately expanded to manufacture cost.

The permitted conclusion is narrow: full-table construction does not inherit
an exponential-in-r end-to-end advantage merely from a fast quantum coordinate
test. Improvements in n, source-evaluation cost, approximation, or a different
output remain possible. No blanket classical domination is established.

## 5. Checks actually executed

All arithmetic in the new reference implementation and checks is exact integer
or rational arithmetic. There is no quantum simulation or hardware result.

All 256 sign functions on three bits were paired with all 64 two-column maps:
16384 cases. All 2144 injective cases returned the exact minimal-rank quotient,
with 17152 output predictions checked. Of the noninjective cases, 13670 were
rejected by local consistency checks and 570 returned incorrect models. Those
failures are retained explicitly. Exact capture rates for true ranks 0,1,2,3
were 1,3/4,3/8,0, agreeing with the finite random-matrix formula.

Sixty bounded five-bit functions were checked with seven-column restrictions.
All 48 injective restrictions reconstructed correctly; 1536 outputs were checked.
The old eight-bit illustration used 288 requested evaluations at 160 distinct
inputs and returned an eight-entry evaluator correct on all 256 inputs. Its
source-visible masks and the earlier 37-query quadratic reconstruction remain
stronger classical routes for that specific function.

A synthetic 32-input, six-coordinate function used 33792 distinct evaluations
and returned a 64-entry table. Equality of coordinate spans and all 64 reduced
truth values provides an algebraic check for that supplied family; 2048 random
inputs were also replayed. The 2^32-input domain was NOT enumerated. The source
itself contains the masks/table, so the example is deliberately not a hard
workload or evidence of quantum advantage.

A zero restriction of a true rank-two quadratic passes all local checks yet
returns a constant wrong on four of sixteen inputs. A separate cache control
has two functions agreeing on seven observed keys and disagreeing on the eighth.
These controls expose the correctness boundary rather than suppress failures.

The new report regenerated byte-for-byte. The supplied predecessor coordinate-
quotient checkpoint verifier passed unchanged. Root/historical verifiers,
production logic tools, general sparse-transform packages, and native quantum
resource estimates were not run. The manuscript stays on hold.

## 6. Reproducibility and next decision

Expanded proofs, exact source, saved model, results and verifier are in the
conversation checkpoint Quantum_Discovery_Quotient_Reconstruction_Audit.zip.
This repository commit contains only the present condensed note.

reconstruct.py SHA256:
17fb3cbe188ceee631778e4839d8799935ad9c45015099fbf19c33f6eff82bac
check.py SHA256:
4c28678a082062de3c9cf080df3739716ed05283678a1f2371897486138364f7
results.json SHA256:
6211c49478824b68c124f14d2668230d9c1210c4d1c105ac938540a377cfe05d

Run `python verify.py` inside the checkpoint. Standard library only. Existing
reports are never overwritten; -O/-OO is rejected by the verifier.

Retain representation discovery, but require the proposed coordinate map to
change a useful downstream computation without hiding another hard task in the
residual. Do not turn a different property-testing output into an application
advantage or demand a new framework merely to preserve the current direction.
No outside contact, submission, paid computation, or administrative change.

## Primary sources and inspection scope

[1] Gopalan et al., Testing Fourier Dimensionality and Sparsity, SICOMP40,
1075-1100 (2011). Primary PDF Sections1.2 and8 inspected; screenshot failed.
https://doi.org/10.1137/100785429
https://www.cs.columbia.edu/~rocco/Public/4-27-2011-gossw.pdf

[2] Cheraghchi and Indyk, Nearly Optimal Deterministic Algorithm for Sparse
Walsh-Hadamard Transform, TALG13(3),34 (2017); SODA2016 precursor. Primary PDF
Sections1.1-1.2 and author-institution metadata inspected; screenshot failed.
https://doi.org/10.1145/3029050
https://arxiv.org/abs/1504.07648

[3] Spencer, Bharti, Gorshkov, An efficient Pauli decomposition algorithm for
structured matrices, arXiv:2606.31952v1 (30 June2026), Lemma3 and Eqs25-37.
Primary PDF page5 parsed equations inspected; screenshot failed. No figure or
table-derived performance claims; no native execution.
https://arxiv.org/abs/2606.31952

[4] van Dam, Quantum Oracle Interrogation: Getting All Information for Almost
Half the Price, FOCS1998. Primary abstract inspected for whole-oracle recovery.
https://doi.org/10.1109/SFCS.1998.743486
https://arxiv.org/abs/quant-ph/9805006

[5] Beals et al., Quantum Lower Bounds by Polynomials, FOCS1998/JACM2001.
Primary abstract inspected for parity-query bounds; full-table-to-parity
transfer is immediate, not a new query theorem.
https://arxiv.org/abs/quant-ph/9802049
