# Quantum-Assisted Algorithm Discovery

**Can a circuit-model quantum computer discover a reusable classical algorithm more efficiently than a serious classical discovery process?**

The intended output is a finite, explicitly verified classical method. Its later use should not require quantum hardware. A compact discovery target can have consequences at much larger application sizes; neither compactness nor reuse alone establishes quantum advantage.

**Status: exploratory research. No useful quantum advantage, new multiplication identity, or deployed faster classical routine has been established.** See [STATUS.md](STATUS.md) for the claim boundaries.

## Current approach

**Current candidate: search only for new helper expressions, while deriving all reachable required expressions deterministically.** Exact arithmetic-schedule synthesis is the present workload; matrix multiplication supplies a calibration, not the project's exclusive scope.

In the gate-count model with free signs/copies and unlimited live storage, a linear map with `d` required non-basis directions has a circuit of at most `d+k` gates exactly when an eager target-closure search can finish with at most `k` non-target helpers. This isolates a finite helper-choice tree instead of searching execution orders. The proof, coefficient bounds, model restrictions and prospective quantum-backtracking accounting are in [the current derivation](docs/target-closure-normal-form.md).

The published dependency-search core for a known 55-addition circuit is reproduced and simplified by positive-rule closure. The same known circuit is reconstructed and checked over the integers. A precise 398-state local neighborhood is also excluded from a 54-addition target. **These are classical calibration and exclusion results, not a quantum advantage or a new arithmetic routine.** There is no claim that 55 is the latest global record or that 54 is globally novel.

The next substantive obstacle is finding a non-calibration workload where the helper choices remain expensive after strong classical deductions, and pricing an entire quantum search against that competitor. The helper tree is not yet a reversible circuit. Old raw-search resource estimates do not apply.

The earlier [staged guided flip-graph design](docs/current-design.md) and immutable experiments remain available. Further compilation of that mechanism is paused while the useful workload and simpler search parameterization are assessed; it is not declared impossible.

## Read and run

- [Current helper-only formulation and proof](docs/target-closure-normal-form.md)
- [Earlier guided design and its boundaries](docs/current-design.md)
- [Claim ledger](STATUS.md)
- [Current research task](work_orders/CURRENT.md)
- [Source provenance and checkpoint history](PROVENANCE.md)

From the repository root, with Python 3.10 or later, verify the new exact synthesis checkpoint:

```bash
python verify_target_closure.py
```

It compares both generated JSON reports byte-for-byte, including the published-core reproduction, helper-only circuit certificates, exhaustive small tests and the exact radius-two neighborhood.

Verify the preserved guided-search checkpoint separately:

```bash
python verify.py
```

For one deterministic compiled benchmark (also requires `g++` with C++17 support):

```bash
python verify.py --quick
```

For all ten archived benchmark configurations:

```bash
python verify.py --full
```

Checks run in temporary copies and do not overwrite the stored reference results. Do not use Python `-O` or `-OO`. The default verifies import hashes, reference generation, 729 integer tensor equations, ten stored witnesses, 19,683 small states, 52,488 directed legal edges, and a small coin/shift inverse test. These are classical mathematical/software checks, not quantum-hardware execution.

## What the existing benchmark says

For 64 specified seed labels and 65,536 outer steps from the 27-product binary schoolbook scheme, the stored runs reach at most 23 products in 0/64 raw, 30/64 legal-move, and 34/64 dependency-guided trials. The step costs differ. These success frequencies are not runtime speedups, do not represent the strongest published solver, and are not quantum-walk search parameters.

The main finding is that weakening the classical search can manufacture apparent difficulty. The target-closure successor applies that lesson to a published exact arithmetic synthesizer. It removes unnecessary schedule search before considering a quantum improvement.

## Scope and provenance

The original guided-search code and data are imported from the checkpoint of 25 September 2026. New target-closure work resides separately under `experiments/target_closure_v1/`, with its own manifest and licensed source provenance. Their original bytes and source archive hash are recorded in [the import manifest](provenance/import-manifest.json). Historical checkpoint ZIPs are indexed in [the history record](provenance/checkpoint-history.json); the bootstrap imports active code/data, not those binary archives.

The known 23-product reference is attributed to its pinned public source. It is a calibration certificate, not a discovery by this project. Binary-field search results do not automatically lift to real arithmetic. Standard flip graphs, directed-edge walks, amplitude amplification, Gaussian elimination, Horn closure, and quantum backtracking are prior tools, not novelty claims here.

## License

[MIT](LICENSE), Copyright (c) 2026 Ruge Lin. The repository's original license is preserved unchanged. See [PROVENANCE.md](PROVENANCE.md) for the public mathematical reference and historical attribution.
