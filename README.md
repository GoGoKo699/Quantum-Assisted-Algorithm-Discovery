# Quantum-Assisted Algorithm Discovery

**Can a circuit-model quantum computer discover a useful reusable classical method more efficiently than a serious classical discovery process?**

The final method should run classically. Compactness and reuse can make discovery worthwhile, but neither establishes a quantum discovery advantage.

**Status: exploratory. No useful quantum advantage, new multiplication identity, or deployed faster routine is established.**

## Current research decision

The latest [eleven-bank filter synthesis screen](experiments/depth2_cover_v1/README.md) is complete in its declared bounded, positive-odd shift/add model. It determines all nondominated binary-operation-count/arithmetic-depth pairs, including the two 15x15 banks omitted from the first screen. The largest bank has a target-only 25-operation, depth-three certificate. The whole new classical screen took about 0.27 seconds in one local run, not a portable or cross-solver benchmark.

**These eleven count/depth tasks are retired as quantum-advantage candidates.** The result does not rule out other synthesis workloads, bit-area or physical-timing objectives, or quantum-assisted algorithm discovery. Do not add constraints just to make the existing classical method fail.

The implementation combines a small first-layer helper coverage problem for depth two with exact depth-aware helper search for the remaining cases. Classical structure removes the apparent difficulty. Covering, signed-digit depth bounds, and helper saturation are not advertised as new general principles. No quantum circuit was compiled in this successor.

The planned native SAT-CMM/RPAG/jMCM comparison remains incomplete: package retrieval/execution was unavailable here. Our code is not their solver. That limitation does not make the explicitly solved eleven cases hard.

## Read and verify

- [Latest derivation, full Pareto table, and limitations](experiments/depth2_cover_v1/README.md)
- [Current continuation contract](work_orders/CURRENT.md)
- [Claim ledger](STATUS.md)
- [New mathematical input and access provenance](experiments/depth2_cover_v1/PROVENANCE.json)
- [Historical provenance](PROVENANCE.md)

From the repository root, with Python 3.10 or later:

```bash
python experiments/depth2_cover_v1/verify.py
```

This regenerates complete reports in temporary storage, checks 1,536 independent tiny-circuit decisions and 972 helper portfolios, and verifies 15 exact integer certificates plus 5,760 signed input evaluations. It uses only the standard library. Generate the full report, including all circuits and failed lower-budget counts, with:

```bash
python experiments/depth2_cover_v1/run_screen.py --output /tmp/new-filter-screen.json
```

Existing output files are not overwritten. Do not use Python `-O` or `-OO`.

## Earlier evidence, preserved

The original [guided flip-graph design](docs/current-design.md), [target-closure normal form](docs/target-closure-normal-form.md), [unique-helper search](experiments/unique_helpers_v1/README.md), and [first filter screen](experiments/filter_mcm_v1/README.md) remain available. Earlier raw/guided quantum resource estimates apply only to their original constructions, not these new algorithms.

Their verifiers remain `python verify.py`, `python verify_target_closure.py`, `python experiments/unique_helpers_v1/verify.py`, and `python experiments/filter_mcm_v1/verify.py`. Consult the versioned notes for optional C++ or native-Z3 requirements and actual historical verification scope. The latest turn reran the supplied previous filter default verifier and the new checks; it did not rerun every historical experiment.

## Research objective, not a platform commitment

Matrix multiplication, linear-map synthesis and filter banks are testbeds. The next substantive result must start from an independently valuable, unsupplied routine and a credible classical discovery shortfall. It must compare the cost of obtaining a qualifying routine, not inflate difficulty through unnecessary optimality proofs or weak search representations. Physical area, latency and fanout constraints require their own models; arithmetic-depth results are not clock-frequency claims.

## License

[MIT](LICENSE), Copyright (c) 2026 Ruge Lin. The original license and historical source/result files remain unchanged. All upstream source notices are retained where applicable; new coefficient data are attributed mathematical transcriptions, not imports of upstream solver code.
