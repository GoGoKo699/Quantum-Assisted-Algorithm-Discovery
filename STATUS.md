# Claim ledger

## Current checkpoint: monitored record instrument, 29 September 2026

[Note 25](exploration/phase_3/RECORD_INSTRUMENT_25.md) follows the live photon-record
work order, not the distinct attached local spectral-cache Note 24. Neither old
note is overwritten. The current construction samples coarse physical emission
histories of a driven dissipative Ising model from a product initial state over
a fixed horizon. Ideal local Markov decay, supplied interaction graph and explicit
detector bins remain assumptions, not an experimental realization claim.

Adding counters to the Lindblad generator preserves the measured unraveling.
Drive rotations, ZZ rotations and exact monitored amplitude-damping steps give
a CPTP discrete instrument retaining the system state between outputs. If h=Delta/r,
counts are accumulated into the SAME detector bins Delta. Multiple emissions and
saturated >=K labels are not dropped; jumps after saturation still update the state.
For ideal primitives the entire record-plus-final-state half-diamond error is
bounded by min(1,C T h/4), with the explicitly derived local commutator constant C.
At bounded degree C is linear in n for fixed rates. Initialization, gate/instrument
precision, output arithmetic and nonideal detector models require their own budgets.
This is a sufficient first-order product-formula result, not a new generic quantum
simulation theorem, optimality result, practical speedup or publication-priority claim.

The circuit description needs n system qubits plus one recycled ancilla and
O((n+edges)T/h) local primitives, before precision synthesis and M-record repetition.
Classical quantum-jump algorithms retain a conditional 2^n-entry pure state rather
than necessarily a 4^n density matrix and may skip empty intervals. Tensor, cluster,
renewal, low-excitation, symmetry and direct-statistic methods remain allowed.
No adequate growing-system classical rank/complexity lower bound is established.

A two-emitter Omega=V=kappa=1, initially gg, two-bin control gives a dark-then-bright
probability 0.42439280916, versus 0.30266450416 for the population-rate extrapolation.
A degree-128 exact-rational Taylor calculation certifies the gap >0.121728304996.
The rate elimination is not assumed valid in this coherent regime. Independent
coherent-emitter renewal is another explicit comparator, not a Poisson straw man.
Strong-dephasing checks are different physical models, not free target modifications.
Exact classical two-emitter propagation solves the diagnostic. No collective
large-system phase, experimental benefit or all-classical hardness follows.

The [work order](work_orders/CURRENT.md) now targets conditional-memory compressibility
in the same driven family. A local jump need not factorize all remaining sites.
The next task is an output-sensitive model comparison, not another generic
instrument theorem or collection of small examples. Direct samples and model-first
exploration remain authorized. No new repository or manuscript is needed.

## Executed evidence and limitations

The final Python/NumPy/SciPy checker ran twice with identical JSON under one BLAS
thread. It constructs 81 saturated two-bin record words for two emitters and checks
four substep counts (16,32,64,128). Observed record-TV errors are about 0.0247878,
0.0123222, 0.00614229 and 0.00306634. The analytic bound is conservative and sometimes
trivial. Numerical Choi trace norms bound, but do not exactly evaluate, the
record-plus-state diamond distance. The count law includes same-site repeated
emissions, whose first-bin probability is about 0.0165283 in this control.

Separate no-count maps reproduce the coarsened dark/bright law. Rational Taylor
arithmetic certifies the event difference, separately from complex128 diagnostics
at tolerance 5e-10. Independent-emitter factorization and two dephasing controls
were checked. Six invalid inputs and -O/-OO execution were rejected. The
[report](experiments/record_instrument_v1/REPORT.json) records scope and values.
The all-size theorem follows from the proof, not a finite-system extrapolation.

Checker SHA256: `d0126af07e0e52dcf91f4425a53de72c604a52eff13a8882173abcd5b1603a5e`.
Report SHA256: `7304d69dc0a39163e476ff2de81791c416175da77b95b151825fda126b41388b`.

No quantum shots, native trajectory package, laboratory measurements, tensor
algorithm, large-system simulation or timing benchmark were used. No earlier
scientific verifier was rerun and no upstream code/data were imported. Primary
model/product-formula/elimination text was inspected; three PDF screenshots failed
and supplied no plot/table-derived results. Source inspection was bounded, not an
exhaustive novelty audit. Standard ingredients are attributed in the note.

## Preserved evidence

The complete previous ledger and its links are pinned at the
[pre-instrument checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/092b2828d2904045923ac2bf72266d00383bf56e/STATUS.md).
Earlier spectral proofs, code, reports, data and rights remain untouched.
Climate/dynamics remain open; Manthan paused; battery/operator routes parked;
both independent spin-offs retain their own projects; Phase-2 Note 27 stays closed.
Manuscript preparation remains on hold. Only this parent repository is modified;
no contact, paid/unattended work, release, branch merge or administration change.
