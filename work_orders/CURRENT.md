# Current research task

Read README.md, STATUS.md, PROVENANCE.md, docs/target-closure-normal-form.md, and experiments/unique_helpers_v1/README.md. Preserve LICENSE, upstream notices, and every historical source/result file. Run the relevant versioned verifier before modifying its successor; do not overwrite evidence or use Python -O/-OO.

## Objective

Useful circuit-model quantum advantage in discovering a reusable classical method. No obligation to matrix multiplication, QML or a hardware platform. Residual/error-correction approaches are not the chosen direction. Do not let compilable machinery displace usefulness or classical comparison.

## Latest evidence: unique-helper successor

In the free-sign/copy, unlimited-storage, exact gate-count model, target closure removes output scheduling. The next normalization merges all histories with the same helper set. A constructible nonempty helper set has a removable helper; deleting the lexicographically largest removable one defines a canonical parent. Local signed-sum generation plus this parent test gives a reverse-search tree with one genuine node per constructible helper set, without a global visited table.

This applies established Avis--Fukuda reverse search; neither that method nor generic quantum backtracking is novel. The application-specific novelty is not established. Reversible predicates and a complete quantum resource estimate have NOT been compiled. Binary prefix/invalid nodes, child selection, parent testing, initialization and repetitions remain charged; earlier raw-search qubit counts do not apply.

The integer four-point Hadamard census through four helpers has 84,925 distinct states versus 453,281 ordered histories. Canonical and memoized enumerators agree. The canonical implementation also runs with no audit/visited records, but uses more closure/pair tests than memoization. The eight-addition construction is known and classically immediate. All 2,048 four-input GF(2) target families and 177,147 disjoint target/helper assignments pass independent checks. These are exact validation results, not a quantum-advantage workload.

A known Winograd input transform has 16 helpers yet an immediately available separable 32-addition construction. Do not equate many helpers with hard discovery. Published larger Hadamard algorithms also show that arithmetic counts and native hardware performance can favor different methods; their native implementations were not benchmarked here.

## Next substantive work

1. Choose a non-calibration exact kernel improvement with an independently needed output and an execution-relevant acceptance metric. Audit existing constructions and native implementations first. A threshold below a historical count is not automatically new or practically useful.
2. Run a serious classical synthesis baseline including target closure, common-subexpression elimination, memoization, symmetry, greedy/learned guidance, SAT and parallelism where applicable. Native CPU/GPU solvers, not a weak discovery tree, are the competition.
3. Use unique helper states rather than inflated ordered-history counts. Test whether the remaining states are still difficult after stronger algebraic structure and decompositions are used. Do not simply increase the Hadamard census or run another supplied-identity rediscovery.
4. Only for a surviving workload, compile and price a complete quantum search on the chosen representation. Compare against both memoized and low-memory classical methods; canonical parent tests cost time. Account for binary-label expansion, precision, storage, repetitions and output checking. The normal form must be reconsidered when latency/register constraints or a different instruction set are charged.

## Verification scope

New complete finite checks: python experiments/unique_helpers_v1/verify.py (Python 3.10+, g++ C++17). Full gate certificates can be emitted with checks.py into a separate output path. Earlier checks remain python verify.py and python verify_target_closure.py. In the unique-helper turn, the new verifier and the supplied local archive's default guided checks were rerun; the remote target-closure verifier and historical long benchmarks were not rerun. All source/result hashes for the new experiment are recorded locally in MANIFEST.json.

No new transform, hardware result, practical speedup or useful quantum advantage is claimed. Update versioned evidence and claim boundaries when results change. Do not promise unattended work, contact external people, incur charges or change repository administration.
