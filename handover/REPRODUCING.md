# Reproducing the evidence

[Handover](../HANDOVER.md) · [Exploration index](../exploration/README.md)

**Reproducible mathematics is not hardware eligibility.** The current no-QRAM
boundary parks the short-seed algorithm as a lead; its earlier exact checks remain
available. Passing them does not implement coherent data access or convert its
RAM-model time into a circuit cost. This maintenance runs no scientific verifier.

## Correct branch and safe output handling

```sh
git clone https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery.git
cd Quantum-Assisted-Algorithm-Discovery
git switch research/prx-quantum-phase2
git rev-parse HEAD
OUT=$(mktemp -d)
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
python -VV
```

Record the actual commit and environment of a rerun. Do not reset a dirty worktree
or overwrite a versioned `REPORT.json`. Use a separate worktree for a historical
revision. The instructions below are opt-in reproductions, not a request to run
all suites before the next research step. No CI pass is implied by this guide.

Never run assertion-dependent checks with `-O` or `-OO`. Install only dependencies
required by the selected source header, in an isolated environment if needed.
There is no all-project environment, test runner, or proof-validation command.

## Phase-4 checks

All three source headers specify Python 3.10+. The readout checker uses SymPy and
NumPy; the graph-contract and short-seed checkers use the standard library.

| Note and source | Saved report | Actual scope |
|---|---|---|
| [02: task-matched readout](../experiments/task_matched_readout_v1/verify.py) | [Readout report](../experiments/task_matched_readout_v1/REPORT.json) | Finite regression/symbolic identities and Gaussian covariance arithmetic; not a sensor experiment |
| [03: implicit graph contract](../experiments/implicit_graph_contract_v1/verify.py) | [Graph report](../experiments/implicit_graph_contract_v1/REPORT.json) | Exact graph/access and comparison controls; not a classifier or randomized sparsifier run |
| [04: short-seed sampling](../experiments/short_seed_sparsification_v1/verify.py) | [Short-seed report](../experiments/short_seed_sparsification_v1/REPORT.json) | Hashing, trace moments, probability rounding, and adaptive-seed checks; not quantum search, a spanner implementation, or a gate-cost audit |

Run only the applicable command:

```sh
python experiments/task_matched_readout_v1/verify.py > "$OUT/readout-02.json"
python experiments/implicit_graph_contract_v1/verify.py > "$OUT/graph-03.json"
python experiments/short_seed_sparsification_v1/verify.py > "$OUT/short-seed-04.json"
```

For example, compare a regenerated short-seed report without changing the archive:

```sh
cmp experiments/short_seed_sparsification_v1/REPORT.json "$OUT/short-seed-04.json"
```

A changed environment can alter printed floating-point output in applicable
suites. Inspect the executable checks and numerical differences instead of editing
an archived report to match. A byte-identical run still does not establish novelty,
proof completeness, an adequate physical model, or useful quantum advantage.
Notes 01 and 05 have no new scientific suite: they are a source/model screen and
an owner hardware decision respectively. The [phase-4 index](../exploration/phase_4/README.md)
links their complete scope.

## The phase-3 activity closeout is separate

```sh
python experiments/activity_acquisition_v1/verify.py > "$OUT/activity-29.json"
python experiments/activity_acquisition_crosscheck_v1/verify.py > "$OUT/activity-29B.json"
```

These require NumPy and SciPy and are more substantial opt-in sparse calculations.
[Note 29](../exploration/phase_3/CLASSICAL_ACTIVITY_ACQUISITION_29.md) uses windows
1, 4, 16 and [its report](../experiments/activity_acquisition_v1/REPORT.json).
[Note 29B](../exploration/phase_3/CLASSICAL_ACTIVITY_CROSSCHECK_29B.md) uses windows
1, 5, 20 and [a distinct report](../experiments/activity_acquisition_crosscheck_v1/REPORT.json).
Do not merge those rows or count the implementations as separate applications.
The [closeout](../exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md) records the
scientific decision; the [import/replay manifest](../provenance/activity_closeout_30.json)
records the earlier 29B replay with NumPy 2.3.5 and SciPy 1.17.0 under one BLAS
thread. This guide does not claim a new installation or replay of that environment.

The [phase-3 index](../exploration/phase_3/README.md) locates the supporting emitter,
spectral, and probability-law checks. Read each source header. Historical scopes
and commands are also preserved in the
[pre-update reproduction guide](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/f957571985efd242cd7d4f3d8058641b483f07e5/handover/REPRODUCING.md).

## Root verification and external inputs

Root `python verify.py` checks the original guided-search imports and its own
mathematics, not every later phase. Its optional `--quick` and `--full` modes add
historical C++17 runs. `verify_target_closure.py` has another separate historical
scope. Do not treat any of these as documentation checks or proof audits.

The battery archive checker uses the authors' external input:

```sh
python experiments/reference_archive_v1/verify.py --archive /path/to/paper_data.zip
```

[Archive replay 04](../exploration/phase_3/ARCHIVE_REPLAY_04.md) records provenance
and scope. The previously supplied archive need not be requested again, imported
into this repository, or relicensed. [Climate audit 13](../exploration/phase_3/CONTINUATION_INFORMATION_13.md)
records the missing continuation/ancestry files; they block only that empirical
test, not model-first analysis. No climate run or measured statistic follows from
an unrelated finite probability-law test.

[PROVENANCE.md](../PROVENANCE.md), earlier manifests, and source notices retain
third-party rights. The root MIT license does not replace their conditions.

## Alternate checkpoints

Use [ALTERNATE_CHECKPOINTS.md](ALTERNATE_CHECKPOINTS.md) before applying any old
attachment patch. Local and committed 03/04 payloads are distinct; canonical file
paths are listed above. Matching numbers or filenames do not establish byte
identity. Notes 24 and 29B also have recorded delivery/import distinctions.
The current work order supersedes bundled historical continuation proposals.

## Maintenance is not a scientific rerun

[NO_QRAM_MAINTENANCE.json](NO_QRAM_MAINTENANCE.json) records this pass's starting
revisions, allowed documentation changes, attachment checks, and navigation scope.
[MAINTENANCE.json](MAINTENANCE.json) remains the earlier immutable maintenance
record. No scientific program, new theorem, hardware test, or performance study
is executed by this update. A future rerun should record its command, commit,
interpreter, package/thread settings, exit status, output path, and comparison
method while preserving the old report.
