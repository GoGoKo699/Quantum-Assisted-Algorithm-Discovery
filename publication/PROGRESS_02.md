# Publication checkpoint 2: cycle obstacle resolved with a budget parameter

25 September 2026. Additive continuation of draft PR #1; no sorting-work changes.

## Candidate central claim, now precise

For explicit weighted equality graphs with cyclic alternatives, selecting local cost caps at the shared boundary and taking a grounded least fixed point exactly characterizes the existence of a qualifying acyclic extraction. This eliminates construction-order guessing and exponential-table access. The generic quantum corollary searches binomial(K+s,s) allocations in square-root time with polynomial workspace.

The theorem section is drafted in BUDGET_THEOREM.tex. The full proof/model and code are in experiments/budget_grounding_v1. It is a candidate contribution, not a claim of priority or publication readiness.

## What moved

Gate 2: complete asymptotic cyclic decision algorithm with cost/addressing accounting; exact polynomial-time integer unranking; compiled binary-cap compute/phase/uncompute marker. Cap unranking and outer search are not gate-count compiled. All 8,374 cap checks and 4,174 basis-marker tests pass. The older 1,790 feasible witnesses also transfer exactly. The cycle requiring one cost-ten seed no longer obtains a fictitious free answer.

Gate 1: primary comparison confirms established weighted cyclic monotone-circuit extraction, treewidth methods, and circuit simplification. Quantum exponential-DP work also has QRAM/time-space assumptions. The new bound does NOT automatically dominate these methods. An independent novelty/classical-complexity comparison is still required.

Gate 3: not advanced. No new large native extractor benchmark was run; retrieval to the execution environment failed. The one pinned public calibration remains classically trivial and the budget representation is worse there. Do not represent the code tests as workload evidence.

## Falsifiable next task

Retain this branch's scope. Audit whether budget-grounded private/core compilation is subsumed by existing AND/OR, weighted monotone-circuit, or extraction algorithms. Compare the minimum of (a) representative enumeration, (b) subset DP, (c) classical budget search with dominance pruning, and (d) applicable treewidth/native extraction methods, with symmetric memory assumptions. Identify a parameter family not immediately solved by a stronger existing method. A generic square-root bound is not enough.

Address cost-grid dependence explicitly: normalize common factors, identify equivalent caps where possible, and do not infer difficulty from duplicated allocations. A qualifying program threshold, not an unnecessary global-optimality proof, is the task. Only after this comparison should the full compact-index quantum circuit and benchmark program be expanded.

A theory-led paper remains possible without hardware or a new multiplication record. It still needs an original result and a meaningful comparative regime. Do not turn this checkpoint into a disconnected methods paper merely to claim publication progress.
