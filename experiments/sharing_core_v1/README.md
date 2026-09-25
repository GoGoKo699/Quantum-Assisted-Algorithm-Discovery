# Shared-choice extraction: exact reduction and publication checkpoint

25 September 2026. This is a separate research branch alongside the repository's sorting-completion work. It does not replace the current sorting work order or any historical experiment. No new useful classical routine, quantum advantage, full native-extractor benchmark, or novelty claim is established.

## Question and model

Can private expression choices be solved deterministically, leaving a smaller exact optimization over genuinely shared choices? The input is an explicit e-graph with roots, ordered dependency ports, and nonnegative integer node costs. A selected computation chooses one representative per reachable class, includes its children, and is acyclic. Each selected class contributes its representative's cost once. Repeated child ports use the same value, so cost is not charged twice. Semantic equivalence is an upstream assumption; this algorithm does not validate rewrite rules or the meaning of operators. The objective is additive shared-DAG cost, not mapped runtime, memory, fanout, or latency.

## 1. Structural boundary

Restrict to classes potentially reachable from the roots through any alternatives. In the class-dependency support graph, count distinct parent classes, not parent nodes or port multiplicity. Let

    C = roots union {classes with at least two distinct possible parent classes}.

Let s = |C|. All other classes are private.

**Lemma.** The private support is acyclic, and different core classes have disjoint private expansions until the expansions hit a core class.

**Proof.** A reachable private cycle either contains a root (then not all vertices are private), or has an entry from outside the cycle. Its entry has a predecessor on the cycle and another predecessor outside, so is core. This is a contradiction. Every private class has a unique parent class. Tracing parents backwards until first hitting C is therefore unique. Two private branches that reconverged from different parent classes would make the first common class core. Two alternatives of the same class may mention the same private child, but only one alternative is selected. Repeated ports of that selected alternative are deduplicated for cost. This proves the disjointness needed for the sum recurrence.

This construction is a structural parameterization, not a certificate that s is small on useful workloads. Shared input leaves can make C large even when extraction is easy.

## 2. Exact local completion

For a set S of already constructed core classes, a reference to a core class in S costs zero; a reference to another core class is unavailable. For private p define

    t_p(S) = min_{node n in p} [w(n) + sum_{distinct child classes x} t_x(S)],

with boundary values 0 or infinity at core references. Evaluate this on the private acyclic support. To construct a new core v, expand v's representative rather than treating v as a boundary terminal:

    c_v(S) = min_{node n in v} [w(n) + sum_{distinct child classes x} t_x(S)].

The selected local witnesses can be recovered during the same computation. All c_v for one S can be evaluated with a shared private memo table in polynomial time in the explicit graph size and cost bit width. There is no exponential table of complete programs inside c_v.

## 3. Cyclic alternatives: exact classical subset dynamic programming

Set D(empty)=0 and otherwise initialize D to infinity. For each S and v outside S use

    D(S union {v}) = min(D(S union {v}), D(S) + c_v(S)).

The exact extraction optimum is min D(S) over S containing every root.

**Proof, extraction to DP.** Take a valid extraction and order its selected core classes with dependencies first. Between core boundaries its private pieces are disjoint by the lemma. At each step, c_v can choose the extraction's local piece, or one no more expensive. The resulting DP path is no more expensive than that extraction.

**Proof, DP to extraction.** Each finite transition builds v using only earlier core classes and a private acyclic piece. Concatenating the local witnesses gives an acyclic computation. No private class is owned by two core pieces, so costs add exactly for everything built. Some built pieces can be unused by the roots. Pruning them does not increase cost, because weights are nonnegative. Combining both inequalities establishes equality of optimum values. An optimal DP path reconstructs an optimum reachable computation.

The bound is 2^s times a polynomial in the explicit graph and bit width. The implemented table uses exponential classical space. This is an exact reference algorithm; no claim of best classical complexity or a compact quantum implementation of this cyclic DP is made.

## 4. Acyclic support: activation choices suffice

Assume the entire potentially reachable class support is acyclic, not just the selected result. For A subset C containing all roots define

    F(A) = sum_{v in A} c_v(A minus {v}).

Then OPT = min F(A). The implementation evaluates all boundary references using A: this is equivalent because v cannot reach itself when support is acyclic.

**Proof.** Local witnesses for A cannot depend cyclically on one another, since every dependency is a support edge/path. Private pieces are disjoint. Joining the witnesses constructs all A with cost F(A); discarding unused pieces cannot raise cost. Conversely, the core classes of an optimum extraction give an activation set whose local minima cost no more than that extraction. The two directions give equality. The claim concerns the minimum: F(A) can overcharge unnecessary activated classes.

If h = |C minus roots|, explicit activation enumeration has 2^h candidates and polynomial work per candidate. This is not always a good representation: the public calibration has 2^11=2048 activation patterns but only 45 full representative combinations after elementary pruning. The solver portfolio should keep the better representation.

### Standard quantum corollary, not a novel speedup theorem

Given a cost threshold K, use the predicate F(A)<=K and standard bounded-error amplitude amplification/search [3]. This gives O(2^(h/2)) predicate evaluations at constant error, including a bounded search schedule when the number of solutions is unknown. On a returned A, reconstruct and verify the root program classically. Existence of an accepted A is exactly existence of a qualifying extraction. Costs can be exact integers; finite rational costs may be scaled, charging the resulting bit width.

The predicate has a polynomial-size reversible implementation in the circuit model: hardwire the explicit topology, evaluate min-plus local expressions in topological order with finite-width integer arithmetic and an infinity flag, sum active contributions, compare with K, phase-mark, then uncompute. A simple implementation keeps polynomially many intermediate arithmetic values. It does not use QRAM or a uniformly prepared table of all programs. However, its logical width and depth depend on the graph's explicit size and cost precision, not only on the h activation qubits. We have NOT compiled/count-optimized this circuit or given physical resources. The current code evaluates F classically.

Thus a justified asymptotic upper bound is O(2^(h/2) poly(N,b)), plus classical preprocessing/output reconstruction, for this acyclic-support model. It is a speedup over activation enumeration, not a proved advantage over the best classical extraction algorithm. Parameterized treewidth methods, representative enumeration, simplification, heuristics, exact solvers, and parallelism are legitimate competitors. No classical lower bound is supplied.

### Why the acyclicity qualification is indispensable

Let a root need A and B. A can use B for cost zero or a leaf for cost ten; B can use A for zero or a leaf for ten. The true optimum is ten. Treating all activated classes as free dependencies incorrectly produces zero by selecting both circular alternatives. The general subset DP returns ten; the activation-only interface rejects cyclic support. This example is tested.

## 5. Tests actually run

`checks.py` compares the cyclic DP with exhaustive representative enumeration on 2100 seeded structural graphs (1-7 classes): 1192 have acyclic support, 908 cyclic support, and 310 have no valid extraction. Across the graphs the exhaustive checker examines 40205 representative assignments. For each acyclic graph the activation formula is checked separately. This is NOT exhaustive enumeration of all small e-graphs, nor semantic certification of randomly generated operators.

A small coupled-sharing example gives exact cost seven versus eight from the supplied greedy core, but its weights are illustrative and it is trivially easy. It is a test, not an application result.

The public calibration transcribes SmoothE's `dataset/diospyros/simple_vec_add_root_7.json` at the pinned commit in PROVENANCE.json. Reconstruction reproduces the exact 17477 source bytes and Git blob SHA. Original class strings, including `7.` for two alternatives, are not corrected. Costs are scaled exactly by 1000. The raw file contains 91 nodes / 18 classes; 17 classes are potentially root reachable. Removing directly self-dependent alternatives and unreachable classes leaves 24 nodes / 16 classes with acyclic support. The declared sharing core has 12 classes, 11 optional.

The original `FasterGreedyDagExtractor` algorithm core is transcribed from the pinned source with a separate input adapter. Its algorithm methods are unchanged; CLI/data-loader/GPU dependencies are not executed. The result has cost 1205 scaled units, as do the exact DP, activation enumeration, and exhaustive check. The output has eight reachable classes. This is a native upstream ALGORITHM CORE calibration, not execution of full optimized SmoothE or e-boost, not a large-instance comparison, and not a quantum advantage. The observed timing file is explicitly excluded from deterministic fixtures.

The prior supplied `egraph_intake_v1` verifier was rerun and passed. No sorting-completion, filter, or other historical long experiment was rerun in this branch.

## 6. Publication status and related work

The intended paper should answer whether structural classical compilation leaves quantum-beneficial implementation choices. These lemmas and tests provide a precise starting point, but novelty is UNRESOLVED. Conditioning on shared structure, min-plus/tree extraction, standard search, and subset DP are familiar techniques; priority must be established by comparison, not by a keyword search returning no exact title.

The closest checked structural work includes [1] and [2]. Their treewidth-based methods and simplifications predate this checkpoint. Our parameter s can be worse than their parameters. The current native heuristics in [4] and [5] must be compared on the same graphs and cost semantics. The generic quantum result [3] is a prior tool, not the paper's contribution by itself.

Read `publication/PLAN.md` at the checkpoint root. No manuscript is ready for submission and no arXiv upload or outside contact is authorized by this package. A substantive theoretical paper need not await a hardware demonstration or a new multiplication record, but it needs an original result and an honest comparison. An application advantage claim additionally needs full resource and useful-output evidence.

## Reproduce

    python experiments/sharing_core_v1/verify.py

Uses only the Python standard library. All generated results go to a temporary directory; immutable evidence is not overwritten. `results.json` must match exactly. `observations.json` records local timings and is not compared. Do not run Python -O/-OO. The source algorithm core retains Apache-2.0 attribution; original code is under the unchanged root MIT license.

## References

[1] Goharshady, Lam, Parreaux. Fast and Optimal Extraction for Sparse Equality Graphs. PACMPL OOPSLA2 (2024), DOI 10.1145/3689801. https://doi.org/10.1145/3689801

[2] Sun, Zhang, Ni. E-Graphs as Circuits, and Optimal Extraction via Treewidth. arXiv:2408.17042. https://arxiv.org/abs/2408.17042

[3] Brassard, Hoyer, Mosca, Tapp. Quantum Amplitude Amplification and Estimation. arXiv:quant-ph/0005055. https://arxiv.org/abs/quant-ph/0005055

[4] Cai et al. SmoothE: Differentiable E-Graph Extraction. ASPLOS (2025); optimized implementation https://github.com/cornell-zhang/SmoothE at 8de74ef2b53aabbb35898400cb5eb890d9a07a54. This checkpoint runs only the named greedy core.

[5] Yin et al. e-boost: Boosted E-Graph Extraction with Adaptive Heuristics and Exact Solving. arXiv:2508.13020. https://arxiv.org/abs/2508.13020
