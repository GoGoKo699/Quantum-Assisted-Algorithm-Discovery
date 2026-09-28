# Claim ledger

## Current checkpoint: exchange memory and resolved response, 28 September 2026

[Exchange memory 17](exploration/phase_3/EXCHANGE_MEMORY_17.md) continues the
model-first analysis of the alternating-offset spin family. It separates the
resolved response time, projected-memory duration, and classical complexity of
obtaining that memory. These are different quantities. No short-memory theorem
for growing chains, useful quantum advantage, physical prediction improvement,
publication priority or optimality is established.

For collective o and staggered v, L_d o=d v and the projected generator is
B_d=L_d-d(|o><v|+|v><o|). The exact physical resolvent is
G_d(z)=1/[z-d^2 F_d(z)], with F_d the spectral transform of B_d in v. The generator
can be written as L_d plus two known sublattice-state reflections on the doubled
register. This exposes an explicit quantum operation without an unknown projected
basis. The projection, Schur and memory-function machinery are established prior
methods; the composition is not claimed novel or resource-optimal.

A bounded variation of F_d around a constant imaginary value on a frequency window
gives a sufficient continuous-TV certificate for a single Lorentzian response.
The bound includes out-of-window mass via the unbroadened second moment. A memory-
time estimate and a statistical scalar-estimation budget specify what would be
needed to use shorter coherent evolutions. The memory tail, state/term access,
precision, shots and classical alternative costs are NOT assumed free. A memory
spectral sample is not itself a sample of the requested physical response.

An exact two-spin control demonstrates a nonuniform weak-offset limit: removing
a memory pole whose weight tends to zero can still cause a fixed spectral-bin
error when linewidth and bins shrink as d^2/J. At fixed linewidth that discrepancy
vanishes. A classical pair of lines at +/-d^2/J has a proved error tending to zero
at the same resolved scale. This is an accuracy/control result, not a quantum-hard
instance, new measured compound or failure of classical resummation.

The [work order](work_orders/CURRENT.md) selects low-frequency memory and effective
slow-mode structure for the next bounded calculation, including the overlap with
the conserved operator sector at zero offsets. Small gaps, system size and the
order of limits must be explicit. No molecule, software installation, dataset,
large simulation, full quantum compiler or third spin-off is the next task.

## Executed verification and scope

The NumPy checker ran twice with identical JSON under one BLAS thread; -O/-OO
refusals and five invalid inputs were checked. Three fixed two/four-spin models
supplied 15 projected-generator checks, nine reflection checks, 45 Schur identities,
45 memory-symmetry checks, 153 window-envelope controls, three binned comparisons
and 18 truncated-memory checks. Four d/J values supplied 24 dimer identities and
resolved-limit/corrected-pair controls. The [report](experiments/exchange_memory_v1/REPORT.json)
and note record scope, assumptions, tolerance and source/report hashes.

These are complex128 mathematical diagnostics at tolerance 3e-10, not interval
certification, compiled circuits, large-chain decay evidence, measured spectra or
timing results. Continuous claims follow from the written proofs. No quantum
hardware, native NMR package, climate simulation, model training or performance
benchmark was run. No previous scientific verifier was rerun; no upstream code,
experimental data or model weights were imported.

Primary projection, resonance and Hamiltonian-simulation sources were inspected.
A relevant primary PDF supplied methods text; its screenshot failed. No plot or
table values were used to assert results. Other comparator sources were inspected
at the scope specified in the note. The search is not an exhaustive novelty audit.

## Preserved historical evidence

The complete preceding ledger and its evidence links remain at the pinned
[pre-memory checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/c6bc4ca6f069bd1f0a7fb94c578d45b17b7b3b4b/STATUS.md).
[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md),
[spectral boundary 16](exploration/phase_3/SPECTRAL_BOUNDARY_16.md), their proofs,
clocks, classical comparisons, source and reports are unchanged. Earlier current
headings describe their checkpoints, not parallel work orders.

Direct samples remain permitted and the model-first sequence remains in force.
Classical dynamics and climate remain open; missing climate records block only
that empirical test. Manthan is paused, battery/operator candidates parked,
both classical spin-offs independent, and Phase-2 Note 27 closed. Manuscript
preparation remains on hold. Prior notes, data, code, reports, licenses and rights
are preserved. Only Quantum-Assisted-Algorithm-Discovery is modified; no contact,
paid/unattended work, release, merge, new repository or administration change.
