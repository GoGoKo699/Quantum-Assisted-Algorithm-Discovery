# Claim ledger

## Current checkpoint: sampling encoding audit, 28 September 2026

The [encoding audit](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md) applies the
[sample-to-verified-logic contract](exploration/phase_3/SAMPLING_TO_VERIFIED_LOGIC_08.md)
to an inspected prefix of a benchmark shipped with Manthan. Its 376 clauses
exactly define 85 internal bits from 119 input bits. Guessing the internal bits
adds a 2^-85 uniform rejection penalty. The fixed-raw-prior Grover calculation
therefore needs at least 2^41 rounds for half success, but this is NOT a lower
bound on structured quantum algorithms or the application.

An independent reversible evaluator has 149 X, 132 CX and 129 CCX gates and 23
clean scratch bits for that prefix. Computing the definitions removes the raw
penalty and preserves the uniform conditional satisfying-assignment law. This
uses standard logic and reversible techniques, is equally available to classical
competitors, and establishes no quantum advantage. Nonuniform dependent-bit
weights require separate treatment. No complete relation oracle was constructed.

The final checker passed twice with identical --native output. It checks 6320
local truth assignments, 128 forward/inverse basis controls, 10880 single-wire
faults and four malformed cases. Native Z3 4.13.3.0 returned UNSAT for two
prefix-equivalence mismatch queries. No independent proof trace was replayed.
Default mode passed; -O/-OO, a modified fixture and an incorrect complete-source
file were rejected. Successful --source validation was NOT run. The
[report](experiments/sampling_encoding_v1/REPORT.json) and
[provenance](experiments/sampling_encoding_v1/PROVENANCE.md) state the exact scope.

## Native execution and application gates remain open

The native Manthan/CMSGen installation and official smoke test did not run:
source transfer failed on runtime DNS, and the inspected successful dependency
workflow returned no artifacts. The available native Z3 checks are not a
substitute claimed to be Manthan. No sample-source ablation, synthesis-stage
timing, classifier, full verified program or useful performance result exists.

Only a selected source prefix was transcribed and checked. The complete benchmark
was not acquired and locally hash-verified. Source/application signal mapping is
unresolved; a USB name does not establish an industrial deployment task. The
[work order](work_orders/CURRENT.md) requires an instrumented native baseline and
provenance before further small demonstrations or substantial quantum costing.
Earlier sampling, root and historical verifiers were not rerun; their sources and
results are unchanged. No useful quantum discovery advantage is established.

## Preserved historical evidence

The preceding ledger is pinned at
[pre-encoding checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/0e02a52f2e52fb5541018e47c5ba4401ca5ea58d/STATUS.md).
It in turn links the complete pre-sampling cumulative ledger. Older current/next
headings describe their original checkpoints and do not create active work orders.
No old scientific fixture, source, report or proof was changed.

The [sampling opening](exploration/phase_3/USEFUL_SAMPLING_07.md) retains the
classical-only deployment distinction and direct precedents. The
[battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md) and
[operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
Both classical spin-offs remain independent; Phase-2 Note 27 stays closed.
Manuscript preparation remains on hold. The original license and upstream
rights notices remain intact. Only the parent repository is modified; no outside
contact, paid/unattended work, release, merge or administration change occurred.
