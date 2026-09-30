# Phase 4 — useful mechanisms with explicit circuit costs

[Handover](../../HANDOVER.md) · [Status](../../STATUS.md) · [Current task](../../work_orders/CURRENT.md)

**Fault-tolerant ordinary circuits; no assumed fast QRAM.**
[Decision 05](NO_QRAM_HARDWARE_BOUNDARY_05.md) remains binding. The current bounded
hypothesis is [packing-column pricing 06](CIRCUIT_NATIVE_PRICING_06.md), not a
reopened RAM-dependent sparsifier or a demonstrated useful advantage.

| Note | Preserved result or decision | Role |
|---|---|---|
| [01 — Model/mechanism screen](MODEL_MECHANISM_SCREEN_01.md) | Graphs, stopping and separate physical-source acquisition | Historical shortlist; not blanket hardware approval |
| [02 — Task-matched readout](TASK_MATCHED_READOUT_02.md) | Calibrated signal admits a resource-matched unentangled comparator | Scope-separated sensing reference |
| [03 — Implicit Gaussian graph](IMPLICIT_GAUSSIAN_GRAPH_03.md) | Useful graph contract and access/classical boundaries | Reference, not a circuit speedup |
| [04 — Short-seed sparsification](SHORT_SEED_SPARSIFICATION_04.md) | Conditional memory refinement in a coherent-RAM model | Parked; mathematical audit and priority unresolved |
| [05 — Hardware boundary](NO_QRAM_HARDWARE_BOUNDARY_05.md) | No fast QRAM premise; charge preparation and all accesses | Binding scope |
| [06 — Circuit-native pricing](CIRCUIT_NATIVE_PRICING_06.md) | Explicit feasible-generator/search path and classical pruning, margin and master-gap bypasses | Active bounded application test; no new algorithm or advantage established |

The new role returns ordinary feasible bin patterns to a classical column-generation
solver. Existing quantum-tree and quantum-pricing literature is attributed. The
next test concerns residual workload and total optimization cost AFTER strong
classical methods, not success against uniform enumeration. Quantum failure does
not certify no improving pattern, and exact pricing may exceed the useful accuracy.

```sh
python experiments/circuit_pricing_v1/verify.py
```

Run from the repository root with Python 3.10+. The [new report](../../experiments/circuit_pricing_v1/REPORT.json)
contains exact finite algebra, not real pricing logs or a circuit benchmark. The
[readout](../../experiments/task_matched_readout_v1/),
[graph-contract](../../experiments/implicit_graph_contract_v1/), and
[short-seed](../../experiments/short_seed_sparsification_v1/) controls remain unchanged.
The [reproduction guide](../../handover/REPRODUCING.md) records their earlier scope.

Same-numbered local archives remain distinct from canonical 03/04 files; see
[the register](../../handover/ALTERNATE_CHECKPOINTS.md). The previous handover's
unselected-next-step text is a preserved snapshot, not today's work order.
No scientific history, hardware boundary, independent spin-off or rights notice
is rewritten. No new repository, branch merge, manuscript or release is started.
