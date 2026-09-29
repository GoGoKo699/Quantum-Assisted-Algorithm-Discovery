# Positive spatial windows 21: sample finite regions without dropping collective correlations

29 September 2026. Baseline: `dfecc43cccda4843a209a9a55f5dc8547850c0ad`.
Branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Outcome:** the full collective spectrum of a bounded nearest-neighbor chain,
at a fixed positive Lorentzian linewidth, has a positive finite-window mixture
approximation with an explicit TV error independent of total chain length. The
proof retains collective correlations inside each window and bounds the effects
of cutting the bonds. It uses established locality and resolvent methods, not a
new locality principle. The same reduction benefits classical and quantum
sampling; it is NOT a quantum-classical separation or an experimental NMR result.

This resolves the window-law question in [Note 20](SMOOTH_RESPONSE_COMPRESSION_20.md).
No generic spectral filter, small-gap promise or learned classical program is
required. The next comparison concerns the cost of the response within a necessary
finite region, rather than the dimension of the whole chain. These are theoretical
model results; an individual molecule or data download is not a prerequisite.

## 1. Model and output stay fixed

Use the high-temperature spin-response model of [1,2] and Notes 15-20:

$$
H=\sum_{i=1}^n\delta_iS_i^z+
  \sum_{i=1}^{n-1}J_i\,\mathbf S_i\cdot\mathbf S_{i+1},
\qquad O=\sum_{i=1}^n S_i^+,\quad S^a=\sigma^a/2.
$$

The main family has even n, delta_i=(-1)^i d and uniform J, but the proof allows
arbitrary real on-site offsets and |J_i|<=J_*. Local parameter bounds and coefficient
bit lengths remain inputs. The chain is a structural subfamily of scalar-coupled
NMR models, not a claim that every measured molecule has this topology. Neglected
long-range bonds or other relaxation mechanisms need separate justification.

Use the normalized Hilbert-Schmidt inner product
<A,B>_tr=2^-n Tr(A^dagger B). Then ||O||_tr^2=n/2 and o=O/sqrt(n/2) is a unit
operator vector. The desired unbroadened probability measure is the spectral law
of L=[H,.] in o. Equivalently, its energy-gap weights are
|<a|O|b>|^2/Tr(O^dagger O). The target density is

$$
p_{H,\gamma}=\mu_{H,O}*\ell_\gamma,\qquad
\ell_\gamma(x)=\frac{\gamma}{\pi(x^2+\gamma^2)},\quad\gamma>0.
$$

Both sides return the same prescribed bin labels to the same allocated absolute
TV accuracy, including overflow bins. The theorem is first proved for the entire
continuous law, so common binning preserves it. This is normalized correlation
shape, not absolute intensity, finite-temperature Gibbs response, or an arbitrary
signed pulse signal. Per-draw law error and finite-sample statistical error are
different; M draws do not automatically have the same joint-TV tolerance as one.

## 2. Construct a positive law before estimating its error

For an integer block limit ell>=1, choose s uniformly in {0,...,ell-1}. Cut bond
b between sites b and b+1 exactly when b mod ell=s. Let C_s be this set of bonds
and let the resulting intervals be B in P_s. All intervals have size at most ell;
short intervals at the physical ends are retained, not discarded or wrapped.

Let H_s contain the original on-site terms and all uncut interactions. Each
partition yields a disjoint-block Hamiltonian. Its collective spectral law is
EXACTLY the positive mixture

$$
p_s=\sum_{B\in\mathcal P_s}\frac{|B|}{n}\,p_{H_B,O_B,\gamma},
\qquad O_B=\sum_{i\in B}S_i^+.
$$

Proof: the full correlation is the sum of block autocorrelations plus cross terms.
Different blocks evolve independently, and Tr(O_B)=Tr(O_B(t))=0. Thus the cross
terms vanish under the product infinite-temperature trace; ||O_B||_tr^2=|B|/2
fixes the weights. Correlations between different spins INSIDE B remain included.

Our candidate is

$$
\bar p_\ell=\frac1\ell\sum_{s=0}^{\ell-1}p_s.
$$

Across shifts the intervals overlap. There are no negative inclusion-exclusion
weights, no postselection and no histogram repair. Sample s, sample a site i
uniformly from {1,...,n}, and use the block containing i. This selects each block
with probability |B|/n. Then obtain one sample of its collective response at the
original gamma. The choice of block is entirely classical and precedes any quantum
state preparation: coherent access to the full chain is not needed by this step.

Keep the original delta_i in every block. Removing a block's carrier without
adding it back changes the law. For n<=ell one can instead choose the uncut whole
chain and incur zero spatial approximation error. The averaged construction above
remains well-defined even in that case, but is unnecessary.

## 3. A locality envelope and the collective boundary norm

We first state the bound using any valid single-site Lieb-Robinson envelope,
uniform over contiguous intervals I and both time directions:

$$
\|[S_k^\alpha,\tau_t^I(S_j^+)]\|
 \leq\min\{1,C\exp(v|t|-\mu|j-k|)\},
\quad C\geq1,\ \mu>0.
$$

Here k is an endpoint of I, alpha is x/y/z, and the norm is operator norm.
Finite-range locality gives such constants independently of n [3,4]. In an
interaction picture for the on-site fields, the remaining bonds are time-dependent
but have the same support and norm. Thus propagation constants can be chosen using
J_* rather than the magnitudes of the on-site frequencies. This does not make
large-offset quantum simulation or coefficient arithmetic free.

A conservative explicit choice for this spin-1/2 chain is C=2, mu=1 and
v=(9 exp(1)/2)J_*. In [3, Theorem 1], bond commutator generators have norm at most
3J_*/2, each bond overlaps at most three bond terms, and the range is one. The
single-site prefactor is bounded by 2. Single-site/disconnected intervals satisfy
the same enlarged envelope trivially. These constants are deliberately loose,
not a measured propagation velocity or an optimal Lieb-Robinson bound.

Define

$$
a=2+\frac{\log C}{\mu}+\frac{2}{(e^\mu-1)^2},
\qquad b=\frac v\mu.
$$

For an endpoint k, the following bound is independent of |I|:

$$
\|[S_k^\alpha,\tau_t^I(O_I)]\|_{\rm tr}^2\leq a+b|t|.
$$

To prove it, split O_I into sites at distances at most
R=ceil[(v|t|+log C)/mu] and the remaining sites. The near sum has normalized
HS norm sqrt((R+1)/2), by orthogonality of distinct S_j^+ and unitary invariance.
Commutation by S_k^\alpha has induced HS norm at most one. The far sum is bounded by
the geometric LR tail 1/(e^mu-1). Squaring their sum, using (x+y)^2<=2x^2+2y^2
and R+1<=(v|t|+log C)/mu+2, proves the claim. This square-root norm control is
stronger than summing the norms of every nearby spin separately.

Let D_s=L-L_s and let A_c(t)=[h_c,exp(-it L_s)O] for a cut c. Each A_c acts on
the two adjacent blocks and has zero partial trace over EITHER block. Indeed,
it is a sum of [S,O_B(t)] tensor S and S tensor [S,O_B'(t)], and every factor
has zero trace. Distinct cut residuals are therefore HS-orthogonal, including
neighboring cuts that share one block. The remaining block supplies a zero trace.

This orthogonality concerns residuals of the CUT dynamics under the normalized
trace. It does not assert that physical collective correlations vanish.
With S_s=sum_{c in C_s} J_c^2, triangle inequality within one cut and the endpoint
bound give

$$
\boxed{\|D_s e^{-itL_s}o\|_{\rm tr}^2
 \leq \frac{18S_s}{n}(a+b|t|).}
$$

The factor 18 follows from ||A_c||_tr<=3|J_c|sqrt(a+b|t|) and ||O||_tr^2=n/2.
Summing residual norms linearly would lose the square-root cancellation and could
incorrectly reintroduce an extensive error. This is the collective accounting that
a single-site locality statement alone does not provide.

## 4. Full-law theorem: spatial cuts have a linewidth-controlled error

Define

$$
X_\ell=\frac{9}{n\ell\gamma^2}\sum_{i=1}^{n-1}J_i^2
          \left(a+\frac b{2\gamma}\right).
$$

Then the positive mixture satisfies

$$
\boxed{d_{\rm TV}(p_{H,\gamma},\bar p_\ell)
 \leq\min\{1,X_\ell,\sqrt{X_\ell/2}\}.}
$$

There is no n-dependent factor beyond the bounded mean-square coupling. No
minimum spectral gap, sharp spectral filter, parity-purity assumption, exact
memory decay or reconstruction of the full eigenbasis is assumed. The linewidth
is unchanged. The theorem is sufficient; an inadequate bound is not a hardness
result or a proof of actual approximation failure.

### Proof by resolvents, including the first-order cancellation

Use z=omega+i gamma, R=(z-L)^-1 and R_s=(z-L_s)^-1. The space of sums of
single-block traceless operators is invariant under L_s and its resolvent.
It contains o. D_s maps that space to sums of two-block operators with zero
partial traces, which are orthogonal to the single-block space. Consequently

$$
\langle o,R_s D_s R_s o\rangle_{\rm tr}=0.
$$

The second resolvent identity used twice gives

$$
R-R_s=R_sD_sR_s+R_sD_sRD_sR_s.
$$

After the vanished term, the absolute scalar error is bounded by
||D_s R_s^dagger o||_tr ||D_s R_s o||_tr/gamma. No reality assumption on the
observable or replacement of a square by an absolute square is needed.
Vector-valued Parseval, for each sign of time, and the boxed residual estimate give

$$
\int_{\mathbb R}\|D_s(\omega\pm i\gamma-L_s)^{-1}o\|_{\rm tr}^2d\omega
 \leq\frac{18\pi S_s}{n\gamma}
       \left(a+\frac b{2\gamma}\right).
$$

The broadened density is -Im<o,R o>_tr/pi. Cauchy-Schwarz in frequency, with the
TV factor 1/(2pi), proves TV(p_H,p_s)<=X_s, where X_s is X_ell with S_s replacing
sum J_i^2/ell. Alternatively, R-R_s=R D_s R_s and
integral ||R^dagger o||_tr^2 d omega=pi/gamma give TV<=sqrt(X_s/2).

Finally TV is convex under mixing, every bond is cut in exactly one of the ell
shifts, and Jensen gives mean_s sqrt(X_s)<=sqrt(mean_s X_s). Thus mean_s X_s=X_ell,
proving both bounds. All frequencies and spectral tails were integrated; there is
no change to a central-window-only task. This uses the residual-square mechanism
already encountered in Note 16, now with a physical cut and collective norm bound.

### A sufficient region size

For an allocated spatial error epsilon_loc, it suffices to choose

$$
\ell\geq\frac{9J_*^2}{\gamma^2\epsilon_{\rm loc}}
              \left(a+\frac b{2\gamma}\right).
$$

With fixed LR constants and v=O(J_*), this is
O(epsilon_loc^-1[(J_*/gamma)^2+(J_*/gamma)^3]). It is a conservative sufficient
size, not a necessary correlation length or a practical hardware forecast. It can
be very large. If it exceeds n, use the full-chain construction instead. Better
physical/symmetry/recursion estimates can supersede this worst-case choice.
For uniform offsets, every block and the full isotropic chain have the same exact
single line; no window-size bound or quantum computation is needed for that limit.

## 5. Checks that the law is not silently simplified

For alternating +/-d offsets, the averaged UNBROADENED fourth moment is

$$
\bar m_4=d^4+\frac{2d^2}{n}(1-1/\ell)\sum_iJ_i^2.
$$

Thus the mixture does introduce a calculable boundary error; it is not asserted
exact at finite ell. This moment identity is a control, not a TV lower bound on
the Cauchy-broadened law, whose fourth moment does not exist.

The earlier two-spin negative control remains binding: a mixture of local spectra
computed in the coupled system is not its collective spectrum. Here O_B is the
whole block observable, and removed inter-block correlations are paid for in the
bound. Using small blocks without that error budget is not justified.

## 6. What this does for quantum and classical computation

Both algorithms can sample the same block mixture. Conditional on a chosen block,
Note 15's observable-state/geometric-clock algorithm uses at most 2ell system
qubits, plus clock and simulation ancillas, rather than 2n. It needs evolution time
T=O(log(1/epsilon_alg)/gamma); localization does not remove the linewidth time.
Block coefficients, controlled evolution, precision, state/clock preparation,
binning and all M repeated shots count. Local-Hamiltonian simulation methods [5]
are available; locality-based simulation is not our invention.

A sufficient block normalization is alpha_B<=ell Delta_*+3(ell-1)J_*/2.
The direct block-query budget is ~O(1+alpha_B/gamma), with all SELECT/PREPARE
costs separate. In particular, the region is chosen classically before those
circuits are built; no QRAM containing a superposition of all chain windows is
assumed. For arbitrary explicit coefficients, reading their input is O(n), and
extracting the selected block is not free. The uniform model needs only n,J,d.

A completely explicit CLASSICAL upper bound diagonalizes each needed block,
constructs positive transition weights, and reuses them. A dense k-spin block
costs O(8^k) arithmetic and up to O(4^k) line storage. Across the shifted partitions
there are at most n+ell-1 distinct intervals when ell<=n. Hence one conservative
preprocessing bound is O((n+ell)8^ell), followed by inexpensive categorical/Cauchy
sampling. Precision and conditioning still count. Dense diagonalization is an
upper bound, not a lower bound against restricted-state, tensor or direct methods
[6,7]. Classical preprocessing is reusable over all requested draws.

For the uniform alternating chain and even ell, all complete ell-site windows
are unitarily equivalent by translation or reflection. Only end blocks need extra
templates. At most O(ell) distinct responses suffice. One may instead use just
the complete-block template with additional TV at most 2(ell-1)/n, the upper bound
on the mixture's end-block weight. That extra simplification is optional and its
error must be allocated; the main theorem already includes exact end blocks.

**Consequence:** at fixed J_*, Delta_*, gamma>0 and accuracy, this family has a
classical sampler with polynomial dependence on total n (after coefficient access),
and a local quantum sampler with n-independent system-register size. An exponential
advantage based only on growing total chain length is therefore not supported in
this regime. This is not efficient classical scaling in inverse linewidth or in
the necessary region size, nor a lower bound on any quantum method.

The remaining possible advantage concerns the cost of response-relevant correlations
INSIDE that region, at the same linewidth and precision. The sufficient ell above
must not be presented as the actual minimum size needed by either side. Classical
tensor compression or effective models may be much better. Physical relaxation
that suppresses those correlations is not excluded merely to favor quantum dynamics.

## 7. Next bounded decision

Use this localization to compare one nontrivial local-block regime of the same
alternating-offset family, with d/J of order one and variable gamma/J. The exact
d=0 and commuting/secular limits remain controls. Determine what the response
actually requires from a classical operator/tensor or recursion representation
on the linewidth time scale, rather than inflating total n or merely using this
loose sufficient window size as evidence of hardness.

Compare the local quantum evolution budget with classical acquisition and reuse
for M requested samples. A failed tensor truncation is not an all-classical lower
bound. A useful next finding could be a sharper classical reduction OR a specific
response-relevant obstruction to the strongest identified compression. Do not
start another generic spectral transformation, locality framework, molecule search
or third spin-off. The broader dynamical-sampling mechanisms remain open.

## 8. Executed evidence and primary sources

The new NumPy script was run twice in its final form with identical JSON under
one BLAS thread; -O/-OO refusal and six invalid-input controls were checked.
Four fixed chains (2,4,6 sites with alternating offsets, and a 5-site nonuniform
control with a negative bond) supply 33 shifted partitions, 99 exact block-mixture
bin comparisons, 90 residual-orthogonality checks, 66 first-order cancellations,
66 second-resolvent identities, 99 boundary-envelope checks and 42 binned-bound
diagnostics. Ten fourth-moment checks, three uniform-field controls and local-
spectrum/carrier mistakes are included. Not every displayed bound is nontrivial.

These are complex128 diagnostics at tolerance 4e-9, not interval certificates,
empirical spectra, thermodynamic simulations, quantum circuits or timings.
The general TV result follows from the proof and the cited locality theorem,
not finite matrices or quadrature. No previous scientific suite was rerun.
No upstream implementation or experimental data was imported. Runtime Git access
failed on DNS; repository reads/writes used the connector.

Checker SHA256: `b896e7b4417e81855afc9a373cf7a315cc03cdff2ad16669820495a5e3a046e7`.
Report SHA256: `e051a0c6f6ac7147e50404e4c7bd8c34899dff6d1bad24082ae0516dbd38bdf9`.

Sources checked 29 September 2026. This is not an exhaustive priority audit.
The mathematical specialization is derived here; no source independently validates
our proof or establishes publication novelty for the exact mixture/TV composition.

[1] Sels et al., Quantum approximate Bayesian computation for NMR model inference,
Nature Machine Intelligence 2, 396-402 (2020). Primary model/application abstract
rechecked; model scope inherited from Notes 14-15. https://arxiv.org/abs/1910.14221

[2] Sels and Demler, Quantum generative model for sampling many-body spectral
functions, PRB 103, 014301 (2021). Primary abstract rechecked; direct spectral
sampling precedent, not a new algorithm here. https://arxiv.org/abs/1910.14213

[3] Barthel and Kliesch, Quasi-locality and efficient simulation of Markovian
quantum dynamics, PRL 108, 230504 (2012), arXiv:1111.4210v2. Theorem 1, definitions
of norm/range/overlap, and Theorem 2 were read; PDF page 3 was visually checked.
Use here is its time-dependent HAMILTONIAN special case, not a physical Lindblad
model or its local-observable theorem copied onto an extensive observable.
https://arxiv.org/abs/1111.4210

[4] Nachtergaele and Sims, Lieb-Robinson Bounds in Quantum Many-Body Physics,
Contemporary Mathematics 529, 141-176 (2010), arXiv:1004.2086. Overview and PDF
text inspected. Screenshot attempt failed; no figure/table data used.
https://arxiv.org/abs/1004.2086

[5] Haah, Hastings, Kothari and Low, Quantum algorithm for simulating real time
evolution of lattice Hamiltonians, arXiv:1801.03922; SIAM J. Comput.,
doi:10.1137/18M1231511. Primary algorithm abstract inspected; its general simulation
lower bound is not transferred to this restricted spectral task.
https://arxiv.org/abs/1801.03922

[6] Savostyanov et al., Exact NMR simulation of protein-size spin systems using
tensor train formalism, PRB 90, 085139 (2014). Primary abstract on topology and
classical compressed response inspected, not a native rerun. https://arxiv.org/abs/1402.4516

[7] Karabanov et al., On the accuracy of the state space restriction approximation
for spin dynamics simulations, J. Chem. Phys. 135, 084106 (2011). Primary abstract
rechecked; its relaxation assumptions are not equated with one common linewidth.
https://arxiv.org/abs/1104.3866

Only the parent repository may be modified. All prior research, source/results,
licenses and third-party notices remain intact. Both spin-offs remain independent;
no new repository, outside contact, paid/unattended work, manuscript, release or merge.
