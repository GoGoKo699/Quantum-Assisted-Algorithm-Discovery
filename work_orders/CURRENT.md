# Current task: validate physical relevance, then price reusable electronic references

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md),
[application case](../exploration/phase_3/APPLICATION_CASE_02.md), and
[executed archive replay](../exploration/phase_3/ARCHIVE_REPLAY_04.md).

## Physical relevance is not yet established for the proposed output

The chemistry has a non-quantum-computing research motivation, but that does not
validate every model of it. The Li40+EC system is a finite, bare-surface calibration
cut from a larger surface model, not a proposed material expected to operate as a
50-atom component in a battery. The cluster paper explicitly leaves clusters
unpassivated and uses finite-size corrections [1]. The dynamics paper explicitly
identifies solvent, electrode voltage, and electron-transfer dynamics as missing
physics [2]. These are model boundaries, not electronic solver errors that quantum
precision automatically removes.

Before substantial Hamiltonian/resource work, complete one short relevance case:
name the actual interface regime (including electrolyte composition and surface
state), one useful observable, and the evidence that this observable needs better
prediction. Support it with primary application research and experimental evidence
where available. Do not borrow relevance from a different electrode or assume a
bare-metal model describes an already passivated interface. A transient early-stage
process may qualify if its connection to the intended use is supported.

State how the selected cluster references would inform that observable, what
omitted physics could change the conclusion, and what independent test could
validate or refute the connection. A full working-cell simulation is not required;
a defensible limited claim is. Required accuracy must follow from the observable,
not an arbitrary demand for exact energies. More accurate electronic labels earn
no claimed prediction benefit when that benefit is unsupported at model level.
A cheaper route at the same adequate accuracy can still be useful.

Current assessment: published calibration verified; useful-interface transfer
unvalidated; quantum advantage unestablished. If the relevance case cannot be
supported, park or redirect this candidate instead of developing the cluster into
a better-looking demonstration. No further archive curation is the default next
step. No claim of improved battery life, capacity, safety, or commercial deployment
is warranted by the current evidence.

Sources rechecked 28 September 2026: [1] Vo et al., arXiv:2603.22139v1,
Introduction/Methods/Conclusion, https://arxiv.org/html/2603.22139v1 ;
[2] Kundu et al., arXiv:2509.14067v1, Discussion (Section III),
https://arxiv.org/html/2509.14067v1 . These support the model classification and
its limitations, not validation of a working battery or a quantum benefit.
This is a documentation/selection-rule update; no new experimental validation or
scientific-verifier run is claimed. The scientific record below is retained.

## Archive acquisition and scalar replay are complete

The supplied paper_data.zip matches the recorded Zenodo MD5 and has SHA256
edc45a55827ed4f07596d7d1e4a5eccc0b736ee77ffe89e40eee7a20a3b28feb.
All 732 geometries and 30 tables were parsed. Li40 parallel/top/transition-state
members are hash-pinned. Do not ask for the archive again or repeat that its
coordinates have not been inspected. The ZIP is not redistributed in this repo;
the checker takes a local copy of DOI 10.5281/zenodo.22116355 as input.

The numerical geometry sequences vary cluster size around fixed molecular
geometries; they are not a reactive-potential training set. Neutral Li40+EC has
166 total and 154 correlated electrons under the audited AFQMC/ORCA C/O-core
convention. Basis counting gives 1436 full spherical cc-pVTZ functions, 1430
post-core spatial orbitals before truncation. These are not gate/runtime estimates.
XYZ files have no explicit unit, charge or spin tags. A new calculation must
state its angstrom, neutral singlet, basis and core conventions.

## What the replay establishes

Four Table II barriers reproduce to printed precision from the released method
endpoints, the CSV PBE series, and the supplied rounded PBE surface limit 5.6.
The limit itself and its transfer are not independently validated. The separate
PBE TXT series is numerically different and must not be silently substituted.

The parallel AFQMC table retains single-determinant values at four cluster sizes;
the paper's HCI refinements are a separately sourced overlay, not archive contents.
Twelve Table I NPE values reproduce with the inclusive lower endpoint N=10,
whereas the caption literally says more than 10. Preserve both interpretations.
This audit does not reproduce every final surface value or the authors' jobs.

A retrospective single-Li40/PBE correction test leaves mean discrepancies of
1.99, 3.43 and 3.06 kcal/mol against released CCSD, DLPNO-CCSD(T) and AFQMC
sequences. This rejects that simple shortcut at uniformly tight tolerance; it is
not an error bound against exact truth, a method ranking, or a no-go theorem for
multiple references, learned corrections, embedding, or quantum-assisted models.

## Conditional next steps after the relevance case

The parent seeks a useful classical simulator built more effectively with offline
quantum assistance, not a more precise isolated energy. Establish whether there
is a defensible joint reference-count and reference-accuracy regime that improves
an actual prediction after finite-size/environment and learned-model errors count.
Use the pinned pair as a calibration, not as the final deployment task.

1. Specify one application-relevant observable and the needed quality using
   application precedent. Identify what reference information must transfer to
   unseen molecular configurations. Cluster-size agreement alone does not validate
   forces, trajectories, solvent effects or a voltage-controlled interface.
   A single constant correction has now been tested; do not assume it is sufficient.
2. For a warranted electronic comparison, define a reproducible Hamiltonian for
   the pinned geometry with explicit basis/core/truncation choices. The archive
   has no SCF orbitals, integrals, FNO thresholds, state coefficients or timing logs.
   A newly configured calculation is not an exact replay of the authors' jobs.
   Do not replace the full correlation problem with an HCI trial active space.
3. Price the complete reference pipeline: preparation/overlap, Hamiltonian
   simulation, precision and repetitions, reference count, classical training and
   held-out validation. Compare at the same required observable quality with
   hybrid functionals, local correlation, AFQMC, embedding, active selection and
   direct classical computation. Energy-only training is allowed, not proven
   adequate for this surface. Neither free forces nor an unavoidable full
   finite-difference multiplier is justified.

A conditional resource sensitivity is acceptable if every unknown is explicit;
it is not a measured advantage. Missing implementation details do not prove
classical hardness. Do not launch a full 1430-orbital campaign, train a model, or
build a new framework before the useful-accuracy/cost case warrants the work.
The application remains a feasibility candidate. The generic architecture is prior
work. No new simulator, quantum advantage or battery improvement is established.

## Verification and boundaries

Run `python experiments/reference_archive_v1/verify.py --archive /path/to/paper_data.zip`.
At the archive checkpoint, the final checker passed twice with identical JSON,
eight malformed-input controls, a modified-archive rejection, and -O/-OO refusals.
It reads but does not extract or modify the archive. This is data/protocol and
arithmetic verification, not chemistry, quantum simulation, native timing or
force-field training. Historical suites were not rerun. Source and report hashes
are in the archive note. None of these tests was rerun for the present documentation
update; their code and reports are unchanged.

The operator remains parked; both classical spin-offs own their further work.
Phase-2 Note 27 remains closed. Preserve all old notes, code, data, reports,
manifests, notices and LICENSE. Modify only Quantum-Assisted-Algorithm-Discovery.
No outside contact, paid/unattended work, manuscript revival, submission, release,
branch merge or repository administration change is authorized.
