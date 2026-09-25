# Microscopic benchmark audit: predict a reaction, not just propagate a state

25 September 2026. Phase 2; PRX Quantum target; manuscript on hold.

This note investigates the microscopic cost left unresolved by the collision-event
record. It considers photofragmentation, not electron-impact scattering. The
incident preparation changes, so no thermal-event guarantee is transferred.
It is an evidence/target-selection note: no new quantum algorithm, molecular
calculation, classical runtime benchmark, or advantage is asserted.

## 1. Why inspect this example

Cyclobutanone photochemistry was a prospective community prediction challenge:
15 contributions preceded comparison with ultrafast electron-diffraction data.
The participants' 2026 analysis identifies electronic-structure choices as a
major source of differing predictions, while also reporting substantial
qualitative and some nearly quantitative classical successes [1]. Its scope is
the challenge submissions, not every subsequent method. Disagreement is not a
classical complexity lower bound.

A participant study varied electronic-structure methods within a surface-hopping
framework and obtained sharply different lifetimes and dominant product channels
[2]. This is evidence that the physical prediction can depend on how the
microscopic problem is approximated, not evidence that classical computation
cannot predict it. The decisive comparison must fix what preparation and
observable are being predicted and distinguish electronic from nuclear effects.

This is a better calibration for the present question than an unexplained solver
timeout or a claim that a wavefunction is too large. It is not yet a selected
useful-advantage workload, and reproducing a now-public answer is not discovery.

## 2. The experimentally specified event

Green et al. study gas-phase cyclobutanone following a 200 nm pump. They identify
an initially excited n3s Rydberg state, depopulation on a roughly 0.29 ps scale,
and secondary fragmentation on a (1.2 +/- 0.2) ps scale. The product channels
include ketene/ethylene and propene/carbon monoxide [3]. These are interpreted
experimental signals, not noiseless direct observations of a complete molecular
wavefunction. Initial ensembles, the pulse and measurement model matter.

The useful question is which products are made, in what fractions and when,
under a stated excitation. The benchmark does not by itself establish an
industrial use case, nor does 200 nm excitation establish relevance to
near-surface solar photochemistry. No new experiment or data reanalysis was run.

## 3. The quantum route already has a concrete cost

Eklund et al. [4] already provide an end-to-end first-quantized chemical-dynamics
algorithm and include cyclobutanone. Table 4, printed page 36, reports:

- 5,869 total logical qubits (2,058 state, 3,811 ancillary);
- 60.1 x 10^12 Toffolis for one 30 fs propagation;
- 1,002 x 10^12 Toffolis in the yield-estimation column at additive error 0.095.

The last number is 1.002 x 10^15. The table and caption were checked visually
and against the parsed PDF. Counts are the authors' estimates,
not measurements or a new resource calculation. Their benchmark uses a
HOMO-to-LUMO excitation and a Gaussian vibrational input; this is not an already
validated preparation for the actual 200 nm experiment. They explicitly note
that longer durations may be required [4].

Therefore this is not yet a cost for predicting the final experimentally
relevant branching ratio from its actual preparation. Thirty femtoseconds is
not the later fragmentation window in [3]. A linear extrapolation of the table
would not establish the correct full resource cost: preparation, spatial
requirements, target accuracy, duration convergence and sampling all need review.
Nor is the large gate count a lower bound excluding a better quantum algorithm.

Do not conflate older propagation estimates with the latest methods. Pocrnic
et al. [5] report 8.7 x 10^9 Toffolis per femtosecond and 1,362 logical qubits
for NH3+BF3, versus roughly 10^11 Toffolis/fs in an earlier treatment [6]. Those
are different benchmark/model/algorithm choices from [4], not interchangeable
costs for cyclobutanone or a complete yield calculation.

## 4. The same physical question must be solved on both sides

A controlled algorithmic approximation to a specified initial state does not
establish that the state is the right experimental preparation. Likewise a
controlled simulation of a Hamiltonian does not, on its own, verify the physical
model or the measurement interpretation. This is a comparison rule, not an
allegation that [4]'s algorithmic analysis is invalid.

Two possible quantum tasks should remain distinct:

**Electronic input to a classical dynamics calculation.** Compute adequate
energies/couplings along the relevant configurations, then retain an effective
classical description. Its cost includes identifying configurations, consistent
state tracking and sufficient information for the subsequent dynamics. If a
few existing classical calculations settle the requested prediction, there is
no quantum discovery advantage.

**Joint electronic and nuclear evolution.** Predict branching without supplying
a precomputed collection of potential-energy surfaces. This avoids importing
those surfaces as an unpriced oracle, but it must evolve to the time and at the
accuracy needed for the outcome. The framework in [4] already pursues this route;
our use of it would not be a new mechanism by itself.

The first task can succeed while approximate nuclear dynamics are sufficient;
the second can matter when their omission changes the answer. The prediction
challenge alone does not separate them. Its authors recommend controlled
comparisons using the same electronic inputs and matched initial conditions [1].
This is particularly relevant: we must not credit a quantum propagator with
fixing an inadequate classical electronic model that we silently grant to the
quantum side in a better form.

## 5. Decision for phase 2

Stop enlarging the thermal-event record. Use cyclobutanone as an independently
specified acceptance test for proposed microscopic mechanisms, not as a promise
that a new quantum simulation project has already been justified. Keep CO2 and
the parallel spectral-record line intact; no historical result is invalidated.

The immediate scientific question is whether predicting the useful branching
requires difficult joint dynamics after adequate electronic input and
preparation are fixed, or whether a substantially cheaper classical route
already determines it. Compare the same observable over a justified time window,
not a quantum full-state calculation against a weaker or differently prepared
classical task. This inquiry can be source-led before new solvers are built.

A potential simple goal remains: obtain a reliable product law without having
to supply the reaction pathways in advance. The task must have useful predictions
that are not already given in the input or fit from the held-out answers. A
short output and later reuse are not sufficient evidence of quantum advantage.
No candidate central quantum innovation is established by this note. The
manuscript stays on hold; no publication, outside contact or paid work follows.

## Work performed and source scope

Read the primary challenge review, individual prediction and experimental
reports, and current quantum-dynamics papers. Visually inspected Table 4 of [4]
using a PDF screenshot. No chemistry package, original source code, quantum
sampler, or hardware was executed. No earlier experimental verifier was rerun.
This additive note changes no code, data, license or other research branch.

[1] J. Janos et al., Perspective on a challenge: predicting the photochemistry
of cyclobutanone (2026). Full HTML v2, especially Sections 2.1-2.4 and 4.
https://arxiv.org/html/2604.12749v2 ; DOI 10.1063/5.0338792.

[2] S. Mukherjee et al., Prediction Challenge: Simulating Rydberg Photoexcited
Cyclobutanone with Surface Hopping Dynamics based on Different Electronic
Structure Methods (2024). Primary abstract inspected; not native code execution.
https://arxiv.org/abs/2402.09890 .

[3] A. E. Green et al., Imaging the Photochemistry of Cyclobutanone using
Ultrafast Electron Diffraction: Experimental Results (2025). Full HTML inspected;
no plot digitization, raw-data analysis or inferred precise final yields.
https://arxiv.org/html/2502.13956v1 ; DOI 10.1063/5.0266559.

[4] E. C. Eklund et al., End-to-End Simulation of Chemical Dynamics on a Quantum
Computer, arXiv:2603.19007v1 (19 March 2026). PDF Sections VI-VIII, Table 4 and
initial-state discussion inspected. Resource estimates not independently rerun.
https://arxiv.org/abs/2603.19007 ; https://arxiv.org/pdf/2603.19007 .

[5] M. Pocrnic et al., Efficient Simulation of Pre-Born-Oppenheimer Dynamics on
a Quantum Computer, arXiv:2602.11272v1 (11 February 2026). Abstract and resource
sections inspected; propagation estimates, not a matched end-to-end comparison.
https://arxiv.org/abs/2602.11272 .

[6] F. H. da Jornada et al., A comprehensive framework to simulate real-time
chemical dynamics on a fault-tolerant quantum computer, arXiv:2504.06348v1 (2025).
Abstract and resource/conclusion sections inspected. Historical cost anchor only.
https://arxiv.org/abs/2504.06348 .
