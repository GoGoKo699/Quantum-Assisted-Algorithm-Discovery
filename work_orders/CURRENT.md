# Current research task

Read README.md, STATUS.md, PROVENANCE.md, and experiments/filter_mcm_v1/README.md first. The newest workload screen is filter_mcm_v1; earlier helper and guided constructions remain historical evidence, not complete quantum advantage results. Preserve LICENSE, all upstream notices, and every historical source/result file. Work in versioned successor directories, use temporary outputs, and do not use Python -O/-OO.

## Objective

Useful circuit-model quantum advantage in discovering a reusable classical method. The final method runs classically. No obligation to matrix multiplication, QML, photonics or a particular platform. Residual/error-correction approaches are not the chosen direction. A compact output and later reuse do not establish a quantum discovery advantage.

## Latest evidence and decision

The new concrete workload family is multiple constant multiplication for published digital/image-filter coefficient banks. Mathematical coefficients are pinned and attributed; no upstream solver code was imported. We ran a new bounded exact bit-vector encoding on the installed native Z3 C backend, not the current specialized SAT-CMM/RPAG/jMCM programs. The upstream SAT-MCM README deprecates it in favor of SAT-CMM. Do not call our generic encoding a strongest-classical baseline.

Eight small banks return bounded optima quickly. For the larger 9x9 lowpass bank, generic SMT times out at budgets 12,13,14, but deterministic target closure produces a 12-operation circuit in milliseconds. Twelve required distinct odd fundamentals give a matching lower bound in the free-shift/sign model. This timeout is encoding weakness, not hardness evidence.

The same bank has exact arithmetic-count/depth Pareto points (12,3) and (13,2). Adding helper 15 or 17 permits depth two; at 12 operations only required fundamentals can exist, and the depth-one set cannot generate 303 in one more gate. Proof and complete certificates are supplied. Both circuits pass all 65,536 unsigned 16-bit inputs and exact integer identities. No claim that the circuits are new. Limited ALAP register counts concern fixed witnesses, not mapped silicon or global register optima.

These instances are useful model-calibration/rejection cases, not the desired unsupplied hard discovery workload. The key design lesson is to preserve real depth and bit costs instead of optimizing only an abstract addition count. Timing-aware/pipelined optimization is established prior work.

## Next substantive work

1. Obtain and run current specialized native synthesis for a concrete coefficient bank and stated depth/bit-cost budget. Include preprocessing, alternate architectures, exact and heuristic methods, memoization, and parallel resources. Do not keep enlarging the independent generic SMT encoding to manufacture a timeout.
2. Select an unsupplied hardware routine meeting a meaningful timing/area constraint, with accepted input widths, arithmetic domain, shifts/sign handling, and overflow rules. A coefficient bank is only part of an image filter; compare complete relevant hardware boundaries, not an unpriced block.
3. Adapt helper-state synthesis only where valid. Unit-cost eager closure does not alone optimize depth, storage or physical cost; fixed-pool earliest-level propagation remains useful. Changes to free shifts, widths, fanout and memory must be explicit, not borrowed silently from the earlier normal form.
4. Only after an independently useful task remains expensive for strong classical discovery, compile and analyze a complete quantum search. Account for coherent closure, state selection, reversibility, success probability, output verification and all resources. Old raw/guided qubit figures do not apply. Compare cost to obtain a qualifying circuit, not proof of an unnecessarily strong global optimum.

The target deliverable is a defensible useful workload with a matched classical/quantum resource comparison. No quantum advantage is currently established; the field is not declared impossible merely because these small candidates are easy.

## Verification

python experiments/filter_mcm_v1/verify.py
python experiments/filter_mcm_v1/verify.py --solver

The optional test uses a native Z3 shared library and checks all 384 four-bit/budget-0-to-2 decisions against independent enumeration. The default validates hashes, all eight stored SAT certificates, exact depth bounds, and both full input-domain bank evaluations. Benchmark timings and UNKNOWN results are observations, not portable deterministic expectations; larger UNSAT results lack independently checked proof traces.

This turn reran the supplied unique_helpers_v1 verifier and all new exact/optional solver checks. It did not rerun the remote target-closure verifier or historical long benchmarks. Do not promise unattended work, contact people, incur charges, or change repository administration.
