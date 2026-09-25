# Budget-grounded extraction with cyclic alternatives

Research successor, 25 September 2026. This extends `sharing_core_v1`; it does not modify its evidence or the sorting-network work on main. Novelty and useful quantum advantage are not established.

## Result and intended contribution

The earlier activation-only objective fails on cyclic alternatives. This successor replaces a guessed construction order by a vector of local cost caps and a least fixed-point construction test. It gives an exact threshold decision formulation even with cycles and zero-cost nodes. A standard quantum-search corollary uses polynomial workspace rather than an exponentially large subset-DP table. Its search domain depends on the numeric cost threshold, so it is not an unconditional improvement over classical subset DP.

The question remains useful quantum-assisted discovery of a reusable classical implementation. No new application family is introduced here. This is a theorem/circuit-model development within the publication branch, not a useful-output or deployed-speedup claim.

## 1. Model and inherited decomposition

Input: an explicit finite e-graph, designated roots, nonnegative integer node costs, and integer threshold K >= 0. One representative is selected per used class; selected dependencies must be acyclic, and shared classes are charged once. Equivalence semantics are assumed from a trusted upstream construction. An extraction algorithm does not by itself validate the rewrite system. Floating-point equivalence and mapped physical costs are not inferred from additive graph costs.

Restrict the support to classes potentially reachable through any alternatives. Let C contain all roots and every class having at least two distinct possible parent classes, and set s=|C|. Other classes are private. By the preceding checkpoint's lemma, each private class has a unique upstream boundary owner, private support is acyclic, and private pieces belonging to distinct core classes are disjoint. Repeated child references count once.

For S subset C, c_v(S) is the cheapest local piece constructing v with previously built core classes S available at zero additional cost; other boundary references are unavailable. It includes v's representative and private dependencies. Local costs and witnesses are computed by min-plus evaluation of the private acyclic graph. The function is monotone nonincreasing as S grows. The code reuses the immutable implementation in `sharing_core_v1/core.py`.

## 2. Grounding by local budgets

For b in the nonnegative integers^s define

    S_0 = empty
    S_(t+1) = S_t union {v in C: c_v(S_t) <= b_v}.

Stop at the fixed point S_*(b), after at most s changing rounds. A zero cap does NOT make a class available automatically: it only allows a genuinely constructible zero-cost piece. All decisions in a round use the preceding round.

**Theorem.** There exists a valid extraction of cost <= K if and only if a vector b exists with sum_v b_v <= K and all roots in S_*(b).

**Soundness.** Record a minimizing local witness when each class first becomes available. Its boundary dependencies belong to earlier rounds, so the assembled program is acyclic even if the support is cyclic. Distinct core pieces have disjoint private nodes. Each built core is charged once and its local price is at most its cap. Thus the cost of everything built is at most sum b. Delete pieces not reachable from the roots; nonnegative costs cannot increase. The resulting extraction costs at most K.

**Completeness.** Take a valid extraction of cost <= K and split it into the local pieces of its used core classes. Assign each used core its actual local cost and assign zero to unused core classes. The sum is exactly the extraction cost. Induct on a dependency-first ordering of its core classes. Once the predecessors are grounded, c_v may choose the extraction's local piece, so c_v(S) <= b_v. Every required root is eventually grounded. Additional zero-cost constructions do not invalidate this induction or increase the bound.

Consequently,

    OPT = min {sum b : roots subset S_*(b)}.

This is a representation change, not a new general fixed-point or amplitude-amplification theorem. It eliminates explicit construction-order enumeration at the price of searching cost allocations.

## 3. Finite search domain and binary-encoded arithmetic

The number of nonnegative integer vectors of length s with sum at most K is

    M = binomial(K+s, s).

The extra slack is implicit. `unrank` decodes a rank from 0 to M-1 into one such vector in lexicographic order. For a next coordinate x when p coordinates and residual K remain, the number of vectors preceding x is

    binomial(K+p,p) - binomial(K-x+p,p).

Binary search selects x. Each binomial can be computed with at most p multiplicative factors; the decoder does not loop K times or allocate an O(K) table. Arithmetic bit widths are polynomial in s and log(K+1). Tests include a 257-bit threshold.

A straightforward uniform quantum procedure starts with q=ceil(log2 M) Hadamards, rejects padded indices >= M, reversibly un-ranks a valid index, computes the grounded-cap predicate, phase marks, and uncomputes. M <= 2^q < 2M when M>1. Standard bounded-error search with an unknown-number-of-solutions schedule finds a qualifying index or decides none exists in O(sqrt(M)) predicate uses at constant error. A measured index is decoded and replayed classically to reconstruct and independently check the actual program. M=1 is evaluated directly.

Thus a uniform circuit-model upper bound is

    O(sqrt(binomial(K+s,s)) poly(N,L,log(K+2))) time,
    poly(N,L,log(K+2)) workspace,

including polynomial classical preprocessing and reconstruction. N is explicit graph size (nodes/classes/dependency ports) and L includes input cost bit lengths. There is no QRAM or table of all local-cost values. This is a speedup over allocation enumeration, NOT a lower bound or an established advantage over the strongest classical method.

For a cap test, all costs may be saturated at K+1: any larger value is infeasible under a valid cap. One round computes all private and boundary costs using O(N) bounded-width min/add operations, and there are at most s rounds. Ordinary compute-copy-uncompute produces a polynomial-size reversible circuit. Binary unranking also has a polynomial reversible implementation; the implementation here checks its classical arithmetic but has NOT compiled unranking into gates.

## 4. What was compiled

`circuit.py` builds a Boolean DAG of the full synchronous cap predicate, including the total-cap bound. Every Boolean operation has a clean target and is expanded into X/CNOT/Toffoli gates. Computing, phase-marking, and reversing leaves all input bits unchanged and all work bits zero. Gates are constant-folded and identical Boolean subexpressions shared.

The cyclic three-core counterexample at K=10 has 12 cap input bits, 385 clean work bits, and 384 Toffolis for compute/phase/uncompute. The five test graphs cover 4,174 basis inputs in total; every marked bit and restored work register agrees with the independent predicate. Cycles with no grounding alternative are rejected even with ample caps. Positive costs, zero costs, private alternatives, and invalid binary cap codes are included.

These are component logical counts. They exclude rank unranking, initial Hadamards, outer search/diffusion, connectivity, and physical error correction. Do NOT label 397 qubits as the complete discovery machine or infer a runtime advantage from the toy graph. The simple cycle costs ten classically without a search.

## 5. Numerical verification

`checks.py` independently enumerates representatives, verifies the selected DAG, and partitions its costs by private ownership. It does not call the local-cost function for this independent cap-feasibility test.

- 400 seeded structural graphs, including 177 with cyclic support and 85 infeasible graphs.
- 3,455 representative assignments, 8,374 complete cap checks, and 2,000 threshold decisions; all agree.
- All 1,790 feasible optimum witnesses among the preceding 2,100 seeded graphs are converted to caps and reconstructed at the same exact cost.
- 31,823 exhaustive ranking/unranking roundtrips, plus 12 selected ranks for large binary-encoded thresholds.
- The pinned SmoothE public calibration reconstructs its known cost-1205 witness. Its approximately 2^94 budget assignments are NOT enumerated. The earlier cheap classical solution remains the correct comparator.

These are finite corroboration, not exhaustive testing of every graph, semantic equivalence proofs of random operators, or timing claims. The five marker tests are basis/linearity checks, not hardware execution.

## 6. Classical comparison and significance boundary

The existing exact subset DP uses O(2^s poly(N,L)) time and exponential space; classical cap enumeration uses M times polynomial work and polynomial workspace. Representative enumeration, memoization, treewidth methods, reductions, SAT/ILP, and current heuristics can be superior to both.

If K=rho*s, log2 M / s tends to (1+rho) H2(1/(1+rho)). The quantum search exponent is half of that. It is below s when rho<1, approaches s at rho=1, and is worse above it (up to polynomial factors). This identifies where comparison with the particular subset-DP upper bound is worth examining; it is NOT a proved separation against all classical methods. The full per-predicate and preprocessing costs remain charged.

There is a serious cost-grid sensitivity. Multiplying every cost and K by the same integer changes M although the feasible programs do not change. Normalize common cost factors before applying the bound; even then distinct cap values can be equivalent. For the public calibration s=12 and K=1205, log2 M is about 94.08 versus only 45 post-pruning representative combinations. This formulation is not a useful search choice for that instance. Do not use large numeric costs or duplicated cap encodings to create an apparent quantum opportunity.

## 7. Related work and publication progress

Sun, Zhang and Ni [1] already equate e-graph extraction with weighted cyclic monotone-circuit optimization and analyze acyclicity and simplification. Goharshady, Lam and Parreaux [2] give classical treewidth/pathwidth algorithms. Grounded reachability, budget allocation, private-tree dynamic programming and amplitude amplification [3] are established techniques. No keyword-search failure certifies novelty of their combination.

Ambainis et al. [4] give quantum exponential-DP algorithms; a 2026 paper [5] specifically studies their large QRAM requirements and time-space tradeoffs. We do not transfer those runtime bounds to this model without their access assumptions. The cap method takes a different, explicitly polynomial-space route, with the stated cost-budget penalty.

Gate 2 of the publication plan advances: an exact cyclic certificate, finite ranking scheme, uniform asymptotic quantum algorithm, and one compiled marker. Gate 1 (novelty and stronger classical comparison) and Gate 3 (representative native workloads and relevance) remain open. A partial manuscript theorem section is in `publication/BUDGET_THEOREM.tex`; this is not a submission-ready paper. Large SmoothE files were not retrievable into the execution environment in this turn. No new large native benchmark is claimed.

## Reproduce

    python experiments/budget_grounding_v1/verify.py

Uses the standard library and preserved sharing_core_v1 code. Run without -O/-OO. The verifier hashes dependencies, regenerates both reports in temporary storage, and compares bytes. It does not overwrite expected evidence. The preceding sharing_core_v1 verifier was also rerun; sorting and older long experiments were not.

## Sources checked in this continuation

[1] Sun, Zhang, Ni, E-Graphs as Circuits, and Optimal Extraction via Treewidth, arXiv:2408.17042v2. https://arxiv.org/html/2408.17042v2
[2] Goharshady, Lam, Parreaux, Fast and Optimal Extraction for Sparse Equality Graphs, OOPSLA2 (2024), DOI 10.1145/3689801. https://doi.org/10.1145/3689801
[3] Brassard, Hoyer, Mosca, Tapp, Quantum Amplitude Amplification and Estimation, quant-ph/0005055. https://arxiv.org/abs/quant-ph/0005055
[4] Ambainis et al., Quantum Speedups for Exponential-Time Dynamic Programming Algorithms, SODA 2019, arXiv:1807.05209. https://arxiv.org/abs/1807.05209
[5] Caroppo, Vihrovs, Zajakina, Zajakins, Quantum Time-Space Tradeoffs for Exponential Dynamic Programming, arXiv:2604.02233. Abstract inspected; no full-paper theorem imported. https://arxiv.org/abs/2604.02233
[6] Yin et al., e-boost: Boosted E-Graph Extraction with Adaptive Heuristics and Exact Solving, ICCAD 2025, arXiv:2508.13020. https://arxiv.org/abs/2508.13020
