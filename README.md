# Quantum-Assisted Algorithm Discovery — exploration phase 2

**Active branch: `research/prx-quantum-phase2`. Target: PRX Quantum.
Manuscript: on hold.**

Can circuit-model quantum computation discover compact classical information
that supports a useful reusable method? The provisional task is an exact local
Weil polynomial for an explicitly specified odd-degree hyperelliptic curve.
It supplies a known classical recurrence for later extension counts; the recurrence
itself is not a newly discovered algorithm. The general quantum zeta capability
is prior work. No useful quantum/classical crossover is established.

Start with the [phase-2 charter](exploration/phase_2/CHARTER.md),
[matched reconstruction comparison](exploration/phase_2/MATCHED_RECONSTRUCTION_COMPARATOR_26.md),
and [current scientific work order](work_orders/CURRENT.md).

## Current result

After the same pruning and endpoint completion, the fresh-twist and ordinary
base-change routes need the SAME number of cardinality calls. Their exact integer
transcripts are interconvertible. Twists replace degree-2n base-change queries
with degree-n queries, not fewer calls than an equally optimized comparator.
For the genus-ten illustration, both routes use 12 calls, with maximum degrees
16 and 8 respectively. These are query schedules, not observed speedups.

The [general-translation analysis](exploration/phase_2/FAMILY_AND_TRANSLATION_COST_25.md)
charges exceptional arithmetic, canonical encodings and uncomputation, but remains
a loose asymptotic construction rather than a compiled circuit. The new matched
comparison uses the same backend and error allocation on both sides. A substantive
complete-resource or capability claim is still needed before an implementation
campaign. The classical method may bypass group orders altogether.

```sh
python experiments/reconstruction_comparator_v1/verify.py
python experiments/translation_cost_v1/verify.py
python experiments/subgroup_stop_v1/verify.py
```

These verify exact diagnostics, not quantum hardware. The [subgroup-stopping rule](exploration/phase_2/SUBGROUP_CERTIFIED_STOPPING_24.md)
also remains available: accept only a unique multiple of a computed subgroup size
in the rigorous ambient interval. All deductions are available to classical methods.

## Preserved work

`main` and `research/sharing-core-publication` retain the earlier investigations.
Sorting, arithmetic synthesis and e-graph results are background evidence, not
compulsory Phase-2 targets. The inherited [claim ledger](STATUS.md) concerns those
earlier investigations; current decisions are in the work order and numbered
notes. Historical source, result and third-party license files are unchanged.
The separate Algebraic-Loop-Certificates project is not developed or counted as
quantum-advantage evidence here.

Original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, unchanged.
