# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The output should run on ordinary
computers and meet a need that exists independently of this project.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current sampling contract: examples become verified classical logic

The [new contract](exploration/phase_3/SAMPLING_TO_VERIFIED_LOGIC_08.md) investigates
quantum-produced examples in Boolean functional synthesis: learn candidate logic
from valid input/output examples, formally check and repair it, then deploy the
verified program classically. This refines the [sampling opening](exploration/phase_3/USEFUL_SAMPLING_07.md)
without changing the classical-only deployment objective.

The classical consumer already exists in Manthan. A published classical experiment
shows that replacing its sample source changes complete synthesis performance.
This is an application precedent, not our benchmark or evidence of quantum advantage.
The inspected current implementation already uses CMSGen and strong preprocessing;
those capabilities must remain in the comparator.

The first explicit quantum producer uses standard weighted amplitude amplification.
Its bound beats rejection sampling, not automatically modern SAT samplers. With
identical complete training-batch laws, the learner behaves identically in law;
only acquisition cost can improve. Different quantum laws must instead beat
classical sources of equally useful examples. Uniform satisfying pairs need not
give uniform input coverage, and sample validity is not final-program correctness.

The [work order](work_orders/CURRENT.md) calls for one native, instrumented
sample-source comparison on an application-derived instance before substantial
quantum implementation. No native Manthan/CMSGen run, useful new circuit,
quantum-resource estimate or industrial performance improvement is established.
A benchmark filename alone does not validate a deployed application.

## Executed checks

Python 3.10+, standard library only:

```sh
python experiments/sampling_synthesis_v1/verify.py
```

The [report](experiments/sampling_synthesis_v1/REPORT.json) records finite logical
and exact ideal-amplitude checks, including zero-success and easy-preprocessing
controls. These are diagnostic checks, not native synthesis, noisy/gate-level
simulation, a sampling-speed benchmark or an application result. Historical
scientific suites were not rerun; their source and reports are unchanged.

## Parked work and organization

The [battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md) and
[small-operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
The [battery archive replay](exploration/phase_3/ARCHIVE_REPLAY_04.md), source,
report and uploaded archive are retained; no new upload is needed.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [parent charter](exploration/phase_2/CHARTER.md) govern the exploration.
`main` is the public entry point, not a merged copy of later research.
[STATUS.md](STATUS.md) gives current claims and a pinned historical ledger;
older next steps do not create parallel work orders. Phase-2
[Note 27](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) remains closed.
Historical proof notes, code, data, reports, third-party notices and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only the parent repository may be modified in this project context.
