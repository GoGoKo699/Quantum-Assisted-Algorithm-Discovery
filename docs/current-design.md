# Guided exploration between classical deductions

## Objective

Find a useful finite classical algorithm through a circuit-model quantum discovery process that survives comparison with strong classical discovery. Matrix multiplication is a testbed, not a commitment to tensor-rank records.

## Representation and local moves

A scheme is a tuple of binary rank-one tensor terms `(a,b,c)`. Integer bit masks encode each factor. Equal first factors permit the identity

\[
a\otimes b\otimes c+a\otimes d\otimes e
=a\otimes(b+d)\otimes c+a\otimes d\otimes(e+c)
\]

over GF(2). Cyclic variants are included. Applying the same labelled flip twice reverses it. Starting from a correct scheme therefore preserves correctness. This is established flip-graph algebra, not a new theorem.

The current Python walk uses only active, rank-preserving moves. The C++ benchmark also allows reductions, compaction, and one exploratory expansion policy. They are not the same stochastic process.

## Why the move address must change

Let `L(S)` be the ordered legal-move list. The map `(S,k) -> (F_{L(S)[k]}(S),k)` can collide because the list changes with the state. An exact collision is stored in `selector_collision.json`.

Instead, put `ell=L(S)[k]`, `S'=F_ell(S)`, and let `k'` be the ordinal of the same label `ell` in `L(S')`. Then

\[
J(S,k)=(S',k'),\qquad J^2=I.
\]

Invalid ordinals are fixed. This is the standard directed-edge reversal construction. The exhaustive tests validate a finite set of small encodings; they do not synthesize an efficient legal-neighbor coin, reverse-address circuit, or complete guided search.

## A classically tractable improvement predicate

For a group sharing factor `a`, write its inner matrix as `BC^T`, with `g` columns. The group admits fewer than `g` rank-one terms iff `rank(BC^T)<g`. This is equivalent to a column dependency in at least one of `B,C`: if both have column rank `g`, `C^T` is onto and `B` is injective, so their product has rank `g`.

If `sum_{j in D} b_j=0`, choose `p in D`. Then over GF(2):

\[
\sum_{j\in D}b_j\otimes c_j
=\sum_{j\in D\setminus\{p\}}b_j\otimes(c_j+c_p).
\]

Gaussian elimination can find this dependency classically. The speculative quantum role is to reach a representation enabling a useful improvement, not to replace that cheap algebra. Check and simplify a marked starting state classically before invoking quantum search.

## Proposed staged process

Classically simplify; coherently explore a fixed-active-count component; mark algebraically reducible representations; measure and verify; classically reduce and restart. This avoids coherently deleting terms or retaining every optimization decision. It may also lose useful classical adaptive behavior, so it must be compared at the level of the final output.

Outstanding costs include legal-neighbor selection and superposition preparation, edge indexing, marker workspace, initialization, any approximate rotations, and the number and quality of successive search stages. A first-hit statistic is not automatically a spectral or electrical quantum-walk parameter. A local-stage speedup need not be a final-discovery speedup.

## Acceptance boundary

Specify the desired arithmetic routine, coefficient domain, additions, storage, numerical properties when relevant, and practical performance criterion. Allow the classical competitor the same prior identities, preprocessing, deductions, symmetry, expansions, restarts, parallelism, and lookup. No useful quantum advantage or new routine is presently established.

## Prior tools

- Kauers and Moosbauer, flip graphs: https://arxiv.org/abs/2212.01175
- Adaptive flip-graph search: https://arxiv.org/abs/2312.16960
- Magniez et al., quantum-walk search: https://arxiv.org/abs/quant-ph/0608026
- Apers, Gilyen and Jeffery, unified quantum-walk framework: https://arxiv.org/abs/1912.04233
- Quantum-annealing algorithm-discovery predecessor: https://arxiv.org/abs/2406.13412

These are inherited checkpoint references, not a fresh completeness or novelty audit at repository initialization.
