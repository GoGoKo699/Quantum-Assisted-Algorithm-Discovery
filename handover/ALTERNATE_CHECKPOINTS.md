# Alternate-checkpoint register

[Handover](../HANDOVER.md) · [Reproduction guide](REPRODUCING.md)

The working branch is authoritative for continuation. A conversation attachment
and a repository note can share a number or filename without containing the same
science. Do not apply an old patch, work-order proposal, or next-step file over
current routing. No alternate scientific payload is imported or executed by this tidy.

## Phase 4: local 03/04 are not replacements for committed 03/04

| Record | Canonical committed location | Distinction |
|---|---|---|
| Graph 03 | [IMPLICIT_GAUSSIAN_GRAPH_03.md](../exploration/phase_4/IMPLICIT_GAUSSIAN_GRAPH_03.md), with `experiments/implicit_graph_contract_v1/` | The attachment uses plural `IMPLICIT_GAUSSIAN_GRAPHS_03.md` and `experiments/implicit_graph_v1/`; it is a separate checkpoint |
| Short-seed 04 | [SHORT_SEED_SPARSIFICATION_04.md](../exploration/phase_4/SHORT_SEED_SPARSIFICATION_04.md), with `experiments/short_seed_sparsification_v1/` | The attachment reuses the same paths, but its note and source bytes differ from the committed files |
| Hardware 05 | [NO_QRAM_HARDWARE_BOUNDARY_05.md](../exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md) | The supplied note's blob matches the committed decision; it is not a new missing science import |

At the pre-tidy research head `f957571985efd242cd7d4f3d8058641b483f07e5`, the canonical graph note has Git blob
`3daf5a173e22904f9acd7fe0e8a6431ac832440b`; the canonical short-seed note has blob
`4a7914d74371f49546579ede5f929c116bc548e9` and its checker has blob
`158283aebf65046a41e1d684e0602c3eefc163b6`.
The attached short-seed note has blob `686f4c09179778cb274e6f8ccd6212588c8c26a9`
and checker `fdf47bc5ac0a146cb92cb5d1d722cf23b8f228b6`. Identical filenames
therefore cannot justify overwriting the repository. No substantive equivalence
or priority audit is claimed from this identity check.

The two supplied ZIP files passed CRC inspection in this maintenance:

| Attachment | SHA256 |
|---|---|
| `Implicit_Gaussian_Graph_Checkpoint_03.zip` | `b1793817a32afc92fba5638599ac738039a3d560986d5cbe43b75da31475c70b` |
| `Short_Seed_Sparsification_Checkpoint_04.zip` | `6b5936c903d9090de0d7adc2bb087fb728bea81da095b54471a37ca68af90514` |

Their substantive payload hashes and inspection limits are recorded in
[NO_QRAM_MAINTENANCE.json](NO_QRAM_MAINTENANCE.json). These attachments are not
represented as files downloadable from the repository, nor required to reproduce
the committed result. Neither is used to reopen the parked algorithm. The matched
Note 05 blob is `0dfcfa68d7764db84b9231da0238706bae12340d`.

## Phase 3, Note 24: previously recorded distinction

The [canonical Note 24](../exploration/phase_3/SAMPLING_REGIME_DECISION_24.md) concerns
fair reuse and the move to physical emission records. The conversation's
`Sampling_Regime_Checkpoint_24.zip` instead concerns smooth spectral-cache reuse.
The earlier handover recorded ZIP SHA256
`dbf7244b3065dcc03246561c2f49399aa8361dfae6cc6730de68f036246d7bfd`
and these payloads:

| Path within that alternate ZIP | SHA256 |
|---|---|
| `exploration/phase_3/SAMPLING_REGIME_DECISION_24.md` | `229d7dc491c5b23eadc6e50eac5fe461ceb6a9022702dd614dbf269d090969ef` |
| `experiments/sampling_regime_v1/verify.py` | `e5932e6fbe270815be78f119b9a19d713165ef5ad97df0ed9defc853016c9a24` |
| `experiments/sampling_regime_v1/REPORT.json` | `ef1d6447640b13bc71274cf6bb6dec73c4f6e179437b0268d7afe69d9705d8e8` |

These identities are retained from the
[previous register](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/f957571985efd242cd7d4f3d8058641b483f07e5/handover/ALTERNATE_CHECKPOINTS.md),
not newly replayed or re-imported here. The alternate archive is not a dependency
of the canonical activity closeout and is not claimed downloadable from this repo.

## Phase 3, Note 29B: repository import is complete

The [29B note](../exploration/phase_3/CLASSICAL_ACTIVITY_CROSSCHECK_29B.md),
[checker](../experiments/activity_acquisition_crosscheck_v1/verify.py), and
[report](../experiments/activity_acquisition_crosscheck_v1/REPORT.json) are committed.
[Closeout 30](../exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md) and
[its manifest](../provenance/activity_closeout_30.json) record the earlier byte-for-byte
import and replay. Original local-only delivery language is historical, not an
unresolved synchronization task. Note 29 remains separate and unchanged.

Some earlier attachments use other 09/15 names and local paths; they are not
aliases for the canonical [phase-3 index](../exploration/phase_3/README.md) without
identity checks. This register is a focused provenance guide, not an exhaustive
conversation-attachment audit. Preserve originals and their rights; import a
needed alternate only under a distinct, documented path after a separate decision.
