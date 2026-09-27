# Source-aware quadratic-descent baseline

This focused diagnostic accompanies [Note 27](../../exploration/phase_2/SOURCE_AWARE_DESCENT_27.md).
It tests one comparative question: can the ordinary requests of Note 26 use the
same actual smaller-field group-order calls as the signed route? Applying the
established K_(2n)=K_n*T_n identity with reuse answers yes in the explicit-source,
odd-characteristic hyperelliptic setting. No quantum order value is provided free.

```sh
python experiments/descent_baseline_v1/verify.py
```

Python 3.10 or later, standard library only. Do not use `-O` or `-OO`.
The verifier checks hashes and reproduces REPORT.json in temporary storage,
without overwriting expected results. There are no imported runtime dependencies.

`descent.py` constructs a classical dependency plan and evaluates supplied integer
leaves. It is not a group solver, a curve recognizer or a quantum circuit compiler.
The leaf label T(n) means a FRESH twist over the degree-n field. Actual curve source,
field construction, correctness of the supplied orders, quantum subroutine costs
and error budgets are outside this diagnostic and must be supplied by a workflow.

`checks.py` verifies 64 matched schedules, 3136 scalar products by independent
chain expansion, 255 nonempty subsets of degrees 1..8, ten malformed cases, and
one elliptic counterexample to replacing cardinality multiplication with a group
or quantum-register direct product. It directly enumerates points over F_5 and
F_25 and the twist embedding. Higher extension orders in the plan controls are
calculated by a known quadratic recurrence, not by enumerating further fields.
The small nonsplitting example is not a proposed hard quantum workload.

Base branch commit: bc62cdcad7927475d40c452112d12af1ed40693c.
No previous source/result file is edited. The three prior current verifiers passed
unchanged. Root historical and 164-curve tests were not rerun, and no native large
point counter, quantum group circuit or hardware was executed. See SOURCES.md for
source scope and the distinction between a comparator correction and a priority
claim for the separate reconstruction theorem. No spinoff is requested.
