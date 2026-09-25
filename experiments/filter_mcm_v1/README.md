# A real coefficient-bank workload, and the limits of operation-count synthesis

25 September 2026. Successor to `unique_helpers_v1`; no historical data or license is changed.

## Decision

Use published constant-multiplier filter banks as a concrete workload family to screen. **Do not nominate the small instances below as quantum-advantage targets.** They expose a useful distinction between minimizing arithmetic operations and meeting timing constraints, but the tested optimum-count instance is easy classically. A surviving hard, useful instance and a comparison with current specialized native synthesizers are still missing.

The intended quantum output would be an exact, reusable classical shift/add circuit satisfying an independently specified timing and bit-cost requirement. No quantum execution is required when that circuit is subsequently used. The old unshifted-addition helper normal form and old quantum resource estimates do not transfer automatically.

## 1. Independently specified task

The first nine coefficient matrices come from the authors' SAT-MCM image-filter benchmark file at a pinned commit; see `PROVENANCE.json`. They include Gaussian, Laplacian, highpass, lowpass, and unsharp kernels. This is mathematical data transcription, not a claim that these exact circuits are deployed or that we ran the authors' synthesizer.

The subproblem is to produce the multiples `c*x` for each prescribed coefficient `c`, sharing intermediate multiples of the same input `x`. Sign and powers of two are separated, leaving positive odd fundamentals. Producing a coefficient bank is only part of a filter implementation: sample delays, accumulation, sign restoration, final scaling, rounding and placement/routing are not modeled here. Fractional-bit annotations come from the source; computations are exact integers, not an approximate image-processing experiment.

This is an established classical optimization task. Bit-level SAT synthesis, pipelined adder-graph optimization, FPGA-specific architectures, and recent decomposition-based methods are prior work [1–4]. Pipelining is not an invention of this project.

## 2. Declared computational model

Start from the coefficient 1. A node selects two earlier positive odd coefficients `a,b` and constructs

`c = abs((a << s) + sign*b) / 2^t`,

with `sign` in `{+1,-1}`, exact division, and `c` positive odd. In the bounded SMT experiment, `c < 2^B` and `0 <= s,t <= B`. Both subtraction orientations are admitted through absolute value. Copying, shifts, signs and arbitrary fanout are free in the operation-count model; one binary addition/subtraction costs one. No modular overflow, truncation or saturation is permitted. Unlimited live storage is assumed unless the separate fixed-witness pipeline calculation is explicitly invoked.

The independent QF_BV encoding uses `W=2B+2` bits. A shifted operand is below `2^(2B)`, and the sum of two operands is below `2^(2B+1)`, so the asserted exact relation does not wrap. `k` nodes represent an at-most-k budget because redundant `1` nodes may pad a shorter circuit. Native UNSAT excludes the stated bounded model, not all coefficient bounds or all architectures.

`mcm_smt.py` is our encoding. `smt_native.py` calls the installed native Z3 C library. **This is not a reproduction of SAT-MCM, its SAT-CMM successor, RPAG, jMCM, or a strongest-native-solver result.** The author's README explicitly deprecates SAT-MCM in favor of SAT-CMM; this successor was located but not executed.

## 3. First classical screen

`cases_observations.json` retains one measured run using Z3 4.13.3.0, a four-second per-query timeout and no configured parallel search. Timing includes SMT-LIB ingestion and solving, not Python formula construction. Models/timings are observations, not expected byte-identical rerun outputs.

| Published bank | Nontrivial odd outputs | First returned node count | Earlier bounded budgets |
|---|---:|---:|---|
| Gaussian 3x3, 8-bit coefficients | 3 | 4 | 3 UNSAT |
| Laplacian 3x3, 8-bit coefficients | 3 | 3 | Cardinality lower bound |
| Unsharp 3x3, 8-bit coefficients | 3 | 4 | 3 UNSAT |
| Unsharp 3x3, 12-bit coefficients | 3 | 5 | 3 and 4 UNSAT |
| Gaussian 5x5, 12-bit coefficients | 3 | 5 | 3 and 4 UNSAT |
| Highpass 5x5, 8-bit coefficients | 4 | 4 | Cardinality lower bound |
| Lowpass 5x5, 8-bit coefficients | 5 | 6 | 5 UNSAT |
| Highpass 9x9, 10-bit coefficients | 5 | 5 | Cardinality lower bound |
| Lowpass 9x9, 10-bit coefficients | 12 | No SAT result within cutoff at 12,13,14 | All three UNKNOWN, not UNSAT |

Every individual conclusive solver call took under 0.5 seconds in this measured run. These are not universal runtime claims. All eight SAT certificates are independently checked by exact arithmetic. The larger-instance UNSAT results are not accompanied by independently checked proof traces.

The last row is especially informative: simple target closure constructs a 12-node answer in milliseconds in this environment (an exploratory run took about 2.9 ms). There are twelve distinct required non-input odd fundamentals, so twelve is also an unconditional operation lower bound within this shift-add/sign/copy model. The solver timeouts were not intrinsic discovery difficulty.

No quantum claim can be based on those timeouts. A serious classical comparator must retain closure and specialized synthesis methods, rather than inherit this generic encoding's weakness.

## 4. An exact count-versus-depth tradeoff

The lowpass 9x9 bank needs the following positive odd fundamentals besides 1:

`5, 7, 25, 31, 63, 65, 67, 73, 97, 117, 165, 303`.

There are two explicit circuits:

- 12 additions/subtractions, arithmetic depth 3, no non-output helper.
- 13 additions/subtractions, arithmetic depth 2, using the helper 15 (17 also works).

For the first circuit, examples of the dependencies are

`25 = 32 - 7`, `97 = 128 - 31`, `303 = 16*25 - 97`.

The last operation occurs at depth 3. For the second circuit,

`15 = 16 - 1`, `63 = 64 - 1`, `303 = 16*15 + 63`.

All twelve outputs can now be produced within two binary-adder layers. The certificates record every operation, not only this final formula.

### Lower bounds, not just two arbitrary witnesses

Twelve nontrivial odd outputs require at least twelve operations. A twelve-operation implementation can contain no non-output fundamental. Its only available depth-one values are

`1, 5, 7, 31, 63, 65`.

The required 303 cannot be made in one further shifted add/subtract using those values. For a positive shift, the numerator is odd, so no right division is possible; the shifted operand must be at most `303+65=368`, giving `s <= 8`. With zero shift, normalized sums/differences are at most 65. This proves that the finite pair check covers arbitrary shifts for this obstruction, not merely the numerical B=10 setting. Thus twelve operations cannot attain depth two. The explicit thirteen-operation witness attains it; depth one is impossible. The points `(12,3)` and `(13,2)` are Pareto-optimal in this declared unit-latency, free-shift/sign, unlimited-fanout model.

`layers` computes earliest feasible levels in a fixed pool of target/helper expressions, starting from 1 alone. Helpers are not supplied as free inputs. Candidate helper enumeration is bounded by B=10, and exactly 15 and 17 work among the one-operation non-output helpers in that range. We do not claim this is an exhaustive classification of arbitrarily large one-operation helper coefficients.

No novelty claim is made for either circuit or for timing-aware synthesis. The result demonstrates that the operation-minimal program need not be the correct answer to a timing-constrained design task.

### Limited register accounting

For unsigned 16-bit input, the two fixed certificates admit explicit fully pipelined ALAP schedules requiring 502 and 422 register bits respectively under the accounting in `pipeline`. Each live positive fundamental has its exact unsigned width; all outputs and the bypassed input are aligned. This is not a global register minimum or an area estimate. The added adder costs hardware; sign/shift restoration and filter logic are excluded. No placement/routing, power, clock frequency, throughput or silicon measurement was performed. The robust measured result is the arithmetic depth tradeoff, not a hardware speedup.

## 5. Verification and reproducibility

Run:

```
python experiments/filter_mcm_v1/verify.py
python experiments/filter_mcm_v1/verify.py --solver
```

The default uses the Python standard library only, checks file hashes, validates all stored SAT certificates, regenerates all deterministic results in a temporary directory, and evaluates both complete multiplier-bank circuits for all 65,536 unsigned 16-bit inputs, checking every intermediate. Exact coefficient identities also establish correctness for arbitrary integer inputs with sufficient precision.

The optional flag requires a discoverable native Z3 shared library. It compares the independent SMT encoding with a direct finite circuit enumeration on all 128 target subsets of the seven nontrivial four-bit odd constants at budgets 0,1,2: 384 decisions, 35 SAT and 349 UNSAT. Both subtraction orientations and normalization are included. This finite comparison validates the encoding on those inputs, not every larger instance.

To repeat the observational benchmark without overwriting reference evidence:

```
python experiments/filter_mcm_v1/run_cases.py --output /tmp/new-mcm-observations.json
```

Do not run with Python -O/-OO. Repeated timing/model outputs need not match the stored observations. UNKNOWN must remain distinct from UNSAT. The supplied previous `unique_helpers_v1` verifier was rerun successfully; older target-closure and long guided-search benchmarks were not rerun this turn.

## 6. Implications for the research project

Keep constant-multiplier hardware synthesis as a concrete candidate workload family, not as an established application of quantum advantage. The next candidate should be an unsupplied circuit satisfying a fixed depth/bit-cost requirement for a real coefficient bank, after strong current classical preprocessing and native synthesis. The known small banks above are calibration and rejection cases, not hardness evidence.

A coherent algorithm may still explore helper sets, but the acceptance test must account for how the values are generated and their depth. Previously free shifts change the expression domain; storage, fanout, word widths and mapped hardware can change equivalence or costs. Do not import an old helper theorem or quantum qubit count unchanged. At a fixed expression pool, earliest-layer propagation is cheap; expensive choices should be genuinely different constructions, not redundant schedules.

Before implementing another quantum oracle, obtain a current specialized solver comparison and a complete design objective. Only then compare the quantum cost of obtaining a qualifying circuit with the full classical cost, including preprocessing, alternative synthesis formulations and parallel resources. Reuse helps justify why the output matters but gives no exclusive advantage to quantum discovery.

## References

[1] N. Fiege, M. Kumm, P. Zipf, *Bit-Level Optimized Constant Multiplication Using Boolean Satisfiability*, IEEE TCAS-I 71(1), 249–261 (2024), DOI 10.1109/TCSI.2023.3327814. Author software/data DOI 10.48662/daks-21. Pinned coefficient-source details are in `PROVENANCE.json`.

[2] M. Kumm, P. Zipf, M. Faust, C.-H. Chang, *Pipelined adder graph optimization for high speed multiple constant multiplication*, ISCAS (2012), DOI 10.1109/ISCAS.2012.6272072.

[3] M. Kumm, *Multiple Constant Multiplication Optimizations for Field Programmable Gate Arrays* (2016), DOI 10.1007/978-3-658-13323-8.

[4] *Decompose, Optimize, and Reconstruct: Very Large Constant Multiplication at Scale*, arXiv:2605.23998 (2026). Abstract-level inspection, not a reproduced benchmark.
