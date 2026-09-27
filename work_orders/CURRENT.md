# Current task: separate the audited reconstruction result from quantum discovery

Active branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.
Read the phase-2 charter and `exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md`.
The parent quantum objective and its existing working target are unchanged.

## What the internal audit establishes

Note 28's g>=32, all-q>=2 supplied-count reconstruction theorem survived a fresh
proof derivation, numerical bit-size audit and an independently constructed
irreducible polynomial control. Its sparse query set, genus threshold and promises
are unchanged. The proof uses attributed Mobius/Newton ingredients; the new result
is the selected-data guarantee with a deterministic polynomial-bit-time decoder.

Explicit bounds now cover input sizes, logarithm range-reduction exponents,
series lengths and intermediate rational operand sizes. An irreducible degree-64
2-Weil control passes exact class/irreducibility checks, independent resultant
replay and reconstruction. This is an internal audit, not external peer review
or a machine-checked proof. It supplies no curve-realizability theorem.

A deliberate one-unit corruption of the last supplied count is accepted by the
decoder and detected by subsequent exact resultant replay. This is not a failure
of the promised-input theorem. Do not present reconstruction acceptance or
successful endpoint divisions as authentication of a curve's true orders.

## Repository separation is now justified

A focused classical reconstruction-theory project is warranted. The user is
asked to create `GoGoKo699/Sparse-Weil-Reconstruction` and provide its link.
No new repository has been created or modified in this checkpoint. Existing
write authorization remains confined to Quantum-Assisted-Algorithm-Discovery;
establish the new project context and access before importing anything there.

The proposed initial import should preserve the tested Note-28 decoder/report,
its full proof and source comparison, and Note 29's audit and fixture. Record
source commit and byte hashes before refactoring. Preserve the root MIT license
and all applicable notices. Do not transfer unrelated experimental history or
claim that the new project has an established quantum speedup.

The separate mathematical scope is sparse cyclic-resultant reconstruction of
integral q-Weil polynomials: theorem, numerical bit complexity, exact decoder,
and rigorous relation to prior results. Priority remains qualified: the inspected
primary statements do not subsume the exact bound, but the search is not exhaustive.
An external response, publication acceptance or journal status is not claimed.
Manuscript drafting remains a later step, not automatic after repository creation.

## Parent-project direction

Retain the theorem as a supporting classical component and keep the main goal:
useful compact information that is materially cheaper to obtain quantumly, with
comparable inputs, preprocessing, reuse, error handling and strong classical
alternatives. Do not continue classical reconstruction extensions indefinitely
inside the parent once the separate project is established.

Note 27's closed comparison remains binding. Known quadratic descent and reuse
let an ordinary source-aware route invoke exactly the same smaller-field backend
calls as the twist route. The new theorem does not reopen that resource claim,
resolve generic first-g+1 cyclic-resultant reconstruction, or remove the prior
quantum generator/arithmetic conditions in small fields. No automatic general
arithmetic compiler or benchmark campaign follows from the mathematical spinoff.

## Evidence and permissions

Run the new `python experiments/reconstruction_audit_v1/verify.py` and the five
preceding current verifiers as applicable. All six passed this round; expected
reports and prior source bytes remain unchanged. The new verifier pins its audited
source dependency and regenerates the exact report in temporary storage.
Historical root and 164-curve suites were not rerun. Full checkout failed on DNS;
GitHub connector access worked. No native curve counter, quantum circuit, hardware,
paid computation, outside contact or unattended work occurred.

Preserve `main`, the sharing-core branch, historical files and LICENSE. Modify no
other repository in this project context. No unrelated merge, administration change,
public release tag, submission or manuscript revival is authorized.
