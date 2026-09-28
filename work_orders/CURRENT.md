# Current task: native synthesis profiling with a structure-preserving sample source

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md),
[consumer contract](../exploration/phase_3/SAMPLING_TO_VERIFIED_LOGIC_08.md), and
[encoding audit](../exploration/phase_3/SAMPLING_ENCODING_AUDIT_09.md).

## Completed diagnostic, not a completed native benchmark

A 376-clause prefix of Manthan's USB-named QDIMACS example exactly defines 85
internal bits as functions of 119 input bits. Guessing them independently adds
a factor 2^-85 to uniform acceptance. An independently constructed 410-gate
reversible evaluator removes that penalty, with 23 clean scratch bits. These
counts describe only the inspected prefix. The same structure is usable
classically; the correction is not a useful quantum speedup or a new technique.

The uniform prepared-and-conditioned distribution is unchanged. Arbitrary
nonuniform weights on dependent bits require the induced weights to be retained;
do not transfer the uniform factor to weighted CMSGen calls. Do not claim that
this prefix solves the entire formula or that its USB name proves deployment value.
The complete source file and original signal mapping remain to be checked.

Native Manthan/CMSGen installation and its smoke test were NOT completed.
Runtime Git access failed on DNS, and an inspected successful upstream dependency
workflow supplied no downloadable artifacts. The already installed native Z3 was
used only for two prefix-equivalence queries, not as a substitute claimed to be
Manthan. No synthesis phase timings, trained classifier or final program exist.

## Next bounded execution

Obtain a working native execution environment before adding further small logic
demonstrations. Pin Manthan and its native dependencies and preserve their notices.
Do not modify an upstream repository. Run the official smoke test as an installation
control, not as application or speedup evidence.

For one application-provenance-checked benchmark, retain preprocessing, unique
extraction, learning, repair and final universal checking. Trace the source
specification and X/Y meanings. A matching filename in another benchmark collection
is insufficient to establish an identical instance or deployable output.

Measure sample acquisition, learning, repair and checking separately, together
with time to a verified function and relevant output size/depth. Preserve the
same classical consumer when changing the sample source. Allow stronger direct
synthesis and task-equivalent classical examples; do not compare only against
rejection or a weakened historical sampler. Complete successful source-file hash
validation before reporting any full-instance run.

For a surviving quantum opportunity, compute deterministic wires rather than
sample them. Price preparation and its inverse, the residual predicate, reflections,
finite precision, unknown-success scheduling, all attempts, adaptation, validation
and output. The prefix circuit is not a whole-oracle resource estimate. If
preprocessing solves the task, retain that result rather than disabling it.

Same-law sample replacement can change acquisition cost, not the learner's law.
A different sample law needs evidence that its useful learning/repair benefit
survives a strong classical source substitution and total cost comparison. A
small raw acceptance probability caused by encoding is not discovery hardness.
No new algorithm, useful quantum advantage or application result is established.

## Checks and boundaries

The final `experiments/sampling_encoding_v1/verify.py --native` ran twice with
identical JSON; default mode passed. Exact structural matching, 6320 local truth
assignments, 128 reversible basis controls, 10880 single-wire fault controls and
four malformed cases passed. Z3 4.13.3.0 returned two UNSAT mismatch decisions;
no independent proof trace was replayed. -O/-OO, an altered fixture and an incorrect
complete-source file were rejected. Successful optional --source was not run.
These are prefix diagnostics, not synthesis or timing results. Earlier sampling,
root and historical suites were not rerun; their code and reports are unchanged.

The battery and operator routes remain parked. Both classical spin-offs own their
further work. Phase-2 Note 27 stays closed. The uploaded battery archive is already
verified; do not request it again. Preserve previous evidence, licenses and rights.
Modify only Quantum-Assisted-Algorithm-Discovery. No outside contact, paid or
unattended work, manuscript revival, submission, release, branch merge or repository
administration change is authorized. No new repository or spin-off is needed.
