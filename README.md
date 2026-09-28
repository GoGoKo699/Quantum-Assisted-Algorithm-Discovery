# Quantum-Assisted Algorithm Discovery

**Can circuit-model quantum computation produce information that makes a useful
computation materially more effective than strong classical alternatives?**

The [direct-sampling extension](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md)
allows samples themselves to be useful outputs. They need not first become a
classical program. Quantum use at sampling time is allowed and fully costed.

**Status: exploratory. No useful quantum advantage is established.
Manuscript preparation remains on hold.**

## Working method: model first, implementation later

For each example, first specify its mathematical model, useful output law,
quantum entry point, essential access/error costs, and strongest classical
comparison. Study a physically motivated parameterized family before choosing
an individual demonstration. A short derivation or structural limiting case
should establish where quantum integration might help before extensive data
collection, package installation or hardware engineering.

This ordering does not remove usefulness or allow an unpriced oracle. A concise
application anchor and explicit model assumptions remain necessary. Exact datasets
and native implementations are not prerequisites for the initial conceptual test.
See [AGENTS.md](AGENTS.md) and the [current work order](work_orders/CURRENT.md).

## Open mechanisms: selection versus direct quantum generation

The [open sampling screen](exploration/phase_3/OPEN_SAMPLING_SCREEN_14.md) keeps the
climate continuation test available and opens a separate mechanism check: direct
sampling of a quantum system's spectral response, with NMR as one motivating
consumer. A blocked dataset for one implementation does not block the parent
exploration. Neither mechanism is an established application advantage.

In the climate-conditioning route, quantum selection filters results of a classical
trajectory calculation. Direct probability evolution is a distinct possibility to
analyze through the Liouville/Koopman-von Neumann representation in
[Note 10](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md). In the spectral route,
quantum many-body evolution produces transition statistics. These representations
and spectral algorithms already have precedents; their adoption is not a novelty.

The immediate comparison is mathematical: which model structures, resolutions
and access conditions make the quantum representation useful against adequate
classical methods? The spectral screen should examine coupling structure,
observable support and finite resolution, not spin count alone. The dynamics
screen must compare with trajectory sampling, not only a full probability grid.
No specific compound, new simulator, separation or positive quantum cost margin
is selected. A measured instance and native benchmark follow a promising analysis.

## Climate investigation retained

The [heatwave task](exploration/phase_3/HEATWAVE_SAMPLING_CONTRACT_11.md),
[segment construction](exploration/phase_3/SEGMENT_SELECTION_12.md) and
[continuation-information audit](exploration/phase_3/CONTINUATION_INFORMATION_13.md)
remain unchanged. The planned empirical check compares legitimate continuations
of the same restart state before later selection. The France source packet is
still missing; no new climate-array analysis, variance estimate or runtime is
claimed. Its upload gates that empirical check, not model-level exploration.

## Evidence and organization

The model-first update changes priorities and documentation only. No new theorem,
numerical experiment, native package, quantum circuit, spectrum fit, performance
benchmark or scientific-verifier run is claimed. The earlier screen's analytic
identities and source-inspection limits remain in Note 14; they are not new runs.
[STATUS.md](STATUS.md) records scope and links pinned historical ledgers.

Manthan [profiling and encoding](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md)
remains paused. The [battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md)
and [operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
Both [Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The original
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [charter](exploration/phase_2/CHARTER.md) retain their historical objectives;
Note 10 explicitly extends the output contract and the current work order sets
the model-first sequence. `main` is an entry point, not a merged copy of later
work. Phase-2 [Note 27](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) stays closed.
Previous proof notes, code, data, reports, upstream rights and the original
[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, are preserved.
Only the parent repository may be modified in this project context.
