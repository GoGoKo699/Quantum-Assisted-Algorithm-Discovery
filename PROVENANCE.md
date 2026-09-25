# Provenance

## Repository creation

Owner: Ruge Lin (`GoGoKo699`). Repository: `Quantum-Assisted-Algorithm-Discovery`.
Initial main commit: `ab13a337dfa474a0d8d3b39082ffe841d1ca5169`.
Initial tree: `9e8bf26490e09c5b362ec181be4541777f59e079`.
Original MIT LICENSE blob, retained unchanged: `e17a781bf47c4aadf18b68fc593846a1193b86c1`.

## Active import

The 18 code/data files under `experiments/guided_search/` are copied byte-for-byte from the supplied `Quantum_Discovery_Guided_Search_Probe.zip`, SHA256 `7b5495a887ba93dd10141f9b3d0245143b93a0ffb18e5f9e0c0e4a2734bb6608`. The source-member mapping and byte hashes are in `provenance/import-manifest.json`.

The complete supplied archive's 26-entry manifest was checked locally. The repository imports the active runnable material, not the three historical binary archives embedded in that package. Their hashes and scope are in `provenance/checkpoint-history.json`. The original guided README, NEXT, STATUS, manifest and verification wrapper remain in the supplied archive; repository-level documentation and verification are newly assembled, not represented as byte-identical imports.

Bootstrap reran the mathematical validation and `school_legal.json` deterministic C++ benchmark. All ten stored witnesses were checked, but all ten search trajectories were not replayed during bootstrap. Historical reproduction claims belong to the earlier checkpoint. See `results/bootstrap-verification.json` for the bootstrap scope.

## Public mathematical reference

The known rank-23 integer coefficient data are transcribed from:

- Repository: `dronperminov/FastMatrixMultiplication`
- Commit: `b28490ca14c884c339a9fc69a3bdcba1f6e2c5da`
- Path: `schemes/known/a_60_addition/3x3x3_m23_additions60_ZT.json`
- Git blob: `482609bcebe1fba1bec7e28e8158d9d7ff4312ff`

https://github.com/dronperminov/FastMatrixMultiplication/blob/b28490ca14c884c339a9fc69a3bdcba1f6e2c5da/schemes/known/a_60_addition/3x3x3_m23_additions60_ZT.json

This is mathematical coefficient transcription, not import of the authors' solver. Output factors were transposed to the row-major convention. No advertised addition count is adopted. The independent C++ ablation is not the published native CPU/GPU solver. The known identity is a reference/calibration case, not this project's discovery.

Inherited literature pointers are listed in `docs/current-design.md`; repository initialization is not a fresh literature or novelty audit.

## Target-closure successor, 25 September 2026

New work is isolated in `experiments/target_closure_v1/`. The 18 original imported files are unchanged. Source paths and classifications are in `provenance/target-closure-sources.json`; successor file hashes are in `provenance/target-closure-manifest.json`.

`trylogical/cn122_add55` was read through the GitHub connector at commit `34949f9ce50a89a5ad6b47a17f5834ad5a87a2fb`. Named synthesizer functions are transcribed into a local extracted module, not claimed as a whole-file exact import. Its sparse mathematical data are transcribed into a compact representation and verified by integer coefficient equations. Both upstream MIT notices are retained; the root Ruge Lin license is unchanged.

The new verifier runs in a disposable copy and compares complete deterministic outputs. The native BFS core is instrumented for state counts without changing its candidate order or reachability semantics. Counts of BFS states and closure firings measure different primitives and are not a runtime speedup factor. The entire upstream CLI, other CPU/GPU/SAT heuristic solvers, and current global records were not reproduced. Full historical trajectories were not rerun during this successor.
