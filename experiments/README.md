# Experiment archive

[Handover](../HANDOVER.md) · [Reproduction guide](../handover/REPRODUCING.md) ·
[Exploration index](../exploration/README.md)

Each versioned directory is an independent checkpoint, not a stage of one pipeline.
Original source, fixtures, notices, and saved reports remain together.

## Phase-4 evidence

| Directory | What it checks |
|---|---|
| [task_matched_readout_v1](task_matched_readout_v1/) | Finite regression and Gaussian readout identities |
| [implicit_graph_contract_v1](implicit_graph_contract_v1/) | Exact graph, access-index, and comparison controls |
| [short_seed_sparsification_v1](short_seed_sparsification_v1/) | Finite hashing, matrix moments, rounding, and adaptive-seed controls |

The short-seed algorithm is parked under the no-QRAM hardware boundary. Its
checker remains useful mathematical evidence; passing it does not supply an
ordinary-circuit implementation or remove the archived coherent-RAM assumption.
No experiment is required to reproduce the owner's hardware decision.

## Earlier evidence and execution

The [phase-3 index](../exploration/phase_3/README.md) maps earlier scripts to notes.
The activity acquisition and its cross-check use different windows and remain
separate. The [guide](../handover/REPRODUCING.md) retains their commands and links.
Older guided, synthesis, sharing-core, and reconstruction work is historical;
its next-step text does not create an active task or restart an independent spin-off.

Read the source header and applicable note before running a script. Root
`verify.py` is not an all-project runner. Write regenerated reports outside the
repository; never overwrite archived output to make a new environment match.
No scientific code or report is altered or rerun in this tidy. Finite checks do
not establish proof completeness, publication priority, application usefulness,
or a quantum speedup. All licenses and third-party rights remain intact.
