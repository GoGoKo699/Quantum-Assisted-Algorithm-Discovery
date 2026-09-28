# Interfacial reference decision 06: park the present battery route

28 September 2026. Starting branch head:
`ce8e9197c0182f5bd8f40b3e7ec68461c742117b`.
Working branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision:** the bounded search did not justify a quantum-reference task for the
selected salt-dependent gas observable. Park this battery-simulator candidate as
an active parent direction. Preserve its calibration and application evidence.
Do not replace it with a general interphase-modeling project or a more precise
isolated-cluster showcase. This is a research-selection decision, not a no-go
result for quantum chemistry or a claim that batteries are unimportant.

## 1. The question actually tested

The [preceding study](PHYSICAL_RELEVANCE_05.md) selected a real experimental
contrast: replacing LiPF6 with LiODFB in EC:EMC changes the observed ethylene
signal during lithium deposition. LiODFB and LiDFOB name the same salt in the
sources discussed here. Xiang et al. attribute the suppression to a protective,
salt-derived interphase [1]. Their observation is not a direct measurement of
one elementary reaction rate.

The task was to identify a specific electronic reference, or a bounded reference
set, whose improvement has a defensible connection to that prediction. It did
not require an already deployed simulator, a complete working-cell calculation,
or proof of quantum advantage before exploration. It did require more than
finding an uncertain energy somewhere in a complex process.

## 2. What the closest inspected classical studies establish

These are relevant comparisons, not a ranking of all classical battery models.

| Study | What was inspected | Consequence for this candidate |
|---|---|---|
| Brown and Lucht [2] | Author-deposited abstract: favorable LiDFOB concentration differs between EC- and FEC-based electrolytes | A salt-only rule cannot substitute for a solvent-conditioned prediction |
| Hawari et al. [3] | Salt comparison with surface spectroscopy and impedance; EC:DEC and Cu/NMC, not the selected EC:EMC/LFP protocol | Supports investigating film evolution, but does not supply the target salt-to-ethylene response model |
| Yang et al. [4,5] | Classical reaction pathways and surface characterization for a LiDFOB additive | Supplies a concrete microscopic candidate to inspect rather than another generic quantum oracle |

Brown and Lucht report favorable concentrations near 1 M in EC electrolytes but
0.05-0.10 M in FEC electrolytes [2]. Those are outcomes for their tested systems,
not global optima or a quantitative model for the selected gas experiment.

Hawari et al. associate the LiDFOB comparison with a different interphase,
deposition morphology, and fitted film resistances [3]. Impedance fits are not
a microscopic electron-leakage coefficient or a prediction of gas generation.
No such conversion is established by this audit.

Yang et al. use 2 wt% LiDFOB added to a LiPF6 electrolyte, rather than replacing
the salt. They use B3LYP/6-311++G(d,p) molecular calculations with a dielectric
continuum, as well as surface calculations [4]. Their proposed mechanism has
initial salt/EC reactions creating boron-containing protective products.
The physical interpretation is a hypothesis to test, not unique identification
of the whole film from its elemental/bond signatures.

## 3. The most direct electronic candidate does not clear the next step

The concrete candidate is the relative free energies of the ring-opening and
B-F-cleavage pathways for the reduced LiDFOB species depicted in Supplement
Figure S3 of [5]. The reported calculation favors ring opening. We visually
checked that figure; no precise energies were digitized and no rate ratio was
inferred from its broken-axis plot.

This is a real molecular question with a classical calculation, not an invented
object. But the candidate does not currently answer our parent research question.
The inspected work does not give the sensitivity of the selected cycle-resolved
ethylene signal to a correction of these reference energies. The following
connections remain unspecified for that prediction:

- how the reaction channels populate and transform the interphase under the
  selected salt replacement, concentration, potential, and surface history;
- how those populations determine coverage and continued solvent/electron access;
- how production and subsequent consumption/transport determine the measured gas.

Those are not all automatically electronic errors, nor are they assumed larger
than electronic errors. They are additional dependencies that cannot be replaced
by a more precise value for the first reaction alone.

A second tempting shortcut is to refine a molecular orbital gap and call the
result a film-conductivity improvement. Supplement Figure S12 contains such gaps
for proposed products [5]. A scalar molecular gap does not specify the geometry,
connectivity, contacts, defects, or transport law of a film. We have not established
a map from that scalar to the needed electron leakage or gas prediction either.
No second active research line is opened around this observation.

An important conceptual distinction follows. Initial reaction of EC can help
build a protective film, whereas continuing EC consumption can be undesirable.
A model that minimizes all initial EC reactivity need not optimize the useful
observable. This is our inference from the proposed mechanism, not a new measured
chemical effect or a denial of the original gas experiment.

## 4. Why this is a stopping decision for the current parent candidate

| Requirement | Present evidence |
|---|---|
| Independent physical motivation | Established for the experimental contrast |
| Relevant classical microscopic proposals | Found and inspected within the stated access limits |
| One justified reference-to-observable sensitivity | Not established |
| Matched quantum advantage in obtaining the required references | Not established |
| Reason to launch a large electronic/resource/training campaign | Not established |

It would be possible to keep adding chemistry, transport, and film-growth work.
Doing so would turn the parent into a broad battery-modeling program before
identifying its quantum-discovery contribution. That is not the selected task.
The bounded search is therefore complete with a parking decision.

This does **not** establish that classical methods already predict every relevant
observable adequately, that no better interfacial model exists, or that quantum
references could never help. It also does not require that an eventual useful
reference set contain only one calculation. The failure here is the missing
supported connection and comparison, not the number of molecules or the absence
of an experimental product today.

The verified Li40 archive remains a calibration resource. It does not authorize
substituting a bare cluster for an electrolyte-dependent interface, and it does
not force the next parent question to remain in chemistry. The failed constant
correction diagnostic and all earlier caveats remain unchanged.

## 5. Reopening criterion and next parent task

Reopen this particular route when there is an independently justified mapping
from a specified electronic reference problem to the required prediction, with
an observable-linked precision or cost requirement and a strong classical
comparator. A credible sensitivity calculation and a bounded validation route
can justify renewed investigation; a completed commercial simulator is not
required. An additional important-looking molecule or another count of qubits
is not sufficient evidence.

The next parent task is application/mechanism selection without a preselected
domain. Compare a few short contracts containing the same five items from the
start: a useful classically deployed output, matched explicit inputs, a specific
discovery bottleneck, a quantum mechanism, and the strongest adequate classical
route. Choose a discriminating calculation before implementation. There is no
new selected application in this checkpoint, no new repository, and no promotion
of either existing classical spin-off into the main result.

## 6. Inspection and execution record

This checkpoint searched and inspected primary literature and wrote a bounded
research decision. Yang et al.'s main-text methods/mechanism and supplementary
PDF pages 2 and 6 (zero-based) were inspected, with successful screenshots for
Figures S3 and S10-S12. Brown/Lucht's institutional abstract was read; its full
PDF download failed. Hawari et al.'s abstract, captions, and initial parsed PDF
material were accessible, but later full-PDF access and screenshot requests
failed. No plotted measurements from that paper were digitized.

A 2026 off-lattice kinetic-Monte-Carlo paper [6] was identified through primary
metadata/indexing. Full-text access did not succeed. It is recorded as an
unassessed potential comparator, not evidence that no advanced classical model
exists or that it does or does not reproduce the selected experiment. Other
related-domain papers found during search were not silently transferred to the
chosen electrolyte. This is not an exhaustive literature or priority audit.

Runtime download attempts failed on DNS. No electronic structure, trajectories,
quantum circuits, force-field training, native performance benchmarks, new
scientific code, or scientific-verifier runs were performed. Neither the archive
nor its existing checker was rerun for this literature decision. Repository
verification is limited to documentation links, branch state, and changed paths.
Historical proof/source/result files, licenses and both spin-offs are preserved.

## Primary sources

[1] Y. Xiang et al., *Gas induced formation of inactive Li in rechargeable lithium
metal batteries*, Nature Communications 14, 177 (2023).
https://doi.org/10.1038/s41467-022-35779-0
Main-text salt intervention, interpretation and methods rechecked.

[2] Z. L. Brown and B. L. Lucht, *Synergistic Performance of Lithium
Difluoro(oxalato)borate and Fluoroethylene Carbonate in Carbonate Electrolytes for
Lithium Metal Anodes*, Journal of The Electrochemical Society 166, A5117-A5121
(2019; online 2018). https://doi.org/10.1149/2.0181903jes
Primary author abstract: https://digitalcommons.uri.edu/chm_facpubs/115/

[3] N. H. Hawari et al., *Understanding SEI evolution during the cycling test of
anode-free lithium-metal batteries with LiDFOB salt*, RSC Advances 13,
25673-25680 (2023). https://doi.org/10.1039/d3ra03184e
Primary abstract/captions: https://pubmed.ncbi.nlm.nih.gov/37649571/

[4] X. Yang et al., *Understanding of working mechanism of lithium
difluoro(oxalato) borate in Li||NCM85 battery with enhanced cyclic stability*,
Energy Materials 3, 300029 (2023).
https://www.oaepublish.com/articles/energymater.2023.10

[5] Supplement to [4], Figures S3 and S12; no new energy calculation or numerical
rate extrapolation from these figures.
https://oaepublishstorage.blob.core.windows.net/42d82b61-6e49-46ff-972e-5f5745195f46/5787-SupplementaryMaterials.pdf

[6] G. Zhou et al., *Atomic Resolution of Solid-Electrolyte Interphase Formation
via Off-Lattice On-the-Fly Kinetic Monte Carlo*, Journal of the American Chemical
Society (2026). https://doi.org/10.1021/jacs.5c21439
Primary indexed metadata only; full mechanism/application comparison unassessed.

Sources accessed 28 September 2026. No outside contact, paid computation,
manuscript preparation, release, branch merge, or other-repository write occurred.
