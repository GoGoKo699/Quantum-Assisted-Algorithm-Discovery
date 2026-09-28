# Open sampling screen 14: broaden the mechanism, not just the application label

28 September 2026. Starting head: `400403deb37e86e8f4b6f5a5d2e6721463bd6d27`.
Branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision:** keep the climate continuation test available, but do not make its
missing data a prerequisite for all exploration. Open a bounded check of direct
many-body spectral sampling, with nuclear magnetic resonance (NMR) as the first
consumer to examine. This is an additional mechanism hypothesis, not a completed
application selection, new algorithm, or useful quantum-advantage claim.

## 1. Separate the mechanisms

| Mechanism | Source of a possible benefit | Present role |
|---|---|---|
| Select rare classical trajectories | Coherent conditioning on a costly classical computation | Climate test retained; empirical comparison still needs its source packet |
| Generate a quantum system's spectral response | Quantum evolution generates transition statistics without enumerating eigenstates or replaying a classical trajectory solver | New bounded literature/consumer check |
| Use quantum proposals for a classical target distribution | Quantum dynamics may connect regions poorly explored by classical updates | Reserve; Note 07's predecessors and strong-classical requirements remain |

These are different hypotheses. A limitation of one is not evidence against the
others. Conversely, changing an application name while retaining the same costly
oracle does not create a new mechanism. No broad simulation campaign is opened.

## 2. An independent consumer for spectral samples

Classical NMR research already fits nuclear-spin Hamiltonian parameters to measured
spectra and uses those models to predict spectra under other field conditions.
Dashti et al. [1,2] supply software and parametrized compounds for molecular
identification and mixture analysis. These establish the use of calculated spectra;
they do not establish a classical bottleneck in any particular compound.

The proposed consumer is a specified spectral-fitting or model-discrimination
calculation at measured resolution. The input includes a supplied spin Hamiltonian,
pulse/observable convention, and experimental conditions. Predicting the spin
response from those parameters is distinct from computing electronic chemical
shifts and couplings from first principles. We must not attribute a speedup in the
former to the whole latter workflow.

Direct spectral quantum samplers already exist [3]. Quantum-assisted NMR model
inference is also prior work [4], with a public code/data repository. Neither
architecture is a proposed novelty here. The potential result must be a useful
regime or improved complete algorithm, not another small-spectrum reconstruction.

## 3. A direct output law, without a classical trajectory oracle

Let H act on D=2^n states, with eigenpairs (E_a, |a>), and let O be a nonzero
Hermitian observable. Set hbar=1. The normalized infinite-temperature
**autocorrelation spectral measure** is

$$
\mu_O(d\omega)=\frac{1}{\operatorname{Tr}(O^2)}
\sum_{a,b}|\langle a|O|b\rangle|^2
\delta_{E_a-E_b}(d\omega).
$$

It is a probability measure because the squared matrix elements sum to Tr(O^2).
It is not automatically an absolute absorption intensity or an arbitrary
multi-pulse NMR signal. Polarization, observable choice, relaxation and instrument
response must match the experiment; signed or complex signals are not positive
probability laws merely because they are called spectra.

Here is an algebraic restatement of the established spectral-sampling mechanism
[3], using a fixed computational-basis vectorization to expose complex conjugation:

$$
|O\rangle\!\rangle=
\frac{\sum_{j,k}O_{jk}|j\rangle|k\rangle}
{\sqrt{\operatorname{Tr}(O^2)}},\qquad
L=H\otimes I-I\otimes H^T.
$$

The eigenvectors of L are |a> tensor |b*> with eigenvalues E_a-E_b. Their overlaps
with the prepared state are O_ab/sqrt(Tr(O^2)), so ideal energy-gap measurement
gives mu_O. The conjugate second register matters; replacing H^T by H for an
arbitrary complex Hamiltonian is not justified. This identity does not assume
that the eigenbasis is classically computed or supplied.

Finite-time phase estimation samples a broadened/discretized measure, not exact
delta peaks. Its resolution, spectral leakage, aliasing, circuit error and
measurement cost must be analyzed against the intended experimental resolution
[5]. One cannot identify its response kernel with the instrument's kernel by fiat.
A frequency sample is a direct classical output; learning a replacement classical
program is not required.

## 4. State preparation need not hide a cold many-body ground state

The high-temperature nuclear-spin approximation is an established NMR regime
[3,4]. It is a statement about nuclear energy splittings relative to temperature,
not a claim that a molecule must be heated without limit. The normalized
correlation shape is distinct from the small physical polarization-dependent
signal strength.

For O=(1/2) sum_j X_j, an elementary preparation illustrates the opportunity:
prepare a one-excitation W state on an n-qubit register B, initialize register A
to zero, then apply H to each A_j and CNOT(A_j,B_j). The result is the equal
superposition of Bell-pair products having one Psi+ pair and n-1 Phi+ pairs.
This equals |O>> because Tr(O^2)=Dn/4. Known W-state rotations and their precision
still cost resources, but this construction needs neither a ground-state oracle
nor rejection over thermally rare eigenstates. It is a standard circuit identity,
not a novelty or optimality claim. General observables need their own preparation.

Finite-temperature corrections beyond the justified high-temperature response,
open-system effects and difficult observables can reintroduce preparation or
simulation costs. The simple identity does not solve those tasks.

## 5. Compare what the experiment uses, not an unnecessary microscopic output

If an experimental bin has response function R_k(omega), the relevant probability
is p_k=integral R_k dmu_O, with appropriate nonnegative normalized responses.
A competitor can compute these probabilities or the fitted physical parameters
directly; it need not reproduce every microscopic transition or our quantum state.
Shot counts retain ordinary statistical uncertainty, and repeated state
preparation/evolution must be charged. Smaller requested linewidth normally
requires longer coherent evolution; a large number of spins is not a cost estimate.

This caution is concrete, not hypothetical. Oh et al. [6] give efficient classical
algorithms for the harmonic vibronic-spectrum problem associated with Gaussian
boson sampling. Their route uses Fourier information about the aggregated spectrum
rather than reproducing the full mode-occupation distribution. Their result does
not settle anharmonic spectroscopy or every spin spectrum, but it rules out
transferring microscopic sampling hardness automatically to a useful spectral task.

The NMR classical baseline is also much stronger than dense diagonalization.
Restricted-state methods reproduced selected protein NMR experiments with over a
thousand spins [7]; tensor-train methods exploit favorable interaction structure
[8]. These results have specific approximation/topology/experiment scopes. They
neither solve every strongly coupled spectrum nor permit us to declare a generic
20- or 30-spin instance classically hard. Fitting against existing spectral libraries
and other experimental measurements are legitimate alternatives too.

## 6. Next discriminating task

For one experimentally studied spin system, trace a measured spectrum, its
Hamiltonian parametrization and field/pulse conditions, and the best classical
calculation of the same resolution-limited output. Identify the time range and
correlations actually needed to distinguish credible fitted models or predict a
held-out experimental condition. Do not demand extra precision solely to defeat a
classical approximation. A previously fitted spectrum is a validation control,
not a new scientific prediction.

A useful initial result could show where classical state-space restriction stops
being adequate at the experimental resolution, or where direct spectral samples
reduce the complete cost of the same inference. A completed quantum advantage is
not required before testing this. But the full comparison must price parameter
acquisition, operator preparation, evolution, controlled/conjugate operations,
sampling, broadening, repeated fitting and validation. No specific compound or
positive margin has yet been established here.

If a classical approximation succeeds for that compound, attribute the result to
that regime instead of treating it as a universal failure of quantum sampling.
If a quantum benchmark uses a real but scientifically unneeded molecule or an
unnecessary resolution, it does not pass the parent's usefulness test. Small
calculations should settle the leading question, not become the research output.

## 7. Execution boundary and sources

This checkpoint performs primary-literature inspection and analytic checking of
the displayed vectorization/Bell-state identities. No numerical model, native NMR
package, quantum circuit, spectrum fit or scientific verifier was run. No new
diagnostic framework or toy census was created. Climate access was not retried;
its previously missing packet is not claimed acquired. Historical evidence is
unchanged. This is not an exhaustive novelty audit.

The PDFs of [3,4,6] supplied text, but web screenshot attempts failed. No numerical
plot or table was digitized or interpreted. Published abstracts/HTML supplied the
application and classical comparison statements. A search also surfaced the
15 September 2026 preprint arXiv:2609.17102, reporting an effective 21-spin NMR
hardware calculation. Only its indexed primary abstract was available in this
screen; its claimed difficulty and end-to-end costs were not verified. It is a
predecessor to audit, not a chosen workload or evidence of our advantage.

[1] Dashti et al., Spin System Modeling of Nuclear Magnetic Resonance Spectra for
Applications in Metabolomics and Small Molecule Screening, Analytical Chemistry
89, 12201-12208 (2017). Primary abstract/application interface inspected.
https://doi.org/10.1021/acs.analchem.7b02884

[2] Dashti et al., Applications of Parametrized NMR Spin Systems of Small Molecules,
Analytical Chemistry 90, 10646-10649 (2018). Primary abstract and interface description.
https://doi.org/10.1021/acs.analchem.8b02660

[3] Sels and Demler, Quantum generative model for sampling many-body spectral
functions, Physical Review B 103, 014301 (2021), arXiv:1910.14213v1. The algorithm
and preparation passages of the preprint were read; not a full audit of its
complexity claims or the journal version. https://arxiv.org/abs/1910.14213

[4] Sels et al., Quantum approximate Bayesian computation for NMR model inference,
Nature Machine Intelligence 2, 396-402 (2020), arXiv:1910.14221v2. Primary abstract,
input/high-temperature description and data statement inspected. Repository README
read through GitHub; no implementation executed.
https://doi.org/10.1038/s42256-020-0198-x
https://github.com/dsels/QuantumNMR

[5] Sakuma et al., Entanglement-assisted phase-estimation algorithm for calculating
dynamical response functions, Physical Review A 110, 022618 (2024). Primary
abstract on finite-resolution spectral leakage; no independent circuit comparison.
https://doi.org/10.1103/PhysRevA.110.022618

[6] Oh et al., Quantum-inspired classical algorithms for molecular vibronic spectra,
Nature Physics 20, 225-231 (2024), arXiv:2202.01861. Publisher abstract and preprint
Fourier-component argument inspected, not every generalization or numerical test.
https://doi.org/10.1038/s41567-023-02308-9

[7] Edwards et al., Quantum mechanical NMR simulation algorithm for protein-size
spin systems, Journal of Magnetic Resonance 243, 107-113 (2014). This is a
CLASSICAL algorithm for quantum spin dynamics. Primary abstract and stated
approximation scope inspected. https://doi.org/10.1016/j.jmr.2014.04.002

[8] Savostyanov et al., Exact NMR simulation of protein-size spin systems using
tensor train formalism, Physical Review B 90, 085139 (2014). Primary abstract and
topology-dependent comparison inspected; no native benchmark reproduced.
https://doi.org/10.1103/PhysRevB.90.085139

Only the parent repository is writable. Manthan stays paused; battery/operator
candidates and both independent spin-offs are not reopened. No new repository,
external contact, paid/unattended computation, manuscript, release or merge.
