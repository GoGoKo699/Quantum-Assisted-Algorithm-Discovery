# Current status

29 September 2026 — phase-4 short-seed integration.

[Note 04](exploration/phase_4/SHORT_SEED_SPARSIFICATION_04.md) derives a conditional
algorithmic memory refinement of the Apers/de Wolf quantum sparsifier. Both the
implicit rough spanner stage and the refined resistance stage use fresh
logarithmic-wise independent selectors. The moment proof establishes spectral
correctness and edge-count tails directly, not equality of the full output law.

In the original finite-word adjacency/coherent-RAM model, the derived time is
approximately sqrt(mn)/epsilon and additional coherent working storage is
approximately n/epsilon^2, up to logarithms. Input storage, coherent lookup,
finite-weight arithmetic, spanners, resistance data, output and search bookkeeping
remain. Hash evaluation adds polylogarithmic reversible work and scratch, not a
new large random-memory table. No QRAM-free or constant-hardware assertion is made.

The independent-copy symmetrization, adaptivity conditioning, probability rounding,
cardinality caps and failure events are explicit. Bounded independence and the
other primitives are prior methods. The exact composition's publication priority
and independent proof audit are unresolved. No experimental or end-to-end useful
quantum advantage is established. Manuscript preparation remains on hold.

## Executed scope

The standard-library checker ran twice with identical JSON. It verifies finite
field hashing and threshold marginals, noncommutative trace-moment equality,
round-up/reweighting, and implicit-layer replay. Negative controls detect seed
reuse and choosing the next graph after its seed. Different sixth moments show
that matching the needed lower moments does not reproduce the full law.
Six invalid inputs and -O/-OO were rejected. The [report](experiments/short_seed_sparsification_v1/REPORT.json)
contains exact arithmetic, not random performance trials. No quantum sampler,
spanner implementation, large graph, classification dataset, hardware or historical
verifier was run. General guarantees rely on the proof and cited subroutines.

Primary source text for quantum sparsification, bounded independence and matrix
moments was inspected. Requested PDF screenshots failed; no figure/table results
were interpreted. Focused searches did not establish novelty. The source record
and all assumptions are in the note.

## Continuation and preservation

The [work order](work_orders/CURRENT.md) calls for a focused audit and a useful
input/resource comparison, not repeated generic certificate development. The
Gaussian label-accuracy and strong-classical boundaries of Note 03 remain binding.
The local plural-filename Note 03 is distinct from the committed singular-filename
note that selected the short-seed hypothesis. Neither is rewritten here.

The [preceding ledger](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/288eedadc67c283f9fb1cce4b942e8c780eb43ec/STATUS.md)
retains prior decisions. All earlier scientific files, handover, licenses and
third-party rights are unchanged. Only the parent repository is modified; no
new repository, third spin-off, branch merge, release, contact or paid work follows.
