# Quantum-Assisted Algorithm Discovery

**Can a circuit-model quantum computer discover a reusable classical algorithm more efficiently than a serious classical discovery process?**

The intended output is a finite, explicitly verified classical method. Its later use should not require quantum hardware. A compact discovery target can have consequences at much larger application sizes; neither compactness nor reuse alone establishes quantum advantage.

**Status: exploratory research. No useful quantum advantage, new multiplication identity, or deployed faster classical routine has been established.** See [STATUS.md](STATUS.md) for the claim boundaries.

## Current approach

Matrix-multiplication algorithm synthesis is the first testbed, not the project's exclusive scope. Start from a correct bilinear algorithm, explore correctness-preserving transformations, and look for a representation admitting an inexpensive algebraic improvement.

The current candidate separates the work:

1. Simplify classically using available algebraic deductions.
2. Explore equivalent fixed-active-count representations coherently, retaining reversible edge addresses.
3. Measure a reducible representation, verify it, reduce it classically, and restart as needed.

The third step is a proposed architecture, not a completed advantage result. Guided coin preparation, addressing, marking, initialization, search parameters, and the cost of the full sequence of stages remain to be established. Earlier raw-search qubit/gate counts do not apply to it.

## Read and run

- [Current design and its boundaries](docs/current-design.md)
- [Claim ledger](STATUS.md)
- [Current research task](work_orders/CURRENT.md)
- [Source provenance and checkpoint history](PROVENANCE.md)

From the repository root, with Python 3.10 or later:

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

The main finding is that weakening the classical search can manufacture apparent difficulty. The next research task is to choose a useful synthesis output and retain the strongest relevant classical structure before claiming a quantum improvement.

## Scope and provenance

The active code and data are imported from the guided-search checkpoint of 25 September 2026. Their original bytes and source archive hash are recorded in [the import manifest](provenance/import-manifest.json). Historical checkpoint ZIPs are indexed in [the history record](provenance/checkpoint-history.json); the bootstrap imports active code/data, not those binary archives.

The known 23-product reference is attributed to its pinned public source. It is a calibration certificate, not a discovery by this project. Binary-field search results do not automatically lift to real arithmetic. Standard flip graphs, directed-edge walks, amplitude amplification, and Gaussian elimination are prior tools, not novelty claims here.

## License

[MIT](LICENSE), Copyright (c) 2026 Ruge Lin. The repository's original license is preserved unchanged. See [PROVENANCE.md](PROVENANCE.md) for the public mathematical reference and historical attribution.
