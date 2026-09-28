# Current task: determine how much observable complexity survives the linewidth

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read [spectral boundary 16](../exploration/phase_3/SPECTRAL_BOUNDARY_16.md),
[model comparison 15](../exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md),
and [AGENTS.md](../AGENTS.md). Models and quantum integration precede detailed
implementation. Direct samples remain permitted; a learned classical program
or quantum-free deployment is not required.

## Completed mathematical comparison

For exact Lanczos recursion of L=[H,.] from the normalized collective raising
observable, the retained real tridiagonal matrix T_m and the boundary residual
b_m determine a sufficient Lorentzian-sampling error certificate. With
q_m=2 gamma integral_0^infinity exp(-2 gamma t)|[exp(-i T_m t)]_(m,1)|^2 dt,
the TV error is at most min(1, b_m sqrt(q_m)/(2 gamma), b_m^2 q_m/(2 gamma^2)).
The discarded spectrum need not be known. The same bound covers common binning.
The proof specializes established Lanczos quadratic-form/resolvent error machinery;
no generic new Lanczos method, publication priority or quantum advantage is claimed.

This is a sufficient certificate, not a hardness test. Its failure does not prove
that the approximation is inaccurate or that another classical method fails.
Numerical recurrence defects, coefficient precision, cancellation in q_m and finite
output arithmetic need separate error budgets; the executed floating-point checks
are not interval certificates. Unbroadened spectral moments are not moments of the
Cauchy-broadened law, which has heavy tails.

For a nearest-neighbor chain, terms in L^k O fit within intervals of length k+1,
although their nonidentity support may contain holes. Through the residual at m,
at most 3 n 4^m Pauli strings are needed. Local indexing gives an explicit
O(n poly(m)4^m) arithmetic upper bound for one classical recursion construction.
This is neither an all-classical lower bound nor a claim that the checker is an
optimized implementation. Small certificate depth gives a real classical sampler:
diagonalize T_m, sample its positive line weights, add Cauchy broadening and bin.
Classical preprocessing can be amortized across all requested samples.

Collective cross terms are retained by using the full O. A mixture of single-site
spectra is not generally the same law, even for two spins. The disconnected-block
mixture of Note 15 is a distinct valid reduction. Keep the exact symmetry, commuting,
coarse-line, cut, and two-spin limits in the classical comparison.

## Next bounded derivation

Study the family with alternating axial offsets delta_i=(-1)^i d on an even
nearest-neighbor chain, initially with uniform or explicitly bounded couplings.
This is a structural subfamily of the justified spin model, not a claim of a new
measured compound or an industrial workload. The broadening and requested bins
are fixed by the mathematical task; do not loosen them to force tractability.

Determine whether observable-space evolution reaches increasingly extended
correlations on the linewidth time scale, and what it costs classically to retain
the information relevant to the spectrum. Use the exact d=0 collective-symmetry
limit and resolved two-spin formulas as controls. Note 16 already gives the first
two recursion levels and an all-size sufficient two-line approximation bound.
Do not treat a failed bound at those levels as evidence of hardness.

Compare exchange narrowing, a justified secular approximation, further recursion,
restricted-operator and tensor-network representations. A large Pauli list or
Lanczos coefficient is evidence about that representation only. The operator-
growth hypothesis is not a theorem for every observable or this parameter family.
A useful outcome is a parameter-dependent truncation/scaling statement or a
specific unresolved obstruction that the direct quantum dynamics can address.

Keep Note 15's linewidth-matched quantum sampler as the other side: its controlled
evolution time is O(log(1/epsilon)/gamma), with explicit preparation, coefficient
access, simulation precision, clock/readout and repeated-sample costs. It need not
compute or learn the classical recursion coefficients. Compare complete costs at
the same spectral-law quality, including the number of requested samples.

Do not conflate phenomenological Lorentzian broadening with order-dependent
physical relaxation in prior classical NMR compression results. Apply each result
only with its assumptions; do not omit physically needed relaxation to create
complexity. No molecule download, native package, large simulation, new compiler,
third spin-off or hardware resource campaign is the next step.

## Executed evidence and preservation

The new NumPy checker ran twice with identical output under one BLAS thread;
-O/-OO refusal was checked. Three fixed systems of 2, 4 and 6 spins check 36 binned
comparisons, 74 moment identities, 15 sparse/dense support controls and 108
resolvent identities, plus nine analytic boundary formulas, three complex-basis
controls, two negative controls and four invalid linewidths. These are numerical
mathematical diagnostics, not experimental spectra, compiled circuits or timing.
The note/report state tolerance and scope. No older scientific suite was rerun.

Climate/distribution evolution remain open. Missing climate data block only their
specific empirical test. Manthan stays paused; battery/operator candidates remain
parked; both classical spin-offs remain independent; Phase-2 Note 27 stays closed.
Preserve all earlier notes, code, data, reports, licenses and third-party rights.
Only Quantum-Assisted-Algorithm-Discovery may be modified. No external contact,
paid/unattended work, manuscript revival, release, merge, new repository or admin change.
