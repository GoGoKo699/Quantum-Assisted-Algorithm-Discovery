# Implicit cyclic completion through directed arborescences

25 September 2026. Additive successor on `research/sharing-core-publication`.
The objective remains useful quantum-assisted discovery of classical programs.
This successor strengthens a conditional theorem; it does not establish practical
quantum advantage, a new deployed routine, or novelty of standard graph algorithms.

## Result

The price-spectrum compiler is unnecessary on a recognizable class of cyclic
e-graphs. Work with the inherited boundary of output/shared e-classes. Project
possible dependencies through private regions and split this graph into strongly
connected components (SCCs).

**Promise:** every local implementation of a boundary result, stopping at other
boundary results, uses at most one distinct other boundary result in its own SCC.
It may use many results in earlier components. Local self-dependence is discarded
because it cannot appear in a valid extraction. Multiple references to one result
are not multiple prerequisites. This is not a requirement that all operators be
unary. All acyclic-support graphs qualify, as do some genuinely cyclic graphs.

Fix a set A of activated boundary results. Private-region dynamic programming
keeps only minimum cost for each possible same-SCC prerequisite (or none), rather
than all attainable prices. Such a table has at most |SCC|+1 meaningful entries.
Represent each alternative as an arc prerequisite -> result, or ground -> result.
The least-cost way of constructing every active result in an SCC is the minimum
rooted spanning arborescence. Sum these optima in dependency-first SCC order.
Private ownership makes the cost additive and witness choices consistent.

The resulting objective F(A) is exact for building all active classes. Removing
unused active classes can lower the cost of the root-reachable output, so the
precise equality is OPT = min_{A containing required classes} F(A). The code checks
both all-active cost and pruned-output cost. Sound mandatory-class propagation
reduces the number h of optional activation bits before enumeration.

The full proof is `publication/COMPONENT_BRANCHING_THEOREM.tex`.

## What changes relative to the earlier theorem

For this structural class, both the local-price compilation cost and the numeric
budget domain disappear. A deterministic evaluation is polynomial in the original
explicit graph and cost bit lengths. Standard quantum search therefore gives
O(2^(h/2) poly(N,L)) time and polynomial original-input workspace, including cyclic
alternatives. Uniformly scaling costs affects bit arithmetic, not label count.

This is not a result for arbitrary cyclic e-graphs. The recognition pass produces
a concrete two-prerequisite obstruction and raises UnsupportedRecurrence. It must
not be mistaken for infeasibility of extraction. Conjunctions cannot be relaxed
to one-parent choices. A checked three-class example has true optimum two, while
that invalid relaxation produces one.

The minimum-arborescence subroutine is the established Chu--Liu/Edmonds algorithm,
implemented independently with exact integer cycle contraction and witness
lifting. One cycle is contracted per call. The code does not enumerate spanning
trees, numerical prices, or construction orders inside the predicate. The generic
quantum-search corollary is prior amplitude-amplification machinery. A fixed-time
reversible implementation exists with polynomial overhead, but it is NOT compiled
or counted in this successor. Old circuit/resource counts do not transfer.

## Classical comparison actually added

The globally unary subcase is exactly directed Steiner tree, not a new extraction
problem. There is an edge for each representative, pointing from its prerequisite
to the class it computes; leaf operations receive edges from an artificial ground
vertex. Required outputs are terminals. An optimal nonnegative Steiner solution
has a directed tree witness, so the conversion preserves optimum in both directions.

`steiner_baseline.py` implements terminal-subset dynamic programming with all-pairs
shortest paths. Its reference bound is O(n^3 + 3^r*n + 2^r*n^2), for r outputs. It
is an implementation of established classical methodology, not a new algorithm or
an optimized native package. A single-output unary instance is a shortest path.
Thus many optional shared classes do not by themselves justify quantum search.
Treewidth algorithms, representative enumeration, pruning, and native extractors
remain competitors outside this unary subcase. No best-classical separation is
claimed.

## Exact evidence

- 770 seeded 1--7-class structural graphs: 635 satisfy the promise; 135 are
  explicitly rejected. Of the admitted inputs, 231 have cyclic support and 126
  have no extraction. These are not all small graphs or verified rewrite systems.
- Global answers agree with independent representative enumeration, covering
  10,965 assignments. Another 1,463 fixed-active-set checks cover 55,593 assignments.
- 59 integer cost-rescaling checks agree, with identical activation semantics.
- 480 separate directed-graph arborescence questions match complete enumeration
  of 29,932 candidate predecessor assignments; 165 cycle contractions occur.
- 360 globally unary e-graphs, totaling 10,580 representative assignments, agree
  among direct extraction, component branching, and the terminal-subset DP.
- All returned extraction certificates are checked by the independent inherited
  Graph.check, including closure, representative ownership, cycle absence, and
  exact shared cost. The chosen activation is also checked as a complete output.

For the earlier exponential-spectrum family with n=32, the root has 3^32 possible
local prices and 2^32 conditional minima by the analytic construction. The new
per-activation compiler stores only a single minimum at each relevant private
vertex. We evaluate three specified activations without materializing the catalog.
The optimum remains elementary componentwise; no quantum search is appropriate.

The inherited public SmoothE vector-addition calibration gives the same known
1205-unit answer. Raw reachable data have 89 nodes/17 classes and small cyclic
SCCs; after direct-self pruning there are 24 nodes/16 classes and acyclic support.
The raw activation enumeration has 65,536 labels. After pruning and mandatory
analysis it has 64. Direct representative enumeration has 45 combinations. This
is a calibration, not evidence of speedup or a new native large-workload run.
Original data strings and the 17,477-byte source reconstruction are unchanged.

## Independent library comparison: recorded discrepancy

An optional comparison ran the installed NetworkX 3.6.1 arborescence routine on
the same 480 directed graphs. It agreed on 479. On one seven-vertex instance it
reported no spanning arborescence, although complete enumeration and an explicit
six-edge witness establish optimum 34. The original instance, witness and returned
outcome are retained in `networkx_observations.json`; they are not removed to make
a comparison pass. The default exact verification does not rely on that library.
This is a local observed library discrepancy, not a diagnosis of its internal
cause, an author-contact report, or a speed comparison. The optional verifier
reports discrepancies explicitly and does not describe them as universal agreement.

## Reproduction

```
python experiments/component_branching_v1/verify.py
python experiments/component_branching_v1/verify.py --networkx
```

Default uses the Python standard library and regenerates deterministic evidence
in a temporary copy. Optional library observations are reported, not required to
match a version-specific exception in future NetworkX versions. No saved evidence
is overwritten. The prior price-spectrum verifier was rerun this round. Older
budget, sharing, sorting and long benchmarks were not independently rerun here.

## Scope and next publication gate

The candidate theorem has a polynomial implicit completion where the previous
price catalog could be exponential. The substantive remaining question is whether
this structural condition and a favorable optional-choice parameter survive
strong simplification on meaningful workloads. The unary directed-Steiner equivalence
shows why another classical parameterization can already dominate. The standalone
square-root corollary and the calibration are not an established publishable advance.

Do not open another application family or compile an isolated oracle as a substitute
for the comparison. First audit novelty against graph branching, directed Steiner,
AND/OR graph algorithms and e-graph structural extraction; measure the recurrence
condition after genuine preprocessing. No full optimized SmoothE/e-boost run, mapped
benefit, physical quantum estimate, or quantum advantage is claimed.

## Primary references

1. J. Edmonds, *Optimum Branchings* (1967), DOI 10.6028/jres.071b.032;
   R. E. Tarjan, *Finding Optimum Branchings* (1977), DOI 10.1002/net.3230070103.
2. M. Boether, O. Kissig, C. Weyand, *Efficiently Computing Directed Minimum
   Spanning Trees*, arXiv:2208.02590. Established branching implementations.
3. J. Guo, R. Niedermeier, O. Suchy, *Parameterized Complexity of Arc-Weighted
   Directed Steiner Problems* (2011), DOI 10.1137/100794560.
4. A. K. Goharshady, C. K. Lam, L. Parreaux, *Fast and Optimal Extraction for
   Sparse Equality Graphs* (2024), DOI 10.1145/3689801.
5. G. Sun, Y. Zhang, H. Ni, *E-Graphs as Circuits, and Optimal Extraction via
   Treewidth*, arXiv:2408.17042v2.
6. G. Brassard, P. Hoyer, M. Mosca, A. Tapp, *Quantum Amplitude Amplification
   and Estimation*, arXiv:quant-ph/0005055.
7. NetworkX official minimum_spanning_arborescence documentation, checked
   25 September 2026; observed installed version 3.6.1, not bundled or modified.

All new source is under the unchanged root MIT license. Inherited Apache-2.0
notices for the calibration remain present. No upstream branching code is copied.
