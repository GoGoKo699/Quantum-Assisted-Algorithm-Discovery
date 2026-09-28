# Continuation information 13: test the unresolved variation, not the whole ensemble

28 September 2026. Starting head: `298abebe763c4030d697de47d7366ed97710e902`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision:** retain the direct-sampling investigation, but do not assign a quantum
cost advantage before examining raw sibling continuations. This checkpoint
specifies a stronger classical comparator and the exact data needed to test it.
The climate arrays and scripts have NOT been acquired. No within-parent variance,
acceptance probability, native runtime or application advantage has been measured.

The [segment construction](SEGMENT_SELECTION_12.md) remains a conditional,
law-correct construction, not a forecast or a proof of useful acceleration.
The consumer remains the [CESM France extreme-summer experiment](HEATWAVE_SAMPLING_CONTRACT_11.md).
No new physical model or alternative application is selected.

## 1. What the source actually makes available

The authors' Zenodo record [1] distinguishes raw simulation arrays (`*_ens`) from
arrays reconstructed along the effective genealogy (`*_eff`). Its France
resampling archive is described as containing regional temperature histories and
selection information for ten experiments. This may allow grouping children by
their immediate restart parent, but the variable schema and indexing have not
been inspected. Metadata alone does not establish that every required pair or
perturbation flag is present.

The record also supplies separate selection, restart-shuffling, and perturbation
scripts. Its documented perturbation scale is 10^-4 in spectral potential-
temperature amplitudes, with the factor for one harmonic shared across vertical
levels. The exact clone kernel, random-number distribution, seed bookkeeping and
whether any member is retained without perturbation require source inspection.
The scale is not a bound on the resulting five-day temperature divergence.

The published procedure scores completed five-day segments and then clones and
perturbs selected states [2]. Thus, siblings created by a selection step must be
compared over the NEXT segment, before that next segment is selected again.
Comparing the score that originally caused cloning answers a different question.

## 2. The information that a fast selection step must add

For one fixed checkpoint population, retain Note 12's parent weights w_i,
continuation laws K_i and positive guide scores G_i(y). Define

$$
a_i=\mathbb E_{K_i}G_i,\qquad v_i=\operatorname{Var}_{K_i}(G_i).
$$

For a parent sampled with weights w, elementary total variance gives

$$
\operatorname{Var}(G)=\operatorname{Var}_{i\sim w}(a_i)
+\sum_iw_i v_i.
$$

Large differences between unrelated parents need not imply large variation among
continuations of the same parent. Conversely, small perturbations need not imply
small finite-time score variation. Neither inference is justified without data.
Small within-parent variation would weaken this continuation-selection mechanism;
it would not rule out faster physical propagation or other quantum samplers.

A large between-parent term may still be computationally costly to discover.
Classical lookahead, pilot estimates and caching must therefore be priced, not
assumed free. The relevant question is what score information remains expensive
after those legitimate classical methods are allowed.

## 3. A stronger, exact classical comparator

The same joint target as Note 12 is

$$
Q(i,dy)=w_i K_i(dy)G_i(y)/Z,\qquad Z=\sum_iw_i a_i.
$$

Suppose a computable bound b_i >= G_i(y) is valid for every allowed continuation
of parent i, with B=sum_i w_i b_i. Select parent i classically with probability
w_i b_i/B, generate y from K_i, and accept it with probability G_i(y)/b_i.
The accepted unnormalized density is exactly

$$
\frac{w_i b_i}{B}K_i(dy)\frac{G_i(y)}{b_i}
=\frac{w_iK_i(dy)G_i(y)}{B}.
$$

Therefore success probability is Z/B and the accepted law is Q. This is standard
rejection-sampling algebra, written to specify the comparator; no new primitive
or novelty claim is made. It needs no separate estimate of each a_i. If a global
bound M exists and b_i <= M, it is never worse in acceptance than using M for
every parent. Building b_i, generating a parent, and evaluating each continuation
still cost resources.

A useful sufficient condition is G_i(y) >= b_i/R for all relevant i,y. Then
Z/B >= 1/R and this classical method needs at most R continuation attempts per
accepted child. Different parents can have enormously different typical scores
while this within-parent factor R remains small. A constant rescaling of all
scores cancels from this comparison.

This is NOT a claim that such tight bounds have already been found for CESM.
The maximum among observed siblings is not a bound for unseen continuations.
Confidence intervals for a mean are not pointwise bounds either. A loose or
expensive envelope can remove this benefit. A quantum producer may use the same
parent preconditioning; its residual acceptance and its full cost must then be
recomputed. Both producers are improved fairly, rather than comparing an improved
classical sampler with an intentionally naive quantum one.

For the climate exponential guide, ratios between two continuations of the same
parent satisfy G_i(y)/G_i(y')=exp(k integral_segment [A_y-A_y'] dt).
Only the variation of the segment integral appears; the parent's already-known
history cancels. No numerical sibling spread or acceptance rate is substituted
for the missing data. Near-constant guides may make local correction easy, but
small empirical spread is not a guarantee of negligible full-season tail error.

## 4. The data analysis to run once the files are present

First validate archive digests, inspect the script bytes without executing them,
and derive the exact time and parent-index convention. Then:

- Use raw, pre-next-selection segment records. Group children by immediate
  restart parent, batch and checkpoint. Do not use eventual survivors alone.
- Distinguish genuinely perturbed siblings, retained unperturbed members, copied
  records and any reused random inputs. No independence is inferred from names.
- Compute the source-defined segment integral and log score. For groups with
  at least two comparable fresh continuations, report within-group spreads and
  variances along with all group sizes. A group with one child has unknown
  within-parent variance, not zero variance.
- State the weighting of every pooled diagnostic. Frequently cloned parents
  are overrepresented; a child-count-weighted result is not automatically an
  estimate for the original parent mixture. Report missing-parent coverage.

Children may be conditionally independent if their perturbations are generated
independently from the same restart. The scripts must support that assumption.
They remain genealogically dependent across times and unconditionally. Population-
level replication, terminal importance weights and the required circulation
observable govern final uncertainty, not the number of descendants.

These records can provide a retrospective diagnostic. They cannot certify
unseen-score envelopes, determine all counterfactual continuations, validate a
new guide on the same data used to choose it, or establish a quantum gate budget.
A useful final comparison remains total cost at matched scenario/composite
uncertainty, allowing weighted classical output. It is not rejection count alone.

Independent 2026 work on TEAMS [3] explicitly measures ensemble spreading from
shared initial states to choose splitting lead times. Its model is an idealized
GCM with a different stochastic forcing, not these CESM experiments. It supports
the diagnostic approach, not a transferable five-day variance or performance
number. We do not import its forcing, model or speedup into the France task.

## 5. Restart access remains a separate missing quantity

The documented scalar archive contains regional averages and selection records;
it is not described as a collection of full model restart states. Those scalars
are sufficient for some score/ancestry diagnostics, not for propagating a new
atmospheric realization. The score is not established to be a closed dynamical
state.

A coherent continuation must have the state used by the active atmosphere and
land components, the relevant coupler/time/forcing state, prescribed parameters,
the declared perturbation seed and accumulated event statistics, or a separately
validated sufficient representation. The run and shuffle scripts can identify
which files the actual setup uses; their sizes and physical logical encoding
remain unmeasured. A 13.3 MB diagnostic archive is not a quantum-memory estimate.

Cost also includes reconstructing the selected full segment. Existing trajectory
means cannot stand in for unarchived histories. Exact sampling under a declared
perturbed numerical kernel does not itself validate that kernel's approximation
to an unperturbed climate model or the real atmosphere. Keep the same approved
kernel and model-quality target on both sides.

## 6. Minimal access packet and stopping point

The following original files are listed in Zenodo 4763283 [1]. MD5 values below
are the RECORD'S values, not newly verified checksums:

| File | Listed MD5 |
|---|---|
| `CAM4_F2000_p144_GK_France_k30_resampling.tar` (13.3 MB) | `b3ebb1baa943dd0959584d235f94935b` |
| `resampling_CAM_France.py` | `24dd0d9af6d5e559759eced621a0836d` |
| `shuffleic_CAM.py` | `ddfbe708da0b370cf14f137728b8885b` |
| `perturb_ic_spectral_fac` | `c289113b811aace887be1ceb44004441` |
| `extract_observable_CAM` | `f9e1c04bacdd530e1f19b7abaeb2fbcf` |
| `CAM4_F2000_p144_GK_France_k30_PT10m4_scale1_batch_0001.GK_run` | `5e17a56f74fa794de9ea5d077ff0a033` |

No global field-composite archives or new model runs are needed for this first
inspection. A local copy/upload of this packet would remove the immediate
transfer obstacle. The old battery archive is unrelated and must not be requested
again. Inspect data rights before any redistribution; no climate bytes are
relicensed by the parent's MIT license.

Runtime requests failed on DNS; the separate download tool failed for the France
archive and selection script. Web record metadata and primary paper text worked,
but script/preview transfers failed. A GitHub search found no matching source
mirror, and plugin discovery returned no Zenodo connector. These are access
limitations, not evidence that the classical problem is intrinsically difficult.

**Stop here rather than extend the artificial examples.** The analytic comparator
and analysis specification are complete. The application-specific measurement is
not complete until the original records are actually read. Circuit engineering
remains deferred; direct useful sampling is not rejected or replaced.

## 7. Evidence and sources

This checkpoint contains source inspection, elementary comparator algebra and
an explicit data-analysis protocol. No climate array, sampling run, gate simulation,
new scientific code, experiment, forecast, native timing or scientific verifier
was executed. The arXiv methods-page screenshot attempt failed; no figure-derived
numbers were used. Documentation hashes and the repository diff are checked
separately; they are not scientific validation. Earlier scientific files remain
unchanged. Only the parent repository is writable in this project context.

Sources checked 28 September 2026:

[1] Ragone and Bouchet, authors' dataset, version v1 (20 May 2021), description,
file inventory and recorded checksums. https://zenodo.org/records/4763283

[2] Ragone and Bouchet, *Rare Event Algorithm Study of Extreme Warm Summers and
Heatwaves Over Europe*, GRL 48, e2020GL091197 (2021), published Methods Section 2.2.
https://doi.org/10.1029/2020GL091197
The arXiv v2 was also consulted as a preprint, not substituted for final-version
numerical results. https://arxiv.org/abs/2009.02519

[3] Finkel and O'Gorman, *Rare Event Sampling for Moving Targets: Extremes of
Temperature and Daily Precipitation in a General Circulation Model*, JAMES 18,
e2025MS005456 (2026), model specification and Section 4.4. Primary HTML text
inspected; no figures digitized or experiment reproduced.
https://doi.org/10.1029/2025MS005456

No new repository, spin-off, manuscript, outside contact, paid/unattended work,
release, branch merge or repository-administration change follows. Manthan remains
paused, battery/operator routes parked, and the two classical spin-offs independent.
