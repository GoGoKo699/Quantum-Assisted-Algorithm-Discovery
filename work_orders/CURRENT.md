# Current task: test whether sparsifier correctness needs the published random-oracle memory

29 September 2026. Branch: `research/prx-quantum-phase2`.
Read [implicit Gaussian graph 03](../exploration/phase_4/IMPLICIT_GAUSSIAN_GRAPH_03.md),
[AGENTS.md](../AGENTS.md), and the preserved [handover](../HANDOVER.md).
Classically supplied input and reusable output are restored as the active comparison.
Direct samples remain permitted. Manuscripts stay on hold; no new repository needed.

## What the model/access check established

The input is an explicit point table and bandwidth; Gaussian similarities define
an implicit complete graph. A spectral sparsifier is a reusable classical object
for graph energies and harmonic label queries. Its energy guarantee is not an
unqualified classifier-accuracy guarantee. An isolated query may bypass the graph.
Classical and quantum algorithms receive the same point representation.

The complete-graph adjacency index is reversible arithmetic. Weight evaluation
needs coordinate lookup, distance and finite-precision kernel arithmetic. The
published Apers/de Wolf algorithm gives ideal RAM time ~n^(3/2)/epsilon and a
classical output, but also ~n^(3/2)/epsilon coherently accessible working bits.
Input ingestion, point memory, working memory, numerical representation, and output
all count. The active-qubit count is not total physical memory. A linear table-scan
circuit can erase the saving, but it is not a lower bound on every architecture.

Broad Gaussian graphs with a certified minimum weight tau have an elementary
classical uniform-edge construction using ~n/(tau epsilon^2) evaluations, followed
by ordinary resparsification if needed. Geometric/kernel methods are additional
competitors. Small tau alone is not hardness. At the opposite extreme, a known
closest-pair reduction supplies conditional near-quadratic hardness for universal
Gaussian graph sparsifiers with compact binary inputs and polylogarithmic weight
precision. The quantum/RAM contrast is conditional; its useful learning-bandwidth
regime and end-to-end advantage are not established by worst-case hardness.

## The next bounded algorithmic hypothesis

Apers/de Wolf use a generic 2Q-wise random-string replacement to preserve the exact
output law of a Q-query quantum algorithm. That accounts for substantial coherent
working storage. The useful output only needs to be a valid sparsifier, not have
that exact independent-edge law. Doron et al.'s bounded-independence spectral
sampling is an existing possible ingredient, not our theorem or a ready quantum
implementation.

Audit a short-seed replacement under the SAME input access assumptions. Start with
the implicit iterative half-sparsifier/spanner construction, then its refined
resistance-sampling stage. Prove correctness conditioned on all previously fixed
choices, using a fresh seed before each sampling layer. Include quantum subroutine
failure, edge-count concentration, probability rounding and reversible hash cost.
Grover search is valid for each fixed marked set; no arbitrary-algorithm
indistinguishability theorem is required if the output property is proved directly.

Do not claim a smaller total memory by improving only the final stage while the
rough sparsifier retains the old storage. Count surviving point-table, spanner,
resistance-data and output memory. A shorter random seed does not eliminate input
QRAM. Time/space and precision counts must be explicit; classical resparsification
and approximate resistance evaluation are permitted. Check prior work before
claiming a new result; a bounded search is not a novelty certification.

The deliverable is one proved integration or a precise obstruction, not a new
randomness library, broad point-cloud census, giant solver or compiled QRAM. If
known methods already establish the same tradeoff, record their scope rather than
repackage them. A successful theoretical memory improvement is still conditional
on access and does not itself prove a new practical label-learning speedup. Tie
any further application claim back to a needed bandwidth/accuracy regime and the
strongest adequate classical construction or bypass.

## Evidence and preservation

Note 03's standard-library exact-rational checker ran twice identically and rejected
-O/-OO and six invalid inputs. It checks adjacency, one small Gaussian graph's
resistance/harmonic identities, finite-bit cut reduction inequalities and a small
absolute-pruning counterexample. No sparsifier, quantum search, bounded-independence
construction, random-memory architecture, classification dataset or timing was run.
The finite examples are not evidence of conditional hardness or a new separation.
Historical scientific verifiers were not rerun.

Sensing remains a scope-separated reference; stopping power is a reserve, not a
parallel work order. The emitter-covariance lead remains closed. Preserve all
historical notes, code, reports, provenance and rights. Only this parent repository
may be modified. No new repo/spin-off, contact, paid/unattended work, manuscript,
branch merge, release or administration change is authorized.
