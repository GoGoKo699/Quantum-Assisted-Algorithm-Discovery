# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

The [direct-sampling extension](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
allows samples themselves to be useful outputs. They need not first become a
classical program. Quantum use at sampling time is allowed and fully costed.

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current test: variation among futures of the same saved state

The [climate task](exploration/phase_3/HEATWAVE_SAMPLING_CONTRACT_11.md) concerns
extreme-summer histories and circulation diagnostics in the published CESM France
experiment. This is model-conditioned analysis, not an operational forecast.
The [segment construction](exploration/phase_3/SEGMENT_SELECTION_12.md) gives an
ideal law-correct joint history/continuation sampler with explicit finite-population
weights. It has not been implemented for CESM or shown to improve total cost.

The [continuation-information audit](exploration/phase_3/CONTINUATION_INFORMATION_13.md)
specifies the next empirical test: compare genuinely perturbed children of the
same checkpoint, over the next segment and before later selection. Large variation
across unrelated parents is not evidence of this within-parent opportunity.
A classical comparator can select parents using valid parent-specific score
bounds and reject only the remaining variation. The quantum producer may exploit
the same information. Those bounds and their costs remain to be established.

The authors' record lists the relevant raw histories, ancestry and scripts, but
runtime transfers have failed. No sibling variance, score acceptance probability,
restart-memory budget or timing has been measured. The
[current work order](work_orders/CURRENT.md) calls for the small original France
packet specified in Audit 13, not another artificial example or a larger simulator.
The scalar archive is not a full collection of model restart states.

## Retained diagnostic and evidence

```sh
python experiments/segment_selection_v1/verify.py
```

Python 3.10+, standard library only. The [saved report](experiments/segment_selection_v1/REPORT.json)
records earlier finite-law controls, not a climate or quantum-performance run.
Audit 13 did not rerun this checker or any historical scientific suite. It adds
source inspection, an elementary comparator calculation and a data-analysis
specification; no new scientific code, simulation or measured advantage.

## Preserved work and organization

Manthan [profiling and encoding](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md)
remains paused. The [battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md)
and [operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
The [battery archive replay](exploration/phase_3/ARCHIVE_REPLAY_04.md) and upload
are retained; that archive is not climate data and no new battery upload is needed.
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
