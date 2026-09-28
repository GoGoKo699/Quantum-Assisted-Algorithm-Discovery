# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The output should run on ordinary
computers and meet a need that exists independently of this project.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current decision: the battery route is parked

The [interfacial-reference study](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md)
completed the bounded search for a useful quantum-reference task in salt-dependent
battery gas formation. Relevant classical mechanisms and experiments were found,
but a supported connection from improved electronic references to the required
prediction was not established. The selected candidate is therefore parked rather
than expanded into a general battery-modeling program.

This is not a claim that batteries are unimportant, that classical chemistry
solves every relevant problem, or that quantum chemistry cannot help. It is a
decision about the evidence for this particular parent-project route. A more
precise bare-cluster energy is not the demonstrated useful output. The decision
note records the concrete reaction candidate inspected, alternatives, source
access limits, and conditions for reopening.

The [current work order](work_orders/CURRENT.md) returns to application/mechanism
selection. Each candidate must connect a classically deployable output, a real
discovery bottleneck, a quantum mechanism, and the strongest adequate classical
route before substantial implementation. No replacement application has yet been
selected. The project is not committed to chemistry or any earlier testbed.

## Retained battery calibration

The [physical-relevance study](exploration/phase_3/PHYSICAL_RELEVANCE_05.md) records
the independent experimental motivation and the missing environment connection.
The [archive replay](exploration/phase_3/ARCHIVE_REPLAY_04.md) preserves the verified
732-geometry/30-table calibration, published-number reconstruction, and bounded
transfer diagnostic. These are fixed-molecule cluster-size scans, not a reactive
training dataset or a working-battery validation.

With a local copy of `paper_data.zip` from the authors' [Zenodo deposit](https://zenodo.org/records/22116355),
DOI 10.5281/zenodo.22116355, the historical analysis can be replayed:

```sh
python experiments/reference_archive_v1/verify.py --archive /path/to/paper_data.zip
```

Python 3.10+, standard library only. The checker reads without extracting or
modifying the ZIP. The [saved report](experiments/reference_archive_v1/REPORT.json)
records its prior execution. Raw coordinates/source tables are not redistributed
or relicensed. The [core audit](exploration/phase_3/REFERENCE_ACCESS_AUDIT_03.md)
retains the matched 154-correlated-electron convention and its limitations.

The latest checkpoint inspected primary literature and selected supplementary
figures. It added no scientific code and ran no electronic calculation, molecular
trajectory, quantum circuit, training, performance benchmark, or scientific
verifier. Historical source/results remain unchanged.

## Scope and organization

The [operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remains parked.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development. Neither replaces the
parent's quantum-discovery objective.

Scientific phase 3 uses `research/prx-quantum-phase2`. The
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [parent charter](exploration/phase_2/CHARTER.md) govern the exploration.
`main` is the public entry point, not a merged copy of later research.
[STATUS.md](STATUS.md) separates current decisions from retained evidence;
older next steps do not create parallel work orders. The
[source-aware descent comparison](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md)
remains closed. Historical proofs, code, reports, notices and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only the parent repository may be modified in this project context.
