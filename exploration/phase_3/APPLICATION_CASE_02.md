# Application case 02: a classical simulator for battery-interface reactions

28 September 2026. Base: `232b060e6ed154a039fc01e0b7b6d30306ec5723`.
Working branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision: select one application for a bounded feasibility comparison, not a
quantum-advantage claim.** The candidate is a reusable classical reactive potential
for initial electrolyte decomposition at a lithium-metal interface. The need is
supported by application research; a quantum contribution is not established.
The operator construction remains parked. No new repository is needed.

## 1. Three application screens

| Workflow and useful output | Evidence outside this project | Quantum-discovery assessment |
|---|---|---|
| Accelerator kernels: faster ordinary training/inference code | AlphaEvolve reports an actual TPU matrix-multiplication tiling improvement, including a 1% reduction in overall Gemini training time [1] | Genuine useful output and a strong classical-AI competitor. Measured hardware latency is not a free coherent predicate. No sufficiently concrete quantum mechanism was identified in this screen. |
| Weather-model radiation: a faster classical radiation component | ECMWF's 2022 ecRad-emulation report describes coupled-model tests, computational gains, and some forecast degradation [2] | Usefulness must include forecast quality. Ordinary supervised training is already a serious comparator; the screen found no distinct quantum obstacle in acquiring its classical training data. |
| Battery-interface chemistry: a classical energy/force evaluator | Reactive molecular-potential research supplies a real target and electronic-reference workflow [3,4] | Electronic many-body calculation gives a physics-specific quantum route. Select a matched-input feasibility test; do not infer advantage from the application label. |

These are screening judgments, not lower bounds or an exhaustive survey. The
first two are not declared unsuitable for all quantum approaches. Their further
investigation is not a parallel active task.

## 2. What would actually be delivered?

The intended users are researchers modeling the initial chemistry of the solid-electrolyte interphase at lithium-metal anodes. The motivation is predictive
interfacial chemistry, not a claim to predict full battery lifetime.

The proposed deliverable is a saved classical model with a declared domain of
atomic configurations, charges, boundary conditions, and compositions. It takes
nuclear positions and species and returns an energy and consistent forces. A
classical trajectory engine can call it repeatedly without quantum access. MACE
already exposes an ASE calculator for this kind of deployment [5]; inventing a
new simulator interface is unnecessary.

This is **learning a reusable classical simulator**, not finding a new symbolic
algorithm or merely computing one reaction energy. It specializes the parent's
reusable-classical-method objective in an explicit way. A finite list of quantum
energies, without a validated evaluator on subsequently encountered geometries,
would not satisfy the proposed deliverable.

A useful result must improve the attainable accuracy/cost tradeoff for declared
reaction observables, against the best classical pipeline. Saving runtime by
changing the chemistry, accepting an unstable force model, or testing only the
training geometries does not qualify. Bulk-cell performance, long-term degradation,
experimental agreement, and transfer to other electrolytes are separate claims.

## 3. Two classical-baseline checks already change the story

Kundu et al. [3] study molecular LiEC and EC on a lithium surface using classical
MACE potentials. Their Table I supplies molecular TST rates and recrossing factors.
Multiplying the reported rounded values gives 10,290,000,000, 78.02, and 153.6 per
second for PBE-D3, omegaB97X-D3, and DLPNO-CCSD(T)-trained models, respectively.
The first-to-third ratio is about 67 million; the third-to-second is about 1.97.

**Inference:** a spectacular difference from PBE is not a quantum advantage when
a stronger classical approximation already tracks the classical correlated result.
These are predicted physical rates, not computational timings, and the molecular
control is not a quantum-hard workload.

More decisively, Vo et al. [4], posted 23 March 2026, already perform correlated
classical calculations for EC on lithium clusters with finite-size corrections.
Their Table II gives a PBE barrier of 5.6 kcal/mol, omegaB97X-V at 17.9, and a
cross-method estimate of 16.3 +/- 0.8. That spread is not a certified true-error
bound. Their full assessment leaves finite-size and electronic approximations.

**Inference:** the actual surface cannot be described as inaccessible to classical
high-level chemistry either. Any proposal must beat or complement this existing
route at matched useful accuracy. A quantum exact energy for a small artificial
fragment is not automatically a more accurate prediction for the interface.

The broader classical comparison also includes methods such as FEMION, which
combines AFQMC with a treatment of nonlocal screening and demonstrates metal-surface
calculations [6]. This is classical electronic-structure computation despite the
word “quantum” in the title. Its success on copper does not establish accuracy for
lithium/EC, but rules out ignoring advanced classical embedding as a category.

## 4. Physical observables before a precision target

The application should distinguish stationary energy differences from dynamical
predictions. In [3], a fast surface pathway lacks a metastable reactant, so a
single transition-state rate is not an appropriate universal observable. Its
finite-temperature branching/first-passage behavior is a separate target from a
static barrier in [4]. We must not interchange the two papers' geometries or
pathways merely because both concern EC on lithium.

For an activated channel with its prefactor held fixed, the Arrhenius/Eyring
exponential gives an illustrative energy sensitivity:

$$
|\Delta\Delta F|\leq R T\log f.
$$

At 300 K a factor-two tolerance corresponds to 0.4132275 kcal/mol; a factor-ten
tolerance corresponds to 1.3727121 kcal/mol. These are our calculated design
illustrations, **not community acceptance criteria or guarantees for the surface
reaction**. Neither formula bounds changes in recrossing, solvent effects,
nonadiabatic physics, or the learned force field. Do not choose an artificially
strict target just to make classical methods fail.

Before promising an application improvement, identify which prediction changes
with higher electronic accuracy, and whether that change exceeds uncertainties
from finite-size treatment, environment, thermal sampling, and model deployment.
A low average energy error alone does not answer that question.

## 5. Plausible quantum role, with the cost included

The proposal is to use a fault-tolerant quantum calculation **offline** for
selected electronic reference values that are expensive at the required accuracy,
then train and deploy the classical evaluator. The model training need not be
quantum. A quantum call at every molecular-dynamics step would be a different
project and would not meet this offline-compilation contract.

This architecture is not new: Schuhmacher et al. [7] explicitly proposed
quantum-generated references for classical machine-learning potentials, with an
H2 demonstration and noise analysis. It establishes a precedent, not evidence of
battery advantage or originality for this project.

Circuit-model electronic simulation and phase estimation have explicit algorithms
[8]. Their input is a specified Hamiltonian/basis plus an implementable starting
state, not a free accurate-energy oracle. Sufficient eigenstate overlap is a real
condition. Charge basis construction, integrals or plane-wave coefficients,
state preparation and its success, precision, measurement, validation, and all
reference geometries. Existing quantum chemistry resource figures from other
molecules must not be assigned to this surface.

Both competitors receive the same geometry and Hamiltonian specification and may
exploit classical chemistry and the same deployment architecture. A comparison
must include all reference generation, training, validation, and repeated use.
The classical side may use a cheaper functional, correlated sampling, local
correlation, embedding, active selection, or a direct observable calculation.
It need not imitate the quantum construction or reproduce unnecessarily exact
labels when approximate labels already deliver the required observable.

This makes the discriminating question specific: **is there an application-relevant
reference-accuracy regime in which quantum preparation improves the complete
classical-simulator construction, after the strongest classical route is allowed?**
The current evidence does not yet answer yes.

## 6. One matched calibration, not a large campaign

The next bounded task is a cost-and-accuracy comparison using a published finite
lithium-cluster instance, not another generic theorem. A neutral Li40+C3H4O3
instance is a proposed calibration because [4] includes 40-lithium correlated
calculations. Under the explicit convention of frozen Li, C, and O 1s cores, this
composition has 50 nuclei, 166 total electrons, and 74 correlated electrons.
That accounting is not an orbital count, an active-space validation, or a quantum
hardness claim. The calibration is deliberately classically accessible.

First obtain and pin the exact published coordinates, charge, spin, basis,
core treatment, and reference method settings. Then establish the orbital count,
classical resource/error evidence, and quantum per-geometry cost with stated
preparation assumptions. Do not create a different geometry and call it a replay.
Only if this comparison exposes a defensible regime should we examine how many
new configurations a useful classical model would need. Reference count is not
free, and one stationary point is not a force-field training set.

The data passages inspected in [3,4] do not supply a downloaded geometry/training
package here: [3] says data/model release will accompany publication; [4] directs
requests to the authors. Public metadata searches did not establish a complete
available package. No contact was made. Search supporting/public deposits before
considering a request; do not treat missing files as evidence of quantum hardness.

Stop or redirect this application if the best classical method already meets
required quality, if environmental/model errors dominate the proposed improvement,
or if complete quantum reference cost erases the advantage. These are decisions
about this workload, not a general rejection of quantum chemistry.

## 7. Reproduction and scope of this checkpoint

```sh
python experiments/application_case_v1/verify.py
```

The standard-library script replays the selected rounded table entries with exact
rational arithmetic, computes the sensitivity examples with ordinary floating-point
logarithms, checks the proposed electron accounting, and rejects six invalid inputs.
It passed twice; refusal under `-O` was checked. It writes no files. Source SHA256:
`b408149c533d43383f1b043fee2a9ce317b4782b6f233ac7c5b4278fccb45d73`.

This is **published-data arithmetic, not a new electronic-structure calculation,
molecular trajectory, force-field training run, quantum simulation, or benchmark**.
No upstream source code, coordinates, or model weights were imported. Root and
historical research verifiers were not rerun. Repository checkout failed on DNS;
GitHub connector reads/writes worked. Earlier research, the license, both spin-offs,
and the other branches are unchanged by this checkpoint.

## Sources and inspection scope

All checked 28 September 2026. This is a focused application screen, not an
exhaustive novelty or literature audit. No source's publication status is used as
proof that its scientific claims are correct.

[1] AlphaEvolve authors, *AlphaEvolve: A coding agent for scientific and algorithmic
discovery*, arXiv:2506.13131v1, Section 3.3.2. Author-reported production comparison;
no independent benchmark here. https://arxiv.org/html/2506.13131v1

[2] M. Chantry et al., *Progress on emulating the radiation scheme with machine
learning*, ECMWF Newsletter 173, Autumn 2022. Historical report, not a 2026
performance claim. https://www.ecmwf.int/en/newsletter/173/news/progress-emulating-radiation-scheme-machine-learning

[3] S. Kundu et al., *Reaction dynamics of lithium-mediated electrolyte decomposition
using machine learning potentials*, arXiv:2509.14067v1. Results, methods, and data
statement inspected; Table I checked visually on PDF page 2.
https://arxiv.org/html/2509.14067v1

[4] E. A. Vo et al., *Adsorption energies and decomposition barrier heights for ethylene
carbonate on the surface of lithium from cluster-based quantum chemistry*,
arXiv:2603.22139v1. Methods/results/conclusion/data statement inspected; Table II
checked visually on PDF page 4. https://arxiv.org/html/2603.22139v1

[5] MACE official ASE-calculator documentation; software interface only, not a claim
that a suitable battery model is supplied. https://mace-docs.readthedocs.io/en/latest/guide/ase.html

[6] C. Cao et al., *Quantum Many-Body Simulations of Catalytic Metal Surfaces*,
arXiv:2508.13036v1. Abstract and method context inspected; not an independent
AFQMC audit or execution. https://arxiv.org/html/2508.13036v1

[7] J. Schuhmacher et al., *Extending the reach of quantum computing for materials
science with machine learning potentials*, AIP Advances 12, 115321 (2022),
arXiv:2203.07219. Primary abstract and publication metadata inspected.
https://arxiv.org/abs/2203.07219

[8] Y. Su et al., *Fault-Tolerant Quantum Simulations of Chemistry in First
Quantization*, PRX Quantum 2, 040332 (2021), arXiv:2105.12767. Circuit/resource
framework and state-preparation qualifications inspected, including PDF page 53.
Not a current best-algorithm claim or a resource estimate for lithium/EC.
https://arxiv.org/abs/2105.12767
