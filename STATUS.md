# Claim ledger

## Current checkpoint: linewidth-weighted observable boundary, 28 September 2026

[Spectral boundary 16](exploration/phase_3/SPECTRAL_BOUNDARY_16.md) continues the
model-first direct-sampling investigation. For exact Lanczos recursion from the
normalized collective raising observable, the retained tridiagonal matrix and
its boundary residual give a sufficient total-variation bound on the complete
Lorentzian-broadened spectral law. The discarded spectrum need not be known.
The same certificate covers common binning; its failure is not a hardness test.

With q_m the exponentially time-weighted occupation of the last retained mode,
the derived bound is min(1, b_m sqrt(q_m)/(2 gamma), b_m^2 q_m/(2 gamma^2)).
The proof is a specialization of established residual-square quadratic-form and
resolvent machinery, with earlier recursion-error literature explicitly attributed.
No new generic Lanczos method, publication priority, optimality or quantum
advantage is claimed. Finite-precision recurrence errors still need accounting.

For nearest-neighbor chains, nested commutators have enclosing intervals of length
at most their order plus one. This yields a constructive O(n poly(m)4^m) arithmetic
upper bound for one classical recursion method. The bound is not a lower bound
against other methods. Small certificate depth supplies an explicit positive
classical line-mixture sampler; preprocessing is reusable across requested draws.
The quantum route remains direct spectral sampling and need not construct that
classical representation. Its linewidth-matched clock and costs remain in Note 15.

The alternating-offset family has explicit first-two-level coefficients and an
all-size sufficient two-line approximation bound. This is a structural diagnostic,
not a new experimental model or a useful quantum result. The collective observable
is not replaced by a mixture of local spectra; a two-spin negative control shows
why that would be wrong. Common phenomenological linewidth is distinguished from
order-dependent physical relaxation in prior NMR state-space-restriction results.

The [work order](work_orders/CURRENT.md) now asks whether the correlations relevant
to the alternating-offset spectrum remain classically compressible on the linewidth
time scale. Failure of an early bound, rapid operator growth or a long Pauli list
is not by itself a classical lower bound. No molecule, native package, large
simulation, third spin-off or implementation campaign has been selected.

## Executed evidence and limits

The independent NumPy checker ran twice with identical output under one BLAS thread;
-O/-OO refusal was checked. Three fixed 2-, 4- and 6-spin models supplied 36 binned
spectral comparisons, 74 moment identities, 15 sparse/dense support controls and
108 quadratic resolvent identities. Nine analytic two-mode formulas, three complex-
basis controls, collective/local and omitted-residual negative controls, and four
invalid linewidths also passed. The [report](experiments/spectral_boundary_v1/REPORT.json)
records all tested cases, including repeated exact closure of the two-spin case.

These are double-precision mathematical diagnostics, not exact-arithmetic or
interval certification, observed spectra, compiled circuits or performance data.
Continuous-TV bounds follow from the proof rather than finite bins. The new note
records code/report hashes and the source-inspection limits. Primary PDF methods
text was read; screenshot attempts failed and no figure/table numbers were used.
No upstream code or experimental data was imported. No older verifier was rerun.

## Preserved historical evidence

The complete previous ledger and its evidence links are pinned at the
[pre-boundary checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/4d601cb7d0d58f552da40784e1f333edf6bf1d78/STATUS.md).
[Model comparison 15](exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md), its clock,
classical limits, code and report are unchanged. A separately attached local
collective-X checkpoint was read but not silently substituted for the live raising-
observable convention or its clock construction. No historical result is rewritten.

Classical probability/climate exploration remains open; its source packet remains
unacquired. Manthan is paused, battery/operator candidates parked, both classical
spin-offs independent, and Phase-2 Note 27 closed. Direct samples are permitted;
model-first investigation continues and manuscript preparation remains on hold.
The original license and third-party rights are preserved. Only the parent
repository is modified; no contact, paid/unattended work, release, merge, new
repository or administration change occurred.
