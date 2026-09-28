# Current task: low-frequency memory versus effective slow-mode compression

28 September 2026. Active branch: `research/prx-quantum-phase2`.
Scientific phase 3; manuscript preparation remains on hold.

Read [exchange memory 17](../exploration/phase_3/EXCHANGE_MEMORY_17.md),
[spectral boundary 16](../exploration/phase_3/SPECTRAL_BOUNDARY_16.md), and
[model comparison 15](../exploration/phase_3/SPECTRAL_MODEL_STRUCTURE_15.md).
Mathematical models and quantum integration precede implementation. Direct samples
remain permitted; quantum-free deployment or a learned classical program is not
required. No useful quantum advantage is established.

## Completed model-level step

For the even alternating-offset chain, the normalized collective mode o obeys
L_d o=d v, with v the explicitly known staggered raising mode. Orthogonal projection
gives B_d=Q L_d Q=L_d-d(|o><v|+|v><o|), and the physical resolvent is
G_d(z)=1/[z-d^2 F_d(z)], F_d(z)=<v,(z-B_d)^(-1)v>. These are exact projection/Schur
identities built on established memory-function methods, not a new framework.

The projected generator is accessible quantumly through L_d plus two reflections
about known sublattice observable states. Preparing those states requires no
unknown eigenbasis. Their preparation, inverses, coefficient access, simulation
normalization, precision and shot counts still cost resources. The mathematical
identity is not a compiled circuit or demonstrated speedup. Memory spectral
samples are not themselves physical NMR-response samples.

A finite-window bound on F_d(z)+i kappa gives a sufficient TV certificate for a
single Lorentzian response of width gamma+d^2 kappa. The certificate accounts for
the unbroadened second-moment tail and scalar estimation error. Its failure is
not a hardness test. Short-time curvature does not prove short memory. The optional
short-time quantum estimate needs an independently justified memory-tail bound;
otherwise it recovers the linewidth time scale. Finite closed systems recur.

The exact two-spin control shows that dropping a memory pole of vanishing mass
can yield an order-one spectral error when linewidth and bins scale as d^2/J.
At fixed linewidth the discrepancy instead vanishes. A corrected classical
pair at +/-d^2/J has a proved vanishing error in that same resolved limit.
This control rejects a naive approximation, not classical effective models and
not the quantum-sampling direction. It is not an application benchmark.

## Next bounded mathematical test

Remain with the uniform even open chain and the same collective observable.
Determine the low-frequency structure of the projected memory as a function of
n, d/J and gamma/J, rather than increasing a numerical Krylov cutoff without a
structural reason. Keep the uniform-field and exact two-spin limits as controls.

A concrete first calculation is the overlap of v with the conserved operator
sector of L_0=[H_J,.], then the first nonvanishing perturbative/effective coupling
inside that sector. Establish the spectral and symmetry assumptions used. Do not
silently assume a size-independent gap to the remaining operator frequencies or
interchange small d, large n and small gamma limits. Small denominators and their
cost must remain in the comparison.

Use this to decide whether the resolved collective response has a compact
classical slow-mode description, a justified short-memory approximation, or a
specific residual many-body calculation. A low-rank identity does not ensure
cheap dynamics; a small perturbation does not guarantee a uniform spectral error.
Compare with symmetry reduction, perturbative resummation, recursion, restricted
operators, tensor networks, projection-free memory methods and relevant complex-
time spectral methods. Best-known upper bounds are not classical lower bounds.

Retain Note 15's direct linewidth-matched quantum sampler. The projected-memory
route is an additional quantum integration, not a requirement to fit a classical
program first. A shorter maximum evolution time is useful only after shots,
tail/accuracy certification, state access, repeated inference and classical
alternatives are included. Neither route is favored by ignoring its costs.

No new molecule selection, dataset acquisition, native package, large simulation,
solver framework, circuit compiler or third spin-off is the next step. An affordable
calculation may check a derived statement, but finite examples cannot establish
short memory or thermodynamic scaling. Keep the broader dynamical route open.

## Execution and preserved evidence

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/exchange_memory_v1/verify.py`
passed twice with identical JSON. -O/-OO refusal and five invalid-input controls
were checked. Three fixed two/four-spin models check projection/reflection and
resolvent identities, memory symmetry, frequency envelopes, three binned bounds
and truncated-memory integrals. Four d/J choices check exact dimer formulas,
the resolved-limit error and the corrected classical pair. The note records hashes.

These are complex128 diagnostics at tolerance 3e-10, not interval proofs,
experimental spectra, a quantum run or performance measurements. Continuous bounds
follow from the written arguments. No prior scientific verifier was rerun and no
upstream code, measured data or model weights were imported. The relevant primary
PDF was read as text; its screenshot attempt failed, and no figure supplied a
numerical result. Priority and fast-memory assumptions remain unestablished.

Climate/dynamics remain open; missing climate files block only their empirical
test. Manthan is paused, battery/operator candidates remain parked, both classical
spin-offs remain independent, and Phase-2 Note 27 stays closed. Preserve earlier
proofs, code, data, reports, manifests, licenses and rights. Modify only Quantum-
Assisted-Algorithm-Discovery. No outside contact, paid/unattended work, manuscript
revival, release, merge, new repository or administration change is authorized.
