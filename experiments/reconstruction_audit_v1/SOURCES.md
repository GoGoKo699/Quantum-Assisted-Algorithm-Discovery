# Proof/priority audit sources and provenance

Inspected 27 September 2026. Base commit:
`4fc01966db525ff761fc6c1b363ef3bd9dfb1023`. The word "independent" refers to a
fresh derivation and checks written independently of the preceding fixture
generator, not an external assessor or a proof-assistant certificate.

## Directly compared primary statements

1. K. S. Kedlaya, *Quantum computation of zeta functions of curves*,
   Computational Complexity 15 (2006), 1-19;
   https://arxiv.org/pdf/math/0411623 , v3.
   Sections 8-9 were reread, including the normalized Mobius formula,
   Newton residue information, cutoff convention, and the fewer-than-2g
   question. PDF page index 13 was rendered and read. Index 11's screenshot
   failed; its text was available. The conditional cardinality-acquisition
   interface in Sections 6-8 remains separate from reconstruction.
   The audited result changes the selected-data support and proves its
   sufficiency; it does not claim the underlying framework or quantum theorem.

2. A. V. Sutherland, *A Generic Approach to Searching for Jacobians*,
   Mathematics of Computation 78 (2009), 485-507;
   https://arxiv.org/pdf/0708.3168 .
   Section 4.1, especially Lemma 4 and its endpoint formulas, was reread.
   The explicit lemma's genus-at-most-three scope does not state a uniform
   varying-genus sparse-query guarantee. The page-index-10 screenshot failed;
   no figure or timing-table information is used. No native implementation ran.

3. C. J. Hillar and L. Levine, *Polynomial recurrences and cyclic resultants*,
   arXiv:math/0411414v4 (2006; Proceedings of the AMS);
   https://arxiv.org/pdf/math/0411414 , v4.
   The introduction, Theorem 1.1, Conjecture 1.2, Theorem 1.4, and the relevant
   reconstruction/recurrence discussion in Section 4 were read. PDF index 1
   was rendered and inspected. Their generic initial-segment sufficient bounds
   are exponential in degree. Their short polynomial recurrence may depend on
   unknown coefficients and is not by itself a uniform efficient decoder.
   The first-sequence conjecture and the q-reciprocal integral promise in
   Note 28 are different problems. No claim of resolving that conjecture is made.

4. C. J. Hillar, *Cyclic Resultants*, Journal of Symbolic Computation 39
   (2005), 653-669; https://arxiv.org/pdf/math/0401220 .
   Primary introduction/statement scope reviewed: uniqueness from the full
   nonzero resultant sequence is not the required finite sparse-data algorithm.
   No new priority claim is inferred from this distinction.

5. D. Roy, N. Saxena, M. Venkatesh, *Complexity of counting points on curves,
   and the factor P_1(T) of the zeta function of surfaces*,
   https://arxiv.org/html/2511.02262v1 (2025 preprint).
   Lemmas 2.10-2.11 and adjacent certification discussion were reread. Lemma
   2.10 uses counts at every index through max(18,2g); Lemma 2.11 treats descent
   from larger fields. That use of the older sufficient theorem does not
   establish our priority or transfer small-field quantum acquisition to it.

These statements do not state the exact audited all-field/g>=32 guarantee.
That is a source comparison, not proof that it is absent from every paper,
thesis, implementation or unpublished argument.

## Search scope and limitations

Public queries combined "Weil polynomial", "cyclic resultants", reconstruction,
Kedlaya, oracle calls, cardinalities and fewer-than-2g, including an arXiv domain
filter and searches for newer results. The directly relevant primary documents
above were inspected, rather than treating search snippets as proof of novelty.
Several broad searches returned unrelated pages; they were not counted as
mathematical evidence. The scope screen also surfaced Yoshizaki's
https://arxiv.org/abs/2503.06194 on p-adic limits of iterated multivariable cyclic
resultants. Only its abstract was examined; it is a convergence result, not an
inspected reconstruction competitor. No full proof audit of that paper is claimed.

Stewart's *Exceptional units and cyclic resultants* was located through its
publisher's metadata (DOI 10.4064/aa155-4-5), but the publisher page failed on
opening and no complete text was assessed here. It is therefore not listed as
an eliminated predecessor. No exhaustive citation-graph or thesis search was
completed, and no external researcher was contacted. Publication priority remains
qualified by those limitations.

## Numerical provenance

The tridiagonal fixture was selected with Python's deterministic seed 280029,
from diagonal entries in {-1,0,1}; candidate index 9 is recorded. Selection
required rigorous spectral bounds and a modular irreducibility check, not a
favorable runtime. SymPy 1.14.0 first generated the selected polynomial and
45 integer resultants. Their fingerprint is retained in CONTROL.json.
The default audit independently verifies all required algebra and calculates
the same integers by a standard-library circulant/Bareiss route. No SymPy code,
third-party solver or author data are imported. This is a mathematical stress
control, not an externally sourced application workload or a curve certificate.

The inherited decoder is pinned by both SHA256 and Git-blob identity in the
manifest. Its source and expected reports remain byte-identical. The mounted
Note-28 archive SHA256 is
`5f2b0c33909295631633f764ac0cda2eb0069b8ebf4bea249e9b12c91d29abfe`.
All five current verifiers in that archive passed unchanged. A full git clone
failed on name resolution; the live repository was read through GitHub.
Historical root and 164-curve verifiers were not run. No quantum order acquisition,
native point-counting application, hardware, or other-repository mutation occurred.
