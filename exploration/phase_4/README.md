# Phase 4 — useful mechanisms with explicit circuit costs

[Handover](../../HANDOVER.md) · [Status](../../STATUS.md) · [Current task](../../work_orders/CURRENT.md)

**Fault-tolerant circuits; no assumed fast QRAM. No useful advantage established.**
[Decision 05](NO_QRAM_HARDWARE_BOUNDARY_05.md) remains binding.

| Note | Result or decision | Current role |
|---|---|---|
| [01 — Mechanism screen](MODEL_MECHANISM_SCREEN_01.md) | Graphs, stopping, and distinct physical-source sensing | Historical shortlist |
| [02 — Task-matched readout](TASK_MATCHED_READOUT_02.md) | Calibrated signal has a strong unentangled comparator | Sensing reference, separate input model |
| [03 — Gaussian graph](IMPLICIT_GAUSSIAN_GRAPH_03.md) | Graph utility and access/classical boundaries | Reference, not a gate-model speedup |
| [04 — Short-seed sparsification](SHORT_SEED_SPARSIFICATION_04.md) | Conditional RAM-model refinement | Parked; correctness/priority unresolved |
| [05 — Hardware boundary](NO_QRAM_HARDWARE_BOUNDARY_05.md) | Charge all preparation and table accesses | Binding scope |
| [06 — Circuit-native pricing](CIRCUIT_NATIVE_PRICING_06.md) | Explicit feasible generator, search and classical bypasses | Conditional construction, not a novel application advantage |
| [07 — Actual pricing workload](PRICING_WORKLOAD_07.md) | Two native-master workflows certify 48 bins on one public benchmark | No supported quantum bottleneck in this slice; residual-regime justification required |

## Latest test

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/pricing_workload_v1/verify.py
```

Run from the root, Python 3.10+, NumPy and SciPy. The
[report](../../experiments/pricing_workload_v1/REPORT.json) includes both exact
packing certificates and separately accounted operation/probability diagnostics.
The [input notice](../../experiments/pricing_workload_v1/SOURCE_NOTICE.md) distinguishes
public synthetic data from industrial records. No source answer is supplied to the
optimizer, and numerical solver flags are not the final optimality proof.

Greedy-first reduces pricing effort but requires more master iterations. Exact
capacity DP already makes the failed cheap screens inexpensive. The next task is
not a larger run of the same fixed-capacity family, a QRAM retrofit, or a new solver
framework. A credible useful residual must be identified before further quantum work.

All older notes and [controls](../../experiments/README.md) remain unchanged.
[Reproduction guidance](../../handover/REPRODUCING.md) and the
[alternate-checkpoint register](../../handover/ALTERNATE_CHECKPOINTS.md) preserve
historical scope and filename distinctions. The handover is a dated snapshot;
CURRENT.md supplies the single live task. No new repository or spin-off is needed.
