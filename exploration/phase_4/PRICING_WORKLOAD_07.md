# Pricing workload 07: test the useful optimizer, not an isolated search oracle

30 September 2026. Baseline: `2680152c9a59c5556e4e44b9b64069219c4e6e0a`.
Branch: `research/prx-quantum-phase2`. Fault-tolerant circuits, no assumed QRAM;
manuscript remains on hold.

**Decision:** the first source-grounded pricing test supplies no quantum-advantage
case. Two classical root-column-generation policies both produce a verified optimal
48-bin solution, starting from a 49-bin greedy packing. Exact pricing has only
11,042 capacity-state relaxations per call. The candidate's generator is not hiding
rare useful columns in the nine actual fallback calls of the greedy-first policy.
A new circuit or a larger member of this fixed-capacity family is not the next step.
This is one bounded benchmark diagnosis, not a general classical tractability or
quantum runtime theorem. The circuit construction in [Note 06](CIRCUIT_NATIVE_PRICING_06.md)
remains hardware-admissible; application benefit and novelty remain unestablished.

## 1. Public input, native master solves, and an actual packing certificate

Use the FIRST listed instance `u120_00` of Falkenauer's uniform class in OR-Library
[1]: 120 items, integer capacity 150, total size 7,078. This is a published synthetic
benchmark, NOT operational factory data or a hand-selected hard pricing instance.
The 120 sizes are a normalized extraction from the primary text. Source reference
optimum 48 is metadata only: the algorithm never uses it. The source notice and
input hash are retained with the code. No BPPLIB or native solver source was copied.

Best-fit decreasing, with a deterministic index tie break, produces 49 bins. Every
feasible packing must use at least ceil(7078/150)=48 bins. Each final report includes
an explicit 48-bin assignment of ALL original item IDs. Integer checks confirm that
each item occurs exactly once and every load is at most 150. This is an exact
optimal-bin-count certificate independent of floating-point LP/MIP optimality flags,
the published answer, or complete root-LP convergence.

The restricted master is solved by SciPy's HiGHS dual-simplex interface [3]. Integer
recovery uses the native HiGHS mixed-integer solver [4], restricted to the current
column pool. The driver and knapsack routines are independently written. This is
not a run of a production branch-and-price package, a quantum simulation, or an
implementation of the strongest known lexicographic/stabilized pricer [2]. A simple
adequate classical method is enough to reject THIS benchmark as immediate evidence
for advantage; it does not establish that stronger methods are necessary elsewhere.

## 2. An exact classical reduction before comparing hardware

Equal-size items are interchangeable in this ROOT problem. The 120 items have 58
size types, with sizes w_t and counts m_t. A type pattern satisfies

$$
0\leq y_t\leq m_t,\qquad y_t\in\mathbb Z,\qquad
\sum_t w_ty_t\leq150.
$$

The master covers m_t items of each type. This is an exact symmetry reduction of
the original binary root LP and integer packing problem, NOT a substitution of
unbounded cutting stock. No pattern can use more copies than the input contains.

For the LP equivalence, map binary patterns to their type counts in one direction.
In the other, distribute a type-pattern coefficient equally over every choice of
its y_t distinct items within each type. Each item of type t then receives coverage
y_t/m_t, so type coverage m_t ensures original-item coverage one. This is an existence
argument; the algorithm need not expand that exponential collection. For an integer
cover, assign concrete items to the selected pattern slots and delete surplus slots.
Every bin remains feasible and all items can be assigned. The report performs this
assignment explicitly. Root exchangeability is lost under item-specific branching
constraints or other metadata, so the reduction is not automatically a branch-node
algorithm. Ordinary type aggregation is prior optimization practice, not novelty.

Both policies start with 100 distinct type columns: the type singletons and patterns
from the same greedy packing. There is no supplied phase model, fabricated dual
vector, quantum-addressable table, or favorable known solution.

## 3. Two complete policies, rather than a misleading one-call comparison

**Exact-pricing policy.** At each master solve, maximize the current pattern score
by capacity dynamic programming. Break score ties by used capacity, retaining the
existing state for remaining ties. Add that pattern if it improves. Also evaluate
three greedy orders as diagnostics, not as a replacement of the chosen column.
This is simpler than the full lexicographic method of [2], not a reproduction of it.

**Greedy-first policy.** Try density order, price order, and descending size. Add
the best of those feasible patterns when its score exceeds one. Otherwise invoke
the same exact pricer. Thus a failed cheap search is an ACTUAL fallback call in this
workflow, not one inferred from a different policy's dual trajectory.

No stabilization is used; the exact symmetry reduction and previous columns are
retained. Advanced smoothing, pricing filters, cores and lexicographic choices can
improve these baselines. Their absence does not support any quantum superiority.
The policies and numerical settings are fully specified; this is not a timing
race between compiled and interpreted software.

Both use one fixed integer-recovery schedule: first attempt when the restricted
LP value reaches the volume lower bound 48, then after every ten added columns.
Each attempt has a 1,000-node cap. A returned candidate is checked combinatorially;
once it uses 48 bins, the workflow stops. The threshold is computed from input
volume, not read from the source answer. This schedule is a declared research
policy, not an optimized schedule selected to make either method win.

| Quantity | Exact pricing | Greedy first |
|---|---:|---:|
| Master LP solves | 56 | 80 |
| Added columns | 55 | 79 |
| Actual exact pricing calls | 55 | 9 |
| Positive exact pricing calls | 55 | 9 |
| No-column exact pricing calls | 0 | 0 |
| Exact DP capacity relaxations | 607,310 | 99,378 |
| Integer-recovery calls | 4 | 5 |
| Final verified bins | 48 | 48 |
| Restricted LP value at stopping (diagnostic) | 47.4545182972 | 47.5164609053 |

For the exact policy, 51 of 55 pricing duals ALSO admit a positive column in the
three greedy orders. The four remaining calls must not be called the fallback
trajectory of the greedy-first optimizer: that policy has its own 79-call path and
nine fallbacks. Faster or easier individual columns can require more master solves.
The differing stopping LP values do not affect the common exact integer certificate.
We do not claim either policy is globally fastest or that the remaining LP problem
has been solved exactly. No measured quantum/classical runtime ratio is reported.

## 4. Exact pricing is small even though the binary representation has 120 bits

The ordinary binary-item recurrence visits

$$
\sum_{i=1}^{120}(150-a_i+1)=11,042
$$

capacity states per pricing call. It stores 151 capacity entries (and reconstruction
information), not a 2^120 table. Each update involves finite integer arithmetic.
A separate bounded-type recurrence checks every invoked DP optimum exactly;
its validation work is counted separately in the report, not hidden inside an
advertised solver cost. The solver needs only the first recurrence.

The full original Falkenauer uniform family has fixed capacity 150 [1]. Thus merely
increasing its number of items does not recreate exponential pricing complexity:
this particular DP has linear arithmetic-step growth in the number of items, with
profit-bit costs still counted. This says nothing comparable about the complete
integer packing problem or arbitrary precision families.

Changing physical units does not supply a difficult capacity. If capacity and
all sizes are multiplied by the same integer, divide by their common gcd before
pricing. The feasible patterns are identical. A putative high-precision workload
must survive ordinary exact rescaling and the approximation/gap bypasses of Note 06.
No all-instance linear classical bound or impossibility of a polynomial quantum
improvement is inferred from the cost of this particular DP.

## 5. Check the actual marked probability, but do not supply it for free

After solving each call that defeated the greedy orders, we computed the exact
probability of improvement under Note 06's fair feasible-prefix generator. Apply
its safe fractional-core fixing first; order the remaining individual item copies
by density, then descending size and stable index. This is a specified admissible
quantum preparation and also a classical sampler. It is not uniform on feasible
patterns. Neither optimizer uses these probabilities or the source optimum.

For the nine ACTUAL greedy-first fallback calls, the masses lie between

$$
0.091686350631\quad\text{and}\quad0.752801740210.
$$

The retained free-item counts are 119 or 120. Thus a large free decision register
has survived the simple fixing rule, yet exact pricing is still small and the
accepted patterns are not rare in this prepared distribution. Repeated classical
draws of the SAME generator need between about 1.33 and 10.91 draws in expectation
for these calls. The quantum square-root dependence remains mathematically valid
but supplies no compelling inference of a hardware benefit. It is not legitimate
to compare an amplification iteration with one cheap classical arithmetic update.

The exact policy's four diagnostic calls have a different range, approximately
0.0537365 to 0.428931. Their rows are separate. We have not inserted quantum-produced
patterns into either master, so no quantum-assisted iteration count is measured.

These probabilities were acquired OFFLINE after exact classical pricing. The
calculation constructs a suffix DP and memoizes weighted branch recursion; it uses
61,789 and 185,124 nontrivial recursion states across the two policy traces,
respectively, plus the reported suffix cells. Its explicit cap is 200,000 states
per call; unresolved states would produce rigorous intervals rather than invented
exact values. Every tested call completes exactly below that cap. This is additional
diagnostic work, not a free p oracle, a scalable probability algorithm, or a cost
that an ordinary column finder needs to pay.

## 6. Numerical duals do not become exact by declaration

HiGHS provides floating-point master coefficients and dual values. For each call
we take the nonnegative duals and round DOWN to denominator D=2^24. Those integers
define the exact pricing problem; comparisons, DP recurrences and probability
calculations use integers/Fractions. Current restricted-column feasibility is
checked exactly for those dyadic duals.

At most seven items fit, so every pattern's score changes by less than 7/D relative
to the nonnegative native dual vector, apart from the explicitly checked floating
interface. A small missed strict improvement is not certified absent. No exact
no-column inference is made from the rounded scores.

For any such scores, an exact pricing bound U gives a fully valid dual lower bound
sum_t m_t v_t/max(D,U), whether or not the floating duals are exactly optimal.
The code also rounds the restricted primal upward and, if necessary, rescales it
until all coverage inequalities hold rationally. Those rational lower/upper checks
are validation of LP bounds, not a claim that the native solver has rational
optimal bases. Final integer optimality instead follows from volume plus the
explicit 48-bin assignment; it does not depend on those solver tolerances.

The final report is reproducible in the recorded NumPy 2.3.5 / SciPy 1.17.0
installation. Future solver versions can choose different degenerate duals and
columns. Their trajectories may change without invalidating the mathematical
contract. Do not overwrite the archived report to force byte agreement.

## 7. Consequence and next decision

This answers the first workload question, not the entire project. In this published
slice, no expensive unresolved pricing or absence-certificate subroutine stands
between the optimizer and the useful integer output. Positive calls dominate;
none required a full no-column certificate. We must NOT report that certification
is the observed bottleneck simply because it was an earlier concern.

The result does not refute QRAM-free quantum pricing on every workload. It does
remove the justification for scaling this fixed-capacity benchmark or building a
new quantum compiler as the next default activity. The classical representation
compresses the calculation more effectively than counting free binary variables
would suggest. The useful root-LP construction in Note 06 remains a reference,
not a demonstrated new algorithm or application speedup.

**Next bounded gate:** before selecting another instance, identify an independently
motivated pricing regime in published optimization workflows whose effective
capacity/representation and required final gap survive these exact and approximate
bypasses. Verify whether its difficult work is useful column discovery, not a
standalone oracle optimum. Richer constraints are not silently covered by Note 06;
any such proposal needs its own real consumer and ordinary-circuit predicate.
Do not add constraints or decimals just to manufacture a difficult search. If no
specific residual mechanism emerges from that limited source/model check, park the
ordinary one-dimensional pricing lead and return to the broader gate-model screen.
No larger uniform-instance census or new solver framework is authorized by this note.

## 8. Reproduction and source provenance

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/pricing_workload_v1/verify.py
# Optional detailed acquired-dual trajectory, outside the versioned report:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/pricing_workload_v1/verify.py --full-trace
```

Python 3.10+, NumPy, SciPy. The standalone checker reads its normalized attributed
input and writes JSON to stdout only. Its two final ordinary runs produced identical
JSON; -O/-OO and six invalid-input controls were rejected. The report carries both
explicit packings and the separate exact/greedy-first operation inventories.
Only one public benchmark is used. Preliminary unaggregated development attempts
are excluded from the reported comparison; one reached an execution cap. No timing
conclusion is taken from them. Complete scope is the final deterministic workflow.

The primary OR-Library page/text was retrieved through web access. Direct runtime
network transfer failed; the first 120-item block was transcribed and checked for
length, capacity and source metadata. The input hash pins that NORMALIZED extraction,
not the unavailable original transfer bytes. No code or data from the secondary
BPPLIB repository was imported. `SOURCE_NOTICE.md` preserves this distinction and
external attribution. No public dataset is called industrial data.

No quantum circuit, amplitude amplification, FPTAS, stabilized/advanced lexicographic
pricer, native SCIP example or measured speedup was executed. HiGHS LP/MIP really
was invoked, but not an entire production branch-and-price package. Earlier
scientific verifiers and source files are unchanged. The primary-source screen
uses HTML/text only; no PDF or figures were analyzed and no new novelty is claimed.

[1] J. E. Beasley, OR-Library, one-dimensional bin-packing data contributed by
E. Falkenauer. `binpack1.txt`, first problem `u120_00`; source and format accessed
30 September 2026.
https://people.brunel.ac.uk/~mastjjb/jeb/orlib/binpackinfo.html
https://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/binpack1.txt

[2] Coniglio, D'Andreagiovanni and Furini, A lexicographic pricer for the fractional
bin packing problem, Operations Research Letters 47 (2019), 622–628. Primary
abstract: lexicographic DP and smoothing can reduce columns and total work;
that full method is not implemented or newly benchmarked here.
https://eprints.soton.ac.uk/435220/
https://doi.org/10.1016/j.orl.2019.10.011

[3] SciPy official documentation, linprog(method='highs'), dual simplex option
and dual marginals. Documentation retrieved 30 September 2026; installed version
is recorded in the report rather than inferred from the current manual.
https://docs.scipy.org/doc/scipy/reference/optimize.linprog-highs.html

[4] SciPy official documentation, milp, its HiGHS backend and node limit.
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html

[5] SCIP official pricer documentation, bin-packing pricing as an established
plugin interface. Read at documentation level only; SCIP was not installed or run.
https://www.scipopt.org/doc/html/PRICER.php

Only Quantum-Assisted-Algorithm-Discovery is writable. No new repository, spin-off,
QRAM assumption, manuscript, branch merge, release or outside contact follows.
