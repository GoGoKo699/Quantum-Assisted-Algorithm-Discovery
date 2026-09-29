# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Phase 4: model-first exploration. Manuscript preparation remains on hold.**
No end-to-end application advantage has been established. Direct useful samples
and reusable classical outputs are permitted; input, accuracy and memory costs count.

## Current derivation: sparsification with output-scale working memory

[Short-seed sparsification 04](exploration/phase_4/SHORT_SEED_SPARSIFICATION_04.md)
integrates bounded-independence sampling with both stages of the existing quantum
sparsifier. It proves the required graph property rather than emulating the exact
fully independent output law. Fresh seeds are chosen after each current graph
and spanner bundle are fixed; they remain fixed during quantum queries.

Under the original finite-word coherent-access model, the derived upper bounds
are time approximately sqrt(mn)/epsilon and additional coherent working memory
approximately n/epsilon^2, up to logarithms. Point/graph input storage is separate.
The result removes the larger random-tape emulation structure, not all QRAM or
arbitrary lookup costs. Output, spanners, resistance data, precision and search
bookkeeping remain charged. The explicit hash implementation uses polylogarithmic
active quantum scratch, not a claimed preservation of the source's exact logarithmic
active-qubit count.

This is an internally derived algorithmic refinement using established matrix
moment, bounded-independence, spanner and quantum-search methods. Publication
priority and an independent proof audit are unresolved. It is not a compiled
quantum implementation, measured speedup, or demonstrated learning improvement.
The [current task](work_orders/CURRENT.md) requests a focused audit and useful-input
resource comparison, not a new randomness library or a third spin-off.

## Evidence and navigation

```sh
python experiments/short_seed_sparsification_v1/verify.py
```

Python 3.10+, standard library only. The [report](experiments/short_seed_sparsification_v1/REPORT.json)
records exact finite field, trace-moment, rounding and adaptive-seed checks.
The final checker ran twice identically and rejected -O/-OO and six invalid inputs.
No quantum search, spanner implementation, large sparsifier, dataset benchmark or
historical scientific suite was run. The general claim follows from the written
integration of cited theorems, not an empirical success rate on small graphs.

[Phase-4 index](exploration/phase_4/README.md) · [Status](STATUS.md) ·
[Handover](HANDOVER.md) · [Phase-3 archive](exploration/phase_3/README.md)

[Implicit graph 03](exploration/phase_4/IMPLICIT_GAUSSIAN_GRAPH_03.md) retains the
harmonic-learning contract and classical shortcuts. Compact input is not free
coherent input; a hard sparsifier instance need not be a useful learning instance.
Sensing remains scope-separated, stopping power a reserve, and the activity-
covariance closeout remains in force. Only this parent repository is modified.
All previous science, the independent spin-offs, and [LICENSE](LICENSE) are preserved.
