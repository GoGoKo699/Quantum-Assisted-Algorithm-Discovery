# Current task: response-relevant resonances and the cost of effective spectral sampling

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read [slow-sector sampling 18](../exploration/phase_3/SLOW_SECTOR_SAMPLING_18.md),
[exchange memory 17](../exploration/phase_3/EXCHANGE_MEMORY_17.md), and
[model comparison 15](../exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md).
Mathematical models and quantum integration precede implementation. Direct samples
remain permitted; no learned classical program or quantum-free deployment is required.

## Completed conditional reduction, not a quantum-classical separation

Let Pi project onto all operators commuting with the exchange Hamiltonian H_0,
L_0=[H_0,.], and D=[V,.]. When Pi D Pi=0, the leading slow generator is d^2 A,
A=-Pi D L_0^+ D Pi. This Pi is not the rank-one observable projector of Note 17.
Reflection-pure energy eigenspaces suffice for the first-order cancellation, but
reflection symmetry alone does not. Opposite-parity degeneracy is an explicit
exception. No arbitrary-size parity-purity theorem was proved for the uniform chain.

For a nonzero-frequency gap lower bound g, ||D||<=v_*, e=|d|v_* and e/g<=1/8,
the exact physical and effective Cauchy(gamma)-broadened laws differ in TV by at
most min(1, 2e/g+2e^3/(g^2 gamma)). The invariant-graph proof includes observable
state dressing, not just energy errors. It assumes neither short-memory decay nor
one-line response. The bound is sufficient and conservative; failure is not hardness.

A acts inside energy blocks as a commutator with the usual second-order H_2.
Single irreducible spin multiplets have scalar-plus-quadratic magnetization shifts;
multiple irreducible copies require matrix-valued coefficients. This is a serious
classical effective-spectrum comparator, with coefficient acquisition charged.
A completely solved maximum-spin sector contributes (n+1)(n+2)/(3*2^n) of the
response, so it cannot replace the full high-temperature spectrum as n grows.

An ideal QSVT construction implements the zero-sector projector, signed inverse
and products from explicit doubled-register Pauli block encodings. A linewidth-
matched spectral measurement of A, rescaled by d^2, gives the effective physical
law directly. It is not a sample of the memory law followed by an unjustified map.
For gamma=c d^2/J, the sufficient query budget loses the inverse-d power of the
straightforward direct quantum route but retains inverse-gap and size factors.
This is NOT a best-classical comparison, arbitrary fast forwarding, a gate/runtime
estimate or a novelty claim. Effective-Hamiltonian quantum algorithms are prior work.

## Next bounded mathematical task

Determine whether the global minimum-gap cost can be replaced by a justified
response-specific treatment of near resonances for the same uniform even chain.
No size-independent gap is available by assumption: a one-magnon calculation
already gives the upper bound g_n<=J[1-cos(pi/n)], and other spacings can be smaller.
An upper bound or a floating-point gap estimate is not the lower-bound promise
needed by an inverse/filtering algorithm. Obtaining that promise also has a cost.

Choose one route: retain the relevant near-resonant modes explicitly in an enlarged
slow sector, or regularize L_0^+ with a bounded function and derive a response-level
error. Show which matrix elements and spectral weights enter, preserve the output
law, and account for projector/filter access. Do not simply discard small weights:
Note 17 shows how they can matter at a shrinking resolved linewidth. An arbitrary
energy-window partition and the change in the observable require their own bounds.

Keep first-order couplings if the zero-sector cancellation cannot be justified.
Do not infer thermodynamic scaling, mixing, memory decay or all-classical hardness
from the four finite controls. The useful output remains normalized broadened
collective response at shared gamma/bins, not an unnecessarily exact line list.
Distinguish the fixed-n weak-field limit from large n and fixed physical linewidth.

Compare with classical symmetry reduction, sampling of effective coefficients,
recursion, restricted operators, tensor networks and projection-free approaches.
Classical effective-model acquisition may be reused across many samples. Quantum
queries must be converted to coefficient-access/preparation gates and repeated-shot
costs before a practical claim. The direct sampler of Note 15 remains available
without the inverse-gap promise; a limitation of this reduction does not close it.

No data acquisition, molecule selection, native package, large numerical sweep,
quantum compiler or third classical spin-off is the next step. Small computations
may check the derivation, not substitute for its proof or an application comparison.

## Executed evidence and preservation

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/slow_sector_v1/verify.py`
ran twice with identical JSON; -O/-OO refusal was checked. Fixed 2/4/6/8-spin
systems check the conserved overlap, 98 parity/multiplet blocks, effective
commutator identities and the solved-sector formula. Four binned 2/4-spin cases,
four abstract invariant graphs, six path-Laplacian identities, negative controls
and four invalid linewidths are recorded. These are complex128 mathematical checks
at tolerance 3e-9, not interval certificates, a QSVT circuit, measured spectra,
timing, a proof of arbitrary-size parity purity or a useful speedup. Continuous
bounds follow from the written proof. No previous scientific suite was rerun.

Climate/dynamics remain open; missing climate records block only their empirical
test. Manthan is paused, battery/operator routes parked, both spin-offs independent,
and Phase-2 Note 27 closed. Preserve earlier research, data, code, reports, licenses
and third-party rights. Only Quantum-Assisted-Algorithm-Discovery may be modified.
No contact, paid/unattended work, manuscript revival, release, merge, new repository
or administration change is authorized.
