# Current task: observable-scale classical compression versus linewidth-matched quantum sampling

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read [model comparison 15](../exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md),
[AGENTS.md](../AGENTS.md), and the [direct-sampling scope](../exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md).
Mathematical models and their quantum integration come before implementation.
Direct samples remain allowed; a learned classical program is not required.

## Completed model-level comparison

The classical-dynamics route retains its Koopman-von Neumann representation, but
must beat direct trajectory sampling, not an explicit probability grid. The
spectral family now has a concrete finite-resolution quantum construction and
several strong analytic classical reductions. It is selected for the next bounded
derivation without closing climate or nonlinear-distribution exploration.

The model is homonuclear spin-1/2 isotropic exchange with inhomogeneous centered
axial offsets, collective raising observable O=sum S_i^+, and the normalized
high-temperature correlation spectrum convolved with a Lorentzian of width gamma.
The output is specified frequency-bin labels at total-variation tolerance epsilon,
not absolute intensity, an arbitrary pulse signal, or exact microscopic lines.
Input spin parameters are supplied; deriving them from chemistry is another task.

An observable-state preparation and a product-state geometric clock give the
required wrapped Lorentzian law through controlled doubled-register evolution
and a dithered Fourier measurement. Explicit truncation, wrap and finite-offset
bounds yield total controlled evolution time O(log(1/epsilon)/gamma). This is
not a compiled gate count, practical runtime, optimality result or quantum speedup.
Coefficient access, state/clock preparation, numerical precision, repetitions and
inference costs count. Spectral sampling and windowed phase estimation are prior
work; priority for this precise composition has not been assessed exhaustively.

## Structural classical responses that must remain in the comparison

The commuting SzSz model has an exact local classical frequency sampler. Uniform
centered fields make the collective spectrum a single line for any isotropic
coupling graph. A coarse-line approximation is certified when the offset variance
is small relative to gamma squared. These are observable-specific statements,
not claims that the full many-body state is simple.

Deleting isotropic bonds of total absolute strength J_cut changes the broadened
spectrum in TV by at most J_cut/(2 gamma). A supplied partition into small components
therefore permits an explicit classical mixture sampler when this tolerance is
adequate. Partition construction counts. The certificate is sufficient and
conservative; its failure is not evidence that the spectrum is classically hard.
The two-spin solution also shows that a weak-coupling approximation must be checked
against linewidth, not just the field-to-coupling ratio.

## Next bounded mathematical derivation

Select one physically motivated bounded-degree inhomogeneous coupling family and
analyze the size of the observable representation actually needed at the requested
linewidth. Compare a suitable restricted-operator, cluster, Krylov or tensor-network
approximation with the explicit quantum construction. Work at the same output-law
or declared-bin tolerance, rather than requiring classical recovery of the full
many-body state or every exact transition.

A useful first result is an error bound relating truncation of the evolving
observable/correlation function to the broadened spectral output, on the time
scale O(log(1/epsilon)/gamma). State how the required classical representation
scales with degree, interaction strengths, offset inhomogeneity, time and error.
The collective observable requires its own spatial/correlation accounting; a
single-site locality bound must not be copied without checking cross terms.

Identify a regime where a certified classical reduction suffices, or a specific
remaining structural obstacle that the quantum representation can address.
A large connected graph, fourth moment or operator entanglement is not a lower
bound against all classical algorithms. Keep direct inference, known libraries
and classical sampling of a task-equivalent distribution available where relevant.
No positive separation is required in advance, and no universal rejection follows
from one easy limit. The goal is to expose a possible useful mechanism, not to
turn the new bounds into another classical spin-off.

Do not make a particular molecule, spectrum download, native package or hardware
estimate a prerequisite. No simulator, full circuit compiler, large toy census
or new experiment campaign is the next task. Detailed implementation becomes
appropriate only when it resolves an identified model-level uncertainty.

## Evidence and preserved work

`python experiments/spectral_structure_v1/verify.py` requires NumPy and Python
3.10+. The checker ran twice with identical JSON; -O/-OO refusals were checked.
It uses five fixed systems of at most four spins, one disconnected-mixture and
complex-transpose control, two-spin formulas, three clock kernels and scalar tail
bounds. These are double-precision mathematical diagnostics, not experimental
spectra, compiled quantum circuits or timings. Continuous claims follow from the
written proofs rather than finite numerical bins. No older verifier was rerun.

No experimental or climate data, model weights or upstream source were imported.
The climate sibling test remains as specified in Note 13; its missing packet blocks
that empirical test only. Manthan remains paused, battery/operator routes parked,
both classical spin-offs independent, and Phase-2 Note 27 closed. Preserve earlier
proofs, code, data, reports, manifests, licenses and third-party rights.
Only Quantum-Assisted-Algorithm-Discovery may be modified. No external contact,
paid/unattended work, manuscript revival, release, merge, new repository or admin change.
