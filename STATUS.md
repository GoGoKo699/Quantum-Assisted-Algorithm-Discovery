# Current status

30 September 2026 — circuit-native packing-pricing screen.

**Hardware-admissible hypothesis, not an established useful quantum advantage.**
Fault-tolerant ordinary circuits without assumed fast QRAM remain the contract.
Manuscript preparation stays on hold.

[Note 06](exploration/phase_4/CIRCUIT_NATIVE_PRICING_06.md) identifies a classical
input/output role: find a feasible negative-reduced-cost column for the root LP
of ordinary one-dimensional bin packing. The method compiles item sizes and current
nonnegative rational prices into reversible capacity/profit arithmetic and then
uses standard amplitude amplification. No arbitrary state, coherent database, or
quantum-addressable classical master/DP table is supplied. Its symbolic gate cost
retains coefficient widths, workspace, routing, updates and repeated calls.

These are existing ideas specialized for a controlled comparison. The quantum-tree
generator is prior work, and quantum pricing/column generation has prior literature.
No algorithmic novelty, speedup threshold or manufacturing improvement is claimed.
Multiplicity variants and branching conflicts are outside the present binary
root-pricing contract. An eligible column does not guarantee immediate LP progress,
integer feasibility or a globally optimal packing.

For any lambda>=0, the classical fractional bound and exact reduced-cost residual
identify safe fixing rules. Classical approximation schemes find a positive column
when a specified improvement margin exists. Scaling a dual by a valid pricing upper
bound gives a full-master lower bound; exact column absence may be unnecessary at
the useful LP/integer gap. Thus even the output criterion must be compared fairly.
These are standard bounds and elementary consequences, not new classical results.

The quantum search cost depends on the actual probability p of acceptable patterns
under its nonuniform feasible generator, not their fraction among feasible patterns.
The O(1/sqrt(p)) comparison is to repeated sampling of that generator, not to the
best knapsack or pricing method. Bounded failure is not a certificate of no column.
The [work order](work_orders/CURRENT.md) asks whether difficult, useful residual
calls survive adequate classical methods and whether discovery, rather than absence
certification, dominates the relevant work. No larger synthetic census is selected.

## Executed scope

The final standard-library checker ran twice with identical JSON and rejected
-O/-OO plus six invalid inputs. Three explicitly illustrative small jobs check
54 reduced-cost identities, preservation of six improving patterns, 54 scaled-dual
constraints and three approximation-margin identities. It enumerates the tiny
feasible-generator laws and detects nonuniform sampling, profit overflow, and
misuse of a stronger threshold as an absence certificate. No quantum circuit or
FPTAS implementation is run; the last checks are algebraic consequences only.

Checker SHA256: `fbf38875b5fd711a6021ec7028a6117912701e8a54b3278468a089330f0987ae`.
Report SHA256: `3d784f41d0f06f8e03925d514ac889fdfa331f25419be4a8357280bbc771d418`.
[Saved report](experiments/circuit_pricing_v1/REPORT.json).

No real pricing data, native LP/knapsack package, amplitude-amplification execution,
large instance, optical/physics simulation, quantum device, or timing benchmark
was used. No old verifier rerun or upstream code/data import occurred. Primary
HTML and abstracts were inspected with scope stated in the note; no PDF or plot
was analyzed. The search is not a complete novelty or best-algorithm audit.

## Preserved evidence

The [pre-screen ledger](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/c149437c106404709c8e19eb717da7904b835d2f/STATUS.md)
and [handover](HANDOVER.md) preserve the no-QRAM decision and prior scope. The
sparsifier remains parked, the emitter covariance stays closed, and both spin-offs
remain independent. All previous science, reports, licenses and rights are unchanged.
Only this parent repository is modified; no merge, release, new repository,
outside contact, paid/unattended work or manuscript revival follows.
