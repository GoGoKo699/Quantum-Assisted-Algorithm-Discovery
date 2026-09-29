# Hardware boundary 05: fault-tolerant circuits, no assumed QRAM

29 September 2026. Baseline: `501ed110ee11abc072627aa13f79a39aa4fbfb9c`.
Branch: `research/prx-quantum-phase2`. This is an owner-directed scope decision,
not a new theorem, hardware feasibility study, or numerical checkpoint.

**Decision:** fast QRAM is outside the allowed hardware assumptions. A future
fault-tolerant gate-model processor with ordinary classical control is allowed.
The distinction applies to input and working memory, not merely the random seed.
The QRAM-dependent sparsification construction is parked as conditional theory.
No replacement scientific candidate is selected in this decision.

## The distinction is substantive

A circuit retaining a quantum state on its logical qubits is not the same resource
promise as fast coherent access to an arbitrary large classical table. The latter
performs a data-dependent lookup for a superposition of addresses. Implementability
by a universal circuit does not grant low gate count, depth, workspace or routing
cost. Circuit constructions for data access have explicit time-space tradeoffs [1].

There is active work on QRAM, including fault-tolerant protocols that explicitly
start with a specialized noisy QRAM device and retain additional classical costs
[2]. This decision neither calls QRAM impossible nor predicts its deployment date.
We do not need to resolve that hardware question: the owner declines it as a
premise of the project's useful-advantage claims.

## What is allowed and what must be charged

| Resource | Project treatment |
|---|---|
| Logical gates, ancillas, coherent registers, measurements and resets | Allowed; gate count, depth, workspace, accuracy and routing remain costs |
| Ordinary classical memory and controller | Allowed; acquisition, preprocessing and adaptive updates count |
| A function computed reversibly from a compact specification | Allowed with an explicit arithmetic/circuit budget, not a unit-cost function oracle |
| A known table compiled into gates, often called QROM | Only its actual gate implementation is allowed; compilation, lookup, ancillas and any updates count |
| Large input or work table with fast superposition-address queries | Not allowed as a QRAM/RAM-oracle assumption |
| Arbitrary amplitude encoding or block encoding of classical data | Not a free input; construction and uncomputation must be supplied and charged |

The QROM distinction is not a loophole. Existing table-lookup circuits demonstrate
nontrivial gate/ancilla tradeoffs [1]; naming a subroutine QROM does not preserve a
fast-RAM theorem automatically. Conversely, the linear scan cost of one circuit
is not a universal lower bound on every structured lookup. No new lookup bound
is claimed here, and no QRAM architecture or generic table compiler is opened.

The permitted model is ambitious fault-tolerant circuit computation, not a demand
for present-day small/noisy hardware. Trapped-ion and superconducting examples do
not commit the project to a company, technology roadmap, or native gate set.
Symbolic circuit costs suffice at the initial model stage; a laboratory build or
full compiler remains unnecessary before a useful mechanism has been identified.

## Consequence for short-seed sparsification

[Note 04](SHORT_SEED_SPARSIFICATION_04.md) and its checker/report remain unchanged.
The note derives a memory refinement in the original coherent-RAM access model.
Removing the large random-string emulator leaves input-coordinate queries,
spanner membership, resistance data and search/output dictionaries requiring
coherent access. The live source records those dependencies explicitly.

The derived RAM-model time must not now be presented as a gate-model runtime on
an ion or superconducting processor. The symbolic conversion would have to include
all access calls with their actual circuits, for example

$$
G_{\mathrm{total}}=G_{\mathrm{prepare}}+G_{\mathrm{other}}
 +\sum_j Q_j G_{\mathrm{access},j}+G_{\mathrm{uncompute}}+G_{\mathrm{readout}},
$$

with storage, depth, routing, precision and classical setup accounted separately.
This is bookkeeping, not a new bound or a claim that the terms are already known.
Short seeds make their own reversible evaluation compact; they do not make
unrelated, adaptively produced data tables compactly computable.

**Disposition:** preserve Note 04 as conditional algorithmic work, with its
correctness and publication-priority questions unresolved. Do not advance it as
an active hardware-compatible advantage lead. This is neither a mathematical
refutation nor permission to create a third classical spin-off. Graph sparsification
is not universally rejected: a distinct, fully priced gate construction could
be considered if it has an independently useful purpose and a credible comparison.
An automatic QROM retrofit or a new memory-design program is not the next task.

## Screening future candidates

Put the actual data path in the initial model statement:

**classical specification -> preparation circuit -> coherent computation ->
measurement -> useful classical output.**

For every access arrow, say whether values are fixed classical gate parameters,
computed on the logical registers, or read by an explicit lookup circuit. Include
coherent accesses to dynamically generated work data, not just the original input.
Classically reading a measured address and compiling subsequent controls does not
implement an address-superposition lookup and cannot be substituted silently.

Prefer a bounded comparison of useful tasks whose quantum step has a native
circuit description. This is not a request to find another algebra toy. A compact
formula is an access advantage only if the quantum and strongest classical routes
are compared on the same useful output. No new application is nominated merely
because it is QRAM-free. Do not automatically reopen the closed emitter result or
move back to the scope-separated physical-sensing input model.

## Sources, evidence and preservation

[1] Low, Kliuchnikov and Schaeffer, *Trading T gates for dirty qubits in state
preparation and unitary synthesis*, Quantum 8, 1375 (2024), arXiv:1812.00954v2.
Primary abstract and publisher summary inspected for explicit circuit/data-access
tradeoffs; no new synthesis optimality claim or full proof audit is made.
https://arxiv.org/abs/1812.00954
https://quantum-journal.org/papers/q-2024-06-17-1375/

[2] Dalzell et al., *A distillation-teleportation protocol for fault-tolerant QRAM*,
arXiv:2505.20265 (2025). Primary abstract inspected for its specialized-device
premise and classical-cost qualification, not to assert feasibility or impossibility.
https://arxiv.org/abs/2505.20265

Sources checked 29 September 2026; no PDF, circuit, simulation, data or scientific
verifier was analyzed/executed in this scope decision. Documentation, relative
links, branch state and the changed-file allowlist are checked. Prior scientific
notes, code, reports, handover, rights and licenses are unchanged. The permanent
[working contract](../../AGENTS.md) gives the new hardware constraint precedence
over earlier acceptance of fast coherent memory. Only the parent repository is
modified; no merge, release, new repository, external contact or paid work follows.
