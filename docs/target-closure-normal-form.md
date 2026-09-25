# Eliminate target scheduling; branch on helper expressions

## 1. Task and model

The task is to construct an exact straight-line program for a specified integer linear map. Start with the `n` coordinate vectors. A gate computes `a+b` or `a-b` from any two available wires; repeated operands are allowed. Copies and sign changes are free. A known zero output is free. Gate count is the objective; live storage, fanout and sign handling have no additional cost in this model.

Vectors are identified only up to **sign**, not arbitrary scaling or gcd. Thus `(2,0)` is not treated as `(1,0)`. Gates and all verification use exact integers. The GF(2) tests are a separate, explicitly declared arithmetic domain.

Let `T` be the set of distinct nonzero target vectors, excluding coordinate vectors, after sign canonicalization. Write `d=|T|`. Any circuit needs at least `d` gates, since each such direction must first appear at some gate. The decision problem is whether at most `d+k` gates suffice.

This objective is a genuine component of arithmetic-program synthesis, but an addition-count improvement is not automatically a runtime improvement. A useful final task must account for its execution context. The normal form below does **not** apply unchanged when registers, recomputation, memory traffic, latency, or arbitrary scalar gates are charged differently.

## 2. Fixed-expression feasibility is positive-rule closure

For a specified set of target/helper expressions, a construction rule has the form

\[
\{a,b\}\subseteq S\quad\Longrightarrow\quad c\in S.
\]

Here `S` denotes computed expressions and the rule is allowed only when `c=±a±b` exactly. Coordinate expressions are initially available. Each rule has a positive prerequisite set. There are no consumable inputs, deletions, or mutually exclusive choices. Consequently computing an available node cannot disable any other rule.

Forward-chain all initially enabled rules, decrementing outstanding prerequisite counts when a new node becomes available. At termination, every reachable node is known. A rule witnessing the first creation of each node supplies a valid straight-line order. Failure to reach a goal is exact infeasibility for this fixed node set.

**Proof.** Soundness follows by induction over fired rules. For completeness, every node on any feasible schedule becomes available no later than the closure's fixed point, by induction over that schedule. Cycles without an initial enabling rule do not create nodes. No subset/scheduling search is necessary. This is standard positive-Horn forward inference [2], not a new general theorem.

The implementation builds the incidence lists and processes each explicit prerequisite occurrence/rule a bounded number of times. Integer-mask operations have their ordinary bit costs; we do not treat unbounded bit vectors as unit-cost primitives.

## 3. Helper-budget normal form

**Proposition (under the model in Section 1).** There is a circuit with at most `d+k` gates if and only if the following search succeeds with at most `k` helper choices:

1. Start with all coordinate vectors.
2. Saturate every still-missing target that is a signed sum of available vectors. Record one gate per newly created target.
3. If all targets are present, return the circuit.
4. Otherwise choose one new nonzero non-target direction `h=a±b`, not already available, from available vectors. Add it as a helper and return to step 2.

**Forward implication.** Remove zero, duplicate-up-to-sign and dead computations from a witness. There are exactly `d` first creations of required non-basis target directions and at most `k` remaining live gate results. Order those non-target helper gates as in the witness. Before each helper, eagerly create every available target, retaining all wires. Inductively the witness's target predecessors are available from closure, and its earlier helper predecessors have already been chosen. The next helper can therefore be chosen. Targets created early replace later occurrences at no extra cost. At the end all targets are available. Creating each mandatory direction once does not raise its unavoidable contribution `d` to the gate count.

**Reverse implication.** The search records a topologically valid gate each time it appends a vector. It appends at most `d` target directions and `k` helpers. Signed output references and exact replay recover the specified map.

The proof uses monotone availability and gate count. It does not assert that all valid schedules have equal physical latency or space. The current tests are finite corroboration, not a substitute for these assumptions.

## 4. Finite branching and bit size

At any node there are at most `M=n+d+k` available vectors. Distinct signed sums/differences, up to global sign and including equal operands, give at most `M^2` helper candidates: two for each distinct pair and one nonzero doubling per repeated pair. A crude helper-tree bound is

\[
T_h\leq 1+M^2+M^4+\cdots+M^{2k}.
\]

For fixed `k` this is polynomial, with exponent depending on `k`. This is **not** a fixed-parameter-tractable bound of the form `f(k) poly(n,d)`.

If target coefficients have magnitude at most `C`, helper magnitudes after `k` helper gates are at most `2^k max(1,C)`: target saturation introduces only prescribed target vectors, and each helper can at most double the current maximum. The bit length is therefore `O(k+log(1+C))`, up to sign and additive constants. No arbitrary real precision or unbounded input oracle is assumed.

The implementation enumerates helper directions in a fixed sorted order. It does not add a coefficient cutoff or divide vectors by gcd. It is intentionally not a state-of-the-art synthesis solver; its purpose is an explicit complete candidate tree and certificate generator for this model.

## 5. Published dependency-core calibration

Reference [1] synthesizes the three factor maps of Perminov's `cr58_cn122` tensor. We inspected and transcribed its relevant publicly licensed functions, preserving option-generation and candidate order. The original BFS is compared against closure on every candidate up to the same first hit. This is a reproduction of the named dependency-search core, not a byte-identical import of its full executable or reproduction of the native CPU/GPU heuristic solvers [3].

The native subset-state counts are 1,459 / 26,642 / 15,577 for U/V/W, including the failed target-only check. The closure construction fires 204 / 1,115 / 1,106 nodes across those same candidate tests. Different primitives are counted; no wall-clock or overall discovery speedup factor is claimed.

There are 12 / 13 / 13 target directions. Target-only closure fails for each, giving exact lower bounds 13 / 14 / 14. Our independent eager helper search constructs matching circuits. Transposing the 14-gate W-factor circuit gives 28 output additions, yielding the published total of 55. Exact replay verifies the generated linear maps and all 729 integer tensor equations. These are an existing identity and optimum, not a new quantum-discovered program. The input factor specification does not hide the 55-gate circuit in the tested helper search, but the reference is publicly available and trivially settles the calibration task.

## 6. Transposition and the small-neighborhood exclusion

For a linear map with `n` essential inputs and `m` nonzero outputs, reverse accumulation of a pruned `L`-gate binary signed-addition circuit uses at most `L+m-n` additions. There are `2L+m` incoming adjoint contributions and `L+n` active nodes at which the first contribution is free; merging the others accounts for the difference. Applying this construction in both directions gives the corresponding additive-complexity equality. This is the established transposition principle used in [1]. Duplicate output directions do not cost a new forward gate but do create adjoint contributions, which are counted.

For the W-factor map here, `n=9` and `m=23`; all inputs are essential and rows are nonzero. Hence the output-map lower bound is the factor lower bound plus 14. These conditions follow from the verified multiplication tensor and nonzero rank-one terms; they are also preserved in the enumerated neighbor set.

Define one neighbor step explicitly: choose an ordered pair of terms sharing a factor up to sign, normalize that shared sign, and apply

\[
(a,b,c),(a,d,e)\mapsto(a,b+s d,c),(a,d,e-s c),\quad s=\pm1.
\]

Reject moves with a zero factor or a coefficient outside `{-1,0,1}` in the new factors. Include all three tensor axes and canonicalize only term permutations and compensating factor signs. This is a fixed-rank integer-ternary local test, not the prior GF(2) search.

For each factor `F`, let `h(F)=d(F)` when target-only closure succeeds, and `h(F)=d(F)+1` otherwise. The circuit-cost lower bound is

\[
h(U)+h(V)+h(W)+14.
\]

At distance one there are 30 distinct nonroot states: 14 have bound 56, 16 bound 57. Distance two adds 368 states: 84 have bound 57, 222 bound 58, 62 bound 59. Exact tensor checks validate all 398 states (290,142 equations); sorted state-set hashes permit comparison on rerun. Thus every examined nonroot state is excluded from the local 54-addition target. The reference itself has exact cost 55.

This does not exclude different tensors, basis transformations, rational coefficients, expansions, longer paths or other cost models. Nor is 54 asserted to be a new/current global record: a current-record and coefficient/basis-cost audit is still required before selecting a novelty target. No unsuccessful empirical search is used as a lower bound here.

## 7. Consequence for a prospective quantum algorithm

Pause further compilation of the old guided graph until an independently worthwhile workload is fixed. A candidate replacement is a binary-encoded helper-choice backtracking tree whose node predicate replays chosen helpers and performs target closure.

Its root is explicit. Coefficient arithmetic and validation are finite and polynomial per node. A final witness is an ordinary classical circuit. However, a quantum implementation still needs reversible closure/replay, state preparation for branching, parent/child operations, predicate uncomputation and an honest memory/time tradeoff.

Montanaro's existing backtracking theorem gives `O(sqrt(T) D^(3/2) log D)` predicate tests for an appropriate binary CSP tree with depth/variable parameter `D` [4]. Here `T` must include binary operand labels, their prefixes, invalid leaves and the actual pruning policy, not just the number of complete helper sequences. This is a possible application of known theory, not a proved useful speedup or a newly compiled circuit. There is no transfer of the old 904-qubit estimate.

The classical opponent must receive the same closure and can additionally use memoization, equivalent-state merging, symmetry, SAT, strong heuristics, parallelism, and any representation exploiting the task. A quantum tree can lose to a classical merged-state graph. The small one-helper calibration is polynomial and easy; amplifying it is not a useful target.

## 8. Decision and remaining work

The proposed task is now **exact linear-map/arithmetic-kernel synthesis above the unavoidable target-direction floor**, not generic long walks and not error correction. Matrix multiplication supplies the calibration, but does not restrict the domain.

The next acceptance test is a non-calibration, independently needed map whose desired improvement is not already supplied, whose relevant classical solver has actually been run, and whose certified output saves a relevant execution cost. Determine its helper budget and complete classical search profile before pricing quantum backtracking. A general normal-form observation plus standard quantum backtracking is not, on its own, a publishable useful-advantage result. Prior-art coverage of this parameterization remains open.

## References

1. S. Karunaratne and A. Idamekorala, *55 Additions Suffice for 3x3 Matrix Multiplication at Rank 23*, arXiv:2607.28676v1 (28 July 2026). https://arxiv.org/abs/2607.28676v1 . Exact fixed-orientation reference, not asserted latest global record.
2. W. F. Dowling and J. H. Gallier, *Linear-Time Algorithms for Testing the Satisfiability of Propositional Horn Formulae*, Journal of Logic Programming 1(3), 267–284 (1984), DOI 10.1016/0743-1066(84)90014-1. https://doi.org/10.1016/0743-1066(84)90014-1 . We use bottom-up positive closure, not a top-down implementation.
3. A. I. Perminov, *Parallel Heuristic Exploration for Additive Complexity Reduction in Fast Matrix Multiplication*, arXiv:2512.13365. https://arxiv.org/abs/2512.13365 . Stronger classical heuristic ecosystem; not reproduced by this checkpoint.
4. A. Montanaro, *Quantum Walk Speedup of Backtracking Algorithms*, arXiv:1509.02374. https://arxiv.org/abs/1509.02374 . Known theorem; access and complete costs remain to be implemented here.

Pinned source paths, licenses, and transcription boundaries are in `provenance/target-closure-sources.json`.
