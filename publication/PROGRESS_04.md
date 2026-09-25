# Publication progress 04: implicit completion by component arborescences

25 September 2026. Additive continuation on research/sharing-core-publication.

## The result being developed

Under a polynomially checkable single-recurrent-boundary condition, fix the active
shared classes and optimize all remaining implementation choices by private min-plus
DP and minimum directed spanning arborescences. Cyclic alternatives are allowed;
arbitrary conjunctions inside a recurrent component are not. The resulting exact
objective is computed in polynomial time/space in the original explicit graph and
binary cost length, without numerical grids or local price catalogs.

Consequently standard quantum search gives O(2^(h/2) poly(N,L)) time and polynomial
original-input workspace for a threshold query, where h counts optional core
classes after sound mandatory inference. This extends the first checkpoint's
acyclic-support corollary to a larger but explicit cyclic class. It does not extend
to all inputs in budget_grounding_v1 or price_spectrum_v1. Old counts do not transfer.

## Why this is preferable to another catalog optimization

The earlier exponential-price family has a linear-time componentwise solution,
so no quantum algorithm should list those prices. The new inner completion avoids
that artifact. It also solves actual choice cycles: a minimum-arborescence entry
arc pays for grounding rather than granting free circular availability.

Both insights strengthen the classical algorithm too. We must not claim the
classical simplification as an exclusive quantum benefit. Arborescence, SCCs,
min-plus DP, and amplitude amplification are established tools.

## A comparative result, not just another own-baseline square root

Globally unary extraction is precisely directed Steiner tree. A terminal-subset
DP gives an independent classical parameterization; for one output it reduces
to shortest path. This correspondence and the implemented comparator exclude a
large optional-core count, by itself, as a convincing quantum opportunity.

The general single-recurrent condition still permits multi-input operations
between components. The unary comparator does not automatically solve that broader
class. Existing e-graph treewidth/circuit algorithms, direct representations,
pruning and modern native extractors must be assessed there. We have NOT proved
superiority to the best classical algorithm or established priority for this
combined extraction reduction.

## Evidence gate accounting

Gate 1 (novelty/comparison): sharper. The directed-Steiner special-case equivalence
and classical reference algorithm were actually implemented and checked. The
reduction's publication-level novelty remains unresolved; not assumed from a
keyword search. The standard search corollary is not alone the contribution.

Gate 2 (complete model): stronger theoretical statement on a narrower explicit
class. Per-activation work and workspace are polynomial in original input, even
with binary weights and cyclic alternatives. Recognition failure is not extraction
infeasibility. A polynomial reversible simulation exists, but no complete quantum
gate compilation or physical resource estimate was performed this round.

Gate 3 (useful external instances): unchanged. The public calibration remains easy;
raw cycles disappear under elementary pruning. Attempts to obtain the larger
pinned JSON in the execution environment failed. A connector read is not an
executed benchmark. The measured small graphs are validation, not a surrogate
for full SmoothE/e-boost or an application advantage.

## Required next result

Stay on the e-graph paper branch. Determine whether the single-recurrent structure
and a genuinely difficult optional-choice problem coexist after strong classical
preprocessing in an independently motivated workload. Analyze comparisons with
Steiner/treewidth/representative methods before attributing significance to h.
An appropriate result could establish an original conditional algorithmic regime;
a generic exponent and unit tests alone remain insufficient.

The implementation discrepancy in installed NetworkX 3.6.1 is retained, with an
explicit exact witness, rather than silently equating its exception with proven
infeasibility. It is an audit observation, not a contribution claim or an external
bug report. No contact, charge, submission, or repository merge is requested here.
