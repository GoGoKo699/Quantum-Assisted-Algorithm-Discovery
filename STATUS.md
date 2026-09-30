# Current status

30 September 2026 — one public packing-pricing workload, two classical policies.

**No useful quantum advantage is established. No assumed fast QRAM is permitted.
Manuscript preparation remains on hold.**

[Note 07](exploration/phase_4/PRICING_WORKLOAD_07.md) moves beyond the illustrative
duals of Note 06: real restricted-master solves now generate the pricing inputs.
The first OR-Library Falkenauer uniform instance has 120 items, capacity 150,
volume 7,078, and 58 equal-size types. It is a public synthetic benchmark, not
industrial data or a representative hard-pricing study.

The root master is aggregated exactly by equal item size, with bounded multiplicity
per pattern; it is not unbounded cutting stock or an extension to branching conflicts.
HiGHS dual-simplex LPs supply numerical duals, converted down to exact dyadic scores.
Exact capacity pricing and a distinct validation recurrence agree. Rational primal/
dual feasibility checks are separate from claims of native numerical optimality.

Both executed policies start from a 49-bin best-fit packing and 100 type columns.
Exact pricing reaches a verified optimal 48-bin packing after 56 master solves,
55 positive pricing calls and four integer-recovery calls. Greedy-first requires
80 master solves, 70 greedy columns, nine positive exact-pricing calls and five
integer recoveries. No no-column call is needed before either integer certificate.
The 48-bin assignments are checked on original item IDs; 47 bins lack total capacity.
The reference answer in the source header is never used by the optimizer.

A full pricing DP performs 11,042 integer capacity relaxations. The once-failed
three-order greedy screens do not demonstrate a hard residual: the nine actual
fallback calls have exact prepared improving probabilities between 0.091686350631
and 0.752801740210. Those probabilities are offline, charged diagnostic calculations
AFTER classical solution, not free inputs to a quantum algorithm. The other policy's
four diagnostic calls are kept separate. No quantum-generated columns were fed
back into the master and no quantum-assisted iteration count is inferred.

The result does not prove general pricing tractability or compare physical runtimes.
It removes this fixed-capacity family as immediate evidence for the proposed quantum
benefit. The [work order](work_orders/CURRENT.md) now requires a source-grounded
residual regime before another benchmark or circuit build. Note 06 is retained as
a hardware-admissible conditional construction, not a novel or validated application.

## Executed evidence

The final independent verifier ran twice with identical output in NumPy 2.3.5 and
SciPy 1.17.0. It invokes native HiGHS LP/MIP routines through SciPy, exact-integer
knapsack, rational checks, and the probability recursion. Reports include both
feasible integer certificates. Six invalid inputs and -O/-OO were rejected.
A --full-trace option exposes all generated dual/pricing rows; the default report
pins those traces and the diagnostic price vectors by SHA256.

Checker SHA256: `bcc46767da15f4f9afcd673e78fc2c51653ca4832d04630260295e6546c4710e`.
Report SHA256: `f2a9a7649b7b98fce9018d1fcac68f0e31f009b2f2a405b53a95c1fb60f094fd`.
Input SHA256: `51f26bd988055d22f9b5fdcfaf218675eaa8bcca41f932f9c8d4ba746a6b16c2`.
[Report](experiments/pricing_workload_v1/REPORT.json) ·
[Source notice](experiments/pricing_workload_v1/SOURCE_NOTICE.md).

No quantum circuit, amplitude amplification, FPTAS, native SCIP, advanced stabilized
or lexicographic pricer, industrial test, or measured speedup was run. This is a
small independently written workflow, not a production solver. A preliminary
unaggregated development probe reached a time cap and is excluded from the reported
comparison. Previous scientific verifiers were not rerun. The primary-source check
used HTML/text, not PDFs or figures. No novelty is claimed.

## Preserved evidence

The [pre-workload ledger](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/2680152c9a59c5556e4e44b9b64069219c4e6e0a/STATUS.md)
retains the circuit-pricing hypotheses and assumptions. Note 06, all earlier science,
original license, manifests and rights remain unchanged. The no-QRAM boundary and
independent spin-offs are preserved. No branch merge, release, new repository,
outside contact, paid work or manuscript revival follows.
