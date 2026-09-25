# Unique helper states, without a global visited table

25 September 2026. Successor to repository commit
`33f32c03f3c33c2491d5542ac76328f1bf6db922`.

**Status:** a classical canonical-parent construction and exact finite checks.
No useful quantum advantage, new transform algorithm, compiled quantum circuit,
or runtime improvement is established. Reverse search and quantum backtracking
are established tools. The application-specific novelty of their combination
here has not been established.

## 1. Why another normalization is needed

Target closure removes irrelevant scheduling of mandatory outputs. It does not
remove different orders of selecting the same helpers. A classical memoized
solver can merge those histories. A quantum comparison against the unmerged
history tree can therefore exaggerate the remaining difficulty.

We retain the earlier model: exact integer addition/subtraction, repeated
operands allowed, free signs/copies, unlimited storage; direction means equality
up to sign, not up to an arbitrary scalar. The finite-field tests use GF(2)
separately. This normalization does not preserve register-constrained scheduling,
latency, or floating-point bitwise behavior.

## 2. A polynomially decidable state and a unique predecessor

Let B be the coordinate vectors, T the distinct non-basis target directions,
and H a set of non-target, non-basis helpers. Start with B and forward-chain only
forms in T union H that are signed sums of available forms. Write C_T(H) for the
result. H is **constructible** iff H is contained in C_T(H).

Crucially, helpers are not initially free inputs in this test. A sorted list of
helpers need not be a constructible order. For example, with target (1,1,-2), the
set {(1,1,0),(1,1,-1)} is constructible, but its lexicographically smallest helper
cannot be constructed alone.

For nonempty constructible H, let h* be the lexicographically largest helper
whose removal leaves a constructible set. Define

    parent(H) = H minus {h*}.

**Existence.** Take any construction of H and remove its last-created helper.
Earlier helpers did not depend on it. Required targets need not all remain
reachable in a partial state. Hence at least one removal is valid.

**Unique root.** The parent is deterministic and decreases cardinality by one.
Repeated removal terminates at the empty set. It defines a rooted spanning tree
on all constructible helper sets up to a chosen budget k.

**Local child generation is complete.** Given constructible H, compute its target
closure and propose every new signed pair sum/difference h. Keep H union {h}
exactly when its canonical parent is H. Conversely, if G has parent H, a
construction of G must create its one additional helper from forms obtainable
using H and target closure. Thus that child is proposed.

This is an application of Avis--Fukuda reverse search [1]. It visits each helper
set once without a global visited table. It removes only identical-helper-set
history multiplicity, not all algebraic symmetries or stronger solver deductions.
It is not a claim that every dynamic program has this property.

## 3. Costs and a prospective quantum use

Set M=n+|T|+k. Each state has at most M^2 candidate helper directions before
removing duplicates. Parent evaluation requires at most k constructibility
checks. Straightforward closure uses polynomially many exact vector operations.
For target coefficients bounded by C, helper coefficients after k helper choices
have magnitude at most 2^k max(1,C), so their bit length is O(k+log(1+C)).

Classical reverse traversal stores a polynomial-size current state and local
candidate/stack workspace. It pays for repeated parent/closure calculations.
The memoized competitor stores visited helper sets and avoids those parent tests.
Neither cost is free.

Let V be the number of distinct constructible helper sets in a bounded search.
At depth j, each set has at most j! constructive orders; the ordered-history tree
can be much larger than V. Our tree has V genuine state vertices. If implemented
with fixed binary labels, invalid labels and selection-prefix vertices must be
included. For a padded label alphabet D<2M^2, a conservative full binary
expansion has at most 1+2DV vertices and depth O(k log D).

Established quantum backtracking [2] can be considered on that explicit tree.
Its query bound is O(sqrt(T_bin) h^(3/2) log h) for the referenced formulation,
where T_bin is the expanded tree size and h its binary depth (small-depth cases
are handled separately). That is a conditional algorithmic route, not a compiled
resource estimate. Reversible closure, parent tests, child deduplication, search
repetitions, initialization and output extraction must be priced. The bounded
node algorithms admit polynomial-size Boolean/reversible implementations in
principle; none is gate-compiled here. No QRAM table of all V states is assumed.
A suitable tree-size upper bound or safe unknown-size schedule is still needed.

The comparison remains with the strongest classical synthesis method, not merely
this spanning-tree traversal. All earlier raw-search qubit counts are irrelevant.

## 4. Exact tests

### Integer four-point Hadamard calibration

The target rows are (1,1,1,1), (1,-1,1,-1), (1,1,-1,-1), (1,-1,-1,1).
The full census through four helpers includes successful states and their
supersets; it is not an early-stopping discovery runtime benchmark.

| Helper count | Distinct states | Ordered helper histories | Successful states |
|---|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 1 | 16 | 16 | 0 |
| 2 | 236 | 356 | 0 |
| 3 | 4,064 | 10,864 | 0 |
| 4 | 80,608 | 442,044 | 3 |
| Total | 84,925 | 453,281 | 3 |

The three successful four-helper sets recover known butterfly constructions,
not a new transform. Together with the helper normal form, exhaustive failure
through three helpers proves eight additions/subtractions are minimal **in this
stated integer +/- model** for this four-point map. It is not a lower bound for
other instruction sets or all larger Hadamard transforms.

The canonical traversal makes 291,989 closure calls and 42,699,150 pair tests;
the memoized traversal makes 84,925 and 14,486,619 respectively. Thus the
memory-saving representation is not a free classical time improvement. Pair
tests are instrumented kernel operations, not wall-clock or quantum gates.

The C++ audit mode records states to verify uniqueness and calculate history
multiplicities. A separate **no-audit run actually stores no visited or audit
records** and reproduces the same vertex, goal and work counts. An independent
Python implementation agrees on every integer state through three helpers and
on a smaller Winograd output-transform census. No artificial coefficient bound
is imposed by the integer enumerators.

### Exhaustive four-input GF(2) checks

All 2,048 target families and all 177,147 disjoint target/helper assignments are
checked. There are 175,700 constructible helper states across the families and
173,652 canonical parent edges. Independent unrestricted circuit enumeration has
1,857 wire states and 9,684 deduplicated extension edges. All optimal gate counts
agree. The optimum-helper histogram is 1,857 zero-helper, 185 one-helper, and six
two-helper target families. These checks are finite evidence, not an application
hardness claim. The large aggregated history count includes easy/empty goals.

## 5. Useful-workload screen

We exactly reconstruct the known separable input transform for Winograd
F(2x2,3x3) convolution [3]: 16 inputs, 16 required directions, 16 helpers and 32
additions/subtractions. The complete gate certificate and all target vectors are
regenerated by checks.py. The underlying one-dimensional B^T matrix is

    [1, 0,-1, 0]
    [0, 1, 1, 0]
    [0,-1, 1, 0]
    [0,-1, 0, 1].

This illustrates that even sixteen helpers need not imply hard discovery: the
separable construction directly supplies them. We neither prove 32 minimal nor
claim a better Winograd routine. This is an independently motivated workload
screen, not the as-yet-missing non-calibration quantum-advantage instance.

Larger Hadamard transforms likewise require serious baselines. Alman and Rao [4]
improve the asymptotic arithmetic count beyond the usual butterfly algorithm.
HadaCore [5] uses hardware-aware tensor-core computations and data exchange; its
reported speedups can occur despite increased nominal floating-point work. We
have not run those native implementations. Gate-count optimality alone therefore
does not choose the practically faster algorithm or satisfy the project goal.

## 6. Decision and claim boundaries

Retain the canonical-parent representation as a candidate way to preserve
identical-state merging without a large coherent memory table. Do not benchmark
quantum search against inflated ordered histories. Do not keep enlarging the
Hadamard census as a substitute for a useful workload. The next task remains a
non-calibration kernel improvement with a complete native classical comparator
and an execution-relevant acceptance criterion. A large helper budget is not
sufficient evidence of classical difficulty. No publishable novelty or useful
quantum advantage is certified in this checkpoint.

## 7. Reproduce and provenance

Run from this directory with Python 3.10+ and a C++17 g++ compiler:

    python verify.py

The verifier checks the local manifest, works in a disposable directory, repeats
all new deterministic experiments, and compares exact output hashes and counts.
To emit full certificates separately: `python checks.py /path/to/output.json`.
Run without Python -O/-OO. The verifier never overwrites stored evidence.

All new code is independently written under the repository MIT license. No
upstream executable is vendored. Mathematical transform coefficients are
transcribed from the cited definitions. The current GitHub base was read through
the connector. The older default guided checks and its 18-file immutable import
manifest were rerun from the supplied local archive; the current remote
verify_target_closure.py and its 398-state census were NOT rerun this turn.
No inherited file is changed by this experiment.

[1] Avis and Fukuda, Reverse search for enumeration (1996).
https://cgm.cs.mcgill.ca/~avis/doc/rs/rsorigins.html

[2] Montanaro, Quantum walk speedup of backtracking algorithms (2015/2016).
https://arxiv.org/abs/1509.02374

[3] Lavin and Gray, Fast Algorithms for Convolutional Neural Networks (2015/2016).
https://arxiv.org/abs/1509.09308
Transform definitions also appear in the authors' implementation:
https://github.com/andravin/wincnn

[4] Alman and Rao, Faster Walsh-Hadamard and Discrete Fourier Transforms From
Matrix Non-Rigidity (2023). https://arxiv.org/abs/2211.06459

[5] Agarwal et al., HadaCore: Tensor Core Accelerated Hadamard Transform Kernel
(2024). https://arxiv.org/abs/2412.08832
