# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Fault-tolerant circuits; no assumed fast QRAM.**
No useful end-to-end quantum advantage is established. Manuscript preparation is on hold.

Direct samples and reusable classical artifacts are allowed. Mathematical models
come before implementation, but preparation, input and working-data access,
accuracy, measurement, and reuse costs must be included from the start.

## Start here

**[Current research handover](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/HANDOVER.md)**

| Destination | Purpose |
|---|---|
| [Working rules](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/AGENTS.md) | Binding hardware and research constraints |
| [Current status](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/STATUS.md) | Current decisions and claim boundaries |
| [Current work order](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/work_orders/CURRENT.md) | Sole continuation instruction; replacement not selected |
| [Exploration index](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/exploration/README.md) | Phase 4 and the preserved scientific archive |
| [Reproduction guide](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/handover/REPRODUCING.md) | Commands and their evidence limits |
| [Project map](PROJECT_MAP.md) | Branch roles and independent projects |

## Decision before the next step

[Hardware decision 05](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md)
excludes assumed fast coherent access to arbitrary large input or work tables.
Ordinary logical registers, classical control and RAM, and explicitly priced
reversible arithmetic or gate-based lookup remain allowed. Calling a lookup QROM,
an oracle, or a block encoding does not make it free.

The short-seed sparsifier is **parked as an active advantage lead**, not disproved.
Its conditional RAM-model derivation and checks remain archived under their
original assumptions; independent correctness and priority are unresolved.
The earlier emitter-covariance closeout also remains in force. No replacement
application, automatic QROM retrofit, memory-device program, or new phase is
started by this cleanup.

## Repository roles

`main` is the public entry point, not a merged copy of the research. The working
branch is `research/prx-quantum-phase2`; the name is historical. Its handover,
status, and work order are the live research references. The sharing-core branch
remains a historical archive, not a publication agenda.

[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
remain independent projects. Only this parent repository is writable here.
Existing proofs, code, data, reports, [provenance](PROVENANCE.md), the original
[MIT license](LICENSE), and third-party rights are preserved. No scientific suite
is rerun, branch merged, release made, or new repository created in this tidy.
