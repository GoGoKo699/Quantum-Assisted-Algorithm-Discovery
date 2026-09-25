# Sorting-network completion: an unsupplied target and a bottleneck audit

25 September 2026. Successor to the completed eleven-bank filter screen.

## Research decision

The candidate task is to find an **18-input sorting network with at most ten comparator layers**, if one exists. The current author-maintained compilation and the recent 28-input construction report retain the depth gap 10--11 for 18 inputs [1,2]. The latter explicitly reports not improving it. These are the sources checked on this date, not a proof that no unindexed construction exists. Unlike the previous supplied filter instances, the desired construction is not given to the search.

This is a mathematical synthesis target, not yet a certified practical quantum-advantage workload. Sorting networks have independently motivated uses and can be used as small kernels inside larger sorting routines [3]. Nevertheless, replacing an eleven-layer kernel with ten layers need not improve whole-program runtime: comparator count, instructions, routing and data movement remain relevant. A concrete execution-level acceptance test and an end-to-end comparison with strong native classical synthesis are still missing. There is no obligation to solve a lower-bound/optimality problem to deliver a useful routine.

The current positive result is an exact, inexpensive classical prefix reduction and an incremental completion baseline. The principal negative result is that brute-force Boolean-input verification is the wrong quantum target for the successful control measured here. No new sorting network, speedup, quantum circuit, or favorable quantum resource estimate is claimed.

## 1. Primary-source audit

Wang's 2025 construction obtains a new 28-input depth-13 network using symmetry-aware prefix generation, a greedy extension and an optimized MiniSat encoding; the reported complete computation is under twenty minutes on a Mac mini M2 [1]. This is a useful modern classical discovery example, not evidence that every sorting-network task is hard. A costly proof that no smaller network exists would be a different workload from finding a usable network.

The public SorterHunter comparator lists provide two exact calibration certificates: 18 inputs / 78 comparators / 11 layers and 28 inputs / 159 comparators / 13 layers. Both are pinned to commit `392762f916688756242d90febced98ad157bc6d2`. `networks.json` transcribes only mathematical comparator lists; no solver implementation was imported. The listed 28-input schedule follows the pinned JSON rather than an assumed figure transcription.

Prefix-output reduction and the zero-one principle are established tools [1]. Counterexample-guided inductive synthesis is also prior work [4]. A recent FPGA study reports subsecond reduced-input verification for a particular 48-input configuration [5]; it is another reason not to compare a quantum verifier exclusively against scalar enumeration of all binary inputs. We did not reproduce that FPGA result, and its reduced-input conditions must be retained.

## 2. Exact reachable-state computation

Write a network as a prefix P followed by a suffix S. It suffices to require that S sort

    R(P) = { P(x) : x in {0,1}^n }.

If this holds, P;S sorts every binary input and hence, by the zero-one principle, all inputs from a total order. Integer bit 0 is the top/minimum wire in our implementation. Comparators always send min to the smaller wire index. Each layer is a disjoint matching; empty layers are allowed. Inputs such as floating-point NaNs require a separately defined total-order comparator and are not implicitly covered.

`prefix.py` computes R(P) by tracking independent connected components of the processed comparator graph. Initially each wire has two states. If a comparator joins two components, form their Cartesian product, then apply the comparator. If its wires are already in one component, map that component's state set directly. Components are independent because no processed comparator has crossed between them; induction proves the representation exact. Duplicated component outputs are merged.

This avoids materializing all 2^n inputs for the selected prefixes. General prefixes can still have exponentially large components; the implementation stops at an explicit two-million-state cap rather than silently approximate.

| Exact quantity | 18-input certificate | 28-input certificate |
|---|---:|---:|
| All initial Boolean inputs | 262,144 | 268,435,456 |
| Outputs after first six layers | 243 | 928 |
| Unsorted outputs after those six layers | 224 | 899 |
| Outputs after the complete known network | 19 | 29 |
| Peak component inputs during the complete reduction | 2,760 | 2,905 |
| Comparator-pattern evaluations during reduction | 30,947 | 57,587 |

The final output sets equal the n+1 sorted Boolean words exactly. The state counts, not a quantum simulation, are reproduced by the default verifier.

A quantum algorithm must be compared with this reduced workload where applicable, not with 2^28 independent simulations. Loading the reduced set coherently would itself require an implementation; no free quantum memory oracle is assumed.

## 3. Independent incremental completion baseline

`completion.py` builds Boolean variables for the presence of each comparator in each suffix layer. Pairwise exclusions ensure disjointness. Given a reachable prefix output, conditional AND/OR equations describe the Boolean comparison gates, and the last wires are constrained to the sorted word of the same Hamming weight.

The baseline starts with at most sixteen reachable unsorted patterns. It keeps one native Z3 solver alive, obtains a candidate suffix, tests it against every reachable prefix output, and appends up to sixteen failing examples before the next solve. Previously learned solver information is retained classically. A counterexample excludes every suffix failing that example, not only the last proposal. This is standard counterexample-guided synthesis [4], not a new quantum method.

Sorted patterns can be omitted because every forward comparator preserves a sorted input. Optional reflection symmetry and an adjacent-only final layer are explicit search restrictions; we do not silently claim they preserve all possible fixed-prefix completions. An additional run removes both restrictions.

The backend is the installed native Z3 4.13.3.0 C library, accessed with this project's earlier original wrapper. **This is not execution of Wang's synthesizer, SorterHunter, or their optimized encodings.** In particular the oneUp/oneDown, window/permutation and last-two-layer optimizations reported in [1] were not ported. A generic backend alone is not the strongest classical comparator.

## 4. Actual observations

`observations.json` contains complete run traces and the successful circuit, not portable timing expectations. The first five restricted runs use per-call five-second timeouts; the unrestricted run uses ten seconds. Solver timeouts are per solve, not full-task deadlines. Total observed wall time includes incremental encoding and testing but excludes prefix reduction and solver/header construction occurring before the timer.

| Known prefix fixed | Requested total depth | Additional restrictions | Observed outcome |
|---|---:|---|---|
| 18 inputs, first 6 layers | 10 | reflection + adjacent final layer | Native UNSAT after 32 examples |
| 18 inputs, first 6 layers | 10 | none | Native UNSAT after 48 examples |
| 18 inputs, first 5 layers | 10 | reflection + adjacent final layer | UNKNOWN at 48 examples |
| 18 inputs, first 4 layers | 10 | reflection + adjacent final layer | UNKNOWN at 64 examples |
| 18 inputs, first 6 layers | 11 | reflection + adjacent final layer | Complete verified suffix, 6 SAT rounds |
| 28 inputs, first 6 layers | 13 | reflection + adjacent final layer | UNKNOWN at 32 examples despite known feasible completion |

The unrestricted UNSAT response excludes a four-layer suffix for **that exact six-layer prefix**, assuming the encoding and solver are correct. It is not a proof that an arbitrary 18-input depth-ten network is impossible. No independently checked UNSAT proof trace is supplied; small exhaustive encoding checks are supporting validation, not a replacement for such a proof.

The successful eleven-layer control uses 80 comparators, worse in count than the supplied 78-comparator certificate. Its suffix was not given to the solver, but discovering another known-feasible solution is calibration, not a useful new routine. Its complete suffix is checked on all 243 reachable prefix outputs.

Most importantly, the 28-input positive control times out even though its known suffix demonstrates feasibility. Thus the open-target UNKNOWN results cannot be used as evidence of intrinsic classical hardness or quantum opportunity. Different seeds, encodings, timeouts and hardware can change these observational outcomes.

## 5. Which part is actually expensive in the successful control?

For the measured 18-input eleven-layer control:

    total timed work                 2.026204459 seconds
    six candidate-verification scans 0.004331832 seconds
    native solving                   1.733391727 seconds

Verification is approximately 0.21379% of the timed work. If we replaced only those six scans by a free operation, keeping all other work and the trajectory unchanged, the maximum speedup would be

    T / (T - T_verify) = 1.002142485...

This is an elementary accounting bound for one measured control, not a general sorting-synthesis limitation. It does not constrain an algorithm that changes candidate generation, prefix selection or the trajectory. It does reject an argument that this particular computation has a practically significant verification bottleneck merely because the raw input domain has 2^18 elements.

Accordingly, the prospective quantum role is choosing a successful construction/remaining comparator arrangement while retaining effective classical deductions, not accelerating an almost-free verification loop. No efficient coherent version of incremental CDCL learning is assumed, and no square root of classical solver statistics is interpreted as a quantum complexity theorem.

## 6. Validation and commands

Default checks use only Python's standard library:

    python experiments/sorting_completion_v1/verify.py

They compare component-factored reachability against an independent list-of-bits simulator for all 1,211 comparator networks of zero through three layers on two, three and four wires. There are 152 independently enumerated suffix-completion questions covering optional symmetry and final-layer restrictions. Both published networks are checked exactly through their reduced output sets and on 1,024 sampled inputs each. The stored 80-comparator completion is checked on all 243 prefix outputs.

To compare all 152 small questions with the native SAT encoding:

    python experiments/sorting_completion_v1/verify.py --solver

All 42 SAT and 110 UNSAT responses agree with independent enumeration in this run; all SAT suffixes are checked directly. This optional mode requires a discoverable Z3 C shared library. Models and runtimes on the larger observational cases are not deterministic fixtures.

To repeat an unrestricted first-six-layer experiment without overwriting evidence:

    python experiments/sorting_completion_v1/completion.py --n 18 --prefix 6 --depth 10 --no-symmetry --unrestricted-last --timeout-ms 10000 --rounds 10 --output /tmp/new-sorting-run.json

New runs additionally store the exact encoded-example list. The original observational files predate this metadata addition; their constraints and model semantics are unchanged. Existing paths are never overwritten. Do not use Python -O/-OO. The code is research software with explicit domain/cap limits, not a production solver.

This turn reran the supplied previous `depth2_cover_v1` verifier successfully. Older optional-Z3 checks and long historical trajectories were not rerun.

## 7. Next substantive test

Keep 18-input depth-ten synthesis as a **provisional unsupplied structural target**, not a committed practical application or a proven quantum-advantage instance. The next experiment must reproduce a strong native classical completion baseline on the known 28-input control before interpreting timeouts on the open target. It must explore a justified diverse prefix family rather than fix an arbitrary doomed prefix or scale a weak encoding's timeout.

Specify an independently relevant execution metric before claiming practical benefit from any new network. Depth counts comparator layers, not actual CPU cycles or FPGA frequency. Account for the final routine's comparator count and mapping. Finding a useful witness is the target; proving global optimality is not automatically required.

Only then select a quantum acceleration mechanism for the measured remaining bottleneck. Include classical prefix generation, learned information, coherent predicates, initialization, all iterations, output verification and matched parallel resources. None of the earlier raw-flip/helper-state qubit counts transfers to sorting completion.

## References

[1] Chengu Wang, *Depth-13 Sorting Networks for 28 Channels*, arXiv:2511.04107v2 (2025). https://arxiv.org/html/2511.04107v2 . Primary implementation: https://github.com/wcgbg/sorting-network-n28d13 . Paper read; native implementation not executed.

[2] Bert Dobbelaere, *List of sorting networks*, author-maintained table checked 25 September 2026. https://bertdobbelaere.github.io/sorting_networks_extended.html . Comparator data: https://github.com/bertdobbelaere/SorterHunter at the pinned commit in `PROVENANCE.json`.

[3] Michael Codish, Luis Cruz-Filipe, Markus Nebel and Peter Schneider-Kamp, *Applying Sorting Networks to Synthesize Optimized Sorting Libraries*, arXiv:1505.01962 (2015). https://arxiv.org/abs/1505.01962 . Small-network reuse does not automatically convert fewer comparators/layers into faster software.

[4] Armando Solar-Lezama, *Program Synthesis By Sketching* (2008), and the author's counterexample-guided synthesis course notes. https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-177.html ; https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm . Standard generate-check-learn architecture, not novelty here.

[5] Philippos Papaphilippou, *Highly Parallel Sorting Network Verification Using FPGAs*, Chips 5(1),5 (4 February 2026), DOI 10.3390/chips5010005. https://www.mdpi.com/2674-0729/5/1/5 . Author-reported hardware results, not reproduced here.
