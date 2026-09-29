# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Fault-tolerant circuits; no assumed fast QRAM.**
No useful end-to-end quantum advantage is established. Manuscript preparation is on hold.

Direct samples and reusable classical outputs are both allowed. We investigate
mathematical models before engineering implementations, while retaining the full
cost of preparation, data access, computation, measurement, and reuse.

## Start here

**[Research handover](HANDOVER.md)**

| Read | Purpose |
|---|---|
| [Working rules](AGENTS.md) | Persistent hardware, usefulness, and evidence constraints |
| [Current status](STATUS.md) | What is active, parked, or closed |
| [Current work order](work_orders/CURRENT.md) | Sole continuation instruction; no replacement candidate selected |
| [Exploration index](exploration/README.md) | Phase 4 and preserved earlier research |
| [Reproduction guide](handover/REPRODUCING.md) | Which checks exist and what passing them means |

## Current decision

[Hardware boundary 05](exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md)
permits ordinary logical qubits, gates, measurements, resets, classical control,
and classical RAM. It excludes assumed fast coherent access to arbitrary large
input or working tables. Reversible formulas and gate-compiled lookups are allowed
only with explicit gate, depth, workspace, precision, routing, and update costs.
QROM, state-preparation, or block-encoding terminology does not remove those costs.

[Short-seed sparsification 04](exploration/phase_4/SHORT_SEED_SPARSIFICATION_04.md)
is **parked as an active advantage lead**. Its conditional coherent-RAM result
and finite checks are preserved; a smaller randomness structure does not remove
its other coherent-table accesses. This is a hardware-admissibility decision,
not a mathematical retraction or a completed correctness/priority audit.

No automatic QROM retrofit, QRAM design project, new application, or new research
phase starts in this maintenance pass. The next explicit research continuation
will compare useful models with fully priced ordinary-circuit operations.

## Evidence and branch roles

[Phase 4](exploration/phase_4/README.md) records the current boundary and prior
screens. The [phase-3 activity closeout](exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md)
remains in force. Earlier sensing, simulation, and graph results retain their
original assumptions; none is automatically re-certified under the new boundary.

The working branch is `research/prx-quantum-phase2`; its name is historical.
`main` routes here rather than duplicating the research. The two independent
classical spin-offs retain their own projects; see [PROJECT_MAP.md](PROJECT_MAP.md).
Only this parent repository may be modified in this project context.

Existing science, code, reports, [provenance](PROVENANCE.md), the original
[MIT license](LICENSE), and third-party rights are preserved. This cleanup checks
navigation and file identity, not scientific correctness or hardware feasibility.
[Maintenance record](handover/NO_QRAM_MAINTENANCE.json).
