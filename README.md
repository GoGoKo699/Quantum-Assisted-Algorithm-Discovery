# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Phase 4: model-first exploration. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

Direct samples are permitted; a reusable classical program is optional. Essential
preparation, input, accuracy and output costs remain explicit. See [AGENTS.md](AGENTS.md).

## Current result and decision

[Task-matched readout 02](exploration/phase_4/TASK_MATCHED_READOUT_02.md) tests the
physical-acquisition candidate from [Screen 01](exploration/phase_4/MODEL_MECHANISM_SCREEN_01.md).
For a supplied signal template and calibrated nuisance shapes, a single chosen
quadrature per temporal mode reproduces the nuisance-insensitive amplitude
statistic. Under the stated pure-loss model, squeezed homodyne is less noisy than
the symmetric two-mode-squeezed Bell scheme at matched photon budgets, even with
unequal signal/reference losses. Squeezed homodyne is unentangled, not classical light.

This does not solve unknown, drifting nuisance inference or refute quantum-dense
metrology. Calibrating the shapes and controlling the measurement angles can be
substantial tasks; their costs are not declared free in a real experiment. The
comparison supplies no new entangled-sensing or general-purpose circuit advantage.
Physical-source access remains a separate proposed input model, not a replacement
of the original classical-input objective.

Sensing is retained as a scope-separated reference. The [next work order](work_orders/CURRENT.md)
returns to the shortlisted graph-sparsification question: useful implicit inputs,
coherent access and memory costs, and strong classical graph construction. No
new dataset, simulator, optical instrument or repository is requested.

## Evidence and navigation

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/task_matched_readout_v1/verify.py
```

Python 3.10+, SymPy and NumPy. The [saved report](experiments/task_matched_readout_v1/REPORT.json)
contains exact finite regression identities and six analytic loss/energy controls,
not physical samples or performance data. Two identical runs; no historical suite
rerun. The [phase-4 index](exploration/phase_4/README.md), [status](STATUS.md),
[preserved handover](HANDOVER.md), and [phase-3 archive](exploration/phase_3/README.md)
retain the decisions and evidence. The activity-covariance lead remains closed.

The research branch name `research/prx-quantum-phase2` is historical. Main remains
a routing entry. Earlier science, source/report pairs, both independent spin-offs,
and the original [MIT license](LICENSE) are preserved. Only this parent is writable.
