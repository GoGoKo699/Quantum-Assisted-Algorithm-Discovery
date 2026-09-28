# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The output should run on ordinary
computers and meet a need that exists independently of this project.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current decision: repair the physical model before quantum costing

The [physical-relevance study](exploration/phase_3/PHYSICAL_RELEVANCE_05.md) identifies
an experimental validation target: electrolyte-dependent ethylene evolution during
lithium deposition in anode-free cells, accompanied by inactive-lithium formation.
The experiment changes the salt while retaining the solvent mixture. It supplies
an independently motivated observable, not a quantum-computing demonstration.

Our fixed bare Li40+EC calibration does not encode that intervention. More precise
energies for the same isolated input do not by themselves predict a salt-dependent
outcome. A justified salt/interphase-aware description is needed; electronic
accuracy has not been established as the dominant bottleneck. Initial molecular
bond breaking is also not the same observable as gas escaping an operating cell.

The [current work order](work_orders/CURRENT.md) requires inspecting an existing
classical interfacial description and identifying at most one electronic reference
whose improvement would affect a useful prediction. If that connection cannot be
supported, park this application. No large simulation, general framework or
bare-cluster quantum resource campaign is the next task.

The known experimental contrast is a validation requirement, not a new discovery.
Any eventual reusable classical model must also predict an unfit condition or
provide equally useful predictions at lower total cost. The generic architecture
of quantum reference generation followed by classical deployment is prior work.
No new simulator, battery-lifetime improvement or commercial benefit is claimed.

## Retained calibration and reproduction

The [archive replay](exploration/phase_3/ARCHIVE_REPLAY_04.md) records the verified
public ZIP, 732 geometries, 30 data tables, published-number reconstructions and a
bounded transfer test. These are fixed-geometry cluster-size scans, not a reactive
training dataset. Calibration integrity does not establish application validity.

With a local copy of `paper_data.zip` from the authors' [Zenodo deposit](https://zenodo.org/records/22116355),
DOI 10.5281/zenodo.22116355, run:

```sh
python experiments/reference_archive_v1/verify.py --archive /path/to/paper_data.zip
```

Python 3.10+, standard library only. The checker reads without extracting or
modifying the ZIP. The [saved report](experiments/reference_archive_v1/REPORT.json)
documents its historical execution. Raw coordinates/source tables are not
redistributed or relicensed. The [core audit](exploration/phase_3/REFERENCE_ACCESS_AUDIT_03.md)
still governs the matched 154-correlated-electron convention.

The current relevance study inspected literature and selected PDF figures and
rechecked the ZIP digest and two geometry members. It did not rerun the full
archive checker or historical suites, calculate electronic structure, simulate a
quantum circuit, train a model, or benchmark a speedup.

## Scope and organization

The [operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remains parked.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [parent charter](exploration/phase_2/CHARTER.md) govern the exploration.
`main` is the public entry point, not a merged copy of later research.
[STATUS.md](STATUS.md) separates current decisions from historical evidence;
previous notes do not create parallel work orders. The
[source-aware descent comparison](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md)
remains closed. Historical proofs, code, reports, notices and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only the parent repository may be modified in this project context.
