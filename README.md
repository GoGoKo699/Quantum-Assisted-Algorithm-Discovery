# Quantum-Assisted Algorithm Discovery

**Can a circuit-model quantum computer discover a useful reusable classical method more efficiently than a serious classical discovery process?** The resulting method should run classically. Compactness and reuse alone do not establish quantum advantage.

**Status: exploratory. No useful quantum advantage, new sorting/multiplication record, or deployed faster routine is established.**

## Current investigation

The [sorting-completion successor](experiments/sorting_completion_v1/README.md) examines a provisional unsupplied target: an 18-input sorting network with at most ten layers, if one exists. The checked primary sources retain a 10--11 depth gap. This is a structural target, not yet a workload with established practical benefit and a strong-classical discovery-cost comparison.

Exact classical prefix reduction leaves only 243/928 Boolean states after six layers for pinned 18/28-input reference networks. An independent incremental native-Z3 encoding then searches for a suffix while retaining classical counterexamples and learned solver information. It is not the published optimized MiniSat or SorterHunter implementation.

The fixed six-layer 18-input prefix received a native UNSAT response for a four-layer completion even without symmetry restrictions; no independently checked UNSAT proof is supplied, and no global impossibility is inferred. Earlier-prefix cases remain UNKNOWN. A known-feasible 28-input control also times out, so those timeouts are not hardness evidence. A recovered eleven-layer control has 80 comparators versus 78 supplied. Its verification accounts for only about 0.214% of measured work; accelerating only that stage cannot yield a meaningful advantage for that run.

The next milestone is a strong native classical completion baseline and an execution-relevant output criterion, not another isolated quantum verifier or unpriced oracle. See the [work order](work_orders/CURRENT.md), [claim ledger](STATUS.md), and [source/measurement provenance](experiments/sorting_completion_v1/PROVENANCE.json).

## Verify the successor

With Python 3.10 or later:

```bash
python experiments/sorting_completion_v1/verify.py
```

The standard-library checks cover 1,211 exact prefix comparisons, 152 independently enumerated completion decisions, known-network certificates and the recovered suffix. The optional command additionally runs the native Z3 C shared library on all 152 small decisions:

```bash
python experiments/sorting_completion_v1/verify.py --solver
```

All generated data go to temporary paths. Never use Python -O/-OO. Recorded benchmark timings and timeout/model outcomes are observations, not deterministic expectations.

## Preserved earlier evidence

The [eleven-bank filter count/depth screen](experiments/depth2_cover_v1/README.md) is complete within its declared bounded model. These small tasks remain retired as quantum-advantage candidates; the current turn reran its default verifier successfully. The older guided-search, target-closure, unique-helper and first-filter experiments remain unchanged in their versioned directories. Consult their notes for verification scope and dependencies. Old quantum resource figures apply only to their old constructions.

The project is not committed to sorting, filters, matrix multiplication, QML or a hardware platform. The target remains a useful classical output and a defensible quantum advantage in obtaining it. All historical source/result bytes and the original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
