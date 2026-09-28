# Current task: sample-source comparison for verified classical logic

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read the [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md),
[parent charter](../exploration/phase_2/CHARTER.md), and
[sampling-to-verified-logic contract](../exploration/phase_3/SAMPLING_TO_VERIFIED_LOGIC_08.md).

## Selected bounded workflow

Investigate quantum-generated satisfying examples as input to a Manthan-style
Boolean functional synthesizer. The saved result is an ordinary verified Boolean
program/circuit, not an imitation of the quantum sampler. This refines the earlier
proposal-learning sketch while preserving classical-only deployment.

The existing classical pipeline is documented, and a historical sample-source
substitution study changes full synthesis performance. That motivates a test,
not a quantum advantage or an end-user improvement already established here.
Use current Manthan/CMSGen and strong direct synthesis alternatives, not only the
older QuickSampler comparison. Keep preprocessing, unique-function extraction,
repair and independent final verification enabled.

## Next bounded execution

1. Establish a small native Manthan/CMSGen installation and run the official smoke
   test as an installation check only. No native installation or run has yet been
   completed. Pin code versions and preserve notices in any local or redistributed
   derivative. Do not modify an upstream repository from this project.
2. Trace one application-derived benchmark to its source specification and X/Y
   partition. The supplied USB-named fixpoint file is only a candidate for this
   check; its name alone is not application validation. A random SAT or deliberately
   easy diagnostic cannot stand in for the final workload.
3. Instrument sample generation, learning, repair and final checking. Record
   total time to a verified function and its size/depth where relevant. Compare
   classical sample producers within the same consumer first. If preprocessing
   already solves the instance, report it rather than disabling that strength.
4. For a surviving bottleneck, price the explicit quantum sampler, including
   reversible relation evaluation, product-state preparation, reflections,
   uncomputation, unknown-success scheduling, finite precision, shots, failed
   trials, validation and adaptation. A simulator's time is not quantum runtime.

The first quantum reference producer is standard weighted amplitude amplification.
Its square-root bound is relative to rejection, not to modern SAT sampling.
Identical full training-batch laws imply identical downstream behavior in law;
then only acquisition cost can improve. Different quantum training laws must be
compared with task-equivalent classical data, not only Born-law imitation.
Equal input weights do not force uniform feasible-input marginals. Uniformity,
validity, informative coverage and speed of verified compilation are distinct.

Correctness comes from the final universal error query, not a sample test. Charge
its solver/translation cost and seek independent proof replay where supported.
Timeouts are not certificates. A low sampling acceptance mass, a large solution
space or a difficult-to-simulate quantum distribution is not evidence of a useful
classical discovery bottleneck. Do not build a new synthesizer or large SAT census.

## Evidence and preserved boundaries

The new standard-library finite checker was run twice with identical JSON and
rejects -O/-OO. It checks 4096 finite synthesis contracts and 2040 ideal-amplitude
round states, retaining 44 zero-success cases; it is not native synthesis, a
noisy/gate-level simulation, or a speedup experiment. The note records full scope
and hashes. Run `python experiments/sampling_synthesis_v1/verify.py` for that scope.
Root and historical scientific suites were not rerun; their files are unchanged.

The battery and small-operator routes remain parked. Both classical spin-offs
own their further development. Phase-2 Note 27 remains closed. The uploaded
battery archive is already verified; do not ask for it or reopen archive curation.
Preserve earlier proof notes, code, data, reports, manifests, licenses and rights.
Modify only Quantum-Assisted-Algorithm-Discovery. No external contact, paid or
unattended work, manuscript revival, submission, release, branch merge or
repository administration change is authorized.
