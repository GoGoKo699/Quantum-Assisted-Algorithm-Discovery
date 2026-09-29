# Claim ledger

## Current checkpoint: excitation-limited emission memory, 29 September 2026

[Note 26](exploration/phase_3/EMISSION_MEMORY_26.md) identifies a coherent classical
memory reduction for the same driven Ising record law. Keeping all amplitudes with
N_e<=q gives dimension D_q=sum_{r=0}^q binom(n,r). It does not cap accumulated photons,
erase detector labels, assume independent populations or alter the required bins.
The model has uniform drive/decay, diagonal interactions, ground initialization,
finite horizon and a local Markov reservoir. No arbitrary initial-state or finite-
temperature extension is claimed. No useful quantum advantage is established.

For full and truncated dynamics, the averaged factorial moments satisfy
M_r(t)<=binom(n,r)[|Omega|/kappa*(1-exp(-kappa*t/2))]^(2r). Positivity, collective
ladder norms and exact decay of factorial moments prove the statement without
assuming factorization, dephasing or a spectral gap. It is not a bound on every
normalized rare-history state.

A count-lifted Duhamel proof gives fixed-ground-initial-state record-plus-final-
state trace distance <= f_q integral sqrt(p_q^(q)(t))dt, with
f_q=|Omega|sqrt((q+1)(n-q))/2. The same bound controls the full detector-record TV.
Using the moment envelope yields min(1,kappa*T/2*sqrt((q+1)*lambda^(q+1)/q!)),
lambda=n Omega^2/kappa^2; q=n is exact. This is not a uniform diamond-norm statement.
The general residual-contraction method is prior work. Priority of this particular
record/moment specialization is not established. Numerical errors remain separate.

At fixed lambda, kappa*T and tolerance, finite q gives a polynomial-in-n coherent
classical sampler with explicitly charged propagation and record discretization.
Holding lambda fixed requires Omega/kappa~n^(-1/2). The result does not establish
fixed-density thermodynamic tractability or a classical lower bound in other regimes.
Classical conditional-state simulation remains stronger than the population-rate
approximation tested previously.

Within q=1, local jumps have rank one and reset the whole conditional state to
vacuum. Uniform open chains need just the vacuum, symmetric endpoint and symmetric
interior amplitudes for no-count evolution. Site-labelled waiting-time laws and
repeated photons follow exactly for that approximation. Its accuracy for the full
model is conditional on the record error bound, not a new physical blockade.
For q>=2, local clicks can leave coherent excitations on other sites. A reachable
small-time expansion and finite check show dependence on the previous waiting
time. Independent emitters can also retain local ages cheaply; nonrenewal and
jump rank alone are not quantum-advantage evidence.

The [work order](work_orders/CURRENT.md) directs the next comparison to a phase-level
or hidden-state description in the coherent non-dilute regime. Prior metastability
work supplies a serious two-phase classical comparator for stated finite-system
conditions. It has not been validated for this complete detector instrument.
No generic new trajectory framework, third spin-off, manuscript or new repository
is being started. Direct quantum sampling remains permitted.

## Executed evidence

The final Python/NumPy/SciPy checker ran twice with identical JSON under one BLAS
thread and rejected -O/-OO and six invalid inputs. A fixed four-site chain at
Omega=0.1 and 1, V=kappa=1, T=6 gives eight excitation-cutoff comparisons. At weak
drive q=2 has full-record upper bound 0.018 and observed three-bin dark/bright TV
about 0.000006314. At equal scales q=1 and q=2 have observed coarse-record TV about
0.496582 and 0.100045. Coarse TV is a lower bound on finer-record error, not an
upper bound. The small exact model is classically easy; no size scaling is inferred.

The [report](experiments/emission_memory_v1/REPORT.json) also records 160 moment
envelopes, 160 drift inequalities, 28 factorial decay identities, eight boundary
norms, eight jump ranks and degree-class/renewal identities. The q=1 n=7/10 tests
propagate only reduced spaces, not full larger spin models. Repeated photons are
explicitly checked, not forbidden by q. Matrix-exponential complex128 diagnostics
are not interval certificates; the general record bounds follow from the proof.

Checker SHA256: `bd8e4ab2cbcd10ec4b4b8601478edc7ef77b6b8c09945e725f59311893da768c`.
Report SHA256: `5220059b73583e542f78520d2d332a217a0e92557c6dba914f2d9757d5d69584`.

No quantum shots, laboratory data, native trajectory/tensor package, large-system
run or timing benchmark was used. No old scientific verifier was rerun or upstream
implementation imported. Primary HTML/abstracts and publisher summaries were
inspected; no PDF or figure was analyzed. Source scope is explicit in the note,
and the search is not an exhaustive novelty or significance audit.

## Preserved evidence

The complete prior ledger and its links remain at the pinned
[pre-memory checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/7faa7b9935e5ec445e975b3cf1d695ae54521066/STATUS.md).
Older current/next headings describe their checkpoints, not competing tasks.
All previous proofs, sources, code, reports, data, licenses and rights are unchanged.
Climate/dynamics remain open; Manthan paused; battery/operator routes parked;
both independent spin-offs and Phase-2 Note 27 retain their boundaries. Manuscript
preparation remains on hold. Only the parent repository is modified; no contact,
paid/unattended work, release, merge or repository administration change occurred.
