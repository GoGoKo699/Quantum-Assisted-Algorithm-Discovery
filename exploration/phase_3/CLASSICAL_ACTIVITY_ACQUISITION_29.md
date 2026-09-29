# Classical activity acquisition 29: test the compact model, including its acquisition

29 September 2026. Baseline: `4f0e57e2ef56e3ddb395ebecb4fec115c29d3b44`.
Active branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Decision:** the source-matched seven-emitter calibration does not support advancing
Note 28's proposed quantum advantage. A small classical tilted contraction was
actually acquired from the specified generator, without supplied phase rates or
trajectory fitting, and compared with full symmetry-reduced propagation. Its
largest observed covariance discrepancy is 3.32e-5 over the three declared windows.
This is a numerical finite-model result, not an all-size tractability theorem or
an interval certificate. It closes this calibration/acquisition test, not direct
quantum sampling as a research direction. No new repository or spin-off is needed.

## 1. The same useful question and the actual source slice

The target from [Note 28](EMISSION_ACTIVITY_CLAIM_28.md) is

$$
G=Z_{12}-Z_1Z_2,\quad Z_b=\mathbb E[e^{-sK_b}],\quad
Z_{12}=\mathbb E[e^{-s(K_1+K_2)}],\quad s=1/(n\kappa\Delta).
$$

K1,K2 count all emissions in adjacent windows Delta. We keep ground initialization,
local Markov decay, and the original nonstationary two-window dynamics. This is one
bounded activity statistic, not a full record, stationary switching rate or rare-event
relative-error task. The transform is a project choice motivated by activity
correlations; neither its numerical tolerance nor these particular windows are
claimed as experimental requirements.

For the decisive calibration use the periodic nearest-neighbor ring of Rose et al.
[1], with n=7, Omega/kappa=50, V/kappa=250. The source explicitly studies this finite
parameter choice and exploits translation symmetry. We use its equations, not
values digitized from its plots and not an experimental dataset. Our ground initial
state remains the one specified by Note 28; it is not silently replaced by the
all-up or transverse product states in some of the paper's figures.

The three fixed checks use kappa*Delta=1,4,16. They cover an early window, an
intermediate window, and a window comparable to the acquired slow time
kappa*tau_s=15.01666357. They were fixed before comparing the target covariances;
there was no search over physical parameters for an advantageous result. They
are diagnostics of one family member, not independent application demonstrations.

## 2. Exact symmetry before any approximation

The uniform periodic generator L, total jump map J(rho)=sum_i J_i rho J_i^dagger,
and ground state are invariant under simultaneous rotations and reflections of
site labels. The total-count tilt Ls=L+(exp(-s)-1)J has the same invariance. Thus
all three exact contractions stay in the dihedral-invariant operator subspace.
This is a weak symmetry of the superoperator: it does not restrict the system to
the fully symmetric spin-n/2 Hilbert subspace, which would be a different problem.

Use orthonormal sums of matrix units |a><b| over these spatial orbits. For n=7,
Burnside counting on the four possible bra/ket symbols per site gives

$$
D_{\rm inv}=\frac{4^7+6\cdot4+7\cdot4^4}{14}=1300,
$$

rather than the full 4^7=16384 operator coordinates. The generator has 20,019
stored nonzero entries after eliminating exact zero entries. It is constructed
from local bit transitions, not from an unknown eigenbasis. An independent
full-basis assembly verifies the intertwining identities Lfull E=E Linv and
Jfull E=E Jinv, as well as E^dagger E=I. These identities also have the direct
group-invariance proof; the reduction is exact before low-mode approximation.

This symmetry reduction is not new and is not polynomial in n asymptotically.
The invariant dimension can still grow approximately as 4^n/(2n). Its value here
is an actually used classical alternative for the selected finite calibration.

## 3. Acquire the two-mode contraction, rather than supplying its parameters

Compute two right and two left slow modes of the UNTILTED 1300-dimensional
generator by shift-invert sparse eigensolves. Let R contain a trace-one stationary
mode and a Hermitian trace-zero slow mode, and choose the dual W with WR=I.
The measured coordinate row and ground-start coefficients are

$$
a={\rm Tr}\circ R,\qquad c=W\rho_0.
$$

Acquire only the two matrices

$$
A=WLR,\qquad B=WJR,\qquad K_s=A+(e^{-s}-1)B.
$$

In one explicitly fixed real coordinate convention, in kappa units,

$$
A\simeq\begin{pmatrix}0&0\\0&-0.066592688531\end{pmatrix},\quad
B\simeq\begin{pmatrix}
0.193578709456&-3.329078385180\\
-0.113665967613&3.233074395649
\end{pmatrix},\quad
c\simeq\binom{1}{-0.031276787240},\quad a\simeq(1,0).
$$

These entries are acquired spectral coordinates, NOT classical probabilities or
transition rates in this basis. In particular, negative entries of B are not
clipped. We do not claim that this projection is completely positive or that it
is a valid photon-history generator for arbitrary tilts. The narrower task is
deterministic evaluation of three scalar contractions, validated below.

The approximation computes

$$
\widetilde Z_1=a e^{\Delta K_s}c,\qquad
\widetilde Z_2=a e^{\Delta K_s}e^{\Delta A}c,\qquad
\widetilde Z_{12}=a e^{2\Delta K_s}c.
$$

The SAME acquired A,B,c,a are reused for all three windows. No covariance value,
photon record, experimental fit, phase rate, or stationary state is supplied as
training data. The stationary mode is computed from the input; it is not used
as the target initial state. Keeping c retains the ground state's slow projection,
not the full fast transient. The omitted transient and within-phase effects are
part of the measured approximation error, not presumed zero.

This is the low-mode tilted projection discussed in [2, Eq. (48)], evaluated
without making its additional reduction to a Poisson switching model. Counting
fluctuations, initial transients and fast-mode corrections in [2] remain relevant.
Success of this calculation does not automatically validate every derivative,
counting field or microscopic record.

## 4. The decisive numerical comparison

The reference uses sparse exponential action of the FULL invariant generator,
not the two-mode model, not a population approximation and not a sample average:

$$
Z_1={\rm Tr}\,e^{\Delta L_s}\rho_0,\quad
Z_2={\rm Tr}\,e^{\Delta L_s}e^{\Delta L}\rho_0,\quad
Z_{12}={\rm Tr}\,e^{2\Delta L_s}\rho_0.
$$

| kappa Delta | Full covariance | Acquired two-mode covariance | Absolute discrepancy |
|---:|---:|---:|---:|
| 1 | 0.007257734477 | 0.007224566599 | 3.31679e-5 |
| 4 | 0.006263468066 | 0.006260284472 | 3.18359e-6 |
| 16 | 0.002807095126 | 0.002806720614 | 3.74512e-7 |

These are observed complex128 errors, NOT certified interval bounds. The code
checks the declared diagnostic threshold 3.4e-5; that threshold is not promoted
to a scientifically mandated tolerance. The largest errors in the individual Z
values are respectively 7.98714e-4, 2.29422e-4 and 5.91738e-5. Covariance accuracy
is better here because some errors cancel. Do not infer that each moment has the
smaller covariance error or that cancellation is guaranteed in other regimes.
For stricter accuracy in this finite case, the full invariant propagation remains
available; a two-mode error floor is not a classical-computation error floor.

### Ground-start information is not free equilibrium preparation

Replacing c by the stationary-mode coefficients gives approximate covariances
0.004058943674, 0.003682506652 and 0.001951147370. Those differ substantially from
the ground-start target. This negative control prevents us from explaining the
successful reduction by changing the initial state. We do not insert an uncounted
burn-in interval, reset the emitters between windows, or delete early photons.

## 5. What acquisition AND validation cost in this executed test

The primary acquisition performs one sparse LU factorization of L-sigma I,
with sigma=1e-4 kappa used only as an eigensolver shift. Its factors contain
1,055,494 nonzeros in total, substantially more than the generator. It then uses
21 inverse actions for the right modes and 21 adjoint inverse actions for the
left modes, reusing that factorization. The code forms B, c and a by projection.
These counts are reported, rather than calling the two-dimensional model free.
They are properties of this numerical run, not a complexity bound for arbitrary
n or a comparison of classical FLOPs with quantum gates.

Validation is additional: a second acquisition with shift 1e-3, the full-basis
symmetry checks, and 18 sparse exponential actions on the 1300-dimensional sector
across the three windows (including half-step consistency checks). Exploratory
full-mode eigendecompositions of this SAME seven-emitter problem independently
cross-checked the selected modes and contractions; those are not part of the
small-model producer or evidence for larger systems. No physical parameter sweep
or larger-emitter simulation was performed.

All of this was executed in the current environment; no external simulator,
precomputed phase data or large numerical campaign was needed. We do not report
a quantum/classical wall-clock ratio. Numerical convergence checks and small
eigenpair residuals are not interval certification of a nonnormal spectral
projection. Stronger rigorous validation would have an additional cost.

After acquisition, evaluating another specified Delta or s requires only small
matrix exponentials, subject to renewed model-accuracy validation. Varying n,
Omega,V or kappa generally changes the acquisition problem; those parameters
are not covered by the same table for free. Classical tensor/cluster approaches
may improve the scaling beyond this exact-symmetry implementation.

## 6. Consequence for the proposed quantum claim

Note 28's two flags, coherent channel access and amplitude-estimation construction
remain mathematically valid. Its O(1/epsilon) estimator calls improve generic
sample averaging, not deterministic evaluation of an adequate small tilted model.
The latter is not forced to draw O(1/epsilon^2) trajectories. At fixed finite size,
full direct propagation is also a deterministic competitor at tighter tolerances.

For this source-matched calibration, the supposedly missing classical acquisition
has now been performed and the result tested. There is no identified cost obstacle
for quantum processing to remove here. A quantum resource-compilation campaign
based on this example would not be justified by the present evidence.

This does NOT establish that a growing ring is easy: the symmetry reduction alone
remains exponential, metastable quality can change with size, and nonnormal
conditioning can affect acquisition. It also does not establish that these three
windows resolve every physically relevant phenomenon. A broad all-size impossibility
claim would exceed the result just as much as a quantum-advantage claim would.

**Priority decision:** retain the emitter constructions and this finite acquisition
as reference evidence; do not continue the standalone activity-precision claim
merely by enlarging the ring or tightening epsilon. Reopening it requires a
specific useful joint size/time/accuracy regime and an independently justified
classical-acquisition bottleneck, not the existence of 2^n amplitudes. The parent
should next broaden its positive mechanism comparison, as Revision 27 prescribes.
No new generic estimator, metastability framework or third spin-off is needed.

## 7. Execution, sources, and preservation

The final checker ran twice with byte-identical JSON under single-threaded BLAS;
-O/-OO and five invalid inputs were rejected. It reconstructs the model and its
low-mode coefficients from scratch. It uses no photon samples. Matrix-generator
intertwining is checked against the full operator basis; direct propagation,
eigensolver-shift, step-composition, zero-tilt and initial-state controls are
recorded. Decimal zeros in the report can reflect rounding below 5e-13, not exact
arithmetic. NumPy/SciPy floating-point diagnostics are not interval certificates.

No quantum circuit, amplitude estimation, laboratory measurement, native upstream
application package, many-size study or speedup benchmark was executed. No earlier
scientific verifier was rerun. No source code, plot data or fitted parameters from
another repository were imported. Earlier notes, including the user-supplied
Note 28 archive, were read without modification.

[1] Rose et al., *Metastability in an open quantum Ising model*, PRE 94, 052132
(2016), arXiv:1607.06780. Model equations (10)-(11), translation reduction,
Sections III B/E, and the stated n=7 parameter slice inspected as parsed primary
PDF text. Figure captions were read to establish source scope, not digitized.
https://arxiv.org/abs/1607.06780

[2] Macieszczak et al., *Theory of classical metastability in open quantum systems*,
PR Research 3, 033047 (2021), arXiv:2006.01227v2. Section V B 2, especially Eq. (48),
its comparison with Eq. (47), nonnormal/fast-mode qualifications, and the initial-
transient discussion inspected. This is not an independent audit of its entire
90-page paper/supplement. https://arxiv.org/abs/2006.01227

Sources checked 29 September 2026. Requested PDF screenshots failed for Rose
pages 5/8 and the 2021 page 18; no numerical conclusion came from a plot or table.
A broader current-literature screen did not supply a new theorem for this ring;
we do not transfer collective-spin or hidden-time-reversal results to it. The
methods are existing symmetry reduction, spectral projection and sparse linear
algebra. No algorithmic priority or new physical prediction is claimed.

Only Quantum-Assisted-Algorithm-Discovery may be modified. Direct outputs and
model-first exploration remain authorized; manuscript preparation stays on hold.
All earlier notes, code, data, reports, licenses and third-party rights remain.
Other mechanisms stay available and both existing spin-offs stay independent.
No contact, paid/unattended work, branch merge, release or administration change.
