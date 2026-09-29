# Alternate-checkpoint register

[Handover](../HANDOVER.md) · [Reproduction guide](REPRODUCING.md)

A conversation attachment and a repository file can share a number without being
the same research record. The working branch is authoritative for continuation.
Never apply a historical patch or `NEXT_STEP.md` over the current work order.

## Note 24: explicit distinction, not a missing dependency

| Record | Subject and role |
|---|---|
| [Canonical repository Note 24](../exploration/phase_3/SAMPLING_REGIME_DECISION_24.md) | Fair reuse and a bounded move to physical emission records; the source for Notes 25 onward |
| Conversation `Sampling_Regime_Checkpoint_24.zip` | Smooth Lorentzian spectral-cache construction; an alternate, noncanonical historical checkpoint |

The alternate archive was inspected during handover and passed ZIP CRC. Its SHA256 is
`dbf7244b3065dcc03246561c2f49399aa8361dfae6cc6730de68f036246d7bfd`.
Its three substantive payload identities match the manifest inside that archive:

| Original path within the alternate ZIP | SHA256 |
|---|---|
| `exploration/phase_3/SAMPLING_REGIME_DECISION_24.md` | `229d7dc491c5b23eadc6e50eac5fe461ceb6a9022702dd614dbf269d090969ef` |
| `experiments/sampling_regime_v1/verify.py` | `e5932e6fbe270815be78f119b9a19d713165ef5ad97df0ed9defc853016c9a24` |
| `experiments/sampling_regime_v1/REPORT.json` | `ef1d6447640b13bc71274cf6bb6dec73c4f6e179437b0268d7afe69d9705d8e8` |

Those alternate payloads are **not imported or executed by this handover**. They
are not required to reproduce the canonical closed activity claim. This register
preserves the distinction and identities; it does not claim the alternate archive
is downloadable from the repository. Recover the exact original attachment before
using its content, and import under a distinct archival path if subsequently needed.
Do not overwrite the canonical files with these same-named payloads.

## Note 29B: import is complete

Unlike the alternate Note 24, the [29B cross-check](../exploration/phase_3/CLASSICAL_ACTIVITY_CROSSCHECK_29B.md),
[code](../experiments/activity_acquisition_crosscheck_v1/verify.py), and
[report](../experiments/activity_acquisition_crosscheck_v1/REPORT.json) are committed.
[Closeout 30](../exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md) and
[its manifest](../provenance/activity_closeout_30.json) document the byte-for-byte
import and maintenance replay. Original local-only delivery language is history,
not an unresolved synchronization task. Note 29 remains separate and unchanged.

## Other attachments

Some earlier conversation checkpoints use different 09/15 filenames or local
working paths. They are not aliases for repository notes without an identity check.
The phase-3 index links the canonical committed paths. This register is a focused
ambiguity check, not an exhaustive audit or import of every conversation attachment.
No original source, code, report, or negative finding was deleted to reconcile names.
