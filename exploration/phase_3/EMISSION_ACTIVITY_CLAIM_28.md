# Emission activity 28: a concrete conditional quantum claim

29 September 2026. Baseline: `0fcf4d7c979003bc2d2508dfb3cde1c4cf4657af`.
Branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

## Decision and claim sheet

**Conditional lead, not an established useful advantage:** estimate a bounded
correlation between photon activities in two successive observation windows.
An exact two-flag encoding makes this a final-state probability problem. Standard
high-accuracy Lindblad simulation and amplitude estimation then give inverse-linear,
rather than inverse-square, sampling dependence on additive accuracy. This does
NOT outperform a supplied adequate small classical tilted generator. The remaining
decisive comparison is the cost of obtaining and validating that classical generator
or evaluating the statistic by another method. No new repository is needed.

This explicitly specializes the earlier full-record output to ONE scalar; it does
not claim to reproduce all photon histories or their joint law. The scalar is a
bounded transform of ordinary two-window activity correlations, independently
motivated by emission intermittency [1,2]. This particular transform is our choice,
not an experimentally established standard metric or proof of a dynamical phase.

| Item | Specification |
|---|---|
| Model | Driven Ising emitters, local Markov decay, supplied parameters, product ground initial state |
| Structural slice | Periodic nearest-neighbor ring, n>=3; the literature's V/kappa=250, Omega/kappa=50 finite-size slice is an application anchor, not a hardness claim |
| Observation | Total emitted counts K1,K2 in successive intervals of length Delta; T=2 Delta, including the initial transient |
| Output | G=Cov(exp(-s K1),exp(-s K2)), s=u/(n kappa Delta), fixed u=1 unless stated otherwise |
| Quality | Additive epsilon with failure <=beta; epsilon is an input justified by a scientifically material prediction difference, not chosen to force a speedup |
| Quantum operation | A two-flag Markovian encoding, high-accuracy channel simulation with retained purification, and amplitude estimation of three flag probabilities |
| Serious classical alternatives | Direct tilted propagation; metastable tilted generator with transient/within-phase corrections AND model acquisition; coherent trajectories, tensors, clusters, low-excitation methods |
| Decisive missing condition | In the same (n,Delta,epsilon) regime, those adequate classical acquisitions must cost more than the fully charged coherent estimator |

The parameter slice and periodic boundary are taken from the family in Rose et al.
[1], rather than silently treating their periodic metastability result as a theorem
about the earlier open-chain, equal-scale control. Their finite n=7 study does not
establish metastability or difficulty for every growing ring. Delta remains a
specified physical observation interval; its relation to internal relaxation and
switching times must be assessed, not assumed or supplied by a free gap oracle.
No stationary preparation, arbitrary ground state, experimental archive or
laboratory reversal is assumed. Direct record sampling from Note 25 remains valid.

## 1. Why this output is physically meaningful and statistically bounded

Keep H=Omega sum_i S_i^x+V sum_edges S_i^z S_j^z,
J_i=sqrt(kappa)|g><e|_i, and rho0=|g...g><g...g|. Let

$$
Y_b=e^{-sK_b},\quad Z_1=\mathbb E Y_1,\quad Z_2=\mathbb E Y_2,
\quad Z_{12}=\mathbb E(Y_1Y_2),\quad G=Z_{12}-Z_1Z_2.
$$

Y is a smooth quietness score: it equals one for an empty window and decreases
with its activity. G measures a particular temporal dependence. It is not a full
count distribution, a waiting-time law, a switching rate, a stationary large-
deviation function, or a proof of quantum correlations. Independent coherent
emitters can themselves have within-emitter temporal correlations.

The normalization avoids deliberately asking for an exponentially small positive
Laplace transform. Since the total photon intensity is <=n kappa at all times,
E K_b<=n kappa Delta. Jensen's inequality gives, without a stationary assumption,

$$
Z_1,Z_2\geq e^{-u},\qquad Z_{12}\geq e^{-2u},\qquad |G|\leq1/4.
$$

This bounds the three probabilities, NOT G away from zero. A small G may be
scientifically negligible at the chosen tolerance. It is not a relative-error
claim for rare features. A long-lived two-phase mixture with distinct intensive
activities can retain a finite difference in these scores; conversely ordinary
self-averaging can make G small. Neither behavior is assumed for the target.
For comparing two predicted values separated by D, epsilon<D/4 is a sufficient
numerical discrimination target; the scientific importance of D and model/input
uncertainties must be supplied separately. No numerical epsilon is mandated here.

## 2. Exactly retain the necessary counting information with two flags

Let r=e^{-s}. For the flag active during a window, initially |0>, replace each
J_i by three computational jump operators on emitter plus flag:

$$
\widetilde J_{i,a}=\sqrt r J_i\otimes|0\rangle\langle0|,\quad
\widetilde J_{i,b}=\sqrt{1-r}J_i\otimes|1\rangle\langle0|,\quad
\widetilde J_{i,c}=J_i\otimes|1\rangle\langle1|.
$$

Use H tensor I and identity on the other flag. A physical emission either leaves
a zero flag at zero, or marks it. Once marked it remains marked; later emissions
still update the emitter. These three operators satisfy
sum_a,b,c Jtilde^dagger Jtilde=J_i^dagger J_i tensor I. For flag-diagonal states,
the sum of flag blocks evolves under the ORIGINAL system Lindbladian.

Write J(rho)=sum_i J_i rho J_i^dagger and L for that Lindbladian. The unmarked
block obeys the exact trace-decreasing tilted evolution

$$
\dot\rho_{0}=\mathcal L_s(\rho_0),\qquad
\mathcal L_s=\mathcal L+(r-1)\mathcal J.
$$

Equivalently, a history with K emissions leaves the flag unmarked with probability
r^K. This is standard counting-field/thinning logic [2,3], explicitly embedded
in a trace-preserving quantum evolution. No postselection is performed.

Activate flag one in [0,Delta] and flag two in [Delta,2Delta], without resetting
the emitters or the first flag. Then exactly

$$
\Pr(F_1=0)=Z_1,\quad\Pr(F_2=0)=Z_2,\quad
\Pr(F_1=F_2=0)=Z_{12}.
$$

The equivalent direct CLASSICAL computation is

$$
Z_1=\operatorname{Tr}e^{\Delta\mathcal L}e^{\Delta\mathcal L_s}\rho_0,
\quad Z_2=\operatorname{Tr}e^{\Delta\mathcal L_s}e^{\Delta\mathcal L}\rho_0,
\quad Z_{12}=\operatorname{Tr}e^{2\Delta\mathcal L_s}\rho_0.
$$

The trace-preserving first factor in Z1 can be removed. These expressions retain
the nonstationary initial condition and correlation across the window boundary.
Two independent restarts would produce a different statistic. X-flipping the
flag on every marked photon records parity, not absence of marks: for two photons
and r=1/2 its unmarked probability would be 1/2 instead of 1/4.

The flags are a computational representation of the chosen statistic, not a
claim to change the physical detector or its unraveling. Their final averaged
state suffices BECAUSE this exact encoding was proved. Note 25's warning that
an arbitrary unlabelled master equation does not fix records remains valid.
Only two flag qubits encode the requested information; the simulation's coherent
workspace and environment registers are additional and are not assumed small.

## 3. Where quantum processing changes the accuracy cost

Simply sampling the flags still has ordinary Monte Carlo accuracy scaling.
Instead, implement the two augmented channels by an explicitly unitary purified
circuit A_eta, retaining its environment/work registers. Estimate the three
projector probabilities using standard amplitude estimation and A_eta's inverse
[4]. Reversal is of the COMPUTATIONAL circuit, not an inverse dissipative physical
channel and not retrospective processing of already measured laboratory records.
Ancillas needed for that inverse cannot be measured, reset or discarded mid-call.

If the simulated final-state trace distance is <=eta and the three probability
estimates have errors <=delta, clipped to [0,1], then

$$
|\widehat G-G|\leq3\eta+3\delta.
$$

Indeed each probability has bias at most eta; the product of two [0,1] numbers
is Lipschitz with the sum of their errors. Choosing eta=delta=epsilon/6 gives
an epsilon guarantee. Three failure probabilities beta/3 give total <=beta.
Amplitude estimation uses O(epsilon^-1 log(1/beta)) circuit/inverse calls, up to
algorithmic logarithms. The comparison is with generic nonzero-variance sample
averaging, not with every classical deterministic method.

**The time-step dependence must not erase this gain.** Reusing Note 25's crude
first-order splitting at eta=O(epsilon) could itself cost O(1/epsilon) per call.
Instead, known high-accuracy Lindblad algorithms have polylogarithmic dependence
on inverse channel error [5,6]. They apply here because the augmented generator
is still an explicit sum of local/Pauli operators. The gate circuit's purification
is retained and reversed; it is not an assumed free state oracle.

For a graph with m edges, one block-encoding normalization in [6]'s convention is

$$
\Gamma=\frac{n|\Omega|}{2}+\frac{m|V|}{4}+n\kappa.
$$

The Hamiltonian has n+m constant-local terms. The 3n jump operators each have
constant-size Pauli expansions, and half the sum of their squared normalizations
is n kappa. For each active flag their physical locality is at most two sites,
although the added flag connects computationally to all emitters. Routing is not
free on a geometrically constrained processor.

The higher-order channel construction [6] uses ~O(1+Gamma T) block calls and
~O(n(1+Gamma T)) additional local gates for the two segments. For explicit
coefficients, straightforward controlled term selection/preparation costs
O((n+m) polylog(precision)) per block call. This yields a conservative total

$$
C_{\rm coherent}=\widetilde O((n+m)(1+\Gamma T)),\qquad
C_Q=\widetilde O((n+m)(1+\Gamma T)/\epsilon),
$$

where logarithms include coefficient/channel/gate accuracy and failure probability.
State preparation, reflections on the retained workspace, and coherent uncomputation
are charged; a safe workspace bound is polynomial in the circuit size, NOT n+2
qubits in total. This is an upper bound using existing algorithms, not a compiled
resource estimate, optimality claim or new Lindblad/estimation theorem. Gate
connectivity, fault-tolerant overhead and a common cost unit are still required
before a practical comparison. T remains fully paid: no fast switching, burn-in
removal or fast forwarding is proved. At fixed small n, direct classical matrix
propagation can have better precision scaling than the quantum estimator.

## 4. The strongest classical response is NOT just more trajectories

Given rho0 and an adequate small tilted model, the three formulas in Section 2
are inexpensive matrix propagations, not Monte Carlo. Rose et al. [1] and
Macieszczak et al. [2, Sections V B 2-4] supply metastable phase and counting
comparators. Their construction includes transition activity, within-phase
fluctuations and initial-transient corrections when these matter. A simple
Poisson telegraph process is not silently substituted for all that theory.
Neither its parameters nor a prepared metastable state is supplied free here.

There is an immediate constraint on our normalized task:

$$
\|\mathcal L_s-\mathcal L\|_\diamond
\leq(1-e^{-s})n\kappa\leq u/\Delta.
$$

Thus long observation bins make this a small tilted perturbation. Where classical
metastability and its conditioning/error assumptions are established, that fact
supports rather than defeats its low-mode treatment. The norm estimate alone
is NOT a nonnormal perturbation theorem or an all-size metastability guarantee.
For ground initialization, the initial transient is retained or priced. One must
not select Delta arbitrarily short solely to invalidate the classical model.

The actual comparison is

$$
C_Q\quad\hbox{versus}\quad
\min\{C_{\rm direct\ tilted},\ C_{\rm phase\ acquisition+validation}
+C_{\rm small\ tilted},\ C_{\rm tensor/cluster},\ C_{\rm trajectories},\ldots\}.
$$

Trajectory averaging of the three bounded scores has a sufficient O(epsilon^-2
log(1/beta)) sample count, but variance reduction, correlation-aware estimators,
rare-event methods and direct propagation are all allowed. Small actual variance
can improve that bound. The number of amplitude-estimation calls is not comparable
to a classical trajectory count without pricing each call. Learned models and
acquired coefficients can be reused across parameter queries as justified.

## 5. The one remaining decision test

This checkpoint identifies a genuine quantum-specific PRECISION mechanism and a
specific observable, not yet a regime beating the best classical strategy.
The unresolved condition is the classical acquisition/validation cost of the same
bounded tilted response in the source-anchored Ising slice. It cannot be replaced
by a Hilbert-space dimension, a large flag-history alphabet, or failure of a weak
population approximation. The generic composition is prior work in its ingredients;
its publication novelty and practical significance are unestablished.

**Next:** test the applicability and acquisition cost of the record-aware
metastable tilted description for this G, including the ground transient and
within-phase corrections. Use the three direct tilted contractions as the
reference problem, not a full history histogram. First identify whether existing
phase/symmetry/tensor methods already produce an adequate answer; only a specified
remaining bottleneck warrants a larger numerical comparison or quantum resource
compilation. Do not develop another flag or generic estimator framework.
If an adequate cheap tilted model is available, prefer it and park this particular
quantum calibration claim. If a specific costly acquisition survives, compare its
resource dependence with the coherent estimate. No universal lower bound is needed
to investigate that conditional claim, but no advantage is asserted before it.

## 6. Verification and primary-source scope

The attached checker independently compares the exact tilted contractions with
the diagonal blocks of the two-flag Lindbladian for one three-emitter ring,
Omega=V=kappa=1, Delta=u=1. This is an algebra control, NOT the published metastable
parameter slice. It checks preservation of the physical marginal, probabilities,
local jump completeness, the no-mark limit, and correlation across the window
boundary. An exact rational control rejects a parity flag. Independent coherent
emitters and a supplied two-state classical model are positive bypass controls.
The latter uses illustrative rates, not a fitted approximation to the spin system.

The final checker ran twice with identical JSON; -O/-OO and six invalid inputs
were rejected. It uses complex128 matrix exponentials, not interval certification.
Reported decimals are rounded to twelve places. No amplitude estimation, channel
simulation circuit, quantum shots, published metastable-slice calculation, large
chain, new empirical advantage, or performance benchmark was executed. Older
scientific verifiers were not rerun. No upstream code or experimental data imported.

Primary sources inspected 29 September 2026:

[1] Rose et al., *Metastability in an open quantum Ising model*, PRE 94,052132
(2016). Model, Section III E and Fig. 7 caption read; page 5 visually inspected.
The requested Fig. 7 page screenshot failed; no graph values were digitized.
https://arxiv.org/abs/1607.06780

[2] Macieszczak et al., *Theory of classical metastability in open quantum systems*,
PR Research 3,033047 (2021), arXiv:2006.01227v2, Sections V B 1-4 and Eqs.44-61.
Parsed equations/qualifications read; requested page-18 screenshot failed. Not a
complete audit of the 90-page paper and supplement.
https://arxiv.org/abs/2006.01227

[3] Ates et al., *Dynamical phases and intermittency of the dissipative quantum
Ising model*, PRA 85,043620 (2012). Model/activity motivation and counting scope.
https://arxiv.org/abs/1112.4273

[4] Brassard et al., *Quantum Amplitude Amplification and Estimation*,
arXiv:quant-ph/0005055. Standard estimation and coherent-access assumptions;
not a claim to improve its primitives. https://arxiv.org/abs/quant-ph/0005055

[5] Cleve and Wang, *Efficient Quantum Algorithms for Simulating Lindblad
Evolution*, ICALP 2017, arXiv:1612.09512. Theorem 1, local Corollary 2 and channel
purification construction inspected. Requested theorem-page screenshot failed;
no figure-derived claim. https://arxiv.org/abs/1612.09512

[6] Li and Wang, *Simulating Markovian open quantum systems using higher-order
series expansion*, arXiv:2212.02051v2. Theorems 1/11, block-encoding normalization
and isometry implementation read in primary HTML. Newer/other implementations
may improve the quoted upper bound. https://arxiv.org/html/2212.02051v2

Quantum counting algorithms and open-system expectation estimation have broader
prior literature; this is a bounded predecessor screen, not a novelty audit.
Only Quantum-Assisted-Algorithm-Discovery is writable. Preserve all prior source,
proofs, data, rights and LICENSE. Other mechanisms remain available; no manuscript,
new repository, third spin-off, external contact, paid work, merge or release.
