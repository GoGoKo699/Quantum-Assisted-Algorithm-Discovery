# Mechanism scout 02: a spectral record for later weak-probe controls

25 September 2026. Phase 2 exploration; target PRX Quantum; manuscript on hold.
This is an exploratory derivation and small sanity check, not a manuscript,
novelty claim, quantum-advantage result, or selected application benchmark.

## The simple candidate

Use a circuit-model quantum computer to sample a fixed many-body fluctuation
spectrum. Store the sampled frequencies as an ordinary classical record. Later,
evaluate many weak-probe pulse responses from that record, including pulses
chosen after looking at it. No new quantum run is needed for each later pulse.

The intended output is a reusable response predictor, not a plotted spectrum or
a table of previously requested answers. No sparse spectral-line assumption,
low-temporal-entanglement assumption, or fitting of an environment model is
needed for the limited additive guarantee below. The quantum-specific task is
producing the samples, NOT the elementary classical compression argument.

Spectral sampling is prior work: Sels and Demler [1] give a quantum generative
algorithm using a purified observable and phase estimation of energy differences.
Random Fourier features [2], control-adapted noise models [3], quantum-enhanced
classical surrogates [4], and influence-matrix tomography [7] are relevant prior
art. The combination below is not claimed original merely because it can be
written in this form.

## 1. An explicit starting state and access model

Both competitors receive an explicit local Pauli Hamiltonian H on n bath qubits
and a fixed Hermitian Pauli B. Take d=2^n and rho=I/d, so B^2=I and ||B||=1.
No low-temperature state, unknown eigenvector, or supplied quantum-data oracle
is assumed. This maximally mixed bath is a declared special case, not an
approximation asserted valid for arbitrary physical devices.

Let B(t)=exp(iHt) B exp(-iHt). The normalized autocorrelation is

    C(t) = Tr[B(t) B]/d = integral exp(i omega t) mu(d omega),

where, in an energy basis,

    mu = (1/d) sum_ab |B_ab|^2 delta_(E_a-E_b).

This is a positive probability measure, symmetric because B is Hermitian.
The eigenbasis expression is a derivation; the quantum procedure need not
calculate that eigenbasis or enumerate the spectral lines.

Prepare n Bell pairs, then apply B to one half:

    |B>> = (B tensor I) |Phi>,   |Phi> = d^(-1/2) sum_x |x,x>.

Phase estimation of

    G = H tensor I - I tensor H^T

samples mu at finite resolution. Transposition is essential for complex H.
For an explicit Pauli sum it just changes signs of terms with an odd number of
Y factors. Evolution under G factorizes into evolution under H and -H^T.
This special Pauli preparation is deterministic; arbitrary nonunitary observables
can have different normalization/preparation costs. The method uses at least
2n bath-register qubits plus phase-estimation workspace, not a machine whose
size is determined by the short output record.

## 2. The future classical query

Fix a duration T. Let a later pulse be a complex integrable function u supported
on [0,T], with integral |u(t)| dt <= A. Define

    M_u = integral_0^T u(t) B(t) dt,
    R[u] = Tr[M_u^dagger M_u]/d.

The spectral representation gives exactly

    R[u] = integral |integral_0^T u(t) exp(i omega t) dt|^2 mu(d omega).

After drawing m independent frequencies omega_j, store just those frequencies.
The classical predictor is

    R_hat[u] = (1/m) sum_j |integral_0^T u(t) exp(i omega_j t) dt|^2.

It is nonnegative and at most A^2. With p piecewise-constant pulse bins, direct
query work is O(mp) arithmetic/transcendental evaluations with the needed
precision; reading and transforming the pulse are not free. A Gram matrix can
also be precomputed classically. This is one predictor for new inputs, not a
separate quantum estimate for each pulse.

## 3. Uniform reuse without a sparse spectrum

Let C_hat(t)=(1/m) sum_j exp(i omega_j t). If

    sup_{|t|<=T} |C_hat(t)-C(t)| <= epsilon,

then direct expansion of the two quadratic forms and the triangle inequality give

    |R_hat[u]-R[u]| <= epsilon (integral |u|)^2 <= epsilon A^2

SIMULTANEOUSLY for every admitted u. No union bound over a list of candidate
pulses is required. A pulse can therefore be chosen adaptively after inspecting
the record. Exact optimization of the approximate response over a fixed feasible
pulse family incurs at most 2 epsilon A^2 loss versus its true optimum; classical
optimization cost is additional, and optimization need not be easy.

The guarantee fixes H, B, the initial bath state, duration bound and pulse norm.
It does not cover arbitrary changes of Hamiltonian, temperature, coupling
operator, or nonlinear/strong probe interactions. It is additive in the
normalized response, not relative accuracy for arbitrarily small probabilities.

For a support bound |omega|<=Omega, ideal empirical Fourier concentration gives

    m = O(epsilon^-2 log[(2+Omega T)/(epsilon delta)]).

Here is one conservative sufficient allocation that ALSO leaves room for
frequency error. Assume 0<epsilon<1, 0<delta<1 and Omega,T>0. Take a grid of
M=ceil(16 Omega T/epsilon)+2 points on [-T,T], and

    m >= 64 epsilon^-2 log(8 M/delta).

At each grid point, real/imaginary Hoeffding bounds give probability at most
4 exp(-m epsilon^2/64) of complex error greater than epsilon/4. The union bound
makes this at most delta/2. C_hat-C is 2 Omega-Lipschitz; interpolation adds at
most epsilon/4. Thus ideal samples have uniform error at most epsilon/2.

If every measured frequency is within zeta=epsilon/(2T) of its associated ideal
frequency, the additional uniform error is at most T zeta=epsilon/2. Allocate
failure probability delta/(2m) to each spectral estimate. Together the guarantee
holds with probability at least 1-delta. Omega=0 or T=0 are trivial cases.

This is ordinary empirical Fourier approximation, closely related to [2], not a
new quantum sampling law. The statistical record length depends only
logarithmically on the bandwidth-time product, but quantum simulation work still
depends on system size and the Hamiltonian description.

## 4. A physically nontrivial interpretation at a maximally mixed bath

Do NOT call R the dissipative susceptibility or energy absorption of the
standalone maximally mixed bath: a bath state I/d is unchanged by unitary driving.
Instead introduce an initially pure probe qubit in |0>, coupled in its
interaction picture by

    V(t)=g [u(t)|1><0| + u(t)^*|0><1|] tensor B(t).

Its flip probability is g^2 R[u] to leading order. This is a weak-probe response,
not a claim to predict the full controlled bath. Spectroscopy and
control-dependent responses have prior filter-function formulations [3].

There is a simple uniform perturbative bound in this declared model. Put
gamma=|g| integral |u|. Each interaction flips the probe, so its off-diagonal
Dyson block has only odd orders. The first-order block has norm at most gamma;
the remaining block has norm at most sinh(gamma)-gamma. Consequently

    |p_flip[u]-g^2 R[u]| <= sinh(gamma)^2-gamma^2 = O(gamma^4).

Combining it with the record error gives an additional g^2 epsilon A^2 term.
For gamma=0.1 the displayed perturbative bound is about 3.34e-5. That is an
illustration, not an externally justified experimental error tolerance. Long
fixed-amplitude pulses grow A and hence the error/weak-coupling requirement;
normalizing the pulse must not be used to conceal that tradeoff.

## 5. Quantum costs and the comparison that is still missing

Resolution zeta=O(epsilon/T) entails coherent evolution lengths of order
T/epsilon per phase-estimation sample, with further logarithmic overhead for
small failure probability. The full construction cost includes m Bell-state
preparations, controlled evolutions under G with adequately small simulation
error, phase estimation, measurements and classical storage. It is more honestly
written as m times the implemented sampling cost than as a sample count alone.

For explicit local H, coefficient loading and gates can be compiled directly;
no large coherent lookup data structure is granted for free. No full gate count,
physical resource estimate, or measured quantum execution is provided here.
Finite-precision simulation errors must be budgeted in addition to the ideal
phase-estimation frequency bound, for example by allocating a sufficiently
small output-distribution error across all m samples.

Both competitors can reuse any classical response model they construct. The
classical method may estimate C(t) directly, use polynomial or Chebyshev
approximations, propagate operators, use tensor networks or dynamical typicality,
or bypass our frequency representation entirely. It need not diagonalize H.
Linked-cluster/typicality methods [5] and recent Pauli-propagation plus time
extension [6] provide concrete alternatives. The latter's reported examples
use few characteristic frequencies; neither its scope nor ours proves all
many-body responses easy or hard.

A broad spectrum is not a hardness certificate. Rapidly decaying correlations
can make the needed response inexpensive to approximate; late-time features
smaller than the required additive tolerance cannot justify expensive discovery.
A classical record learned once benefits from the same later reuse. The quantum
claim would have to concern obtaining an equally adequate record, or the same
answers by another method, after those alternatives are allowed.

The PRX Quantum article [4], published 12 June 2026 (arXiv v2 revised 4 August
2026), already studies quantum-enhanced classical surrogates of parameterized
landscape patches. It has its own quantitative patch guarantees, including
uniform results in restricted regimes. Our bounded-area response formulation
is not automatically novel relative to that literature. No priority claim
follows from this short scout.

## 6. The calculation actually run

`spectral_record_check.py` is a NumPy-only, four-spin square-lattice toy with
unequal ZZ interactions and X, Y, Z fields. The Y terms make H complex, so the
transpose-sensitive doubled-generator identity is tested rather than hidden
by a real Hamiltonian. This is NOT a named material or classically hard workload.

The script diagonalizes the 16-dimensional bath CLASSICALLY and samples the
exact spectral weights with seed 20260925. It does not execute a quantum
sampler, compile phase estimation, or establish advantage.

For T=8 and twelve equal pulse bins, it evaluates all 4096 sign pulses of
amplitude 1/T (area one). Maximum response discrepancies in the recorded run:

- 128 spectral samples: 0.1124540057.
- 1024 samples: 0.0217331131.
- 8192 samples: 0.0012226383.

These are observed maxima over that finite pulse set, not certified universal
errors or a general monotonic convergence claim. Entrywise Gram-matrix errors
also bound arbitrary complex area-one coefficients in the same bin family,
up to the numerical arithmetic used. The toy's best pulse is constant; all
three records select it, so its zero measured selection regret is NOT evidence
of nontrivial optimization or algorithm discovery.

The maximum correlation identity discrepancy is 5.56e-16; the explicit
Liouvillian-action discrepancy is zero at the recorded precision. Rounding
frequencies on a 0.002 grid gives maximum sampled-time discrepancy about
7.40e-4, below the all-time perturbation bound 0.008. Six distinct
pulse/coupling pairs are also checked against the full 32-dimensional probe+bath
unitary; the quadratic response errors satisfy the displayed Dyson bound.

Reproduce without overwriting stored observations:

    OPENBLAS_NUM_THREADS=1 python exploration/phase_2/spectral_record_check.py \
      --output /tmp/new-spectral-record-observations.json

Requires NumPy; the recorded run used 2.3.5. Floating-point values and timing are
not portable byte-identical fixtures. No old research verifiers were rerun in
this exploratory pass; historical code, licenses and results remain unchanged.

## 7. Decision

Retain this as one simple mechanism to probe, not a paper-ready contribution:
quantum spectral samples can act as a reusable positive classical response
model for bounded-area weak probes. The main computation is the response model,
not a residual correction to an existing answer.

The decisive missing object is an independently motivated interacting-system
response, with a required time/accuracy window, that remains expensive for
strong classical methods but has affordable explicit quantum sampling. A
high-temperature local-spin probe is a possible physical setting, not a fixed
application or demonstrated necessity. Do not scale the four-spin toy until
one chosen classical solver fails. Do not claim novelty for [1]+[2] or reuse
alone. Manuscript preparation stays on hold.

## Primary references

[1] D. Sels and E. Demler, Quantum generative model for sampling many-body
spectral functions. Physical Review B 103, 014301 (2021).
https://arxiv.org/abs/1910.14213 ; https://doi.org/10.1103/PhysRevB.103.014301

[2] A. Rahimi and B. Recht, Random Features for Large-Scale Kernel Machines.
NeurIPS 20 (2007).
https://papers.nips.cc/paper/2007/hash/013a006f03dbc5392effeb8f18fda755-Abstract.html

[3] T. Chalermpusitarak et al., Frame-Based Filter-Function Formalism for Quantum
Characterization and Control. PRX Quantum 2, 030315 (2021).
https://arxiv.org/abs/2008.13216 ; https://doi.org/10.1103/PRXQuantum.2.030315

[4] S. Lerch et al., Efficient quantum-enhanced classical simulation for patches
of quantum landscapes. PRX Quantum 7, 020359 (2026).
https://arxiv.org/abs/2411.19896 ; https://doi.org/10.1103/fhc5-8sm6

[5] J. Richter and R. Steinigeweg, Combining Dynamical Quantum Typicality and
Numerical Linked Cluster Expansions. Physical Review B 99, 094419 (2019).
https://arxiv.org/abs/1901.02909

[6] A. F. Kemper et al., Efficient computation of real-time correlators using
Pauli Propagation. arXiv:2607.24924 (27 July 2026); preprint.
https://arxiv.org/abs/2607.24924

[7] I. A. Luchnikov, M. Sonner and D. A. Abanin, Scalable tomography of many-body
quantum environments with low temporal entanglement. arXiv:2406.18458.
https://arxiv.org/html/2406.18458v2
