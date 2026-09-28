# Current task: useful quantum sampling that leaves a classical method

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md), and the
[useful-sampling opening note](../exploration/phase_3/USEFUL_SAMPLING_07.md).

## Direction authorized: sampling as discovery information

Explore whether a bounded quantum sampling stage can reveal useful structure
that a classical computer retains as an efficient sampling rule, proposal, or
update mechanism. The first hypothesis is learning useful collective moves or
coverage of poorly visited regions, not cloning an arbitrary hard distribution.
No application, new algorithm, or advantage is yet established.

Distinguish direct useful quantum sampling from offline discovery followed by
classical-only deployment. Both are legitimate scientific questions, but the
second preserves the parent's current contract. Do not silently replace it with
a device needed at every subsequent sampling step.

Difficulty of reproducing a full Born distribution does not establish difficulty
of obtaining its useful consequences. A classical competitor may use a different
distribution or bypass sampling. Randomness, compact output and reuse alone do
not establish a quantum advantage. Circuit preparation, parameters, depth, noise,
measurement and access costs remain explicit.

## Direct precedents and constraints

Layden et al., Nature 619, 282 (2023), use quantum proposals during MCMC.
Nakano, Okada and Fujii, PRX Quantum 7, 010338 (2026), already train a classical
neural proposal on QAOA samples. Classical self-learning Monte Carlo and the
annealer-to-generative-model literature also precede this project. Do not claim
that this generic architecture is new, or that a spectral-gap improvement over
uniform proposals proves a useful end-to-end advantage.

For a classical Metropolis-Hastings deployment, generate proposals and evaluate
acceptance ratios using the same learned classical law. Establish support,
irreducibility and aperiodicity. Correct stationarity is not rapid mixing or
finite-run correctness; a biased quantum training set is not automatically an
unbiased target sample set. A first comparison should freeze the learned rule;
online adaptation needs its own argument.

The quantum circuit need not supply a full wavefunction or accurately estimated
probabilities if the proposed classical extraction genuinely avoids those tasks.
Do not assume cheap arbitrary state preparation, free postselection, or a general
ability to learn every hard quantum distribution with a small classical model.

## Next bounded deliverable

Select at most one real sampling workflow together with a concrete circuit/sample
mechanism. Specify its consumer, input specification shared by both designers,
useful output quality, deployment interface, and strongest classical alternative.
A random Ising or SAT instance may be a diagnostic, not evidence of deployment
value. Do not choose a domain first and start broad modeling before this match.

The first discriminating comparison is a sample-source substitution test: hold
the classical learner and deployment task fixed and replace quantum-produced data
with strong classical data and a task-equivalent classical surrogate. Count data
production, tuning, training, validation and deployment, not just equal numbers
of shots or training examples. Permit tempering, appropriate cluster updates,
learned classical proposals, source inspection and direct downstream algorithms.
A competitor need not reproduce the quantum distribution to defeat the proposed
useful advantage.

Measure consumer-relevant error, coverage or validated mixing performance with
honest finite-time uncertainty. High acceptance, low energy, or raw sample count
alone is insufficient. Reuse is available to both sides. The first output should
be one compact task/distribution/compiler/comparator contract and a short
calculation that can reject it, not a new neural framework or large benchmark.

## Parked work and evidence

The [battery decision](../exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md)
remains binding. The battery and small-operator candidates are parked; the two
classical spin-offs remain independent. The uploaded battery archive is already
verified: do not request it again or make archive curation a new workstream.
Phase-2 Note 27's comparison remains closed. Older Fourier/coordinate notes are
historical constraints, not automatically reopened by the sampling perspective.

This opening checkpoint is a primary-source screen and research-direction update.
No sampling experiment, quantum circuit, model training, performance measurement,
new scientific code or scientific-verifier run was performed. The short note
records source-inspection limits; it is not an exhaustive novelty audit.
Preserve earlier proofs, code, reports, manifests, licenses and third-party rights.
Modify only Quantum-Assisted-Algorithm-Discovery. No external contact, paid or
unattended work, manuscript revival, submission, release, branch merge or
repository administration change is authorized.
