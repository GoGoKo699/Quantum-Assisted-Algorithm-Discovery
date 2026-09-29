# Reproducing the evidence

[Handover](../HANDOVER.md) · [Research index](../exploration/phase_3/README.md)

**There is no single all-project test and no claim that these scripts demonstrate
quantum advantage.** Select the evidence you intend to check. Never overwrite a
saved report with output from a new environment.

## Obtain the correct branch

```sh
git clone https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery.git
cd Quantum-Assisted-Algorithm-Discovery
git switch research/prx-quantum-phase2
git rev-parse HEAD
```

The research evidence is not all present on `main`. For the immutable scientific
closeout, use commit `a286ba415b0550db837e9c8144b80c4f21909d82` in a separate worktree
or checkout; later handover documentation is not part of that older snapshot.
Do not force-reset a working tree with uncommitted work.

## Environment and output discipline

Recent emitter checks declare Python 3.10+ with NumPy and SciPy. The last successful
29B closeout replay recorded NumPy **2.3.5** and SciPy **1.17.0**, with one BLAS
thread; see [the original manifest](../provenance/activity_closeout_30.json).
Use an interpreter supported by those pinned packages. The handover does not
claim to have freshly installed or tested every interpreter/package combination.
Other historical suites have different requirements; consult their source headers.

Example isolated setup, when the dependencies are not already available:

```sh
python3 -m venv /tmp/qaad-handover-venv
. /tmp/qaad-handover-venv/bin/activate
python -m pip install 'numpy==2.3.5' 'scipy==1.17.0'
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
OUT=$(mktemp -d)
python -VV
python -c 'import numpy, scipy; print(numpy.__version__, scipy.__version__)'
```

Package installation needs network access; none is required by the self-contained
recent checkers after setup. Never use `python -O` or `python -OO`. They disable
assertions; the guarded checkers reject those modes. Keep regenerated outputs in
`$OUT`, not over versioned `REPORT.json` files. Floating arithmetic, library versions,
and BLAS differences can change final decimals. A byte mismatch is a reason to
inspect numerical tests and provenance, not to replace the reference until it passes.

## The closed activity claim: two separate reproductions

**Note 29 — original acquisition; windows 1, 4, 16.**

```sh
python experiments/activity_acquisition_v1/verify.py > "$OUT/activity-29.json"
```

Compare with [its saved report](../experiments/activity_acquisition_v1/REPORT.json)
and [method note](../exploration/phase_3/CLASSICAL_ACTIVITY_ACQUISITION_29.md).
It acquires the small model from the specified seven-emitter generator and checks
it against the full invariant-sector contraction. It is not a trajectory fit.

**Note 29B — separate cross-check; windows 1, 5, 20.**

```sh
python experiments/activity_acquisition_crosscheck_v1/verify.py > "$OUT/activity-29B.json"
```

Compare with [its saved report](../experiments/activity_acquisition_crosscheck_v1/REPORT.json)
and [method note](../exploration/phase_3/CLASSICAL_ACTIVITY_CROSSCHECK_29B.md).
It includes additional full-space and tilted-mode controls. Its source and report
were imported byte-for-byte; Closeout 30 records a successful replay. Do not merge
its rows with Note 29 or count the implementations as independent experiments.
These sparse matrix calculations are more substantial than the small identity
checks below. They are opt-in reproductions, not part of opening the repository.

## Supporting emitter checks

| Note | Command, from the research root | What it tests |
|---|---|---|
| 25 | `python experiments/record_instrument_v1/verify.py` | Count-labelled instrument identities and finite discretization controls |
| 26 | `python experiments/emission_memory_v1/verify.py` | Excitation-cutoff, moment, and renewal controls |
| 28 | `python experiments/activity_flags_v1/verify.py` | Exact flag/tilted-law identities and elementary classical controls |

These require NumPy/SciPy, not experimental data or a quantum device. General
all-size statements belong to the written proofs, not extrapolation from finite
checks. Successful exit does not establish publication priority, physical adequacy,
a complete proof audit, quantum hardware performance, or a best-classical separation.

## Other scientific evidence

The [phase-3 index](../exploration/phase_3/README.md) pairs the spectral, sampling,
and climate notes with their experiment directories. Read the applicable note and
source header before running a historical suite. A directory is not a dependency
of every other experiment; there is no reason to install every optional solver.
The [phase-2 index](../exploration/phase_2/README.md) separates older exploration
from the current objective and the two independent spin-offs.

The repository-root command has a narrower purpose:

```sh
python verify.py
```

It checks the 18 original guided-search imports, regenerates the known reference
in a disposable directory, and runs the guided-core checks. It does **not** verify
all later spectral or emitter work. Its optional `--quick` and `--full` modes also
require a C++17 compiler and perform additional historical runs; do not invoke them
as a routine documentation check. `verify_target_closure.py` is likewise a separate
historical scope. Optional native-Z3, NetworkX, and other comparisons belong only
to the suites that explicitly request them.

## External inputs and rights

The battery archive checker requires the authors' external `paper_data.zip`:

```sh
python experiments/reference_archive_v1/verify.py --archive /path/to/paper_data.zip
```

[Archive replay 04](../exploration/phase_3/ARCHIVE_REPLAY_04.md) records provenance,
expected digests, and what was reproduced. The checker reads the ZIP without
turning it into a training dataset. It is not redistributed or relicensed here.
The earlier uploaded archive is not an unresolved request for another upload.

[Climate audit 13](../exploration/phase_3/CONTINUATION_INFORMATION_13.md) records
the missing ancestry/continuation data and its exact source-file list. The data
block only that empirical test, not model-first exploration. Do not claim its
sibling-continuation statistic has been measured. Finite probability-law checkers
in Notes 11–12 are not a CESM run.

[PROVENANCE.md](../PROVENANCE.md), the manifests in `provenance/`, and experiment
source notices retain the rights and import scope. The root MIT license does not
override separately attributed third-party material.

## Alternate checkpoints

Two different documents used the number 24. The repository's canonical
[Note 24](../exploration/phase_3/SAMPLING_REGIME_DECISION_24.md) concerns fair reuse
and the move to physical records. The conversation's smooth spectral-cache version
is separate historical material, not a replacement work order. Its source archive
and exact payload identities are recorded in
[the alternate-checkpoint register](ALTERNATE_CHECKPOINTS.md).

The old local-delivery wording in Note 29B remains historical. Its later repository
import is established by Closeout 30 and `provenance/activity_closeout_30.json`.
Paths, titles, or equal note numbers do not establish byte identity; use the recorded
hashes. Never apply an old checkpoint's bundled patch or next-step file over current
routing merely because its science is being inspected.

## Maintenance versus scientific validation

This handover checks navigation and preservation, not the numerical suites. The
maintenance record lists the starting commits and exact scope. No continuous
integration workflow is added and no CI pass is claimed by this handover. To report a new
scientific rerun, record the command, interpreter, packages, thread settings,
exit status, output location, and comparison method; retain the previous report.
