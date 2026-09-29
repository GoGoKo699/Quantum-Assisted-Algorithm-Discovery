# Current task: test the classical acquisition cost of one activity statistic

29 September 2026. Branch: `research/prx-quantum-phase2`.
Model-first; direct samples allowed; manuscript on hold. No new repository needed.

Read [activity claim 28](../exploration/phase_3/EMISSION_ACTIVITY_CLAIM_28.md) and
[strategic revision 27](../exploration/phase_3/STRATEGIC_REVISION_27.md).
The target is now explicitly one bounded two-window statistic, not full histories.
The new calculation does not solve the earlier fine-record output contract.

## A specific quantum mechanism is now stated

In the driven dissipative Ising family start from the ground product state and
count all emitted photons K1,K2 in consecutive windows Delta. Set
s=u/(n kappa Delta), u=1, and estimate
G=Cov(exp(-s K1),exp(-s K2)) to a justified additive epsilon and confidence.
This is a bounded measure of temporal activity dependence, not a complete count
law, switching rate, stationary phase claim or relative-error rare-event target.
The physical task motivates activity correlations; this particular bounded
transform is chosen here and is not asserted to be an experimental standard.

For source matching use the periodic nearest-neighbor family of Rose et al.,
including its V/kappa=250, Omega/kappa=50 finite-size slice as a reference.
This explicitly differs from the previous open/equal-scale controls. No all-size
metastability is assumed. Delta and accuracy must come from a useful prediction;
neither is chosen solely to defeat a classical approximation. The ground transient
and full horizon T=2 Delta are retained, with no free equilibrium preparation.

Two absorbing flags exactly encode Z1=E exp(-sK1), Z2 and Z12=E exp(-s(K1+K2)).
Flag-zero probabilities give these three numbers and G=Z12-Z1 Z2. The total system
marginal obeys the original Lindbladian. No full photon tape or count cutoff is
needed for this statistic. Both flags and the system are simulated coherently;
other simulation/environment workspace is additional, not a free reset resource.

Use established high-accuracy Lindblad algorithms, retain their purification,
and use standard amplitude estimation with the circuit and its inverse. This gives
~O(1/epsilon) evaluations instead of the generic O(1/epsilon^2) sampling dependence.
It cannot be applied to already measured laboratory records. With explicit local
term access a sufficient total bound is ~O((n+edges)(1+Gamma T)/epsilon),
Gamma=n|Omega|/2+edges|V|/4+n kappa. T, input precision, workspace, routing and
fault-tolerant costs remain. This is not an all-classical separation or novelty claim.
Using the old first-order splitting alone can erase the precision gain; the
high-accuracy channel theorem is a material ingredient, not a free exact step.

## Decisive comparison, not another general construction

The exact classical target is THREE tilted contractions:
Z1=Tr exp(Delta L) exp(Delta Ls) rho0,
Z2=Tr exp(Delta Ls) exp(Delta L) rho0,
Z12=Tr exp(2 Delta Ls) rho0, Ls=L+(exp(-s)-1)J.
A supplied adequate small tilted generator evaluates these cheaply without any
Monte Carlo. Compare its ACQUISITION AND VALIDATION cost, not just supplied rates.
Include Macieszczak et al.'s within-phase/transient corrections, coherent
few-excitation methods, tensors/clusters and direct tilted propagation.
Classical trajectory estimators can use the continuous bounded scores and variance
reduction; do not add extra flag-marking noise to weaken them.

The input-computable bound ||Ls-L||_diamond<=u/Delta makes long windows a small
perturbation and may favor classical metastability. It is not by itself a
nonnormal perturbation or all-size gap theorem. Small G at the useful tolerance
is also a legitimate cheap answer. Independent coherent emitters can already
have temporal correlations, so nonzero G alone is not evidence of many-body hardness.

Next assess whether existing phase/symmetry/tensor methods obtain this G adequately
and cheaply in the source-matched slice, with the ground transient retained.
A specific surviving acquisition bottleneck warrants one focused resource or
native comparison. A cheap adequate tilted model ends this claim's priority.
Do not add another flag framework, generic estimator proof, small-instance census,
harder graph or finer detector merely to keep the candidate alive.

## Evidence and preservation

`python experiments/activity_flags_v1/verify.py` uses NumPy and SciPy. The final
checker ran twice identically; -O/-OO and six invalid inputs were rejected. One
three-emitter equal-scale ring checks the flag/tilted identities and physical
marginal, not the published metastable parameter regime. An exact parity-control
calculation, independent coherent emitters and a supplied classical two-state
model prevent invalid simplifications. No amplitude-estimation circuit, high-order
channel compiler, large-system calculation or speedup measurement was run.
No earlier verifier was rerun; no upstream code/data imported.

Preserve every earlier scientific note, source, report, license and rights notice.
Other mechanisms remain available; the two classical spin-offs remain independent.
Only Quantum-Assisted-Algorithm-Discovery may be modified. No external contact,
paid/unattended work, manuscript revival, new repository, merge, release or admin.
