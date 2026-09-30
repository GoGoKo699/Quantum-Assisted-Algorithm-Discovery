# Quantum-Assisted Algorithm Discovery

**Can quantum computation obtain useful information more effectively than strong classical alternatives?**

**Fault-tolerant circuits; no assumed fast QRAM.** No useful end-to-end quantum
advantage is established. Manuscript preparation remains on hold.

## Current bounded hypothesis: packing columns from explicit circuits

[Circuit-native pricing 06](exploration/phase_4/CIRCUIT_NATIVE_PRICING_06.md)
specifies a possible quantum subroutine inside a classical bin-packing optimizer:
return a feasible item subset with negative reduced cost. Sizes and current dual
prices become fixed gate constants in sequential comparisons and additions; the
classical master and its column pool are not queried in superposition.

The feasible-pattern generator and amplitude amplification are prior methods,
and quantum-assisted column generation also has prior literature. This is a
hardware-admissible comparison to investigate, not a new algorithm or demonstrated
application advantage. Circuit preparation, inversion, precision, routing, price
updates, and repeated calls remain explicitly charged.

The classical side is not uniform enumeration. Fractional/core bounds, dynamic
programming, approximation schemes, previous columns, and stabilized or coordinated
pricing are allowed. A fixed improvement margin already has a polynomial classical
finder, and a scaled dual can certify an adequate master gap without exact pricing.
The key test is whether useful near-boundary calls remain difficult AFTER those
bypasses, and whether faster column finding would reduce total solver work.
A failed quantum search is not a no-column certificate.

[Current work order](work_orders/CURRENT.md) · [Status](STATUS.md) ·
[Phase-4 index](exploration/phase_4/README.md)

## Executed evidence

```sh
python experiments/circuit_pricing_v1/verify.py
```

Python 3.10+, standard library. The [report](experiments/circuit_pricing_v1/REPORT.json)
contains exact finite reduced-cost, core, feasible-law, approximation-margin and
scaled-dual controls. The final checker ran twice identically and rejected -O/-OO.
There were no real pricing logs, quantum circuits, native optimizers, or timing
benchmarks. Historical scientific verifiers were not rerun.

## Preserved scope and decisions

[AGENTS.md](AGENTS.md) and [hardware decision 05](exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md)
remain binding. Direct samples and reusable classical artifacts are both permitted.
The [handover](HANDOVER.md) is the preserved pre-selection snapshot; its unselected
next-step wording is historical. The live work order above governs continuation.

The RAM-dependent sparsifier remains parked and the emitter-covariance closeout
remains in force. Physics/transport are screened alternatives, not parallel default
programs; unknown-source sensing is not substituted for a classical input task.
[Reproduction guidance](handover/REPRODUCING.md) and the
[exploration index](exploration/README.md) retain all earlier evidence.

The working branch is `research/prx-quantum-phase2`; its name is historical.
`main` routes to the working branch. Only this parent repository is writable here;
both classical spin-offs retain their independence. No new repository, manuscript,
release, or branch merge is needed. [LICENSE](LICENSE), prior science, and all
third-party rights remain unchanged.
