# Current task: a matched numerical cost test, not another polynomial bound

Active branch: `research/prx-quantum-phase2`. Target: **PRX Quantum**.
Manuscript preparation remains **on hold**. No submission deadline is imposed.
Read the phase-2 charter and `exploration/phase_2/FAMILY_AND_TRANSLATION_COST_25.md`.

## Boundary and preserved capability

Modify only Quantum-Assisted-Algorithm-Discovery. Preserve other branches,
historical sources/results and LICENSE. The classical spinoff remains separate.
Do not merge the earlier sharing-core PR or revive its manuscript here.

Retain Notes 19-24: exact reconstruction and its prior-art boundary, the stronger
endpoint schedule where applicable, rank-aware generation, retained-register
character tuples, recycled control, initial-order reuse, bounded classical
completion and rigorous subgroup-divisor stopping. Incomplete samples are not an
error on an accepted interval-certified branch. All failures and fallback costs
remain charged; the classical competitor receives the same deductions.

## What Note 25 settles

Use the standard local-Weil-polynomial task for odd-degree hyperelliptic curves
as an explicit mathematical comparison contract. It is a useful compact invariant,
not a claim of a new application or a chosen hard benchmark. Both sides see the
same polynomial, prime, structural information, prior data and reuse allowance.

Classical fixed-genus, small-characteristic, real-multiplication and all-primes
methods remain admissible. A general point counter may bypass group orders.
Do not infer intrinsic hardness from an expensive generic group algorithm or
from a fixed-genus asymptotic theorem outside its stated uniformity/characteristic
conditions. Do not invent a curve promise solely to disable classical methods.

General controlled translation now has a conservative constructive bound
Otilde(g^3 n^2 b^2 + g n^3 b^3), with b=ceil(log2 p), including validity tests,
non-generic support and clean uncomputation. Store-all-history space is charged.
The inherited full schedule's translation component is
Otilde(g^10 b^3 + g^9 b^4). These are loose upper bounds without emitted gates or
numerical constants, not physical requirements, speedups or total-workflow costs.
Fast classical algebra and improved reversible implementations are allowed.

## Next decisive work

Choose a small, independently sourced collection of general curves in parameters
where a complete comparison is informative. Pin source bytes and define the same
exact output for all routes. Inspect or execute the appropriate native classical
point counter, preserving its documented preprocessing, precision and extra
structure; do not use only a generic order finder or a weak replacement solver.

For the same parameters, select an existing general-divisor arithmetic strategy
and obtain a defensible numerical gate/space bound. A focused arithmetic audit is
preferred to a general compiler. Account for all support/degree cases and invalid
encodings; genus-one or degree-one formulas cannot silently replace general
Jacobian translation. Keep the highest-degree extension calls and the stronger
current reconstruction schedule, not only the older Note 21 illustration.

Combine remaining setup, sampling, precomputed multiples, factorization/order
verification, phase/readout, integer postprocessing, completion, reconstruction
and failure/fallback costs before claiming a crossover. A large loose upper bound
proves neither viability nor nonviability. A smaller formal envelope is not by
itself a substantive new quantum result. If the selected regime supplies no
consequential benefit, preserve that conclusion and the wider compact-input
question rather than changing the comparator.

## Verification and actual scope

Run `python experiments/translation_cost_v1/verify.py` and
`python experiments/subgroup_stop_v1/verify.py`. Both passed this round. The first
checks source hashes and exact arithmetic; it is not a compiled group-law circuit.
The second reruns the unchanged supplied Note 24 checkpoint. Historical root and
164-curve verifiers were not rerun; a full checkout download failed. No native
large-curve counter, quantum order finder, hardware or paid computation was run.
Preserve expected reports. No manuscript revival, outside contact, unattended
work, unrelated merge or repository administrative change is authorized.
