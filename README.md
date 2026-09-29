# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Hardware boundary: fault-tolerant gate-model computation, without assumed fast QRAM.**
No end-to-end useful quantum advantage is established. Manuscript preparation
remains on hold. Direct samples and reusable classical outputs are both allowed.

## Current decision

[Hardware decision 05](exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md) records
the owner's exclusion of fast quantum-addressable classical memory from the
permitted assumptions. Ordinary logical qubits, coherent circuit operations and
classical control remain allowed. Every preparation and data-access step must
have a gate-level cost, including lookups into intermediate working data.

A lookup compiled into ordinary gates is not an assumed QRAM primitive, but it
must be paid for. Renaming an access routine QROM, an oracle or a block encoding
does not make it free. Detailed hardware engineering is not a prerequisite to
model-first analysis; an explicit symbolic circuit cost is.

[Short-seed sparsification 04](exploration/phase_4/SHORT_SEED_SPARSIFICATION_04.md)
is retained as conditional theory under its original RAM assumptions, not an
active hardware-compatible advantage lead. It reduces randomness storage without
eliminating coherent point-table, spanner, resistance or bookkeeping access.
Neither its scientific content nor its saved checks are changed by this decision.
Its independent correctness audit and publication priority remain unresolved.

The [current work order](work_orders/CURRENT.md) calls for a bounded useful-model
comparison within the new hardware boundary. It does not mandate a QROM retrofit,
a memory architecture, another sparsifier framework or a replacement application.

## Navigation and evidence

[Working rules](AGENTS.md) · [Status](STATUS.md) ·
[Phase-4 index](exploration/phase_4/README.md) · [Handover](HANDOVER.md) ·
[Reproduction guide](handover/REPRODUCING.md)

The [implicit-graph contract](exploration/phase_4/IMPLICIT_GAUSSIAN_GRAPH_03.md)
and all prior scientific notes, code and reports remain at their original paths.
Their conditional resource claims are not converted into QRAM-free guarantees.
The hardware decision is documentation only; no scientific verifier or new
simulation was run. Other mechanisms remain alternatives, not parallel programs.

The working branch remains `research/prx-quantum-phase2`; the name is historical.
The emitter-covariance closeout stays in force. Sensing remains scope-separated,
and electronic stopping remains a reserve subject to all current assumptions.
Both spin-offs are independent. Only this parent repository may be modified.
No new repository, branch merge or release is needed. [LICENSE](LICENSE) and
third-party rights are preserved.
