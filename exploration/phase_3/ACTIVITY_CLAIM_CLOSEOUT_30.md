# Closeout 30: retain the results, stop the unsupported activity-advantage claim

29 September 2026. Repository maintenance and research-decision checkpoint.
Starting research head: `22c9594bcc7e5539c913e8c6756baf5459388bd6`.
Branch: `research/prx-quantum-phase2`.

**Decision: the two-window emission-covariance proposal is not selected for further
quantum-advantage development on the present evidence.** Its source-matched finite
calibration has an executed classical acquisition and deterministic evaluation
route. Preserve the quantum constructions, comparison, code and negative findings.
No useful quantum advantage, universal classical tractability, or quantum runtime
disadvantage has been proved. The parent exploration remains open; no replacement
application is selected by this closeout. Manuscript preparation stays on hold.

## 1. Precisely what is being closed

[Claim 28](EMISSION_ACTIVITY_CLAIM_28.md) proposed estimating
G=Cov(exp(-s K1),exp(-s K2)), with s=1/(n kappa Delta), for successive photon-count
windows. Two flags and coherent amplitude estimation give a conditional quantum
precision mechanism relative to generic sample averaging. That mechanism does not
outperform every deterministic classical calculation of the same scalar.

[Acquisition 29](CLASSICAL_ACTIVITY_ACQUISITION_29.md) and the separately executed
[cross-check 29B](CLASSICAL_ACTIVITY_CROSSCHECK_29B.md) acquired a two-mode tilted
contraction from the supplied Hamiltonian and jump operators. They did not receive
phase rates, target covariances, a stationary initial state, or fitted photon data.
Both retained the ground-start target and compared with full symmetry-reduced
propagation. Acquisition and validation work are recorded, not assumed free.

The common calibration is a seven-emitter periodic ring with Omega/kappa=50 and
V/kappa=250. Its exact invariant operator sector has dimension 1300 rather than
16384. This finite reduction remains exponential in general as n grows; it is
not an all-size complexity theorem. The sources and model assumptions are retained
in the original notes. No new literature or physical result is introduced here.

**Why stop this lead:** the proposed missing classical acquisition was actually
performed, and the resulting deterministic contractions closely reproduce the
chosen output at the tested windows. Consequently, generic 1/epsilon^2 trajectory
averaging is not the adequate sole classical baseline for this example. A quantum
resource campaign cannot be justified by that comparison alone. No compiled
quantum-versus-classical runtime comparison has been performed.

## 2. The two evidence sets remain distinct

| Record | Tested kappa Delta | Largest observed once-acquired covariance discrepancy | Additional scope |
|---|---|---:|---|
| [Note 29 report](../../experiments/activity_acquisition_v1/REPORT.json) | 1, 4, 16 | 3.3167878e-5 | One acquisition reused; full invariant propagation and validation controls |
| [Note 29B report](../../experiments/activity_acquisition_crosscheck_v1/REPORT.json) | 1, 5, 20 | 3.3167878e-5 | Separate implementation; full-space and subdivided checks; additionally reacquired tilted modes |

These are numerical checks of one shared parameter point, not six independent
applications or an external peer review. Rows from different windows must not be
combined or relabeled. In 29B the optional tilted-mode refinement at kappa Delta=5
has observed covariance discrepancy about 1.50e-8; this costs extra acquisition
and is not the once-acquired baseline. Entries below display resolution are not
exact equalities.

Individual Laplace-moment errors can exceed the covariance errors because errors
can cancel in G. A scalar contraction is not automatically a positive approximate
photon-history generator. Neither report certifies the full microscopic record,
arbitrary initial states, every counting field, or an interval enclosure of the
printed decimals. Stronger classical alternatives remain legitimate.

## 3. What remains usable

[Record instrument 25](RECORD_INSTRUMENT_25.md) retains the direct monitored quantum
construction and its record-level error accounting. [Emission memory 26](EMISSION_MEMORY_26.md)
retains the coherent excitation-truncation comparison and exact renewal limit.
Their proofs and diagnostics have not been deleted or reclassified as advantage
proofs. [Claim 28](EMISSION_ACTIVITY_CLAIM_28.md) remains a conditional algorithmic
reference with its original access, coherence, accuracy and horizon costs.

Earlier spectral, locality, trace-acquisition and reuse results remain references.
The battery/operator candidates stay parked, Manthan stays paused, and classical
probability/climate directions remain open alternatives rather than concurrent
work orders. The two independent classical spin-offs own their own development.
There is no third spin-off and no need for a new repository.

This closeout does not establish that larger emitter systems are always easy.
It also does not establish that they are hard. Increasing n, tightening epsilon,
or demanding a finer record is not, by itself, new support for reopening this
particular claim. A justified useful regime and a concrete acquisition bottleneck
would be needed; a universal lower bound is not required to explore such a claim.

## 4. Reconcile the formerly local checkpoint

The three substantive files from `Classical_Activity_Crosscheck_29B.zip` are now
stored at their distinct repository paths: the 29B note, its verifier and report.
They are imported byte-for-byte. Note 29 and its experiment are unchanged.
The [import and replay manifest](../../provenance/activity_closeout_30.json)
records the source archive digest and all three payload hashes.

Statements in the archived 29B text that it was delivered locally and was not yet
committed describe its ORIGINAL delivery. They are preserved as provenance, not
current access limitations. This closeout records its subsequent repository import.
The old patch and proposed work order are not applied as current routing; the live
work order is updated separately. No historical result is overwritten to simplify
the synchronization story.

## 5. Reproduction and closeout checks

For the original acquisition, whose saved execution remains historical here:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/activity_acquisition_v1/verify.py
```

For cross-check 29B:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/activity_acquisition_crosscheck_v1/verify.py
```

Python 3.10+, NumPy and SciPy are required. During this closeout, the unchanged 29B
script was replayed once under NumPy 2.3.5 and SciPy 1.17.0 with one BLAS thread.
It exited successfully and produced JSON byte-identical to its archived report.
The script's six invalid-input controls passed; explicit -O and -OO invocations
both refused execution before scientific checks. The ZIP passed CRC, its three
payloads matched the supplied manifest, and the Python source parsed successfully.

This is a maintenance replay of an existing finite calculation, not new research,
a benchmark, or a new independent proof audit. The two historical runs described
inside 29B are distinct from this one closeout replay. Note 29's verifier and all
other historical scientific suites were not rerun. No experimental data, quantum
circuit, larger system, new model, or performance claim is added.

The README, claim ledger and active work order must agree with this stopping
decision. The default-branch entry point and canonical project map route to the
research closeout and reflect the direct-output/model-first scope. Only routing
documentation changes on main; no research-branch merge, deletion, release, or
repository administration change is part of this checkpoint.

## 6. State at handoff

**This acquisition test is complete; the covariance advantage lead is inactive.**
There is no pending instruction to repeat it, enlarge it, compile its quantum
circuit, or draft a manuscript. The parent question remains unresolved.

A later continuation starts with the model/mechanism comparison required by
[Revision 27](STRATEGIC_REVISION_27.md), using this negative result as evidence.
No new exploration is performed in this wrap-up. Future checkpoint handoffs must
land the evidence and update the current decision before another candidate begins.
Preserve all earlier scientific files, source attribution, LICENSE and rights.
Only Quantum-Assisted-Algorithm-Discovery may be modified in this project context.
