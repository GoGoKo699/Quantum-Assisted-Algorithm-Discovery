# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The output should run on ordinary
computers and address a need that exists independently of this project.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current application test: battery-interface reaction simulation

The [application case](exploration/phase_3/APPLICATION_CASE_02.md) investigates a
classical energy/force evaluator for initial electrolyte chemistry at lithium-metal
interfaces, potentially constructed using selected quantum electronic references.
Later simulations would be classical. This generic architecture is prior work;
no new simulator or advantage has been established here.

**Physical relevance remains a separate test.** Li40+EC is a finite bare-surface
calibration model, not a working battery or a proposed 50-atom battery component.
Published motivation for the chemistry does not establish that a more accurate
energy for this model improves a useful interfacial prediction. The source studies
also identify finite-size, solvent, electrode-voltage and electron-transfer issues;
see the source-backed boundaries in the [work order](work_orders/CURRENT.md).

Before substantial resource or model-development work, identify one actual
interface regime and useful observable, and explain how the calibration informs
it despite the omitted physics. If that connection cannot be supported, park or
redirect the candidate. A calibration success must not be presented as application
success. No battery-lifetime, capacity, safety or commercial benefit is claimed.

The [latest archive replay](exploration/phase_3/ARCHIVE_REPLAY_04.md) verifies the
supplied public ZIP, all 732 geometries and 30 tables, and the published Li40
calibration. It reproduces four corrected barrier estimates at printed precision
using the paper's supplied PBE surface limit. It also records the distinct PBE
series, AFQMC trial refinements absent from the ZIP, and an averaging-endpoint
ambiguity instead of silently mixing them.

The numerical geometry sequences grow lithium clusters around fixed molecular
geometries. They are not a trajectory-training dataset. A retrospective test of
one Li40 correction transferred to other cluster sizes leaves appreciable
method-relative discrepancies. A precise isolated energy therefore does not,
by itself, establish a useful reusable simulator. This does not rule out a
multi-reference or structured learning approach.

Following a supported physical-relevance case, the [work order](work_orders/CURRENT.md)
requires an application-relevant accuracy and total reference-preparation cost
comparison. The archive-access step is complete; Hamiltonian coefficients, state
preparation, native timings and a validated learned model are not. Modern classical
chemistry, active learning, and energy-only model construction remain legitimate
alternatives.

## Reproduce the archive analysis

Obtain the original `paper_data.zip` from the authors' [Zenodo deposit](https://zenodo.org/records/22116355),
DOI 10.5281/zenodo.22116355. Python 3.10+, standard library only:

```sh
python experiments/reference_archive_v1/verify.py --archive /path/to/paper_data.zip
```

The checker reads without extracting or modifying the ZIP. It checks the pinned
digest, geometry inventory, selected published arithmetic and malformed inputs.
Compare its output with the [executed report](experiments/reference_archive_v1/REPORT.json).
No raw archive, coordinates or full source tables are redistributed here; their
rights are not replaced by this repository's license.

The archive checkpoint is data/protocol verification, not an electronic-structure,
quantum-circuit, molecular-dynamics or performance benchmark. No scientific tests
were rerun for the subsequent physical-relevance documentation update. Historical
source/results remain unchanged. The earlier
[core audit](exploration/phase_3/REFERENCE_ACCESS_AUDIT_03.md) still governs the
matched 154-correlated-electron convention; the older hypothetical 74-electron
model and small HCI trial spaces are not equivalent electronic problems.

## Parked and independent work

The [first phase-3 operator construction](exploration/phase_3/MECHANISM_SCREEN_01.md)
remains parked, with its note and tests preserved.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development. Neither replaces
the parent goal.

## Organization and evidence

Scientific phase 3 uses the existing branch `research/prx-quantum-phase2`.
The [canonical project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [parent charter](exploration/phase_2/CHARTER.md) govern the exploration.
The default branch is an entry point, not a merged copy of later research.
[STATUS.md](STATUS.md) separates recorded scientific findings from historical claims;
the live work order determines the next task.
The [source-aware descent comparison](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md)
remains closed. Earlier research, third-party notices and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only the parent repository may be modified in this project context.
