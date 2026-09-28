# Claim ledger

## Current checkpoint: gap-explicit slow-sector sampling, 28 September 2026

[Slow-sector sampling 18](exploration/phase_3/SLOW_SECTOR_SAMPLING_18.md) derives a
conditional effective description of the alternating-offset collective spin
response, with direct quantum integration. It does not require short-memory
decay or a single Lorentzian approximation. No useful quantum-classical separation,
physical prediction improvement, publication priority or practical speedup is
established.

Pi projects onto the entire conserved operator sector of L_0=[H_0,.]. If Pi D Pi=0,
the second-order generator is d^2 A, A=-Pi D L_0^+ D Pi. Reflection-pure energy
blocks suffice for that condition, but reflection symmetry alone does not exclude
opposite-parity degeneracies. Four finite uniform chains satisfy the numerical
checks; no arbitrary-size parity-purity or nondegeneracy theorem is claimed.

An invariant-graph proof gives a continuous-TV response bound, including state
dressing: for e=|d|v_*, ||D||<=v_*, a certified nonzero-frequency gap g and e/g<=1/8,
TV<=min(1,2e/g+2e^3/(g^2 gamma)). The bound survives common binning. At fixed n,
gamma=c d^2/J and fixed g>0 it vanishes with d. This is not a uniform large-chain
bound or a prescription to demand unnecessary experimental resolution.

Standard QSVT projector/inverse/product operations can block encode A from explicit
doubled-register Pauli descriptions. The effective spectral sample, rescaled by
d^2, has the required effective physical law. Under gamma=c d^2/J its sufficient
query budget has no inverse d power, but retains inverse-gap, size, access,
precision and repeated-shot costs. This comparison is with straightforward direct
quantum evolution, not the best classical method. A certified gap is not supplied
by an unverified numerical estimate. Related quantum effective-Hamiltonian methods
are explicitly attributed; no new matrix-arithmetic primitive is claimed.

The classical counterpart is [H_2,.] inside the energy blocks. Single irreducible
spin multiplets have scalar-plus-quadratic magnetization corrections. Acquiring
or sampling their coefficients remains a classical alternative. The maximum-spin
sector has an exact all-even-n correction, but its full-response weight is only
(n+1)(n+2)/(3*2^n). Solving that sector is not solving the full response. A one-magnon
identity gives g_n<=J[1-cos(pi/n)], an upper bound rather than the lower-bound promise
needed for inversion. The [work order](work_orders/CURRENT.md) now targets a justified
response-specific treatment of near resonances, not a larger benchmark campaign.

## Executed checks and limitations

The final NumPy checker ran twice with identical JSON under one BLAS thread;
-O/-OO refusal was checked. Four fixed 2/4/6/8-spin systems test zero conserved
staggered overlap, 98 parity/single-multiplet/quadratic-block controls, 12 effective-
commutator identities, the maximum-spin formula and its response weight. Four
2/4-spin binned comparisons obey the conservative error bound. Four small abstract
block systems test the invariant graph and norm/state bounds, and six path
Laplacians check the closed inverse quadratic form. Degenerate-parity, broken-
reflection and omitted-first-order negative controls and four invalid linewidths
are retained. The [report](experiments/slow_sector_v1/REPORT.json) records exact scope.

These are complex128 diagnostics at tolerance 3e-9, not interval certification,
large-n spectral claims, experimental spectra, a compiled QSVT circuit or runtime
measurements. Continuous guarantees come from the proof. The first draft's NumPy
boolean-negation error was fixed before the final successful runs. No historical
scientific suite was rerun; all previous scientific sources and reports are intact.
No upstream code, climate arrays or measured spectra were imported.

Primary effective-subspace and QSVT methods were inspected, including a visual
check of the QSVT inverse-normalization page. The SW screenshot failed. The recent
Li et al. effective-Hamiltonian preprint was checked at primary-abstract/version
level, not through a full independent proof audit. Source limits are in the note.

## Preserved historical evidence

The complete previous ledger and links remain at the pinned
[pre-slow-sector checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/7da0ca4a8f2f87a5283280f5a8541b17af97b521/STATUS.md).
Notes 15-17, their proofs, quantum clocks, classical comparisons, code and reports
are unchanged. Old current/next headings describe checkpoints, not parallel tasks.

Direct samples and model-first investigation remain authorized. Classical dynamics
and climate remain open; missing records block only their empirical test. Manthan
is paused, battery/operator routes parked, both classical spin-offs independent,
and Phase-2 Note 27 closed. Manuscript preparation remains on hold. Preserve prior
research, licenses and third-party rights. Only the parent repository is modified;
no contact, paid/unattended work, release, merge, new repository or admin change.
