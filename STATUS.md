# Claim ledger

## Current checkpoint: smooth response compression, 28 September 2026

[Note 20](exploration/phase_3/SMOOTH_RESPONSE_COMPRESSION_20.md) completes a bounded
smooth alternative to sharp-band classification. A real function of the FULL
Liouvillian preserves its spectral probabilities while moving line positions.
If its core frequency error is delta inside |omega|<=kappa, the Cauchy(gamma)-
broadened response differs in TV by at most
min(1, ||Lo||^2/kappa^2+delta/(pi gamma)). The same bound holds after common binning.
The alternating-offset collective response has ||Lo||^2=d^2 exactly.

An existing bounded odd amplitude-multiplication polynomial supplies a quantum
encoding of K=2 kappa P(L/alpha) without a smallest-gap or cutoff-edge-margin
promise. It retains a positive full spectral law and is not state postselection.
It is not a smooth projector inserted into Note 19, a smaller Hilbert space,
or a new effective physical spin Hamiltonian. Tail probability is paid for, not
renormalized away. Physical linewidth and the useful output are unchanged.

The generic transform-then-simulate budget is ~(alpha/kappa)(1+kappa/gamma),
so the leading alpha/gamma cost remains. This familiar cancellation and the
generic oracle-transform restriction are explicitly attributed to prior work.
The latter does not lower-bound state-specific sampling or an explicit spin
family against every classical/quantum algorithm. No gap-independent speedup,
quantum-classical separation, publication priority or measured benefit is claimed.

The [current work order](work_orders/CURRENT.md) asks for a physical-locality
comparison: a positive finite-window approximation of the collective response,
including cross terms and boundary error, against direct local quantum sampling
and strong classical methods. Generic cutoff engineering is not an indefinitely
active workstream. No locality-based TV result or new useful regime is established
by Note 20. Direct samples and model-first analysis remain authorized.

## Executed evidence

The independent NumPy diagnostic ran twice with identical JSON and exit code zero;
-O/-OO refused execution. Three fixed n=2,4,6 chains supplied six moment checks,
six smooth-cap comparisons and three bounded cubic-polynomial comparisons.
Eight continuity checks, four Lorentzian translation checks, six invalid-input
rejections and a state-filtering negative control also passed.
The [report](experiments/smooth_response_v1/REPORT.json) records scope and results.

The analytic C2 cap is not the efficient amplification polynomial from the cited
theorem. No scalable polynomial synthesis or phase sequence was implemented.
The numerical controls are complex128 at tolerance 3e-10, not interval certificates.
The continuous-law result follows from the proof rather than finite bins.
Both runs emitted an unrelated runtime-startup warning; the research diagnostic
completed normally and its report was deterministic.

No experimental spectrum, native application, climate run, quantum circuit,
hardware, model training or timing benchmark was used. No upstream code or data
was imported, and no older verifier was rerun. Primary spectral-amplification and
QSVT statements were inspected, with two successful PDF-page screenshots and one
failed screenshot attempt; no experimental figure was digitized. Source scope
and hashes are in the note. This is not an exhaustive priority audit.

## Preserved historical evidence

The preceding ledger and its links are pinned at the
[pre-smoothing checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/4628eb7a18823bbe3b974c07d11fc671da3ecb9e/STATUS.md).
Notes 15-19 and all earlier source, proofs, checks and reports remain unchanged.
Their current/next headings describe their original checkpoints, not concurrent
work orders. Climate/dynamics remain open; Manthan is paused, battery/operator
routes parked, both classical spin-offs independent and Phase-2 Note 27 closed.
Manuscript preparation remains on hold. Earlier licenses and third-party rights
are retained. Only the parent repository is modified; no outside contact,
paid/unattended work, release, merge or new repository is part of this checkpoint.
