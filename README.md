# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Fault-tolerant circuits; no assumed fast QRAM.** No useful end-to-end quantum
advantage is established. Manuscript preparation remains on hold.

## Current finding: test the optimizer, not only the quantum search formula

[Pricing workload 07](exploration/phase_4/PRICING_WORKLOAD_07.md) executes two
classical root-column-generation policies on the first public Falkenauer uniform
benchmark. Both improve a 49-bin greedy packing to an explicitly verified, optimal
48-bin packing. The proof uses item assignments and the input volume, not the
published answer or a floating-point solver's optimality flag.

An exact equal-size reduction gives 58 item types. Capacity dynamic programming
needs 11,042 state relaxations per pricing call. The exact-pricing policy uses
56 master solves and 55 pricing calls; greedy-first uses 80 master solves but only
nine exact fallback pricing calls. Thus a cheaper individual column does not imply
fewer optimization iterations. Useful patterns in those nine fallbacks have
non-small probability under the proposed feasible generator.

This is one synthetic benchmark, not industrial workload validation or a best-
classical lower bound. No quantum circuit or runtime comparison was performed.
The [circuit construction 06](exploration/phase_4/CIRCUIT_NATIVE_PRICING_06.md)
remains QRAM-free but does not yet have a supported application advantage. Larger
members of a fixed-capacity benchmark are not the next default experiment. A new
pricing regime must be independently useful and survive exact/approximate classical
bypasses before further quantum development.

[Current work order](work_orders/CURRENT.md) · [Status](STATUS.md) ·
[Phase-4 index](exploration/phase_4/README.md)

## Reproduce the executed workload

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/pricing_workload_v1/verify.py
```

Python 3.10+, NumPy and SciPy. The [report](experiments/pricing_workload_v1/REPORT.json)
contains the two operation inventories, explicit 48-bin assignments and offline
probability diagnostics. The [source notice](experiments/pricing_workload_v1/SOURCE_NOTICE.md)
attributes the single normalized OR-Library input and its extraction limits.
`--full-trace` also prints the acquired pricing trajectory; no output files are
written. The final checker ran twice identically and rejected -O/-OO and invalid
inputs. Earlier scientific suites were not rerun.

## Preserved boundaries

[AGENTS.md](AGENTS.md) and [hardware decision 05](exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md)
remain binding. Direct samples and reusable classical objects are both allowed.
The [handover](HANDOVER.md) remains a dated pre-selection snapshot, not a second
current work order. The coherent-RAM sparsifier is parked, the emitter covariance
remains closed, and the two spin-offs own their independent projects.

Only this parent repository is writable here. No new repository, release, branch
merge, manuscript, or hardware commitment is needed. All prior science,
[LICENSE](LICENSE), provenance and third-party rights remain preserved.
