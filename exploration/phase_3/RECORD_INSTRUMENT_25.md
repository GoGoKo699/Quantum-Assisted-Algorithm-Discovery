# Record instrument 25: simulate the counts and the state that produces the next count

29 September 2026. Live baseline: `092b2828d2904045923ac2bf72266d00383bf56e`.
Branch: `research/prx-quantum-phase2`. Manuscript preparation remains on hold.

**Outcome:** an explicitly monitored local splitting method samples a prescribed
finite-time photon-count record with a whole-record TV guarantee. The proof lifts
the dynamics to counters before approximation, so it also controls the remaining
conditional system state. A two-emitter coherent control has a certified dark-event
discrepancy from a population-rate reduction. Exact classical conditional-state
propagation still solves that control. No many-body advantage, experimental
validation, novel general simulation method, or new repository is claimed.

The live [Note 24](SAMPLING_REGIME_DECISION_24.md) opened this mechanism. Its content
and work order differ from the attached local same-numbered spectral-cache note,
which proposed an XX-chain comparison. Both were inspected; neither was overwritten
or silently conflated. This checkpoint follows the live work order. Earlier
spectral constructions and their qualifications remain preserved references.

## 1. Fix the physically defined output

For n two-level emitters on an explicitly supplied bounded-degree graph, use

$$
H=H_x+H_z,\quad H_x=\sum_i\Omega_i S_i^x,\quad
H_z=\sum_{\langle ij\rangle}V_{ij}S_i^zS_j^z,\quad
J_i=\sqrt{\kappa_i}\,|g\rangle_i\langle e|,
$$

with nonnegative decay rates. In the ordered basis (g,e),
$S^z=(|e\rangle\langle e|-|g\rangle\langle g|)/2$ and
$S^x=(|g\rangle\langle e|+|e\rangle\langle g|)/2$.
This is the dissipative transverse-field Ising model used to study emission
activity and intermittency [1]. The local zero-temperature Markov reservoir,
finite-range interactions, and ideal site-resolved counting are model assumptions,
not assertions that every Rydberg device implements this exact instrument.
A finite product initial state is supplied; no stationary state or free burn-in.

Choose detector-bin width Delta, integer bin count L, and horizon T=L Delta.
For each site and each bin output the photon count, or a declared saturated label
0,1,...,K-1,>=K. Saturation is a common deterministic map of both record laws,
not dropping high-count outcomes or renormalizing them away. Within-bin event
ordering/times are not part of this particular output. The diagnostic uses K=2.
Changing detector resolution or labels would change the task.

An important downstream bounded statistic is the probability of a dark interval
(no detected photons), followed by a bright interval (at least one). The model's
stationary large-deviation phase claims are NOT asserted for this finite transient
experiment. If only this scalar is needed, direct classical evaluation is permitted;
requiring the production of all histories would be an artificially stronger task.

## 2. Add counters to the generator before applying a product formula

Let c be the vector of current-bin counts, and rho_c its unnormalized conditional
system state. The exact number-resolved master equation is

$$
\dot\rho_c=-i[H,\rho_c]-\frac12\sum_i\{J_i^\dagger J_i,\rho_c\}
+\sum_i J_i\rho_{c-e_i}J_i^\dagger.
$$

A missing negative-count term is zero. Its Dyson expansion is the usual quantum-
jump law, integrated over all ordered event times that have those counts [2].
At a detector boundary retain the classical count, reset the current counters,
and continue with the conditional system state. This defines an instrument
(channel to record plus remaining state), not just the unlabelled master equation.

For proof one may attach an integer shift register to every jump:
$\widetilde J_i=J_i\otimes T_i$, where $T_i|c_i\rangle=|c_i+1\rangle$.
The resulting bounded Lindblad generators act on system plus counters, and an
initial zero counter stays in nonnegative counts. Alternatively, use finite
saturating counters with jump Kraus terms for every count-to-next-count transition;
at saturation further jumps still update the system. Neither proof register must
be stored coherently by the implementation below.

Write the lifted generator as

$$
\mathcal A=-i[H_x,\cdot],\qquad \mathcal B=-i[H_z,\cdot],\qquad
\mathcal D=\sum_i\widetilde{\mathcal D}_i.
$$

All three generate CPTP maps, also with arbitrary reference systems present.
Different local damping generators commute because they act on distinct
site/counter pairs. The drive terms commute with each other, and all ZZ terms
commute with each other. This remains true for saturated records.

A density-channel bound after erasing the counters would not suffice. The lifting
is what permits record accuracy to follow from channel accuracy without changing
the measured unraveling. It is a specialization of established product-formula
and quantum-trajectory methods [2-5], not a new general framework.

## 3. Explicit quantum step

Let h=Delta/r with integer r>=1. Each substep applies, in order:

1. All one-spin rotations generated by H_x for time h.
2. All ZZ rotations generated by H_z for time h.
3. Each site's exact amplitude-damping instrument for time h, record the outcome,
   and reset the ancilla, WITHOUT resetting the other system qubits.

Thus the lifted substep is
$\mathcal S_h=e^{h\mathcal D}e^{h\mathcal B}e^{h\mathcal A}$.
For site i its last operation has Kraus operators

$$
A_{i,0}=|g\rangle\langle g|+e^{-\kappa_i h/2}|e\rangle\langle e|,
\qquad A_{i,1}=\sqrt{1-e^{-\kappa_i h}}|g\rangle\langle e|.
$$

A ground ancilla, a controlled Ry rotation, and a controlled system flip implement
$|e,0\rangle\mapsto e^{-\kappa_i h/2}|e,0\rangle+
\sqrt{1-e^{-\kappa_i h}}|g,1\rangle$, with $|g,0\rangle$ unchanged.
Measure the ancilla and accumulate its bit in the current detector bin. One
ancilla can be reused sequentially, or n ancillas can operate in parallel. Every
branch is retained; no rejection, amplitude amplification or postselection is used.

The step is EXACT for the stated split instrument. Its approximation to continuous
simultaneous drive/interaction/decay is bounded next. Different substep records are
forgotten only after updating and retaining the conditional system state. That
coarse-graining reproduces the split coarse instrument, not a freshly reset state
at each count. There can be multiple emissions from a site during one detector
bin because the r substeps allow repeated excitation and emission.

## 4. A whole-record bound with local rather than global-square constants

Define the explicit nonnegative rate-squared quantity

$$
\begin{aligned}
\mathcal C={}&\sum_{\langle ij\rangle}|V_{ij}|(|\Omega_i|+|\Omega_j|)
 +4\sum_i|\Omega_i|\kappa_i\\
 &+2\sum_{\langle ij\rangle}|V_{ij}|(\kappa_i+\kappa_j).
\end{aligned}
$$

For ideal primitives and the same initial state, the exact and split instruments
for the ENTIRE L-bin record and final quantum state obey

$$
\boxed{\tfrac12\|\mathcal I_T-\widetilde{\mathcal I}_{T,h}\|_\diamond
\leq \min\{1,\mathcal C T h/4\}.}
$$

Tracing the final system gives the same upper bound on record TV. Any common
saturation, detector-label coarsening, or other classical postprocessing contracts
it. Any statistic f of the record in [0,1], including a joint dark/bright event,
has expectation error at most that TV. Unbounded count moments require a tail
bound or a bounded/capped observable; they do not follow from TV alone.

### Proof

For bounded CPTP semigroup generators X,Y, differentiating
$e^{(h-s)(X+Y)}e^{sX}e^{sY}$ and integrating the inner commutator gives

$$
\|e^{h(X+Y)}-e^{hX}e^{hY}\|_\diamond
\leq\tfrac{h^2}{2}\|[X,Y]\|_\diamond.
$$

All intervening evolutions have diamond norm one, so there is no artificial
$e^{h\|X+Y\|}$ factor. Applying this identity twice bounds the three-factor error
by $h^2/2$ times the sum of the A/B, A/D and B/D commutator norms.

A drive generator at site i has norm at most $|\Omega_i|$; an edge generator has
norm at most $|V_{ij}|/2$; a lifted decay generator has norm at most $2\kappa_i$.
The last estimate follows from a jump-map norm $\kappa_i$ and an anticommutator
norm at most $\kappa_i$, regardless of the counter size. Disjoint terms commute.
Using $\|[X,Y]\|\leq2\|X\|\|Y\|$ only for intersecting terms gives precisely
$\mathcal C$. Multiplication by the half-diamond convention gives
$h^2\mathcal C/4$ per step. Telescoping over T/h steps, retaining reference and
past-record registers, proves the result. Moving completed bins to the output and
resetting only the counters are common CPTP operations and do not increase it.

For uniform Omega,V,kappa and m graph edges,

$$
\mathcal C=2m|\Omega V|+4n|\Omega|\kappa+4m|V|\kappa.
$$

At bounded degree it is linear in n for fixed rates. This is a sufficient
first-order upper bound, not optimal step complexity or a new Lindblad-simulation
lower bound. The all-size guarantee follows from the proof, not the small checks.

### Finite representation and nonideal operations

For a prescribed saturated record the theorem already includes every multi-photon
outcome, including emissions after saturation. No event-count-tail approximation
is used. If unsaturated counts are wanted with finite overflow storage, total
emissions have predictable intensity at most $\sum_i\kappa_i$ and are dominated
by a Poisson count of mean $T\sum_i\kappa_i$. That supplies a separate optional
storage-tail budget. Exact continuous times and bin counts are different laws;
endpoint timestamps are not close in continuous-TV to an absolutely continuous
point process. We claim only the agreed bins.

Let epsilon_0 be initial-state trace-distance error and eta_l the half-diamond
error of primitive l, including its measured record. A sufficient total bound is

$$
\epsilon_{\rm rec}\leq\epsilon_0+\mathcal C T h/4+
\sum_l\eta_l+\epsilon_{\rm classical\ output},
$$

capped at one. Rotation angles, finite precision, coefficient input and output
arithmetic are included here. Independent inefficiency can be implemented by
thinning every internally generated emission BEFORE count saturation; keep the
emission's system update even when its detected label is lost. The same
postprocessing contracts record error. Detector dead time, jitter, feedback or
non-Markov reservoirs require their own specified instrument and are not included.
The fixed-horizon product-state problem has no unpriced stationarity assumption.

## 5. Symbolic cost and the appropriate classical comparator

For allocation epsilon_disc, it suffices to take

$$
r=\max\{1,\lceil\mathcal C T\Delta/(4\epsilon_{\rm disc})\rceil\},
\qquad N_{\rm step}=Lr.
$$

The method needs n system qubits plus one recycled ancillary qubit if sequential,
and O((n+m)N_step) ideal local one-/two-qubit primitives and O(n N_step)
measurements/resets. This is a symbolic local-gate budget, not a fault-tolerant
count, hardware time, or a new efficiency theorem for open systems [3,4]. Precision
synthesis multiplies the primitive count as required. The retained output has
nL capped counters, or can be streamed. Each fresh trajectory restarts the initial
state; M independent target histories multiply its cost by M. Caching follows
Note 24's approximate-law versus fresh-information distinction.

At bounded degree and local rate bound Lambda, this simple bound scales as
$O[n(T/\Delta+n\Lambda^2 T^2/\epsilon_{\rm disc})]$ before precision factors.
Higher-order or specialized methods may improve it. A coarse detector need not
force h=Delta: arbitrarily many internal steps may be summed into the SAME bins.

The strongest elementary classical implementation is NOT a $4^n$-entry density
matrix. Quantum-jump algorithms propagate one $2^n$-entry conditional pure state
under $H_{\rm eff}=H-i\sum J_i^\dagger J_i/2$, sample jump times and labels,
apply the jump, and continue [2]. Sparse local actions cost O((n+m)2^n) arithmetic.
One can also classically execute this very split instrument with state vectors,
incurring that state-size factor per layer. Event-driven algorithms may skip many
empty steps and must be allowed; they are not forced to follow the quantum grid.
Tensors, clusters, symmetries, low-excitation sectors and hidden-state samplers
can reduce cost. Their adequate rank/size here is NOT established to be large.

Ordinary records need no rare-event postselection quantumly or classically.
Both can estimate a fixed event with the usual sampling variance. If the consumer
only needs a few event probabilities, it may be cheaper to propagate a no-count
or tilted generator directly; full records are not mandatory for that consumer.
A large history alphabet, antibunching or full-vector entanglement proves no
useful separation. The possible quantum role is economical conditional many-body
state propagation between the actually requested outputs, if it survives these
classical reductions and all accuracy costs.

## 6. A finite coherent test in the OUTPUT law

Consider two coupled emitters, Omega=V=kappa=1, initially gg, with two bins of
width 2. All times are in inverse-decay units. This is a simple coherent-interaction
control, not a new physical device, phase diagram, large-n scaling fit or hard
instance. Six exploratory parameter choices were evaluated privately before
retaining the equal-scale choice; no parameter-optimization benefit is claimed.

For a dark interval define the no-detected-jump map
$\mathcal N_t(\rho)=e^{-iH_{\rm eff}t}\rho e^{iH_{\rm eff}^\dagger t}$,
and let $S(t)=\operatorname{Tr}\mathcal N_t(\rho_0)$.
Then the event 'first bin dark, second bin bright' has probability S(2)-S(4).
It is one bounded event of the same binned physical records, with no conditioning
on a rare successful run.

A usual population adiabatic elimination gives local stimulated flip rate

$$
w_i(z)=\frac{\Omega_i^2\Gamma_i}{2(\Gamma_i^2+\Delta_i(z)^2)},\quad
\Delta_i(z)=\sum_j V_{ij}z_j,\quad z_j=\pm\tfrac12,
$$

and spontaneous decay kappa_i. Here Gamma_i=kappa_i/2 plus any separately included
pure-dephasing coherence rate. Setting the coherence derivative to zero derives
the formula. Such rate descriptions have a controlled motivation in a fast
coherence-decay/weak-drive limit [6], NOT uniformly at Omega~V~kappa. We explicitly
test the extrapolation rather than assert it should be exact.

| Model | Dark then bright probability |
|---|---:|
| Exact interacting two-emitter dynamics | 0.42439280916 |
| Population-rate reduction, same Omega,V,kappa | 0.30266450416 |
| Exact independent emitters, V set to zero | 0.47877173795 |

The first-versus-second event difference is rigorously greater than
0.121728304996, and therefore lower-bounds full-record TV. The exact proof uses
rational Taylor polynomials for the four-dimensional no-jump amplitude propagator
and the four-state classical no-emission generator. Norm-based remainder bounds
are included; this witness does not depend on floating eigenvalues.

Across the four binary records (DD,DB,BD,BB), the exact interacting probabilities
are (0.11324257,0.42439281,0.10604592,0.35631871). The population-model TV is about
0.1217283; the independent-emitter model differs by about 0.0925813. These latter
complete-vector numbers are floating diagnostics. Independent coherent emitters
have exact small renewal samplers, so non-Poisson fluorescence alone is not a
quantum opportunity. Setting V=0 is a comparator, not the same Hamiltonian.

Adding pure dephasing of coherence rate 4 or 20 gives record differences about
0.02446 and 0.001806 from the corresponding rate model in two fixed controls.
Those are DIFFERENT physical models, not a dephasing operation granted free on
the target. They illustrate the intended classical limit; no convergence theorem
is inferred from two points. The cited strong-dephasing results have their own
Rydberg-model assumptions and are not a theorem for this exact finite control.

Most importantly, exact classical two-emitter conditional-state propagation
reproduces the reference at negligible research-scale cost. The witness excludes
one rate approximation in its uncontrolled regime; it does not establish any
classical hardness or that collective intermittency is present in this small system.

## 7. Executed instrument checks and decision

The independent checker constructs the exact two-site saturated counting generator
for labels 0,1,>=2 per emitter per bin. Two bins have 81 possible record words.
It retains post-overflow jumps in the system dynamics and checks the exact local
amplitude-damping instrument against the lifted decay semigroup.

For 16,32,64,128 internal steps per bin, the observed full-record TV errors of the
split method are respectively 0.0247878, 0.0123222, 0.00614229, 0.00306634.
These are fixed finite diagnostics, not asymptotic timing or large-n observations.
Choi matrices of the record-plus-final-state instrument also provide numerical
lower/upper diagnostics on its half-diamond error, with the correct input-dimension
factor. The proven all-size commutator bound is much looser (and initially trivial).
No numerical SDP or claim of exact diamond-norm evaluation is made.

The probability that some emitter emits at least twice in the first bin is about
0.0165283. Thus a model that silently caps the actual physics at one emission per
site per DETECTOR bin would omit a real outcome. Saturated >=2 labels preserve it.
The common coarsening of the 81-word law agrees with separately evaluated dark maps.

The final checker ran twice with identical JSON and rejected -O/-OO and six invalid
inputs. The rational witness uses degree-128 Taylor bounds and is distinguished
from complex128 matrix exponentials at diagnostic tolerance 5e-10. No sampled
quantum shots, native trajectory package, tensor algorithm, laboratory data,
large-system simulation or performance benchmark was used. Historical verifiers
were not rerun; no upstream code or experimental arrays were imported.

**Decision:** the monitored sampling mechanism has an explicit law-preserving
quantum integration with complete finite-step/output error accounting. The next
question is not another generic instrument theorem. In the same driven-chain
family, determine whether monitoring admits an adequate finite conditional-memory,
cluster or tensor description for the relevant temporal record, or whether a
specific output-relevant many-body dependency survives. A local jump resets that
site but does not automatically factorize the remaining sites. Charge the same
horizon, detector/coarsening, initialization and required statistic on both sides.
Do not infer a separation from the small rate-law discrepancy or an exponentially
large history space. No new repository or spin-off is needed.

## Sources and inspection limits

[1] Ates, Olmos, Garrahan and Lesanovsky, *Dynamical phases and intermittency of the
dissipative quantum Ising model*, PRA 85, 043620 (2012), arXiv:1112.4273v2.
Equations (1),(2),(6) and finite-time versus stationary discussion inspected as PDF
text. https://arxiv.org/abs/1112.4273

[2] Dalibard, Castin and Molmer, *Wave-function approach to dissipative processes in
quantum optics*, PRL 68, 580 (1992), arXiv:0805.4002. Primary abstract and standard
conditional pure-state baseline. https://arxiv.org/abs/0805.4002

[3] Kliesch et al., *Dissipative Quantum Church-Turing Theorem*, PRL 107, 120501
(2011); erratum PRL 109,119904 (2012), arXiv:1105.3986. Primary theorem/method text
and publisher erratum metadata inspected. Our conservative commutator bound is
proved above, not copied from a dimension-dependent formula.
https://arxiv.org/abs/1105.3986

[4] Cattaneo et al., *Collision models can efficiently simulate any multipartite
Markovian quantum dynamics*, PRL 126,130403 (2021), arXiv:2010.13910. Primary
abstract: collision simulation and analytical error precedents, not a complete
instrument-level priority audit. https://arxiv.org/abs/2010.13910

[5] Whalen, *Collision model for non-Markovian quantum trajectories*,
arXiv:1906.03449. Primary abstract establishes monitored-collision/photodetection
precedent; its non-Markovian setting is not assumed here.
https://arxiv.org/abs/1906.03449

[6] Lesanovsky and Garrahan, *Kinetic constraints, hierarchical relaxation and onset
of glassiness in strongly interacting and dissipative Rydberg gases*, PRL 111,
215305 (2013), arXiv:1307.8078. Primary abstract and elimination passages; it is a
classical rate description under explicit strong-dephasing assumptions.
https://arxiv.org/abs/1307.8078

Sources checked 29 September 2026. Three requested PDF screenshots failed with
cache misses. No plot or experimental-table values were extracted; model and
method equations came from parsed primary text. This is not an exhaustive novelty
or significance audit. Standard counting, collision, product-formula and quantum-
jump ingredients are attributed, not claimed as newly invented.

Checker SHA256: `d0126af07e0e52dcf91f4425a53de72c604a52eff13a8882173abcd5b1603a5e`.
Report SHA256: `7304d69dc0a39163e476ff2de81791c416175da77b95b151825fda126b41388b`.

Only Quantum-Assisted-Algorithm-Discovery is writable. Earlier spectral, climate,
Manthan, battery/operator and independent spin-off boundaries remain as stated in
the live work order. No outside contact, paid/unattended work, manuscript revival,
branch merge, release or repository administration is part of this checkpoint.
