# Quantum-Assisted Algorithm Discovery — exploration phase 2

**Active branch: `research/prx-quantum-phase2`. Target: PRX Quantum.
Manuscript: on hold.**

Can circuit-model quantum computation discover compact classical information
that supports a useful reusable method? The provisional task is an exact local
Weil polynomial for an explicitly specified odd-degree hyperelliptic curve.
The polynomial supplies a classical recurrence for later extension counts.
The general quantum zeta algorithm is prior work. No useful quantum/classical
crossover or publication-ready contribution is established.

Start with the [phase-2 charter](exploration/phase_2/CHARTER.md),
[family and translation-cost analysis](exploration/phase_2/FAMILY_AND_TRANSLATION_COST_25.md),
and [current scientific work order](work_orders/CURRENT.md).

## Current result

The mathematical task now has an explicit source-aware comparison: classical
point counters may bypass Jacobian order finding entirely. Fixed genus, small
characteristic, algebraic structure and batching each permit important classical
methods. Large extension fields alone are not quantum-hardness evidence.

For the retained quantum route, Note 25 supplies a constructive asymptotic bound
for controlled GENERAL Jacobian translation, including canonical validity,
exceptional cases, unused encodings and clean uncomputation. Its store-all-history
workspace is charged. This is not a compiled circuit or a physical resource claim.
The next step is a matched numerical cost comparison on independently sourced
curves, not another generic polynomial-time theorem or tiny-group census.

```sh
python experiments/translation_cost_v1/verify.py
python experiments/subgroup_stop_v1/verify.py
```

The first checks arithmetic in the cost analysis, not a quantum circuit. The
second preserves [certified subgroup stopping](exploration/phase_2/SUBGROUP_CERTIFIED_STOPPING_24.md):
accept only a unique multiple of a computed subgroup size in the rigorous ambient
interval. Both methods and their deductions are available to the classical side.

## Preserved work

`main` and `research/sharing-core-publication` retain the earlier investigations.
Sorting, arithmetic-synthesis and e-graph results are background evidence, not
compulsory Phase-2 targets. The inherited [claim ledger](STATUS.md) concerns those
earlier investigations; current decisions are in the work order and numbered
notes. Historical source, result and third-party license files are unchanged.
The separate Algebraic-Loop-Certificates project is not developed or counted as
quantum-advantage evidence here.

Original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, unchanged.
