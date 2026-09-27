# Quantum-Assisted Algorithm Discovery — exploration phase 2

**Active branch: `research/prx-quantum-phase2`. Target: PRX Quantum.
Manuscript: on hold.**

The parent project asks whether quantum computation can acquire compact
structural information that enables a useful reusable classical method.
A distinct classical reconstruction theorem has emerged from that exploration;
it is not itself an established new quantum advantage.

Start with the [phase-2 charter](exploration/phase_2/CHARTER.md),
[proof audit and separation decision](exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md),
and [current work order](work_orders/CURRENT.md).

## Audited mathematical result

For every finite field and genus g>=32, set h=g-2. The true Jacobian counts at
indices 1..h and the even indices through 2h determine the Weil polynomial and
permit a polynomial-bit-time reconstruction. This uses h+ceil(h/2)<2g selected
ordinary counts, not the first h+ceil(h/2) counts. No twist oracle is required.

The [theorem in Note 28](exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md)
survives a fresh internal proof derivation, explicit rational bit-size bounds,
and an independently checked irreducible degree-64 2-Weil-polynomial control.
No theorem parameter was changed by the audit. This is not external peer review,
proof-assistant verification, minimum-query optimality or an unconditional
publication-priority claim. The decoder receives true counts; successful rounding
is not an input-authentication certificate.

```sh
python experiments/reconstruction_audit_v1/verify.py
python experiments/all_field_reconstruction_v1/verify.py
```

## Separation decision

The classical result now warrants a focused mathematical project under the
proposed name `Sparse-Weil-Reconstruction`. No new repository has been created;
owner creation and separate access are pending. Its initial scope is finite
selected cyclic-resultant reconstruction, exact bit complexity, and predecessor
comparison. The parent retains the theorem as a supporting component while
preserving its independent quantum-discovery objective.

The general quantum zeta algorithm remains prior work. The [source-aware descent
comparison](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) remains closed: known
splitting and reuse allow the ordinary route the same smaller-field backend
calls as the twist route. The reconstruction theorem does not reopen that claim
or supply an all-field quantum order-acquisition implementation.

## Preserved evidence

All earlier experiment sources, reports and third-party notices are unchanged.
The five current predecessor verifiers and the new audit verifier passed.
Historical root and 164-curve suites were not rerun. `main` and
`research/sharing-core-publication` are unchanged. The inherited [claim ledger](STATUS.md)
concerns earlier investigations; current decisions are in the numbered notes.
No native point-counting application, quantum circuit or hardware was run.

Original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, unchanged.
