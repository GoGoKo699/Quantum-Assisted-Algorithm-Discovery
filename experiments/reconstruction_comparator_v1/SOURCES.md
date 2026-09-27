# Sources and comparison boundary

Inspected 27 September 2026. New code is independently written; no external
implementation is imported. The exact pruned comparator is derived in Note 26,
not asserted to appear verbatim in these papers.

1. K. S. Kedlaya, **Quantum computation of zeta functions of curves**,
   computational complexity 15 (2006), 1-19; arXiv:math/0411623v3.
   https://arxiv.org/pdf/math/0411623
   Sections 8-9 were read in parsed primary text. PDF page index 13 was rendered
   and visually checked for the cyclic-resultant/query discussion; index 11's
   screenshot failed. The normalized Mobius sum and consecutive query range are
   prior work. No timing or table data are used.

2. A. V. Sutherland, **A Generic Approach to Searching for Jacobians**,
   Mathematics of Computation 78 (2009), 485-507; arXiv:0708.3168.
   https://arxiv.org/pdf/0708.3168
   Section 4.1 and Lemma 4's endpoint/twist reconstruction were read. Repeated
   screenshots of page index 10 failed; no table or figure was used. Low-genus
   reconstruction is a direct predecessor. Its special formulas are not extended
   to variable genus by attribution; Note 26 gives its own elementary endpoint step.

3. C. J. Hillar and L. Levine, **Polynomial recurrences and cyclic resultants**,
   arXiv:math/0411414v4 (2006).
   https://arxiv.org/abs/math/0411414
   Primary abstract/version metadata inspected. Generic reconstruction scope is
   not an efficient worst-case algorithm or a minimum-query bound for the promised
   Weil-polynomial class. No full proof or completeness-of-priority audit claimed.

4. D. Roy, N. Saxena and M. Venkatesh, **Complexity of counting points on curves,
   and the factor P_1(T) of the zeta function of surfaces**, arXiv:2511.02262v1
   (2025), preprint.
   https://arxiv.org/html/2511.02262v1
   Introduction, Lemma 2.10, and surrounding group-cardinality/verification scope
   inspected. Lemma 2.10 uses the consecutive max(18,2g) reconstruction. This is
   not evidence that the elementary pruned schedule is new. No implementation,
   higher-cohomology capability, or interactive-verification guarantee is imported.

A focused public search for quantum zeta reconstruction, cyclic resultants, and
quadratic twists did not locate a directly stated theorem identical to the
pruned schedule. This is an incomplete priority search, not a novelty conclusion.
The conclusion supported by the direct algebra is comparator equivalence and
cost placement, independent of whether that pruning has appeared elsewhere.

## Internal mathematical and byte provenance

- Base branch: research/prx-quantum-phase2.
- Base commit: 8daa8ae16458acd25155179ad2ab35a97f600b40.
- Reconstructed endpoint schedule: h=max(1,g-2) for g>=2, as retained in the
  earlier assessment and Notes 22-25. Genus one is handled separately.
- One genuine low-genus polynomial control is the inherited
  y^2=x^5+x^2+x+1 over F_5, P=[1,4,10,20,25], K_1=60, T_1=12, K_2=720.
  The curve is not newly enumerated. Larger tests supply factored Weil polynomials
  and generate their orders by elementary quadratic-root recurrences.
- The arithmetic-envelope dependency is unchanged
  experiments/translation_cost_v1/cost.py, Git blob recorded in MANIFEST.json
  together with its SHA256. Source/report files of that predecessor are not edited.
- The mounted Note-25 checkpoint was extracted into a fresh directory; both of
  its existing verifiers passed unchanged. A full checkout failed on DNS, so no
  full-repository or 164-curve verification is claimed.

No new field, Jacobian, native point counter, order-finding circuit or hardware
was executed. Query and formal arithmetic counts are symbolic diagnostics,
not evidence of quantum advantage. Full error/fallback/setup accounting is still
required by any future complete-resource claim.
