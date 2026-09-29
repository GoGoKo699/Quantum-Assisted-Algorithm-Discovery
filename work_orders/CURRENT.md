# Current task: compare the cost of response-relevant finite regions

29 September 2026. Branch: `research/prx-quantum-phase2`.
Model-first exploration; direct samples allowed; manuscript preparation on hold.

Read [positive spatial windows 21](../exploration/phase_3/POSITIVE_SPATIAL_WINDOWS_21.md),
[model comparison 15](../exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md), and
[spectral boundary 16](../exploration/phase_3/SPECTRAL_BOUNDARY_16.md).
No dataset, molecule, native installation, learned classical program or quantum-free
deployment is an entry condition. Physical model and useful output stay explicit.

## Completed locality result

For the normalized high-temperature collective raising spectrum of the bounded
nearest-neighbor chain, cut every ell-th bond and average uniformly over all ell
boundary shifts. For each shift the disconnected collective response is exactly
the positive mixture of its block responses, with weight |block|/n. Across shifts
these form overlapping windows. Ends and original block frequency offsets are
retained. Selecting a shift and a uniformly random site samples the block weights.

A uniform single-site Lieb-Robinson envelope C exp(v|t|-mu distance) gives
 a=2+log(C)/mu+2/(exp(mu)-1)^2 and b=v/mu. With
 X_ell=9 sum_i J_i^2 (a+b/(2 gamma))/(n ell gamma^2),
continuous TV error is at most min(1,X_ell,sqrt(X_ell/2)). Common binning preserves
it. A conservative explicit chain envelope has C=2, mu=1, v=9 exp(1)J_*/2.
On-site fields can be removed for the locality proof, not for free quantum evolution.

The proof uses two collective facts: distinct cut-bond residuals have zero partial
trace on both adjacent blocks and are HS-orthogonal; the first resolvent correction
has zero expectation between single-block operator sums. LR then bounds the
remaining residual-square term. This is not a claim that full-chain cross
correlations vanish or that a local-observable theorem automatically covers O.
All frequencies, positivity and the original linewidth are retained.

A sufficient block size is O(epsilon_loc^-1[(J_*/gamma)^2+(J_*/gamma)^3]), independent
of total n. This bound can be very large and is not a necessary size or physical
correlation length. If the sufficient size exceeds n, use the uncut full model.
At uniform offsets the collective response is exactly a single line anyway.
There is no spectral gap, cutoff classification, memory-decay or parity assumption.

## Quantum and classical consequences

A classically selected block requires at most 2ell system qubits plus ancillas
for the existing doubled-register sampler. Its controlled evolution still lasts
O(log(1/epsilon_alg)/gamma). Coefficient access, preparation, block construction,
simulation precision, measurement, binning and repeated shots count. No coherent
full-chain lookup is required by the mixture, and no time fast forwarding is proved.

The SAME blocks are a classical sampler. Dense diagonalization is one explicit
upper bound, with preprocessing O((n+ell)8^ell) for all distinct intervals and
reuse across draws; it is not the best-classical cost. Uniform alternating chains
have only O(ell) distinct block templates. At fixed local parameters, linewidth
and accuracy there is therefore no exponential-in-total-n obstruction for this
sampling task. A potential advantage concerns required resolution/local response
complexity, not total spin count alone. No quantum-classical separation is shown.

## Next bounded model-level task

Use a nontrivial regime of the SAME alternating-offset model with d/J of order
one and variable gamma/J. Determine which operator/tensor or recursion information
is actually necessary inside a finite region on the linewidth time scale. Keep
the exact symmetry and commuting/secular limits as controls, and compare classical
acquisition plus reuse for M draws against direct local quantum evolution.

Do not use the loose sufficient ell as a lower bound on every classical method,
or failed tensor truncation as an all-classical hardness theorem. Seek a concrete
response-relevant compression or obstruction. The window theorem resolves total-
length dependence; repeatedly enlarging n is not the next test. A local quantum
processor may help only if the remaining block response earns its full cost.

Retain applicable restricted-state, tensor-network, effective-model and direct-
correlation methods, and physical relaxation when its assumptions apply. A common
Lorentzian kernel is not arbitrary order-dependent relaxation or a finite-temperature
state. Do not extend the chain proof to long-range graphs without new accounting.
No generic spectral filtering, locality framework, molecule search, large simulation,
compiler or third classical spin-off is requested.

## Evidence and preservation

The new NumPy checker ran twice in final form with identical JSON under one BLAS
thread; -O/-OO and six invalid inputs were rejected. Four fixed chains (2,4,6 and
a nonuniform 5-site control) check 33 partitions, 99 block-mixture bin identities,
90 cut-residual orthogonality identities, 66 first-order cancellations and 66
second-resolvent identities, 99 residual envelopes and 42 binned bounds. The
continuous result is proved, not inferred from those finite matrices. Tests are
complex128 diagnostics at tolerance 4e-9, not interval certificates or timings.
No older suite was rerun. No experimental data or upstream implementation imported.

Climate/dynamics remain open; Manthan is paused; battery/operator routes parked;
both spin-offs independent and Phase-2 Note 27 closed. Preserve all prior notes,
proofs, code, data, reports, licenses and rights. Modify only Quantum-Assisted-
Algorithm-Discovery. No outside contact, paid/unattended work, manuscript revival,
release, merge, new repository or administration change is authorized.
