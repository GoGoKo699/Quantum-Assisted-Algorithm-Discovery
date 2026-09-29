# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Phase 4: fresh model/mechanism comparison. No useful quantum advantage is established. Manuscript preparation remains on hold.**

Direct quantum samples are permitted; a reusable classical program is optional.
Model-level reasoning comes before implementation, with preparation, input access,
accuracy, validation and output costs retained. See [AGENTS.md](AGENTS.md).

## Current exploration

[Screen 01](exploration/phase_4/MODEL_MECHANISM_SCREEN_01.md) compares three
independently motivated possibilities: reusable graph sparsifiers, electronic
energy-deposition calculations, and better acquisition of physical signals.
The first two retain classically specified computational inputs. Physical signal
learning instead accesses an unknown source before measurement; it is explicitly
a proposed different input model, not a claimed speedup on supplied classical data
or a silent replacement of the circuit-model objective.

The next bounded check examines whether a useful joint signal diagnostic benefits
from quantum-assisted acquisition after energy, loss, calibration and optimized
unentangled readout are matched. Existing quantum-dense metrology and quantum
signal-learning results are prior work, not our contribution. Simple rotated
measurements are retained as an important bypass. No new sensor or simulator is
being built, and no input-model extension is treated as an established result.
Graph sparsification remains the closest shortlisted fit to the original goal.

## Navigation

| Read | Purpose |
|---|---|
| [Phase-4 index](exploration/phase_4/README.md) | Fresh screen and its scope |
| [Current work order](work_orders/CURRENT.md) | One active comparison, not three parallel tasks |
| [Status](STATUS.md) | Current limits and pinned earlier ledger |
| [Handover](HANDOVER.md) | Preserved starting snapshot and history |
| [Phase-3 index](exploration/phase_3/README.md) | Previous scientific notes and evidence |
| [Reproduction guide](handover/REPRODUCING.md) | Scope of historical checkers and external inputs |

The activity-covariance lead remains closed on present evidence; see
[Closeout 30](exploration/phase_3/ACTIVITY_CLAIM_CLOSEOUT_30.md). It is not reopened
by this restart. The handover's unselected-next-phase wording is historical.
No old scientific verifier was rerun in the new source/model screen.

The working branch remains `research/prx-quantum-phase2`; its name is historical.
`main` is a routing entry, not a merged research copy. Both classical spin-offs
retain their independent projects. Earlier notes, code, reports, rights and the
original [MIT license](LICENSE) are preserved. Only this parent repository may be
modified; no new repository, manuscript, release or branch merge is required.
