# Current task: mathematical models first, quantum integration second, implementation later

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

The owner requests greater emphasis on the mathematical models of every example
before actual implementation. The model-first section of [AGENTS.md](../AGENTS.md)
governs this ordering. Retain the [direct-sample scope](../exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
and the mechanism distinctions in [screen 14](../exploration/phase_3/OPEN_SAMPLING_SCREEN_14.md).
Samples themselves remain permitted outputs; quantum-free deployment is not required.

## Immediate deliverable: a structural comparison, not a software/data task

Prepare compact mathematical analyses of the two open mechanism families below,
then select the most informative derivation. Do not make a particular molecule,
a downloaded experimental trace, a native installation, or climate-array transfer
a prerequisite to this initial analysis. Keep one bounded calculation active;
this is not a mandate for parallel implementation projects or a new framework.

For each family state:

1. The physically motivated model and parameter regime, with a concise primary-
   source application anchor. State the approximations; do not invent an obscure
   instance just to make the mathematics quantum-friendly.
2. Shared input/access, the exact desired probability law or observable, and its
   useful resolution/error criterion. Samples, scalar expectations, normalized
   spectra, absolute intensities and conditional path laws are different outputs.
3. The explicit quantum representation and operation, and why measurement gives
   the requested result. A formal linearization or large Hilbert space is not
   itself an efficient algorithm.
4. Symbolic cost/error dependence and the strongest relevant classical approach
   for the same output. Keep preparation, normalization, success probabilities,
   resolution, evolution time and output size visible. Conditional budgets are
   allowed; a best-known classical cost is not a lower bound.
5. One structural test: a solvable limiting case, a reduction, a resolution/error
   bound, or a parameter regime that exposes a possible separation or shortcut.
   Identify what remains a conjecture instead of prematurely declaring success
   or rejecting the entire mechanism.

This initial deliverable should reveal where quantum computation might enter and
what mathematical obstacle it must overcome. It need not establish novelty, a
complete advantage proof or deployment before the exploration can proceed.

## Open family A: direct many-body spectral sampling

Start with an established nuclear-spin Hamiltonian family, a justified initial
state/temperature regime, an observable and finite spectral resolution. Use the
normalized autocorrelation measure and doubled-register energy-gap construction
in Note 14 as prior ingredients, not a new algorithm. Seek structural dependence
on interaction topology, coupling structure, observable support and resolution,
rather than increasing spin count in a named molecule.

The question is whether the required response is costly for applicable restricted-
state, tensor-network or direct spectral methods while its quantum preparation
and evolution remain tractable. Correlation growth is a diagnostic, not a proof
that every classical algorithm fails. Coarse resolution may remove the difficult
information. Signed pulse signals are not probability distributions by definition.
A finite-resolution sampling bound must identify its actual broadening kernel;
it cannot silently replace the measurement response. State unknown assumptions.

An experimentally parametrized instance and a native solver comparison come after
this model-level screen identifies a credible regime. Initial relevance requires
a real scientific observable and community model, not a full new validation study.

## Open family B: probability evolution and conditional trajectories

Distinguish direct evolution of a classical probability law from conditioning a
classically computed trajectory. Specify dynamics, initial uncertainty and the
requested state/path law. Examine the Liouville/Koopman-von Neumann representation
from Note 10 at the model level, including boundary, discretization, positivity
and amplitude-to-probability semantics. Its linearity alone does not beat direct
classical trajectory sampling. Coherent rejection is another mechanism, not the
only permitted integration.

The CESM consumer and Notes 11-13 remain valid application/comparator records.
Their segment weights, finite-population limitations and checkpoint-access costs
are not erased. The missing six-file packet gates only the sibling-array test;
analytical exploration need not wait for it. Do not infer empirical continuation
variance, cheap envelopes or a climate advantage without that evidence.

## Implementation threshold and preserved boundaries

Advance to detailed data acquisition, native code, circuit compilation or hardware
budgets only when a structural argument makes them discriminating. Deferring such
engineering does not license free arbitrary state preparation, free database
access or ignored conditioning/precision factors. A modest independent computation
is appropriate when it resolves a mathematical question; another toy census is not.

This checkpoint changes research priorities/documentation only. Prior spectral-
sampling and Koopman-von Neumann sources were rechecked at abstract level. No new
theorem, model-level separation, numerical experiment, native package, quantum
circuit, performance result or scientific-verifier run is claimed. No new data
was acquired. Earlier notes, code, reports and scientific conclusions remain intact.

Manthan stays paused; battery/operator candidates remain parked; both classical
spin-offs own their separate development; Phase-2 Note 27 stays closed. Preserve
licenses and third-party rights. Modify only Quantum-Assisted-Algorithm-Discovery.
No external contact, paid/unattended work, manuscript revival, submission, release,
branch merge, new repository or administration change is authorized.
