# Task-matched readout 02: measure the statistic, not an unnecessary joint record

29 September 2026. Baseline: `cdc3f30129e2428759aa97213ee4ab296528cd0b`.
Branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision:** the calibrated signal-template subtask has an explicit unentangled
Gaussian measurement that obtains its nuisance-insensitive amplitude estimate
without reconstructing both quadratures. With matched sensing-photon or total
squeezed-photon budgets it is less noisy than the symmetric two-mode-squeezed
Bell-readout construction considered in Screen 01, including unequal pure loss.
This is a task-specific comparison, not a no-go theorem for entangled sensing,
an all-measurement optimum, or a refutation of the cited experiments. The
unentangled competitor itself uses squeezing: it is NOT classical light.

The uncalibrated, nonstationary problem does not inherit this conclusion. But no
new resource-matched acquisition benefit or circuit-computing role is established
there by this checkpoint. Retain sensing as a separately scoped reserve rather
than build another generic metrology program. The next parent investigation returns
to graph sparsification, the original-input candidate from Screen 01. This switch
is a research-priority choice, not a claim that all sensing tasks are resolved.
No new repository, manuscript, laboratory request, or implementation campaign.

## 1. Use the real disturbance model and state the simpler subtask honestly

The 2016 quantum-dense-metrology experiment [1] models backscatter components as

$$
x_j=\theta g_j+A\sin\phi(t_j),\qquad p_j=A\cos\phi(t_j).
$$

Here we have denoted the desired known waveform template by g and its unknown
amplitude by theta; the paper fits an injected chirp and a deterministic scatter
model. Its actual phase phi(t) is fitted from data, not granted known. The
sinusoid/harmonic phase model, detector imbalance and constant relative phase are
explicit parts of that experiment. An earlier unentangled dual-readout experiment
also models and subtracts backscatter [2]. Joint acquisition is therefore a real
scientific technique, not evidence by itself of a new computational contribution.

**Subtask chosen for exact analysis:** g and a finite set of nuisance SHAPES are
calibrated before this record; their amplitudes are unknown. In the simplest
case phi(t_j) is known and only A is unknown. More generally, stack 2m coordinates
in x=theta h+B beta, where h and B are known real arrays, theta is the one parameter
of interest and beta contains arbitrary fixed nuisance amplitudes. Each pair of
coordinates belongs to one independently prepared temporal sensing mode. Independent,
parameter-independent Gaussian readout noise is the explicit model assumption.

This is an exact affine displacement model. A smooth unknown-phase model can be
linearized into it at a calibrated operating point, but then the result is LOCAL:
calibration, pilot observations and nonlinear remainder cannot be silently omitted.
The full unknown chirp, arbitrary drifting scatter, model selection, or many post-hoc
queries are not solved. The 2016 experiment's unknown nuisance phase is a material
limitation when connecting this subtask back to the whole experiment.

Both strategies receive the same h,B, one interaction with each signal-bearing
mode, and the same requested mean-square error for theta. They do not receive a
classical sampler for an unknown field distribution. This remains the scope-
separated physical-source model of Screen 01, not an answer to the original
classical-input circuit-algorithm problem.

## 2. A single target statistic is enough in the affine model

Assume B has independent columns; use its column space if it has redundancies.
Let

$$
r=(I-P_B)h,\quad P_B=B(B^TB)^{-1}B^T,\quad S=r^Tr>0.
$$

If S=0, theta cannot be identified separately from unrestricted beta by these
mean data. No quantum procedure is assumed to repair identical input signals.
For a two-quadrature record Y=theta h+B beta+epsilon with covariance nu_B I,

$$
\widehat\theta_B=\frac{r^TY}{S},\qquad
\mathbb E\widehat\theta_B=\theta,\qquad
\operatorname{Var}(\widehat\theta_B)=\frac{\nu_B}{S}.
$$

This is the usual nuisance-projected Gaussian estimator. It attains the classical
Gaussian Cramer-Rao/least-squares variance for unbiased theta estimation with
unknown fixed beta; nuisance-parameter estimation is established prior theory [3].
It is not a claim about every Bayesian prior, biased estimator, multiple targets,
or distribution-learning problem.

Partition r into two-coordinate pieces r_j. Before acquisition choose one homodyne
quadrature per sensing mode with unit direction u_j=r_j/||r_j||; zero pieces can
use any direction and are given zero weight. If y_j is that scalar measurement,
form

$$
\boxed{\widehat\theta_H=\frac1S\sum_j\|r_j\|y_j.}
$$

Since sum_j r_j^T B_j=0 and sum_j r_j^T h_j=S, this has exactly the same mean theta
for every beta. With independent equal readout variance nu_H per selected direction,

$$
\boxed{\operatorname{Var}(\widehat\theta_H)=\nu_H/S.}
$$

Equivalently, the matrix U containing the unit readout rows obeys U^T w=r and
w^Tw=S, where w_j=||r_j||. No simultaneous estimation of the unwanted amplitudes
is needed. This implements the desired linear statistic AT measurement rather
than learning the whole joint record and compressing it afterward. A one-mode
example is measuring p-bx directly instead of measuring both p and x to cancel a
known nuisance direction. This is standard projection/matched-estimation algebra,
not a newly discovered general sensing primitive.

For equal noise nu_H=nu_B, the two displayed scalar estimators have the same exact
Gaussian distribution. For nu_H<nu_B, adding independent Gaussian noise to the
homodyne estimate can reproduce the Bell estimator's scalar law pointwise in
(theta,beta). This does not simulate the full joint record or its ability to answer
new questions. It is a statement about THIS supplied task, not informational
completeness or a global quantum lower bound.

## 3. Match energy, signal response and loss before comparing noise

Use [x,p]=i, vacuum variance 1/2. Let E be the mean squeezed-vacuum photons available
per temporal source use, summed over signal and retained reference. This is not the
entire laser/local-oscillator power. Both schemes have a calibrated common phase
reference, the same displacement coupling and signal transmission eta_s>0. Treat
pure loss AFTER the unknown displacement. Reference transmission eta_r lies in
[0,1]; it need not equal eta_s. Rescale readouts to unit input-displacement gain.
No thermal environment, back-action or uncalibrated excess noise is included.

The symmetric two-mode-squeezed state has E/2 photons in each mode. Write

$$
C=E+1,\quad R=\sqrt{E(E+2)},\quad g(e)=(\sqrt{e+1}-\sqrt e)^2.
$$

Its local quadrature variance is C/2 and opposite/same-sign cross covariance is
R/2. Balanced Bell outputs x_s'-x_r' and p_s'+p_r', divided by sqrt(eta_s), have
independent equal input-referred noise

$$
\nu_B=\frac{C(\eta_s+\eta_r)+2-\eta_s-\eta_r
-2\sqrt{\eta_s\eta_r}R}{2\eta_s}.
$$

This follows directly by applying two independent vacuum loss channels to the
4-by-4 covariance matrix. Unequal-loss Bell noise, including antisqueezing leakage,
is already studied in [1]. Our normalization is vacuum 1/2 rather than its vacuum
1 convention; compare input-referred sensitivity, not unrescaled detector noise.
This formula concerns this specified symmetric resource and Bell readout, not all
possible entangled Gaussian probes or all joint measurement designs [4].

For squeezed homodyne aligned to u_j, allocating e photons to the sensing mode gives

$$
\nu_H(e)=\frac{1-\eta_s}{2\eta_s}+\frac{g(e)}2.
$$

Two fair comparisons are possible. Set e=E to use the same TOTAL available photon
budget entirely in the sensing mode. Or set e=E/2 to use the same SENSING-mode
photon count as Bell, consuming less total squeezed energy and no stored reference.
The second option avoids attributing a gain merely to extra probe illumination.

Both give the same result ordering. With t=sqrt(eta_r/eta_s) and C^2-R^2=1,

$$
\nu_B=\frac{1-\eta_s}{2\eta_s}+\frac1{2C}
+\frac C2\left(t-\frac RC\right)^2+\frac{1-\eta_r}{2\eta_s}.
$$

Since g(E/2)=1/(C+R)<=1/C and g is decreasing,

$$
\boxed{\nu_H(E)\leq\nu_H(E/2)\leq
\frac{1-\eta_s}{2\eta_s}+\frac1{2C}\leq\nu_B.}
$$

Thus a known scalar target does not require the Bell scheme's second output in
this model, and concentrating sensitivity along the needed direction is adequate.
This is not a claim that squeezing is unnecessary or that classical coherent
light attains the result. It is an explicit UNENTANGLED quantum-optical comparator.
For example, E=2 and no loss give nu_B=0.171573 and nu_H(E)=0.050510. With eta_s=0.8
and eta_r=1, they are 0.337722 and 0.175510. These are analytic sensitivity values,
not experimental performance data. Both theta variances divide by the same S.

The signal/reference loss difference is included, but this is not a full resource
estimate for an interferometer. Optical routing, preparation and reference energy,
phase-locking bandwidth, extra detectors, source lifetime, and calibration time
must still be considered before comparing working instruments.

## 4. Do not hide the cost of knowing or rotating the useful direction

All directions u_j must be selected BEFORE their signal modes are measured. In the
exact affine task they follow from supplied h,B, not from an answer oracle. Building
r is ordinary least squares with input and numerical costs, and there is one
homodyne reading per source use, not a free second pass through an unknown event.

If B is instead learned from the same unknown event, this recipe does not supply
its own pilot data. A joint record can be used retrospectively for nuisance learning;
the compressed record need not allow that. Its possible benefit is calibration or
adaptation, not a demonstrated intrinsic advantage for the calibrated scalar task.
A two-stage strategy may work for repeated/stationary sources, but its sample cost
and stability have NOT been bounded here. No arbitrary repeatability is assumed.

If the true mean has an unmodeled component delta m, the estimator bias is

$$
\frac{r^T\delta m}{S},\qquad
|\operatorname{bias}|\leq\|\delta m\|/\sqrt S.
$$

For a scattered amplitude A and phase errors delta phi_j, a useful bound is
||delta m||<=|A| sqrt(sum_j delta phi_j^2). The norm is over both quadratures.
Large contamination therefore makes even small phase-calibration errors important.
This is exactly why granting the experiment's fitted phase as a perfect input
would overstate the result. A small S also magnifies both model and quantum noise.

The squeezing axis must follow the readout direction. Rotating only the local
oscillator while leaving a strongly squeezed probe misaligned changes its noise to
[g(e) cos^2 delta+g(e)^(-1) sin^2 delta]/2 before the loss term. Angle control is
not free. In a continuous detector, frequency-dependent squeezing, temporal noise
correlations and radiation-pressure back-action can change the measurement model.
They cannot be inferred from independent loss-only temporal modes.

The 2025 quadrature-witness proposal [5] explicitly studies backscatter mitigation
compatible with frequency-dependent squeezing and back-action. This and [1,2]
are substantial predecessors for the genuinely unknown-noise problem, not proof
that it has no remaining open questions. No practical advantage is inferred from
our ideal angle-selection algebra or an arbitrarily restricted alternative.

## 5. Decision and next task

The calibrated-template task does NOT justify developing the phase-4 Bell-sensing
lead into a new parent result. For the broader random-field/post-hoc task, the
2026 signal-learning paper [6] makes important measurement restrictions explicit.
In particular, fixed-angle marginal blindness cannot be silently transferred to
optimized task-aligned measurements. Neither this small affine subtask nor the
covariance identity refutes that paper's carefully scoped comparisons.

We have not solved nonlinear nuisance inference or arbitrary distribution learning,
and do not close quantum sensing in general. We also have not identified a useful
new matched regime beyond the cited metrology, or a general-purpose circuit role.
The parent input-model exception remains unapproved as a replacement objective.
**Park this sensing audit as a reference and next investigate the in-scope graph
sparsification candidate from Screen 01.** No further generic sensing certificates,
finer artificial features, or extra waveform-fitting framework is requested.

The next graph step must combine: one useful implicitly specified graph family;
its explicit coefficients and coherent-query implementation; the known quantum
sparsifier and working-memory costs; the strongest geometric/kernel classical
construction; and a task/output that actually uses the sparsifier. Do not price
an implicit classical graph as an explicitly loaded n^2-edge array, and do not
claim novelty for the existing Apers-de Wolf algorithm. Select a bounded input-
access comparison before code or a new theorem. This is the shortlisted original-
input alternative, not reopening the closed emitter case. No new repository needed.

## 6. Evidence and source scope

The independent checker ran twice with identical JSON and rejected -O/-OO and
six invalid inputs. It checks one rational four-mode/two-nuisance regression,
an exact symbolic square decomposition, six analytic energy/loss cases against
an independent covariance-matrix calculation, and a phase-drift negative control.
No Monte Carlo, optical experiment, waveform fit, adaptive pilot, device compilation,
timing benchmark, or historical scientific verifier was run. Symbolic equalities
and written inequalities support the statements; finite noise values are not
interval-certified physical parameters or claims of all-strategy optimality.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/task_matched_readout_v1/verify.py
```

Requires Python 3.10+, SymPy and NumPy. No input files, network or output writes.
Checker SHA256: `299e8d1fa371f6a9e98930cce48fa58bc59844402a560ab794b7f4ebaea8e1c0`.
Report SHA256: `283619c5e2f2e833a447707d1ffa26d2e4852b8066e972b45eb29ab5043f890d`.

Primary sources inspected 29 September 2026; not an exhaustive priority audit:

[1] Ast, Steinlechner and Schnabel, Reduction of Classical Measurement Noise via
Quantum-Dense Metrology, PRL 117,180801 (2016), arXiv:1607.00130. PDF methods,
Eqs. 1-5 and stated limits inspected. Screenshots of the relevant pages failed;
no plotted performance values are extracted or used as our resource comparison.
https://arxiv.org/abs/1607.00130

[2] Meinders and Schnabel, Sensitivity improvement of a laser interferometer limited
by inelastic back-scattering, employing dual readout, CQG 32,195004 (2015).
Primary abstract: unentangled dual readout already subtracts modeled scatter.
https://arxiv.org/abs/1501.05219

[3] Suzuki, Yang and Hayashi, Quantum state estimation with nuisance parameters,
J. Phys. A 53,453001 (2020), arXiv:1911.02790v3. Primary abstract/method scope only;
the finite affine derivation above is self-contained, not a claimed new theory.
https://arxiv.org/abs/1911.02790

[4] Bradshaw, Lam and Assad, Ultimate precision of joint quadrature parameter
estimation with a Gaussian probe, PRA 97,012106 (2018). Primary abstract on tight
Gaussian joint-estimation bounds. Its optimization theorem is not assumed to
cover our full waveform/control problem or used as an all-resource lower bound.
https://doi.org/10.1103/PhysRevA.97.012106

[5] Boettner, Schnabel and Korobko, Quadrature-witness readout for backscatter
mitigation in gravitational-wave detectors limited by back-action,
arXiv:2511.03842v1 (2025). Primary abstract only; no full detector simulation or
new experimental claim reproduced. This is a proposal, not a deployment claim.
https://arxiv.org/abs/2511.03842

[6] Cotler, Danielson and Kannan, Quantum Advantage for Sensing Properties of
Classical Fields, arXiv:2602.17591 (2026). Primary HTML Sections III-IV and B.2:
finite-angle restrictions, squeezed-homodyne readout, energy and post-hoc scope.
No all-measurement impossibility is inferred from fixed-axis examples.
https://arxiv.org/html/2602.17591

Only Quantum-Assisted-Algorithm-Discovery is modified. Prior notes, code, reports,
licenses and handover remain intact; both classical spin-offs stay independent.
No external contact, paid/unattended work, merge, release or manuscript follows.
