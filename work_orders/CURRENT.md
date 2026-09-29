# Current task: conditional many-body memory in physical emission records

29 September 2026. Branch: `research/prx-quantum-phase2`.
Model-first exploration; direct samples allowed; manuscript preparation on hold.

Read [record instrument 25](../exploration/phase_3/RECORD_INSTRUMENT_25.md),
[live sampling decision 24](../exploration/phase_3/SAMPLING_REGIME_DECISION_24.md),
and [AGENTS.md](../AGENTS.md). No new repository or third spin-off is needed.
The attached local spectral-cache Note 24 is not the live same-numbered record
screen. Both are preserved, not silently interchanged. This continues the live task.

## Completed construction

For driven dissipative Ising emitters with local jumps sqrt(kappa_i)|g><e|,
a product initial state, fixed horizon T and detector bins Delta, lift the jump
generator to photon counters. A local step applies all transverse rotations,
all ZZ rotations, and exact monitored amplitude damping, retaining the conditional
system state and resetting only the ancillary detector qubit. Sum internal-step
counts into the original detector bins; h=Delta/r is numerical, not the detector
resolution. Saturated output labels include all later emissions and state updates.
No record postselection, stationary-state oracle or free burn-in is assumed.

With
C=sum_edges |Vij|(|Omega_i|+|Omega_j|)+4 sum_i |Omega_i|kappa_i
 +2 sum_edges |Vij|(kappa_i+kappa_j),
the full record-plus-final-state half-diamond error is at most C T h/4, capped at
one, for ideal primitives. It bounds record TV and every bounded record statistic.
The proof uses contractive semigroup product identities on the lifted instrument,
not a bound after erasing records. At bounded degree C is linear in n for fixed
rates. The construction uses n system qubits and one recycled ancilla, with
O((n+edges) T/h) local primitives. Precision, initial state, reset/measurement,
classical output, repeated histories and detector assumptions still count.
These are existing collision/trajectory/product-formula ingredients specialized
and proved here, not a generic simulation novelty or quantum advantage.

## Matched classical comparison and actual finding

Classical quantum-jump methods propagate a 2^n-entry conditional pure state, not
necessarily a 4^n-entry density operator; event-driven implementations may avoid
empty steps. Tensors, clusters, symmetries, low-excitation and hidden-state models
are allowed. A consumer needing only a dark probability may use direct no-count
evolution rather than full histories. Typicality, spectral clocks and old
infinite-temperature bounds do not transfer automatically to monitored records.

For two emitters Omega=V=kappa=1 initially gg, two detector bins of width 2 give
P(dark,bright)=0.42439280916. A population adiabatic-elimination extrapolation
gives 0.30266450416; their event difference is certified above 0.121728304996 by
rational Taylor bounds. The rate limit is not claimed valid at coherent equal
scales. Exact independent-emitter renewal is another control. Neither discrepancy
is a classical hardness result: exact two-emitter propagation solves the model.
Strong-dephasing controls modify the physical model and are not free operations
on the target. No large-system intermittency or experiment is demonstrated.

## Next bounded model-level question

In the SAME driven interacting-chain family, determine whether monitoring permits
an adequate finite conditional-memory, cluster or tensor representation for a
specified joint temporal record statistic, or whether a concrete response-relevant
many-body dependency survives. Retain fixed input/initialization, finite horizon,
detector bins and target error. State which approximation is tested and how its
error enters the actual record law, not only the averaged density state.

A local emission resets its site but need not factorize the remaining sites.
Do not assert a renewal process from that reset without proving the conditional
independence. Strong monitoring may simplify classical propagation; weak monitoring
may require longer histories to see events. Both costs must remain. Do not infer
classical hardness from full-vector entanglement or a huge history alphabet.

The result should identify one defensible regime or structural obstruction to a
specific classical reduction, not produce another generic Trotter theorem, more
two-emitter examples or an implementation campaign. If no specific opportunity
survives the adequate classical descriptions, retain the completed result and
broaden mechanisms. Direct spectral and classical-dynamics alternatives remain open.

## Evidence and boundaries

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/record_instrument_v1/verify.py`
requires Python 3.10+, NumPy and SciPy. The final checker ran twice identically,
rejected -O/-OO and six invalid inputs. One two-emitter instrument has 81 saturated
record words and four step refinements; it checks local damping, record/final-state
Choi bounds, coarse dark maps, rational event bounds and two separate dephasing
controls. Floating matrix diagnostics are not interval certificates. The general
law follows from the proof, not extrapolation of the finite check.

No sampled quantum shots, laboratory data, native trajectory package, tensor run,
large-system simulation or performance benchmark was used. No older verifier
was rerun; no upstream code/data were imported. Primary PDFs supplied model/method
text but three screenshots failed, with no figure-derived numbers used.
Preserve all old proofs, code, reports, data, licenses and third-party rights.
Only Quantum-Assisted-Algorithm-Discovery is writable. No outside contact, paid or
unattended work, manuscript revival, release, merge or repository administration.
