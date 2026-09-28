# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

The original exploration sought reusable classical methods. The current
[direct-sampling extension](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
also permits quantum samples themselves to be the useful output. Converting them
into a classical program is not a requirement of this investigation.

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Current question: directly useful samples for probabilistic prediction

Chaotic-system ensemble prediction is a candidate application class. The desired
output would be samples of specified possible futures, trajectories, or forecast
quantities, consumed directly in an existing prediction or risk workflow. This
would allow quantum use at prediction time, with its cost counted. It is an
explicit change from the earlier quantum-free deployment requirement.

The [opening note](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md) connects this
question to existing ensemble forecasting, Koopman-von Neumann/Liouville quantum
representations, and classical rare-event and learned forecast generators. These
are precedents and comparators, not our algorithm or a demonstrated speedup.
A chaotic quantum circuit does not automatically sample a classical forecast law.

The [work order](work_orders/CURRENT.md) calls for one task-level comparison: a
consumer, physical/model domain, conditioning information, output law, useful
accuracy, implementable quantum mechanism and strong classical baseline. The
leading family to inspect is rare-event scenario generation. No particular model
or event has yet earned selection. No climate simulation campaign is underway.

The comparison must charge preparation, propagation, numerical accuracy, readout,
repeated sampling and validation. Classical ensembles need not store an entire
probability grid. Direct quantum samples do not automatically reduce statistical
sampling error; coherent amplitude estimation is a distinct possible output task.

## Paused synthesis work and preserved evidence

The [sample-to-logic contract](exploration/phase_3/SAMPLING_TO_VERIFIED_LOGIC_08.md)
and [encoding audit](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md) remain intact.
Native Manthan/CMSGen profiling is paused, not refuted. It was not completed;
the existing small prefix checks are not a full synthesis benchmark.

The [battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md) and
[operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
The [battery archive replay](exploration/phase_3/ARCHIVE_REPLAY_04.md), source data
rights and uploaded archive remain unchanged; no new upload is needed.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development.

## Scope and organization

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) retain their historical objectives;
Note 10 and the live work order explicitly extend the output contract for this
investigation. `main` remains an entry point, not a merged copy of later work.
[STATUS.md](STATUS.md) records the current decision and links historical ledgers.
Phase-2 [Note 27](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) remains closed.

This checkpoint is a literature screen and scope/documentation update only.
No experiment, forecast, quantum circuit, native solver or scientific verifier
was run. Historical source/results, third-party notices and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only the parent repository may be modified in this project context.
