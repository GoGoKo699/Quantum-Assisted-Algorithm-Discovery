# Primary-source audit and source boundaries

Inspected 27 September 2026. The source comparisons are not native executions,
a complete literature search, or a priority claim for a new algorithm. No external
solver or arithmetic source is copied into this experiment. Sources are numbered
as in [Note 25](../../exploration/phase_2/FAMILY_AND_TRANSLATION_COST_25.md).

1. **Simon Abelard, Pierrick Gaudry and Pierre-Jean Spaenlehauer, Improved
   Complexity Bounds for Counting Points on Hyperelliptic Curves**, arXiv
   1710.03448v2 (2018). https://arxiv.org/pdf/1710.03448 . Section 2, Theorem 1
   and its fixed-genus interpretation were read; PDF index 0 was rendered. The
   precise hypothesis includes q>q_0(g) and p>=(log q)^(c g). The notation O_g
   can hide rapidly growing genus-only factors. This is not a uniform finite
   runtime model at g growing with log p. Section 2 also specifies the local-zeta
   task and Mumford representation, and cites fast Cantor group operations.

2. **David Harvey, Kedlaya's algorithm in larger characteristic**, arXiv
   math/0610973v2 (2007). https://arxiv.org/pdf/math/0610973 . Theorem 1 and the
   discussion of precision were read; PDF index 0 was rendered and the formula
   checked visually. The matrix bound is Otilde(p^(1/2) k^(5/2) g^omega a +
   k^4 g^4 a log p), subject to p>(2k-1)(2g+1). The precision is not a fixed
   constant when the genus grows. No timing table is used or reproduced.

3. **David Harvey, Counting points on hyperelliptic curves in average polynomial
   time**, Annals of Mathematics 179 (2014), 783-803.
   https://annals.math.princeton.edu/2014/179-2/p07 . The primary abstract fixes
   one integer polynomial and obtains all good odd-prime reductions below an
   input bound. Its average-polynomial statement is a batched result; it must
   not be transferred to a single arbitrary large prime for free. Conversely,
   that batch capability must not be withheld when it matches the workload.

4. **Kiran S. Kedlaya, Quantum computation of zeta functions of curves**, arXiv
   math/0411623v3; published 2006. https://arxiv.org/pdf/math/0411623 . Abstract
   and introduction were reread; PDF index 0 was rendered. The polynomial-time
   quantum zeta capability is established prior work. No original quantum
   advantage claim is made for reinstantiating it with the present fallback
   arithmetic. Detailed reconstruction boundaries remain in Notes 19-22.

5. **Simon Abelard, Counting points on hyperelliptic curves with explicit real
   multiplication in arbitrary genus**, arXiv 1810.11068; Journal of Complexity
   57 (2020), 101440. https://arxiv.org/abs/1810.11068 . Primary abstract/scope
   inspected. The favorable exponent in log q is stated for fixed genus and
   explicit real multiplication. It is not a general variable-genus bound, nor
   an excuse to ignore known structure in an input curve. No implementation run.

6. **Andrew V. Sutherland, A Generic Approach to Searching for Jacobians**,
   Mathematics of Computation 78 (2009), 485-507; arXiv 0708.3168.
   https://arxiv.org/pdf/0708.3168 . Parsed Section 4, its conditional exponent
   algorithms and group-operation model were inspected. These are stronger
   classical options than generic unstructured enumeration. No sample-size or
   hardness distribution is imported, and no timing table is used. They do not
   force a source-aware point counter to compute group orders at all.

7. **SageMath, Jacobian morphism / Cantor composition and reduction documentation**.
   https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/hyperelliptic_curves/jacobian_morphism.html .
   The public API explicitly distinguishes composition from reduced canonical
   output; validity and unique reduction contracts were inspected. A live source
   read of `src/sage/schemes/hyperelliptic_curves/jacobian_morphism.py` returned
   blob `ef9616a5a890a5066022ce3b163b3e84afe316a0`; only its representation and
   validation section was read. The direct AMS PDF for Cantor's original 1987
   paper could not be fetched. Neither Sage nor an upstream Cantor implementation
   was run, modified or copied. The padded construction in Note 25 is specified
   independently; its bound is not attributed as Sage's measured complexity.

8. **Charles H. Bennett, Logical Reversibility of Computation**, IBM Journal of
   Research and Development 17 (1973), 525-532, DOI 10.1147/rd.176.0525.
   Primary-paper text mirrored at
   https://www.cs.princeton.edu/courses/archive/fall04/cos576/papers/bennett73.html .
   The compute/copy/reverse construction was inspected. Storing history costs
   workspace; it is not an O(data-width)-space compiler. The 1989 time/space
   tradeoff was also screened, but its constants and machine-to-gate conversion
   are not used in the present bounds.

9. **A. Barenco et al., Elementary gates for quantum computation**,
   arXiv quant-ph/9503016 (1995).
   https://arxiv.org/abs/quant-ph/9503016 . Primary abstract and elementary-gate
   scope inspected. The only use is the standard constant-cost conversion of
   fixed-size reversible gates; no physical error-correction or architecture
   resources are transplanted.

A supplementary current-public-source screen read **Madeleine Kyng, Computing zeta
functions of algebraic curves using Harvey's trace formula**, Research in Number
Theory (2022), DOI 10.1007/s40993-022-00398-7,
https://link.springer.com/article/10.1007/s40993-022-00398-7 . The paper explicitly
distinguishes its p^(1/2+o(1)) theorem outline from its p^2 implementation.
Therefore its native timings cannot be represented as execution of the stated
asymptotic bound. No table/figure data are used. This reinforces the separation
between mathematical envelopes and measured solver performance in Note 25.

## Internal provenance

Live base: `af9dc73040c24352ab1b71b0339d3a55b01cfaef`.
The inherited subgroup checkpoint was supplied as a mounted ZIP. Its verifier
passed unchanged. This experiment reconstructs Note 21's parameter arithmetic
independently; it does not claim to import its unavailable source archive.
The actual ordered query multiset is recorded in REPORT.json. For the historical
twist schedule it means T_n for n=1..10, then K_n for odd n=1,3,5,7,9 (only degree
and genus affect this envelope). The order of this bookkeeping is not the
physical execution order or a new reconstruction proof.
