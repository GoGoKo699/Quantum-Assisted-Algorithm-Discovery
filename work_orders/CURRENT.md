# Current task: audit the short-seed refinement and its useful resource consequence

29 September 2026. Branch: `research/prx-quantum-phase2`.
Read [Note 04](../exploration/phase_4/SHORT_SEED_SPARSIFICATION_04.md),
[the committed graph contract](../exploration/phase_4/IMPLICIT_GAUSSIAN_GRAPH_03.md),
and [AGENTS.md](../AGENTS.md). No new repository is needed. Manuscript stays on hold.

## Derived result to audit, not merely a final-stage substitution

Both stages of the existing quantum sparsification algorithm can use logarithmic-
wise independent sampling, with a fresh seed drawn after the current graph and
bundle/importance data are fixed. The proof matches a finite trace moment and
uses a separate count tail; it does not emulate every random-oracle transcript.
An independent-copy symmetrization explicitly supplies the distributional symmetry
required by the cited matrix moment inequality. A fixed sampled graph is a valid
input for quantum search and spanner construction even though its edges are not
fully independent. Conditioning on an already-used seed is not allowed.

Rough sampling uses spanner packings with enlarged logarithmic constants and
fixed total rough accuracy. Retain old seeds and bundles for implicit replay; do
not materialize the dense intermediates. Final sampling uses upper resistance
estimates, rounded-up probabilities and reweighting by the ACTUAL probability.
Output caps, subroutine failure, numerical graph error, final rounding and searches
are counted. The approximation success event is sufficient for all later graph
energy queries; independent-edge output samples are not the required product.

In the source finite-word RAM model, the resulting internally derived bounds are
~sqrt(mn)/epsilon time and ~n/epsilon^2 additional coherently accessible working
bits, excluding the supplied point/graph input. The random seeds alone have
polylogarithmic size. The input lookup, spanner/resistance/output storage, active
hash scratch, finite arithmetic and hardware error correction are NOT eliminated.
A small active quantum register is not the total physical memory. No quantum
implementation or empirical speedup has been run.

## One focused next decision

Check the exact two-stage integration against published quantum sparsification
and bounded-independence work. Verify its subroutine time/space promises and the
fresh-seed conditional proof. The finite checker is not an independent proof audit
and no claim of publication priority follows from a bounded search. If the same
refinement is already known, record that provenance and do not present it as new.

Then state one complete resource comparison for compact Gaussian point input at
a bandwidth and prediction tolerance that an actual learning task needs. Separate
input ingestion and point lookup from the saved randomness storage; price the
strongest adequate geometric/kernel construction or direct prediction bypass.
At fixed broad kernels, classical sampling can already be near linear. A minimum
weight or a worst-case universal-sparsifier reduction alone is not evidence that
useful predictions require difficult connectivity. Reuse benefits both sides.

A meaningful theoretical memory saving can merit study without a hardware demo
or universal classical lower bound. It does not by itself prove a practical
learning gain. Do not open a hash library, a spanner framework, a large census,
a new QRAM architecture, a dataset hunt or a third spin-off just to extend the note.
Keep the positive quantum mechanism and its useful consequence in one argument.

## Evidence and boundaries

The new standard-library exact checker ran twice identically, with -O/-OO and
six invalid inputs rejected. It checks finite polynomial hashing, trace moments,
probability rounding and layered replay, with explicit invalid-seed controls.
It does not run quantum search, a quantum spanner, a large sparsifier, a classifier,
a circuit, or a hardware benchmark. Older scientific verifiers were not rerun.
Only Quantum-Assisted-Algorithm-Discovery may be modified. Preserve existing
notes, code, reports, provenance and rights; no outside contact, paid/unattended
work, manuscript revival, branch merge, release or administration change.
