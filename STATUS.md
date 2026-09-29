# Claim ledger

## Current checkpoint: activity-claim closeout, 29 September 2026

**No useful quantum advantage is established. The standalone two-window
emission-covariance proposal is not being advanced on the present evidence.**
[Closeout 30](exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md) records the completed
decision and reconciles the previously local cross-check with the live repository.
The parent exploration remains open; no replacement application is selected in
this checkpoint. Manuscript preparation remains on hold.

## Evidence supporting the decision

[Acquisition 29](exploration/phase_3/CLASSICAL_ACTIVITY_ACQUISITION_29.md) and
[cross-check 29B](exploration/phase_3/CLASSICAL_ACTIVITY_CROSSCHECK_29B.md) evaluate
the same bounded covariance for a ground-start seven-emitter periodic ring with
Omega/kappa=50 and V/kappa=250. An exact translation/reflection reduction has
1300 operator coordinates. A two-mode tilted contraction is acquired from the
generator rather than supplied as rates, fitted to photon data, or initialized
in a free stationary state. Full invariant propagation supplies the reference.

| Evidence set | kappa Delta | Observed once-acquired absolute covariance errors |
|---|---|---|
| [29 report](experiments/activity_acquisition_v1/REPORT.json) | 1, 4, 16 | 3.3167878e-5; 3.183594e-6; 3.74512e-7 |
| [29B report](experiments/activity_acquisition_crosscheck_v1/REPORT.json) | 1, 5, 20 | 3.3167878e-5; 2.33856e-6; 2.41971e-7 |

The two implementations are separate numerical checks, not six independent
physical applications or an external review. Their windows are not interchangeable.
29B also reacquires modes of the actual tilted generator; that is extra work,
not free improvement of the once-acquired baseline. Individual moment errors
can exceed the covariance errors. Numerical cancellation in one output does not
certify a complete photon record or every observable.

These are finite complex128 diagnostics, not interval certificates or all-size
tractability results. The exact symmetry dimension still grows exponentially in
general. No quantum circuit or quantum/classical runtime comparison was performed.
The conclusion is that the tested calibration does not supply the needed
classical-acquisition obstacle, not that quantum dynamics is universally easy.

[Claim 28](exploration/phase_3/EMISSION_ACTIVITY_CLAIM_28.md) retains its conditional
flag/amplitude-estimation construction. Its improvement over generic sampling
precision does not establish superiority to deterministic classical contractions.
[Notes 25](exploration/phase_3/RECORD_INSTRUMENT_25.md) and
[26](exploration/phase_3/EMISSION_MEMORY_26.md) retain their record-level quantum
and coherent classical results. Their assumptions and scopes are unchanged.

## Repository reconciliation and validation

The previously delivered `Classical_Activity_Crosscheck_29B.zip` passed CRC.
Its note, verifier and report have been imported byte-for-byte to distinct paths.
The [manifest](provenance/activity_closeout_30.json) pins the archive and payload
hashes. Original statements in 29B about local-only delivery describe its earlier
checkpoint; Closeout 30 records the later repository import. Note 29 and all
other pre-existing scientific notes, programs and reports are unchanged.

During this maintenance checkpoint the 29B verifier was replayed once with NumPy
2.3.5, SciPy 1.17.0 and single-threaded BLAS. It passed and reproduced the saved
JSON byte-for-byte. Its six invalid-input checks passed; separate -O and -OO calls
refused execution. This is an additional replay, distinct from the two original
runs documented in 29B. Note 29's verifier and other historical suites were not
rerun. No new model, physical parameter, experiment, proof or benchmark is added.

The [work order](work_orders/CURRENT.md) no longer asks to perform the completed
acquisition. It records a closed checkpoint and a handoff, not another active
emitter calculation. The main-branch entry point and project map route to the
closeout and reflect the authorized direct-output/model-first scope. No branch
merge or release is part of this maintenance work.

## Preserved history and next-state boundary

The preceding ledger, which still described Claim 28 as a conditional lead, is
preserved at the [pre-closeout commit](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/22c9594bcc7e5539c913e8c6756baf5459388bd6/STATUS.md).
[Revision 27](exploration/phase_3/STRATEGIC_REVISION_27.md) governs a future
model/mechanism screen. This checkpoint does not begin that screen or choose a
replacement application. Larger rings or finer accuracy alone do not reopen the
activity claim. A useful new regime and a specific acquisition obstacle are needed.

Earlier spectral and dynamical results remain references. Climate/dynamics remain
open alternatives; Manthan is paused; battery/operator routes are parked; the two
classical spin-offs remain independent; Phase-2 Note 27 stays closed. No new
repository, manuscript, external contact, paid/unattended computation, branch
merge, release or administration change is initiated. LICENSE, source attribution,
third-party rights and all earlier scientific evidence are preserved.
