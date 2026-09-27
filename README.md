# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The resulting method should run
on ordinary computers.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current exploration: compile a small classical operator

The [phase-3 mechanism screen](exploration/phase_3/MECHANISM_SCREEN_01.md) compares
spectral operators, symmetry-based reductions, and quantum-trained classical
predictors. The selected calculation concerns a regularized Gram matrix generated
by a classical program: construct a small dense matrix once, then use it for
later classical energies and linear solves.

A conditional exact-arithmetic argument repeatedly improves an upper matrix
bound using scalar amplitude estimates. It does not use an input-sized random
inclusion table. Its ideal row-query bound is written, but finite-precision gate
costs, publication priority, and a useful source family with a strong classical
comparison remain unresolved. This is not a completed QRAM-free implementation
or a new sparse-row sampling theorem.

Small deterministic algebra checks, Python 3.10 or later, standard library only:

```sh
python experiments/operator_compilation_v1/verify.py
```

The checks include noncommuting matrices, final solve-error inequalities, and
negative controls. They do not simulate amplitude estimation or quantum gates.
The [current work order](work_orders/CURRENT.md) sets the next bounded audit.

## Project organization

Scientific phase 3 uses the existing working branch,
`research/prx-quantum-phase2`; no branch was renamed or merged. Start with the
[canonical project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and the governing [parent charter](exploration/phase_2/CHARTER.md).
The default branch is the public entry point, not a merged copy of all research.

[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
have independent projects and repositories. Their further development belongs
there, not as the default continuation here. Neither replaces the parent goal.

## Retained evidence

The [selected-count theorem](exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md)
and [reconstruction audit](exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md)
remain supporting historical records. Their independent project maintains the
ongoing classical work. Historical requests to create that repository are not
live instructions.

The [source-aware descent comparison](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md)
remains closed. A reconstruction theorem does not reopen its quantum resource
claim or authenticate supplied counts.

[STATUS.md](STATUS.md) separates the latest checkpoint from retained historical
claims. Earlier proofs, experiment code/results, manifests, third-party notices,
and the sharing-core branch are unchanged. Only the new finite algebra verifier
was run for this checkpoint; root and historical suites were not rerun.

Only the parent repository is writable in this project context. The original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, is unchanged.
