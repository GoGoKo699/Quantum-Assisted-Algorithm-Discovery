# Physical relevance 05: electrolyte-dependent ethylene formation

28 September 2026. Base: `296c479edb2c1e456739de5753a6f5d1d115e699`.
Working branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision: repair the physical model before quantum resource estimation.** A
specified cell experiment supports a useful prediction target. The present bare
Li40+EC calibration does not describe the intervention that changes that target.
This is a completed scope/identifiability check, not a new chemistry calculation,
a quantitative error decomposition, or a general rejection of quantum chemistry.

## 1. An experimental target, not an application label

Xiang et al. [1] studied anode-free Cu||LiFePO4 cells: lithium is deposited on
copper during charging. The electrolyte was 1 M LiPF6 in ethylene carbonate (EC)
and ethyl methyl carbonate (EMC), 3:7 by weight. The comparison replaced LiPF6
with 1 M lithium difluoro(oxalato)borate (LiODFB), retaining that solvent mixture.
The reported protocol used room temperature, 0.75 mA/cm2, and a 2.8-3.8 V
**cell-voltage** window. It does not specify a constant anode potential versus
Li/Li+; that must not be inferred from the full-cell voltage.

Their baseline produced recurring ethylene signals during lithium deposition;
they reported no detectable ethylene for the LiODFB comparison. Isotope/titration
experiments linked electrolyte-derived ethylene to inactive LiH and Li2C2, whose
accumulation was suppressed in the comparison. The supplementary gas trace [2]
is a nondetection, not proof of a zero production rate.

This supplies a useful provisional task: **predict the salt-dependent suppression
of ethylene during lithium deposition, with a consistent explanation of inactive
lithium formation.** Predicting only the first broken bond is not the same output.

The existing experiment already establishes this particular empirical contrast.
Reproducing it is a validation requirement, not a new discovery or the ultimate
benefit. A useful reusable classical model must eventually predict an unfit
condition or composition, or obtain equally useful predictions at lower total
cost. We have not selected or validated that held-out case yet.

## 2. What observable can be compared honestly?

The first validation target is the **cycle-resolved, instrument-assigned ethylene
signal** under the stated protocol, not an assumed exact molecular branching
fraction or a battery-lifetime prediction. LiH/Li2C2 measurements provide a separate
consistency check, not a universal stoichiometric conversion of signal into loss.

A predicted gas-generation rate would need a measurement model accounting for
consumption, retention/dissolution, transport to the outlet, and instrument
response before comparison with the trace. This follows from material balance;
a smaller outlet signal need not, by itself, mean less gas was initially made.
Independent product measurements are therefore important to the proposed test.

No precise gas-yield tolerance or detection limit was established in this audit.
The main text/Methods label the ethylene channel m/z=28 while Fig. 1 and Fig. S11
captions label m/z=26 [1,2]. These may involve parent/fragment channels, but the
acquisition and calibration details were not resolved here. We retain the
authors' species assignment and qualitative contrast without silently selecting
a channel, extracting absolute yields, or claiming a resolved CO/ethylene ratio.
The article's data statement offers datasets on request; no raw traces were
obtained and no contact was made.

Required energy precision must be derived later from the validated observable
and its uncertainty. No arbitrary factor-two rate or sub-kcal threshold is set.
The existing trace is a test of a prediction contract, not a supplied electronic
accuracy target.

## 3. The present input cannot represent the tested change

The [pinned archive](ARCHIVE_REPLAY_04.md) provides a fixed EC molecule on nested
bare lithium clusters. The two Li40 members were rechecked in the supplied ZIP:
50 atoms each, with composition Li40 C3 H4 O3 and blank metadata comments. The
verified members contain no phosphorus, fluorine, boron, copper substrate,
solvent bath, evolved interphase, or potential history. Nor does the proposed
neutral, isolated Hamiltonian contain an effective representation of those inputs.

**Our inference:** when the same isolated cluster specification is supplied for
both electrolytes, a more accurate solver still solves the same problem. It
cannot by itself produce an electrolyte-dependent prediction. This is a missing
input/model connection, not a claim that an arbitrarily accurate solver is useless
inside a properly conditioned multiscale model.

Adding a salt name to a fitted wrapper can distinguish the examples, but learning
and validating that relationship then becomes an additional task whose data,
assumptions, and cost must be counted. Explicit atoms are not mandatory: an
independently justified embedding or boundary model can carry the dependence.
The present calibration supplies neither route automatically.

The selected experiment also must not be treated as pristine neutral Li(001).
Independent experiments by Menkin et al. [4] identify an interphase on copper,
voltage-dependent composition, and plating morphology dependent on surface history.
Those results concern another study, not a determination of the exact interphase
in Xiang et al. They justify treating surface state/history as an input to test,
not assigning a convenient clean surface by default.

## 4. Why the earlier reaction branching does not settle the experiment

Kundu et al. [3] study a single EC on neutral, unbiased bare Li and restrict
subsequent decomposition/desorption. Their rapid ring opening is a precursor
toward CO/CO2, not an outlet-gas measurement. Their ethylene-forming route is
analyzed with the competing bond constrained; its rate cannot simply be combined
with the rapid, non-metastable process as two independent competing exponential
rates. Solvent, potential and electron-transfer dynamics are explicitly omitted.

Their frozen-surface control also suppresses rapid ring opening at the same
nominal electronic level. This shows model/dynamical sensitivity in that system;
it is not a measured magnitude for the error caused by an experimental interphase.
Nor does detecting ethylene in the cell falsify the bare-surface result: the
initial ensembles, surface conditions, subsequent chemistry and measured outputs
differ.

**What follows:** precise energies for the archived parallel/transition-state pair
are not yet a justified way to predict the selected gas-suppression contrast.
What does not follow is that environmental error has been proved numerically larger
than electronic error. No such error budget has been calculated.

## 5. A bounded repair, not a new simulation campaign

The next decision concerns one mechanism: does the salt intervention primarily
change access of EC/electrons to reactive lithium through interphase formation,
or does it change the conditional chemistry after EC reaches a reactive site?
The authors favor preferential anion decomposition and passivation [1]. That is
a mechanistic interpretation to test, not uniquely identified causation from the
salt comparison alone; solvation, transport and surface morphology can also change.

Inspect existing classical descriptions of this intervention before building a
new one. Require the proposed description to map both electrolyte recipes and
the electrochemical/surface history into the measured observable using one
consistent model. Audit its most consequential uncertain electronic input, if any.
The immediate output is at most one concrete interfacial reference problem with
an explicit link to a measurable prediction and a classical comparator.

A model need not simulate the whole battery atom by atom. A validated reduced
kinetic or boundary description could suffice. Conversely, adding a larger bare
cluster or more total-energy digits does not supply the missing dependence.
Existing classical methods are not restricted to PBE: Vo et al. [5] already
identify competitive hybrid references for their static benchmark. Their success
is not proof of sufficiency for the evolving electrolyte, but must be permitted.

Proceed to quantum costing only if a warranted interfacial reference changes the
prediction at useful accuracy, or reduces total model-preparation cost at that
accuracy. Include preparation/overlap, reference multiplicity, validation and any
environment reduction. A few accurately solved examples cannot replace a
held-out prediction test. If no specific quantum-improvable reference is exposed,
park this application rather than undertake general interphase modeling here.

## 6. Evidence and stopping decision

| Question | Outcome of this audit |
|---|---|
| Is there an independently useful observable? | Yes: experimentally observed salt-dependent gas/inactive-lithium behavior |
| Does the present isolated calibration encode that comparison? | No, not without an additional justified environment/history mapping |
| Is electronic accuracy the demonstrated dominant bottleneck? | Unknown; no quantitative ranking of uncertainties was established |
| Is a quantum resource campaign justified now? | No; retain only the bounded interfacial-model/reference selection task |

Primary literature, main-text methods and supplementary gas measurements were
inspected. The experiment's Fig. 4, Supplement Fig. S11, and the dynamics paper's
Fig. 3 were visually checked from PDFs. The experimental Fig. 1 screenshot failed;
its textual description was read, without digitizing that graph. No experimental
results were reproduced. No native chemistry, trajectories, learned model,
quantum simulation, new scientific verifier or performance test was executed.

A fresh local read verified archive SHA256
`edc45a55827ed4f07596d7d1e4a5eccc0b736ee77ffe89e40eee7a20a3b28feb`,
and the two Li40 compositions/member hashes already recorded in Note 04. It did
not extract or change the archive. The full archive checker and root/historical
suites were not rerun. No upstream data or code is redistributed by this note.
Source research, proofs, reports, licenses and both spin-offs remain unchanged.

## Primary sources and scope

[1] Y. Xiang et al., *Gas induced formation of inactive Li in rechargeable lithium
metal batteries*, Nature Communications 14, 177 (2023). Results, Methods,
Discussion and data statement inspected. https://doi.org/10.1038/s41467-022-35779-0

[2] Supplement to [1], especially Figs. S9-S13. Fig. S11 visually inspected;
no raw data, calibration or detection-limit estimate reconstructed.
https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-022-35779-0/MediaObjects/41467_2022_35779_MOESM1_ESM.pdf

[3] S. Kundu et al., *Reaction dynamics of lithium-mediated electrolyte decomposition
using machine learning potentials*, arXiv:2509.14067v1. Sections II-III and
Fig. 3 inspected; not a new audit of its calculations.
https://arxiv.org/html/2509.14067v1

[4] S. Menkin et al., *Toward an Understanding of SEI Formation and Lithium Plating
on Copper in Anode-Free Batteries*, J. Phys. Chem. C 125, 16719-16732 (2021).
Primary author-deposit abstract inspected, not the full experimental dataset.
https://doi.org/10.1021/acs.jpcc.1c03877
https://www.repository.cam.ac.uk/handle/1810/324307

[5] E. A. Vo et al., *Adsorption energies and decomposition barrier heights for
ethylene carbonate on the surface of lithium from cluster-based quantum chemistry*,
arXiv:2603.22139v1. Introduction/Methods and stated comparison scope rechecked.
https://arxiv.org/html/2603.22139v1

Sources checked 28 September 2026. This bounded study neither establishes that
no better model exists nor exhausts the literature. It makes a decision about the
current parent candidate: physical-model repair first, no stronger battery claims
and no quantum resource estimate for an unconnected calibration.
