# Quantum-Assisted Algorithm Discovery

**Can quantum computation discover a useful reusable classical method more
cheaply than a strong classical alternative?** The output should run on ordinary
computers and meet a need that exists independently of this project.

**Status: exploratory. No useful quantum discovery advantage is established.
Manuscript preparation remains on hold.**

## Current sampling contract: examples become verified classical logic

The [consumer contract](exploration/phase_3/SAMPLING_TO_VERIFIED_LOGIC_08.md) tests
whether quantum-produced examples can help a classical synthesis pipeline learn,
repair and formally verify reusable Boolean logic. Manthan provides an existing
classical consumer. Its sample-source sensitivity is a published precedent, not
our performance result; modern classical preprocessing and CMSGen must remain
in the comparison.

The [latest encoding audit](exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md) checks
an actual clause prefix from the supplied USB-named benchmark. It defines 85
internal bits deterministically. Naively guessing them creates an artificial
2^-85 uniform-acceptance penalty. A small reversible evaluator removes that
penalty without changing the uniform conditional law. Classical processing can
use the same definitions; this is a producer correction, not quantum advantage.
The circuit counts cover only the prefix, not a complete sampler.

Native Manthan/CMSGen installation remains incomplete because runtime source
transfer failed. Available native Z3 checked only the prefix identities. There
are no native synthesis timings, trained classifier or final verified program.
The whole benchmark and original signal/application mapping were not verified.
Its filename is not a substitute for useful workload provenance.

The [work order](work_orders/CURRENT.md) retains one instrumented native comparison
as the next task. It must price the residual sampling problem after legitimate
classical simplification, learning, repair and checking. No additional small
logic demonstration is a substitute for that baseline. Identical full training
batch laws give identical learner behavior in law; useful differences from a
new law must survive strong classical sample-source substitution.

## Reproduce the executed prefix diagnostic

Python 3.10+, standard library; --native additionally requires installed libz3:

```sh
python experiments/sampling_encoding_v1/verify.py
python experiments/sampling_encoding_v1/verify.py --native
```

The [report](experiments/sampling_encoding_v1/REPORT.json) records exact gate checks,
reversible basis controls and two native equivalence decisions. The
[provenance and upstream notice](experiments/sampling_encoding_v1/PROVENANCE.md)
distinguish the transcribed prefix from the unacquired complete source. These are
not native synthesis, independent UNSAT-proof replay, quantum hardware tests or
performance benchmarks. Earlier verifiers were not rerun; their files are unchanged.

## Parked work and organization

The [battery route](exploration/phase_3/INTERFACIAL_REFERENCE_DECISION_06.md) and
[operator candidate](exploration/phase_3/MECHANISM_SCREEN_01.md) remain parked.
The [battery archive replay](exploration/phase_3/ARCHIVE_REPLAY_04.md) and uploaded
archive remain available; no new upload is needed.
[Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates)
and [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction)
are independent projects and own their further development.

Scientific phase 3 uses `research/prx-quantum-phase2`. The
[project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md)
and [parent charter](exploration/phase_2/CHARTER.md) govern the exploration.
`main` is the entry point, not a merged copy of later research.
[STATUS.md](STATUS.md) summarizes claims and links pinned historical ledgers.
Phase-2 [Note 27](exploration/phase_2/SOURCE_AWARE_DESCENT_27.md) remains closed.
Earlier proofs, code, data, reports and third-party notices are preserved, as is
the original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin.
Only the parent repository may be modified in this project context.
