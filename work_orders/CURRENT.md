# Current task: a matched battery-interface feasibility comparison

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md), and
[application case 02](../exploration/phase_3/APPLICATION_CASE_02.md).

## Selected application, not an established quantum advantage

Investigate a reusable classical energy/force evaluator for initial electrolyte
chemistry at lithium-metal interfaces. Quantum computation would supply selected
expensive electronic references offline; subsequent simulation would be classical.
This is learning a reusable simulator, not a newly discovered symbolic algorithm,
a one-off energy prediction, or quantum inference at every trajectory step.

An external application need and an existing software interface are documented.
The quantum-reference-to-classical-potential architecture is prior work. No new
quantum method, novel force field, useful advantage, or battery-performance
improvement is established. The kernel and weather screens are not parallel tasks.
The old Gram/operator candidate remains parked and unchanged.

## The classical comparison must include the March 2026 work

Vo et al., arXiv:2603.22139v1, already provide correlated classical calculations
for EC on lithium clusters and identify a competitive hybrid functional. Kundu
et al., arXiv:2509.14067v1, already provide classical learned reactive potentials.
Do not use poor PBE predictions or the size of the electronic Hilbert space as
proof that useful chemistry needs a quantum computer. AFQMC and FEMION are
classical methods, despite the word quantum in their terminology.

The replayed molecular rate ratios are physical predictions, not computational
speedups. The newer static barrier data are not finite-temperature surface rates.
Their cross-method spread is not a certified error bound. Finite-size, environment,
model, and trajectory uncertainty must be distinguished from electronic precision.

## Next bounded task

Use one published neutral Li40+EC cluster as a proposed classically accessible
calibration, not as a manufactured hard instance. First seek the actual public
coordinates and method inputs through supporting deposits and cited source papers.
The data statements inspected so far did not supply a downloaded package; do not
invent coordinates or label a new geometry as the published one. No outside
contact is authorized.

For a pinned instance, establish charge, spin, basis, frozen cores, orbital count,
classical approximation/error evidence and actual resource evidence where
available. The explicit Li/C/O 1s-frozen convention gives 166 total and 74
correlated electrons; it does not establish orbital count or active-space adequacy.
Compare a fully charged quantum per-geometry calculation, including initial-state
overlap/preparation, with the strongest applicable classical route at required
observable accuracy. Do not borrow gate counts from a different molecule.

Determine whether electronic improvements could change a useful prediction beyond
finite-size, solvent/voltage, sampling and model uncertainty. Select an observable
appropriate to the pathway: a non-metastable reactant cannot be assigned an
ordinary activated rate without justification. The factor-two/300 K energy
sensitivity in the note is illustrative, not a required community tolerance.

Only a defensible per-instance comparison justifies analyzing the number of
reference geometries, training, validation, and total reusable-model preparation.
Classical active learning, embeddings, hybrid functionals, source knowledge and
direct observable computation must be permitted. A few accurate training energies
are not a useful general evaluator. Do not begin a large chemistry campaign,
model training, or generic theorem development before this comparison warrants it.

## Evidence and boundaries

`python experiments/application_case_v1/verify.py` passed twice; -O rejection was
checked. It replays selected published numbers, derives sensitivity and electron
accounting, and rejects six invalid inputs. It is not an electronic-structure,
molecular-dynamics, quantum-circuit, or performance test. No weights, coordinates,
or upstream implementation were imported. Root/historical suites were not rerun.

Both classical spin-offs own their further development. No writes there are
allowed. Phase-2 Note 27's source-aware comparison remains closed. Preserve old
proofs, code, data, reports, manifests, notices, and LICENSE. Historical next steps
do not override this work order. Modify only Quantum-Assisted-Algorithm-Discovery.
No manuscript revival, external contact, paid or unattended work, submission,
release, branch merge, or repository administration change is authorized.
