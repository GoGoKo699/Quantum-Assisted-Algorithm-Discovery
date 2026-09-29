# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Phase 4: model-first exploration. No new useful quantum advantage is established.
Manuscript preparation remains on hold.**

Direct samples are allowed; a reusable classical program is optional. Essential
preparation, access, accuracy, and output costs remain explicit. See [AGENTS.md](AGENTS.md).

## Current candidate: an implicit graph with a reusable classical output

[Implicit Gaussian graph 03](exploration/phase_4/IMPLICIT_GAUSSIAN_GRAPH_03.md)
examines Gaussian similarity graphs for harmonic label propagation. The input is
a point table, not a quadratic edge list. A spectral sparsifier is a small classical
graph reusable across label/energy queries; it does not require later quantum use.
The known quantum sparsification algorithm is prior work, with explicit coherent
input and working-memory assumptions.

This candidate has a substantive conditional worst-case classical obstacle from
closest-pair reductions, not merely a dense-matrix dimension. But broad kernels
already admit an inexpensive classical sampler, geometric/kernel algorithms can
be stronger, and the hard bandwidth need not be useful for learning. Neither
conditional hardness nor an ideal-RAM quantum upper bound establishes a practical
advantage. Coordinate precision, input loading and coherent memory are priced.

The [current task](work_orders/CURRENT.md) targets a specific possible improvement:
can the existing quantum algorithm use shorter random seeds by proving sparsifier
correctness instead of emulating an entire independent random output law?
Bounded-independence sparsification is existing classical theory. Its adaptive
quantum integration and resulting full memory/time budget are NOT established
here; reducing random storage would not remove input QRAM.

## Evidence and navigation

```sh
python experiments/implicit_graph_contract_v1/verify.py
```

Python 3.10+, standard library only. The [report](experiments/implicit_graph_contract_v1/REPORT.json)
contains exact finite arithmetic controls for the input/accuracy contract, not a
quantum sparsifier, experimental dataset, hardness test or performance comparison.
The final checker ran twice identically; no older scientific suite was rerun.
The general facts are derived or attributed in the note, not inferred from a
small graph. No new repository or third spin-off is needed.

[Phase-4 index](exploration/phase_4/README.md) · [Status](STATUS.md) ·
[Handover](HANDOVER.md) · [Phase-3 archive](exploration/phase_3/README.md)

[Readout 02](exploration/phase_4/TASK_MATCHED_READOUT_02.md) remains a separate-input
sensing reference, not a no-go for unknown-waveform sensing. Electronic stopping
is a reserve. The emitter activity-covariance closeout remains in force. The active
branch name `research/prx-quantum-phase2` is historical; main routes to this work.
Earlier source/report pairs, the two independent spin-offs, and the original
[MIT license](LICENSE) are preserved. Only this parent repository is writable.
