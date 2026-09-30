# Phase 4 — useful mechanisms with explicit circuit costs

[Handover](../../HANDOVER.md) · [Status](../../STATUS.md) · [Current task](../../work_orders/CURRENT.md)

**Fault-tolerant circuits; no assumed fast QRAM. No useful advantage established.**
[Decision 05](NO_QRAM_HARDWARE_BOUNDARY_05.md) remains binding.

| Note | Result or decision | Current role |
|---|---|---|
| [01 — Mechanism screen](MODEL_MECHANISM_SCREEN_01.md) | Graphs, stopping, and distinct physical-source sensing | Historical shortlist |
| [02 — Task-matched readout](TASK_MATCHED_READOUT_02.md) | Calibrated signal has a strong unentangled comparator | Separate-input sensing reference |
| [03 — Gaussian graph](IMPLICIT_GAUSSIAN_GRAPH_03.md) | Graph utility and access/classical boundaries | Reference, not a gate-model speedup |
| [04 — Short-seed sparsification](SHORT_SEED_SPARSIFICATION_04.md) | Conditional RAM-model refinement | Parked; correctness/priority unresolved |
| [05 — Hardware boundary](NO_QRAM_HARDWARE_BOUNDARY_05.md) | Charge all preparation and table accesses | Binding scope |
| [06 — Circuit-native pricing](CIRCUIT_NATIVE_PRICING_06.md) | Feasible circuit generator and classical bypasses | Conditional circuit reference |
| [07 — Actual pricing workload](PRICING_WORKLOAD_07.md) | Two native-master workflows certify 48 bins on a public benchmark | No supported bottleneck in that fixed-capacity slice |
| [08 — Risk-aware pricing gate](RISK_AWARE_PRICING_GATE_08.md) | Independent uncertainty-aware application, published bottleneck, risk predicate and bound-aware target | One conditional residual-call test; no speedup or new algorithm established |

## Current evidence

```sh
python experiments/risk_pricing_gate_v1/verify.py
```

Run from the root, Python 3.10+ and standard library. The
[report](../../experiments/risk_pricing_gate_v1/REPORT.json) checks finite risk and
threshold identities, not a cloud workload or quantum circuit. The published
runtime shares in Note 08 are source-reported aggregates, not reproduced here.
The new risk constraint and confidence assumptions are explicit; Note 07's
single-capacity representation is not silently reused.

The useful target is a feasible score v>1 and v>=z_R/L, the published hybrid
criterion for skipping a particular exact bound computation. Stronger later
classical bounds may settle that task cheaply and must be tested first. No new
native solver framework or benchmark campaign is selected.

The [previous workload report](../../experiments/pricing_workload_v1/REPORT.json),
[source notice](../../experiments/pricing_workload_v1/SOURCE_NOTICE.md), and all
older science remain unchanged. [Reproduction guidance](../../handover/REPRODUCING.md)
and the [checkpoint register](../../handover/ALTERNATE_CHECKPOINTS.md) retain
historical scope. The handover is a snapshot; CURRENT.md is the sole live task.
No new repository, spin-off, manuscript or release is needed.
