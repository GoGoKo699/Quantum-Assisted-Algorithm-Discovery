# Normalization as a computational resource: conditioning by reverse preparation

26 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.
This follows the author's observation about unitary normalization. It does not
commit the project to chemistry, QML, a device, or a new manuscript. These are
explicit special cases of established retrodiction, plus finite sanity checks;
no novelty, classical lower bound, or useful quantum advantage is established.

## 1. A prior-preserving unitary is a conditional sampler

The input label x is CLASSICALLY drawn with probabilities pi_x, after which the
basis state |x> is prepared. The basis and ensemble are part of the problem, not
inferred merely from a density matrix. Apply an explicitly known circuit U and
measure in the same basis. Write W_yx=|U_yx|^2 and rho=sum_x pi_x |x><x|.

Suppose U rho U^dagger=rho. Then (pi_x-pi_y)U_yx=0 and the output distribution
is pi. For an event B consisting of basis labels, with pi(B)>0,

    p(x|B) = pi_x sum_(y in B) W_yx / pi(B).

Draw y from pi conditioned on B, prepare |y>, apply U^dagger, and measure x.
The result has distribution

    sum_(y in B) [pi_y/pi(B)] W_yx = p(x|B).

The conditional endpoint preparation and inverse circuit must both be affordable.
A rare event is not necessarily difficult to prepare, but an arbitrary set B
can encode a difficult constraint problem. No generic conditional-state oracle
is assumed. This sufficient invariance condition is not necessary for every
special process: a classical invertible permutation, for example, can have an
easy inverse posterior even when it changes the prior.

This extends the uniform-prior calculation without reweighting: rho can be
highly nonuniform across invariant sectors. A concrete case is U conserving
Q=sum_j n_j and pi_x=f(Q(x))/Z. Either fixed particle number or independent
identically biased occupation bits gives an exactly invariant classical ensemble.
It is not a general low-temperature Gibbs-state preparation result for an
arbitrary interacting Hamiltonian.

The conceptual distinction is to encode the final condition in the starting
state of a reverse computation rather than reject forward histories until it
happens. The literature already relates physical reversal and Bayesian
retrodiction [1,2]. The computational novelty of a useful application remains
unestablished. U^dagger means inverse circuit gates, not an assumed physical
antiunitary time-reversal operation on an unknown device.

## 2. An application-shaped question, not an advantage claim

Consider an interacting lattice with n occupied/unoccupied sites, fixed particle
number N, and a uniform classical ensemble over its binomial(n,N) initial basis
configurations. Number-conserving U leaves that ensemble invariant. Condition
on a specified patch of k sites being fully occupied at the final time.

The final event probability is exactly

    p(B)=binomial(n-k,N-k)/binomial(n,N).

Conditioned final preparation is elementary: fill the patch, choose N-k occupied
sites uniformly among the remainder, and prepare that basis state. No forward
rare-event waiting is involved. A reverse circuit sample gives the exact initial
configuration distribution conditional on the final patch event.

For n=100,N=50,k=20 the event probability is 8.79303628551999e-8, so naive
forward rejection averages 11372635.885 trials. This is a combinatorial example,
NOT a 100-spin simulation, resource estimate, or speedup against best classical
computation. The inverse procedure still pays the full many-body circuit cost.
The one-time marginal is stationary and easily known; the two-time conditional
law can depend on the dynamics. Thus equilibrium normalization does not make
the inference question vacuous. It may nevertheless be classically tractable,
particularly for low-order queries or effectively free dynamics.

The scientific question would be which initial configurations statistically
precede an atypical final density patch. It is not a unique reconstruction of
an actual past, a claim about arbitrary unmeasured quantum histories, or a way
to estimate p(B) by counting backward successes. That probability is already
known here from the ensemble. Conditioned trajectory ensembles with intermediate
measurements require a separately specified measurement model.

Rare-dynamics sampling has substantial prior work, including quantum Doob
transforms for trajectory observables of open systems [4]. That is a different
conditioning task, not a theorem that this endpoint sampler replaces those
methods. Reversible classical processes also exploit backward sampling; the
quantum question concerns interference-rich dynamics without a comparably cheap
classical conditional simulator.

## 3. Two boundary conditions expose where rejection returns

Let A and B be finite sets of basis states, with ranks a and b, and let

    Z_AB = sum_(x in A,y in B) |U_yx|^2.

With a uniform initial ensemble on A, forward acceptance at B is Z_AB/a.
With a uniform reverse ensemble on B, acceptance at A is Z_AB/b. Thus

    p_reverse(A|B) = (a/b) p_forward(B|A).

Both procedures, conditioned on acceptance, yield the same joint endpoint
law W_yx/Z_AB. The identity assumes the two uniform preparations and membership
tests are implementable; their sizes do not guarantee their preparation cost.
If A is an invariant sector and B is a subset, Z_AB=b and reverse acceptance
is one. If A is a special tiny initial set, reverse acceptance may again be tiny.
This is elementary reciprocity, not a new fluctuation theorem.

The fixed initial work register of an ordinary simulator is exactly such a
constraint. Take a controlled likelihood circuit

    V = sum_theta |theta><theta| tensor V_theta,

with uniform theta and work input |0>. Observe work outcome y. Starting reverse
from uniform theta and |y> leaves the theta marginal uniform: the controlled
unitary cannot change theta. Accepting only reverse work output |0> gives the
correct posterior, but its acceptance probability is the ORIGINAL evidence
probability p(y). The expensive conditioning has not vanished. More general
quantum inference algorithms have nontrivial evidence-probability dependence [3].
Dilations and ignored environment correlations must not be assumed reversible
without their proper prior treatment [2].

## 4. What specifically requires quantum computation?

Both a quantum circuit and a classical stochastic kernel can be doubly
normalized. If a classical kernel has efficiently sampleable forward and
reverse steps, the same inference benefit is classical. In particular, drawing
an efficiently invertible random permutation and undoing it is not quantum
advantage. For circuits close to free-fermion models, strong classical simulation
algorithms must also be retained [5].

Replacing each gate by its entrywise squared magnitudes instead gives a different
process: it removes interference after every gate. The correct total transition
matrix is |G_L ... G_1|^2, not in general |G_L|^2 ... |G_1|^2. This distinction
is necessary but is not a classical lower bound. Tensor networks, amplitude
methods, structural algorithms, rare-event techniques and approximations adequate
for the actual conditional observable remain legitimate competitors.

The broad uniform-prior retrodiction task even contains ordinary quantum circuit
sampling: given V, use U=V^dagger and condition on y=0. The posterior over x is
|<x|V|0>|^2. This is a simple reduction showing the task is not automatically
classically easy, NOT a new supremacy theorem or independently useful instance.
Any strong generic conditional sampler would also sample general circuits.

The seed idea remains simple: normalization enforced by dynamics can remove an
otherwise expensive conditional sampling step. We have not proved that nature
provides a new universally fast inference algorithm, or that our quantum sampler
outperforms every classical strategy on a worthwhile problem.

## 5. Exact finite checks actually run

reverse_inference_check.py builds 28 number-conserving two-site gates on eight
sites, using NumPy dense matrices. This is a small classical calculation, not
execution on a quantum computer. The four-particle sector has 70 configurations.
Conditioning on three occupied output sites leaves five compatible endpoints.

- Evidence equals 1/14 to floating-point precision.
- Direct Bayes and inverse sampling agree to TV distance 3.73e-16.
- A nonuniform stationary product prior with occupation probability .27 agrees
  to TV distance 3.64e-16; evidence is .27^3.
- Replacing every gate by a stochastic transition changes the conditional law
  by TV distance .196880. This is a different physical model, not a best-classical
  comparator or a speedup claim.
- Fixing the initial configuration to 01010101 gives forward probability
  .0607376183 but reverse acceptance .0121475237, exactly the 1/5 rank ratio.
- A four-hypothesis controlled-likelihood example retains a uniform hypothesis
  distribution before the initial-workspace filter. Filtering gives the desired
  posterior and accepts with probability .0007497050543, equal to forward evidence.
- The 100-site example above was only evaluated by binomial arithmetic.

Reproduce with NumPy and exclusive output creation:

    OPENBLAS_NUM_THREADS=1 python exploration/phase_2/reverse_inference_check.py \
      --output /tmp/reverse-inference-observations.json

Floating-point observations need not be byte-identical across platforms.
No earlier research verifier, real material model, hardware, or strong native
classical conditional-sampling baseline was executed in this pass.

## 6. Next discriminating question

Keep this as an open mechanism branch; do not force it into the chemistry task.
The next substantive issue is an independently informative conditional observable
for an interacting model with affordable endpoint preparation. Test the SAME
observable against strong classical reverse and conditional methods, not just
forward rejection. If a coarse precursor statistic is already determined by
hydrodynamics or free-particle theory, sampling an intricate posterior is not
needed for that purpose. A full conditional sampler is a broader task and
needs its own justification.

Do not convert these elementary identities into a manuscript. The useful
research target is a consequential conditional computation whose normalization
cost is genuinely removed and whose remaining coherent evolution matters.
The reusable artifact here is a sampler/circuit and classical conditional samples
for specified evidence, not a universal record for all future observations.

## Primary sources and inspection scope

[1] F. Buscemi and V. Scarani, Fluctuation theorems from Bayesian retrodiction,
Phys. Rev. E 103, 052111 (2021), arXiv:2009.02849.
https://doi.org/10.1103/PhysRevE.103.052111
Primary abstract checked; the elementary formulas in this note are derived above.

[2] C. C. Aw et al., Role of Dilations in Reversing Physical Processes:
Tabletop Reversibility and Generalized Thermal Operations,
PRX Quantum 5, 010332 (2024), arXiv:2308.13909.
https://doi.org/10.1103/PRXQuantum.5.010332
Publisher abstract and popular summary inspected on 26 September 2026. The
article relates Bayesian reverse maps to reversing dilations while accounting
for system-environment correlations. No claim to reproduce the full proofs.

[3] G. H. Low, T. J. Yoder, I. L. Chuang, Quantum inference on Bayesian networks,
Phys. Rev. A 89, 062315 (2014), arXiv:1402.7359.
https://doi.org/10.1103/PhysRevA.89.062315
Primary abstract and stated rejection-sampling complexity checked.

[4] F. Carollo et al., Making rare events typical in Markovian open quantum
systems, Phys. Rev. A 98, 010103(R) (2018), arXiv:1711.10951.
https://doi.org/10.1103/PhysRevA.98.010103
Primary abstract inspected; different trajectory-conditioning problem, no
unmatched performance comparison is asserted.

[5] Improved simulation of quantum circuits dominated by free fermionic
operations, Quantum 8, 1549 (2024).
https://quantum-journal.org/papers/q-2024-12-04-1549/
Author summary inspected for the strong classical competitor, no native run.

[6] M. Liu, V. Scarani, G. Bai, Proper and Improper Mixed States Serve as Different
Prior Beliefs for Quantum State Retrodiction, Phys. Rev. Lett. 136, 060203 (2026).
https://doi.org/10.1103/xx43-p1py
Primary abstract inspected. This note fixes the classical preparation labels
rather than conflating all ensembles with the same density matrix.
