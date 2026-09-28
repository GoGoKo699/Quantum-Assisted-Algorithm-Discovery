# Current task: spatially local response versus full-chain spectral sampling

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read [smooth response 20](../exploration/phase_3/SMOOTH_RESPONSE_COMPRESSION_20.md),
[model comparison 15](../exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md), and
[spectral boundary 16](../exploration/phase_3/SPECTRAL_BOUNDARY_16.md).
Direct samples and model-first analysis remain authorized. No dataset, molecule,
native installation, learned classical program or quantum-free deployment is an
entry condition. Usefulness and honest complete costs remain required.

## Completed cutoff calculation; do not extend generic filtering indefinitely

A bounded odd polynomial of the FULL Liouvillian gives K=2 kappa P(L/alpha).
It keeps the original spectral probabilities and approximately preserves frequencies
inside |omega|<=kappa, without a sharp projector, a smallest-spacing promise or
a cutoff-edge margin. If the core frequency error is delta, the broadened-law TV
error is at most min(1, ||Lo||^2/kappa^2+delta/(pi gamma)).
For the existing alternating-offset collective response, ||Lo||^2=d^2 exactly.

This is generator transformation, not applying the polynomial to the state and
postselecting. The latter reweights the law and can remove its dominant line.
It is also not Note 19's Schur formula with a smooth function substituted for P,
nor a promise that the retained Hilbert space is smaller. State/filter errors
and the same linewidth and digital bins must be retained.

Standard amplitude multiplication implements the bounded polynomial, but each
compressed-block call costs order alpha/kappa original-block calls up to logs.
Combining it with a linewidth-matched sampler gives the sufficient budget
~(alpha/kappa)(1+kappa/gamma), retaining the alpha/gamma leading term of the direct
route. The absence of a generic simulation gain is prior work, explicitly attributed.
This calculation removes an access artifact, not the physical time/accuracy cost.
No quantum-classical separation or practical advantage has been established.

A standalone generic uniform eigenvalue transform has an oracle-hybrid lower
bound proportional to alpha/kappa. That is not an all-algorithm lower bound for
our explicitly supplied spin model or for state-specific spectral sampling.
Endpoint/sum-of-squares and specially structured encodings are different regimes.
The global-gap reduction, resonance-window proof and direct sampler remain intact
with their own assumptions. Do not infer that all smooth reductions fail.

## Next bounded model-level question

Return to physical locality of the same even nearest-neighbor, alternating-offset
chain and collective raising response. Determine whether the linewidth-resolved
spectral law can be approximated by a positive mixture of overlapping finite
spatial windows, with an error independent of the total length once the chain is
large enough. The requested gamma, bins and accuracy must remain fixed.

Construct the candidate observable/window law before bounding it. Include the
collective cross correlations; an average of isolated one-spin spectra is wrong
even in Note 16's exact two-spin control. If a correlation approximation is not a
positive measure, it is not automatically a directly usable sampler. Account for
physical boundary conditions and for any error introduced by cutting interactions.

Use a locality/finite-time argument or another justified structural reduction,
then translate it to the SAME broadened full-law or specified-bin tolerance.
Do not assume that short evolution, high temperature or an extensive observable
automatically gives a system-size-independent error. Retain dependence on J, d,
gamma, epsilon, block size and graph geometry.

If a suitable finite-window law is valid, compare classical construction/sampling
of its block response with direct local quantum spectral sampling. Price state
preparation, coefficient access, time evolution, repeated draws, block selection
and any approximation needed to treat the whole chain. Tensor-network,
restricted-operator and direct-correlation methods remain competitors; exponential
dense-state cost is not their lower bound. Classical preprocessing can be amortized.

This is one discriminating mathematical derivation, not a new simulator or a large
toy census. No locality-based TV guarantee for this collective construction exists
in Note 20. A failure for the chosen windows should inform the model comparison,
not become a universal rejection of direct quantum sampling.

## Executed evidence and preservation

The new NumPy checker ran twice with identical JSON and exit code zero. -O/-OO
refusals were verified. Three fixed n=2,4,6 chains test six moment identities,
six smooth-cap comparisons and three bounded cubic-polynomial comparisons, with
eight edge-continuity, four translation and six invalid-input controls. A state-
filtering negative control is retained. These are complex128 diagnostics at
tolerance 3e-10, not interval certificates, general polynomial synthesis, quantum
circuits, measured spectra or timings. The continuous bound follows from the proof.

The note records the unrelated Python startup warning and source-inspection scope.
No older verifier was rerun; prior files remain unchanged. No source code or
experimental data was imported. Direct spectral algorithms, polynomial amplitude
multiplication and the oracle-hybrid argument are prior work.

Climate/dynamics remain open; Manthan is paused, battery/operator routes parked,
both spin-offs independent and Phase-2 Note 27 closed. Preserve all earlier notes,
proofs, data, code, reports, licenses and rights. Modify only Quantum-Assisted-
Algorithm-Discovery. No outside contact, paid/unattended work, manuscript revival,
release, merge, new repository or administration change is authorized.
