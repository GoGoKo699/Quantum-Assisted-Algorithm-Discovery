# Current status

29 September 2026 — phase-4 task-matched measurement comparison.

**No useful quantum advantage, new sensing experiment or publication result is
established. Manuscript preparation remains on hold.**

[Note 02](exploration/phase_4/TASK_MATCHED_READOUT_02.md) defines an exact affine
signal-plus-nuisance model with supplied template shapes. A nuisance-projected
scalar estimate can be implemented by one preselected homodyne direction per
independent temporal mode. Exact Gaussian means and variances follow without
estimating nuisance amplitudes. This is standard regression/measurement algebra,
not a novel nuisance-parameter theory or a full joint-record reconstruction.

For symmetric two-mode squeezed probes and balanced Bell readout, an explicit
unequal-pure-loss covariance calculation bounds the noise below by a quantity
already exceeded in sensitivity by aligned single-mode squeezing. Both same-total
and same-sensing-photon comparisons are included. The competitor uses squeezing,
so it is NOT a comparison of all quantum techniques with classical light.
No theorem against arbitrary entangled states or measurements is asserted.

Known nuisance shapes, stable phases, selectable squeezing angles, independent
modes and no back-action are explicit assumptions. The actual backscatter experiment
fits a nonlinear unknown phase; it is not solved by granting that phase in advance.
Calibration error can dominate the gain. Adaptive acquisition, nonlinear fitting,
unknown-source distribution learning and arbitrary post-hoc queries remain open,
and have substantial existing metrology precedents. No new matched benefit there
has been established here. Physical-source access remains scope-separated; the
original circuit-model rules are unchanged.

The [work order](work_orders/CURRENT.md) now selects the in-scope implicit-graph
access comparison from Screen 01. This is a priority decision, not a universal
rejection of sensing or a reopening of the closed emitter calibration.

## Executed evidence

The new checker ran twice with identical output and rejected -O/-OO and six invalid
inputs. It uses exact SymPy arithmetic for one finite nuisance projection and a
noise square identity, plus six analytic Gaussian covariance controls and a phase-
drift negative control. The [report](experiments/task_matched_readout_v1/REPORT.json)
contains no sampled signals, fitted waveform, adaptive pilot, optical circuit,
experimental performance or timing. No historical scientific verifier was rerun.

The note records primary-source scope. Relevant PDF text was inspected; screenshot
attempts failed and no plotted performance values were used. This was not an
exhaustive novelty audit or an independent validation of physical hardware assumptions.

The [preceding ledger](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/cdc3f30129e2428759aa97213ee4ab296528cd0b/STATUS.md)
and all historical notes and reports remain immutable. The phase-3 closeout,
handover, independent spin-offs, licenses and rights are preserved. No new repository,
merge, release, external contact, paid work or manuscript is part of this checkpoint.
