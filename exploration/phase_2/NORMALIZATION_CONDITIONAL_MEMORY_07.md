# Conditional memory: the cost is in dependencies, not the number of histories

26 September 2026. Phase 2; target PRX Quantum; manuscript stays on hold.
This is a source-led mechanism audit and exact finite calculation. No new
quantum algorithm, inference-speed claim, trained model, or native Pluck run
is established. It continues NORMALIZATION_MODEL_EVIDENCE_06.md.

## 1. A genuinely coupled public program

The pinned Pluck program [1] has a binary hidden Markov chain with initial
probabilities (1/2,1/2), row-stochastic transition matrix

    A = [[2/5,3/5],[3/5,2/5]],

and observation-True probabilities (2/5,9/10). Its query asks for the eleventh
hidden state conditioned on the first fifty observations all being True; another
query requests a sample of the complete fifty-state hidden sequence.
The choices are coupled across time. This is not the independent-emission
source-kernel calibration of the preceding note.

Our exact forward-backward calculation gives

    P(50 True observations) = 1.2624840248137385e-10,
    P(X_11=True | all 50 observations) = 0.6338219329206618.

Conditioning only on the first eleven observations instead gives
0.6636916625343868. Future evidence matters. There are 2^50 hidden histories,
but their weights need not be enumerated: a two-entry boundary message suffices
at each time. Forward and backward recurrences each contain 196 transition
terms. These counts are not CPU timings; exact rational bit lengths grow with
sequence length. Native Pluck and its execution semantics were not reproduced.

Plain rejection would require about 7.92e9 full trials per accepted history.
The scale 1/sqrt(p) is about 88999 for whole-history amplitude amplification,
not a gate count or a lower bound on all quantum inference. Direct classical
conditioning is polynomial and is the appropriate comparator.

## 2. The posterior is another small generator

For fixed observations y_1,...,y_T, let

    b_t(x) = P(y_(t+1:T) | X_t=x),     b_T(x)=1.

If e_y(x) is the emission likelihood, backward recursion gives

    b_t(x)=sum_z A[x,z] e_(y_(t+1))(z) b_(t+1)(z).

Then the initial distribution and transition rows of a conditioned generator are

    q_1(x)=pi(x) e_(y_1)(x) b_1(x) / P(y_1:T),
    Q_t(z|x)=A[x,z] e_(y_(t+1))(z) b_(t+1)(z) / b_t(x).

Every row sums to one. Products telescope to the exact posterior probability
of each complete hidden path. Rows with zero b_t are unreachable and can be
assigned arbitrary normalized transitions; the present source has no such rows.
Sampling this generator does not reject any generated path. Computing and
storing its messages is classical setup; both competitors may use it. These
are standard forward-backward/conditioned-Markov formulas, not new methods.

The positive square-root state of the full posterior also has Schmidt rank at
most two across each temporal cut. Its amplitude factors through the binary
boundary state. For S-state HMMs the corresponding bound is S. This is an
elementary factorization, not a general theorem that all small quantum states
can be prepared efficiently: here the factors and their normalization can
actually be computed. Different variable orderings can give different ranks.

## 3. Normalization is not a free Bayesian update

Suppose a prior is represented as |psi_p>=sum_x sqrt(p_x)|x>. For likelihood
l_x in [0,M], a coherent flag operation can implement

    |x>|0> -> |x>(sqrt(l_x/M)|1>+sqrt(1-l_x/M)|0>).

Conditioning on flag 1 gives the desired posterior amplitudes. The success
probability is Z/M, where Z=sum_x p_x l_x. Constructing the flag requires the
stated coherent likelihood circuit; this is not automatically supplied by a
classical point-query service or a stochastic program's output samples.

The successful map on the label register is a nonunitary filter. For unequal
strictly positive likelihoods, it cannot be a single fixed deterministic unitary
acting correctly on every unknown sqrt-prior state: pure basis priors must stay
in the same basis labels, forcing such a unitary to be diagonal up to phases,
whereas a superposed prior must change its relative magnitudes. A unitary
TAILORED to a known prior can prepare the posterior, but calculating/compiling it
can be the inference task. Ancillas, measurements, restart/amplification and
other structured algorithms must be costed rather than omitted.

Sequentially conditioning a complete forward execution and requiring every
observation still has the original total evidence probability. A different
algorithm need not pay this cost. However, writing one separately normalized
formula per time step does not by itself construct the needed coherent
reflections or eliminate rejected runs. Wiebe and Granade [4] already establish
limitations of generic black-box quantum Bayesian updating and discuss
approximate alternatives. No universal new impossibility claim is made here.

Harrow and Wei [5] provide adaptive quantum simulated annealing for Bayesian
inference and partition functions. Such methods use controlled transitions,
intermediate distributions, overlaps and Markov-chain gaps rather than requiring
literal reproduction of the whole dataset. They are a positive established
alternative, not a ready advantage for this public HMM or a free normalizer.

## 4. Where a nontrivial computational question can survive

For several hidden processes with a shared observation, the transitions may
factor while the POSTERIOR does not. In a factorial HMM with M binary chains,
a general exact boundary message can have 2^M entries. This describes a standard
exact representation, not a lower bound against every classical algorithm.

The simplest example is two independent fair bits with the observation that
exactly one is one. Both posterior marginals remain 1/2, but the posterior joint
law is concentrated on (0,1),(1,0). Replacing it by the product of its marginals
has total-variation error 1/2. The example is classically trivial: Gaussian
elimination or direct enumeration resolves it. It demonstrates lost relational
information, not a hard instance or an application need for global parity tests.

The research question is whether quantum processing can preserve and interrogate
application-relevant correlated uncertainty more cheaply than adequate classical
inference, AFTER the model's exact and approximate decompositions are used.
Representing 2^M amplitudes with M qubits does not prove efficient preparation,
updating, recovery after measurements, or useful readout. Requiring the whole
joint distribution when the consumer needs a local marginal would create an
artificial burden for the classical side.

The best comparator is not a dense 2^M by 2^M transition matrix. Specialized
FactorialHMM algorithms [2] exploit independent transitions and avoid the naive
quadratic-in-joint-state-count cost. Ghahramani and Jordan [3] already proposed
variational and sampling approximations. Rimella and Whiteley [6] establish
local approximation guarantees whose bounds need not grow with overall model
dimension under their conditions, and demonstrate a passenger-flow application.
The local guarantee is not automatically a global-joint guarantee, but it may
already answer the actual consumer's question adequately.

For comparing executable explanations, classical learned likelihood-ratio or
posterior surrogates are also allowed. Brehmer et al. [7] use latent information
from simulators to improve those surrogates. Not evaluating exact likelihoods
is a legitimate classical strategy when calibration and prediction requirements
permit it. Training cost and generalization requirements apply to both sides.

## 5. Scope of the calculation

conditional_message_check.py uses only fractions.Fraction and standard-library
code. It checks all 254 binary observation sequences of lengths 1 through 7,
all 21844 associated hidden-path probabilities, 1538 smoothing marginals, and
640 temporal boundary factorizations. Direct path summation agrees exactly with
the forward-backward calculation and with the complete conditioned generator.

The length-fifty source query is evaluated by exact rational messages, not by
enumerating 2^50 histories. The two-bit joint-dependence control and small
likelihood-filter examples are also exact. No factorial-HMM package, native
Pluck, LLM, quantum circuit, quantum hardware, or runtime advantage was tested.
No historical verifier was rerun in this scout. The report is reproduced exactly
in the same Python environment; ratios are stored as fractions and rounded
decimals only aid presentation.

    python exploration/phase_2/conditional_message_check.py --output /tmp/messages.json

Existing output files are never overwritten.

## 6. Decision

Do not attach a quantum likelihood oracle to this easy HMM. It is a necessary
calibration against a misleading 2^T history count, not a surviving workload.
Do not declare all inference easy from it either.

The next positive mechanism should target a small explicit coupled latent model
where the required correlated query resists strong classical messages,
approximation and amortization, and where the COMPLETE quantum inference can
be priced. A factorial model is a concrete family to examine, not a commitment
or a claim that an exponentially large classical table is unavoidable.

The simple question is: can a quantum machine retain useful relationships among
hypotheses through conditioning without paying the cost of explicitly tracking
them classically? The answer is not supplied by normalization alone. The generic
update obstruction and the standard positive quantum alternatives must inform
the choice. Keep the broad exploration open; no manuscript revival or venue
change follows from this note.

## Sources and inspection scope

[1] pluck-lang/Pluck.jl, commit 2ac3400e24d7fa67d87f3ef43265bda2f311e1bc,
programs/hmm.pluck, blob 644473d86d870fece95850b07bfc88bafb78fd4e.
https://github.com/pluck-lang/Pluck.jl/blob/2ac3400e24d7fa67d87f3ef43265bda2f311e1bc/programs/hmm.pluck
Read through GitHub. Mathematical parameters transcribed; no source code imported.

[2] R. Schweiger, Y. Erlich and S. Carmi, FactorialHMM: fast and exact inference
in factorial hidden Markov models, Bioinformatics 35(12),2162-2164 (2019).
https://doi.org/10.1093/bioinformatics/bty944 . Publisher full HTML inspected;
no native code or results reproduced.

[3] Z. Ghahramani and M. I. Jordan, Factorial Hidden Markov Models, Machine
Learning 29,245-273 (1997), DOI 10.1023/A:1007425814087.
https://mlg.eng.cam.ac.uk/zoubin/zoubin/fhmmML.abstract.html . Author abstract read.

[4] N. Wiebe and C. Granade, Can small quantum systems learn?, Quantum
Information and Computation 17,568-594 (2017), arXiv:1512.03145.
https://arxiv.org/abs/1512.03145 . Primary abstract and publisher metadata checked;
no theorem-specific new lower-bound transfer asserted.

[5] A. W. Harrow and A. Y. Wei, Adaptive Quantum Simulated Annealing for Bayesian
Inference and Estimating Partition Functions, SODA2020, arXiv:1907.09965v2.
https://arxiv.org/abs/1907.09965 . Primary abstract inspected for algorithm scope;
no implementation or application-specific mixing bound supplied.

[6] L. Rimella and N. Whiteley, Exploiting locality in high-dimensional factorial
hidden Markov models, JMLR23 (2022),1-34, arXiv:1902.01639v3.
https://arxiv.org/abs/1902.01639 . Abstract-level guarantee and application scope;
not a reproduced benchmark or a claim that its assumptions hold universally.

[7] J. Brehmer, G. Louppe, J. Pavez and K. Cranmer, Mining gold from implicit
models to improve likelihood-free inference, PNAS117,5242-5249 (2020).
https://arxiv.org/abs/1805.12244 ; DOI10.1073/pnas.1915980117.
Primary abstract inspected for classical comparator capabilities; no native run.
