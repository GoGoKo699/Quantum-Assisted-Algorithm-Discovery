# Target closure and helper-only synthesis, v1

Research date: 25 September 2026. **Classical exact synthesis and a candidate search normal form; no quantum advantage, new matrix identity, or practical runtime improvement is established.**

## What changed

Before pricing a coherent search, eliminate scheduling choices that classical reasoning does not need. With free copying/sign changes and unlimited live storage, producing a required linear form can only help. The feasibility check in the cited published zero/one-helper synthesizer is positive-rule reachability, solvable by forward closure instead of subset breadth-first search.

For an integer linear map with `d` distinct nonzero non-basis target vectors up to sign, a circuit of at most `d+k` binary additions/subtractions can be sought by branching only on at most `k` non-target helper vectors, saturating constructible targets after every choice. This is a proved normal form under the specified gate-count model; its novelty has not been audited. Horn closure and quantum backtracking are established methods. See [the derivation](../../docs/target-closure-normal-form.md).

## Reproduce without modifying stored evidence

```bash
python verify_target_closure.py
```

Run that command from the repository root. Python 3.10+ and its standard library suffice. It checks the successor manifest, executes both programs in a disposable directory, compares the generated JSON byte-for-byte, and rechecks the files. Do not use `-O` or `-OO`.

Individual runs require a new output path:

```bash
python experiments/target_closure_v1/probe.py --output /tmp/qaad-closure-new.json
python experiments/target_closure_v1/neighborhood.py --radius 2 --output /tmp/qaad-neighbors-new.json
```

The optional timing output from `probe.py` is observational only and is not the fixed benchmark. In particular, its two timers have different floor-test coverage. We do not report their ratio as a speedup.

## Published-core calibration

Karunaratne and Idamekorala, arXiv:2607.28676v1, give a fixed-oriented 55-addition, 23-product 3x3 multiplication circuit. We transcribed the relevant functions from their public synthesizer into a licensed extracted module. We reused its option and candidate generation, original BFS, candidate order, and first-hit rule. We did not reproduce its entire command-line application or the native C++/GPU heuristic ecosystem.

| Factor | Target directions | All auxiliary candidates | Tested until first hit | Native BFS states popped | Closure node firings | Exact additions |
|---|---:|---:|---:|---:|---:|---:|
| U | 12 | 346 | 16 | 1,459 | 204 | 13 |
| V | 13 | 372 | 123 | 26,642 | 1,115 | 14 |
| W factor | 13 | 369 | 121 | 15,577 | 1,106 | 14 |

The work columns are different primitives, not equal-cost operations or a wall-clock comparison. Both methods reject the target-only floor and identify the same first successful helper. The independent helper-only search constructs factor circuits of these lengths. Reversing the W circuit gives 28 output additions, for a total of 55. Exact linear-map replay and all 729 integer multiplication equations pass. This is a known optimum for the fixed tensor/orientation, not a quantum-advantage workload.

## Further checks

- All 4,096 three-node positive-rule systems, tested with four goal prefixes: 16,384 BFS/closure agreement checks, including cycles.
- 45 two-input integer target-pair decisions versus independent unrestricted full-circuit enumeration through three gates. Doubling is allowed; there is no intermediate coefficient cutoff.
- 42 three-input binary target/budget decisions versus unrestricted enumeration through four gates.
- A defined integer-ternary flip neighborhood around the cited tensor: 30 states at distance one and 368 additional states at distance two. Exact direction/closure lower bounds exclude every one from a 54-addition target (indeed all need at least 56). All 290,142 nonroot tensor equations pass. State-set hashes are recorded.

The neighborhood does not cover all rank-23 tensors, basis changes, coefficient lifting, or paths involving expansions. Exclusion of a finite neighborhood is not global hardness. The threshold 54 is a local test below this historical 55-addition reference, not an asserted current global record target.

## Files and provenance

- `probe.py`: independent closure, helper-only synthesis, replay, transposition, and comparison tests.
- `neighborhood.py`: fully specified small integer-ternary neighborhood and lower-bound screening.
- `cn122_source.json`: mathematical/source-data transcription to compact `[wire, sign]` arrays, not a byte-identical upstream file.
- `vendor/upstream_dependency.py`: selected upstream functions with local imports/header, not an entire byte-identical upstream module. Upstream MIT licenses are included.
- `results.json`: deterministic output and full generated classical circuit certificates.
- `neighborhood_results.json`: deterministic finite-neighborhood summary and canonical hashes.
- [Pinned source records](../../provenance/target-closure-sources.json).

No physical or logical quantum resource estimate is transferred from the earlier raw/guided walks. A possible binary helper-choice tree is now specified mathematically, but has not been reversibly compiled or shown to beat strong classical discovery.
