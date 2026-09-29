# Emission memory 26: simultaneous excitations, not accumulated photon count

29 September 2026. Baseline: `7faa7b9935e5ec445e975b3cf1d695ae54521066`.
Branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Result and decision.** A coherent, excitation-truncated classical trajectory
model has a bound on the COMPLETE prescribed photon record, not only the averaged
state. The bound identifies a controlled low-occupation regime without eliminating
coherences or weakening the Ising interactions. With at most one excitation, each
emission is a genuine renewal; on a uniform open chain its no-count dynamics has
only three amplitudes. This is an exact reduction of the truncated model, not an
assumed global blockade in the original model. At comparable drive and decay a
fixed four-site check shows that this renewal approximation changes the actual
record appreciably. It does not establish many-body hardness or quantum advantage.

This continues [Note 25](RECORD_INSTRUMENT_25.md). The parent objective is useful
quantum sampling, not another classical spin-off. The point is to identify the
conditional information that quantum propagation would actually need to improve.
Existing projection/residual, quantum-jump, and renewal methods are attributed;
priority for this particular moment/record specialization is not established.

## 1. The model, output, and proposed classical memory

Use n emitters, the ground product initial state |0>=|g>^n, uniform real drive
Omega, uniform local decay kappa>0, and the SAME diagonal Ising Hamiltonian:

$$
H=\frac\Omega2\sum_i(S_i^++S_i^-)+H_z,\qquad
H_z=\sum_{\langle ij\rangle}V_{ij}S_i^zS_j^z,\qquad
J_i=\sqrt\kappa S_i^-.
$$

S_i^+=|e><g|, S_i^z=(|e><e|-|g><g|)/2. This convention agrees with Note 25.
The main graph is an open chain. The error argument allows any diagonal H_z;
bounded degree and bounded coefficients enter the cost, not the occupation bound.
Uniform rates, ground initialization and the absence of incoherent pumping are
assumptions. No stationary-state preparation, strong dephasing, unknown quantum
state, or changed detector is supplied. The application is finite-time emission
statistics of the established dissipative Ising family [1]. It is not a claimed
new experimental platform or a quantum-computing demonstration molecule.

Let N_e=sum_i |e><e|_i be instantaneous excitation number and P_q=1_{N_e<=q}.
The comparison keeps ALL coherent amplitudes in this subspace:

$$
H_q=P_qHP_q,\qquad J_{i,q}=P_qJ_iP_q,\qquad
D_q=\dim P_q=\sum_{r=0}^q\binom nr.
$$

This is a legitimate positive quantum-jump model executed CLASSICALLY with D_q
amplitudes. It is not a population-rate equation, a product-state projection, or a
projection measurement repeatedly imposed on the target. Its error is proved below.
Every jump and all subsequent re-excitation remain; q does NOT cap the cumulative
photon count. Time binning, site labels and saturated output labels are the same
as Note 25. No histories are discarded or renormalized away.

For M target records, distinguish approximation to each record law from statistical
uncertainty in M draws. The cache warning in Note 24 still applies. Bounded dark/
bright or count-threshold events inherit a TV bound; unbounded count moments need
additional tail accounting. Detector inefficiency can be applied as the same
classical thinning, before saturation; it does not undo the underlying jump.

## 2. A factorial-moment envelope, without a population approximation

For either the full state or the truncated state, averaged over its records, put

$$
M_r(t)=\operatorname{Tr}\left[\binom{N_e}{r}\rho(t)\right],\qquad M_0=1.
$$

All ground-start moments M_r(0), r>=1, vanish. For 1<=r<=n,

$$
\boxed{M_r(t)\leq\binom nr
\left[\frac{|\Omega|}{\kappa}(1-e^{-\kappa t/2})\right]^{2r}.}
$$

This is an upper bound, not a binomial-distribution assertion or independent-spin
assumption. It can be trivial when the bracket exceeds one. It controls ordinary
averaged moments, NOT every normalized state conditioned on a rare history.
No interaction strength, spectral gap, or mixing assumption enters the bound.

### Proof

Let p_m=Tr(1_{N_e=m} rho). The sum T^+=sum S_i^+ has block norm

$$
\|1_{N_e=m+1}T^+1_{N_e=m}\|=\sqrt{(m+1)(n-m)}.
$$

This follows from the usual total-spin ladder decomposition: at fixed magnetic
quantum number the maximum is the symmetric spin-n/2 representation, which is
present. Removing transitions above q only decreases the set of contributing
blocks. Positivity gives ||rho_{m,m+1}||_1<=sqrt(p_m p_{m+1}).

Because H_z commutes with N_e and
\(\binom{m+1}{r}-\binom mr=\binom m{r-1}\), the absolute drive contribution is at
most

$$
|\Omega|\sum_m\binom m{r-1}\sqrt{(m+1)(n-m)p_mp_{m+1}}.
$$

Cauchy-Schwarz bounds this by
|Omega| sqrt(r(n-r+1) M_r M_{r-1}): the first squared sum is r M_r because
(m+1) binom(m,r-1)=r binom(m+1,r); the second is at most (n-r+1) M_{r-1}.
The local lowering dissipators give the exact identity

$$
\sum_i\mathcal D_{J_i}^{\dagger}\binom{N_e}{r}
=-\kappa r\binom{N_e}{r}.
$$

It holds in the truncated subspace too, since lowering never leaves it. Therefore

$$
\dot M_r\leq |\Omega|\sqrt{r(n-r+1)M_rM_{r-1}}-\kappa r M_r.
$$

For y_r=sqrt(M_r), division where y_r>0 gives the linear comparison
\(\dot y_r\leq |\Omega|\sqrt{r(n-r+1)}y_{r-1}/2-\kappa r y_r/2\).
At a zero use a regularized square root and take its limit. Induction from y_0=1
compares with
\(\sqrt{\binom nr}(|\Omega|/\kappa)^r(1-e^{-\kappa t/2})^r\), which satisfies the
corresponding equality. Squaring proves the result. This proof retains arbitrary
coherences and correlations within the model.

## 3. Promote the occupation control to the entire monitored record

Let P_rec and P_rec^(q) be the full and truncated record laws. For q<n define

$$
f_q=\frac{|\Omega|}{2}\sqrt{(q+1)(n-q)},\qquad
p_q^{(q)}(t)=\operatorname{Tr}[1_{N_e=q}\rho_q(t)].
$$

For the ground initial state, a stronger record-plus-final-state bound implies

$$
\boxed{d_{\rm TV}(P_{\rm rec},P_{\rm rec}^{(q)})
\leq \min\left\{1, f_q\int_0^T\sqrt{p_q^{(q)}(t)}\,dt\right\}.}
$$

The same RHS bounds the trace distance of the block-diagonal classical-record/
quantum-final-state outputs after embedding the truncated state. This is a FIXED-
INITIAL-STATE guarantee, not a uniform diamond-norm assertion for arbitrary input.
The integral is an a posteriori option, not freely given data: obtaining and
certifying it costs a truncated evolution and time-integration error control.

### Proof, with no normalization by rare-history probabilities

Extend H_q to H'=P_qHP_q+Q_qHQ_q on the original Hilbert space, and keep the
ORIGINAL jump operators and their detector labels. Ground-start dynamics stays in
P_q under H' and all jumps; it is exactly the proposed truncated model. The only
generator difference is the Hamiltonian boundary F+F^dagger, where
F=1_{N_e=q+1}H P_q and ||F||=f_q. Also F^dagger F<=f_q^2 1_{N_e=q}.

Apply Duhamel's formula to the number-resolved instrument of Note 25, retaining all
past-record registers. Completely positive trace-preserving propagation contracts
the trace norm of Hermitian differences. For each unnormalized positive branch
sigma_a supported in P_q,

$$
\tfrac12\|[F+F^\dagger,\sigma_a]\|_1
=\|F\sigma_a\|_1
\leq\sqrt{\operatorname{Tr}(F^\dagger F\sigma_a)\operatorname{Tr}\sigma_a}.
$$

Sum branches and use Cauchy-Schwarz, sum Tr sigma_a=1. The result is at most
sqrt(Tr(F^dagger F rho_q))<=f_q sqrt(p_q^(q)). Integrate over time. Detector-bin
boundary operations, saturation and common record postprocessing are contractions.
The argument works for any prescribed finite binning; it neither confuses fixed
endpoint timestamps with continuous times nor erases the detector before proving
the bound. No worst-case rare-branch normalization is needed.

The Duhamel residual/trace-contraction mechanism is prior work; [3, Lemma 1]
provides a close general Lindblad-truncation predecessor. The present application
uses the count-lifted instrument and this excitation-sector residual. It is not a
new general truncation theorem, and is not inferred from closeness of the final
unlabelled density operators.

### An a priori, input-computable sufficient bound

In the truncated space p_q^(q)=M_q. Substitution of Section 2 gives

$$
\epsilon_q\leq\min\left\{1,
\frac{|\Omega|}{2}\sqrt{(q+1)(n-q)\binom nq}
\left(\frac{|\Omega|}{\kappa}\right)^q
\int_0^T(1-e^{-\kappa t/2})^qdt\right\}.
$$

Replacing the integral by T yields a simpler conservative expression. Let
\(\lambda=n\Omega^2/\kappa^2\), a COLLECTIVE drive-to-decay parameter, not a measured
steady-state occupation. With binom(n,q)<=n^q/q!,

$$
\boxed{\epsilon_q\leq\min\left\{1,
\frac{\kappa T}{2}\sqrt{\frac{(q+1)\lambda^{q+1}}{q!}}\right\}.}
$$

For q=n the error is exactly zero; use that fact rather than this looser envelope.
The q=0 model is the all-dark ground record and the boundary argument also applies.
For Omega=0 the full record is exactly dark. Negative Omega is covered by |Omega|.
A warm/pumped bath or a different initial state requires another moment argument.

For fixed lambda, kappa T and error, the factorial lets one choose a finite q
independent of n. D_q=O(n^q) then supplies polynomial dependence on n. This is NOT
a fixed-local-drive thermodynamic theorem: holding lambda fixed requires
|Omega|/kappa=sqrt(lambda/n). At fixed nonzero Omega/kappa, lambda grows with n.
The bound cannot be presented as a certificate that every strongly monitored,
fixed-density chain is easy.

As an analytical example only, lambda=0.01 and kappa T=100 give sufficient errors
0.707107, 0.0612373, 0.00408249 and 0.000228218 for q=1,2,3,4. No large system at
those settings was simulated. They show how a finite observation period may
contain repeated emission while a small instantaneous-excitation sector suffices;
they do not set a community acceptance threshold or claim a runtime speedup.

## 4. Cost of the adequate classical memory

The classical sampler stores D_q coherent amplitudes, not only populations, and
can apply sparse H_q and J_i,q actions in O(n D_q) arithmetic with local indexing.
Jump labels and waiting-time sampling use the SAME instrument; no arbitrary
unravelling or dephasing is chosen to ease simulation. Exact trajectory simulation
and renewal machinery are prior work [2,4].

A conservative complete discrete implementation is available without trusting an
ODE tolerance as a record guarantee. Subtract H_z's scalar ground energy. On a
maximum-degree-z graph with |V_ij|<=V_*, one has, for q>=1,

$$
\|H_q-H_z(0)I\|\leq W_q:=|\Omega|\sqrt{nq}+qzV_*/2.
$$

The raising/lowering block-tridiagonal norm is bounded by twice its largest
neighbor-block norm, giving the first term. A q-excitation configuration changes
at most qz Ising bonds relative to the ground configuration, each by |V|/2.
The lifted truncated damping generator has diamond norm <=2 kappa q because
sum J_i,q^dagger J_i,q=kappa N_e<=kappa q, including its counter shifts.

Split exact exp(-ihH_q) and the exact monitored amplitude-damping layer. The
same contractive two-factor calculation as Note 25 gives a whole-record error
at most 2 W_q kappa q T h. Let h=Delta/r and choose
r>=max(1,ceil(2 W_q kappa q T Delta/epsilon_num)). This does not change detector bins.
The local damping layer preserves P_q and includes repeated emissions across steps.
The whole H_q rotation is used: individually rotating and projecting every spin
would be a DIFFERENT, unaccounted approximation.

One explicit classical upper bound diagonalizes the D_q matrix once to prepare
its unitary step, costing O(D_q^3), then applies each dense unitary and n sparse
local damping updates. For L detector bins and M fresh records, a sufficient
arithmetic budget is

$$
O\big(D_q^3+M Lr(D_q^2+nD_q)\big),
$$

plus coefficients, finite precision, random-bit sampling, counters and output.
Preprocessing can be reused. Sparse event-driven methods may be much better;
this is an existence upper bound, not a prescribed implementation or optimality
claim. Truncation, numerical-instrument and output errors add. No stochastic
postselection or rare-state preparation has been hidden in the classical route.
At fixed q the whole construction is polynomial in n, T and inverse error under
the stated bounded-input assumptions. The direct quantum construction of Note 25
remains another option with n system qubits and its own gate/error budget. Neither
side receives free integration, and unlike primitive counts are not ratios of time.

## 5. The exact renewal limit is stronger than independent populations

Within q=1, write |i> for the single excitation at site i. Every jump has the form

$$
J_{i,1}=\sqrt\kappa |0\rangle\langle i|.
$$

It resets the WHOLE conditional state to |0>, for every possible pre-jump state
with nonzero detection probability. Thus successive waiting times and site marks
have an exact marked-renewal description; waiting time and site in the same cycle
can be correlated. The system can emit arbitrarily many times through repeated
re-excitation, even though it never has two simultaneous excitations in this
approximation. No accumulated photon-count cutoff is imposed.

For a uniform open chain n>=3, no-count evolution from the vacuum needs only
|0>, the normalized sum |E> over the two ends, and the normalized sum |B> over
the n-2 interior sites. Subtracting the ground energy,

$$
H_{\rm eff}^{(1)}\big|_{\{0,E,B\}}=
\begin{pmatrix}
0&\Omega\sqrt2/2&\Omega\sqrt{n-2}/2\\
\Omega\sqrt2/2&-V/2-i\kappa/2&0\\
\Omega\sqrt{n-2}/2&0&-V-i\kappa/2
\end{pmatrix}.
$$

For time t since the last photon, let a(t)=exp(-it H_eff^(1)) (1,0,0)^T.
The survival probability is ||a(t)||^2. Each endpoint's waiting-time density is
kappa |a_E(t)|^2/2; each interior site's is kappa |a_B(t)|^2/(n-2).
This specifies times and detector labels, not only total activity. The terminal
no-count survival is retained. The first cycle also starts in |0>.

The proof is degree-class symmetry: the energy of a single excitation at a vertex
of degree z_i shifts by -Vz_i/2, and the uniform drive couples |0> only to the
bright sum within each equal-degree class. On a general uniform bounded-degree
graph, at most z+2 amplitudes suffice for this q=1 ground-start evolution. With
nonuniform coefficients the q=1 space has size n+1 and is still classically small.
Neither version establishes that q=1 is accurate for the original interacting
model; Section 3 or another validated estimate is required for that claim.

Superpositions such as |B> are entangled across sites. Their presence does not
prevent this simple renewal calculation. A long record, a delocalized excitation,
or non-exponential waiting times is therefore not a computational advantage test.
This is a classical comparator, not a new restricted application selected to make
quantum simulation easy or hard.

## 6. Why a general photon does not globally reset the system

For the q-excitation space the local jump has matrix rank

$$
\operatorname{rank}(J_{i,q})=\sum_{r=0}^{q-1}\binom{n-1}{r}.
$$

For q>=2, the other sites can retain an excitation and its coherence after that
site emits. Rank alone does not prove that every such state is dynamically
reachable, much less that its information is necessary for the chosen output.
The rank-one reset criterion and failure of local resets to reset coupled global
systems are established in [2, section on renewal processes].

There is also a reachable check without choosing arbitrary entangled input states.
Evolve from |0> with no counts until time t, then detect the first photon at i.
Small-time expansion shows, after normalization,

$$
|\psi_{i,\mathrm{post}}(t)\rangle
=|0\rangle-\frac{i\Omega t}{2}\sum_{j\ne i}|j\rangle+O(t^2),
$$

up to a global phase. This holds in the full model and q>=2. The other sites'
immediate future intensities depend on the waiting time even though the clicked
site has reset. It is a conditional-state identity, not a probability assigned
to a zero-width time point or a record-TV lower bound for every renewal model.
Independent emitters ALSO retain the ages/states of the unclicked sites; they
have an economical local-renewal sampler. Hence this observation alone is not a
many-body quantum advantage.

## 7. What the actual fixed-size calculation shows

One four-site chain, initial gggg, V=kappa=1 and three bins of width 2 was used.
The checked output coarsens the original site counts to global dark/bright labels.
Its TV is a lower bound on the corresponding fine-record TV, not an upper bound
on what detector detail can be discarded. The theorem itself covers the original
site-resolved count record and the final state.

| Drive Omega | q | Amplitudes D_q | Coarse-record TV | Analytic full-record upper bound |
|---|---:|---:|---:|---:|
| 0.1 | 1 | 5 | 0.000685889 | 0.146970 |
| 0.1 | 2 | 11 | 0.000006315 | 0.018000 |
| 0.1 | 3 | 15 | <0.000000010 | 0.001200 |
| 1 | 1 | 5 | 0.496582 | 1 |
| 1 | 2 | 11 | 0.100045 | 1 |
| 1 | 3 | 15 | 0.017015 | 1 |

All q=4 comparisons are exact. The weak-drive full model emits at least once
with probability about 0.07105, so a silent all-dark replacement would not meet a
5% record-TV target even though a controlled small-excitation model can. These are
numerical diagnostics, not experimentally prescribed tolerances. The q=1 coherent
approximation still produces photons in all three bins with probability 0.23806;
its error is NOT caused by an imposed one-photon total cap.

At Omega=V=kappa=1 the small-q approximations visibly lose temporal information.
Four spins remain easy to calculate classically, and q=3 already improves the
coarse statistic substantially. This is not evidence of growing-system hardness,
minimum memory for all samplers, or an absence of a different compact model.
The analytic guarantee is sufficient and conservative; its failure is not proof
of approximation failure. The report separates actual numerical differences.

## 8. Consequence for the quantum opportunity and next bounded decision

The new exact distinction is simultaneous excitation/coherence versus accumulated
emission count. The quantum device retains the former between output events;
when that information fits in a fixed-q space, an explicit polynomial classical
competitor retains it too, without discarding coherence. The dilute collective-
drive regime is therefore not justified as a quantum-advantage target by spin
count or temporal complexity alone. This does not close the coherent, finite-
density regime or the broader direct-sampling direction.

The next comparison should NOT merely enlarge q or enumerate more four-site laws.
There is a directly relevant stronger classical precedent: Rose et al. [5] find
that, in a parameter/time regime of a related finite one-dimensional dissipative
Ising model, metastable states form mixtures of two phases and their slow dynamics
is effectively classical. That does not automatically reproduce this fixed-start,
site-resolved finite-bin instrument. It is nevertheless a serious comparator:
intermittent bright/dark records are not automatically evidence of expensive
conditional quantum memory. Its spectral data, initialization and regime of
validity must be obtained, not supplied free.

**Next task:** compare the coherent, non-dilute record task with an explicitly
stated two-phase/hidden-state or cluster description. Identify the temporal/site
information it preserves and loses, keeping the original detector law or explicitly
specifying a separately useful coarsening. Derive one record-sensitive criterion
for its adequacy using the model's existing physical timescales. Do not infer
instrument accuracy only from a slow unlabelled Liouvillian or introduce arbitrary
observation precision to manufacture difficulty. If no output-relevant many-body
obstacle remains after those reductions, broaden mechanisms rather than adding
another approximation theorem. No new repository, manuscript or third spin-off.

## 9. Checks and sources

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/emission_memory_v1/verify.py
```

Checker SHA256: `bd8e4ab2cbcd10ec4b4b8601478edc7ef77b6b8c09945e725f59311893da768c`.
Report SHA256: `5220059b73583e542f78520d2d332a217a0e92557c6dba914f2d9757d5d69584`.

The new checker ran twice with identical JSON, refusing -O/-OO and six invalid
inputs. Only a fixed four-site chain was fully propagated, at two explicitly
chosen drive strengths. It checks eight cutoff record/final-state comparisons,
160 moment envelopes and 160 drift inequalities, 28 dissipative factorial identities,
eight raising-boundary norms and eight jump ranks. The q=1 reduced spaces at n=4,7,10
check degree-class invariance and site-resolved renewal formulas; the latter are
NOT full seven-/ten-site simulations. One reachable post-first-click calculation
checks the differing neighbor intensities. All calculations use complex128 and
matrix exponentials; they are not interval certificates. General claims follow
from the written proof, not fitted scaling or the numerical check.

No quantum shots, native trajectory/tensor package, experimental data, large-system
run, timing benchmark, or upstream code import occurred. No historical scientific
verifier was rerun. Coefficient, integration and random-output numerical errors are
separate from the analytic truncation theorem. Literature search was focused, not
an exhaustive novelty audit. HTML/abstracts were inspected; no PDF was analyzed,
no figure digitized, and no experimental measurement reproduced in this round.

[1] C. Ates et al., *Dynamical phases and intermittency of the dissipative quantum
Ising model*, PRA 85, 043620 (2012). Existing model and photon-activity motivation;
primary abstract rechecked; no phase boundary reproduced.
https://arxiv.org/abs/1112.4273

[2] G. T. Landi et al., *Current Fluctuations in Open Quantum Systems: Bridging the
Gap Between Quantum Continuous Measurements and Full Counting Statistics*, PRX
Quantum 5, 020201 (2024). Primary publisher/renewal-section search text inspected,
including the global reset criterion; full HTML retrieval failed. Not a complete
independent audit of its results.
https://doi.org/10.1103/PRXQuantum.5.020201
https://arxiv.org/abs/2303.04270

[3] P.-L. Etienney, R. Robin and P. Rouchon, *A posteriori error estimates for the
Lindblad master equation*, Quantum 10, 2031 (2026), arXiv:2501.09607v6. HTML Section 2,
Lemma 1, and stated scope inspected. The residual/contraction method is prior work;
its unlabelled-state statement is not silently substituted for a record theorem.
https://arxiv.org/html/2501.09607v6
https://quantum-journal.org/papers/q-2026-03-16-2031/

[4] J. Dalibard, Y. Castin and K. Molmer, *Wave-function approach to dissipative
processes in quantum optics*, PRL 68, 580 (1992). Classical conditional-state
baseline retained from Note 25; no upstream implementation was run.
https://arxiv.org/abs/0805.4002

[5] D. C. Rose et al., *Metastability in an open quantum Ising model*, PRE 94,
052132 (2016). Primary abstract/publisher summary inspected, not full detector-
record validation, numerical regime reproduction or a proved universal two-state
reduction for the present model.
https://arxiv.org/abs/1607.06780
https://doi.org/10.1103/PhysRevE.94.052132

Only Quantum-Assisted-Algorithm-Discovery may be modified. Prior scientific notes,
code, reports, licenses and third-party rights are unchanged. Other mechanisms
and both independent spin-offs keep their existing boundaries. No external contact,
paid/unattended work, release, merge or repository administration is authorized.
