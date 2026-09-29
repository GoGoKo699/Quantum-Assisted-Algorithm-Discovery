# Research handover

29 September 2026 · `research/prx-quantum-phase2`  
**Phase 4, after the no-QRAM decision. No replacement candidate selected.**

## Objective and hardware contract

Use a fault-tolerant gate-model quantum processor to obtain useful information
more effectively than strong classical alternatives. Direct quantum samples and
reusable classical artifacts are both permitted. Model-first analysis remains
required; an implementation or dataset is not a prerequisite to a credible
mathematical opportunity.

The binding [working rules](AGENTS.md) and
[hardware decision 05](exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md) exclude
assumed fast QRAM for inputs AND intermediate/output work tables. Ordinary logical
registers, gates, measurements, resets, classical control, and classical RAM remain
allowed. Every preparation or access operation must be a reversible computation,
classical operation, or gate-compiled lookup with explicit costs. Symbolic circuit
bounds suffice initially; no near-term-device restriction or vendor is imposed.

A universal processor's ability to implement a lookup does not establish cheap
lookup. Count gates, depth, ancillas, routing, precision, setup, uncomputation,
and updates. Do not relabel a RAM oracle as QROM or a block encoding. No automatic
memory-design program or forced retrofit is requested.

**No useful end-to-end quantum advantage is established. Manuscript preparation
remains on hold.** This cleanup starts no new investigation.

## Decisions to carry forward

| Thread | Current disposition | Read |
|---|---|---|
| Short-seed quantum sparsifier | Parked under the hardware boundary; conditional RAM-model science retained | [04](exploration/phase_4/SHORT_SEED_SPARSIFICATION_04.md) and [05](exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md) |
| Implicit Gaussian graphs | Useful input/output reference, not an eligible speedup inherited from the RAM model | [03](exploration/phase_4/IMPLICIT_GAUSSIAN_GRAPH_03.md) |
| Physical-source sensing | Separate-input reference; calibrated task has an unentangled squeezed comparator | [01](exploration/phase_4/MODEL_MECHANISM_SCREEN_01.md) and [02](exploration/phase_4/TASK_MATCHED_READOUT_02.md) |
| Electronic stopping | Reserve only; preparation, physical adequacy, and circuit access still require a fresh check | [Screen 01](exploration/phase_4/MODEL_MECHANISM_SCREEN_01.md) |
| Two-window emitter covariance | Closed on present evidence after classical acquisition and validation | [Phase-3 closeout 30](exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md) |
| Spectra, full emission records, classical dynamics, and earlier synthesis | Preserved comparisons, not parallel active work orders | [Exploration index](exploration/README.md) |

The short-seed result reduces the randomness structure, not the point table,
spanner membership, resistance data, or search bookkeeping. Its mathematical
audit and publication priority remain unresolved. Parking it changes eligibility,
not the conditional proof statement. Do not present its RAM time as a gate count,
and do not create a third spin-off merely to preserve it.

The emitter closeout concerned one statistic at a finite calibration, not an
all-size classical-tractability theorem. Notes 29 and 29B retain different windows
(1/4/16 and 1/5/20) and implementations. Their full account remains in Closeout 30;
they are not independent applications, interval certificates, or a runtime ratio.

Older results do not become no-QRAM algorithms by association. A previously used
simulation, sensing, or arithmetic primitive must be reassessed under the current
input model before it is promoted into a new lead.

## One authoritative path for continuation

| Location | Responsibility |
|---|---|
| `AGENTS.md` on this branch | Binding scope, hardware, comparison, preservation, and action rules |
| `work_orders/CURRENT.md` on this branch | Sole current research instruction |
| `STATUS.md` on this branch | Live claim/disposition ledger, linked to immutable earlier ledgers |
| This handover and directory indexes | Orientation; not extra work orders |
| Numbered notes, scripts, reports, `docs/`, and `publication/` | Dated evidence under its stated assumptions |
| `main` | Public entry point and canonical project map, not a merged research copy |
| `research/sharing-core-publication` | Preserved historical branch, not an active manuscript agenda |

Read [CURRENT.md](work_orders/CURRENT.md) before acting on an old “next step.”
The no-QRAM constraint supersedes earlier acceptance of fast coherent memory.
Direct-output and model-first extensions still supersede older mandatory-classical-
program language. Phase numbering restarts; cite full paths rather than bare numbers.

The independent Algebraic-Loop-Certificates and Sparse-Weil-Reconstruction projects
own their further development. Only Quantum-Assisted-Algorithm-Discovery is writable
here. The [canonical project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md) records those roles.
No new repository, merge, release, external contact, or paid/unattended work follows.

## The next research step is not preselected

On the next explicit continuation, compare a bounded set of independently useful
model–mechanism pairs. Each proposal must connect its useful output and accuracy
to a complete path:

**Classical input → explicit preparation → coherent operations → measurement → useful output.**

For each access, identify the classical data, any changing work tables, the
circuit/control implementing it, and the cost per call and over all repetitions.
Compare against the strongest adequate classical acquisition or direct-output
bypass, with reuse allowed on both sides. State one bounded calculation that can
reject the proposed benefit. A query upper bound alone does not meet this hardware
contract; a universal classical lower bound is not required to explore a credible
conditional proposal.

Do not automatically resume the sparsifier audit, enlarge the emitter ring,
tighten a tolerance to defeat a baseline, or change to unknown physical-source
sensing to evade input loading. Reopening needs a specific useful regime and a
fully charged circuit mechanism, not sunk effort or a larger Hilbert space.
Land each checkpoint's evidence and decision before changing candidates.

## Provenance, reproduction, and verification

Use [Reproducing the evidence](handover/REPRODUCING.md) for current and historical
commands. Mathematical checks of a parked result remain reproducible; passing
them does not remove its hardware assumptions. Root `verify.py` is not an
all-project test. No scientific script is run by this maintenance pass.

The [alternate-checkpoint register](handover/ALTERNATE_CHECKPOINTS.md) distinguishes
repository Notes 03/04 from same-numbered local archives, and preserves the older
24/29B distinctions. A matching filename is not matching content. Do not apply an
old add-only patch or continuation proposal over the live files.

External battery data retain their authors' rights; the previously supplied
archive need not be requested again. Missing climate data block only the specified
empirical test. No archive is imported, relicensed, or executed during this cleanup.

[This maintenance record](handover/NO_QRAM_MAINTENANCE.json) is separate from
[the earlier handover record](handover/MAINTENANCE.json). Earlier science and both
records remain available in history. The
[pre-update handover](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/f957571985efd242cd7d4f3d8058641b483f07e5/HANDOVER.md)
preserves the detailed phase-3 orientation without duplicating it as the live agenda.
Navigation and blob checks are not a proof audit, numerical rerun, novelty review,
feasibility study, or CI result.
