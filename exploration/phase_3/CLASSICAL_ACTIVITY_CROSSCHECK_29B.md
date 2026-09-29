# Classical activity cross-check 29B: execute the strongest immediate bypass

29 September 2026. Live base: `4f0e57e2ef56e3ddb395ebecb4fec115c29d3b44`.
Intended branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Synchronization:** while this calculation was in progress, the live branch
advanced to `cbf06221c667b49b76140f241384e1e14e3cab20`, adding
`CLASSICAL_ACTIVITY_ACQUISITION_29.md`. That separate note tests Delta=1,4,16.
The present independently executed check uses Delta=1,5,20 and also re-acquires
tilted modes. Its result agrees with the live note's narrow decision, but the
files and numerical rows are NOT interchangeable. It is delivered as Note 29B
and a distinct experiment directory; it does not overwrite live Note 29 or claim
to have created that remote commit.

**Decision:** the source-matched finite example does not supply the missing
classical acquisition bottleneck for Note 28. A two-mode tilted contraction can
be acquired from the Hamiltonian and jump operators, without fitted trajectory
data, and reproduces the chosen covariance at the tested windows. Stop treating
this covariance/precision proposal as an active advantage lead without an
independently justified new regime. Preserve the quantum algorithm as a conditional
reference. This is NOT a proof of classical tractability for arbitrary n or every
emission observable, and not a timing comparison with a compiled quantum computer.
No new repository or classical spin-off is needed.

## 1. One source-matched calculation, rather than another small identity test

Use the periodic seven-site dissipative Ising instance from Rose et al. [1]:

$$
H=\Omega\sum_{i=1}^{7}S_i^x+V\sum_{i=1}^{7}S_i^zS_{i+1}^z,
\qquad J_i=\sqrt\kappa\,|g\rangle_i\langle e|,
\qquad (\Omega,V,\kappa)=(50,250,1),\quad S_8=S_1.
$$

Spin operators are Pauli matrices divided by two. In the computational order
(g,e), Sz=diag(-1/2,1/2). Start from the original all-ground state, not a supplied
stationary or metastable phase. This retains Note 28's declared initialization;
it is not a reproduction of an experimental dataset or every initial condition
used in [1]. The coefficients and finite size, not a digitized phase diagram,
are taken from that paper. Local Markovian photon counting remains an assumption.

For two successive windows Delta retain EXACTLY the chosen statistic

$$
G=Z_{12}-Z_1 Z_2,\qquad Y_b=e^{-sK_b},\quad s=\frac1{7\kappa\Delta},
\quad Z_b=\mathbb E Y_b,\quad Z_{12}=\mathbb E(Y_1Y_2).
$$

We examine kappa Delta=1,5,20. They span a short, intermediate and longer window
relative to the fixed decay time; they are not claimed to be the paper's bin
choices or experimentally mandated settings. A Delta=5 pilot preceded this
three-window check; no parameter sweep over Hamiltonians or fit to G was used.
No numerical accuracy threshold is claimed to be a scientific requirement.

Let Jcal(rho)=sum_i J_i rho J_i^dagger. The exact target computations are

$$
Z_1=\operatorname{Tr}e^{\Delta\mathcal L_s}\rho_0,\quad
Z_2=\operatorname{Tr}e^{\Delta\mathcal L_s}e^{\Delta\mathcal L}\rho_0,\quad
Z_{12}=\operatorname{Tr}e^{2\Delta\mathcal L_s}\rho_0,
\quad \mathcal L_s=\mathcal L+(e^{-s}-1)\mathcal J.
$$

The reference evaluates these full generators numerically, with no low-mode
truncation. Every statement about agreement below is numerical, not an interval
certificate. It concerns G and its three components, not the complete record law.

## 2. Exact symmetry is used before approximation

Uniform periodic dynamics, the ground product state, the total-count jump map and
the trace are invariant under simultaneous spatial translations and reflections.
Thus the operator evolution stays in their invariant subspace. This is symmetry
of density operators, not a claim that local decay preserves the permutation-
symmetric pure-state Hilbert space. Individual site-conditioned records do not
inherit this total-count simplification automatically.

Use normalized orbit sums of matrix units |a><b|. Each site contributes one of
four paired bra/ket symbols. For n=7, Burnside counting of dihedral orbits gives

$$
D_{\rm inv}=\frac{4^7+6\cdot4+7\cdot4^4}{14}=1300,
$$

rather than 4^7=16384 operator coordinates. If U is the orbit isometry, then
L U=U L_inv and Jcal U=U J_inv. These are exact mathematical invariances. The
implemented equalities were checked against an independently assembled full-space
Kronecker generator. Both ordinary and tilted propagation preserve the subspace.

The sparse invariant generator has 20,019 stored nonzero entries in this
implementation. Symmetry alone is NOT a scalable classical solution: in general
this sector still has exponential dimension. The paper [1] already uses translation
symmetry; our addition of reflection and normalized orbit bookkeeping is not a
claimed new physical or algorithmic principle.

## 3. Acquire one small response model from the supplied operators

Acquire the two eigenpairs nearest a small positive real shift of L_inv, including
both right and left eigenvectors. For this calculation the retained eigenvalues
are approximately 0 and -0.066592688531 kappa. Their selection is validated by
direct propagation; it is NOT an arbitrary-size theorem excluding other slow
modes or a certified global gap. Let R contain the two right vectors and B be the
biorthogonal dual, so B R=I. Define

$$
D=\operatorname{diag}(\lambda_0,\lambda_1),\quad
J_2=B\mathcal J_{\rm inv}R,\quad
K_s=D+(e^{-s}-1)J_2,\quad
c=B\rho_0,\quad a=\operatorname{Tr}\circ R.
$$

The three approximate moments are then

$$
Z_1^{(2)}=a e^{\Delta K_s}c,\quad
Z_2^{(2)}=a e^{\Delta K_s}e^{\Delta D}c,\quad
Z_{12}^{(2)}=a e^{2\Delta K_s}c.
$$

After acquisition these are two-by-two matrix exponentials. R, B, D, J2, a and c
are reused across all three Delta values. No phase occupation, switching rate,
photon trace or exact value of G is supplied to fit the model.

This is the leading projected tilted-generator comparator in spectral coordinates,
following the established ideas in [1,2]. It is NOT asserted to be a positive
classical two-state jump generator in this coordinate basis. Positivity of a
complete approximate record law is not required by the current scalar task, and
no such record guarantee is claimed. All reported three-moment estimates lie in
[0,1] in this check.

The overlaps c retain the specified ground initialization instead of setting
it to the steady mode. Nevertheless a two-mode projection omits fast-transient
contributions. We do not assume they vanish: the full ground-start reference
measures their effect. Substituting stationary weights in the SAME small model
is an explicit negative control, not a cheap burn-in step.

### Acquisition is measured as an executed calculation, not granted as input

The baseline acquired both right and left modes using one sparse LU factorization
and its Hermitian-transpose solves. The recorded factorization stores 1,055,494
nonzero factor entries, and the eigensolver used 21 inverse applications for each
side. This is an operation inventory for this implementation, not a portable
wall-clock benchmark or the cost of an optimal algorithm. It is more work than
simply receiving a two-by-two matrix, and that work has actually been performed.

The eigenpair residual test, by itself, does not certify the nonnormal projection
or the output error. Reference propagation and the independent checks below are
additional validation costs. No extrapolation of this sparse-factorization cost
to large n is justified.

## 4. Result: the covariance is closely reproduced

| kappa Delta | Full tilted G (numerical) | Once-acquired two-mode G | Absolute discrepancy |
|---|---:|---:|---:|
| 1 | 0.007257734477 | 0.007224566599 | 3.31679e-5 |
| 5 | 0.005851009803 | 0.005848671243 | 2.33856e-6 |
| 20 | 0.002199682382 | 0.002199440410 | 2.41971e-7 |

These values were computed here from the supplied equations. They are not numbers
transcribed from [1]. The largest individual Z error is about 7.987e-4, 1.851e-4
and 4.744e-5, respectively. G benefits from cancellations: the accurate covariance
must NOT be relabeled as the same accuracy for each probability or a complete
counting distribution. The report retains all three moments and both error types.

For example, at Delta=5 the reduced model with the WRONG stationary initial
weights gives G about 0.003492397208, rather than the ground-start reference
0.005851009803. Thus the comparison has not succeeded by pretending that the
initial condition is irrelevant. No photons from the initial transient are
removed from the target or charged as free state preparation.

### A systematic correction is available without a new sampling framework

As an additional check, acquire two right/left modes of the ACTUAL tilted
L_s for each window. Evaluate the same contractions using those modes and their
actual ground-state/boundary overlaps. This includes the tilt's deformation of
the eigenvalues and vectors rather than keeping only P L_s P. It can incorporate
corrections from eliminated modes, but is not a claim to include every finite-time
fast contribution. The full reference remains necessary to test the truncation.

This adds one factorization and two eigensolves for each s; it is not free and
not the once-acquired baseline. Its G discrepancies are about 1.91965e-5,
1.4957e-8 and below 1e-12 in the three windows. For Delta=5 its largest Z error is
about 4.49e-8. Below-1e-12 entries in the report mean numerical/display resolution,
NOT exact equality. The shortest window still has a nonzero finite-time error.

We neither replaced all classical theory by a Poisson telegraph process nor
claimed that the leading model is the strongest possible classical method.
[2, Sec. V B 2-4] explicitly supplies non-Poissonian and transient qualifications.
Direct tilted contractions, corrected spectral modes, tensors and trajectories
remain available where their costs and accuracy are favorable.

## 5. What this decides, and what it does not

Note 28's amplitude-estimation route improves a generic sampling-precision cost.
The present classical route obtains G without Monte Carlo at all. It also acquires
its small model from H and the jumps rather than a provided set of rates. Thus
ordinary 1/epsilon^2 sampling is not the appropriate sole baseline at this source
anchor. Nothing here requires or proves a separation against every conceivable
classical algorithm.

This single seven-site example cannot settle the joint n,Delta,epsilon scaling.
The symmetry space and sparse factorizations can grow badly with n; tilted modes
may cease to be isolated, and stronger short-time correlations may matter. No
uniform error theorem, tensor-rank bound, or large-n classical tractability result
is inferred. Equally, those possibilities are not evidence that the present
proposal has a useful quantum regime.

**Narrow research decision:** the supported finite anchor does not provide the
missing quantum advantage case. The current two-window covariance proposal should
leave active development and remain a quantitative reference, unless independent
physics identifies a different regime and a specific acquisition bottleneck. Do
not automatically raise n, tighten epsilon, or refine the detector to keep it alive.
The controlled quantum flag/instrument constructions remain valid with their
original access and error assumptions. Monitored quantum sampling as a mechanism,
and other direct quantum outputs, are not rejected.

The next parent step should be a short comparison of independently useful
model/mechanism pairs, not further flags, generic error bounds, or a new classical
metastability solver. A new candidate needs a positive reason the useful output
retains quantum-computational difficulty after the strongest adequate classical
reduction, rather than only a large latent state. A universal lower bound is not
required for that initial hypothesis. No replacement family is selected by this
one experiment; no new repository is warranted.

## 6. Verification, sources, and delivery scope

The final standalone checker ran twice with identical JSON. It performs one
seven-emitter parameter instance at three windows, with no size or coupling
sweep. It checks exact-group bookkeeping against a separately assembled full
16384-coordinate generator; a full-space one-window Z1 propagation at Delta=1;
subdivided exponential-action reference at Delta=5; and acquisition using a
second eigensolver shift. It rejects six invalid inputs and -O/-OO execution.
The small projected models are independently checked against full tilted
propagation, not used to validate themselves.

All executable numbers use complex128, with diagnostic comparison tolerance
3e-8 and twelve-decimal reporting. This is not an interval-certified proof of
those decimals. The exact symmetry argument is separate from numerical
integration, eigenvector conditioning and approximate-mode validation. NumPy's
seed fixes internal numerical norm-estimation choices, not physical trajectories.
No Monte Carlo samples, quantum circuit, amplitude estimation, hardware, native
upstream package, experiment or quantum/classical timing comparison was used.
No historical scientific verifier was rerun or upstream implementation imported.

A preliminary repeated-validation shell call hit its execution timeout; it is
not counted as a successful replay. Redundant full-space validation was reduced
to one independent Z1 propagation while the exact full-space intertwining check
was retained. The final version described above then completed twice. Temporary
prototypes and unfinished outputs are not part of the deliverable.

Primary literature [1] model equations and n=7/V=250/Omega=50 text were inspected;
[2] Sec. V B 1-4 was read as parsed text. Three requested PDF screenshots failed;
no graph values or experimental measurements were inferred from them. This was
not a complete audit of the 90-page source or a novelty claim. A 2026 hidden-
time-reversal metastability preprint was screened but not used to claim that its
assumptions apply to this uniform locally damped ring.

[1] D. C. Rose et al., *Metastability in an open quantum Ising model*,
Physical Review E 94, 052132 (2016). https://arxiv.org/abs/1607.06780
https://doi.org/10.1103/PhysRevE.94.052132

[2] K. Macieszczak et al., *Theory of classical metastability in open quantum
systems*, Physical Review Research 3, 033047 (2021).
https://arxiv.org/abs/2006.01227
https://doi.org/10.1103/PhysRevResearch.3.033047

The live connection exposed read operations but no file-write action; runtime
GitHub access failed on DNS. The installed GitHub integration was checked; no
unrelated integration or permission change was used. This checkpoint is local,
with an add-only patch, NOT a remote commit or an update already made to the live
work order. The final observed remote head is the parallel Note 29 commit stated above;
its contents were read before packaging. No commit was made by this tool session.

Checker SHA256: `fba4c6acd18e9d31ea11fc703ffb752d5d194d58253c49be52ab5534843303d5`.
Report SHA256: `bdbc673e98f1788ba3df070fc82cd164228140dd65037951072e362f34b9e04a`.

Only Quantum-Assisted-Algorithm-Discovery may be modified. Preserve all previous
proofs, code, reports, source data, licenses and third-party rights. The two
classical spin-offs remain independent. No manuscript, release, merge, external
contact, new repository or paid/unattended work is initiated.
