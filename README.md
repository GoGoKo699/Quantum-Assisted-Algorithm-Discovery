# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The resulting method should run
on ordinary computers and address a need that exists independently of this project.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current task: useful computation first

Identify a documented real computational bottleneck, the classical method that
would help, and why quantum discovery might overcome the obstacle to obtaining
it. The [current work order](work_orders/CURRENT.md) requires an evidence-backed
application case before substantial development of another mathematical mechanism.

A candidate needs a named workflow or user community, a deployment interface,
realistic correctness or accuracy requirements, and a strong classical comparison.
Its output should matter without a quantum label. A domain name, small matrix,
compact certificate, or improved symbolic count does not establish that benefit.
A real application may justify theoretical work; immediate production deployment
or a hardware demonstration is not a prerequisite.

No replacement application has yet been selected. The next deliverable is a
concrete problem case and a discriminating calculation, not a new framework.

## Parked operator candidate

The [first phase-3 mechanism screen](exploration/phase_3/MECHANISM_SCREEN_01.md)
contains a conditional regularized-Gram construction and ideal row-query analysis.
It is preserved as exploratory evidence, **not the active lead**. It has not
identified a useful source family or established an advantage over strong
classical alternatives. Its finite-precision and predecessor audits are deferred
until an application case warrants them. This is a priority decision, not a
mathematical refutation or a claim that the construction has no possible use.

The existing finite algebra controls remain available:

```sh
python experiments/operator_compilation_v1/verify.py
```

They do not simulate amplitude estimation or quantum gates. They were not rerun
for this documentation-only priority change.

## Project organization and retained evidence

Scientific phase 3 uses the existing working branch,
`research/prx-quantum-phase2`; no branch was renamed or merged. See the
[canonical project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and the governing [parent charter](exploration/phase_2/CHARTER.md).
The default branch is the public entry point, not a merged copy of all research.

[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
have independent projects and repositories. Their further development belongs
there, not as the default continuation here. Neither replaces the parent goal.

The [selected-count theorem](exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md)
and [reconstruction audit](exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md)
remain supporting historical records. The
[source-aware descent comparison](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md)
remains closed. Historical next steps do not override the current work order.

[STATUS.md](STATUS.md) separates current decisions from retained claims.
Proofs, experiment code/results, manifests, third-party notices, and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are unchanged. Only the parent
repository is writable in this project context.
