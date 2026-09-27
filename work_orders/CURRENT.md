# Current task: pin the released battery reference and compare the same problem

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md),
[application case](../exploration/phase_3/APPLICATION_CASE_02.md), and the latest
[reference/protocol audit](../exploration/phase_3/REFERENCE_ACCESS_AUDIT_03.md).

## Purpose, unchanged

Test whether offline quantum electronic references can improve construction of a
useful classical simulator for initial lithium-metal/electrolyte chemistry. The
architecture is prior work. No quantum advantage, new force field, or improved
battery prediction is established. The operator candidate stays parked and the
two classical spin-offs remain independent.

## Inputs now located; runtime transfer remains incomplete

The static cluster paper has a public [Zenodo deposit](https://zenodo.org/records/22116355),
DOI 10.5281/zenodo.22116355, published 26 August 2026. The archive is
`paper_data.zip`, displayed size 1.4 MB, listed MD5
`cf3b3c01508a96749a39442850007f32`. Its preview lists Li40 parallel, top and
transition-state XYZ files and correlated energy data. Earlier access statements
are historical; do not repeat that no public geometry deposit was found.

The archive itself has not been transferred into the runtime. No checksum or
member hashes have been checked. Obtain the original ZIP through a working download
or user upload; no author contact is needed. Inspect README, units and rights before
redistributing anything. Do not recreate coordinates or call a new geometry published.
The static archive is not established to contain a full training/model package.

## Matched-model correction that must be retained

Supplement S3 of Vo et al., arXiv:2603.22139v1, and ORCA 6.0 Table 7.15 specify
C/O 1s freezing, not Li 1s freezing, for the audited AFQMC/ORCA comparison.
Neutral Li40+EC therefore has 166 total and 154 correlated electrons in that
convention. The previous 74-electron count was a different hypothetical convention.
Do not use it as the published problem. Independently confirm the PySCF CCSD setup.

The full spherical cc-pVTZ basis contains 1436 spatial functions, or 1430 after
six core orbitals are removed and before any virtual-space truncation. The 2860
system-qubit count for one untapered occupation encoding is not a minimum or a
full resource estimate. HCI trial active spaces in the supplement do not define
the full AFQMC correlation space and do not establish a quantum overlap bound.

## Next bounded calculation

After obtaining the ZIP, verify its digest, inspect and hash the needed members,
and pin the parallel/transition-state Li40 pair, charge, spin, basis, core and
method settings. Determine which published energies can actually be replayed.
Record native classical runtime only if it is measured or supported by a source.
No inference of runtime from Hilbert-space size, basis size or a plot is permitted.

For a quantum estimate, establish the Hamiltonian representation and coefficients,
truncation error, initial-state preparation/overlap, precision and full circuit
cost. Do not borrow numbers from another molecule. Compare at required observable
quality, allowing hybrid functionals, local correlation, AFQMC, embedding, active
selection and direct classical computation of the observable.

Keep energy-only model construction as a legitimate alternative: Kundu et al.
trained their molecular CCSD(T) model without force labels. This does not validate
energy-only training at the surface. Neither free force labels nor an unavoidable
finite-difference multiplier may be assumed. Training and held-out validation
reference costs count; published sample counts are precedents, not lower bounds.

The static calibration is not the fluctuating surface pathway. Establish relevance
to the intended prediction and environmental/model uncertainty before a full
reference campaign. A small-model exact energy is not automatically better interface
physics. No large chemistry run, model training or generic theorem is now scheduled.

## Evidence and authority

The latest checkpoint is a source/protocol audit plus executed integer dimension
accounting. No archive import, Hamiltonian build, electronic calculation, molecular
trajectory, quantum simulation or performance test occurred. No new verifier was
added; existing scientific suites were not rerun. Historical test claims are not
new runs. Preserve old notes, code, data, results, manifests, notices and LICENSE.

Only Quantum-Assisted-Algorithm-Discovery may be modified. No outside contact,
paid or unattended work, manuscript revival, submission, release, branch merge
or repository administration change is authorized. Phase-2 Note 27 remains closed.
