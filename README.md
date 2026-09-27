# Quantum-Assisted Algorithm Discovery — exploration phase 2

**Active branch: `research/prx-quantum-phase2`. Target: PRX Quantum.
Manuscript: on hold.**

Can circuit-model quantum computation discover compact classical information
that supports a useful reusable method? The provisional example is the exact
local Weil polynomial of an explicit hyperelliptic curve. It supplies the
coefficients of a known classical counting recurrence; the general quantum
zeta capability is established prior work, not this project's discovery.
No useful quantum/classical crossover is established.

Start with the [phase-2 charter](exploration/phase_2/CHARTER.md),
[source-aware descent comparison](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md),
and [current work order](work_orders/CURRENT.md).

## Latest comparison

The ordinary group-order requests can use the same smaller-field computation
as the signed/twist route: apply the known identity K_(2n)=K_n*T_n and reuse
computed values. After this classical preprocessing, the two routes have the
same underlying curve/twist order calls. Thus Note 26's degree-weighted ratios
measure a comparison with an **unsplit** ordinary backend, not with every
source-aware quantum implementation. This is not a classical simulation of
quantum group-order finding and does not disprove the general quantum capability.

The [focused diagnostic](experiments/descent_baseline_v1/README.md) tests the call
normalization and a finite-field counterexample to confusing equality of group
cardinalities with a direct-product decomposition of quantum group registers.
The exact reconstruction theorem remains useful; its precise priority in the
restricted ordinary-query model is a separate, unresolved question.

```sh
python experiments/descent_baseline_v1/verify.py
python experiments/reconstruction_comparator_v1/verify.py
python experiments/translation_cost_v1/verify.py
python experiments/subgroup_stop_v1/verify.py
```

These are exact component checks, not quantum-hardware or native application
benchmarks. [General-translation arithmetic](exploration/phase_2/FAMILY_AND_TRANSLATION_COST_25.md)
and [subgroup-certified stopping](exploration/phase_2/SUBGROUP_CERTIFIED_STOPPING_24.md)
remain preserved supporting results. All allowed deductions and source information
must be available to the classical competitor, which may bypass group orders.

## Preserved work

`main` and `research/sharing-core-publication` retain the earlier investigations.
Sorting, arithmetic synthesis and e-graph results are background evidence, not
compulsory Phase-2 targets. The inherited [claim ledger](STATUS.md) concerns those
earlier investigations; current decisions are in the work order and numbered
notes. Historical sources, results and third-party notices remain unchanged.
The separate Algebraic-Loop-Certificates project is not developed or counted as
quantum-advantage evidence here. No further spinoff is currently requested.

Original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, unchanged.
