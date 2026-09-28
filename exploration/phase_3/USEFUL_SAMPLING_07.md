# Useful sampling 07: quantum samples as discovery information

28 September 2026. Starting branch head:
`d0a65c4c0c56cbce9fc8838f73bc38f19db0231f`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision:** explore useful quantum sampling as the next mechanism family. The
first question is whether quantum-generated samples can help construct a useful
classical sampling rule or proposal, with the quantum computer absent at deployment.
This is an opening hypothesis and source screen, not a selected application,
novel architecture, algorithmic theorem, or quantum-advantage claim. The battery
and small-operator routes remain parked. The parent objective is unchanged.

## 1. What the sampling perspective changes

A measured circuit produces an outcome from its Born distribution. The opportunity
is not randomness itself, but the cost of producing task-relevant structure in
that distribution. Sampling is an interface to the computation; it does not make
preparation, interference, circuit depth, or measurement cost disappear.

Distinguish three questions:

1. Is the full circuit distribution difficult to reproduce classically under the
   stated approximation and access assumptions?
2. Do its samples provide information useful for a independently specified task?
3. Is the complete route to that useful output better than the strongest adequate
   classical route, including a different distribution or bypass?

No implication from the first question to the other two is assumed. As a logical
example, attach a hard-to-sample unused register to an ordinary coin. A consumer
that uses only the coin gains nothing from the unused sampling hardness. This is
an illustration, not a new lower bound.

A relevant warning is the GBS dense-subgraph study [4]: the useful heuristic
behavior in its investigated regime survives into classically simulable regimes.
This does not settle every GBS application or exclude every polynomial benefit;
it does show why the useful output, not circuit imitation, is the comparison.

The statement that sampling demonstrations have no useful consequences is also
too broad. Certified randomness [5] uses random-circuit challenges for an untrusted
server. The reported demonstration certifies entropy against a restricted
adversary under additional assumptions and uses substantial classical verification.
It is a genuine use of sampling hardness, not evidence for our reusable-method
objective or an unrestricted cryptographic/economic advantage.

## 2. Two different research contracts

**Direct useful sampling:** a quantum device supplies fresh samples whenever a
consumer needs them. This can be a valid application, but continued dependence on
the quantum sampler is not the parent's classical-only deployment contract.

**Sampling-assisted discovery:** a bounded quantum sampling stage supplies data
from which a classical learner constructs a reusable rule, proposal distribution,
or update mechanism. After construction, the actual application runs classically.
This is the preferred first screen because it retains the existing objective.
A retained list of samples alone is not automatically a reusable algorithm.

The working hypothesis is:

> Can quantum samples reveal useful collective changes or poorly visited regions
> that allow an ordinary sampling algorithm to make better progress afterward?

For example, learn a proposal that changes several coupled variables together,
rather than copying a complete hard Born distribution. This describes the desired
information flow, not a promise that quantum dynamics finds the relevant changes
or that a small classical representation exists.

A classical deployment rule does not contradict quantum discovery advantage:
executing a supplied rule and discovering that rule from the original input are
different tasks. Conversely, no general ability to compress an arbitrary quantum
sampling distribution into an efficient classical generator is assumed.

## 3. Close precedents already exist

| Source | What is already established by the inspected material | What it does not establish for this project |
|---|---|---|
| Layden et al. [1] | Quantum circuit proposals with classical accept/reject steps for Ising Boltzmann sampling; reported improvements in iteration counts on studied instances | Quantum-free deployment, superiority to every strong classical alternative, or a new useful workload for us |
| Nakano, Okada and Fujii [2] | QAOA samples train a generative neural proposal; subsequent MCMC uses the classical surrogate | Novelty of the quantum-samples-to-classical-sampler architecture or a complete application advantage from a uniform-proposal comparison |
| Liu et al. [3] | Classical self-learning Monte Carlo learns efficient updates from trial-simulation data | Any necessity for a quantum teacher |

The publisher confirms [2] as PRX Quantum 7, 010338, published 24 February 2026.
Its published abstract reports spectral-gap scaling relative to uniform proposals;
the preprint/summary also reports roughly two orders of magnitude relative to
simple baselines. Neither quantity is a total wall-clock advantage after training
and quantum sample production. Do not interchange the published and preprint
wording or turn a comparison with uniform proposals into a best-classical claim.

Scriva et al. [6] provide an earlier annealer-to-generative-model precedent. That
is a different hardware/access model; it is not permission to silently replace
the parent's circuit-model setting. These sources establish that the proposed
information flow is concrete, not that adopting it is a contribution.

For direct QeMCMC, Orfi and Sels [7] give a no-speedup result on a particular
unstructured worst-case problem. It is not a ban on structured useful instances,
but quantum proposals alone cannot be presumed to improve mixing.

## 4. Correctness must be separated from fast convergence

A tractable classical proposal can be combined with a Metropolis-Hastings rule
using the target weight ratio and the proposal's own forward/reverse probabilities
[2,3]. Use the same classical proposal both to generate candidates and to compute
those ratios. An estimate of an intractable quantum proposal probability cannot
silently stand in for its exact acceptance ratio.

With the needed support, irreducibility and aperiodicity conditions, this can
preserve the target stationary law even if the training samples are biased or
the learned proposal differs from the quantum teacher. It does not make finite
runs exact, ensure the learner covers all relevant regions, or prove rapid mixing.
Freeze the learned proposal for a first deployment test; continuous adaptation
requires its own correctness argument. Any fallback ensuring support counts in
the cost and may still mix slowly.

This distinction suggests looking for quantum samples that are informative for
proposal construction, not automatically demanding unbiased target samples or
full state tomography. Whether such samples are cheaper or more useful than
classical data is precisely the unresolved research question.

## 5. The first decisive comparison: replace the sample source

Before a new neural architecture, large simulation, or random-spin benchmark,
select one real sampling workflow with an identified consumer, specified target
or task score, correctness/tolerance requirement, and existing classical solver.
Candidate selection must couple this need to a concrete circuit-generated sample
mechanism. Random Ising instances may calibrate a mechanism, but do not substitute
for that application case. No application is selected in this note.

Then compare a fixed classical learner/deployment interface supplied with:

- quantum-generated training samples;
- samples from strong applicable classical producers;
- a task-equivalent classical surrogate that need not reproduce the quantum law.

The last comparison is essential. Similar downstream success can defeat the
proposed advantage even when the surrogate is far from the quantum distribution
in total variation. Where pertinent, include the classical randomized-rounding
route in [8]; that study concerns specified noisy, two-body-objective settings,
not all sampling tasks, and the cost of obtaining its needed marginals also counts.

Count input encoding, preparation, circuit parameter selection, accepted and
rejected shots, correlations, learning, validation, proposal evaluation and
subsequent use. Equal sample counts are an ablation, not equal computational
budgets. Permit parallel tempering, appropriate cluster updates, learned classical
proposals, source structure, and direct downstream computation. Reuse is available
to both sides and cannot erase a larger setup cost by itself.

Judge the resulting method on the consumer's required quality: validated estimator
error or an appropriate sampling/coverage guarantee, with honest finite-time
uncertainty. Energy alone, acceptance rate alone, raw shot count, or a spectral-gap
improvement over one weak proposal is insufficient. Check unqueried states or
held-out conditions as appropriate; replaying the training sample pool is not the
deployment test.

The desired first deliverable is one compact task/distribution/compiler/comparator
contract and its most discriminating calculation. The possible contribution is
in a demonstrated useful regime or mechanism, not the generic architecture.

## 6. Source and execution scope

This checkpoint inspected primary abstracts/publisher metadata and selected HTML
method sections. It is not an exhaustive priority audit. No PDF figure or table
was used to infer results; no PDF analysis, experiment, circuit simulation,
training, benchmark or scientific-verifier run was performed. No upstream code
or data was imported. All earlier scientific files and both spin-offs are unchanged.
Only this note and current exploration routing are changed.

Sources checked 28 September 2026:

[1] D. Layden et al., *Quantum-enhanced Markov chain Monte Carlo*, Nature 619,
282-287 (2023). Primary abstract inspected; publisher full-text access failed.
https://arxiv.org/abs/2203.12497
https://doi.org/10.1038/s41586-023-06095-4

[2] Y. Nakano, K. N. Okada and K. Fujii, *Neural-Network-Assisted Monte Carlo
Sampling Trained by Quantum Approximate Optimization Algorithm*, PRX Quantum 7,
010338 (2026). Publisher abstract/date and preprint HTML methods inspected.
This is not a full independent audit of its experiments or proofs.
https://doi.org/10.1103/9nhx-5pym
https://arxiv.org/html/2506.01335v1

[3] J. Liu, Y. Qi, Z. Y. Meng and L. Fu, *Self-Learning Monte Carlo Method*,
Physical Review B 95, 041101 (2017). Primary abstract and HTML text inspected.
https://doi.org/10.1103/PhysRevB.95.041101
https://arxiv.org/html/1610.03137v2

[4] N. R. Solomons, O. F. Thomas and D. P. S. McCutcheon,
*Gaussian-boson-sampling-enhanced dense subgraph finding shows limited advantage
over efficient classical algorithms*, arXiv:2301.13217. Abstract-level scope only.
https://arxiv.org/abs/2301.13217

[5] M. Liu et al., *Certified randomness using a trapped-ion quantum processor*,
Nature 640, 343-348 (2025). Primary abstract inspected; restricted-adversary and
verification-cost qualifications retained. Not an independent security audit.
https://arxiv.org/abs/2503.20498
https://doi.org/10.1038/s41586-025-08737-1

[6] G. Scriva, E. Costa, B. McNaughton and S. Pilati, *Accelerating equilibrium
spin-glass simulations using quantum annealers via generative deep learning*,
SciPost Physics 15, 018 (2023). Publisher record inspected.
https://scipost.org/10.21468/SciPostPhys.15.1.018

[7] A. Orfi and D. Sels, *Bounding speedup of quantum-enhanced Markov chain Monte
Carlo*, arXiv:2403.03087; Physical Review A 110, 052414 (2024). Primary abstract
inspected; scope is its unstructured worst-case construction, not every instance.
https://arxiv.org/abs/2403.03087

[8] V. Martinez, O. Fawzi and D. Stilck Franca, *Sampling (noisy) quantum circuits
through randomized rounding*, Quantum 10, 2068 (2026); arXiv:2507.21883v3.
Primary abstract inspected, not its full proof or marginal-acquisition complexity.
https://arxiv.org/abs/2507.21883
