# Close the small filter-bank count/depth screen

25 September 2026. Successor to `filter_mcm_v1`, based on repository commit `9a9c8c02acc50a6855e460f00c5d98cbd268ab74`.

**Decision: retire these eleven banks' unweighted arithmetic-count/depth synthesis problems as quantum-advantage candidates.** They have exact, inexpensive classical solutions in the model below. This does not rule out other constant-multiplier tasks, larger inputs, bit-cost optimization, physical implementation, or quantum-assisted algorithm discovery generally.

## 1. Scope and independently specified data

`banks.json` transcribes the numerical coefficient sets of all eleven image-filter banks in `Rammbock9000/sat_mcm`, commit `7a0705a5a699a748d7421405b2635d312c55e08d`, file `benchmark/inputs/mcm/mcm.csv`, Git blob `5e6a36da1fc80edae17c69610d42474eb31dfa25`. The complete 2,477-byte source was checked against this Git blob locally. Repeated coefficients are removed because copying is free; all distinct signs and even coefficients remain in the data. The trailing upstream CSV field is not adopted as an optimum. No upstream program code is incorporated. Names are published benchmark labels, not deployment evidence.

The software source is GPL-3.0-or-later; our scripts are independently written. This successor incorporates only mathematical coefficient values, not the source CSV or the authors' implementation. Source attribution and access limits are in `PROVENANCE.json`. The user's original MIT license and historical experiments are unchanged.

The task produces `c*x` for each listed constant. It is a coefficient bank, not an entire image filter: sample delays, accumulation, scaling/rounding, signed-output circuitry, placement/routing, power and clock frequency are outside the objective. Fixed-point scales are not modified; arithmetic before final scaling is exact.

## 2. Declared model

Represent every nonzero available multiple by its positive odd fundamental. Start from 1. A node creates

`c = abs((a << s) + sign*b) / 2^t`,

where division is exact, `sign` is +1 or -1, `0 < c < 2^B`, and `0 <= s,t <= B`. Both inputs refer to earlier nodes. Copies, signs, constant shifts and unlimited fanout/storage are free; a binary add/subtract costs one. Depth is the longest number of such nodes on an input-output path. The bound is `B = max(bit_length(abs(c))) + 1` over the original coefficients, as in the previous screen. Normalizing signs/powers of two does not identify arbitrary scalar multiples.

This is not a bit-area or FPGA clock model. Counts are exact only within this positive-fundamental, finite-shift/coefficient domain. A signed-digit lower bound on depth is also valid without these bounds; the circuit certificates attain that lower bound in every bank, but this does not make their node counts unrestricted global optima.

## 3. Two layers remove most of the synthesis freedom

Every non-output helper in a depth-two circuit is at layer one: a layer-two helper could not feed an output without exceeding the depth cap. A first-layer nontrivial odd fundamental has the form `2^s-1` or `2^s+1`. Thus the first-layer universe is only O(B), not all integers below `2^B`.

Let T be the required nontrivial odd fundamentals, d=|T|, and E the first-layer universe (including 1). Every target in E can be produced immediately at layer one. This costs its unavoidable one node and cannot hurt any other output in this unlimited-storage/fanout node-count model. Put F=T intersect E and let the possible non-output helpers be H0=E minus (F union {1}).

For each target c not in F, enumerate every permitted normalized shifted sum of a,b in E giving c. Each representation requires zero, one or two helpers from H0. Remove helper-requirement sets that strictly contain another requirement for the same c.

A selected helper set H works exactly when, for every remaining c, at least one of c's requirement sets is contained in H. The total node count is exactly d+|H|. Sufficiency constructs F and H at layer one and every remaining output at layer two. Necessity follows from the normal form above. This is a finite monotone coverage problem, not a claim to invent covering or MCM graph methods.

The exact recurrence starts with the empty portfolio. For each output, union every current portfolio with each allowed requirement, then retain all inclusion-minimal unions. If A is a subset of B and both satisfy the outputs already processed, A union C is no larger than B union C for every future choice C. Removing B therefore preserves all minimum-cardinality solutions. The number of retained portfolios may be exponential in general. No polynomial-time or fixed-parameter tractability claim is made.

On the eleven banks, eight are feasible at depth two. The largest intermediate antichain has eleven portfolios. Three banks contain targets whose minimum signed-digit weight exceeds four, making depth two impossible independently of the bounded search.

## 4. The depth lower bound is prior knowledge

Let w(c) be the minimum number of nonzero signed powers of two needed for c. At depth D a binary add/subtract circuit can produce only coefficients with w(c)<=2^D, by subadditivity and invariance under exact power-of-two scaling. Thus D>=ceil(log2(w(c))). A signed-digit adder tree attains the individual depth bound. These facts are established in Gustafsson et al. (2006), not a new result here [1].

`signed_weight` computes the exact integer recurrence w(0)=0, w(1)=1, w(2n)=w(n), w(2n+1)=1+min(w(n),w(n+1)). The unit-depth bound is not a bound on physical gate delay.

Examples excluded at depth two include 171 and 1109 (weight 5), 343 and 1267 (weight 5), and 1197 (weight 6). The largest lowpass bank nevertheless has a target-only 25-node circuit attaining its minimum depth three.

## 5. Exact bounded-depth helper search completes the remaining cases

For depth three and above, `layered.py` adapts the earlier helper-only normal form to shifted scalar arithmetic and a deadline. For a proposed set of targets and helpers, start only from 1 and derive every reachable expression at its earliest layer. A helper is never supplied for free. Branch only on new non-output fundamentals reachable from the available pool before the final layer. A final-layer non-output helper would be dead.

Completeness follows by ordering helpers as in a witness circuit: eager target propagation cannot delay a predecessor, and every useful helper is generated before the final layer. The fixed-pool earliest-layer certificate selects one predecessor rule per expression and is acyclic because levels strictly increase. Identical helper sets are memoized classically. This is not a compiled quantum tree and does not include bit costs or register budgets.

For a total g=d+k node budget, depth g suffices to cover all g-node DAGs. We first find the least feasible helper budget without an additional deadline, then check each depth from the signed-weight lower bound until that global bounded-model node count is attained. This determines every nondominated (node count, depth) pair; larger depths cannot improve the already minimum node count. Failed lower budgets are exhaustive finite searches, not SAT timeout interpretations.

## 6. Results

| Published bank | Complete bounded-model Pareto points (nodes, depth) |
|---|---|
| Gaussian 3x3, 8-bit | (4,2) |
| Laplacian 3x3, 8-bit | (3,3), (4,2) |
| Unsharp 3x3, 8-bit | (4,2) |
| Unsharp 3x3, 12-bit | (5,3) |
| Gaussian 5x5, 12-bit | (5,4), (6,3) |
| Highpass 5x5, 8-bit | (4,2) |
| Lowpass 5x5, 8-bit | (6,3), (7,2) |
| Highpass 9x9, 10-bit | (5,2) |
| Lowpass 9x9, 10-bit | (12,3), (13,2) |
| Highpass 15x15, 12-bit | (12,2) |
| Lowpass 15x15, 12-bit | (25,3) |

The whole synthesis screen, including construction of the helper requirements and exact output certificates, took approximately 0.27 seconds in an initial local Python run. This excludes import/setup and independent verification, is not a cross-solver comparison, and is not a portable runtime guarantee. The core conclusion is constructive classical easiness on these finite tasks, not superiority over the published solvers. No novelty is claimed for the recovered routines, count/depth tradeoffs, coverage methods or signed-digit bound.

For example, the minimum-depth Gaussian 5x5 certificate uses helpers 3,5,13 and computes 23,343,1267 within three layers using six nodes. Its five-node optimum requires at least four layers in this bounded model. The relevant five-node/depth-three exclusion checks 1+23+1095 distinct partial helper states. This is small classical computation, not a quantum search target.

## 7. Verification

```
python experiments/depth2_cover_v1/verify.py
python experiments/depth2_cover_v1/run_screen.py --output /tmp/new-screen.json
```

The first command uses Python's standard library and checks hashes before regeneration in a temporary directory. The second creates the full report with all integer certificates and exhaustive lower-budget counts. Both refuse optimized assertion-disabled execution; output generation refuses to overwrite an existing file.

Independent checks do not use the synthesis move generator: both operands are shifted independently and complete tiny circuits are enumerated with explicit depth labels. All 1,536 decisions (128 target families, four gate budgets, three depth bounds) agree with layered helper search. All 972 target/helper-subset combinations agree with the depth-two coverage model. The 15 Pareto certificates pass exact integer identities and 384 signed input tests each (-128 through 255), including restoration of every original distinct signed/even coefficient: 5,760 network evaluations. These new finite input checks are not called exhaustive 16-bit tests; exact coefficient identities establish arbitrary-integer correctness at sufficient precision.

`expected.json` fixes both generated report hashes and a readable summary. Full generated certificates are also included in the external checkpoint. No reference outputs or historical source files are overwritten to obtain agreement.

The supplied previous `filter_mcm_v1` default verifier was rerun, including its own full 16-bit checks. Its optional native-Z3 check and older historical verifiers/long benchmarks were not rerun.

## 8. What remains uncompleted

We inspected current specialized-tool interfaces: jMCM supports depth constraints and bit costs; SAT-MCM directs users to SAT-CMM; RPAG/PAGSuite is another relevant established baseline [2-4]. We did not run these packages. Raw/archive retrieval for the GitLab packages failed in this environment, and Julia/RPAG/SAT-CMM executables were not installed. No source-transcribed substitute is called a native upstream run.

That leaves the requested specialized-native comparison unfinished. It does not rescue these eleven node-count/depth tasks as hard workloads: the explicit classical procedure above already solves them quickly. Physical bit-area/depth/fanout/placement problems are different objectives and remain open here; antichain subset dominance for node count must not be transferred to such objectives without a new proof.

The research priority is no longer to compile a quantum oracle for these small banks. A successor should begin with a concrete unsupplied routine and an execution-relevant requirement where a documented strong classical discovery process falls short. New restrictions must be externally motivated, not added simply to defeat the current classical solver. Quantum-assisted discovery remains the objective; the eleven-bank count/depth screen is closed in its declared model.

## References

[1] O. Gustafsson, A. G. Dempster, K. Johansson, M. D. Macleod, L. Wanhammar, *Simplified Design of Constant Coefficient Multipliers*, Circuits, Systems, and Signal Processing 25, 225-251 (2006), DOI 10.1007/s00034-005-2505-5.

[2] N. Fiege, M. Kumm, P. Zipf, *Bit-Level Optimized Constant Multiplication Using Boolean Satisfiability*, IEEE TCAS-I 71(1), 249-261 (2024), DOI 10.1109/TCSI.2023.3327814. Pinned numerical input source in `PROVENANCE.json`.

[3] `remi-garcia/jMCM`, author repository; depth-constrained/pipelined and bit-cost MILP interfaces inspected, not executed. `Rammbock9000/sat_mcm` author README points to `gitlab.uni-kassel.de/uk025743/sat_cmm`.

[4] M. Kumm, P. Zipf, M. Faust, C.-H. Chang, *Pipelined adder graph optimization for high speed multiple constant multiplication*, ISCAS 2012, DOI 10.1109/ISCAS.2012.6272072. `gitlab.com/kumm/pagsuite`; no native reproduction.

[5] T. Cantaloube, N. Fiege, A. Volkova, C. Solnon, *Decompose, Optimize, and Reconstruct: Very Large Constant Multiplication at Scale*, arXiv:2605.23998 (2026). A pointer to stronger classical decomposition baselines, not a reproduced result or a claimed current global record.
