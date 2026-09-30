# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Fault-tolerant circuits; no assumed fast QRAM.** No useful end-to-end quantum
advantage is established. Manuscript preparation remains on hold.

## Current bounded hypothesis: risk-aware packing at a useful pricing threshold

[Risk-aware pricing 08](exploration/phase_4/RISK_AWARE_PRICING_GATE_08.md) completes
the source/model gate after the deterministic benchmark. Cloud workload allocation
with an overload-risk constraint is independently motivated, and published
classical optimization experiments identify a pricing-heavy medium-scale family.
Those are source-reported generated benchmarks, not a new cloud workload run or
industrial quantum advantage.

The new pattern constraint depends on both total mean demand and pooled variance.
After clearing denominators, it needs two running sums and a sign-guarded squared
comparison. Coefficients are sequential gate constants, not coherent table queries.
The note gives a symbolic feasible-prefix circuit and charges multiplication,
precision, recompilation, routing and amplitude-amplification costs. No circuit
was compiled; no free random-demand oracle or quantum-addressable master is assumed.

A published hybrid-pricing rule makes the target more specific than any positive
column: find a feasible score v>1 with v>=z_R/L, where z_R is the restricted-master
objective and L its valid existing lower bound. Such a witness makes an exact
pricing call unable to improve that particular bound. It does not prove the whole
packing optimal, and classical algorithms receive the same threshold.

Recent classical non-convex relaxations, approximation methods and existing heuristic
pricing must be tested first. The next task is whether materially expensive calls
remain undecided after those methods, not a larger synthetic census or a new cloud
framework. The quantum pattern-finding probability is unknown and is not given as
free input. Generic chance-constrained quantum knapsack also has prior literature;
no priority claim is made.

[Current work order](work_orders/CURRENT.md) · [Status](STATUS.md) ·
[Phase-4 index](exploration/phase_4/README.md)

## Evidence and boundaries

```sh
python experiments/risk_pricing_gate_v1/verify.py
```

Python 3.10+, standard library. The [report](experiments/risk_pricing_gate_v1/REPORT.json)
contains exact illustrative predicate/generator and threshold controls. The final
checker ran twice identically; -O/-OO and six invalid inputs were rejected.
No cloud trace, native pricer, quantum circuit, performance study or historical
scientific verifier was run. The published workload statistics remain explicitly
attributed and were not reproduced.

[Workload 07](exploration/phase_4/PRICING_WORKLOAD_07.md) retains the two classical
48-bin certificates and closes that fixed-capacity slice as immediate evidence
for advantage. [Note 06](exploration/phase_4/CIRCUIT_NATIVE_PRICING_06.md) remains a
conditional circuit reference. The nonlinear risk model is a distinct specification,
not an unannounced extension of either result.

[AGENTS.md](AGENTS.md), the [no-QRAM decision](exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md),
and [LICENSE](LICENSE) are unchanged. The graph lead stays parked, emitter covariance
stays closed, and independent spin-offs retain their projects. The historical
handover is a snapshot; the current work order governs continuation. Only this
parent repository is writable; no new repository, release or merge is required.
