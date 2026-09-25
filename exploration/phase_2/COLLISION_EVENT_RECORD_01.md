# Collision-event records: reuse without a full cross-section table

25 September 2026. Phase 2, PRX Quantum target. Manuscript remains on hold.
This is an exploratory importance-sampling calculation, not a new quantum
algorithm, collision calculation, novelty claim or demonstrated advantage.
The parallel spectral-record scout and all historical files remain unchanged.

## 1. Literature boundary

Picozzi et al. [1] already separate a quantum R-matrix inner calculation from
classical outer-region scattering. Their noiseless hydrogen example recovers
a selected symmetry-sector spectrum, not a scalable fault-tolerant advantage.
Classical partitioned R-matrix methods [2] already avoid complete diagonalization
by accounting approximately for omitted eigenpairs. A separate 2025 quantum
rotational-collision demonstration [3] precomputes its coupling matrix
classically. These are different methods, not a matched runtime comparison.

Abidi et al. [4] calculate vibrationally resolved CH dissociation data using
classical R-matrix, electronic-structure and local-complex-potential methods.
CH is not CO2, but state-resolved quantum dynamics alone is not a hardness
argument. No new state-resolved CO2 computational bottleneck was established.

The new question is whether a reusable output must reconstruct the entire
state/energy/product table. For a specified family of incoming distributions
and one bounded output observable, it need not.

## 2. A labelled event record

Fix a Hamiltonian, one resolved molecular preparation, an incident-wavepacket
protocol labelled by energy E, and a product event Y in {0,1}. Let
P(E)=E[Y|E]. Any unrecorded angle, transverse, spin or other variable has a fixed
specified distribution. Otherwise include it among the retained input labels.

For a later normalized input density g_theta, the normalized prediction is

    mu(theta) = integral g_theta(E) P(E) dE.

Choose a reference density q. Draw E_i classically, run the microscopic process,
and retain (E_i,Y_i). The ordinary importance estimator is

    mu_hat(theta) = (1/m) sum_i g_theta(E_i) Y_i / q(E_i).

It is unbiased. The unknown response P need not be reconstructed or smooth.
Sampling P accurately can still be expensive, particularly near narrow
resonances. Reweighting is classical and equally available to classical
simulations and measured event data. Combining proposals and reusing thermal
rate data are established methods [5,6], not the quantum contribution.

## 3. Exact thermal-envelope calculation

Set theta=k_B T. Maxwellian particle density multiplied by speed and normalized
gives the thermal-flux energy density

    g_theta(E) = E theta^(-2) exp(-E/theta),  E>=0.

This is the flux density, not the unweighted Maxwellian particle distribution.
The familiar thermal rate integral uses this weighting [4, Eq.14]. Restrict
0<a<=theta<=b. This is a declared family, not a claim that a nonequilibrium
CO2 electron distribution is Maxwellian.

At a fixed E, the maximizing temperature is clip(E/2,a,b). Thus

    h(E)=sup_theta g_theta(E)
        = g_a(E)                  if E<2a,
          4 exp(-2)/E             if 2a<=E<=2b,
          g_b(E)                  if E>2b.

The integral is Z=1+4 exp(-2) log(b/a). The left and right masses are
1-3 exp(-2) and 3 exp(-2); the middle adds 4 exp(-2) log(b/a).
Take q=h/Z. It is explicitly sampleable by a mixture of truncated Gamma(2,a),
log-uniform and truncated Gamma(2,b) densities. No collision data are needed
to prepare this classical proposal. Tail rejection probabilities are constants.

For all theta,E, g_theta(E)/q(E)<=Z. This minimizes the worst importance
weight over all normalized q: any bound h<=Wq implies Z<=W by integration.
This does NOT minimize arbitrary variance or energy-dependent simulation cost.
For b/a=10,100,1000 the factors are 2.246484,3.492968,4.739452. They are
coverage factors, not speedups or numbers of microscopic runs.

## 4. A simultaneous guarantee

X_theta=g_theta(E)Y/q(E) is in [0,Z], with mean<=1 and second moment<=Z.
Bernstein gives, for 0<epsilon<=1,

    Pr(|mu_hat(theta)-mu(theta)|>epsilon/2)
        <=2 exp[-m epsilon^2/(10Z)].

To cover a continuum, write t=log(theta). Differentiating g gives
partial_t g=g(E/theta-2). Its integral is zero and its positive part integrates
to c=4 exp(-2). Thus |d mu/dt|<=c for any fixed measurable 0<=P<=1.
For neighboring grid values theta_l<=theta<=theta_u spaced by at most h in t,

    exp(-2h) g_(theta_l) <= g_theta <= exp(2h) g_(theta_u).

The same sandwich holds for empirical averages because Y>=0. A grid with
h<=epsilon/16 and J=ceil(16 log(b/a)/epsilon)+1 points therefore extends
pointwise epsilon/2 accuracy to uniform epsilon accuracy. One sufficient upper
interpolation coefficient is

    exp(1/8)-1 + exp(1/8)[c/16+1/2] < 1.

For a=b use J=1. The sufficient independent sample count is

    m >= ceil[10 Z epsilon^(-2) log(2J/delta)].

With probability at least 1-delta the SAME record is accurate at every
temperature in [a,b], including one chosen after inspecting the record.
Clipping a final normalized estimate to [0,1] cannot increase absolute error.
Any nonnegative mixture of those flux distributions inherits the same uniform
bound by linearity. This is not a guarantee for every EEDF or arbitrary
post-hoc observables. The microscopic preparation and event law are fixed.

## 5. Physical and resource boundaries

A finite-wavepacket outcome is not automatically sigma(E)/Sigma. If an
independently justified protocol supplies a known area Sigma and a bounded
estimator with E[Y|E]=sigma(E)/Sigma, then

    k(T)=Sigma sqrt(8 theta/(pi m_e)) mu(theta).

Constructing that estimator is an additional obligation: beam/flux normalization,
transverse averaging or partial waves, channel detection, finite-time convergence,
energy resolution and state preparation. A loose Sigma worsens the accuracy
required in mu. No inexpensive cross-section oracle is assumed.

Ideal energy tails can be bounded: omission above E_max loses at most
(1+E_max/b)exp(-E_max/b) of normalized event probability; omission below E_min
loses at most (E_min/a)^2/2. These are not bounds on an unbounded cross section.
Finite energy labels and simulation errors must be budgeted. Avoiding a fine
output grid does not imply avoiding long coherent evolution for a resonance.

Only additive accuracy is established. Relative precision for rare outcomes
can remain expensive. For arbitrary later molecular populations, a joint
proposal pi_nu q(E) introduces weights p_nu/pi_nu. With r arbitrary pure
preparations, the minimax worst coverage factor is at least r. The logarithmic
temperature dependence does not cover arbitrary internal-state inputs for free.

Total quantum work includes preprocessing, m times mean IMPLEMENTED event cost
under q, record generation, and later O(m) classical work per query. Classical
competitors may use the same reuse, choose another surrogate, or bypass sampling.
The selected q optimizes coverage, not necessarily computation time. Reuse is
not the source of quantum advantage.

This rate-query record is not a drop-in replacement for all of LoKI: an electron
Boltzmann solve needs energy-resolved collision information, and its EEDF need
not belong to this family. Repeated-collision and nonlinear kinetic sensitivity
are also separate from the single-event bound.

## 6. Work actually run

thermal_record_check.py is a small NumPy/SciPy synthetic-event test, not a
molecular simulation. P(E) is a supplied constant plus three disjoint weighted
energy bands. Proposal normalization, the analytic envelope, energy-unit
rescaling, exact integrals and mixture reweighting were checked.

At a=.1,b=10, seed20260925 and129 test temperatures, observed maximum errors
were .0334258,.0139026,.00255018 for1024,8192,32768 samples respectively.
These finite-grid observations are NOT a universal confidence certificate.
The conservative theorem requests153486 samples at epsilon=delta=.05.
Two executions reproduced the report exactly on this environment; numerical
values need not be byte-identical across platforms. No old research verifier,
scattering solver, quantum sampler, native baseline or hardware was run.

Reproduce without overwriting evidence:

    OPENBLAS_NUM_THREADS=1 python exploration/phase_2/thermal_record_check.py \
      --output /tmp/new-thermal-record-observations.json

## 7. Decision

The output burden can be smaller than a full collision table. This is a useful
interface simplification, not a PRX Quantum result by itself. Quantum advantage
must come from obtaining the microscopic information. That comparative regime
is still missing. Do not extend this into a large data framework, claim
importance-sampling novelty, or resume the manuscript. The next positive step
must identify the microscopic computation quantum processing actually improves.

## Sources and inspection scope

[1] Picozzi et al., Phys. Rev. A114,012407 (6 July2026),
https://arxiv.org/html/2507.05514v2 ; https://doi.org/10.1103/q8ry-hlxt .
Full HTML workflow/method inspected; no native run.
[2] Tennyson, Partitioned R-matrix theory for molecules, J. Phys. B37,1061 (2004),
https://discovery.ucl.ac.uk/id/eprint/1307/ ; DOI10.1088/0953-4075/37/5/009.
Author/institution abstract inspected; no full-paper numerical analysis.
[3] Andrade-Plascencia et al., JCTC (2025), DOI10.1021/acs.jctc.5c00504,
https://pubs.acs.org/doi/abs/10.1021/acs.jctc.5c00504 . Publisher abstract only.
[4] Abidi et al., arXiv:2602.10649 (2026),
https://arxiv.org/html/2602.10649v1 . HTML method and rate Eq.14 inspected.
No table/figure-derived performance claim; CH is not CO2.
[5] Veach and Guibas, SIGGRAPH1995, DOI10.1145/218380.218498;
Sbert and Elvira, https://arxiv.org/abs/1903.11908 . Prior methodology,
not a claim these sources contain the exact envelope derivation above.
[6] Hahn and Savin, https://arxiv.org/abs/1506.07127 (2015).
Abstract inspected for prior reuse of Maxwellian rate data. No arbitrary-EEDF
or finite-temperature-mixture universality inferred.
