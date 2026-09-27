# Phase 3, checkpoint 1: compile a small classical operator

27 September 2026. Starting commit: `22fa0c54076be48ca0a61781645067d56b8161cb`.
The new scientific phase uses the existing working branch; no branch is renamed or merged.
The [parent charter](../phase_2/CHARTER.md) and [project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md) still govern the objective.

**Decision:** investigate quantum compilation of a small classical operator. The first calculation replaces sparse-row selection by a dense, low-dimensional matrix. A conditional exact-arithmetic construction and finite algebra checks are recorded below. No finite-precision circuit theorem, practical speedup, or publication-priority claim is established. Manuscript preparation remains on hold.

## 1. Three mechanisms, one selected calculation

| Mechanism | Reusable output | Strongest immediate objection | Decision |
|---|---|---|---|
| Compile a spectral surrogate | A small matrix used for later energies or linear solves | Existing quantum sparsification already does this; access costs and classical sampling can remove the apparent advantage | Pursue one access-cost calculation, not a new application claim |
| Discover symmetry or reduced coordinates | A smaller classical evaluator | Finding coordinates is not the same as constructing an inexpensive residual evaluator | Park the generic version; do not reopen the closed Boolean-table comparison |
| Train quantumly, predict classically | A compact classical predictor | Some relevant advantages concern streaming memory rather than unrestricted classical discovery time | Retain as a reserve under an explicitly stated access/resource model |

Apers and de Wolf [1] already construct explicit graph sparsifiers quantumly. Thus classical output and reuse are precedents, not our contribution. Apers and Gribling [2] extend spectral approximation to tall matrices. Their Section 2 explicitly accounts for QRAM of size sqrt(N) poly(d); Section 3.2.3 supplies random-oracle access using a query-budget-sized data structure. Source-computed rows alone do not remove that internal memory. Straightforward serial QRAM simulation does not preserve their sublinear time guarantee; this observation is not a lower bound against better implementations.

The hidden-subgroup compression construction [3] includes subgroup information and values on coset representatives. A compact group description alone need not supply a compact evaluator. For the earlier exact Boolean Fourier-dimension model, [Note 15](../phase_2/CLASSICAL_QUOTIENT_RECONSTRUCTION_AUDIT_15.md) already records a classical reconstruction of both coordinates and residual table. Neither observation excludes all useful symmetry reductions.

The 2026 oracle-sketching preprint [4] is directly relevant to classical deployment: it constructs classical predictors for sparse test inputs. Its key comparisons include memory restrictions and sample access. Those statements cannot be relabeled as an unrestricted classical time separation for the present explicit-source problem. Its full proof corpus was not audited here.

## 2. Proposed output and honest input model

Both designers receive the same finite classical row-generating program C and parameters N, d, lambda > 0, and a justified bound R. On index i, C returns a rational vector a_i in R^d, with norm at most R. Define the fixed positive-definite matrix

$$
G=\lambda I+\sum_{i=1}^{N}a_i a_i^T.
$$

The desired classical output is a d-by-d matrix H satisfying

$$
G\preceq H\preceq(1+\epsilon)G,
\qquad 0<\epsilon\leq1.
$$

Here X <= Y in Loewner order means Y-X is positive semidefinite. The output is dense and contains O(d^2) numbers; it is NOT a sparse subset of rows. Low d is therefore part of the prospective useful regime, not a hidden claim of dimension-independent readout.

The proposed quantum implementation must reversibly evaluate C, uncompute its workspace, and implement the arithmetic and flag rotations described below. The classical competitor may inspect C, simplify the sum, choose a different representation, sample nonuniformly, or bypass compilation. A stored arbitrary N-row input does not receive free coherent access. Producing or checking R, if costly, also belongs in the accounting.

This checkpoint separates two claims:

* The matrix argument is exact arithmetic, conditional on additive estimates of specified scalar energies.
* Standard amplitude estimation gives a row-query bound in the ideal coherent-arithmetic model. A complete finite-bit implementation and its gate/space cost remain a next task.

A positive lambda is explicitly part of the selected regularized problem. No singular, unregularized extension is claimed. The source family and downstream application have not yet been selected.

## 3. The short mechanism

Start with a known upper bound H on G. In coordinates scaled by H, the unknown matrix is bounded by the identity. Estimate that small matrix to constant additive accuracy, add a safety margin, and transform back. This improves the upper bound by a constant factor. Repeat until the bound is close enough, then perform one accurate final round.

The quantum step estimates scalar energies. It does not maintain an N-entry random inclusion table or coherently navigate a large learned data structure. Only the current small matrix and scalar estimates are retained between rounds. This avoids the particular random-oracle dependency discussed above, but does not by itself establish a finite-gate implementation or application advantage.

## 4. Exact matrix contraction

Suppose G <= H and factor H=W W^T with W invertible. Let

$$
M=W^{-1}G W^{-T}.
$$

Then 0 < M <= I. Assume a symmetric estimate E obeys

$$
\|E-M\|_2\leq\tau.
$$

Set

$$
H_{\mathrm{new}}=W(E+\tau I)W^T.
$$

Since -tau I <= E-M <= tau I, congruence gives the complete invariant

$$
G\preceq H_{\mathrm{new}}\preceq G+2\tau H.
$$

This proof does not assume that G and H commute. It also shows that the safety shift cannot simply be omitted.

Initialize

$$
H_0=(\lambda+NR^2)I,
\qquad c_0=1+NR^2/\lambda.
$$

Then G <= H_0 <= c_0 G. With tau=1/8, an envelope H_j <= c_j G updates by

$$
c_{j+1}=1+c_j/4.
$$

For K=ceil(log_4 c_0) rounds (zero if c_0=1),

$$
c_K=\frac43+4^{-K}\left(c_0-\frac43\right)
\leq\frac73<3.
$$

A final round with tau=epsilon/6 consequently returns

$$
G\preceq H_{\mathrm{out}}
\preceq G+\frac{\epsilon}{3}H_K
\preceq(1+\epsilon)G.
$$

These are conditional deterministic inequalities, not statements that a numerical estimate certifies its own error.

## 5. Obtaining the small matrix from quantum estimates

For a unit vector v define the data contribution

$$
z_v=\sum_i(v^T W^{-1}a_i)^2.
$$

On a successful previous history, each summand lies in [0,1], and z_v <= 1, because

$$
W^{-1}\left(\sum_i a_i a_i^T\right)W^{-T}\preceq M\preceq I.
$$

Prepare a uniform index register, compute the row and its scaled squared projection, and rotate a flag with that value as its success probability. Uncompute the row workspace. The flag probability is p_v=z_v/N <= 1/N. Non-power-of-two N can be padded with zero rows to a power of two less than 2N. For all possible, including failed, histories, clamp the flag probability to [0,1]; clamping is inactive on the histories used in the proof.

The Brassard-Hoyer-Mosca-Tapp bound [5] gives, with constant success probability,

$$
|\widehat p_v-p_v|
\leq \frac{2\pi\sqrt{p_v(1-p_v)}}{T}+\frac{\pi^2}{T^2}.
$$

Thus the additive error in N times the estimate is at most

$$
\frac{2\pi\sqrt N}{T}+\frac{\pi^2N}{T^2}.
$$

An additive eta estimate of z_v needs O(sqrt(N)/eta) coherent row evaluations in this ideal model. Independent repetitions and a median reduce the failure probability logarithmically. Small probabilities, not a generic O(1/eta) additive bound applied blindly to the mean, are essential to this accounting.

The known contribution lambda v^T W^{-1}W^{-T}v is added classically. Estimate the directions e_j and (e_j+e_k)/sqrt(2) for j<k. The polarization identity is

$$
M_{jk}=v_{jk}^T Mv_{jk}-\frac{M_{jj}+M_{kk}}2.
$$

If each directional estimate has error at most eta, diagonal errors are at most eta and off-diagonal errors at most 2 eta. A symmetric matrix with these entrywise bounds has operator norm at most 2d eta. Choose eta=tau/(2d). There are d(d+1)/2 directional estimates per round.

The resulting conditional row-query bound is

$$
\widetilde O\!\left(
 d^3\sqrt N\left(K+\epsilon^{-1}\right)
\right),
$$

where the tilde hides logarithmic confidence and padding factors. More explicitly, amplify each of the (K+1)d(d+1)/2 estimates to failure at most delta divided by that count. Union bound the conditional failures along successful histories. This handles adaptively chosen H without assuming independence of entire rounds. Abort if a failed numerical round gives a non-positive-definite proposed H. Not aborting is not a correctness certificate.

Only the current d-by-d matrix, its factor, the row workspace, and scalar-estimation workspace are needed in the ideal description. There is no random string indexed by all N rows. Dependence on d is deliberately crude and not claimed competitive with the dimension dependence of [2].

### What is not proved by that formula

The formula counts row queries, not elapsed time or fault-tolerant gates. Finite precision for W, its inverse, the projections, flag rotations, and final matrix storage must be charged. In particular, implementing an ideal flag to a fixed absolute error is not automatically enough: p_v is of order 1/N, and coherent implementation error accumulates over T calls. A valid circuit proof must budget those errors and show that the required bits and reversible workspace do not reintroduce a large access cost. Lambda may be small, so its bit length and the conditioning of intermediate arithmetic cannot be ignored.

No QRAM hardware, quantum circuit, or scalar amplitude estimator was implemented in this checkpoint. This is an alternative construction to audit, not a claim to have already removed QRAM from the published algorithm.

## 6. Why the output is reusable, and what reuse does not prove

For an already supplied b in R^d, let x=G^{-1}b and y=H_out^{-1}b. The generalized eigenvalues lie between 1 and 1+epsilon, hence

$$
\frac{\|y-x\|_G}{\|x\|_G}
\leq\frac{\epsilon}{1+\epsilon}
$$

for nonzero b. This follows by conjugating with G^(1/2) and bounding S^{-1}-I for S=G^(-1/2) H_out G^(-1/2). On the same spectral-success event it holds for every b, including subsequently chosen b. Factoring the small output once permits entirely classical later solves. Ordinary finite-precision solve costs and additional solve error still count.

This does NOT make a new N-entry label vector free to process. If b=A^T y for a newly supplied long vector y, acquiring b is an additional task. Nor does one compiled matrix automatically cover changing rows, weights, or lambda.

For R_use deployments with the same classical use cost U, quantum compilation costs P_Q+R_use U. A classical competitor may pay P_C+R_use U or bypass compilation altogether. Increasing reuse cannot change the sign of P_Q-P_C. Therefore reuse supports usefulness but supplies no discovery advantage by itself.

## 7. Strong classical objections and stopping conditions

The immediate baselines are source-level algebra, exact accumulation of G, classical importance/leverage sampling [6], and application-specific solvers. For example, if lambda >= NR^2/epsilon, the known matrix (lambda+NR^2)I already meets the one-sided target without inspecting any row. A source that visibly lists a rare exceptional row is also not a hidden-search workload.

A useful source family must survive classical methods that sample rows more intelligently than uniformly, exploit low coherence, use known matrix identities, or compute the desired downstream answer without reconstructing G. The OR-style worst-case row-query lower bound in arbitrary matrices does not establish hardness for an explicit program C. No source family has cleared this comparison yet.

**Next bounded task:** audit the conditional construction's finite-precision and circuit costs, alongside a focused predecessor search for QRAM-free, classical-output covariance/Gram approximation. Then choose at most one useful, source-generated fixed-operator family and test its strongest classical route. Do not build a general sparsification framework or a large benchmark first. If prior work already supplies the same construction, attribute and reuse it; usefulness and the complete comparison remain the parent's question.

## 8. Checks actually run

The standard-library [finite algebra verifier](../../experiments/operator_compilation_v1/verify.py) uses exact rational arithmetic. It checks 45 congruence cases, including 30 noncommuting cases; 45 final relative bounds; 180 right-hand-side inequalities; nine polarization identities; 15 scalar contraction schedules; and 12 sufficient amplitude-budget inequalities. Nine negative controls confirm that omitting the safety shift can break the upper-bound invariant.

These are small deterministic checks of the written algebra, not a quantum simulation, amplitude-estimation run, full numerical implementation, proof-assistant verification, or benchmark. The verifier was run twice successfully; its refusal to run under Python -O was also checked. It writes no files.

```sh
python experiments/operator_compilation_v1/verify.py
```

Verified source SHA256: `edd913c220344e94eb45508d87c8f24cd7750312ea1daf6be22b4c9bde391345`.
The root and historical experiment verifiers were not rerun; none of their sources or fixtures changed. Full checkout failed on DNS; the GitHub connector was used for repository access. No upstream implementation was imported or executed.

## 9. Sources and inspection limits

[1] S. Apers and R. de Wolf, *Quantum Speedup for Graph Sparsification, Cut Approximation and Laplacian Solving*, arXiv:1911.07306v4; SIAM J. Comput. 51(6), 2022. Inspected Theorem 1 and computational-model discussion; primary PDF screenshots checked. https://arxiv.org/abs/1911.07306

[2] S. Apers and S. Gribling, *Quantum speedups for linear programming via interior point methods*, arXiv:2311.03215v3, 30 January 2026. Inspected Section 2, Theorem 3.1, and the repeated-halving/random-oracle construction, including Lemmas 3.10-3.12. PDF pages 13 and 19 visually checked. https://arxiv.org/abs/2311.03215

[3] *Information compression via hidden subgroup quantum autoencoders*, arXiv:2306.08047v3. Inspected the oracle/compression interface and coset-representative output; no native experiment reproduced. https://arxiv.org/abs/2306.08047

[4] J. Zhao et al., *Exponential quantum advantage in processing massive classical data*, arXiv:2604.07639v1, April 2026. Inspected introductory models, oracle sketching, classical readout, and stated classical-memory comparisons. This was not an audit of all 144 pages or a new verification of its theorems. https://arxiv.org/abs/2604.07639

[5] G. Brassard, P. Hoyer, M. Mosca, A. Tapp, *Quantum Amplitude Amplification and Estimation*, arXiv:quant-ph/0005055, Theorem 12. This is the source of the scalar-estimation primitive, not a new primitive proposed here. https://arxiv.org/abs/quant-ph/0005055

[6] M. B. Cohen et al., *Uniform Sampling for Matrix Approximation*, arXiv:1408.5099. Primary abstract and its use in [2] inspected. Classical row sampling must be permitted; no native baseline was run. https://arxiv.org/abs/1408.5099

Additional keyword searches for prior QRAM-free spectral/covariance constructions produced substantial irrelevant results and do not constitute an exhaustive novelty search. The contraction and its proposed composition are internally derived here; priority, optimality, and significance remain unassessed. Both classical spin-offs and all historical evidence remain separate and unchanged.
