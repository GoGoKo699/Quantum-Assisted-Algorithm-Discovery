# Current task: identify one justified interfacial reference, not a bare-cluster showcase

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md), and the
[physical-relevance decision](../exploration/phase_3/PHYSICAL_RELEVANCE_05.md).

## Completed decision: repair the physical model first

An independent experiment supplies a concrete validation contrast: Cu||LiFePO4
cells with 1 M LiPF6 versus 1 M LiODFB, both in EC:EMC 3:7 by weight, show different
ethylene evolution and inactive-lithium accumulation. The source is Xiang et al.,
Nature Communications 14, 177 (2023), DOI 10.1038/s41467-022-35779-0.

This is an evolving, electrolyte-covered, electrochemically driven interface,
not a single EC on neutral bare lithium. The fixed Li40 calibration has no salt
or justified effective environment input; improving its solver alone does not
predict the experimental intervention. The published initial ring-opening
observations are not outlet-gas branching fractions. A constrained slow-path
rate cannot be divided by a non-metastable first-passage time to obtain a
competition probability. The decision is model repair, not a numerical proof
that environmental error dominates electronic error.

The empirical salt comparison is already known. Matching it is necessary
validation, not a new useful discovery. Any eventual classical simulator must
predict an unfit condition or provide equally useful predictions more cheaply.
No validated simulator, quantum advantage or battery improvement is established.

## Next bounded task

Inspect the strongest existing salt/interphase-aware classical description of
this contrast. Focus on the competition between interphase-mediated access to
reactive lithium and the chemistry conditional on reaching it. Do not build a
new general molecular-simulation framework.

Determine whether at most one uncertain electronic reference controls a useful
prediction after solvent, salt, surface history, electron availability and the
measurement mapping are accounted for. An explicit interfacial configuration or
a justified embedding is acceptable; supplying a salt label to a fitted wrapper
without pricing its learning and validation is not a quantum advantage.

The deliverable is one specific reference problem with an observable sensitivity,
matched adequate classical comparator, and a route to testing an unfit condition.
If no such reference is exposed, park this application instead of launching
broad interphase modeling. The old Li40 pair remains a calibration tool only.
No substantial quantum resource estimate, model training, large simulation or
further archive-curation campaign follows automatically.

For the experimental comparison, retain room temperature and the reported
0.75 mA/cm2, 2.8-3.8 V cell protocol. Full-cell voltage is not anode potential.
Nondetection is not zero production. Channel assignments, calibration and gas
transport/consumption must be resolved before absolute yield claims; no numerical
detection limit or predictive energy tolerance is established. The paper and
supplement use different ethylene channel labels; preserve that uncertainty.

Only a warranted reference may proceed to costing: Hamiltonian representation,
state preparation/overlap, precision, repetitions, reference multiplicity,
classical model construction and held-out validation. Allow hybrid functionals,
local correlation, AFQMC, embedding, energy-only training, active selection and
direct classical prediction. Do not demand exact energies when they are unnecessary.

## Preserved evidence and authority

The [archive replay](../exploration/phase_3/ARCHIVE_REPLAY_04.md) completed the
732-geometry/30-table audit. The upload is present and pinned; do not request it
again. Those files are cluster-size scans, not a reactive training set. The
matched [core convention](../exploration/phase_3/REFERENCE_ACCESS_AUDIT_03.md)
remains 154 correlated electrons for Li40+EC; a small HCI trial space is not the
full correlation problem and basis size is not runtime.

This relevance checkpoint inspected primary research and selected PDF figures,
and locally rechecked only the archive digest and two Li40 member compositions
and hashes. No electronic, MD, quantum, timing or training calculation was run;
the full archive and historical verifiers were not rerun. Record future checks
accurately and preserve all historical source/results and rights notices.

The operator remains parked; both classical spin-offs own their further work.
Phase-2 Note 27 remains closed. Modify only Quantum-Assisted-Algorithm-Discovery.
No external contact, paid/unattended work, manuscript revival, submission, release,
branch merge or repository administration change is authorized.
