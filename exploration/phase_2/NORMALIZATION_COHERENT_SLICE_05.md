# Condition the decisions before generating the object

26 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.
This is a focused integration argument and finite algebra check, not a new
quantum primitive, a classical-hardness result, an LLM benchmark, or a claim
that arbitrary language models have a small coherent interface. It continues
NORMALIZATION_GENERATOR_SPACE_04.md and preserves earlier research unchanged.

## 1. The distinction we needed

A classical model supplying scores after measuring each quantum proposal does
not, by itself, supply a coherent acceptance oracle. For an unstructured hidden
marked label among N labels, an algorithm that receives information only by
classical point queries has success at most min(1,(q+1)/N) after q queries and
one possibly unverified output. A verified hit has probability at most q/N.
Before a hit, the transcript rules out only queried labels. Conditional on that
transcript, the hidden label is uniform among the remaining ones; internal
quantum processing has obtained no further target-dependent information. This
is an elementary black-box statement, not a lower bound on explicit structured
programs or all hybrids. Quantum search [1] uses coherent queries, a stronger
interface. Learned structure or preprocessing changes the information model
and must be priced rather than silently supplied.

The constructive question is therefore whether the coherent query can be much
smaller than the classical program whose output we condition. It can under an
exact, checkable factorization. The critical object is the computation of the
acceptance event, not necessarily the computation producing the whole output.

## 2. Exact causal-slice interface

Fix a bounded, deterministic classical generator g driven by independent uniform
random tapes A in {0,1}^k and R in {0,1}^ell. All other context is fixed. Let
X=g(A,R), and let E(X) be a specified Boolean acceptance event. Suppose we have
an explicit circuit h such that

    E(g(a,r)) = h(a)     for EVERY a,r.

This is an equality of the actual finite generator, not an assertion that a
small semantic summary probably predicts the event. It can follow from a
sound data/control-dependence slice or a proved structural property. A small
output bit alone does not imply a small circuit. Any access to weights, large
constant tables, environment calls or state used to compute h must be included.

Then, writing p=Pr[h(A)=1]>0,

    Law(A,R | E) = Law(A | h(A)=1) times Uniform(R).

Indeed every accepted a has all 2^ell completions, each with the same original
weight. Thus R remains independent and uniform after conditioning. Produce a
uniform accepted a by standard amplitude amplification/search, generate R only
AFTER measurement, and execute g(a,R) classically once. The resulting output law
is exactly Law(X | E). Multiple tapes giving the same output retain their
correct multiplicities; outputs themselves need not be uniformly distributed.

Only the k relevant bits and the reversible workspace of h need be coherent.
Neither the deferred random tape nor the rest of the generator must be part of
the quantum circuit. Ordinary phase-oracle construction computes h, phase-marks,
and uncomputes it. Standard Grover iterations preserve equal amplitudes inside
the accepted set, so the output conditional on verified success is uniform there.
A randomized iteration schedule handles unknown p>0; a bounded run needs a
stated positive lower bound for its success guarantee, or the usual bounded
search for the empty case. No efficiency promise follows for exponentially
small p without retaining the corresponding search cost.

This does NOT say an existing autoregressive LLM can be automatically replaced
by a few semantic qubits. For constraints on the actual generated language, the
acceptance computation may depend on almost every token choice and model call.
A plan-based generator with a proved constraint on the plan is a different,
explicitly structured model unless it is shown to preserve the original law.
External calls cannot be evaluated in superposition for free.

## 3. How the input probability is preserved

Finite biased coins can be implemented from independent uniform bits and exact
threshold operations at a declared finite precision. The slice must retain the
bits and computations needed by those operations. Correlated nonuniform inputs
cannot just be declared independent after a convenient split. Variable-length
or nonterminating generators need additional treatment; the statement here is
for a fixed bounded tape and terminating execution.

The independence condition concerns ACCEPTANCE, not the output itself. The
unobserved output may depend strongly on both A and R. We replay g with the
conditioned A and fresh R, preserving those output correlations. The expensive
completion is deferred, not approximated or fabricated by another generator.

Syntactic probabilistic program slicing and specification-based refinements are
established prior work [2,3]. The elementary product factorization here does not
claim to cover their full control-flow/termination theory or compute a minimal
slice. A compiler that finds a sound conservative slice is sufficient for
correctness, although it may give no resource reduction. Source inspection and
slice validation are classical setup costs for BOTH competitors.

## 4. What cannot be frozen classically

Suppose the event is genuinely h(a,r), rather than h(a). Drawing r from its
original law and independently conditioning a within each fixed r is usually
wrong for the JOINT conditional task. Let

    p_r = Pr_A[h(A,r)=1].

The correct posterior of r is proportional to Pr(R=r)*p_r. Completing every
chosen r successfully erases these relative evidence weights. If r is supplied
external context rather than a latent quantity to infer, conditioning on that
fixed r is a different and legitimate task.

Exact control: R is one unbiased bit, A is three unbiased bits. For r=0 accept
only a=0; for r=1 accept a=0,...,6. Both conditional subproblems are nonempty.
The correct R posterior is (1/8,7/8). First choosing R uniformly and perfectly
solving the corresponding inner conditional problem gives (1/2,1/2). Their
joint laws are at TV distance 3/8. Even an ideal inner quantum routine does not
repair that incorrect outer distribution. This is Bayesian factorization, not
a newly discovered quantum limitation.

A general sufficient interface can instead carry the required conditional
likelihoods, but computing them may be the original hard problem. A guessed
surrogate or a truth table of precomputed full-generator evaluations is not an
unpriced interface. The safe route used here is to retain ALL relevant random
choices coherently and defer only those proved irrelevant to the event.

## 5. Fair end-to-end cost

Let C be the classical cost of evaluating the small slice, Q the full coherent
iteration cost (including reflection, uncomputation and input operations), and
D the cost of one accepted classical completion. Costs must be compared using
a stated resource model, not equating a Toffoli to a CPU instruction. With
classical and quantum setup costs A_C,A_Q, the simple matched rejection bounds are

    T_C = A_C + O(C/p) + D,
    T_Q = A_Q + O(Q/sqrt(p)) + D.

The classical baseline must also postpone the irrelevant completion. Comparing
Q/sqrt(p)+D with (C+D)/p would give the classical algorithm an avoidable burden.
D includes drawing the deferred random choices and constructing/reading the
required output. Enlarging D does not strengthen quantum advantage; it can make
both total times effectively equal. Reuse of a compiled slice can amortize setup
on BOTH sides, not only on the quantum side.

These formulas compare with sliced rejection, NOT with optimal classical
inference. Exact counting, factorization, tractable graphical structure,
compiled decision diagrams, SAT-based almost-uniform sampling, importance
sampling, and good conditional proposals remain competitors. A low p alone is
not classical hardness. Nor is slow computation of a full posterior table the
right comparison if one adequate sample is all that is required.

Quantum rejection sampling with explicit Bayesian-network compilation is prior
work [4]. Quantum weighted constrained sampling is also prior work [5]. Our
factorization plus [1] is a standard-method combination, not by itself a PRX
Quantum contribution. Its value here is resolving when an entire classical
model need not be evaluated coherently, and precisely where that statement fails.

## 6. A strong classical counterweight already exists

Pluck [6] exploits lazy evaluation for exact knowledge compilation and for a
sequential Monte Carlo construction with locally optimal proposals. The authors
provide code and a PLDI 2025 artifact. Its approach already avoids evaluating
unnecessary random choices and already breaks inference into subproblems. We
inspected the primary paper abstract and project description, not its full
implementation or numerical benchmarks. No performance number is used here.

This gives a concrete comparison agenda: the potential quantum kernel is the
remaining constrained-sampling problem after equally strong laziness/slicing,
not the entire program space before those deductions. Candidate-test circuit
size and full posterior-compilation size are different, but a large diagram is
not a lower bound against other classical methods. Do not pick an unfavorable
variable order or a weak solver to manufacture the residual bottleneck.

For a first genuine application, seek a public probabilistic generator whose
acceptance slice is small enough for explicit coherent evaluation, while current
classical conditional sampling of that slice still expends substantial effort.
The required output distribution or decision quality must be justified by its
consumer, not chosen only to make sampling harder. Language is one possibility,
not the default or a boundary. No such positive workload is established here.

## 7. Exact finite check actually run

coherent_slice_check.py uses only Python's standard library and exact fractions.
A toy generator has eight random bits. Its event depends on four through

    h(a,b,c,d) = (a AND b) XOR (c AND d).

Six of sixteen core labels pass. The other four bits change the output but not
acceptance. All 256 full tapes were enumerated. One simulated Grover iteration
has success 27/32; conditional on success its six labels are exactly uniform.
Classically completing the other four bits reproduces the exact conditional
output law, including its nonuniform many-to-one multiplicities, at TV error 0.
A compute-phase-uncompute marker was checked on all sixteen input basis states
with two clean work bits. This is not a full reversible compiler or gate count.

The same toy has a direct classical sampler with no rejection: choose which
pair is 11, then choose the other pair uniformly from 00,01,10. This sampler is
also checked. The example therefore validates semantics, not quantum advantage.
The context-freezing counterexample in Section 4 is checked exactly as well.
No LLM, trained model, native inference package, large solver or quantum hardware
was run. Historical experiments and their verifiers were not rerun.

Reproduce to a new path:

    python exploration/phase_2/coherent_slice_check.py --output /tmp/slice-results.json

Existing files are not overwritten. Outputs are deterministic exact fractions.

## 8. Decision

The constructive mechanism is: condition a sufficient set of decisions coherently,
then realize the full classical object only once. It replaces neither the target
model nor its score with an assumed cheap approximation. The remaining task is
to find an independently useful hard kernel that survives strong classical
inference and whose reversible evaluation is affordable.

Do not start a general compiler or claim an LLM benefit from this toy. Do not
revive the manuscript. The next finding should decide whether such a kernel
exists in a specific externally motivated generator, or whether a different
quantum mechanism is needed. Simplicity is a constraint on the explanation, not
permission to omit the exact factorization or comparable classical preprocessing.

## Primary sources

[1] Brassard, Hoyer, Mosca, Tapp, Quantum Amplitude Amplification and Estimation
(2000/2002). https://arxiv.org/abs/quant-ph/0005055 . Primary theorem summary read;
standard quantum tool, no new speedup law claimed.

[2] Amtoft and Banerjee, A Theory of Slicing for Probabilistic Control-Flow Graphs
(expanded 2017 preprint of FOSSACS 2016 work).
https://arxiv.org/abs/1711.02246 . Primary abstract/scope inspected.

[3] Navarro and Olmedo, Slicing of Probabilistic Programs Based on Specifications
(2022). https://arxiv.org/abs/2205.03707 ; DOI 10.1016/j.scico.2022.102822 .
Primary abstract and published summary inspected; no native implementation run.

[4] Low, Yoder, Chuang, Quantum Inference on Bayesian Networks, PRA 89,062315
(2014). https://arxiv.org/abs/1402.7359 ; DOI 10.1103/PhysRevA.89.062315 .
Primary abstract and explicit-operation claim inspected. Its comparison is not
a proof against every classical inference method.

[5] Riguzzi, Quantum algorithms for weighted constrained sampling and weighted
model counting, Quantum Machine Intelligence 6,73 (2024).
https://doi.org/10.1007/s42484-024-00209-5 . Published abstract/conclusion inspected;
black-box complexity statements are not imported as explicit-program hardness.

[6] Bowers, Lew, Tenenbaum, Solar-Lezama, Mansinghka, Stochastic Lazy Knowledge
Compilation for Inference in Discrete Probabilistic Programs, PACMPL 9,PLDI,222
(2025), DOI 10.1145/3729325. Primary MIT repository abstract and project description
read: https://hdl.handle.net/1721.1/164737 ; https://pluck-lang.github.io/ .
Artifact located at https://zenodo.org/records/15377922 but not executed.
