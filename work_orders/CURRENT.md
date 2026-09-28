# Current task: test the accuracy and total cost of reusable electronic references

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md),
[application case](../exploration/phase_3/APPLICATION_CASE_02.md), and
[executed archive replay](../exploration/phase_3/ARCHIVE_REPLAY_04.md).

## Archive acquisition and calibration are complete

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

## Next bounded scientific decision

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
The final checker passed twice with identical JSON, eight malformed-input controls,
a modified-archive rejection, and -O/-OO refusals. It reads but does not extract or
modify the archive. This is data/protocol and arithmetic verification, not chemistry,
quantum simulation, native timing or force-field training. Historical suites were
not rerun. Source and report hashes are in the new note.

The operator remains parked; both classical spin-offs own their further work.
Phase-2 Note 27 remains closed. Preserve all old notes, code, data, reports,
manifests, notices and LICENSE. Modify only Quantum-Assisted-Algorithm-Discovery.
No outside contact, paid/unattended work, manuscript revival, submission, release,
branch merge or repository administration change is authorized.
