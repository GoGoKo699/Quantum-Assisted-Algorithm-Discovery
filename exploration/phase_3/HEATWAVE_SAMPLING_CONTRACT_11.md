# Direct sampling 11: extreme-summer scenarios, with the preparation cost exposed

28 September 2026. Starting head: `215c256127998b4aedb56a678b2af5a0a710370a`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision:** retain direct sampling and select one task-level comparison: scenario
histories and circulation diagnostics conditional on extreme summer temperature
in an established climate-model experiment. This is a model-based climate-risk
and mechanism task, not a forecast conditional on today's observations. An
explicit quantum reference construction and a cost screen are given below.
No climate run, operational forecast, speedup or novel quantum primitive is claimed.

## 1. A consumer that already uses the samples

Ragone and Bouchet [1] use CESM1.2.2 to study extreme summers over France and
Scandinavia. Their output includes time histories and circulation composites,
not just a scalar event frequency. The archived setup [2] is F2000 with CAM4,
seasonally varying prescribed ocean boundary conditions and year-2000 forcing.
The experiment applies classical trajectory selection every five days during
90-day summer runs. Its public scalar files contain 100-by-720 arrays per batch;
the composite products include surface temperature and 500-hPa geopotential.
This establishes a directly useful consumer independently of quantum computing.

For a first matched contract choose the France experiment. Fix its domain mask,
model configuration, initial-state law, perturbation protocol, numerical semantics
and reference climatology. Write Z=C(R) for a complete discretized trajectory
produced by a classical simulator from random input R with law w. Let A(Z) be
the 90-day regional mean surface-temperature anomaly and let a be a threshold
fixed from the control climatology, such as its 99th percentile. The target is

$$
P_a(dz)=P(dz\mid A(z)\geq a).
$$

Return coherent scenario histories and the requested temperature/circulation
fields, or statistically justified weighted equivalents for the same diagnostics.
Here coherent means time-consistent, not that the delivered data stay quantum.
A finite control percentile is not an exact or observed 100-year return period.
Estimating the unconditional event probability is a separate task. No universal
numerical error tolerance is borrowed from a quantum benchmark.

This fixes the algorithmic input/output contract, not a runnable CESM circuit.
Model binaries, full initial-state construction and numerical settings have not
been imported or compiled. A finite initial-condition list cannot be silently
promoted to the full climatological distribution. Any fresh perturbations must
have the same declared interpretation on both sides; cloning perturbations are
not automatically physical model noise.

The baseline is the published genealogical importance sampler, with its actual
weights, finite-population effects and dependence between descendants. Do not
require it to discard useful weighted trajectories just to make quantum output
look better. A 2025 IPSL-CM6A-LR study [3] uses related sampling and reaches a
different mechanistic interpretation of hot summers: the selected CESM model is
not a certificate of universally correct atmospheric physics. For transient
extremes, TEAMS [4] is another relevant algorithm, not a timing result transferable
to seasonal CESM composites. Modern learned forecasts likewise need task-matched
validation rather than automatic inclusion or dismissal.

## 2. An explicit quantum sampler without probability-grid reconstruction

Use a finite random input R: initial-state selection, numerical innovations and
any other declared random choices. A reversible implementation U computes the
event bit from R while retaining enough workspace to invert the computation:

$$
U|0\rangle=\sum_r\sqrt{w(r)}|r\rangle|g_r\rangle
  |\mathbf 1\{A(C(r))\geq a\}\rangle.
$$

The garbage register g_r is permitted and must be uncomputed by U inverse during
amplification. It is not discarded for free. Distinct random inputs remain
orthogonal even when they produce the same physical trajectory. Conditioning on
the event and measuring R therefore gives exactly w(r) conditioned on the event.
Classical replay of C(r) then gives P_a, including the correct multiplicities of
many-to-one maps. No probability-amplitude tomography is needed.

Standard amplitude amplification [5] supplies the conditioning procedure. The
full physical model need not be measured as a gigantic register: measure the
random input and replay the validated classical simulator once for each accepted
sample. This is direct scenario sampling plus postprocessing, not learning a
classical program. The classical replay time and all requested output bytes count.
Replay must be reproducible with pinned arithmetic/parallel execution semantics;
a seed is not enough if those semantics vary.

The quantum machine STILL computes the event coherently many times. Turning
classical arithmetic into reversible gates, controlling numerical error, preparing
w, retaining history or using reversible checkpoints, and implementing U inverse
remain potentially dominant costs. No CESM implementation of U has been built.
Unconditioned reversible simulation followed by measurement merely reproduces the
ordinary classical sampling law and gives no sampling-query improvement by itself.
Koopman-von Neumann propagation [6] remains an alternative, not a free replacement
for U or a reason to compare with an explicit exponentially large density grid.

## 3. A finite cost screen, not an asymptotic slogan

Let p=P(A>=a), theta=asin(sqrt(p)), and use the illustrative known-p schedule
j=floor(pi/(4 theta)). This is a first-peak schedule, not a proof of optimality.
One attempt succeeds with s=sin^2((2j+1)theta), using 2j+1 calls to U or U inverse.
Repeated fresh attempts require an expected n_U=(2j+1)/s such calls per success.
This assumes p known; learning it or using an unknown-p schedule adds obligations.

Let C0 be the cost of one ordinary trajectory, rho=C_U/C0 in a common stated
resource metric, and charge one C0 for classical replay. Even before separate
marking/reflection, validation, setup and output costs, this particular recipe costs

$$
C_Q/C_0=\rho n_U+1.
$$

At rho=1, with the omitted costs set to zero, the sensitivity calculation gives:

| Assumed event mass p | Ordinary rejection trajectories/sample | U or inverse calls/sample | Quantum recipe plus replay in C0 units |
|---|---:|---:|---:|
| 0.01 | 100 | 15.0702 | 16.0702 |
| 0.001 | 1000 | 49.0217 | 50.0217 |
| 0.0001 | 10000 | 157.0001 | 158.0001 |

These are hypothetical arithmetic cases, NOT measured climate frequencies or
quantum times. rho=1 is a favorable comparison scenario, not hardware evidence.
If a classical targeted method improves on rejection by a quality-matched factor
G, this recipe can win only if

$$
\rho < \frac{1/(pG)-1}{n_U},
$$

when the right side is positive, before the omitted costs. For G=10 and p=0.001,
this threshold is about 2.0195; for G=100 it is about 0.1836. Neither G is claimed
measured here. Published gains in raw extreme counts or in estimating a different
return period cannot be inserted as G for independent conditional scenarios or
for a different composite-error requirement. Compare cost to the same uncertainty
in requested diagnostics, including genealogy and importance weights.

Thus the square-root improvement over rejection alone is not an application
advantage. This screen does not rule out better schedules, genuinely faster
propagators, guided preparations, or quantum processing of shorter continuations.
It does not justify building a full reversible climate model yet.

## 4. Test of a seemingly stronger shortcut: tilt, then unbias

The classical rare-event method targets an exponentially tilted trajectory law
[1]. In ideal-law notation write q_beta(z)=exp(beta A(z)) P(z)/Z_beta, beta>=0.
A hypothetical quantum preparer of this law cannot simply condition on A>=a:
that returns an over-tilted tail, not P_a. One correct rejection flag is

$$
r(z)=\mathbf 1\{A(z)\geq a\}\exp[-\beta(A(z)-a)].
$$

It lies in [0,1], requires neither Z_beta nor p to evaluate, and satisfies

$$
q_\beta(z)r(z)=\frac{e^{\beta a}}{Z_\beta}P(z)\mathbf 1_E,
\qquad \alpha=\mathbb E_{q_\beta}r=\frac{e^{\beta a}p}{Z_\beta}.
$$

Quantum rejection/amplification [5,7] could obtain unweighted conditional samples
in O(1/sqrt(alpha)) preparation calls. Classical consumers allowed weighted
samples can instead use the weights directly. Independence and population errors
of an implemented q_beta are separate from this exact change-of-measure identity.

A cheap q_beta is NOT obtained merely by globally filtering P twice. Suppose the
first preparer makes q_beta from P by the flag exp(beta(A-Amax)), with a supplied
upper bound Amax. Its acceptance is alpha1=Z_beta exp(-beta Amax). The product is

$$
\alpha_1\alpha=p\exp[-\beta(A_{\max}-a)]\leq p.
$$

Accordingly, straightforward nested amplitude amplification with multiplicative
preparation costs has scaling 1/sqrt(alpha1 alpha), no better than direct 1/sqrt(p)
conditioning and potentially worse. Fusing the filters recovers a direct scaled
event filter, not an additional speedup. This is an accounting result for this
global-rejection implementation, not a lower bound for other ways to prepare a
guided law. Classical sequential selection has structure not represented by a
single global filter; any quantum improvement must retain and price that structure.

The missing quantity worth investigating is the cost of a genuinely guided
preparation, not a larger tail bias parameter. We do not claim these elementary
identities or quantum rejection sampling as new primitives.

## 5. Rare outcomes and rare harmful events are not identical

Guo et al.'s June 2026 preprint [8] filters outcomes whose individual probabilities
fall below a supplied threshold without first identifying the rare outcomes,
using coherent sampler access. Our event is an explicit physical threshold A>=a,
irrespective of how likely each detailed trajectory label is. Appending unused
independent bits makes each outcome label less probable without changing heatwave
frequency. Filtering individual seed probabilities would therefore not solve our
task. The new paper is relevant prior work, but its query result is not a
demonstrated climate algorithm or a reason to ignore source-aware classical
samplers. Only its stated task and access model were screened here, not its
complete proof or experimental corpus.

Accuracy also matters after conditioning. If approximate and target base laws
have total-variation distance eta and the same event has target probability p>0,
with nonzero probability under both laws, then their conditioned laws differ by
at most eta/p (or 1, whichever is smaller). To see this, normalize both restricted
measures by the larger event mass and bound the remaining normalization term;
the within-event and outside-event variations together are at most 2 eta.
A finite control attains raw TV=10^-5 and conditional TV=0.01 for p=0.001.
This is a worst-case mathematical sensitivity, not a physical-model error budget
or a required gate fidelity. A smaller observable-specific bound may suffice.
Quantum implementation error and physical model uncertainty must not be conflated.

## 6. The next bounded decision

Keep direct sampling; do not restart the classical-program requirement. Investigate
whether a quantum routine can accelerate SHORT stochastic continuations inside a
classical rare-event method, rather than coherently regenerate a whole season for
every trial. Use the existing climate task as the consumer; a small dynamical test
alone is not evidence of useful climate performance.

The first derivation must preserve the path law. If h is a prefix and q(h)=P(E|h),
choosing h from its ordinary law and sampling a successful future at each h does
not produce P(h,future|E): successful prefixes should be weighted by q(h). Any
estimation, normalization, resampling or acceptance needed to retain those weights
counts. At a fixed observed prefix the conditional task is different and must be
stated explicitly. Do not square-root a classical particle count or assume a
finite cloning population is a free coherent conditional-state oracle.

The deliverable is a law-preserving segment-level cost comparison, or a clear
reason that it gives no gain. No CESM port, broad climate campaign, new neural
architecture, large toy census or separate spin-off is warranted by this screen.

## 7. Execution and sources

`python experiments/direct_tail_sampling_v1/verify.py` ran twice with identical
JSON. It checks 12 exact rational tilt/correction/cost identities, an intentionally
wrong uncorrected tilt, the conditioning sensitivity, unused-label refinement and
the known-p cost table. Five invalid probabilities are rejected; -O/-OO refusals
were checked. It writes no files. These are artificial finite-law controls and
arithmetic sensitivities, not simulated or observed weather. Historical verifiers
were not rerun; their code and reports are unchanged.

Checker SHA256: `b17ad0f98d23483e158f3123bee7f70eca9ac9f68f04ad8645f18e4b5e8b96af`.
Report SHA256: `e949f85e6b1320bc7df1515506a186b73cc92a0b0184058c00c41d70f3b3af9a`.

The public climate data inventory and primary methods were read. Download attempts
for the two scalar archives and resampling script failed on runtime DNS; no archive
was acquired, checksum verified, or data-derived performance result computed.
No upload is requested for this analytical checkpoint. The 2020 preprint's PDF
text was inspected for the tilted-law equation; both screenshot attempts failed.
No figures were digitized or performance inferred from inaccessible images.
Publisher HTML provides the 2021 results; the preprint is not substituted for
changed final-paper figure interpretations. No raw data or upstream code is
redistributed. No quantum circuit or atmospheric model was run.

Sources checked 28 September 2026; focused comparison, not an exhaustive novelty audit:

[1] Ragone and Bouchet, GRL 48, e2020GL091197 (2021), Methods 2.1-2.2 and Results
3.2. https://doi.org/10.1029/2020GL091197 ; preprint Eq. (2):
https://arxiv.org/pdf/2009.02519

[2] Authors' dataset and configuration description, Zenodo 4763283, v1 (2021).
https://zenodo.org/records/4763283

[3] Noyelle et al., GRL, e2025GL115552 (2025). Primary HTML methods and conclusions
inspected; no model or data reproduction. https://doi.org/10.1029/2025GL115552

[4] Finkel and O'Gorman, JAMES 18, e2025MS005456 (2026). Abstract, scope and data
statement inspected; reported probability-estimation gains not used as G above.
https://doi.org/10.1029/2025MS005456

[5] Brassard et al., Quantum Amplitude Amplification and Estimation, standard
primitive. https://arxiv.org/abs/quant-ph/0005055

[6] Joseph, PRR 2, 043102 (2020). Abstract's density-grid versus Monte Carlo
comparison inspected, not a new full algorithm audit. https://arxiv.org/abs/2003.09980

[7] Ozols, Roetteler and Roland, Quantum rejection sampling, TOCT 5 (2013).
Primary abstract and author-institution record inspected. https://arxiv.org/abs/1103.2774

[8] Guo et al., Quantum enhanced rare event discovery and sampling,
arXiv:2606.06316v1 (4 June 2026), Sections I-II and access definitions.
https://arxiv.org/html/2606.06316v1

Only Quantum-Assisted-Algorithm-Discovery is modified. Manthan stays paused;
battery/operator candidates and spin-offs remain separate. No manuscript,
external contact, paid/unattended work, branch merge or administration change.
