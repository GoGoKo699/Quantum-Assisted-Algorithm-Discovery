# Predecessor comparison and provenance

Inspected 27 September 2026. Sources below were read through the web tool as
primary documents, not inferred from summaries in earlier conversations. No
third-party source code is imported. A focused search is not a certificate that
no predecessor exists. The full mathematical proof here is independently derived
from the attributed ingredients, and is not a claimed quotation from a paper.

## 1. Kiran S. Kedlaya

Quantum computation of zeta functions of curves, Computational Complexity 15
(2006), 1-19. arXiv:math/0411623v3, 30 November 2005.
https://arxiv.org/pdf/math/0411623
https://arxiv.org/abs/math/0411623

Primary Sections 8-9 were read, including the cutoff-dependent Mobius formula,
Newton residue information, consecutive max(18,2g) schedule, and explicit query-
count question. PDF page index 13 was rendered and read. Section 8 also records
the separate condition used to acquire orders via Proposition 11. That condition
must not be dropped when interpreting an abstract reconstruction as an executed
quantum algorithm. The metadata identifies v3 as the refereed version.

The present construction uses the same normalized power-sum approximation, not
a new cancellation principle. The sparse input support, varying cutoff within
that support, all-field g>=32 tail bound and range-reduced decoder are proved in
Note 28. No statement identical to that theorem was found in the inspected text.
The polynomial-time quantum zeta capability is fully prior work.

## 2. Andrew V. Sutherland

A Generic Approach to Searching for Jacobians, Mathematics of Computation 78
(2009), 485-507; arXiv:0708.3168.
https://arxiv.org/pdf/0708.3168

Parsed Section 4.1 and Lemma 4 were read. The lemma concerns genus at most three
and sufficiently large q, with unconditional exact endpoint algebra in genus two.
It is a direct predecessor for endpoint/twist reasoning. The page-index-10
screenshot failed; no figure/table-derived claim is used. No timing is reproduced.
The present variable-genus theorem is not attributed to that low-genus lemma.

## 3. Christopher J. Hillar and Lionel Levine

Polynomial recurrences and cyclic resultants, arXiv:math/0411414v4,
7 November 2006; Proceedings of the AMS.
https://arxiv.org/pdf/math/0411414
https://arxiv.org/abs/math/0411414

Introduction, Theorem 1.1 and Conjecture 1.2 were read in the primary PDF text.
Their generic monic result has 2^(d+1) initial resultants; the generic monic
palindromic even-degree case has 2*3^(d/2). Their short-initial-segment conjecture
is not a proved optimal query theorem for q-reciprocal integer Weil polynomials.
A polynomial recurrence of short length is not automatically an effective
worst-case reconstruction with that many observations. No full proof audit or
runtime comparison is claimed here.

## 4. Christopher J. Hillar

Cyclic Resultants, Journal of Symbolic Computation 39 (2005), 653-669;
arXiv:math/0401220v3, 28 April 2005.
https://arxiv.org/pdf/math/0401220
https://www.sciencedirect.com/science/article/pii/S0747717105000374

Primary introduction and Theorem 1.1 were read. The characterization concerns
identical full nonzero cyclic-resultant sequences. It does not state our finite
selected-data or all-field polynomial-time bound. Bibliographic information was
checked on the publisher page. No native reconstruction implementation was run.

## 5. Diptajit Roy, Nitin Saxena and Madhavan Venkatesh

Complexity of counting points on curves and the factor P_1(T) of the zeta function
of surfaces, arXiv:2511.02262v1, 4 November 2025.
https://arxiv.org/html/2511.02262v1
https://arxiv.org/abs/2511.02262

The primary HTML Lemma 2.10 explicitly assumes the consecutive max(18,2g) counts;
Lemma 2.11 and surrounding verification discussion were read. Current retrieved
metadata lists v1. This is a preprint in the inspected record. Its use of the
older reconstruction is not proof of our priority. The certification and surface
results are not reproduced or imported as new claims.

## Search scope

Focused public searches covered "cyclic resultants" with reconstruction and Weil
polynomials; "Kedlaya" with fewer-than-2g, oracle calls, reconstruction and
cardinalities; and zeta reconstruction/Jacobian query terms, including arXiv-
restricted checks. Many results were irrelevant or secondary and were not used.
The inspected primary statements do not subsume the exact candidate theorem.
This does not exclude an unindexed paper, thesis, implementation or implicit
corollary elsewhere. Publication priority remains unresolved.

## Executed and unexecuted work

The new source independently implements exact rational range reduction and
Mobius/Newton/endpoint reconstruction. All source and expected report bytes are
pinned in MANIFEST.json. Seven test polynomials are constructed from specified
quadratic factors and factors 1+q^a*T^(2a); they have the required Weil/reciprocity
properties but are not claimed to be Jacobians. Only q,g and requested K-values
are passed to the decoder. A separate companion-matrix determinant routine checks
36 small factor-generated orders.

The mounted Note-27 archive was extracted and all four current verifiers passed.
Their local Git tree hashes match the earlier recorded committed tree identities.
The source repository's active branch was read live at
63a617d3302f1ef1df52febe7b8d231c15a2ead6. A full git checkout failed on DNS.
No historical root/164-curve run, native curve counter, quantum circuit, hardware,
external contact, or other-repository modification occurred.
