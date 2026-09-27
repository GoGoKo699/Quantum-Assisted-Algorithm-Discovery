# Current task: audit the small-operator quantum compiler

27 September 2026. Scientific phase 3 uses the existing branch
`research/prx-quantum-phase2`. Manuscript preparation remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md), and
[phase-3 mechanism screen and conditional derivation](../exploration/phase_3/MECHANISM_SCREEN_01.md).

## Current lead

A classical program generates N bounded d-dimensional rows. The proposed quantum
computation compiles the fixed regularized Gram matrix into a small dense classical
operator. Later energies and solves use that operator without quantum hardware.
This is not sparse-row selection, a singular-matrix theorem, or a new label-vector
processing algorithm. No useful explicit-source quantum advantage is established.

The exact matrix invariant and ideal scalar-estimation query bound are written.
Small exact rational controls pass. A complete finite-precision circuit bound,
publication-priority assessment, and a useful workload with a strong classical
comparison remain open. Avoid claiming that the published sparsification algorithm
has already been made QRAM-free: the present proposal is a different construction.

## Next bounded work

1. Audit finite precision: row generation and reversal, the small matrix factor and
   inverse, rare flag probabilities, rotations, adaptive errors, output rounding,
   and final classical solve error. Count gates and workspace rather than only
   row queries. Preserve the upper-bound invariant with explicit safety margins.
2. Check the closest prior classical-output covariance/Gram and QRAM-free quantum
   approximation methods. The amplitude-estimation primitive is standard; no
   priority claim follows from the present bounded search.
3. Select at most one useful source-generated fixed-operator family. Compare
   source inspection, analytic accumulation, classical sampling/importance scores,
   and direct downstream computation. Reject examples made hard only by hiding
   source-visible information or restricting classical memory. Include input,
   bound construction, discovery, certification, extraction, and reuse costs.

Do not build a general solver, a random-oracle data structure, or a large benchmark
before these questions justify it. The other two screened mechanisms are reserves,
not simultaneous active implementation projects.

## Evidence and continuation boundaries

Run `python experiments/operator_compilation_v1/verify.py` for the new finite
algebra checks. It is not a quantum simulation or full implementation. At this
checkpoint it passed twice; its -O rejection was checked. Root and historical
verifiers were not rerun because their source and fixtures were unchanged.
Execute additional applicable checks when later changes warrant them and report
exactly what was run. Use temporary outputs; do not execute assertion-dependent
research code under -O/-OO.

Both classical spin-offs own their further development. Do not extend or modify
them from this project. Phase-2 Note 27's source-aware descent comparison stays
closed; Notes 28 and 29 remain unchanged supporting records, with their true-count
promise and authentication/novelty limitations intact. Historical next steps do
not create parallel active tasks.

Preserve prior proofs, sources, reports, manifests, notices, and LICENSE. Modify
only Quantum-Assisted-Algorithm-Discovery. No manuscript revival, outside contact,
paid computation, unattended work, submission, release, branch merge, or repository
administration change is part of this work order.
