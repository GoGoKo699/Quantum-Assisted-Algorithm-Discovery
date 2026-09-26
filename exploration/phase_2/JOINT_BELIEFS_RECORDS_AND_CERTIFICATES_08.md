# Preserve joint uncertainty, then test whether a classical replacement is safe

26 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.
Repository base read: 601668d46c68879eeb76965a8e12daaf541a083e.
This is a mechanism/refinement note with finite checks, not a new fidelity,
concentration, quantum-inference, or distribution-testing theorem. No useful
quantum advantage, trained model, or native inference benchmark is claimed.

## 1. The distinction from the preceding conditional-memory note

Retaining correlations does not necessarily mean retaining a quantum register.
For a classical posterior p(x|e), measuring a correctly prepared quantum encoding
in the label basis produces an entire JOINT sample, not independently sampled
marginals. Such samples preserve relationships that a product approximation
would erase. The difficulty can lie in obtaining those samples, rather than in
storing and querying them afterward. Preparation/update costs remain open.

Two downstream jobs must be separated:

- Answer a specified family of statistical/decision questions under a fixed p.
- Certify that a cheaper candidate distribution q can replace p for every bounded
  question, including ones not chosen in advance.

The first can use a compact ordinary sample record. The second is genuinely
stronger. Coherent comparison gives a concrete conditional route to it, provided
we can prepare suitable states. This reconnects to discovery-and-classical-reuse:
a classical surrogate is useful only if the intended relationships survive it.
Neither operation creates information about an unknown data source for free.

## 2. A joint record preserves many specified queries

Let X_1,...,X_m be independent samples from p. Fix a family F of M functions
f:X->[0,1], independently of the realized samples. Empirical means obey

    Pr(max_f |mean_i f(X_i) - E_p f| > epsilon)
       <= 2 M exp(-2 m epsilon^2).

Thus m >= log(2M/delta)/(2 epsilon^2) suffices. This is Hoeffding plus a union
bound [1], not a new statistical result or a quantum sample-count advantage.
One may choose which f in this already-declared family to ask AFTER seeing the
record. Arbitrary newly invented functions need not be covered. Dependence
between samples requires an appropriate analysis; raw MCMC steps are not iid.

For bounded utilities u_a in a fixed finite action family, an action maximizing
the empirical utility is within 2 epsilon of the true optimum on this event.
If the empirical optimizer is only eta-optimal, add eta. Actually evaluating
or optimizing the utilities still costs computation. Correlation between action
payoffs and hypotheses is not thrown away by storing complete samples.

For n binary hypotheses, all 2^n even-parity predicates are one possible family.
The sufficient record length is O((n+log(1/delta))/epsilon^2), not exponential.
A parity on an arbitrary subset may involve all n variables. This example shows
that 'high-order correlation' does not by itself force quantum storage. It is
an explanatory family, not an assertion that parity is an application target.

If an approximate iid sampler has output law p_tilde with TV(p,p_tilde)<=tau,
the same empirical bounds have bias at most tau for [0,1] queries. A certified
sampling error, statistical error and correctness of the original model are
separate issues. No sample-bank calculation supplies the first two assumptions
about the generator that created it.

## 3. A record can answer many questions while remaining far in total variation

Take 20 initially independent fair bits and condition on even parity in each
of five disjoint four-bit blocks. There are 32768 equally likely posterior
configurations. Every one-bit and two-bit marginal remains the independent
uniform marginal, but each four-bit parity holds with probability one rather
than one half. The probability that all five hold is one, not 1/32.

The posterior is deliberately EASY classically: draw three independent bits
per block and choose the fourth as their XOR. No inference speedup is implied.

We generated iid records and checked all 1,048,576 parity predicates with an
integer Walsh transform. For the fixed seed 2026092608:

  m=1024: maximum parity-probability error 1/16 = .0625;
          empirical total variation 15877/16384 = .96905517578125.
  m=4096: maximum error 41/1024 = .0400390625;
          empirical TV 28915/32768 = .882415771484375.
  m=8192: maximum error 183/8192 = .0223388671875;
          empirical TV 25491/32768 = .777923583984375.

At m=8192, the bit-packed sample labels occupy 20480 bytes. This does NOT
include the diagnostic's large enumeration arrays, metadata, or the cost of
obtaining samples. The record contains 7277 distinct posterior configurations.
The event 'the next x belongs to this observed set' has empirical probability
one but true probability 7277/32768. That sample-adapted event is not one of our
fixed parity predicates. There is no contradiction between small query error
and large TV distance. The Hoeffding sufficient count for all parity predicates
at epsilon=delta=.05 is 3511; the measured maxima are observations, not an
independent validation of the theorem or a portable performance benchmark.

No distribution can be certified globally merely by showing its agreement on
a convenient list of marginals. Conversely, total-variation certification is
unnecessarily strong when the consumer only needs a declared smaller family.
Choosing the consumer's metric is part of the application, not an opportunity
to burden the classical comparator with an irrelevant problem.

## 4. A global certificate through an inverse circuit

Assume explicit preparation circuits A and B on the same padded register space,

    A|0> = |Psi>,     B|0> = |Phi>.

A specified common measurement of their output labels gives p and q. There may
be auxiliary registers, but they remain part of the coherent preparation and
its inverse; they are not silently discarded and restored. The return test
prepares A|0>, applies B^dagger, and checks the all-zero outcome. Its probability is

    F = |<Phi|Psi>|^2.

Measurement contractivity and pure-state trace distance imply

    TV(p,q) <= sqrt(1-F).

Therefore a rigorous lower bound F>=1-tau^2 certifies EVERY expectation of a
function f:X->[0,1] to additive tau. This holds even if phases or purifications
are not aligned. A selected q-optimal decision is at most 2 tau worse under p,
before adding any optimization or Monte Carlo error. The fidelity/distance
facts are established [2]; distribution testing with coherent access is a
substantial pre-existing subject [3,4]. No new generic certificate is claimed.

The simplest finite test is deliberately one-sided: accept only if all m
independent return experiments succeed. For a fixed candidate with TV(p,q)>tau,
its pass probability is at most (1-tau^2)^m. Choose

    m >= ceil(log(delta)/log(1-tau^2)) = O(tau^-2 log(1/delta)).

At tau=.1, delta=.05 this is 299 all-zero returns; at tau=.05 it is 1197.
This bounds false acceptance, not the probability of accepting every good q.
Candidate fitting must precede a fresh validation sample, or multiple/adaptive
attempts need a valid allocation of confidence. A failure is INCONCLUSIVE about
output closeness, as explained below. With noise or approximate A/B, the test
concerns the implemented states; additional errors relative to the stipulated
model have to be bounded separately.

The gate cost is at least m times the cost of A and B^dagger (plus measurement),
not simply m. Access to normalized posterior states is not furnished by a stream
of classical samples. A heralded inference algorithm must pay its success and
reflection/reconstruction costs before it can be treated as a coherent A.
No free QRAM, density table, or efficient posterior preparation is assumed.

## 5. Why the output distributions can agree when the return test fails

If the states are exactly the nonnegative square-root encodings,

    |psi_p> = sum_x sqrt(p_x)|x>,    |psi_q> = sum_x sqrt(q_x)|x>,

then F=(sum_x sqrt(p_x q_x))^2 is classical squared fidelity. This is a useful
special case, NOT automatically the output of reversibly running a sampler.

The same distribution can have incompatible phases: |+> and |-> both generate
a fair bit, yet their overlap is zero. More importantly for explicit generators,
let a fair random tape z be retained. The deterministic generators g0(z)=z and
g1(z)=1-z produce identical output laws. Their reversible states

    (|00>+|11>)/sqrt(2),    (|01>+|10>)/sqrt(2)

are orthogonal. Thus running the inverse of one after the other always fails
the return test, even though their classical outputs are identical.

High return probability is still a sound sufficient certificate. Low return
probability is not proof that a classical surrogate has lost correlations.
Seeking better phase/environment alignment can be an optimization problem
itself; an optimal alignment is not a free oracle. The distinction between
probability access, purified access and square-root state access is explicit
in the existing literature [3,4]. A general same-distribution tester cannot be
replaced by this sufficient return test without a completeness assumption.

For ordinary Bayesian hypotheses, keeping the full coherent execution history
can be easy relative to producing a clean amplitude proportional to the square
root of its MARGINAL probability. Summing over latent executions is exactly the
inference computation we have been auditing. Do not hide it in uncomputation.

## 6. Which classical comparison is legitimate?

Classical sample-only uniformity testing on a D-point domain has a square-root
D sample dependence at fixed separation [5]. A canonical coherent-state
representation can be compared with a known reference through its overlap.
This motivates a distinction between sampling access and coherent access; it
is NOT a proved separation for an explicit public generative program.

Both of our competitors receive the model description. A classical method may
inspect its code, compare exact formulas, exploit graphical structure, compute
likelihood ratios, or provide an application-specific guarantee. For example,
when normalized point probabilities p_x and q_x are efficiently available,
Bhattacharyya overlap can be estimated classically from samples of q using
sqrt(p_x/q_x): its second moment is at most one. This removes a generic
D-dependent sampling argument in that stronger classical access model. The
precision and evaluation costs of that estimator still matter.

Likewise, classical direct samplers and certificates solve the parity example.
We are not selecting it as a hard workload. The purpose of the two checks is
to distinguish 'many useful queries' from 'uniform validity for all queries,'
and to separate a sound certificate from an unjustified complete tester.

## 7. Limits of reuse

Both record guarantees and global TV compare fixed distributions on fixed
labels, at fixed evidence and model assumptions. They do not imply unlimited
future Bayesian conditioning. A rare additional event of probability alpha can
be absent from an m-sample bank with probability (1-alpha)^m. Conditioning can
magnify small distribution errors. In the easy parity example, alpha=1/32768
for one specified full posterior state, and an 8192-sample bank misses it with
probability .7787978121274097. The directly known model can of course answer
that event without the bank.

Neither a good sample record nor high agreement with a specified quantum
model establishes that the model describes real data. Training, model selection,
state preparation, coverage and the usefulness of the later queries stay in
the end-to-end comparison. The target is a useful probabilistic computation,
not necessarily a physical system, but it must have an independently justified
acceptance metric.

## 8. Work performed and next experiment

joint_record_check.py checks the explicit affine posterior and all parity queries.
Small direct parity sums independently verify the integer transform (16512
summands). The large query census is a classical algebra diagnostic, not a
many-qubit simulation. The only quantum readout discussed is not executed.

belief_overlap_check.py constructs dense small preparation matrices and checks return
probabilities on 96 pairs in dimensions 4,8,16. It verifies 192 full/coarse-output
distance bounds, the tight two-outcome F=.99/TV=.1 example, and the phase and
workspace false-negative controls. Largest numerical return-probability residual
is 5.55e-16. These QR-completed matrices are not a scalable preparation algorithm.
Both reports were regenerated; exact fractions/integers are retained where
applicable, floating-point diagnostics need not be portable byte-identical.
No native inference package, learned model, older verifier, or hardware was run.

Reproduce to fresh paths:

    OPENBLAS_NUM_THREADS=1 python exploration/phase_2/joint_record_check.py --output /tmp/record.json
    OPENBLAS_NUM_THREADS=1 python exploration/phase_2/belief_overlap_check.py --output /tmp/overlap.json

Candidate direction: quantum-assisted validation of a reusable classical
probabilistic replacement, retaining the relationships actually needed by its
consumer. This is not yet the project's accepted central contribution. The
next discriminating test must use a genuinely available coherent target and a
classically executable candidate, determine whether a useful alignment is
constructible without solving the original inference problem, and compare with
source-aware classical validation. Do not optimize return gates before resolving
this interface. If only a finite query family is needed, use the cheaper sample
record and do not impose global TV as an artificial obstacle.

## Primary references and inspection scope

[1] W. Hoeffding, Probability Inequalities for Sums of Bounded Random Variables,
JASA 58 (1963), 13-30. DOI 10.1080/01621459.1963.10500830.
https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500830
Publisher abstract checked; the finite-family corollary above is derived here
from the standard inequality, with no claim of new concentration theory.

[2] C. A. Fuchs and J. van de Graaf, Cryptographic Distinguishability Measures
for Quantum Mechanical States (1999), arXiv:quant-ph/9712042.
https://arxiv.org/abs/quant-ph/9712042 . Primary abstract/metadata inspected;
our elementary pure-state bound is also directly tested. This is foundational
mathematics, not a cryptographic application for this project.

[3] A. Belovs, Quantum Algorithms for Classical Probability Distributions
(2019), arXiv:1904.02192. https://arxiv.org/abs/1904.02192 . Primary abstract and
scope inspected for distinctions among access models; no new query lower bound
is transferred to the explicit-program task.

[4] A. Gilyén and T. Li, Distributional property testing in a quantum world,
ITCS 2020; arXiv:1902.00814. https://arxiv.org/abs/1902.00814 . Primary abstract
and author-institute proceedings record checked. Their general property-testing
algorithms are not replaced or claimed improved by our sufficient return test.

[5] L. Paninski, A Coincidence-Based Test for Uniformity Given Very Sparsely
Sampled Discrete Data, IEEE TIT 54 (2008), 4750-4755.
DOI 10.1109/TIT.2008.928987; author-institution abstract:
https://www.columbia.edu/cu/neurotheory/publications.html . Sample-only model
scope checked, no native test or hardness experiment reproduced.

The previous posterior-construction and preparation-cost obligations remain;
this note does not revive the manuscript or assert publication readiness.
