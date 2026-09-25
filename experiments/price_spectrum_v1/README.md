# Scale-invariant price-spectrum search

25 September 2026. Successor to `budget_grounding_v1` on the publication branch.
No historical experiment, original MIT license, or sorting work is changed.

## Exact result

The old cap domain binomial(K+s,s) depends on arbitrary cost units. Let P_v
contain costs at most K of private local constructions of core v, stopping
at boundary references. These references cost zero locally but must still be
constructed by the grounded predicate. Private disjointness permits union and
Minkowski-sum propagation of prices. Include cap zero, and round each cap down
to the largest such price it permits. Every enabling comparison is unchanged:

    c_v(S) <= b_v  iff  c_v(S) <= snap_v(b_v).

Consequently the exact cyclic threshold decision survives this finite-alphabet
restriction. Multiplying all costs and K by a positive integer changes price
magnitudes but NOT alphabet cardinalities. Extra arithmetic bits are still charged.
The alphabets can overapproximate distinct effective thresholds; minimality is
not claimed.

Before compiling prices, infer mandatory classes by positive intersection/union
propagation. Give mandatory core v its lower price c_v(C minus {v}), others zero.
Ground this lower vector. Caps of the classes it constructs can be fixed to their
lower prices: any successful vector dominates the lower vector, so those classes
remain available and all other construction rules retain their caps. Threshold
existence and final grounded sets are preserved, without promising identical rounds.

Full proof: `publication/PRICE_SPECTRUM_THEOREM.tex`. Publication and prior-work
assessment: `publication/PROGRESS_03.md`. These are candidate results, not priority
or significance claims for standard propagation or quantum-search machinery.

## Costs that must not be hidden

With alphabet sizes q_v and Q=product q_v, standard quantum search gives

    A + O(sqrt(Q) poly(N,P,log(K+2)))

time, where A is ACTUAL price-compilation work and P the explicit table size.
Workspace is polynomial in the compiled representation, not necessarily the
original input. A zero/one-label domain is solved classically. Mixed-radix
constant division and reversible table scans avoid a free-QRAM assumption.

An easy O(n)-class family can have 3^n local prices and 2^n conditional minima,
even after the mandatory-grounding prepass. Root needs p_i and q_i, each either
costing 3^i directly or using shared b_i at zero local cost; b_i costs 2*3^i+1.
The exact optimum is sum_i 2*3^i by independent direct construction. Thus explicit
price listing can be exponential on an easy instance. Compilation limits raise
SpectrumLimit, NEVER infeasibility. Decomposition remains a legitimate comparator.

## Calibration, not application advantage

The inherited public SmoothE graph has known optimum 1205 and 45 representative
combinations after elementary pruning. Its original numeric domain is about
2^94.075. Price alphabets reduce this to 4096 labels; mandatory grounding leaves
128, of which 28 satisfy the total cap and ONE succeeds. Counting the 28 uses an
explicit 76-state sparse sum-DP; this count/ranking is not free in the quantum
algorithm, which searches all 128 labels.

The indexed circuit includes decoding, lookup, budget checking, grounded
construction, marking and uncomputation. Calibration resources: 7 index qubits,
3024 clean work qubits, 3026 marker Toffolis; with diffusion, 3035 Toffolis per
Grover iteration and 3031 logical qubits. Search repetitions, preprocessing,
connectivity and physical fault tolerance are excluded. This is not a successful
search runtime or a quantum-over-classical win.

## Verification

    python experiments/price_spectrum_v1/verify.py

Standard library only. Source/dependency hashes are pinned. Reports are generated
in temporary storage and compared with expected SHA256 digests; full reports
are available in the downloadable checkpoint or can be emitted separately:

    python experiments/price_spectrum_v1/checks.py --output /tmp/price-results.json
    python experiments/price_spectrum_v1/indexed_circuit.py --output /tmp/price-circuits.json

Existing outputs are not overwritten. Do not use Python -O/-OO.

Finite evidence: 400 seeded graphs, 3739 representative assignments, 8366 cap
snaps, 351120 enabling comparisons, 3088 forced-cap checks, 2000 threshold
questions, 598 rank roundtrips and 431 scaled-label checks. Circuits: 2540
constant-division cases, 164 marker basis inputs (including invalid padding),
clean uncomputation and reduced index-space amplitude checks. Tests are not
exhaustive over all e-graphs and do not certify semantic rewrite equivalence.

Both predecessor budget/sharing verifiers were rerun. No large native extractor,
sorting, filter, or older long benchmark was run. A larger pinned SmoothE file
was read through the connector but could not be downloaded into execution.

## Classical comparison

Goharshady--Lam--Parreaux's O(N*5^w*w) bound does not enforce acyclic extraction
from cyclic support; their egg discussion explicitly states the reachability
extension incurs c^(w^2). Their Cranelift support is acyclic. This is a scope
qualification, NOT an error claim. Sun--Zhang--Ni's acyclicity-aware bound is
2^(O(w^2))*poly(N,w). Compare those correct models, subset DP, representative
search, simplification, and native solvers; no best-classical separation is proved.

Primary references: DOI 10.1145/3689801; arXiv:2408.17042v2;
quant-ph/0005055; quant-ph/9605034; arXiv:2508.13020.

Publication remains focused on one original comparative result in e-graph
extraction, not more unrelated probes or a repackaged standard search theorem.
