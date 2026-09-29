# Fresh exploration 01: computation, simulation, and information acquisition

29 September 2026. Baseline: `f2c82701cddf7e1c813638b342d278bfd8eb7fcb`.
Working branch: `research/prx-quantum-phase2`; the name is retained for continuity.

**Decision:** open phase 4 with a three-way model/mechanism comparison, not another
extension of the closed activity-covariance study. Quantum-assisted physical signal
acquisition is the most distinct hypothesis to examine next, but it is explicitly
a DIFFERENT INPUT MODEL, not an established answer to the original classical-input
circuit-computation objective. Graph sparsification remains the closest in-scope
alternative; electronic stopping is a physics-simulation reserve. No new quantum
advantage, algorithmic novelty, or implementation result is claimed. No new
repository, manuscript, experiment, or hardware commitment is made.

## 1. Do not rank benefits obtained from different inputs as if they were the same

Three possible comparisons are:

| Candidate | Input both competitors receive | Useful output | Potential quantum change |
|---|---|---|---|
| Graph sparsification | The same weighted graph, with the input representation and lookup cost specified | A small classical graph preserving relevant quadratic forms | Reduce acquisition of the sparse representation |
| Electronic stopping | The same physical Hamiltonian, initial-state prescription and numerical accuracy | Energy transferred from a projectile to matter | Direct correlated quantum dynamics |
| Physical signal learning | Access to the same unknown field/source, not its distribution as a file | A calibrated measurement record or task-specific estimate | Retain more information before measurement |

The third comparison is proposed for a bounded scope/utility audit. It does not
silently amend AGENTS.md or the original circuit-model charter. An optical sensing
improvement alone would not be a demonstrated discovery algorithm on supplied
classical data. Conversely, cheap classical processing of a record need not imply
that acquiring that record from an unknown physical source is cheap. This is a
logical distinction, not a claimed separation.

The next check may conclude that the sensing branch is outside the intended
parent contribution or already adequately covered by existing metrology. In that
case use the in-scope shortlist; do not keep a domain label merely to claim impact.
The phase-3 closeout and handover remain preserved historical decisions.

## 2. A reusable classical graph is a real, already-established precedent

For a weighted graph with Laplacian L, a spectral sparsifier has Laplacian Ls with

$$
(1-\epsilon)x^TLx\leq x^TL_sx\leq(1+\epsilon)x^TLx
\quad\text{for all }x.
$$

This preserves graph energies and supports repeated cut and Laplacian calculations.
Apers and de Wolf [1] already give a quantum algorithm returning a classical
sparsifier with approximately n/epsilon^2 edges in time
\(\widetilde O(\sqrt{mn}/\epsilon)\) in their access model. This is prior work,
not a new proposal here. The guarantee illustrates the original parent's desired
information flow without requiring a quantum computer during later use.

The cost premise matters: coherent adjacency-list access, elementary operations,
and quantum-read/classical-write RAM operations are counted. The stated memory
contains \(\widetilde O(\sqrt{mn}/\epsilon)\) classical bits accessible coherently;
the logarithmic number of active qubits is not the total hardware resource.
Loading an arbitrary edge list once cannot be omitted from an end-to-end comparison.

An implicit kernel graph can avoid explicit quadratic input storage, but also
changes the classical baseline. Bakshi et al. [2] obtain subquadratic graph and
linear-algebra primitives through kernel-density estimation. Their bounds depend
on kernel/data assumptions, dimension, precision and a lower weight parameter;
they are not a universal solution or a license to assume every dense kernel costs
n^2 to process.

**Discriminating test before adoption:** choose one useful input family where edge
queries can be implemented without materializing the whole graph, price coherent
working-memory access, and compare against the appropriate geometric/kernel method.
The known theorem is encouraging, but reimplementing it would not supply novelty.
This candidate remains in-scope and available; no graph instance is declared hard.

## 3. Energy deposition: important physics, a nontrivial initial-state obligation

Stopping power describes the loss of a charged projectile's kinetic energy with
travel distance. A proposed quantum calculation evolves electrons and projectile
from an explicit initial state and estimates the energy-transfer observable.
Rubin et al. [3] already develop such a first-quantized quantum approach. The
nonequilibrium response, rather than an arbitrary microscopic transition list,
is the consumer-facing quantity.

A material limitation in that construction is visible before any gate-count work:
the electronic initial ensemble is assumed well represented by finite-temperature
mean-field orbitals, rather than supplied as the exact interacting Gibbs state.
The proposed simulation subsequently treats correlated dynamics. We must test
whether this initial approximation suffices for the selected observable and
regime, not attach an exact-thermal-state interpretation to it.

Classical real-time density-functional and orbital-free methods are genuine
comparators [4]. Neither an important application nor a large many-electron state
proves that the useful observable requires a quantum computation. The first
possible task is an observable-specific initial-state/classical-error comparison,
not a new resource-estimation or material-screening campaign. This remains a reserve;
no particular medium, projectile parameter, device or experimental claim is selected.

## 4. A different opportunity: quantum processing before the data become classical

Independent experimental work supplies a concrete consumer. Quantum-dense
metrology has been used in proof-of-principle interferometry to distinguish a
phase signal from parasitic scattered light [5]. A subsequent experiment used
the additional measurement information to reduce classical contamination without
discarding measurement segments [6]. These are not our results, not deployment
claims, and not evidence that an arbitrary unknown signal distribution is difficult.
They establish that simultaneous amplitude/phase information can answer a real
noise-rejection question independently of quantum-supremacy demonstrations.

Cotler, Danielson and Kannan [7] formulate a related distribution-learning problem:
a classical field couples linearly to bosonic quadratures, producing an unknown
random-displacement channel. Entangling sensing modes with retained reference
modes and performing a Bell measurement gives a jointly informative classical
record with reduced ideal measurement noise. Their protocol uses squeezing,
passive optics and homodyne detection. It is existing quantum sensing/learning
work, not a new general-purpose quantum-computer algorithm from this project.

A schematic source model is

$$
\mathcal E_P(\rho)=\int P(dx)D(x)\rho D(x)^\dagger.
$$

P is unknown and not freely sampled classically. Both strategies have the same
source uses, physical coupling, bandwidth and prior information. A calibrated
joint readout can be represented as

$$
Y=X+\xi,\qquad X\sim P,\quad\xi\sim\mathcal N(0,\nu I),\quad \xi\perp X.
$$

Here nu is variance per real, standardized coordinate. It is not assigned a
universal hardware value or compared across inconsistent quadrature conventions.
The optical protocol supplies one ideal realization; loss, phase drift and
technical noise can change this channel and must be estimated or bounded.
For canonical quadratures with [x,p]=i, the two-mode observables
\(x_s-x_r\) and \(p_s+p_r\) commute. Joint readout therefore does not measure
both conjugate quadratures of a single system sharply in violation of uncertainty.

**Proposed useful question:** when separating a phase signal from unknown
amplitude/phase contamination, or reusing a record for genuinely multiple
signal-quality diagnostics, does a lower-noise joint record reduce the complete
acquisition cost at fixed useful decision quality? A new source-specific model
and decision threshold are not yet selected. The existing experiments motivate
this question but do not answer our resource-matched comparison.

## 5. An elementary calculation shows where information can be lost

For the calibrated Gaussian readout and any vector k, write
\(\phi_X(k)=\mathbb E e^{ik^TX}\). Independence gives

$$
\mathbb E e^{ik^TY}=e^{-\nu\|k\|^2/2}\phi_X(k).
$$

Consequently the deconvolved estimator
\(Z_k=e^{\nu\|k\|^2/2}e^{ik^TY}\) is unbiased, and for R independent records,

$$
\mathbb E|\bar Z_k-\phi_X(k)|^2
=\frac{e^{\nu\|k\|^2}-|\phi_X(k)|^2}{R}.
$$

This follows from |exp(ik^TY)|=1 and independence; it is standard noise inversion,
not a new theorem or a lower bound against every classical estimator. Decreasing
measurement noise can reduce the statistical penalty of retrieving a feature.
It does not automatically supply a useful exponential advantage: the chosen
frequency k must correspond to a needed feature, and a prior or a different
measurement may estimate the same output more cheaply.

This is also NOT the claim that quantum-generated samples from a fixed identical
law evade ordinary Monte Carlo uncertainty. The measured laws differ because the
acquisition operations differ. If the original P is instead given by a tractable
classical generative model, it can be sampled directly; this physical-access
argument is no longer the relevant comparison.

Calibration can limit the benefit. If the variance used in the inversion differs
from the true variance by delta_nu, the estimated mean is multiplied by
exp(delta_nu ||k||^2/2). Treating an arbitrarily fine feature as retrievable without
calibrating the noise would simply hide the difficulty in an input assumption.
The many-query acquisition cost and correlations between reused estimates also
remain charged; more synthetic queries do not create new experimental information.

## 6. Keep optimized conventional and unentangled strategies

A deliberately elementary bypass prevents an unfair comparison. If all we need
is the covariance c between two centered coordinates X and P, then

$$
c=\frac12\left[\operatorname{Var}\frac{X+P}{\sqrt2}
-\operatorname{Var}\frac{X-P}{\sqrt2}\right].
$$

Measurements at two rotated quadrature angles can recover it. Equal known
measurement-noise variances cancel in this difference. A single known scalar
projection can likewise be measured along its own optimal angle. Thus failure
of fixed x/p-axis marginals to reveal c is NOT a failure of all homodyne strategies.
Variance, calibration, nonstationarity and rotation costs determine the actual
comparison. This identity is ordinary covariance algebra, not a new method.

Allow optimized homodyne angles, squeezed but unentangled probes, adaptive
allocation, classical denoising and adequately specified priors. A squeezed-only
strategy is itself nonclassical; beating heterodyne is not synonymous with beating
all unentangled strategies or proving that quantum memory is necessary. [7]
distinguishes restricted-measurement practical statements from prior-dependent
worst-case separations. Neither is silently transferred to the proposed application.

Resource matching must include probe and reference energy, preparation rate,
reference storage loss, detection efficiency, mode bandwidth, stable phase
references, calibration, source uses, integration time and downstream computing.
A general-purpose fault-tolerant processor is not automatically needed by Gaussian
optical sensing. Our eventual contribution must identify a useful new algorithmic
or acquisition improvement beyond the established metrology, not merely rename it.

## 7. Next bounded decision

The preferred next CHECK is an input-and-resource-matched comparison of one
application-grounded joint-signal diagnostic against optimized separate/rotated
readouts. It is an audit of this scope-separated candidate, not a commitment to
replace the parent's classical-input objective with sensing.

Specify the actual signal/nuisance family, observable, timing of the requested
queries, energy/loss constraints and adequate decision accuracy. Do not invent
post-hoc queries solely to obstruct an otherwise optimal preselected measurement.
Show whether the task truly needs the joint record, rather than only a small set
of marginals. Price the best unentangled acquisition and its processing, not just
fixed-axis heterodyne. A surviving matched benefit deserves a new-result/prior-art
assessment; a cheap task-aligned alternative or complete coverage by existing work
ends this branch before new proof machinery is built.

Graph sparsification remains the strongest shortlisted fit to the original
reusable-classical-output goal. No claim about the physical-input candidate counts
as solving that graph problem or accelerating a classical simulator. Do not run
all three as parallel default programs. The closed emitter covariance remains
closed, and its seven-emitter test is not enlarged as part of this restart.

## 8. Evidence and primary sources

This checkpoint is a primary-literature/model screen and elementary algebra.
Three symbolic consistency checks were run with SymPy: rotated covariance,
Gaussian mean attenuation/inversion, and the equivalent variance expressions.
Those checks do not validate physical noise assumptions or quantum advantage.
No simulation, sampling experiment, native package comparison, device circuit,
new data acquisition, performance benchmark, or historical scientific verifier
was run. No large checker framework was added. PDF text was inspected for the
access assumptions of [1-3]; screenshot attempts failed and no plotted/table
performance values were inferred. [7] was inspected in primary HTML; [4-6]
were used at the primary abstract/application level. This is not an exhaustive
novelty audit, independent proof audit, or demonstrated application improvement.

Sources checked 29 September 2026:

[1] Apers and de Wolf, Quantum Speedup for Graph Sparsification, Cut Approximation
and Laplacian Solving, SICOMP 51(6) (2022); arXiv v4 (2023), Theorem 1 and Section 2.
https://arxiv.org/abs/1911.07306

[2] Bakshi et al., Sub-quadratic Algorithms for Kernel Matrices via Kernel Density
Estimation (2022), model and spectral-sparsification sections.
https://arxiv.org/abs/2212.00642

[3] Rubin et al., Quantum computation of stopping power for inertial fusion target
design, PNAS 121 (2024); arXiv Section II state-preparation assumptions.
https://arxiv.org/abs/2308.12352

[4] White et al., Time-dependent orbital-free density functional theory for
electronic stopping power: Comparison to the Mermin-Kohn-Sham theory at high
temperatures, PRB 98, 144302 (2018). Primary abstract; full publisher fetch failed.
https://doi.org/10.1103/PhysRevB.98.144302

[5] Steinlechner et al., Quantum-Dense Metrology, Nature Photonics 7, 626-630 (2013).
https://arxiv.org/abs/1211.3570

[6] Ast, Steinlechner and Schnabel, Reduction of Classical Measurement Noise via
Quantum-Dense Metrology, PRL 117, 180801 (2016).
https://arxiv.org/abs/1607.00130

[7] Cotler, Danielson and Kannan, Quantum Advantage for Sensing Properties of
Classical Fields (2026), Sections II-III and the scope of the Section IV comparisons.
https://arxiv.org/html/2602.17591

Only Quantum-Assisted-Algorithm-Discovery is modified. The phase-3 scientific
archive and handover are preserved. Both classical spin-offs remain independent.
No new repository, merge, release, manuscript, external contact or paid work follows.
