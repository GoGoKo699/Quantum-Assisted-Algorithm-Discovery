# Claim ledger

## Current checkpoint: model-level spectral construction, 28 September 2026

[Note 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md) compares the two open
model families and develops finite-linewidth spectral sampling. Classical dynamics
remain open, with direct trajectory sampling as a baseline for distribution
outputs. Direct samples and model-first analysis remain authorized. No useful
quantum advantage, physical prediction improvement or publication priority is
established by this checkpoint.

### Mathematical claims and their scope

For an explicitly supplied homonuclear isotropic-spin Hamiltonian and collective
raising observable, the note specifies the normalized high-temperature correlation
measure and a Lorentzian-broadened bin-output contract. This is not arbitrary NMR
pulse output, absolute intensity or a full open-system model.

An easily factorized geometric clock and the vectorized observable state yield a
dithered Fourier measurement with a finite Poisson kernel. The limiting wrapped
law is Lorentzian; truncation, wrapping and digital-offset bounds specify its
approximation. Controlled evolution time O(log(1/epsilon)/gamma) concerns the
chosen broadened output, not exact energy gaps. Coefficient access, preparation,
simulation precision, repetitions and inference costs are not suppressed. Prior
spectral-sampling and tapering algorithms are attributed. Novelty and optimality
of the displayed composition remain unassessed.

Classical comparisons include an exact commuting-model sampler, a uniform-offset
symmetry limit, a coarse-line bound and a resolvent perturbation certificate.
Deleting isotropic bonds of total absolute coupling J_cut changes the broadened
law by at most J_cut/(2 gamma) in total variation. A supplied small-component
partition gives a classical mixture construction when that bound is adequate.
The single-line sufficient bound is proportional to offset variance/gamma^2.
The fourth spectral moment exposes a term J_ij^2(delta_i-delta_j)^2; it is a
moment of the unbroadened measure, not the heavy-tailed Lorentzian spectrum.
A solvable two-spin control makes the linewidth dependence of a secular
approximation explicit. These are not lower bounds on all classical methods.

The [work order](work_orders/CURRENT.md) selects an observable-specific classical
compression/error analysis at the required linewidth, not a data or implementation
campaign. A candidate separation must survive restricted-state, tensor-network,
cluster, direct correlation and task-equivalent output methods. Failure of the
simple sufficient bounds is not itself a quantum opportunity certificate.

### Executed verification

The NumPy checker passed twice with identical output under single-threaded BLAS;
-O/-OO refusal was checked. Five fixed systems of at most four spins verify
25 moment formulas, 15 secular-law checks, 15 cut bounds, 15 coarse-line bounds
and five observable-state identities. Additional controls cover eight two-spin
cases, a disconnected mixture, the required complex transpose, three geometric
clocks, uniform-clock mismatch, and six Cauchy-tail bounds. The
[report](experiments/spectral_structure_v1/REPORT.json) records the actual scope.

These are complex128 numerical diagnostics at tolerance 2e-10. They support the
written algebra but do not replace its proofs or certify continuous-law bounds
from finite quadrature. No experimental spectrum, native NMR package, climate
model, compiled circuit, hardware, performance benchmark or inference run occurred.
No source dataset or upstream implementation was imported. Earlier verifiers were
not rerun; their source, fixtures and reports are unchanged.

Primary model, algorithm and comparison literature was inspected. Relevant PDF
text was available, but screenshots failed; no figure/table numbers supplied an
application result. The source search was bounded, not an exhaustive novelty audit.

## Preserved historical evidence

The full preceding ledger is pinned at the
[pre-derivation checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/8134a253d94d6fd2218971c41fb54d5be51214fc/STATUS.md),
which preserves earlier source and evidence links. Old current/next headings are
checkpoint records, not competing work orders. No earlier research note, proof,
code, dataset or report was rewritten.

Climate analysis remains open; the six-file sibling packet was not acquired.
Manthan is paused, battery/operator candidates are parked, both classical spin-offs
are independent, and Phase-2 Note 27 is closed. Manuscript preparation remains
on hold. The original license and third-party rights are preserved. Only this
parent repository is modified; no contact, paid/unattended work, release, merge,
new repository or administration change occurred.
