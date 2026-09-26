# Sample the interactions before choosing the simplification

26 September 2026. Phase 2; PRX Quantum target; manuscript remains on hold.
Live research-branch base: 90e8b45bc29c99d46da9cb91817930cddcf498cc.
This is a candidate mechanism and finite audit, not a novelty or advantage claim.
Neither user preference nor the desired journal establishes scientific value.

## Independent task

Replace a repeatedly evaluated multivariable model with several inexpensive
small models, while preserving important joint effects under a specified input
law. This is average-case approximation, not exact compiler equivalence or
worst-case correctness. Surrogate modeling and sensitivity analysis already
pursue this task. A usable output needs both variable groups and executable
functions on those groups; a list of interactions alone is not a predictor.

Instead of quantumly evaluating candidate policies, investigate sampling the
interaction structure itself. A classical algorithm can then compare many
possible simplifications using the same record. This reopens mechanism-first
exploration without confining the project to policy learning, LLMs or physics.

## Exact finite interface

Let f:{0,1}^n -> [-1,1] be an explicit deterministic finite-precision program,
with independent uniform input bits. Write

    f(x)=sum_S fhat(S) chi_S(x),  chi_S(x)=(-1)^(sum_(i in S)x_i).

For a partition P of the variables, the best additive-over-blocks approximation is

    f_P(x)=sum_(G in P) E[f|X_G=x_G] - (|P|-1) E[f].

Orthogonal projection and Parseval give its exact mean-square loss:

    L(P)=sum_(S nonempty, S not contained in any block of P) fhat(S)^2.

Likewise, retaining only features J incurs optimal MSE
sum_(S not subset of J) fhat(S)^2. These are standard orthogonal-decomposition
identities, not claimed new theorems. An unrestricted one-block partition has
zero loss; a meaningful size/deployment-cost restriction must come from the
task, not from a desire to defeat the classical solver.

## Quantum sampling without hidden normalization

Prepare uniform x, reversibly calculate f(x), rotate a flag to

    sqrt(1-f(x)^2)|0> + f(x)|1>,

uncompute the value/workspace, apply H^tensor(n) to x, and measure. The sign of
f belongs in its amplitude. The ideal joint measurement law is

    Pr(flag=1,S)=fhat(S)^2.

Keep flag-zero outcomes as NULL records. Their mass is 1-E[f^2]. The probability
that one RAW record crosses a proposed partition is exactly L(P). We do not
postselect until success or assume E[f^2] known. Normalizing only the successful
records instead estimates L(P)/E[f^2], which is a different quantity. Relative
Sobol indices similarly require the variance normalization and precision cost.

For Boolean signs every flag succeeds: this is familiar phase-oracle Fourier
sampling. Quantum learning of Boolean influences and juntas is prior work.
The candidate connection is to the approximation loss of many classical model
partitions, not a new quantum primitive.

For independent known finite laws rho_i, prepare sqrt(rho) and use a local basis
transform mapping each constant mode to zero. Coarse-grain each coordinate to
zero/nonzero. The resulting set mass is ||f_S||^2 for the corresponding functional
ANOVA component. This is the tensor product of constant/complement projectors.
Input preparation and basis transformations are charged. No arbitrary correlated
input distribution, free whitening or coherent model API is assumed.

## Reusable classical record

For M admissible partitions, m >= log(2M/delta)/(2 epsilon^2) independent raw
records suffice for simultaneous additive-epsilon estimates of every L(P).
This is Hoeffding plus a union bound. A partition can be chosen after seeing
the record. A gamma-suboptimal empirical optimizer then has true loss at most
optimum+2epsilon+gamma. Known deterministic complexity penalties can be included.
For all set partitions, Bell(n)<=n^n gives O((n log n+log(1/delta))/epsilon^2)
raw records. Their storage is O(mn) bits, not a complete interaction tensor.

This statistical bound does not make constrained partition optimization cheap.
Both competitors may use the same classical optimizer. A fixed family of feature
panels can be evaluated similarly. Computational costs of scoring and selecting
among them remain separate from the number of samples.

The record loses coefficient signs: f and -f have identical record laws. It
cannot alone predict outputs. For a fixed selected partition with small groups,
the retained signed Walsh basis has d=1+sum_G(2^|G|-1) coefficients. A separate
classical labeled sample bank estimates them with total expected squared
coefficient error <=d/m_fit, because each bounded coefficient estimator has
variance <=1/m_fit. Orthogonality gives expected MSE <=L(P)+d/m_fit. This is an
elementary bound, not an optimized training method. Fitting samples are independent
of group selection in this argument. Exact code analysis and better regression
remain available. Fitting, validation, storage and deployment are not free.

## Strong classical responses

For one bipartition, write independent X=(A,B), X'=(A',B'). Then

    L(A|B)=E[(f(A,B)-f(A',B)-f(A,B')+f(A',B'))^2]/4.

Thus four ordinary model evaluations per trial estimate the same loss, without
listing every interaction. This belongs to established contrast/pick-freeze
sensitivity methodology. For a multiway partition, another unbiased expression is

    E[f^2]-sum_G E[f(X)f(X_G,X'_-G)]+(|P|-1)(E[f])^2.

We cannot advertise a quantum advantage for checking a single split merely
because its Fourier expression contains exponentially many terms. Adaptive
classical partition search, shared evaluations and direct source simplification
must be allowed too.

Sobol tensor trains already represent interaction indices compactly and permit
aggregation, variable selection and model analysis. SPEX uses sparse Fourier
recovery for feature interactions; ProxySPEX learns a tree surrogate and extracts
interactions with fewer original-model evaluations in its reported cases.
These are direct comparators, not obsolete baselines. Their goals include signed
attribution and need not coincide with our squared-mass loss. None was executed
in this pass. Classical sparse Fourier learning also prevents a generic
exponential-speedup claim based merely on a sparse spectrum.

The possible difference is producing a reusable interaction-sensitive record
without first fitting the entire significant spectrum or a low-rank surrogate.
No sparsity assumption is needed for the sampling identity. But neither the
absence of sparsity nor the exact quantum record law is automatically necessary
to solve the user's approximation task. A different adequate classical method
may win. Search results do not establish priority for this formulation.

## Costs and boundaries

Each quantum trial includes reversible f evaluation and its inverse, signed
value-to-amplitude conversion, basis preparation/transforms and measurement.
The ideal rotations require finite-precision synthesis. A small output register
is not a resource estimate. A cheap learned proxy supplies information about the
proxy, not automatically about the original model. An LLM API does not provide
coherent access; a full model implementation could be prohibitively expensive.

The model law is explicit. Independent intervention settings are not arbitrary
observational data. For stochastic f, adding its random tape to the variables
analyzes realized randomness; analyzing its expected response can require an
additional averaging calculation. No such calculation is granted for free.

Absolute MSE is the specified criterion. A loose scaling bound B multiplies
loss by B^2 and can worsen the required precision. Tiny interactions may still
matter for rare events or worst-case decisions that this criterion does not
cover. Correlated inputs can invalidate the decomposition: a parity that has
variance one on independent fair bits is constant on two identical fair bits.
No causal-effect or changed-distribution guarantee follows.

## Checks actually run

The companion diagnostic tests all 256 Boolean sign functions on three bits,
twenty bounded rational functions on four bits, and zero/constant controls:
278 functions, 1610 additive-partition identities, 2400 retained-feature identities,
and 84992 four-corner evaluations. All these comparisons use exact fractions.
Thirty-six numerical ideal-circuit checks agree with the predicted flagged
probabilities within 2.78e-16. A three-bit biased product-law ANOVA check agrees
within 2.78e-17. These are small classical statevector calculations, not a compiled
reversible evaluator or a hardware experiment.

An explicit six-bit example has coefficients 2/7 on three disjoint pairs and
1/7 on a triple crossing those pairs. Its record masses are 4/49,4/49,4/49,1/49,
with NULL mass 36/49. Under maximum block size two, the original pairs minimize
MSE at 1/49. All 203 partitions and 76 admissible partitions were checked. A
4096-trial classical sample from this exact small spectrum chooses the same
blocks. The decomposition is visible in the supplied source: this is NOT an
advantage example. Discarding NULL records incorrectly changes 1/49 to 1/13.

The full diagnostic source, exact report and expanded derivation are in the
conversation checkpoint Quantum_Discovery_Interaction_Record_Scout.zip, rather
than imported into this documentation-only commit. SHA256 of the source is
40ea6a5361758e724eb35fb3a3bb1efd92319b49b115d2fbfd5620c87ae9f061;
the report SHA256 is
0dd3dc33201a1a15050e1944c463d7b13f4fe1fb4b8a576cadb9bc3dc15dedaa.
Reproduce with `OPENBLAS_NUM_THREADS=1 python interaction_record_check.py --output /tmp/new-interactions.json`.
NumPy is used only for numerical circuit checks; remaining arithmetic is standard
library. Reports were regenerated byte-identically in this environment, not
asserted bitwise portable across numerical libraries.

The unchanged supplied active_digits_v1 verifier was rerun and passed, including
native CART and 1797 callback-only replays. The full historical/root verifier was
not rerun. No native SPEX, ProxySPEX, Sobol-TT or language-model benchmark ran.

## Decision

Retain a candidate with a concrete output: use a quantum-generated interaction
record to choose, build and validate a cheaper classical model. The decisive
comparison includes discovery, fitting and later execution, with strong classical
surrogate construction and direct contrast estimators. An original result or
meaningful end-to-end regime is still missing. Do not enlarge the toy to create
a timeout or revive the manuscript. No external contact or paid work occurred.

## Primary sources inspected

1. Chertkov, Ryzhakov, Oseledets. Black Box Approximation in the Tensor Train
Format Initialized by ANOVA Decomposition. SIAM J. Sci. Comput.45,A2101-A2118
(2023), DOI10.1137/22M1514088. Publisher abstract/method scope.
https://epubs.siam.org/doi/10.1137/22M1514088
2. Ballester-Ripoll, Paredes, Pajarola. Sobol Tensor Trains for Global Sensitivity
Analysis, arXiv:1712.00233. Primary abstract and described operations.
https://arxiv.org/abs/1712.00233
3. Kang et al. SPEX: Scaling Feature Interaction Explanations for LLMs. ICML2025,
PMLR267:28878-28903. Proceedings abstract/method; no benchmark reproduced.
https://proceedings.mlr.press/v267/kang25a.html
4. Butler et al. ProxySPEX: Inference-Efficient Interpretability via Sparse
Feature Interactions in LLMs, arXiv:2505.17495v2, revised23 October2025.
Primary abstract/version; no performance results reproduced.
https://arxiv.org/abs/2505.17495
5. Li and Yang. A quantum algorithm for approximating the influences of Boolean
functions and its applications. Quantum Inf. Process.14,1787-1797 (2015),
arXiv:1409.1416v2. Primary abstract and influence interpretation.
https://arxiv.org/abs/1409.1416
6. Atici and Servedio. Quantum Algorithms for Learning and Testing Juntas.
Quantum Inf. Process.6,323-348 (2007). Author publication summary.
https://www.cs.columbia.edu/~rocco/papers/qipjunta.html
7. Owen. Variance Components and Generalized Sobol' Indices. SIAM/ASA JUQ1,
19-41 (2013), DOI10.1137/120876782; arXiv:1205.1774. Primary abstract for
contrast estimators; displayed special cases independently derived and checked.
https://arxiv.org/abs/1205.1774
