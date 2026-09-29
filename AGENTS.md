# Research continuation contract

## Hardware boundary: fault-tolerant circuits without assumed QRAM

Owner direction, 29 September 2026: scalable fault-tolerant gate-model processors
are acceptable assumptions; fast QRAM is not. This is a firm admissibility
constraint, not a hardware caveat to leave until after deriving a query speedup.
It supersedes earlier permission to select a lead conditional on fast coherent
adjacency-list or quantum-read/classical-write RAM. Preserve those earlier results
as conditional theory with their original assumptions, not as eligible applications.

Use ordinary logical qubits, gates, measurements, resets, classical control and
classical RAM. Logical qubits may retain coherent computational states; that is
not a blanket permission for efficient arbitrary table lookup in superposition.
No specialized QRAM device, unit-cost large coherent data oracle, free arbitrary
amplitude encoding, or cheaply updatable quantum-addressable classical table may
be assumed for either the input or intermediate/output working data.

A reversible formula is allowed only with its actual circuit cost. A table lookup
compiled into an ordinary gate circuit (sometimes called QROM) is not free or
excluded merely by its name: count gates, depth, ancillas, routing, preprocessing,
coefficient precision and updates/recompilation. Do not relabel QRAM as QROM or
hide its cost in a block-encoding/state-preparation oracle. Do not infer a universal
linear lower bound on lookup from the cost of one implementation.

Every candidate must expose classical input -> circuit/state preparation ->
coherent operations -> measurement -> useful output, with ALL data accesses
priced before it becomes an active advantage lead. Symbolic circuit bounds are
enough for initial model-first screening; a specific vendor, near-term device,
full hardware compiler or empirical benchmark is not required. Trapped-ion and
superconducting examples motivate the allowed model, not a platform commitment.

The QRAM-dependent short-seed sparsifier in phase-4 Note 04 is parked under this
constraint. Its reduced randomness storage does not remove point-table, spanner,
resistance or search-bookkeeping access. No continued QRAM design or automatic
QROM retrofit is authorized. Reopen a graph candidate only with a specific ordinary-
circuit construction, fully charged costs and a credible useful comparison.
See [hardware decision 05](exploration/phase_4/NO_QRAM_HARDWARE_BOUNDARY_05.md).

## Model-first exploration for every example

Owner direction, 28 September 2026: focus first on mathematical models and the
possible quantum integration, rather than actual implementation. This changes
the order of investigation, not the requirement for useful and honest science.
It supersedes earlier instructions that make a particular measured dataset,
native installation, or concrete hardware implementation a prerequisite to
initial model-level analysis. Preserve the scientific conclusions of those notes.

For each example, start with a concise mathematical specification: an established
model family and its independently motivated observable; shared classical input
and access assumptions; the required output law and error criterion; a specific
quantum representation and operation; the strongest relevant classical approach;
and the structural parameter regime in which a benefit might survive. Explain
why a quantum operation produces the requested law rather than only something
with a similar name. Distinguish an identity or conditional upper bound from a
separation, a novelty claim, and a demonstrated application improvement.

Use parameterized families before choosing a single demonstration instance.
Derive a limiting case, reduction, error estimate or symbolic cost comparison
that can expose the mechanism or an immediate classical shortcut. A missing file
or unavailable package blocks only the test requiring it, not the investigation.
Do not create a new framework or large toy census merely to fill the gap.

Keep mathematically essential costs visible from the outset: input/preparation
access, normalization, success probability, conditioning, resolution, evolution
time, output size and repeated sampling. Explicitly conditional, symbolic budgets
are acceptable at this stage; free arbitrary state preparation or an unpriced
exponentially large oracle is not. Distinguish best-known classical costs from
proved lower bounds and apply the same useful accuracy to both sides.

Keep a concise primary-source application anchor and physically justified model
assumptions. Model-first does not mean choosing arbitrary difficult Hamiltonians
and attaching a domain label. Full experimental calibration, software integration,
detailed fault-tolerant gate counts and native performance studies come after
there is a credible structural quantum opportunity. Neither a completed advantage
proof nor deployment is required to explore that opportunity. Keep alternative
mechanisms open; a failure in one model or regime is not a universal rejection.

## Current exploratory output contract: direct samples are allowed

On 28 September 2026 the owner proposed direct use of quantum samples, including
probabilistic prediction of chaotic systems. Read
[direct-sampling note 10](exploration/phase_3/DIRECT_SAMPLING_FORECASTS_10.md) and the
live work order. For this investigation, do not require a learned classical
program or quantum-free deployment. Continued quantum sampling is allowed and
must be included in the complete cost. This is an explicit extension of the
original charter, not an assertion that direct sampling met its old condition.
The requirement for useful outputs, accurate claims and strong classical
comparison remains. Manthan profiling is paused, not refuted. No useful direct
sampler or forecasting advantage has yet been established.

## Read the current project, not an old checkpoint

Read the [canonical project map](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/main/PROJECT_MAP.md), README.md, STATUS.md, and
work_orders/CURRENT.md first. The active parent research branch is
`research/prx-quantum-phase2`; the work order on `main` routes to that branch.
Read its phase-2 charter before selecting the next scientific step, subject to
the explicit output-contract extension above.

Quantum-Assisted Algorithm Discovery is one continuing parent exploration. The
independent Algebraic-Loop-Certificates and Sparse-Weil-Reconstruction projects
own their further classical research, software, teaching material, and manuscripts.
Do not automatically resume either spin-off when asked to continue this project.
Neither substitutes for the parent's quantum-discovery objective. This context
may modify only `GoGoKo699/Quantum-Assisted-Algorithm-Discovery`.

The older ledger sections, `docs/current-design.md`, experiment notes, and previous
work orders are historical records. Their uses of "current", "next", or a pending
spin-off creation do not override the project map and active work order. Consult
PROVENANCE.md and the relevant source/experiment documentation before reusing evidence.

## Useful computation before substantial mechanism development

Begin with a documented need that exists outside this project, a concrete useful
output, and a plausible quantum role in obtaining it. Name the workflow,
required quality, deployment interface, and strongest classical alternative.
Do not choose an abstract construction first and attach a broad application label
afterward. A tractable theorem or a small test family is not sufficient evidence
of usefulness. Small models are welcome when they expose a mechanism for the real
problem rather than replace it. Immediate deployment is not required.

The first phase-3 operator candidate is parked for lack of an established
application case. Its finite-precision audit is not the current task. Preserve
its note and checks; revive it only if the same usefulness standard applied to a
fresh candidate is met. This is not a refutation or a new spin-off mandate.

## Physical relevance is a separate requirement

A real molecule or an important application area does not establish that the
chosen geometry, charge state, environment, reaction, or requested accuracy is
important. Separate three claims: the domain matters; the computational model
predicts something useful in that domain; quantum preparation improves the complete
route to that prediction. Evidence for one is not evidence for the others.

Before substantial resource estimation or model development, identify a concrete
physical regime and observable, supported by primary application research. Include
experimental evidence where available, not only quantum-computing demonstrations.
State what the small benchmark omits and how those omissions will be controlled,
tested, or reflected in the scope of the result. A transient intermediate may be
important; it need not be a stable isolable substance. Its relevance must come
from a supported role in the target process, not computational convenience.

A calibration result remains a calibration result until the application connection
is supported. Do not relabel a finite bare cluster as a working battery, a trial
active space as the full electronic problem, or extra energy digits as improved
physical prediction. Compare against the strongest adequate classical workflow
at the same useful output quality, including all preparation and validation costs.
Do not demand unnecessary precision merely to make that workflow fail.

If the physical connection cannot be supported, park or redirect the candidate;
do not rescue it with a more impressive domain label or further toy calculations.
This is not a ban on small models, theoretical work, or honest methodological
benchmarks. Such work alone does not satisfy this parent's application objective.
When explaining a result, say what was established and what remains unestablished
in language the project owner can assess without specialist chemistry knowledge.

## Preserve scientific and comparison boundaries

The original objective is a useful reusable classical output discovered more
efficiently with a circuit-model quantum computer. The current direct-sampling
extension is specified above. No useful quantum advantage is established.
No application or device platform is mandated by earlier experiments.
Manuscript preparation remains on hold.

Retain strong classical deductions and realistic baselines. Treat seed choice,
horizon, initialization, marked-set definition, coefficient domain, readout, and
all access costs as explicit model choices. Verify published claims from primary
sources before relying on them for new research. Attribute standard methods and
public reference certificates. Unit tests, local rediscovery, stored success
frequencies, compactness, or reuse alone are not novelty or speedup evidence.
Do not transfer historical quantum resource counts to a new construction.

## Evidence and execution

Preserve LICENSE, third-party notices, proof notes, source data, manifests, and
reference outputs. Imported files are tracked by provenance/import-manifest.json;
put substantive new work in a versioned successor directory. Do not overwrite
historical evidence to make tests pass or remove it merely to simplify navigation.

For scientific changes, run the applicable verifiers, including `python verify.py`
for its historical scope when applicable, and record what was actually rerun.
For documentation-only changes, check links, branch routing, and the diff; do not
claim an experimental rerun. Use temporary paths for generated data and benchmarks.
Never run assertion-dependent code under -O or -OO.

Keep commits scoped. Update current status and the active work order when evidence
or ownership changes; distinguish new findings from retained historical claims.
Never promise unattended work. No external contact, paid computation, unrelated
branch merge, submission, release tag, or repository administration change is
authorized by this continuation contract.
