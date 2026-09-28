# Direct sampling 10: samples may be the useful output

28 September 2026. Starting head:
`a71412194e0f4a5cd15937ffe3ab5ed4e67c500a`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

## Scope decision

The owner proposes consuming quantum samples directly, with probabilistic prediction
of chaotic systems as a possible application. Investigate that proposal without
requiring the samples to be converted into a reusable classical program first.
This is an explicit exploratory extension of the original classical-only deployment
objective, not a claim that direct sampling already met the old contract. Continued
quantum use at prediction time is allowed in this investigation and must be costed.
The scientific comparison and usefulness requirements remain in force.

The Manthan synthesis investigation is paused, not refuted. Its installation
problems do not constitute evidence for or against direct sampling. Existing
encoding diagnostics, the battery archive, earlier negative findings and both
independent spin-offs remain unchanged. No new repository is needed.

## 1. What chaotic-system forecasters actually need

ECMWF's ensemble methodology treats uncertainty in initial conditions and model
formulation by generating multiple possible future evolutions [1,2]. The purpose
is a conditional prediction and its uncertainty, not additional random bits.
For a simplified deterministic model with flow Phi_t and present observations D,

$$
X_0\sim p_0(\cdot\mid D),\qquad X_t=\Phi_t(X_0)
$$

induces the forecast distribution. A stochastic model also requires an appropriate
law for its forcing history and uncertain parameters. The random source and the
physical/observational uncertainty model must not be confused.

The proposed quantum deliverable could be samples of a future state, a consistent
trajectory, or a consumer-relevant quantity Z=g(X_[0,T]). For example, an event can
be defined by a threshold crossing within a declared time window. Sampling marginal
states independently at several times does not in general produce a valid path.
A distribution over long-run climate extremes is also not a weather forecast
conditional on today's observations; these are separate input/output contracts.

A forecast ensemble can be useful even when individual long-horizon trajectories
cannot be predicted reliably. It cannot restore missing observational information,
make the physical model correct, or guarantee skill at arbitrary horizons.
Probabilistic reliability must be assessed against observations or an independently
validated reference at the scope actually claimed [1,2].

## 2. A concrete quantum connection, already in the literature

For deterministic dynamics, the Liouville equation evolves the probability density
linearly even when the individual dynamics are nonlinear. Joseph [3] develops a
Koopman-von Neumann quantum representation of classical distribution evolution.
Succi et al. [4] discuss ensemble fluid simulation through a Liouville formulation.
These are direct precedents, not a new architecture or operational weather result.

For a discrete forecast law p_t, a suitable measurement representation is

$$
|\psi_t\rangle=\sum_x\sqrt{p_t(x)}e^{i\theta_x}|x\rangle.
$$

Measuring this register gives p_t. By contrast, a normalized numerical vector with
amplitudes proportional to p_t(x) gives probabilities proportional to p_t(x)^2.
Likewise, sampling a spatial index from an amplitude-encoded velocity vector is
not a draw of the full fluid configuration. The physical meaning of the encoded
basis and amplitudes is therefore part of the algorithm, not readout bookkeeping.
Mixed-state or other representations are allowed if their measurement law is shown.

This representation does not establish efficient preparation or propagation.
A finite discretization, boundary conditions, initial distribution, access circuits,
Hamiltonian/operator normalization, relevant resolution, precision, and repeated
sample extraction all need a cost and an error argument. Dissipation and stochastic
forcing cannot simply be represented by an unqualified unitary for an unrelated
quantum system. A classical chaotic system is not simulated correctly merely by
running a quantum-chaotic circuit.

## 3. What the change removes, and what it does not

Direct use removes the requirement to learn a compact classical emulator of a
potentially classically difficult distribution. Samples can go straight into an
existing statistical or decision procedure. This may avoid a needless bottleneck
in our earlier contract; it supplies no speedup by itself.

The correct classical comparator does not store the full probability density on
an exponentially large grid. It can draw initial states and propagate trajectories,
use a learned forecast generator, exploit source structure, or target selected
outcomes. An advantage against a full probability-grid calculation is not
necessarily an advantage against these sample-based alternatives [1,3].

As elementary accounting, M independent event-indicator samples with probability q
have sample-mean variance q(1-q)/M. The formula is independent of the source's
hardware. Raw quantum shots do not automatically change that scaling. Correlations
and importance weights require their own variance accounting. Repeated state
preparation or a validated multi-sample generation procedure must be charged;
one encoded distribution is not an unlimited independent sample collection.

Amplitude estimation is a separate option for estimating one probability or mean.
It can reduce coherent query complexity under its assumptions [5], but it is not
the same task as delivering an ensemble of physical scenarios. It requires coherent
access to the preparation/computation and appropriate inverse operations, not just
stored classical measurement results. Do not substitute that output silently for
requested trajectories, or interpret ordinary shots as amplitude estimation.

Lewis et al. [6] give limitations for nonlinear/chaotic simulation formulated as
preparing an amplitude-encoded normalized solution vector under their input and
coordinate assumptions. Their specific output contract is not an automatic
no-go theorem for every coarse forecast observable or distribution sampler.
Nor does changing the output contract prove those tasks efficient. Scope must be
checked before either extrapolating the lower bound or claiming to evade it.

## 4. A useful direction to test, not a selected operational application

The first suggested family is **direct sampling of physically consistent rare-event
scenarios for an existing risk or forecast consumer**. Identify whether the consumer
needs ordinary forecast draws, samples conditional on an extreme, or a probability
estimate. Conditional extreme samples alone do not give the event's unconditional
frequency. Biased sampling requires a justified weighting or probability procedure.

Classical work already samples heatwave trajectories in a substantial climate model
[7]. The 2026 TEAMS study extends rare-event sampling to transient extremes in an
idealized general circulation model [8]. The latter is a methodological study in
an idealized atmosphere, not an operational regional forecast. Both show that
rare-event examples can have direct scientific use and that ordinary rejection
sampling is an inadequate sole competitor.

For broader forecast generation, GenCast [9] is a classical probabilistic generator.
ECMWF's official page reports operational AIFS ensembles and a v2 update on
12 May 2026 [10]. Compare against applicable current classical generators, not
only traditional trajectory integration. Training/data costs must be allocated
consistently on both sides. Their existence neither solves every rare-event task
nor identifies a quantum shortfall automatically.

The next deliverable is one task-level comparison: a named consumer and event,
physical/model domain, conditioning data, required law or statistical accuracy,
classical baseline, implementable quantum representation, and full cost per useful
output. Begin with the output law and the strongest baseline, not a large climate
simulation or a proof that random circuits are hard to sample. A Lorenz model
may diagnose a mechanism but cannot by itself establish weather or engineering
utility. No specific model/event pair has passed this comparison in this note.

## 5. Evidence and source scope

This checkpoint is a scope decision and focused literature inspection. It contains
no new theorem, numerical experiment, circuit, simulation, forecast, native solver
run or performance estimate. No scientific verifier was rerun. Prior source/results
and licenses are preserved. No PDF was analyzed in this screen: sources were read
as primary HTML text, abstracts or official documentation. No charts were digitized.

Sources checked 28 September 2026; this is not an exhaustive novelty audit:

[1] Leutbecher and Palmer, Ensemble forecasting, ECMWF Technical Memorandum 514
(2007). Institutional abstract on uncertainty and ensembles inspected.
https://www.ecmwf.int/en/elibrary/75394-ensemble-forecasting

[2] ECMWF, Fact sheet: Ensemble weather forecasting (2017). Reliability and purpose
sections inspected; historical ensemble configuration is not asserted current.
https://www.ecmwf.int/en/about/media-centre/focus/2017/fact-sheet-ensemble-weather-forecasting

[3] Joseph, Koopman-von Neumann Approach to Quantum Simulation of Nonlinear
Classical Dynamics, Phys. Rev. Research 2, 043102 (2020), arXiv:2003.09980v4.
Abstract and indexed publisher sections on probability amplitudes and Monte Carlo
comparison inspected; not a full circuit or error-proof audit.
https://arxiv.org/abs/2003.09980
https://doi.org/10.1103/PhysRevResearch.2.043102

[4] Succi et al., Ensemble fluid simulations on quantum computers, Computers &
Fluids 270, 106148 (2024). Publisher/institutional abstract inspected.
https://doi.org/10.1016/j.compfluid.2023.106148
https://eprints.gla.ac.uk/311476/

[5] Montanaro, Quantum speedup of Monte Carlo methods, Proc. R. Soc. A 471,
20150301 (2015), arXiv:1504.06987. Primary abstract; no resource instantiation.
https://arxiv.org/abs/1504.06987

[6] Lewis et al., Limitations for Quantum Algorithms to Solve Turbulent and Chaotic
Systems, Quantum 8, 1509 (2024), arXiv:2307.09593v2. HTML introduction, specified
output Eq. (9), and state-discrimination assumptions inspected.
https://arxiv.org/html/2307.09593v2

[7] Ragone and Bouchet, Rare Event Algorithm Study of Extreme Warm Summers and
Heatwaves Over Europe, Geophys. Res. Lett. 48 (2021), e2020GL091197. Primary
abstract and HTML description inspected; no performance reproduction.
https://doi.org/10.1029/2020GL091197

[8] Finkel and O'Gorman, Rare Event Sampling for Moving Targets: Extremes of
Temperature and Daily Precipitation in a General Circulation Model, JAMES 18
(2026), e2025MS005456. Publisher HTML abstract, model, conclusion and data statement
inspected. Published 6 March 2026. No figures or performance numbers replayed.
https://doi.org/10.1029/2025MS005456

[9] Price et al., Probabilistic weather forecasting with machine learning,
Nature 637, 84-90 (2025), online 4 December 2024. HTML model description inspected;
no independent validation of accuracy or runtime claims.
https://www.nature.com/articles/s41586-024-08252-9

[10] ECMWF, AIFS Machine Learning data. Official operational-version statement.
https://www.ecmwf.int/en/forecasts/datasets/aifs-machine-learning-data

Only Quantum-Assisted-Algorithm-Discovery may be modified. No external contact,
paid/unattended computation, manuscript revival, submission, release, branch
merge, new repository or administration change follows from this exploration.
