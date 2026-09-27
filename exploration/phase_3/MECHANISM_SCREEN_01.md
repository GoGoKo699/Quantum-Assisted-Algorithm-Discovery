# Phase 3, checkpoint 1: compile a small classical operator

27 September 2026. Starting commit: `22fa0c54076be48ca0a61781645067d56b8161cb`.
The new scientific phase uses the existing working branch; no branch is renamed or merged.
The [parent charter](../phase_2/CHARTER.md) and [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md) still govern the objective.

**Decision:** investigate quantum compilation of a small classical operator. The first calculation replaces sparse-row selection by a dense, low-dimensional matrix. We have a conditional exact-arithmetic argument and finite algebra checks, not a finite-precision circuit theorem, practical speedup, or priority claim. Manuscript preparation remains on hold.

## 1. Three mechanisms screened

| Mechanism | Reusable output | Immediate objection | Decision |
|---|---|---|---|
| Compile a spectral surrogate | A small matrix for later energies or solves | Existing quantum methods; access costs and classical sampling | Pursue one access-cost calculation |
| Discover symmetry or coordinates | A smaller evaluator | Coordinates need not supply a cheap residual evaluator | Park the generic version |
| Train quantumly, predict classically | A compact predictor | Memory separation is not unrestricted classical time separation | Reserve, with its access model explicit |

Apers and de Wolf [1] already output explicit graph sparsifiers quantumly; classical output and reuse are not new here. Apers and Gribling [2] extend spectral approximation to tall matrices. Their Section 2 explicitly accounts for QRAM of size sqrt(N) poly(d), and Section 3.2.3 provides random-oracle access through a query-budget-sized data structure. Source-computed rows do not remove that internal memory. Straightforward serial QRAM simulation does not preserve the sublinear time guarantee; this is not a lower bound against better implementations.

Hidden-subgroup compression [3] includes subgroup information and coset-representative values. For our earlier exact Boolean Fourier-dimension model, [Note 15](../phase_2/CLASSICAL_QUOTIENT_RECONSTRUCTION_AUDIT_15.md) already records classical reconstruction of coordinates and residual table. Neither observation excludes every useful symmetry reduction.

The 2026 oracle-sketching preprint [4] constructs classical predictors for sparse test inputs. Its key comparisons involve memory and sample access; they cannot be relabeled as an unrestricted time separation for our explicit-source task. Its full proof corpus was not audited here.

## 2. Input and output

Both designers receive the same finite classical program C. On index i it returns a rational vector a_i in R^d. Parameters N, d, lambda > 0, and a justified bound ||a_i|| <= R are supplied. The fixed target is

$$
G=\lambda I+\sum_{i=1}^{N}a_i a_i^T.
$$

Compile a classical d-by-d matrix H with

$$
G\preceq H\preceq(1+\epsilon)G,
\qquad 0<\epsilon\leq1.
$$

Loewner order X <= Y means Y-X is positive semidefinite. The output contains O(d^2) numbers and is dense, NOT a sampled subset of rows. Low d is part of the prospective useful regime. No singular, unregularized extension is claimed.

The quantum implementation must reversibly evaluate C, uncompute workspace, and pay for arithmetic and rotations. Arbitrary stored N-row inputs do not receive free coherent access. Any costly construction or validation of R counts. The classical competitor may inspect C, simplify the sum, choose another representation, sample nonuniformly, or bypass compilation.

**Two levels:** the matrix argument below is exact arithmetic conditional on scalar estimates. Standard amplitude estimation supplies an ideal coherent-arithmetic row-query bound. A complete finite-bit circuit and its gate/space costs remain unproved. No useful source family has yet been selected.

## 3. Matrix contraction

Start with G <= H and factor H=W W^T. Then

$$
M=W^{-1}G W^{-T},\qquad 0\prec M\preceq I.
$$

Given symmetric E with ||E-M||_2 <= tau, set

$$
H_{\mathrm{new}}=W(E+\tau I)W^T.
$$

Because -tau I <= E-M <= tau I, congruence proves

$$
G\preceq H_{\mathrm{new}}\preceq G+2\tau H.
$$

No commutativity is assumed. The safety shift cannot simply be omitted.
Initialize

$$
H_0=(\lambda+NR^2)I,\qquad c_0=1+NR^2/\lambda.
$$

Thus G <= H_0 <= c_0 G. With tau=1/8, the envelope updates by c_{j+1}=1+c_j/4. After K=ceil(log_4 c_0) rounds (zero if c_0=1),

$$
c_K=\frac43+4^{-K}\left(c_0-\frac43\right)\leq\frac73<3.
$$

One final round at tau=epsilon/6 gives

$$
G\preceq H_{\mathrm{out}}\preceq G+\frac{\epsilon}{3}H_K
\preceq(1+\epsilon)G.
$$

Interpretation: scale by the current upper bound, estimate the bounded small matrix, add a safety margin, and scale back. Constant-accuracy rounds improve the bound; only the last round needs the requested accuracy.

## 4. Scalar quantum estimates

For a unit vector v, the data energy is

$$
z_v=\sum_i(v^T W^{-1}a_i)^2.
$$

On a successful preceding history, each summand is in [0,1] and z_v <= 1, since the normalized data Gram matrix is at most M <= I. Prepare a uniform index, compute the scaled squared projection, rotate a flag with that success probability, and uncompute. Its probability is p_v=z_v/N <= 1/N. Pad with zero rows to a power of two less than 2N when needed. Clamp probabilities to [0,1] on arbitrary histories; this is inactive on histories used in the proof.

The Brassard-Hoyer-Mosca-Tapp estimate [5] obeys, with constant success probability,

$$
|\widehat p_v-p_v|\leq
\frac{2\pi\sqrt{p_v(1-p_v)}}{T}+\frac{\pi^2}{T^2}.
$$

Therefore the additive error in N times the estimate is at most

$$
\frac{2\pi\sqrt N}{T}+\frac{\pi^2N}{T^2}.
$$

Estimating z_v within eta costs O(sqrt(N)/eta) coherent row evaluations in the ideal model. Repetition and a median amplify confidence. Exploiting the small probability is essential; blindly estimating the mean to additive eta/N would give a worse bound.

Add the known contribution lambda v^T W^{-1}W^{-T}v classically. Estimate directions e_j and v_jk=(e_j+e_k)/sqrt(2). Polarization gives

$$
M_{jk}=v_{jk}^T Mv_{jk}-\frac{M_{jj}+M_{kk}}2.
$$

Directional errors at most eta give diagonal error at most eta and off-diagonal error at most 2 eta. The symmetric error matrix has norm at most 2d eta. Set eta=tau/(2d); there are d(d+1)/2 estimates per round. Consequently the conditional row-query bound is

$$
\widetilde O\!\left(d^3\sqrt N\left(K+\epsilon^{-1}\right)\right).
$$

Amplify each of the (K+1)d(d+1)/2 estimates to failure at most delta divided by that count. A union bound on conditional failures along successful histories handles adaptive H; entire rounds need not be independent. Abort if a failed round proposes a non-positive-definite H. Not aborting is not a correctness certificate.

The ideal description retains only the small matrix, its factor, scalar estimates, and row/estimation workspace. No random string is indexed by all N rows. Dependence on d is crude and not claimed competitive with [2]. This is a different construction, not a completed removal of QRAM from the published sampling algorithm.

### Finite-precision boundary

Row queries are not elapsed time or fault-tolerant gates. Charge factorization, inverse computation, projections, flag rotations, and output storage. The probabilities are at most 1/N and implementation error accumulates through coherent calls. A fixed absolute flag error is not automatically sufficient. A circuit proof must budget precision, including small lambda, and show that the required bits and reversible workspace preserve the intended resource bound. No such circuit, scalar amplitude estimator, or QRAM hardware was implemented here.

## 5. Classical use and the comparison

For an already supplied nonzero b in R^d, set x=G^{-1}b and y=H_out^{-1}b. Conjugate by G^(1/2); the eigenvalues of S=G^(-1/2)H_out G^(-1/2) lie in [1,1+epsilon]. Bounding S^{-1}-I gives

$$
\frac{\|y-x\|_G}{\|x\|_G}\leq\frac{\epsilon}{1+\epsilon}.
$$

On the same spectral-success event this holds for every b, including later chosen b. Factor the small output once, then solve classically. Finite-precision solve cost and error still count. If b=A^T y for a newly supplied N-entry label vector, acquiring b is an additional task. One compiled matrix does not automatically handle changed rows, weights, or lambda.

With R_use deployments at common use cost U, compare P_Q+R_use U against P_C+R_use U and classical bypasses. Reuse cannot change the sign of P_Q-P_C. It supports usefulness, not a discovery advantage by itself.

Classical baselines include source-level identities, exact accumulation, importance/leverage sampling [6], low-coherence sampling, and direct downstream algorithms. For example, if lambda >= NR^2/epsilon, the supplied bound already makes (lambda+NR^2)I a valid output with no row queries. A source-visible rare exception is not a hidden-search workload. Worst-case OR-style row-query lower bounds do not establish hardness for the explicit program C.

**Next bounded work:** audit finite-precision circuit costs and the closest QRAM-free, classical-output covariance/Gram predecessors. Then select at most one useful source-generated fixed-operator family and test the strongest classical route. Do not build a general framework or large benchmark first. If the construction is already known, attribute and use it; the parent's complete advantage comparison remains the question.

## 6. Checks actually run

The standard-library [verifier](../../experiments/operator_compilation_v1/verify.py) checks exact rational finite controls: 45 congruence cases (30 noncommuting), 45 final relative bounds, 180 right-hand-side inequalities, nine polarization identities, 15 scalar schedules, and 12 sufficient amplitude-budget inequalities. Nine negative controls show that omitting the safety shift can violate the invariant.

These are not quantum simulations, amplitude-estimation runs, benchmarks, proof-assistant verification, or a full numerical implementation. The verifier passed twice; its -O refusal was checked. It writes no files.

```sh
python experiments/operator_compilation_v1/verify.py
```

Verified source SHA256: `edd913c220344e94eb45508d87c8f24cd7750312ea1daf6be22b4c9bde391345`.
Root and historical verifiers were not rerun; their code and fixtures are unchanged. Full checkout failed on DNS; repository access used the GitHub connector. No upstream implementation was imported or executed.

## 7. Sources and inspection limits

[1] S. Apers and R. de Wolf, *Quantum Speedup for Graph Sparsification, Cut Approximation and Laplacian Solving*, arXiv:1911.07306v4; SIAM J. Comput. 51(6), 2022. Theorem 1 and model discussion inspected; primary PDF screenshots checked. https://arxiv.org/abs/1911.07306

[2] S. Apers and S. Gribling, *Quantum speedups for linear programming via interior point methods*, arXiv:2311.03215v3, 30 January 2026. Section 2, Theorem 3.1, repeated halving and Lemmas 3.10-3.12 inspected. PDF pages 13 and 19 visually checked. https://arxiv.org/abs/2311.03215

[3] *Information compression via hidden subgroup quantum autoencoders*, arXiv:2306.08047v3. Oracle/compression interface and coset-representative output inspected; no experiment reproduced. https://arxiv.org/abs/2306.08047

[4] H. Zhao et al., *Exponential quantum advantage in processing massive classical data*, arXiv:2604.07639v1, April 2026. Introductory models, oracle sketching, classical readout, and stated memory comparisons inspected; not a full 144-page proof audit. https://arxiv.org/abs/2604.07639

[5] G. Brassard, P. Hoyer, M. Mosca, A. Tapp, *Quantum Amplitude Amplification and Estimation*, arXiv:quant-ph/0005055, Theorem 12. Source of the standard scalar primitive. https://arxiv.org/abs/quant-ph/0005055

[6] M. B. Cohen et al., *Uniform Sampling for Matrix Approximation*, arXiv:1408.5099. Primary abstract and its use in [2] inspected; no native classical baseline was run. https://arxiv.org/abs/1408.5099

Additional keyword searches produced substantial irrelevant results and are not an exhaustive novelty audit. The contraction and proposed composition are internally derived here; priority, optimality, and significance remain unassessed. Both classical spin-offs and all historical evidence remain separate and unchanged.
