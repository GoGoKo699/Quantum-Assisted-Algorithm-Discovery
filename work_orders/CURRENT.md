# Current task: physical record laws and a matched classical comparison

29 September 2026. Branch: `research/prx-quantum-phase2`.
Model-first exploration; direct quantum samples allowed; manuscript on hold.

Read [sampling decision 24](../exploration/phase_3/SAMPLING_REGIME_DECISION_24.md)
and [AGENTS.md](../AGENTS.md). No new repository is needed. Retain the prior
spectral results; do not convert them into a third classical spin-off.

## Completed decision and corrected comparison

The available spectral arguments do not yet identify a regime that requires
costly classical response acquisition while admitting cheaper quantum sampling.
This is not a proof that the model is easy at every resolution. Its direct
quantum sampler and classical typicality, half-time tensor, recursion, effective
and positive-window alternatives remain valid quantitative references.
Do not accumulate more generic spectral certificates as the default task.

Both producers may cache. A quantum source can supply original samples to a
classical empirical table; it need not invoke the device for every later draw.
Standard finite-distribution learning prices the bank. Replayed draws are
conditionally independent from that table but share its error unconditionally.
For S original event samples and M replays, variance is
p(1-p)(S+M-1)/(SM), not p(1-p)/M. This is a statistic-specific calculation, not a
universal effective-sample-size definition. Do not compare per-draw TV with an
M-independent-target-draw inference contract. The same caution applies classically.

## One bounded additional mechanism: monitored interacting emitters

Use the established driven dissipative Ising model in Note 24, with
H=Omega sum S_i^x+V sum_neighbors S_i^z S_j^z and local jumps sqrt(kappa) S_i^-.
Start with a specified product state on a finite bounded-degree graph, prescribed
finite horizon, and ideal photon-counting instrument. The initial task is not a
stationary distribution with free burn-in. The Markovian local zero-temperature
bath is a different model from the earlier closed, infinite-temperature spin trace.
State the graph, truncation and detector assumptions; no arbitrary Rydberg platform
is presumed to satisfy them. Existing photon-activity theory motivates this model.
Experimental excitation-count data are not photon-time records or a validation of
our proposed detector law.

The quantum entry is successive local system-ancilla interactions, measurements
and resets, preserving the conditional system state between outputs. Classical
quantum-jump methods implement the same law by conditional pure-state propagation;
comparing only against a full density matrix would be artificially weak.
The framework is prior work, not a new simulation primitive.

## Next bounded mathematical deliverable

Specify one coarse-grained physical record law and derive the accuracy/cost of a
local quantum collision or splitting construction for it. A local amplitude-damping
step is exactly implementable; its full driven continuous-record limit has NOT
been bounded here. Account for time binning, possible multiple emissions, detector
labels/efficiency, initial-state error, finite precision and the number of steps.

Use the instrument channel that outputs the record AND remaining quantum state.
Half-diamond error eta_j per step telescopes to record TV at most sum eta_j.
An error bound on the density channel after erasing the record is insufficient.
Note 24's two-emitter Kraus mixing gives identical unlabelled dynamics but different
labelled records; do not change the measured unraveling merely to ease simulation.

Compare with a justified classical rate/renewal or conditional-state approximation
in one coherent-interaction regime. Select a fixed finite-time statistic, such as
a dark-interval probability or correlations of consecutive count bins, and show
how the record guarantee controls it. Permit direct evaluation when the consumer
needs only a few statistics rather than whole histories. An exponentially large
history alphabet, antibunching, or a failed mean-field approximation is not proof
of useful quantum advantage. Independent emitters and strong-dephasing rate limits
are controls, not hard examples. Allow tensors, cluster methods, hidden-state
models and exact small-sector reductions whenever adequate.

The deliverable is a matched law/error and symbolic-cost comparison, not a new
trajectory framework, large simulation, hardware port, data acquisition campaign
or assumption of a favorable gap/mixing time. A small diagnostic may verify an
identity but cannot establish many-body hardness or experimental usefulness.
Retain uncertainty explicitly and keep other mechanisms available.

## Executed evidence and preservation

The new checker ran twice with identical JSON, rejecting -O/-OO and six invalid
inputs. It evaluates three analytical spectral-resolution settings, exact cache
variance through rational binomial enumeration, a standard table-learning budget,
and a two-emitter Kraus-channel control. It does NOT propagate the listed 20/26/32-
spin systems, simulate a driven record, compile a quantum circuit, or benchmark
classical/quantum runtime. Earlier scientific verifiers were not rerun. No upstream
code or data were imported. Primary proofs/model methods and two PDF pages were
inspected; the note states the limited source scope and no priority claim.

Preserve all prior notes, proofs, code, reports, data, licenses and third-party
rights. Climate/dynamics remain open, Manthan paused, battery/operator routes parked,
both spin-offs independent, and Phase-2 Note 27 closed. Modify only Quantum-Assisted-
Algorithm-Discovery. No outside contact, paid/unattended work, manuscript revival,
release, branch merge, new repository or administration change is authorized.
