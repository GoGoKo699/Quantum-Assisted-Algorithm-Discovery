# Current task: test a phase-level classical description against physical records

29 September 2026. Branch: `research/prx-quantum-phase2`.
Model-first exploration; direct samples permitted; manuscript preparation on hold.

Read [emission memory 26](../exploration/phase_3/EMISSION_MEMORY_26.md),
[record instrument 25](../exploration/phase_3/RECORD_INSTRUMENT_25.md), and
[AGENTS.md](../AGENTS.md). No new repository or third spin-off is needed.

## Completed distinction: simultaneous occupation versus accumulated photons

In the same driven Ising model, keep all coherent amplitudes with excitation
number N_e<=q. Its dimension is D_q=sum_{r=0}^q binom(n,r). This is not a
population approximation or a cap on total emissions; lowering and repeated
re-excitation continue throughout the original observation horizon.

For uniform drive Omega, local decay kappa>0, diagonal interactions, and the
all-ground initial state, the averaged factorial moments obey
M_r(t)<=binom(n,r)[|Omega|/kappa*(1-exp(-kappa*t/2))]^(2r).
This holds for the full and truncated model without factorization or dephasing.
It does not bound every normalized state conditioned on a rare history.

A count-lifted Duhamel argument bounds the record-plus-final-state trace distance
by f_q integral_0^T sqrt(p_q^(q)(t))dt, where
f_q=|Omega|sqrt((q+1)(n-q))/2 and p_q^(q) is the truncated q-sector population.
This is a fixed-initial-state bound, NOT an arbitrary-input diamond guarantee.
It implies TV control of the original site/time-binned record and its coarsenings.
With lambda=n Omega^2/kappa^2, a sufficient envelope is
min(1, kappa*T/2*sqrt((q+1)*lambda^(q+1)/q!)); q=n is exactly the full model.
The controlled dynamics and numerical instrument errors are charged separately.

At fixed lambda, kappa*T and tolerance, finite q suffices and gives a polynomial
classical method. Fixed lambda requires Omega/kappa to scale as n^(-1/2).
Do not misstate this as fixed-local-drive thermodynamic tractability. The
conditional-state producer stores D_q amplitudes; sparse or precomputed unitary
propagation and monitored local damping have explicit costs in Note 26.

## Exact renewal and the non-dilute limitation

In q=1, every photon resets the whole conditional state to vacuum. On a uniform
open chain, the vacuum, symmetric endpoint excitation, and symmetric interior
excitation give an exact three-amplitude no-count model. Its waiting times and
site marks reproduce the q=1 instrument, including repeated photons. This is not
an assumed global blockade in the original model; use the error certificate
before replacing that model. Nonuniform q=1 inputs still have at most n+1 states.

For q>=2, a local jump can leave coherent excitation on other sites. A reachable
first-click expansion and a fixed check show waiting-time-dependent neighboring
intensity. That alone is not hardness: even independent emitters retain local
ages and have inexpensive samplers. A large jump rank is not evidence that every
state is reachable or every amplitude is required by the detector output.

A four-site check separates weak and equal-scale drives. At Omega=0.1,V=kappa=1,
T=6, q=2 has a proved full-record upper bound 0.018. At Omega=V=kappa=1, q=1 and
q=2 differ from the exact three-bin dark/bright law by about 0.4966 and 0.1000.
Those differences are numerical lower diagnostics on finer-record error, not
all-classical lower bounds; four sites are easy to solve. No advantage is shown.

## Next bounded model-level comparison

Rose et al., PRE 94,052132 (2016), arXiv:1607.06780, give a directly relevant
classical alternative: two metastable phases with effective classical switching
in a parameter/time regime of a related finite driven dissipative Ising chain.
The source has been screened at abstract/publisher level only. Inspect its actual
assumptions before transferring it to the present model, initialization or detector.

Compare the coherent, non-dilute record task with one explicitly stated two-phase,
hidden-state or cluster description. Determine which temporal/site information
it reproduces and which remains necessary, with a record-sensitive criterion
rather than closeness only of the averaged density state. Phase identification,
transition/emission data, preparation, burn-in and approximation errors all count.
Keep the original detector law or explicitly state a separately useful coarsening.
Do not demand arbitrary fine resolution solely to invalidate the classical model.

The deliverable is one discriminating model-level comparison, not another generic
truncation theorem, increasing cutoff census, new simulator or large trajectory
campaign. A failed two-phase approximation is not all-classical hardness. If no
specific output-relevant many-body obstacle survives adequate classical models,
broaden mechanisms rather than endlessly adding certificates. Quantum collision
sampling from Note 25 remains available with its full record/error cost.

## Executed evidence and preservation

The new NumPy/SciPy checker ran twice identically, rejecting -O/-OO and six invalid
inputs. One four-site model at two drives gives eight cutoff record/final-state
comparisons, 160 moment envelopes, 160 drift checks, 28 dissipative identities,
eight boundary norms and eight jump ranks. Three q=1 reduced-space controls check
the three-amplitude formula and site-resolved renewal; they are not full larger-
system simulations. Floating diagnostics are not interval certificates.
No hardware, native trajectory/tensor package, experimental data, timing study,
large-system run or old scientific verifier was used. General bounds are proved.

Preserve all old proofs, code, reports, data, licenses and rights. Climate/dynamics
remain open; Manthan is paused, battery/operator routes parked, both spin-offs
independent and Phase-2 Note 27 closed. Modify only Quantum-Assisted-Algorithm-
Discovery. No outside contact, paid/unattended work, manuscript revival, release,
merge, new repository or administration change is authorized.
