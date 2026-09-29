# Current task: price the response information needed by a classical sampler

29 September 2026. Branch: `research/prx-quantum-phase2`.
Model-first exploration; direct quantum samples allowed; manuscript on hold.

Read [response readout 22](../exploration/phase_3/RESPONSE_READOUT_22.md),
[spatial windows 21](../exploration/phase_3/POSITIVE_SPATIAL_WINDOWS_21.md),
[model comparison 15](../exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md),
and [spectral boundary 16](../exploration/phase_3/SPECTRAL_BOUNDARY_16.md).
No new repository is needed. Do not revive a classical-only deployment requirement.

## Completed output-level comparison

The same alternating-offset, scalar-coupled block has collective raising response
C(t)=<o,exp(-itL)o>. A mismatch in this scalar return amplitude lower-bounds the
Lorentzian spectral TV by exp(-gamma|t|)|Delta C(t)|/2. For a specified bin task,
include the additional within-bin and tail correction; arbitrary coarse binning
can erase a continuous-law witness.

An exact-rational six-spin d=J control at t=2/J and gamma=J/4 rejects the independent-
spin and commuting SzSz approximations at 5% TV for explicitly declared fine bins.
This is not a hard instance or evidence that stronger classical methods fail.
The small model and tolerance are mathematical controls, not an asserted experimental
requirement. Rational moment/Taylor witnesses are separate from floating diagnostics.

The finite geometric-clock law is a positive Fourier polynomial determined by N-1
scalar values C(h tau). Approximate values with errors e_h give a constructive
classical bin sampler: integrate the polynomial, take positive bin parts and
normalize. The proved readout error is at most sqrt(2 sum_h a_h^2 e_h^2), including
the possible negativity repair; clock truncation, unwrapping and arithmetic add.
A second-moment wrap bound avoids resolving every extensive microscopic gap.

For d=J, gamma=J/4, tau=0.1/J and N=256, 255 correlation values within 0.002 give
per-block TV below 0.02834 before arithmetic, independent of block size. This is a
CONDITIONAL accuracy target, not an executed cheap large-block acquisition. Add
Note 21's spatial error for a full-chain result. Per-draw and joint M-draw error
are different. Positivity repair alone does not validate incorrect correlations.

## Strong classical acquisition and remaining uncertainty

Time splitting is established prior work. C(t)=<u(-t/2),u(t/2)>; because this model's
L and o are real, C(2s)=u(s)^T u(s). One forward half-time tensor trajectory suffices;
the contraction is bilinear, not the conserved conjugated norm. A normalized
vector approximation error delta gives scalar error at most 2delta. This is
sufficient only: scalar output may remain accurate with larger operator errors.
Do not use Schmidt rank, a large Pauli list or failed vector truncation as an
all-classical spectral lower bound. Tensor errors, time-step errors and their
certification costs must be charged; discarded squared norms cannot simply be
summed and relabeled as a global amplitude error.

The key unknown is C_acquire(k,N,{e_h}), not the storage size of the final spectrum.
The classical route may reuse its acquired scalars and bin table across M draws.
The direct quantum sampler avoids constructing these classical scalars but repeats
preparation/evolution/readout. Its cost retains the physical linewidth, coefficient
access and all accuracy terms. Neither route's displayed upper bound is optimal.

## Next bounded mathematical task

For the SAME intermediate d/J~1 family, analyze one controlled way to acquire the
weighted scalar returns at the required accuracy as gamma/J varies. Prefer a
translation/symmetry-aware operator recurrence or a half-time tensor contraction
with an actual response-error bound. Derive the required representation size or
identify a response-sensitive obstruction to that representation; do not merely
quote full-vector entanglement growth. Permit direct resolvent, restricted-state,
effective and alternative sampling methods as competitors.

Include preparation once versus repeated samples explicitly. A meaningful result
would identify a parameter regime where the best justified classical contraction
is small, or a specific necessary response component that remains expensive for
it while quantum evolution can retain it. A failed sufficient certificate is not
hardness. All-size claims must not be extrapolated from the six-spin control.
No new generic readout framework, further small-size census, data dependency,
native solver installation, large simulation, or third classical spin-off is the
next step. The local quantum integration remains active, not refuted.

## Evidence and preservation

The new checker ran twice with identical JSON under one BLAS thread. It computes
exact moments through order 80 and rational Taylor enclosures for one six-spin
block and its two surrogates. Separate complex128 checks cover half-time identities,
clock/Fourier reconstruction, deterministic correlation perturbations, negativity
repair and invalid inputs. -O/-OO refusal was checked. No tensor algorithm, quantum
circuit, measured spectrum, native NMR package or performance run was executed.
No previous verifier was rerun and no upstream code/data was imported.

Climate/dynamics remain open; Manthan is paused; battery/operator routes parked;
both independent spin-offs retain their own projects; Phase-2 Note 27 stays closed.
Preserve prior proofs, code, reports, data, licenses and rights. Modify only
Quantum-Assisted-Algorithm-Discovery. No outside contact, paid/unattended work,
manuscript revival, release, branch merge, new repository or administration change.
