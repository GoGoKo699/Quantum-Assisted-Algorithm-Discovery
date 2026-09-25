# Publication plan: a result, not a sequence of probes

25 September 2026. Working research plan, not a submission announcement.

## Target claim

Working title: **Quantum Search over Shared Choices in Program Extraction**.

The desired paper would show that a precisely defined structural reduction preserves valuable classical reasoning while leaving a quantum-search problem with a demonstrably better complete resource bound in an identified regime. It must say which parameter controls search, which parameters control coherent implementation, and which classical algorithms remain better elsewhere.

The original project objective remains useful quantum-assisted discovery of reusable classical methods. This plan does not require one paper to establish all quantum computing usefulness, and does not require a quantum hardware demonstration, world-record multiplication identity, or unrestricted exponential separation. Nor does it settle for a known Grover theorem attached to an application name.

## What is on the table now

The sharing-core checkpoint derives an exact decomposition into private expression forests and shared class decisions, an ordering-aware classical subset DP for cyclic alternatives, and an activation objective for acyclic support. Standard quantum search gives an acyclic O(2^(h/2) poly(N,b)) upper bound relative to 2^h activation enumeration. No free QRAM, free verifier, or h-qubit whole-machine claim is used. However, the reduction's novelty and its advantage over stronger classical extraction methods are not established. The available public calibration is easy and actually favors representative enumeration over enumerating activation subsets.

This is a candidate theorem package, not a publishable significance claim. The exploratory filters, raw walks, and supplied-identity reconstructions are background calibration, not separate sections masquerading as several contributions.

## Main paper versus stronger downstream claim

**Theory-led first paper:** an original algorithmic or structural theorem with complete circuit-model access/cost accounting, meaningful comparison with existing exact algorithms, and evidence that the parameter regime is relevant. This can be legitimate before fault-tolerant hardware exists. A conditional complexity comparison must be labeled conditional. A speedup over one enumerator is not a speedup over classical computation.

**Stronger application paper/claim:** a qualifying unsupplied or held-out classical routine, measured time-to-quality against current native methods, verified output semantics, full quantum logical/physical resource assumptions, and a useful mapped execution benefit. This is a stronger milestone, not a prerequisite silently imposed on all theory publication.

Do not describe all previous negative screens as evidence that quantum algorithm discovery is impossible. They excluded particular weak targets. A systematic negative paper would itself need comprehensive scope and independent significance; that is not the chosen fallback.

## Three acceptance gates before submission drafting

### Gate 1: exact novelty and classical comparison

Compare the shared-boundary decomposition against the actual algorithms and reductions in DOI 10.1145/3689801, arXiv:2408.17042, general AND/OR DAG / circuit conditioning, and relevant extraction implementations. Record equivalences, separations, and prior parameters. Establish a defensible original contribution; if it is already implied by existing work, keep it as preprocessing and do not market it as the paper's main theorem.

For the acyclic case, the square-root enumeration bound is a standard corollary. The main result must improve something nontrivial: the structural parameter, coherent memory/time, retention of classical pruning, extension to cyclic alternatives, or a complete application regime with genuine resource benefit. Rebranding a generic corollary is insufficient.

### Gate 2: complete algorithm and falsifiable regime

State an explicit input family and whether its support is acyclic. Define nonnegative costs and exact bit widths. Compile the actual predicate, record graph-dependent work/space, and include classical preprocessing and certificate reconstruction. Where cyclic alternatives are needed, establish a valid ordering-aware quantum procedure; do not apply the acyclic activation formula or enumerate all orders and call it faster than the classical subset DP.

Compare with the best relevant parameterized/dynamic-programming algorithms and classical representative enumeration, not only the activation baseline. State memory limits symmetrically. Produce either a justified winning regime or a precise reason the proposal requires a different mechanism.

### Gate 3: externally supplied workload evidence

Freeze a small primary-source benchmark subset BEFORE tuning, with a public calibration split and held-out instances. Run full current native extraction methods where the claim depends on them, retain preprocessing/warm starts and parallelism, and measure time to the SAME preregistered cost threshold. Do not count proof-of-optimality time when finding an adequate routine is the actual need. If only theorems are claimed, use benchmark parameter measurements to motivate scope rather than to imply an empirical speedup.

Separate additive extraction cost from compiled execution cost. For a claim about improved deployed algorithms, verify sound semantics and map the output to the actual timing/area/runtime metric. A public graph already containing known optimum witnesses is a calibration, not a new discovery.

## Manuscript outline to build against

1. Problem and precise contribution statement: quantum search after classical structural compilation.
2. Input model and prior-work comparison: trusted equivalence versus structural extraction; no free access assumptions.
3. Shared-boundary theorem and its exact limits; cyclic counterexample.
4. Complete quantum method and matched classical bounds.
5. Reproducible evidence and declared threshold/parameter regimes.
6. Limitations: difficult private input access, large shared cores, cycles, semantic and hardware mapping.

The contribution statement, theorem/proof, and missing-evidence ledger should be drafted now. Do not write a celebratory abstract claiming significance before Gates 1-3 justify it.

## Venue strategy

A quantum-algorithms paper is the primary route. *Quantum* is a plausible venue to evaluate only if the completed contribution is significant; its official criteria explicitly require an advance beyond correct incremental work. The present checkpoint is not at that threshold, and no acceptance prediction is made. See https://quantum-journal.org/instructions/authors/ and https://quantum-journal.org/instructions/referees/ (checked 25 September 2026).

If the substantial contribution instead proves classical and delivers a better extractor, a programming-languages / synthesis paper may be the honest outcome. Do not append a token quantum paragraph to disguise a classical result, and do not lower the scientific standard just to obtain a paper.

## Stop the unbounded exploration loop

Keep e-graph extraction as this branch's scope through the three gates. Do not open another family or compile another unrelated oracle because a benchmark proves easy. The sorting-completion work on main remains separate and must not be overwritten. At the next publication checkpoint, answer which gate moved with evidence, not how many files were added.

No time estimate, journal submission, arXiv posting, outside contact, paid computation, or automated background work is authorized by this plan.
