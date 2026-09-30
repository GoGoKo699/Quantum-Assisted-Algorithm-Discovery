# Current task: justify a residual pricing regime before further development

30 September 2026 · `research/prx-quantum-phase2`
Read [workload 07](../exploration/phase_4/PRICING_WORKLOAD_07.md),
[circuit construction 06](../exploration/phase_4/CIRCUIT_NATIVE_PRICING_06.md), and
[AGENTS.md](../AGENTS.md). No fast QRAM, new repository, or manuscript is required.

## Completed decision test

One public 120-item Falkenauer uniform instance was solved through actual native
restricted-master LPs, classical pricing, and integer recovery. Exact equal-size
aggregation preserves the original binary root problem and leaves 58 types.
Both policies improve the 49-bin greedy incumbent to 48 bins; volume and an explicit
item assignment certify global integer optimality without completing root-LP pricing.

The exact-pricing policy has 55 pricing and 56 master calls. Greedy-first has nine
exact pricing and 80 master calls. Each full DP needs 11,042 integer updates.
The nine true fallback calls have substantial marked probability, computed offline
as a diagnostic, not supplied to the quantum algorithm. No no-column certification
call was needed before either useful answer. Do not report absent-column proving
as an observed bottleneck just because it was a previous concern.

This is a published synthetic benchmark, not an industrial trial or an all-instance
negative theorem. But fixed capacity makes larger uniform instances an inappropriate
next default test of exponential pricing difficulty. Multiplying every size and
capacity by a common factor changes units, not the feasible set. Free-item count
and a QRAM-free circuit are not, by themselves, evidence of useful quantum leverage.

## One bounded source/model gate

Before another workload, identify an independently motivated pricing regime in
published optimization practice whose effective capacity/representation and required
LP/integer accuracy survive the already identified DP, core, approximation, and
scaled-dual bypasses. Name the actual consumer, input family, what is costly to
obtain, and why its cost affects the final solution rather than just one oracle.
Retain native solver reuse and the different progress caused by different columns.

No bigger fixed-capacity census or quantum compiler is selected. The routine of
Note 06 remains a hardware-admissible candidate finder, not a proved novelty or an
eligible speedup on this tested slice. Do not force continuation because code exists.
If there is no specific credible residual case after a limited literature/model
check, park the ordinary one-dimensional pricing lead and resume the broader
ordinary-circuit mechanism screen.

Richer constraints may be considered ONLY with independent application motivation
and an explicit new input/output/circuit contract. They are not covered silently by
the binary root generator, equal-size symmetry, or knapsack approximation scheme.
Do not add dimensions, conflicts or excess digits solely to make classical pricing
fail. A universal classical lower bound is not needed to investigate a credible
conditional mechanism, but a squared sampling-cost formula alone is insufficient.

## Evidence discipline

The [verifier](../experiments/pricing_workload_v1/verify.py) and
[report](../experiments/pricing_workload_v1/REPORT.json) retain the precise two
policies, operation counts, explicit packings and separately charged probability
calculations. The normalized public input travels with its source notice.
No production branch-and-price framework, quantum search or physical runtime was
measured. The final verifier ran twice identically and rejects optimized Python;
historical scientific suites were not rerun.

Preserve all prior proofs, reports, hardware rules and rights. Only Quantum-Assisted-
Algorithm-Discovery may be modified. The graph lead stays parked, the emitter
covariance stays closed, and the two spin-offs remain independent. No outside
contact, paid/unattended work, branch merge, release or administration change follows.
