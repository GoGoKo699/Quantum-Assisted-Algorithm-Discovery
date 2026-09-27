# Quantum-Assisted Algorithm Discovery — exploration phase 2

**Active branch: `research/prx-quantum-phase2`. Target: PRX Quantum.
Manuscript: on hold.**

Can quantum processing discover compact classical information that supports a
useful reusable method? The current provisional application is an exact Weil
polynomial, which specifies a known classical counting recurrence. The general
polynomial-time quantum zeta algorithm is prior work; no practical quantum
advantage or publication-ready new quantum algorithm is established here.

Read the [phase-2 charter](exploration/phase_2/CHARTER.md),
[all-field reconstruction theorem and audit](exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md),
and [current work order](work_orders/CURRENT.md).

## Current mathematical candidate

For genus g>=32 over EVERY finite field, put h=g-2. The exact ordinary Jacobian
counts at degrees 1..h and the even degrees through 2h suffice to reconstruct
the Weil polynomial in polynomial bit time. This is h+ceil(h/2)<2g selected
cardinality requests, with maximum requested degree 2g-4. For genus 32 it means
45 counts through degree 60, not the first 45 counts.

The decoder uses more of the already available low-degree data for Mobius
cancellation and rounds coefficients using Newton's congruence information.
Certified, range-reduced rational logarithms handle small fields. This removes
the previous large-field hypothesis from this high-genus RECONSTRUCTION theorem;
it does not supply a new small-field/characteristic-two quantum group backend.
The underlying proof ingredients are prior work. Publication priority of the
precise combined statement remains unresolved after a focused source comparison.

```sh
python experiments/all_field_reconstruction_v1/verify.py
```

The executable checks reconstruct supplied Weil polynomials, not newly counted
curves. The [source-aware comparator](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md)
still rules out the earlier twist-specific resource claim: an equally prepared
ordinary route may use the same smaller-field computations. The new theorem does
not reopen that closed comparison or prove minimum-query optimality.

## Preserved work and limitations

The preceding descent, reconstruction-comparator, translation-cost and
subgroup-stopping verifiers remain in their versioned directories. Their source
and report bytes are unchanged. `main` and `research/sharing-core-publication`
retain earlier investigations. The inherited [claim ledger](STATUS.md) covers
those earlier branches; current decisions are in the numbered notes and work order.

No new spinoff is opened. The next step is an independent proof-and-priority audit
of the all-field reconstruction statement, not a general arithmetic compiler or
a threshold-optimization exercise. Historical licenses and evidence are preserved.
The separate classical spinoff is not developed or counted as quantum evidence.

Original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, unchanged.
