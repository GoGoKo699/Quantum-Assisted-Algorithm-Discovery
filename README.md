# Quantum-Assisted Algorithm Discovery — exploration phase 2

**Active branch: `research/prx-quantum-phase2`. Target: PRX Quantum.
Manuscript: on hold.**

Can circuit-model quantum computation discover compact classical information
that supports a useful reusable method? The current provisional candidate uses
Jacobian cardinalities to reconstruct a curve's zeta function. The general
quantum zeta algorithm and the classical group-order ingredients are prior work;
no useful quantum advantage or publication-ready contribution is established.

Start with the [phase-2 charter](exploration/phase_2/CHARTER.md),
[latest subgroup-stopping result](exploration/phase_2/SUBGROUP_CERTIFIED_STOPPING_24.md),
and [current scientific work order](work_orders/CURRENT.md).

## Current result

A sampled list need not generate the whole group before an exact cardinality
can be accepted. Count the subgroup it actually generates, then accept only when
the rigorous ambient interval contains one multiple of that subgroup size.
Otherwise remain inconclusive or use the established fallback. The result
refines the premises of [bounded cofactor completion](exploration/phase_2/EXPONENT_FIRST_CARDINALITY_COMPLETION_23.md);
it does not establish cheaper quantum order finding.

The [standalone diagnostic](experiments/subgroup_stop_v1/README.md) includes its
source, exact report, manifest and verifier:

```sh
python experiments/subgroup_stop_v1/verify.py
```

This tests supplied abstract groups, including incomplete lists. It is not a
curve sampler, quantum order finder, complete gate estimate or native benchmark.
The next gate is a justified useful family and a complete comparison of the
remaining period acquisition with strong classical methods.

## Preserved work

`main` and `research/sharing-core-publication` retain the earlier investigations.
Their sorting, arithmetic-synthesis and e-graph results are background evidence,
not compulsory Phase-2 targets. The inherited [claim ledger](STATUS.md) records
those earlier investigations; current Phase-2 decisions are in the work order
and numbered notes. Historical source, result and third-party license files
are unchanged. The separate Algebraic-Loop-Certificates project is not developed
or counted as quantum-advantage evidence here.

Original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, unchanged.
