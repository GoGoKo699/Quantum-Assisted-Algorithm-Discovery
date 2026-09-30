# Current task: does useful packing pricing leave a quantum-search opportunity?

30 September 2026 · `research/prx-quantum-phase2`
Read [Note 06](../exploration/phase_4/CIRCUIT_NATIVE_PRICING_06.md) and
[AGENTS.md](../AGENTS.md). No assumed fast QRAM, new repository, or manuscript.

## One selected hypothesis, not a new generic solver

A classical packing optimizer supplies item sizes, capacity, and current rational
nonnegative dual prices. A quantum routine may return a feasible bit string whose
score exceeds one. Fixed constants drive sequential reversible arithmetic; the
master, existing columns and DP work tables remain purely classical. All circuit
preparation, reflection, routing, precision, price updates and verification count.
Quantum tree generation and quantum-assisted column generation are existing work,
not novelty claims. A useful practical regime remains unestablished.

The current scope is root LP pricing in ordinary one-dimensional binary bin packing.
Do not silently substitute unbounded cutting stock, branch conflicts, or another
constraint family. Negative reduced cost does not promise immediate objective
improvement or an integer packing. The complete solver output and needed gap matter.

## The next discriminating test

Characterize pricing calls arising within a specified adequate classical column-
generation workflow, not arbitrary hard standalone knapsacks. First apply cheap
existing-column/greedy searches, fractional/core bounds, capacity DP when appropriate,
and approximation-scheme or scaled-dual bounds at the ACTUALLY needed quality.
The full-master lower bound z_R/max(1,U), for a valid pricing upper bound U, can
sometimes avoid exact no-column pricing. A constant improvement margin admits a
polynomial classical finder. Do not invent tiny margins solely to defeat it.

Identify whether remaining expensive work finds new columns or mostly proves
there are none. The proposed quantum finder helps only the former without an
additional justified certification routine. Establish the residual free-item count,
coefficient widths, target reduced cost and actual feasible-generator marked mass p
(or a justified bound), and compare against strong core/DP/branch-and-bound and
lexicographic/stabilized pricing. Extracting p may be expensive; do not supply it
free as an algorithm input merely because an offline small check knows it.

Judge setup plus all master/pricing iterations at the same LP/integer solution
quality, including failed quantum attempts, fallback certificates and recompilation.
Classical reuse of columns, dual information, approximations and alternative direct
solutions is allowed. A faster random column can still slow master convergence.
Recent pricing-filter/template results are relevant precedents with their own
problem-specific scope, not instantly transferred packing guarantees.

A small existing benchmark slice or model-level family may be used when it answers
this one question. No dataset campaign, general quantum compiler, native solver
reimplementation, or larger synthetic census is requested. If classical methods
make all useful surviving calls cheap, or certification is the real bottleneck,
park the claim early. A concrete residual opportunity justifies a focused cost
and novelty audit, not an all-classical lower-bound assertion.

## Preserved boundaries and evidence

The numerical controls in Note 06 are exact algebra on three easy illustrative
jobs, not acquired industrial pricing inputs. They check pruning, generator masses,
overflow and margin/scaled-dual logic; no FPTAS, quantum circuit or native optimizer
was executed. The final checker ran twice identically and rejects optimized Python.
No historical suite was rerun. Use saved reports without overwriting them.

The prior handover remains a dated pre-selection snapshot. Do not revive the
parked RAM-model graph or closed emitter covariance to avoid this decision.
Particle dynamics and transport remain alternatives, not parallel programs.
Only Quantum-Assisted-Algorithm-Discovery may be modified. Preserve prior science,
rights and both independent spin-offs. No outside contact, paid work, unattended
execution, branch merge, release or repository-administration change is authorized.
