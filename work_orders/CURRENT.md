# Current work order: ready for a new circuit-model comparison

29 September 2026 · `research/prx-quantum-phase2`

**No replacement candidate is selected. This maintenance pass starts no research.**
Read [AGENTS.md](../AGENTS.md), [HANDOVER.md](../HANDOVER.md), and
[hardware decision 05](../exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md).
Manuscript preparation remains on hold; no new repository is needed.

## Carry forward the decision

Fault-tolerant gate-model computation is allowed; fast QRAM is not an assumption.
The restriction covers arbitrary input and changing work tables, not merely data
loading. Ordinary logical registers, classical control and RAM, reversible formulas,
and gate-compiled lookups are allowed with all gate/depth/workspace/precision,
routing, setup, update, and repeated-access costs counted. Do not hide access in
an oracle, state preparation, QROM name, or block encoding.

[Short-seed Note 04](../exploration/phase_4/SHORT_SEED_SPARSIFICATION_04.md) is parked
as an active lead. Its RAM-model theorem and finite evidence remain unchanged,
with correctness and priority questions unresolved. It is not proved wrong and
not promoted as hardware-compatible. No automatic QRAM design, table compilation,
sparsifier audit, or third spin-off is the next task.

## On the next explicit research continuation

Compare a bounded set of independently useful models with ordinary-circuit quantum
operations. For each, state the useful observable and necessary accuracy, the
shared classical input, and the full path from preparation through coherent work
to measurement and output. Identify every data access, including intermediate
bookkeeping, its circuit or classical-control implementation, and total cost.
Symbolic resource bounds suffice initially; no vendor choice, full compiler,
near-term device, or empirical benchmark is required.

Put the positive quantum mechanism, strongest adequate classical acquisition or
bypass, reuse/sample demand, and one discriminating test in the same proposal.
Neither a giant Hilbert space nor an abstract query improvement is an advantage
under this contract. A universal classical lower bound is not required to explore
a well-motivated conditional opportunity.

Do not preselect a graph retrofit, revive the closed emitter covariance, or change
to unknown-source sensing merely to avoid input costs. A graph route could return
only with a distinct useful gate construction and a credible complete comparison.
Other archived methods require fresh access and model checks before becoming leads.
Do not invent extra precision or difficult instances solely to defeat a baseline.

## Checkpoint and action discipline

Preserve prior conclusions and scientific bytes. Use
[canonical paths](../exploration/phase_4/README.md) and the
[alternate-checkpoint register](../handover/ALTERNATE_CHECKPOINTS.md); old attached
patches and next-step files do not override this work order. Finish each research
checkpoint in the repository before changing candidates.

[Reproduction instructions](../handover/REPRODUCING.md) describe opt-in checks.
No scientific suite is rerun for this tidy. Only Quantum-Assisted-Algorithm-Discovery
may be modified. Keep licenses and third-party rights. No outside contact,
paid/unattended work, manuscript revival, branch merge, release, new repository,
or administration change is authorized here.
