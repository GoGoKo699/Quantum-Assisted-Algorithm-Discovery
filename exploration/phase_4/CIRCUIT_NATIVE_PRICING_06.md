# Circuit-native pricing 06: useful packing columns without QRAM

30 September 2026. Baseline: `c149437c106404709c8e19eb717da7904b835d2f`.
Branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision:** investigate one hardware-admissible hypothesis: a quantum circuit
finds a feasible negative-reduced-cost pattern for a classical packing optimizer.
Quantum tree generation and quantum-assisted pricing are already published ideas
[3,4]. This is a model/access/comparator screen, not a new algorithm, established
speedup, industrial improvement, or priority claim. No new repository is needed.

The missing condition is whether useful pricing calls remain difficult after
strong classical methods, and whether quantum assistance reduces TOTAL solver
work. A hard standalone knapsack or a square-root search formula is insufficient.
The old sparsifier stays parked and the emitter covariance stays closed.

## 1. Bounded screen

| Candidate | Useful output | First access/accuracy obligation |
|---|---|---|
| First-quantized particle dynamics | Reaction, scattering, or energy-transfer information | Pair interactions admit coordinate arithmetic; preparation, physical approximation, evolution time and readout remain [10] |
| Stochastic transport | Dose, flux, or response estimates | A reversible history must price material/cross-section access and strong variance-reduced classical transport [11] |
| Packing column generation | A feasible pattern for a classical optimization model | Sizes/prices can be fixed gate constants; ordinary pricing can bypass the quantum call |

Packing is selected for one bounded test, not a claim that the alternatives fail.
It retains classical input and directly useful classical output. Neither physics
nor transport is a parallel default program. No physical-source input is substituted.

## 2. An actual optimization interface

Column generation avoids enumerating every material-use or packing pattern [1].
Our precise scope is the root LP of ordinary one-dimensional binary bin packing
[2], not unbounded cutting stock, nonlinear packing, or all branch-and-price nodes.
Positive integer sizes a_i<=B describe individually indexed items. Define

$$
P=\{x\in\{0,1\}^n:a\cdot x\leq B\},\qquad
\min_{z\geq0}\sum_{x\in P}z_x\quad
\text{subject to }\sum_{x\in P}x_i z_x\geq1.
$$

A classical restricted master solves this covering relaxation with only selected
columns, for example starting with singletons. Its nonnegative duals pi_i assign
a score to each item. The subproblem, called pricing, is

$$
\boxed{\text{find }x\in P\text{ with }\pi\cdot x>1.}
$$

The column's reduced cost is 1-pi dot x. It is eligible to improve the relaxation,
but degeneracy can prevent an immediate objective decrease. A column alone is not
an integer packing, fewer bins, or a global optimality certificate. The classical
master, integer recovery, branching and validation remain paid components.

Use supplied exact rational prices pi_i=v_i/D with nonnegative integer v_i and
D>0. The common denominator's full bit length counts. Actual numerical duals and
price rounding must be validated; they are not supplied as exact optimal duals for
free. A declared stronger acceptance margin changes the subproblem and cannot
certify absence of arbitrarily small improvements. Multiplicities and branching
conflicts need additional representations/predicates and are outside this screen.

## 3. Classical reductions come first

Greedy patterns, prior columns, capacity dynamic programming, adaptive core methods,
and stronger exact pricers are all allowed [5]. A classical fractional bound gives
an elementary, exact filter. For lambda>=0 put d_i=pi_i-lambda a_i and

$$
U=\lambda B+\sum_i\max(d_i,0).
$$

For every feasible x,

$$
U-\pi\cdot x=\lambda(B-a\cdot x)
+\sum_{d_i>0}d_i(1-x_i)+\sum_{d_i<0}|d_i|x_i\geq0.
$$

A fractional-knapsack break slope obtained by classical ratio sorting gives a
tight LP upper bound U. If U<=tau=1, there is no improving column. If a cheap
heuristic already finds one, return it without quantum work. Otherwise let g=U-tau.
Every improving pattern must have x_i=1 when d_i>g and x_i=0 when -d_i>g: violating
one of these bits makes the nonnegative residual exceed g. These safe fixings
leave k free items, capacity B', and fixed score v_fix/D. They need not match the
smallest core a mature solver can expose, and k is not a classical lower bound.
Both competitors get all valid classical reductions.

### Approximate pricing may already answer the useful question

Knapsack has fully polynomial approximation schemes [12]. If OPT>=1+eta, a feasible
(1-zeta) approximation with zeta=eta/[2(1+eta)] returns at least 1+eta/2>1. A fixed
improvement margin therefore has a polynomial classical finder. Artificially tiny
margins do not establish useful quantum difficulty. Small integer capacities also
favor capacity dynamic programming; logarithmic quantum register width is not a
complete comparison to that method.

A valid pricing upper bound can certify a sufficient master gap without proving
exact column absence. Set alpha=max(1,U). Then pi/alpha is dual feasible for ALL
patterns. If the restricted master was solved exactly with common primal/dual
objective z_R, weak duality gives

$$
z_R/\alpha\leq z_{\rm full\ LP}\leq z_R.
$$

If an approximation returns vhat<=1 and vhat>=(1-zeta)OPT, take
U=vhat/(1-zeta); the full-master lower bound is at least (1-zeta)z_R.
Its ceiling can sometimes certify an integer packing if it equals a known feasible
integer upper bound. Numerical feasibility and rounding still need validation.
These are standard approximation/duality consequences, not new optimization theory.
They prevent us from requiring exact pricing when the consumer needs only a gap.

## 4. Ordinary-circuit preparation, with no data oracle

Discard residual items larger than B' and check an already-profitable fixed pattern
classically. Fix a classical item order. Initialize k decision bits to zero and
a capacity register to B'. At each item:

1. Reversibly compute f=[r>=a_i].
2. Apply a Hadamard to its zero decision bit controlled by f.
3. Uncompute f BEFORE changing r.
4. Subtract fixed a_i from r controlled by the decision bit.

This is a simple specialization of the established quantum tree generator [3].
The full operations are reversible; reachable branches never underflow. Decision
bits retain the history. Induction gives support on every feasible pattern and
none on infeasible patterns, without feasibility postselection. Its probabilities
are generally not uniform: a path with b(x) genuine binary decisions has mass
2^(-b(x)). The item order matters. This is also the law of a classical sequential
fair-choice generator, which is one comparator, not the best classical algorithm.

Add fixed v_i into a score register controlled by each selected bit, include v_fix,
compare with D, phase-mark strict improvement, then uncompute the score. Invert
the preparation for the initial-state reflection. Computing the old fit flag from
an already reduced capacity would NOT correctly uncompute it.

Item sizes and prices are gate constants used at fixed places in the circuit.
No unknown quantum address queries an input database, DP table, column pool or
changing classical search tree. The master and stored columns stay in ordinary
classical RAM. This is not QRAM relabeled as a state-preparation oracle.

## 5. Complete symbolic resource boundary

Sufficient counter widths are

$$
w=\max\{1,\lceil\log_2(B'+1)\rceil\},\qquad
b=\max\{1,\lceil\log_2(1+\max(D,v_{\rm fix}+\sum_i v_i))\rceil\}.
$$

The score register must represent the threshold and every possible sum without
wraparound. Ripple-carry comparison/addition/subtraction [6], controlled variants,
uncomputation, and the initial reflection give a sufficient O(k+w+b) logical-qubit
and O(k(w+b)+w+b) logical-gate cost per iteration. These are derived upper bounds,
not a decomposed Toffoli circuit or physical performance estimate. k=0 is classical.

Read all original coefficient bits and pay classical sorting/pricing/compilation.
Residual gate constants occupy O(k(w+b)) bits; original widths can be larger.
Dual updates may change profit circuits, core and order. Only applicable templates
can be reused. No all-to-all logical connectivity is assumed free: a deliberately
loose line-routing construction adds an O(k+w+b) gate/depth factor using swaps.
Architecture-specific routing and fault-tolerant overhead require separate pricing.

If p is the actual prepared mass of acceptable patterns, standard amplitude
amplification [7] gives O(1/sqrt(p)) expected preparation/inverse calls for p>0,
including methods not given p. Thus one conditional logical-gate bound is

$$
\widetilde O\left([k(w+b)+w+b]/\sqrt p\right),
$$

before classical setup, routing, physical overhead and validation. Repeated draws
from the SAME generator need 1/p in expectation. This does not bound the cost of
the strongest classical core, DP, approximation, or branch-and-bound method.
p can be exponentially small, and optimum probability is not the same as the mass
of all useful columns. No useful lower bound on p is established here.

A bounded search failure does not distinguish p=0 from a small p. This is a column
FINDER, not an exact no-column or optimality certificate. Classical exact pricing
or a valid objective bound supplies termination. Rechecking a measured pattern
catches an invalid answer but cannot certify absence from no answer. Budget circuit
errors, failures, fallback and updates across the entire optimization run.

## 6. The actual competition and novelty boundary

The candidate claim is conditional: some useful residual column-finding calls
might be costly classically but have sufficient generator mass for fully priced
quantum search. Their output would immediately enter an ordinary optimizer. That
is a concrete role, not a proved workload or an exponential-advantage claim.

The metric is setup plus all master/pricing iterations to a specified packing or
certified gap, not the speed of one arbitrary positive column. Degeneracy can make
quick weak columns unhelpful. Exact lexicographic pricing improves the complete
fractional-bin-packing process [2]. Pricing filtering reuses prior duals [8], and
recent template pricing coordinates columns in other decomposition models [9].
Their results do not transfer automatically to this target, but they rule out
independent brute-force pricing as the sole classical baseline.

Quantum-assisted column generation is already studied for vertex coloring on
neutral-atom platforms [4]. Quantum tree generation for knapsack is also prior
work [3]. Its generated standalone benchmarks and assumed clock/connectivity
comparisons do not establish an industrial pricing regime, nor a crossover for
this proposal. Merely composing the two ideas does not establish novelty.

A major failure mode is that positive columns are cheap, while the expensive work
proves there are NO more useful columns. Another is that an approximate dual bound
already meets the solver's actual accuracy. Either can defeat this proposal even
if a worst-case exact knapsack calculation is difficult.

## 7. Next bounded test

Characterize pricing calls induced by a specified classical bin-packing workflow,
retaining its true duals, stabilization and required LP/integer gap. Apply adequate
cheap patterns, fractional/core bounds, approximation and scaled-dual checks first.
Identify residual k, coefficient widths, target score, generator p or a justified
bound, and whether cost is column discovery or absence certification. Computing p
must not require an uncounted exact answer or become a free quantum input.

Use existing model families or a small declared benchmark slice only to answer
that question. No new solver framework, large synthetic census, or dataset campaign
is selected. A hardware compiler comes after a credible application case. If useful
residual calls are cheap or mainly certification, park the candidate. A surviving
bottleneck warrants one focused cost/novelty audit, not a presumption of advantage.
A universal classical lower bound is not required for that conditional investigation.

## 8. Executed checks and source scope

```sh
python experiments/circuit_pricing_v1/verify.py
```

Python 3.10+, standard library. Three easy illustrative jobs check 54 exact
reduced-cost identities, preservation of six improving patterns, 54 scaled-dual
constraints, and three approximation-margin identities. In one eight-item control,
three safe fixed bits leave five free decisions: improving mass changes from 7/16
to 7/8, while the original uniform-feasible fraction was 1/8. Another job is rejected
by a bound and a third becomes fully fixed. These are not pricing duals acquired
from an industrial instance or demonstrations of a hard residual problem.

The final checker ran twice with identical JSON, rejected -O/-OO and six invalid
inputs, and detects nonuniform sampling, score overflow and misuse of a stronger
margin as an absence certificate. No FPTAS, native LP/knapsack solver, quantum
circuit, amplitude amplification, actual pricing workload or timing comparison was
executed. General algebra/circuit arguments are given above, not inferred from the
finite tests. No old scientific verifier was rerun or upstream code/data imported.

Primary sources checked 30 September 2026. The QTG primary HTML methods/discussion
and other primary abstracts/records were inspected. No PDF was analyzed, no plot
or table was digitized, and no source implementation ran. Native SCIP documentation
requests were rate-limited; no native behavior is claimed verified. This is not
an exhaustive novelty or proof audit.

[1] Gilmore and Gomory, A Linear Programming Approach to the Cutting-Stock Problem,
OR 9 (1961), and Part II, OR 11 (1963). Established material-use motivation;
cutting-stock multiplicities are not silently covered by our binary model.
https://doi.org/10.1287/opre.9.6.849
https://doi.org/10.1287/opre.11.6.863

[2] Coniglio, D'Andreagiovanni and Furini, A lexicographic pricer for the fractional
bin packing problem, OR Letters 47 (2019). Primary abstract and model scope.
https://doi.org/10.1016/j.orl.2019.10.011

[3] Wilkening et al., A quantum algorithm for solving 0-1 Knapsack problems,
npj Quantum Information 11,146 (2025). Explicit circuit architecture and limitations.
https://www.nature.com/articles/s41534-025-01097-8

[4] Coelho, Henriet and Henry, Quantum pricing-based column-generation framework
for hard combinatorial problems, PRA 107,032426 (2023). Primary abstract.
https://doi.org/10.1103/PhysRevA.107.032426

[5] Pisinger, A Minimal Algorithm for the 0-1 Knapsack Problem, OR 45 (1997).
Primary abstract on adaptive cores, not a rerun of its benchmarks.
https://doi.org/10.1287/opre.45.5.758

[6] Cuccaro et al., A new quantum ripple-carry addition circuit (2004).
https://arxiv.org/abs/quant-ph/0410184

[7] Brassard et al., Quantum Amplitude Amplification and Estimation (2000).
https://arxiv.org/abs/quant-ph/0005055

[8] Bulaich Mehamdi et al., Pricing Filtering in Dantzig-Wolfe Decomposition (2024).
Primary abstract; reuse is not automatically applicable to every packing instance.
https://arxiv.org/abs/2411.11338

[9] Marshall, Shah and Dey, Accelerating Column Generation in Highly Degenerate
Integer Programming Problems with Template Pricing (2026). Primary abstract;
its generalized-assignment results are not claimed for bin packing.
https://arxiv.org/abs/2604.12070

[10] Pocrnic et al., Efficient Simulation of Pre-Born-Oppenheimer Dynamics on a
Quantum Computer (2026). Primary abstract-level alternative screen only.
https://arxiv.org/abs/2602.11272

[11] NQCC, Quantum Monte Carlo Radiation Transport Simulation. Application/project
description only, not an inspected oracle or a speedup theorem.
https://www.nqcc.ac.uk/quantum-monte-carlo-radiation-transport-simulation/

[12] Lawler, Fast Approximation Algorithms for Knapsack Problems, MOR 4 (1979).
Primary abstract. The margin/dual-scaling consequences are derived above.
https://doi.org/10.1287/moor.4.4.339

Only Quantum-Assisted-Algorithm-Discovery is writable. Preserve the no-QRAM rule,
prior science and rights, and the independent spin-offs. No new repository,
manuscript, third spin-off, branch merge, release, outside contact or paid work.
