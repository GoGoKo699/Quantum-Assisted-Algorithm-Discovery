# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

The current [direct-sampling extension](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
allows samples themselves to be the useful output. They need not first become a
classical program. Quantum use at sampling time is allowed and fully costed.

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current direct-sampling task: extreme-summer scenarios

The [task and cost screen](exploration/phase_3/HEATWAVE_SAMPLING_CONTRACT_11.md)
selects histories and circulation diagnostics conditional on extreme summers in
an established CESM climate-model experiment. Climate researchers already use
these samples to study extremes. This is model-based climate-risk analysis,
not a forecast of today's weather or a demonstrated improvement in climate physics.
Classical importance/splitting methods, with their weights and correlations,
are the baseline; ordinary rejection sampling is not the only competitor.

One explicit quantum reference construction computes an event from a complete
random-input register, amplifies the successful inputs, measures one, and replays
the trajectory classically. It delivers a consistent scenario without tomography.
The coherent propagation, inverse operations and classical replay are not free.
No CESM quantum circuit, native model run or end-to-end advantage has been built.

The executed cost sensitivity shows how the quantum recipe must compete with a
quality-matched classical rare-event gain, not merely a huge probability grid.
Its numerical inputs are illustrative, not measured climate or hardware data.
A globally prepared exponential tilt followed by an inverse-weight correction
cannot simply multiply two supposed quantum advantages: the preparation costs
cancel that extra gain in the analyzed nested-rejection construction.

The [work order](work_orders/CURRENT.md) now asks whether short quantum stochastic
continuations can be combined with a classical rare-event method while retaining
the correct full path weights. No full reversible climate-model port or large
simulation campaign is the next task. A different guided preparation remains open;
no broad impossibility result is claimed.

## Executed check and evidence boundaries

```sh
python experiments/direct_tail_sampling_v1/verify.py
```

Python 3.10+, standard library only. The [report](experiments/direct_tail_sampling_v1/REPORT.json)
contains artificial finite-law controls and a known-probability cost table. It is
not atmospheric data, quantum hardware, or a sampling-performance benchmark.
Public climate archive metadata was inspected; runtime download failed. No raw
climate archive or upstream implementation was imported or redistributed.
Historical scientific verifiers were not rerun; their source/results are unchanged.

## Preserved work and organization

Manthan [profiling and encoding work](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md)
remains paused, not refuted. The [battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md)
and [operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
The uploaded battery archive is already verified; it is not climate data and no
new upload is needed. [Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
remain independent projects and own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) retain their historical objectives;
Note 10 explicitly extends the output contract. `main` is an entry point, not
a merged copy of later research. [STATUS.md](STATUS.md) records the present
checkpoint and links pinned historical ledgers. Phase-2
[Note 27](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) stays closed.
Earlier proofs, code, reports, notices and the original [MIT license](LICENSE),
Copyright (c) 2026 Ruge Lin, are preserved. Only the parent repository may be modified.
