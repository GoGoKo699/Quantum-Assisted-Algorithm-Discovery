# Collision application check: chemical branching in CO2 plasmas

25 September 2026. Phase 2; target PRX Quantum; manuscript remains on hold.

This note follows the collision-law discussion. It is separate from the spectral-record investigation now recorded as MECHANISM_SCOUT_02.md on the shared branch. Neither that file nor earlier experiments are replaced. This is literature-based problem selection and elementary accounting, not a quantum algorithm, new cross-section dataset, benchmark or novelty claim.

## 1. The independently specified consumer

LoKI-GM couples an electron Boltzmann solver with chemical kinetics. Its inputs include cross sections, internal-state populations and reaction rates; its outputs include electron distributions, transport, power deposition and species densities [1]. The quantum output contemplated here would be microscopic collision data consumed by such a classical model, not a quantum simulation of the reactor. This is physical-model compilation, not discovery of a general arithmetic algorithm.

## 2. A useful distinction: electron transport versus chemical products

Liu et al. [2] split effective electron-excitation channels into dissociative and nondissociative contributions while retaining the electron transport predictions by construction. Their experimentally assessed update uses a 15% dissociative share for a lumped 7 eV channel and a fully dissociative 10.5 eV channel. These are effective cross-section assignments, not pure molecular states or overall conversion efficiencies. Experimental chemistry data already constrain them. Their remaining excited-state-data qualifications are statements about that paper, not a verified absence of all subsequent work.

The elementary mechanism can be written without a plasma solver. Let q(E) be a total inelastic cross section. Divide it as

    sigma_d(E) = b(E) q(E),
    sigma_e(E) = (1-b(E)) q(E).

If both labels use the same outgoing-electron energy/angle kernel, their contributions to the electron collision operator add to q(E) times that kernel. At FIXED gas composition and internal-state populations, this part of electron transport does not identify b. The dissociation source does depend on b. In a coupled reactor model different chemical products can subsequently change the electron distribution, so the invariance is not a claim about the entire self-consistent time evolution.

This is an explanation of an existing modeling distinction, not a new identifiability theorem. It motivates asking for product-resolved information, rather than merely another fit to transport data.

## 3. The actual output interface

Let f(E) be a normalized electron energy probability density, with E in joules, integral f(E)dE=1. For a declared molecular preparation nu and product channel j, the rate coefficient is

    k[j,nu;f] = integral f(E) sqrt(2E/m_e) sigma[j,nu](E) dE.

For electron density n_e and state populations n_nu, the corresponding binary-collision source is

    R_j = n_e sum_nu n_nu k[j,nu;f].

Here sigma has units of area, k volume/time, and R number/(volume*time). Conventions using eV or a differently normalized EEDF require the corresponding conversion factors. These expressions do not replace other reaction channels or assert the validity of a binary-collision closure in every regime.

For a fixed, justified nonnegative basis of normalized energy distributions phi_a, write f=sum_a p_a phi_a. A finite record

    K[j,nu,a] = integral phi_a(E) sqrt(2E/m_e) sigma[j,nu](E) dE

then supports R_j=n_e sum_nu,a n_nu p_a K[j,nu,a]. This is elementary linearity, not a learning theorem. It covers only the declared preparations and distribution family. No bound on a useful number of basis functions, numerical tolerance or energy window is established here. One Maxwellian-averaged rate is not a universal record for non-Maxwellian plasmas.

Finite wavepacket probabilities are not automatically cross sections: incoming flux, angular/partial-wave sums, continuum boundaries and finite-time convergence must be supplied. Dissociation requires electronic excitation and subsequent nuclear motion to be treated at the fidelity relevant to products. No free potential-energy surfaces, state preparation, full spectrum, or postselected rare-event probability is assumed.

## 4. A sharper candidate question

Does initial vibrational excitation alter the chemically relevant electron-impact outcomes in a way that cannot be captured by a threshold shift of ground-state data, after averaging over the distributions the kinetic model needs?

Pietanza, Colonna and Capitelli [3] explicitly use threshold-shifting prescriptions for missing state-resolved dissociation and ionization data. That provides a real classical surrogate to test, rather than a deliberately weak dense-wavefunction solver. The mechanism question is whether internal excitation acts only as an energy credit or also changes pathway competition. Failure of a threshold-shift prescription, if established, would still not establish classical computational hardness.

No incoming vibrational level, narrow resonance, accuracy target or device regime has been chosen merely to defeat classical approximations. A future minimal comparison should use ground and an independently populated excited preparation, the same energy/distribution family, the current surrogate, and a credible classical scattering calculation. Compare the required averaged product rates, not expensive microscopic details the consumer does not use.

## 5. Regime and classical-competitor checks

A low-pressure CO2/O2 glow-discharge study [4] finds electron-impact dissociation dominant, but weak vibrational excitation makes ladder-climbing dissociation negligible; vibrational kinetics still changes the electron distribution through superelastic collisions. It does not demonstrate that state-dependent dissociation itself is the important missing quantity.

At atmospheric pressure under nanosecond pulses, Dias et al. [5] instead find delayed dissociation driven by gas heating and molecular collisions in the afterglow. An improved direct electron-dissociation calculation cannot automatically be credited with improving that entire regime. Both direct and indirect effects would need checking.

Accordingly, the regime where excited-state collision information is consequential remains to be established. We have found an identifiable data/interface question, not an accepted advantage workload or an independently justified numerical error tolerance.

The serious alternative includes empirical rate data, threshold laws, classical R-matrix/close-coupling electronic calculations, nuclear propagation and statistical approximations. In particular, Horton et al. [6] calculate vibrationally resolved dissociative processes for H3+ with convergent close coupling. Different species are not matched benchmarks, but this is enough to reject any premise that polyatomic, state-resolved dissociation is intrinsically beyond classical calculation.

## 6. Quantum prior art and the actual obligation

Picozzi et al. [7], published 6 July 2026, formulate the R-matrix inner-region problem using variational quantum algorithms. Their electron-H2 example uses a noiseless classical simulator and recovers a selected subspace spectrum and boundary amplitudes. Therefore, quantum electron-scattering data feeding a classical outer calculation is already prior work. Neither that demonstration nor a small output proves useful fault-tolerant advantage for CO2.

A candidate positive result here would have to supply an independently needed, transferable product-resolved law with a complete preparation/evolution/readout cost that beats strong classical alternatives at the same useful accuracy. It need not reproduce an entire spectrum or scattering matrix when the downstream use only needs inclusive product probabilities. Avoiding those outputs is a design requirement, not a novelty claim; classical methods may avoid them too.

A microscopic Hamiltonian that is expensive classically is insufficient if its required rates are easy. Conversely, missing data may reflect measurement difficulty, inadequate modeling or limited historical attention rather than costly classical computation. Those explanations must be distinguished before estimating a quantum speedup.

## 7. Decision and work actually completed

Keep CO2 state-dependent chemical branching as the first application check for the collision-law mechanism, not a commitment to this molecule or a claim of superiority. The next decisive comparison is whether a physically justified excited-state rate changes a useful kinetic prediction beyond what existing surrogate and microscopic classical calculations can already supply. Retain a separate account of the quantum cost; do not infer it from data uncertainty.

This pass read primary papers and the LoKI interface, and derived the elementary operator relationships above. No LoKI, scattering solver, electronic-structure calculation, numerical sensitivity analysis or quantum resource estimate was run. No new collision data, completed absence/novelty audit, manuscript, external contact, paid work or unattended task was produced. The manuscript stays on hold.

## Primary sources and provenance

[1] LoKI-Suite/LoKI-GM README, version label LoKI-GM_26.07, inspected through the GitHub connector on 25 September 2026. Blob a1605d0fe76fdcd9c1f5d1b3adc01f56319084b6. https://github.com/LoKI-Suite/LoKI-GM/blob/master/README.md . Source-interface inspection, not code execution.

[2] Y. Liu et al., An updated set of electron-impact cross sections for CO2: untangling dissociation and application to CO2 with Ar and N2 admixtures. Plasma Sources Sci. Technol. 34, 035003 (2025). https://doi.org/10.1088/1361-6595/adba86 . Publisher full text read in HTML through ResearchGate, including Sections 2.2 and 3. No plot digitization or downloaded dataset analysis.

[3] L. D. Pietanza, G. Colonna, M. Capitelli, Self-Consistent State-to-State Kinetic Modeling of CO2 Cold Plasmas: Insights on the Role of Electronically Excited States (2023). https://doi.org/10.1007/s11090-023-10407-x . Publisher HTML inspected for the state-to-state model and threshold prescriptions.

[4] T. C. Dias et al., Study of vibrational kinetics of CO2 and CO in CO2-O2 plasmas under non-equilibrium conditions (2023). https://doi.org/10.1088/1361-6595/acb665 . Primary abstract/conclusions inspected; no reproduced kinetic simulation.

[5] T. C. Dias, L. M. Martini, P. Tosi, V. Guerra, Beyond electron impact: Dissociation driven by molecular collisions in CO2 nanosecond pulsed plasmas. Journal of CO2 Utilization 108, 103435 (June 2026). https://doi.org/10.1016/j.jcou.2026.103435 . Publisher and author-institution abstracts inspected; no full model reproduced.

[6] R. K. Horton, M. V. Pak, I. Bray, D. V. Fursa, Convergent close-coupling approach to electron scattering on H3+: Scattering dynamics and dissociative processes. Phys. Rev. A 111, 022802 (2025). https://doi.org/10.1103/PhysRevA.111.022802 . Primary abstract inspected as evidence of a classical methodology, not a CO2 performance comparison.

[7] D. Picozzi, J. Tennyson, V. Graves, J. D. Gorfinkiel, Electron-molecule scattering via R-matrix variational algorithms on a quantum computer. Phys. Rev. A 114, 012407 (6 July 2026). https://doi.org/10.1103/q8ry-hlxt ; https://arxiv.org/html/2507.05514v2 . Full arXiv HTML and publication metadata inspected; no code execution. An attempted PDF screenshot did not render and is not used as evidence for a figure or table.
