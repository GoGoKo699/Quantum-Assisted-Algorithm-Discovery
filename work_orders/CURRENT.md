# Current task: decide the sampling regime after pricing classical trace acquisition

29 September 2026. Branch: `research/prx-quantum-phase2`.
Model-first exploration; direct quantum samples allowed; manuscript on hold.

Read [trace acquisition 23](../exploration/phase_3/TRACE_ACQUISITION_23.md),
[response readout 22](../exploration/phase_3/RESPONSE_READOUT_22.md), and the
quantum/spatial constructions in Notes 15 and 21. No new repository is needed.
The classical comparator is not a renewed classical-program output requirement.

## Completed acquisition budget

For O=sum S_i^+ on k spins, random-phase trace estimation of the normalized
high-temperature correlation has mean-square error at most 2/(R 2^k) for R
independent GLOBAL Z4 phase vectors. This holds at every time. The collective
identity Tr[(O^dagger O)^2]=2^k k^2/2 and a Schatten bound establish it without
assuming mixing, a spectral gap, or a small tensor rank. The same probes may be
reused across times; errors at different times are not independent.

With the existing clock weights a_h and A_2=sum a_h^2, the repaired Fourier-bin
sampler has statistical error at most epsilon_stat with probability >=1-beta
when R>=max(1,ceil(4 A_2/(2^k beta epsilon_stat^2))). Clock, wrapping, deterministic
propagation, output arithmetic and the full-chain spatial error remain separate.
The bound concerns a once-constructed table; repeated draws share its error.
Do not turn a per-draw guarantee into an M-draw joint guarantee without accounting.

Use the known trace normalization, not a random denominator. Independent phases
on k individual spins do not satisfy the global-phase variance formula. The
product-phase counterexample in Note 23 does not prohibit other efficient designs;
it rules out that particular substitution. Arbitrary global random states are
not assumed cheaply preparable on quantum hardware.

## A strong classical route now has an explicit symbolic cost

Propagate U(t)r and U(t)Or, contract with O^dagger, and average. Each vector has
2^k entries, not the 4^k entries of a full operator. Matrix-free H and O actions
cost O(k 2^k). A sufficient grid/Taylor budget is O(R N k 2^k(q+1)), with
q=O(W tau+log(N/delta_U)), W>=||H||. Vector accuracy delta_U gives correlation
error <=6k delta_U. Finite-bit coefficient and rounding errors still count.
One sequential probe uses O(2^k+N+B) working words plus indexing/workspace.
This implementation evolves to the FULL last lag; it does not automatically
inherit half-time evolution from the distinct operator-tensor method in Note 22.

Random-phase trace methods and dynamical typicality are prior work. A growing
Hilbert dimension reduces statistical probe count but makes each propagation
more expensive. The R=1 bound at one specified 26-spin accuracy setting is not
an executed 26-spin calculation, a spatial-window certificate or a cheap scalar
query. Actual tensor compression, symmetry reduction and better propagation
algorithms can improve this classical upper bound. It is not a lower bound.

Classical linked-cluster methods already combine with typicality. Signed
subtraction can cancel physical boundary errors while amplifying probe noise;
the quantum/classical positive-mixture bound cannot be copied to such a subtraction.
No linked-cluster convergence theorem was proved for this collective response.

## Next bounded decision; do not accumulate more generic readout machinery

For the same intermediate d/J~1 response, give one explicit resolution/sample-count
comparison using the strongest justified classical option, not dense diagonalization
alone: typicality/full-time pure-state propagation, half-time operator tensors,
certified recursion and any valid translation/effective reduction. Compare with
direct local quantum spectral sampling at the same gamma, bin law and M draws.
The direct route may avoid classical trace acquisition but repeats state/clock
preparation, coefficient access, controlled evolution and readout for each draw.

Identify the structural reason that any proposed quantum regime survives those
alternatives. A crossing of nonoptimal upper bounds, a large sufficient spatial
window, or full-vector entanglement is not an all-classical hardness result.
Retain uncertainty when necessary. If no specific reason survives, broaden the
mechanism comparison instead of inventing a difficult molecule or conducting
more small-size demonstrations. The parent objective is a useful quantum result,
not another classical approximation project or a new simulator framework.

## Executed evidence and preservation

The final NumPy diagnostic ran twice with identical JSON; -O/-OO and six invalid
inputs were rejected. It actually acquires 255 correlations for ONE ten-spin
block with eight fixed-seed probes, using matrix-free two-vector propagation.
A separate magnetization-block diagonalization validates that small calculation.
Its finite-clock bin TV is about 0.006989, not a high-probability large-block result.
The other probe-budget rows are analytical evaluations only. Phase-ensemble,
observable-moment and invalid product-state controls check the proof ingredients.

No native NMR or upstream typicality package, tensor implementation, quantum
circuit, experimental spectrum, large-block run or timing benchmark was used.
No prior verifier was rerun; earlier scientific files and rights are unchanged.
Climate/dynamics remain open; Manthan is paused; battery/operator routes parked;
both spin-offs independent; Phase-2 Note 27 closed. Modify only Quantum-Assisted-
Algorithm-Discovery. No contact, paid/unattended work, manuscript revival, release,
merge, new repository or administration change is authorized.
