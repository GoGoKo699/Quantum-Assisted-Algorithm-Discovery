# Current research task

Read README.md, STATUS.md and experiments/sorting_completion_v1/README.md. Preserve LICENSE, upstream notices and every historical experiment byte. New research belongs in a versioned successor. Use temporary outputs and never Python -O/-OO.

## Objective

Useful circuit-model quantum advantage in discovering a reusable classical method. Compact output and later reuse are not quantum advantage. No obligation to QML, photonics, matrix multiplication, filters or sorting. Residual/error-correction approaches are not the selected direction. Do not let implementable machinery replace a useful task and a serious comparator.

## Latest evidence

Sorting-network completion is the new provisional family. An 18-input depth-ten network is unsupplied in the checked primary sources; its existence and practical mapped benefit are not established. The published 28-input depth-thirteen construction was found classically in under twenty minutes using specialized prefix and SAT techniques. Do not confuse expensive optimality proofs with expensive useful discovery.

Independent exact component-prefix reduction leaves 243/928 Boolean states after six layers for pinned 18/28-input networks, rather than 2^18/2^28. A native-Z3 incremental completion baseline retains learned clauses and counterexample inputs. It is NOT the published optimized MiniSat or SorterHunter implementation.

The fixed six-layer 18-input prefix has no four-layer completion according to native UNSAT even without symmetry/final-layer restrictions; no independently checked UNSAT proof is supplied. Earlier-prefix trials are UNKNOWN. A known-feasible 28-input control is also UNKNOWN, so timeouts are evidence of an inadequate baseline, not intrinsic classical hardness. The successful 18-input eleven-layer control has 80 comparators versus 78 supplied, not an improved routine. In that single timed control, candidate verification is 0.214% of work, so making only verification free could improve total time by at most about 0.214%.

## Next decisive work

1. Reproduce a strong native classical completion baseline on the published 28-input positive control, including the documented window, oneUp/oneDown and relevant pruning/last-layer techniques, before interpreting open-target timeouts. The current independent encoding is calibration only. Do not increase its timeout as a substitute for this step.
2. Explore justified diverse prefixes for the unsupplied 18-input target, or another independently useful missing routine. A fixed infeasible prefix is not global hardness and must not become a quantum search target. Preserve effective classical deductions and compare time to find a satisfactory witness, not an unnecessary global optimum proof.
3. Establish an execution-relevant acceptance metric before claiming practical value from fewer layers: include comparator count, instruction mapping/shuffles or hardware delay/routing as appropriate. No artificial constraints just to obstruct the classical solver.
4. For a surviving measured bottleneck, analyze a complete quantum discovery procedure. Do not target the almost-free verification stage shown in the control, square-root native CDCL statistics, assume free coherent learned-clause access, or transfer previous qubit estimates. Include prefix preparation, whole adaptive process, reversible predicates, success, extraction and matched classical parallelism.

## Verification

python experiments/sorting_completion_v1/verify.py
python experiments/sorting_completion_v1/verify.py --solver

Default: 1211 independent exact prefix comparisons, 152 finite completion decisions, exact known-network reductions, 1024 sampled inputs each and all 243 states for the recovered control. Optional native Z3: 42 SAT/110 UNSAT responses match complete tiny enumeration. Larger timing/model/timeout observations are not deterministic fixtures. Previous depth2_cover_v1 default verifier passed this turn; older long trajectories and optional tests were not rerun.

The eleven small filter count/depth tasks remain retired. No new sorting algorithm, useful quantum advantage, complete quantum circuit, or mapped runtime improvement is established. No external contacts, paid computation, unattended work or repository administration changes are authorized.
