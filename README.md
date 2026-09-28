# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

The [direct-sampling extension](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
allows samples themselves to be useful outputs. They need not first become a
classical program. Quantum use at sampling time is allowed and fully costed.

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current candidate: joint selection of short scenario continuations

The [climate task](exploration/phase_3/HEATWAVE_SAMPLING_CONTRACT_11.md) concerns
extreme-summer histories and circulation diagnostics in an established CESM
France experiment. This is model-conditioned climate analysis, not today's
forecast or a new claim about real-world climate accuracy. Weighted classical
rare-event outputs are legitimate competitors.

The [segment derivation](exploration/phase_3/SEGMENT_SELECTION_12.md) selects a
partial history and its short continuation jointly. This preserves their
relative selection weights without estimating a separate success probability
for every parent. Standard quantum rejection/amplification can implement that
ideal conditional law. Restart loading, reversible propagation and replay are
still required; no climate circuit has been built.

A correct next-step law does not make a finite cloud an exact seasonal ensemble.
The note gives terminal guide corrections and an independent-pilot construction
for unbiased unnormalized path expectations. Finite ratios, genealogy, pilot
variance and uncertainty in the final diagnostic remain part of the comparison.
These use established sampling ingredients; no novelty or practical speedup is
claimed. Amplified success frequencies must not be used as original probabilities.

The [current work order](work_orders/CURRENT.md) now tests the remaining cost
condition against the actual five-day selection/perturbation workflow. Quantum
work must improve generation of as-yet unevaluated continuations, not simply
resampling a known list. Deterministic continuations can be cached classically.
No larger simulator, new toy census or reversible CESM port is the next task.

## Executed diagnostic

```sh
python experiments/segment_selection_v1/verify.py
```

Python 3.10+, standard library only. The [report](experiments/segment_selection_v1/REPORT.json)
contains exact artificial-law checks, finite-population and weighting controls,
and explicitly hypothetical cost sensitivities. It is not climate simulation,
gate-level simulation, a physical error budget or a performance benchmark.
The checker passed twice; -O/-OO refusal was checked. Earlier suites were not rerun.

Primary literature and public climate metadata were inspected. A small script
transfer and PDF screenshot attempts failed; no climate archive or upstream
implementation was acquired or numerically analyzed in this checkpoint.

## Preserved work and organization

Manthan [profiling and encoding](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md)
remains paused. The [battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md)
and [operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
The [battery archive replay](exploration/phase_3/ARCHIVE_REPLAY_04.md) and upload
are retained; the battery archive is not climate data.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) retain their historical objectives;
Note 10 explicitly extends the output contract. `main` is an entry point, not
a merged copy of later research. [STATUS.md](STATUS.md) records current claims
and links pinned historical ledgers. Phase-2
[Note 27](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) stays closed.
Earlier proofs, code, reports, notices and the original [MIT license](LICENSE),
Copyright (c) 2026 Ruge Lin, are preserved. Only the parent repository may be modified.
