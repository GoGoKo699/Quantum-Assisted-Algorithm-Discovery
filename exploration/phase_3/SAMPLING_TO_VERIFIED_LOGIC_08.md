# Sampling to verified logic 08: an existing consumer for quantum examples

28 September 2026. Starting head: `02862ad2bc01266d97b48494dbb9066403c8eb88`.
Branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Decision:** use sample-guided Boolean functional synthesis as the next bounded
sampling contract. The classical output is a verified program/circuit, not a
replica of a quantum distribution. The application interface and classical
sample-source sensitivity are documented. No native synthesis run, useful quantum
advantage, or priority claim is established. This refines Note 07's proposal-learning
hypothesis; it does not change the classical-only deployment objective.

## 1. A concrete consumer, already used without quantum computing

Manthan [1] combines constrained examples, decision-tree learning and formal
repair to generate Boolean functions. Given a relation F(X,Y), it constructs a
function vector Psi(X) such that

$$
\exists Y\,F(X,Y)\quad\Longleftrightarrow\quad F(X,\Psi(X)).
$$

For any input admitting an output, the program must choose a legal output. Inputs
with no legal output impose no obligation. The output is not a list of all
solutions. The official implementation [3] writes Verilog and supplies a separate
Skolem checker against the original QDIMACS specification. This is a real formal
synthesis workflow; an end-user speedup, useful newly synthesized design, or
commercial deployment has not been demonstrated by this project.

The important application precedent is a source-substitution experiment, not just
a claim that sampling matters. Golia et al. [2] replaced Manthan's sample producer
while retaining its synthesis pipeline. Of 609 benchmark problems, the CMSGen
configuration solved 345, versus 275 with QuickSampler, with a 7200-second overall
timeout and a 3600-second sampling timeout. These are the authors' historical
results, not our measurements, a universal runtime ratio, or current best results.
Their Table IV includes hardware-fixpoint and service-related benchmark labels;
those labels alone do not certify our next individual workload's provenance.

Later Manthan2 [4] improves dependency handling, unique-function extraction,
variable retention and repair. The live implementation includes such features and
already calls CMSGen. Comparing against the old QuickSampler configuration would
therefore not be an adequate contemporary baseline. Direct non-sampling synthesis
and knowledge-compilation methods [5] must also be allowed.

## 2. The quantum-to-classical contract

Both designers receive the same explicit relation, X/Y partition and useful
output constraints. Preserve classical preprocessing and elimination of constant
or uniquely defined outputs. Only the unresolved sampling subproblem is eligible
for the proposed replacement. Keep the same learner, repair policy, random seeds
and final independent verification in an initial controlled comparison.

The proposed information flow is:

> specification -> quantum-produced valid examples -> classical learning and
> repair -> universally checked classical logic -> ordinary deployment.

This consumer differs from Note 07's deployed Monte Carlo proposal. The measured
examples now help discover a program directly. General sample-guided synthesis
is prior work [1]; neither the architecture nor its verifier is claimed new.
A faster way to collect examples is only useful if total time to an acceptable
verified program improves, or a genuinely useful program becomes attainable.

The official sample adapter `src/generateSamples.py` calls CMSGen on a temporary
CNF, reads signed assignments, and returns a binary array. The main routine learns
candidate functions and invokes repair. There is no inspected command-line flag
that already imports quantum samples; an independently validated adapter is still
needed. Pin variable order, preprocessing constraints and auxiliary-variable
semantics rather than silently passing a differently interpreted array.

## 3. One implementable quantum source, with its limits

Use standard amplitude amplification [6] as the first fully specified reference
producer, not as a new primitive. Prepare an efficiently specified product prior
w(z), z=(x,y), coherently evaluate F, phase-mark satisfying assignments, uncompute
all predicate workspace, and reflect about the prepared prior state.

Let a=sum_z w(z)F(z)>0. Conditional on successful measurement in the satisfying
subspace, ideal amplification samples

$$
\pi_w(x,y)=\frac{w(x,y)F(x,y)}{a}.
$$

Uniform w gives uniform satisfying *pairs*. Product-biased output literals also
fit the adaptive weighting used by the classical consumer. This preparation has
no input-sized sample database; implementing the explicit predicate, rotations,
reflections, uncomputation and success estimation still costs gates and space.
After measurement, classically check every proposed assignment before admitting
it to the learner. Noise does not preserve the ideal law automatically.

O(1/sqrt(a)) predicate uses versus O(1/a) rejection trials is a comparison with
rejection sampling, not with CMSGen or a modern SAT solver. Small a may coexist
with easy symbolic sampling. Unknown a needs a budgeted stopping/randomization
scheme; a fixed number of amplification rounds can overshoot to zero success.
For a=0, no sampling failure or timeout is a proof of unsatisfiability. A classical
SAT check or another justified feasibility procedure remains part of the workflow.
No quantum query lower bound for the explicit-source workload is asserted.

A related published Grover-mixer QAOA construction [7] preserves equal amplitudes
within cost levels in its ideal model. Its reported random-3SAT scaling is against
random sampling, not complete functional synthesis with strong classical solvers.
Its parameter search and sampling costs also count. It is context for a later
alternative, not a simultaneous implementation project.

### Same examples imply the same downstream law

If two producers deliver the same joint law over complete training batches, and
the downstream learner/repair randomness is matched, the output distribution and
repair behavior are identical in law. This follows by applying the same classical
map to identically distributed inputs. Matching only one-sample marginals is not
sufficient when correlations differ.

Thus the ideal amplification source cannot claim better learning at fixed samples
than a classical producer of the same weighted law. Its possible benefit is the
cost of obtaining that law. A different, task-biased quantum law could instead
improve example quality, but must then beat classical ways of obtaining equally
useful data, not merely classical reproduction of its full Born distribution.

## 4. A short diagnostic: uniform solutions are not uniform inputs

For uniform satisfying pairs, define N_F(x)=|{y:F(x,y)}|. Marginalization gives

$$
\Pr[X=x]=\frac{N_F(x)}{\sum_{x'}N_F(x')}.
$$

Inputs with many acceptable outputs occur more often. Likewise, equal input
literal weights do not imply a uniform feasible-input marginal after conditioning.
The original Manthan work already discusses relation-valued labels and biased
sampling; this is not a newly discovered defect in that method.

The deliberately easy check F_r(x,y)=AND_i(not x OR y_i) has 2^r witnesses for
x=0 and one for x=1. With r=20, 10000 independent uniform-pair samples miss x=1
with probability about 0.9905086. A perfectly fair quantum sampler has the same
marginal. This is an exact counting consequence, not an empirical performance
claim or a reason to impose a uniform-input contract on every synthesis problem.

Crucially, every output can simply be set to one. Standard positive-unate
preprocessing solves this control without sampling. We checked that constant
witness. It would be invalid to disable preprocessing and advertise this instance
as quantum-hard. The control tests our interpretation; it is not the application,
a new algorithm, or a result to spin off.

## 5. Correctness is checked after learning

For an X-only candidate Psi, the standard error query is

$$
E_\Psi(X,Y)=F(X,Y)\land\neg F(X,\Psi(X)).
$$

Unsatisfiability is equivalent to the desired synthesis contract: a counterexample
requires a legal Y and an illegal proposed output for the same X [1]. Sparse,
biased or imperfect training therefore need not corrupt a successfully verified
final program. They can instead make learning or repair expensive or unsuccessful.
A timeout is not verification. Trusted translation and SAT solving must be stated;
independent UNSAT-proof replay is preferable where supported. We have not run
Manthan's checker or produced such a proof in this checkpoint.

## 6. Next experiment and decision rule

Run a small native baseline before committing to circuit engineering. Start with
the official smoke test for installation only. Then trace one application-derived
benchmark's original specification, quantifier partition and intended output.
The repository includes `usb-phy-fixpoint-1.qdimacs`, but a filename alone does not
make it a verified USB design task; that provenance remains to be established.
A randomly generated SAT formula is not the deployed benefit.

For that selected instance, retain preprocessing and profile sample production,
learning, repair and final checking separately. Record final circuit size and
any relevant depth/evaluation constraint. Try classical sample-source substitution
within the same downstream pipeline before a quantum run. Compare both useful
sample quality and complete preparation cost, with classical bypasses allowed.
If preprocessing already solves it, report that outcome rather than disabling it.

For identical batch laws, let f be the fraction of total preparation time spent
producing samples. Even free samples improve the total time by at most 1/(1-f),
holding the remaining work fixed. This elementary accounting bound is useful only
with measured f; no value has been inferred from an old aggregate plot. A change
in sample law can change repair cost and needs its own complete comparison.

Proceed only if either sample cost or source-dependent downstream work leaves a
consequential opportunity. No positive quantum result is required before this
bounded test, but a generic square-root upper bound is not the eventual result.
Do not turn this into a new synthesizer, a large SAT census, or another abstract
classification study. The next deliverable is one instrumented native comparison
and an honest assessment of the candidate quantum sampling budget.

## 7. Checks actually executed

The independent standard-library diagnostic in
`experiments/sampling_synthesis_v1/verify.py` enumerates all 256 relations on two
input bits and one output bit, with all 16 candidate functions: 4096 contract
comparisons, of which 1296 pass and 2800 fail. It also checks exact rational ideal
amplification algebra for two priors and 255 nonempty three-bit relations over
four round states. All 2040 norm checks pass; 44 states have zero success and are
explicitly retained, not treated as samples. The other 1996 states give the correct
conditional law and 7984 projected-input checks. Eight small unate controls and
the analytic r=20 calculation also pass.

The script was run twice with identical JSON; -O and -OO were rejected. It writes
no files. These are finite logic/ideal-state checks, not a gate-level or noisy
simulation, native synthesis, a sampling benchmark, or a quantum resource estimate.
No upstream code was imported. Root and historical scientific suites were not
rerun; their sources and fixtures are unchanged. Native Manthan/CMSGen were not
installed or run; no compiled dependencies or upstream timing results are claimed.

SHA256 of the executed checker:
`15624f3d56fbaa24d43f9d98634ca3b61a8346e59df1cf7e5ce4b0c685a55a7d`.
SHA256 of its deterministic report:
`5ace9be587d6be8fb293af68499a30a9d460f73adee5c8d6f0f8fdc39073b2b3`.

## Primary sources and inspection limits

Checked 28 September 2026. No publication-priority claim; quantum-synthesis
keyword searches returned substantial unrelated material and are not exhaustive.

[1] Golia, Roy and Meel, *Manthan: A Data-Driven Approach for Boolean Function
Synthesis*, CAV 2020. Contract, algorithm and weighting sections inspected;
PDF overview figure visually checked. https://priyanka-golia.github.io/publication/cav20-manthan/cav20-manthan.pdf

[2] Golia, Soos, Chakraborty and Meel, *Designing Samplers is Easy: The Boon of
Testers*, FMCAD 2021. Section V.B, Fig. 3 and Table IV inspected, including PDF
screenshots. Historical experiment, not our reproduction.
https://www.cs.toronto.edu/~meel/Papers/fmcad21.pdf

[3] Official Manthan repository, read only. README, main preprocessing path and
sample adapter inspected; no native execution. https://github.com/meelgroup/manthan
README blob `ed5e093838e493ebcff8c7a9c8c8213f09d0e5b8`;
main blob `ea8eea93c8e5c4501c7abbf24c367cf01347fd82`;
sample adapter blob `654fc7471235b44fcf899920b94de0a991f2aaa7`.

[4] Golia, Slivovsky, Roy and Meel, *Engineering an Efficient Boolean Functional
Synthesis Engine*, ICCAD 2021. Primary abstract and current code paths inspected;
not a new audit of its complete benchmark campaign. https://arxiv.org/abs/2108.05717

[5] Akshay et al., *Counterexample Guided Knowledge Compilation for Boolean
Functional Synthesis*, CAV 2023. Primary abstract inspected; no native comparison.
https://doi.org/10.1007/978-3-031-37706-8_19

[6] Brassard, Hoyer, Mosca and Tapp, *Quantum Amplitude Amplification and Estimation*.
Standard primitive, not a novel synthesis result. https://arxiv.org/abs/quant-ph/0005055

[7] *Grover-QAOA for 3-SAT: Quadratic Speedup, Fair-Sampling, and Parameterization*.
Primary abstract and HTML method sections inspected; no figures used for new
numerical claims. https://arxiv.org/abs/2402.02585

The battery and small-operator candidates remain parked. Both classical spin-offs
remain independent. Only the parent repository is modified; no outside contact,
paid/unattended computation, manuscript, release or branch merge follows.
