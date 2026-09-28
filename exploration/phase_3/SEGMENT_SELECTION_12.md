# Segment selection 12: preserve the history weights, then price the gain

28 September 2026. Base: `5272b5f70e87fbbd99c731989d1a4a53deb8d342`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Outcome:** a law-correct short-segment construction is specified, including an
independent-pilot correction for unnormalized full-path expectations at finite
population size. Its ingredients are established sampling methods, not a new
primitive or priority claim. A useful climate advantage is NOT established.
The unresolved test is now local continuation cost, checkpoint access and total
weighted-estimator variance, rather than another correctness-free square root.

The consumer remains Note 11's CESM France extreme-summer histories and circulation
composites [1,2]. Weighted scenarios are allowed. This is model-conditioned climate
analysis, not today's forecast. No atmospheric or quantum circuit was run.

## 1. Select the parent and continuation together

At a checkpoint, let the stored prefix histories be h_i with normalized classical
weights w_i. A declared short continuation kernel K_i generates a segment y from
that prefix, including exactly the prescribed perturbation/numerical semantics.
Let g_i(y) be a computable selection score in [0,1]. Define

$$
a_i=\mathbb E_{K_i}g_i,\qquad
\alpha=\sum_i w_i a_i>0.
$$

The required weighted continuation law is

$$
Q(i,dy)=\frac{w_iK_i(dy)g_i(y)}{\alpha}.
$$

Its parent marginal is w_i a_i/alpha. Choosing i from w_i first and then generating
an accepted continuation independently at each i instead produces w_i K_i g_i/a_i.
That is generally different. For two equally likely parents with success masses
1/4 and 3/4, the correct successful parent proportions are 1/4 and 3/4, not 1/2
and 1/2. The finite control has total-variation discrepancy 1/4.

The repair is to prepare the joint prior over parent index and continuation seed,
compute the segment and its score coherently, flag acceptance with probability
g_i(y), and amplify the joint accepted subspace. Measure the parent index and
seed, then classically replay just that segment. Conditional on success the
measurement law is Q, with all seed-to-path multiplicities preserved.

No individual a_i estimate is required for this sampling step. Unknown aggregate
alpha can be handled by standard randomized amplification schedules [5]; it is
not a freely known parameter. Alpha=0 needs separate handling, and a timeout is
not a proof that no acceptable continuation exists. Each returned child requires
a fresh preparation; the quantum state is not a reusable sample bank.

This is the joint selection/mutation law underlying fully adapted particle
methods [3]. Rejection-based particle methods and their normalizing-constant
issues are prior work [4]. Quantum rejection/amplification is also prior work
[5,6]. Replacing classical rejection by quantum conditioning does not itself
establish a new particle-filter architecture or application advantage.

### A finite implementation of the score flag

For g_i(y)=m_i(y)/2^b, add an independent uniform b-bit register u and mark
u<m_i(y). This realizes the specified flag without an ideal arbitrary-angle
rotation for each score. Reversible score computation, comparison and all their
inverses still count. Parent-weight and seed preparation also count.

A non-dyadic guide can be replaced by an explicitly specified dyadic guide, with
that actual guide used in all subsequent weights. For full-path recovery below,
keep guides strictly positive on every path of interest: silently rounding a
small positive guide to zero can discard valid extreme scenarios. A positive
floor is allowed as a change to the proposal, not to the physical dynamics.
There is no finite-precision CESM circuit or hardware error bound here.

## 2. A short guide is not a full-season event oracle

Before the end of summer, g_t can depend on a five-day temperature increment or
another declared short-segment score. It must not be called P(final heatwave|h)
unless that probability has actually been computed. Testing the full seasonal
event normally requires the remaining season; this construction does not make
that computation local.

For fixed, nonadaptive positive guides g_1,...,g_T and the declared path law P,
define W_t(h)=product_{s<=t} g_s(h). At the exact-distribution level, successive
joint selection steps satisfy

$$
\eta_t(dh)=\frac{P(dh)W_t(h)}{Z_t},\qquad
Z_t=\mathbb E_P W_t.
$$

This follows by multiplying the previous prefix law by the next kernel and guide
and normalizing once, globally. Parent-dependent normalizers must not be dropped.
For the seasonal event E and an integrable scenario diagnostic f,

$$
\mathbb E_P[f\mid E]=
\frac{\mathbb E_{\eta_T}[f\mathbf1_E/W_T]}
     {\mathbb E_{\eta_T}[\mathbf1_E/W_T]}.
$$

The global normalizer cancels in this exact identity. With exponential increment
guides, W_T is proportional to the seasonal exponential tilt and this is the
correction in Note 11. Other positive guides may target the same P and E through
the corresponding inverse weights, but their statistical efficiency can differ.
No assertion is made that an arbitrary guide increases useful tail coverage.

Independent snapshots are not substituted for histories. A returned child retains
its parent pointer, accumulated selection weight and reproducible segment seed.
The coherent routine needs the current restart state and sufficient accumulated
statistics, not necessarily the entire earlier trajectory. The ancestry and
requested output fields still have storage and replay costs.

## 3. Finite populations need more than a correct local sampler

An exact draw from Q for a finite stored population is not an exact draw from
the true seasonal law. Prefixes missing from that population cannot reappear by
improving its continuation sampler. Different children are independent conditional
on the frozen pool in this construction, but share random ancestors unconditionally.
This is not the same finite-particle kernel as every bootstrap/residual resampler.

A control illustrates the distinction. Draw N parent labels independently with
probability 1/2 each, then select perfectly using the 1/4 and 3/4 success masses
above. For N=1 the expected high-success-parent fraction is 1/2; for N=2 it is
5/8, not the true 3/4. At N=4 it is 111/160. Local exactness does not remove the
random-denominator bias. These are artificial finite-law checks, not climate data.

### One explicit correction: independent pilot weights

There is a simple way to retain unbiased *unnormalized* path expectations without
pretending the finite cloud is exact. It is an importance-weight construction,
not a claim of independent unweighted samples or a new SMC theorem.

Initialize N independent histories from the prescribed P_0 and set Zhat_0=1.
At step t, conditional on the entire past population, let muhat_{t-1} be its
empirical law and define Q_t=muhat_{t-1} K_t g_t/alpha_t. Generate N children
independently from Q_t using the joint routine. Separately generate m_t ordinary
parent/continuation trials from muhat_{t-1} K_t and average their scores:

$$
\widehat\alpha_t=\frac1{m_t}\sum_{j=1}^{m_t}g_t(H_t^{\mathrm{pilot},j}),
\qquad \widehat Z_t=\widehat Z_{t-1}\widehat\alpha_t.
$$

These pilots must be independent of the accepted children conditional on the
past. Use the score itself, rather than unnecessarily adding Bernoulli flag noise.
No individual-parent normalizer is estimated. For any bounded path function phi,

$$
\mathbb E[\widehat Z_t\widehat\mu_t(\phi)\mid\mathcal F_{t-1}]
=\widehat Z_{t-1}\widehat\mu_{t-1}(K_t(g_t\phi)).
$$

The equality uses conditional independence and E[alphahat_t|past]=alpha_t.
Induction gives

$$
\mathbb E[\widehat Z_T\widehat\mu_T(\phi)]
=\mathbb E_P[W_T\phi].
$$

Consequently, the returned paths with nonnegative weights
Zhat_T/(N W_T(h_i)) reproduce unnormalized P-expectations in expectation, including
P(E) and E_P[f 1_E]. In a finite-state discretization with strictly positive guides,
these quantities are finite. This is an exact expectation statement in the ideal
sampling model, even for fixed N. Ratios of the two estimators are not unbiased
at finite sample size. Independent whole-population replicates permit consistent
ratio estimates when their means exist; useful error bars and cost depend on the
variance, not on the mere count of paths. The relevant unit of replication is
not an individual descendant treated as independent.

The two-stage N=1 control enumerates all 32 extended random histories and recovers
the correct mass of every one of its eight physical paths. Omitting the pilot
normalizers fails that control. No proof of small variance for the climate task
is supplied, and particle-adaptive guides need a separate derivation.

### This correction can be expensive

Conditionally on the current cloud,

$$
\frac{\operatorname{Var}(\widehat\alpha_t)}{\alpha_t^2}
=\frac{\operatorname{Var}_{\widehat\mu K}(g_t)}{m_t\alpha_t^2}.
$$

For an indicator score this is (1-alpha_t)/(m_t alpha_t). At alpha_t=0.01,
obtaining a conditional relative standard deviation of 0.1 by these ordinary
pilots requires 9900 trials. These are illustrative inputs, not a necessary
climate tolerance, a measured rejection rate, or a lower bound on all algorithms.
Soft guides can have much smaller score variance. Noisy unbiased weights can be
used without enforcing a fixed per-step precision, but their final uncertainty
must be evaluated. Better normalizer schemes are allowed and must be priced.

Amplified acceptance frequencies are not alpha_t. For example alpha=1/4 becomes
success one after one Grover round. Substituting that frequency into a classical
normalizer estimator is wrong. The negative-binomial stopping-count estimator of
an alive classical filter [4] cannot simply use quantum attempt counts instead.
Ordinary amplitude estimation is a separate possible estimator; an unqualified
plug-in value does not inherit the unbiasedness proof above.

## 4. The actual cost condition

For one stage returning N children, an explicit accounting is

$$
C_{Q,t}=B_t+N[n_U(\alpha_t)C_{U,t}+C_{\mathrm{replay},t}+C_{\mathrm{extra},t}]
       +m_t C_{\mathrm{pilot},t}.
$$

B_t is per-stage setup, including organizing the new checkpoint population.
C_U includes one complete coherent preparation or inverse: parent-weight/seed
preparation, controlled restart loading, propagation, score arithmetic and
workspace management. C_extra includes additional marking/reflection, readout
and validation not already charged; adaptivity and unknown-alpha scheduling also
count. n_U is an expected forward/inverse call count for the selected schedule.
The pilot term is for the explicit finite-population weight correction above;
a different estimator may have a different cost and bias contract.

Against the SAME-LAW classical joint-rejection routine, accepted children cost
N C_segment/alpha plus any corresponding setup/weight bookkeeping. In the ideal
coherent model n_U=O(1/sqrt(alpha)) [5]. This is not a comparison with the best
classical genealogy, importance sampler, learned proposal, cache or direct
observable estimator. The actual condition is total C_Q < C_best-classical at
the same scenario-diagnostic uncertainty, including all stages and population
replicates. Summing costs is not a claim that stage errors add harmlessly.

For orientation only, the known-alpha first-peak schedule from Note 11 gives:

| Local acceptance alpha | Coherent forward/inverse calls per child | At unit coherent/ordinary cost, plus one replay |
|---|---:|---:|
| 1/4 | 3 | 4 |
| 1/16 | 7.28166 | 8.28166 |
| 1/100 | 15.07016 | 16.07016 |

This table omits setup, checkpoint loading beyond the unit-cost assumption,
pilots, additional gate overhead, hardware and validation. It is a sensitivity,
not a resource estimate. The 1/4 case merely ties classical rejection before
those omitted costs. Seasonal event rarity is NOT the local acceptance rate.

### Two strong classical responses

If the children and scores have already been computed, classical resampling
uses that explicit weight list [7]. Amplitude-amplifying a list of known scores
does not save the preceding simulations. Our routine must instead select among
as-yet unevaluated continuations, before paying to produce all candidate fields.

If each of N stored prefixes has a deterministic continuation, the classical
competitor can compute and cache all N continuations once and then draw from their
known weighted law. Its propagation cost is O(N C_segment), not N C_segment/alpha
for N children. Do not replace this competitor by repeated rejection. With truly
variable continuations the comparison is different, but their prescribed law and
variation at the chosen segment length must actually be established.

A small alpha can also be manufactured by multiplying every guide by 1/100:
Q is unchanged while rejection becomes 100 times harder. Tight, justified score
envelopes matter. A maximum over a few observed children is not a global bound
on scores of unseen continuations. Do not create a quantum opportunity through
an unnecessarily loose normalization.

## 5. Checkpoint access and the application-specific next test

The parent indices must be in coherent superposition to realize joint selection.
The corresponding classical restart records do not enter quantum memory for free.
An elementary serial lookup into N records of b_state bits has linear database
work (for example O(N(b_state+log N)) controlled operations with equality tests).
Other circuits or hardware can improve tradeoffs, but their construction, memory
and repeated access must be charged. This is an upper-bound implementation sketch,
not a lower bound or a QRAM assumption. As segments shorten, loading can dominate.

The archived CESM procedure selects every five days, then perturbs clones [1,2].
The documented perturbation is small and the innovations are not a license to
inject arbitrary extra weather noise. Chaotic evolution does not guarantee that
five-day selection scores differ enough between continuations from the same
checkpoint to justify a quantum selection stage. Nor does the observed diversity
between unrelated parents establish that within-parent opportunity.

**Next bounded test:** examine the released five-day scores, ancestry and stated
restart/perturbation procedure for the France task. Separate already-computed
weight resampling from costly generation of fresh children. Determine what these
records can actually say about score variance among descendants of the same
checkpoint, correction-weight variance and the amount of state a coherent segment
would load. Preserve the classical base law and allow cached, stratified and
guided classical continuations. A terminal composite's error must be assessed
across independent populations, not raw clone count. No new climate campaign is
scheduled; do not replace inaccessible data by an arbitrary Lorenz test.

Proceed only if this narrow computation leaves a plausible total-cost margin.
No useful quantum advantage or publication novelty has yet been established.
The result here is that the path-weight obligation can be met explicitly, but it
is neither free nor sufficient for usefulness. No new repository is warranted.

## 6. Executed checks and sources

`python experiments/segment_selection_v1/verify.py` passed twice with identical
JSON; -O/-OO refusal was checked. The 1458 artificial prior/kernel/score choices
include 50 empty selection laws. The other 1408 give 5632 exact ideal-amplitude
round states, including 64 zero-success states and 5568 correct conditional laws.
Additional controls check parent-first bias, the two-segment correction, finite-
pool bias, independent-pilot unnormalized path masses, deterministic caching,
guide scaling, the normalizer trap and five invalid inputs. These are diagnostic
probability calculations, not climate simulation, gate compilation or benchmarking.

Checker SHA256: `9960c3820c5620d4c8b2b3a19c51e1e5d7601ecff3bc902e0f1d8ba3d0995bf9`.
Report SHA256: `9c797fdfe0977a58ccf7554270040b81fe4c6096f94cc0276ef3dad7ffa78e31`.
The script writes no files. Earlier scientific checkers were not rerun and their
source/results were not altered. No upstream implementation was imported.

Primary sources checked 28 September 2026:

[1] Ragone and Bouchet, GRL 48, e2020GL091197 (2021). Primary HTML methods and
consumer rechecked; no new figure or climate performance interpretation.
https://doi.org/10.1029/2020GL091197

[2] Authors' CESM dataset, Zenodo 4763283. Configuration, five-day selection,
perturbations, ancestry products and scripts inspected as metadata. A direct
runtime download of resampling_CAM_France.py and web file fetches failed; no
script bytes or climate array were newly acquired or analyzed.
https://zenodo.org/records/4763283

[3] Pitt, Silva, Giordani and Kohn, Auxiliary Particle filtering within adaptive
Metropolis-Hastings Sampling, arXiv:1006.1914. Section 2's fully adapted joint law
and normalizing-constant discussion inspected, not its numerical benchmarks.
https://arxiv.org/abs/1006.1914

[4] Jasra, Lee, Yau and Zhang, The Alive Particle Filter, arXiv:1304.0151v1 (2013).
Sections 2.2-2.3, Algorithm 1 and normalizer discussion inspected. The later journal
version adds Del Moral as an author; preprint claims are attributed to that version.
https://arxiv.org/abs/1304.0151

[5] Brassard et al., Quantum Amplitude Amplification and Estimation. Primary
abstract/standard amplification result; no new primitive proposed here.
https://arxiv.org/abs/quant-ph/0005055

[6] Ozols, Roetteler and Roland, Quantum rejection sampling, TOCT 5 (2013).
Primary abstract and author-institution record inspected.
https://arxiv.org/abs/1103.2774

[7] Murray, Lee and Jacob, Parallel resampling in the particle filter,
arXiv:1301.4019. Primary abstract and resampling scope inspected; no GPU benchmark
reproduced. https://arxiv.org/abs/1301.4019

PDF text supplied the equations in [3,4]. Screenshot attempts on their relevant
pages failed; no numerical table or figure was used. Further quantum/particle-
filter keyword searches were nonexhaustive, including irrelevant uses of classical
SMC for quantum-system estimation. Low, Yoder and Chuang's quantum Bayesian-network
sampling (PRA 89, 062315, 2014) is another conditioning precedent, not a climate
implementation: https://doi.org/10.1103/PhysRevA.89.062315 .

Only the parent repository is modified. Direct-sample scope remains; Manthan is
paused, battery/operator routes parked, and the two spin-offs independent. Preserve
historical evidence and rights. No outside contact, paid/unattended work, manuscript,
release, branch merge or repository administration change is authorized.
