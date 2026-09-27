# Current task: independently audit the all-field reconstruction candidate

Active branch: `research/prx-quantum-phase2`. Target: **PRX Quantum**.
Manuscript remains **on hold**. Read the phase-2 charter and
`exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md`.

## Scope

Modify only Quantum-Assisted-Algorithm-Discovery. Preserve other branches,
LICENSE and historical experiment/source/report bytes. Do not merge the previous
sharing-core PR, revive its manuscript, or modify the separate classical spinoff.
The broader aim remains useful compact structural information obtained quantumly
from an explicit input, with classical execution afterwards. Zeta is provisional.

## New precise candidate

For every integer field-size parameter q>=2 and genus g>=32, put h=g-2.
A reciprocal integral Weil polynomial of degree 2g is reconstructible from
ordinary cyclic resultants at D_h={1,...,h} union {2,4,...,2h} in polynomial time
in g and log q. Thus h+ceil(h/2)<2g selected exact-count requests suffice and
maximum degree is 2g-4. For actual curves this includes every finite field and
does not require hyperellipticity or physical twist access.

The proof uses k_n=max(2,floor(h/n)) in the published normalized Mobius formula.
Every needed count remains in D_h. A three-case rational envelope proves the
error in S_n/n is below 1/3 uniformly for g>=32 and q>=2. Newton's known residue
information enables coefficient rounding; the final two coefficients come from
the inherited endpoint equations. Range reduction of each rational logarithm
is included, giving a polynomial-bit-time decoder at small q.

The primary statements inspected do not subsume this exact bound, but publication
priority is NOT established. The same classical/quantum reconstruction ingredients
are prior work. Do not call an absent matching search result a novelty proof.
No optimality or all-field genus-3..31 theorem is supplied. Threshold 32 is only
a sufficient constant, not an intrinsic transition or a proposed next target.

## Next decisive audit

Audit the new theorem independently of its implementation: analytic tail bounds,
Newton-residue rounding, integer endpoints, polynomial bit complexity and the
precise Weil/reciprocity promise. Seek an actual predecessor with the same or
stronger finite selected-query guarantee; distinguish it from infinite-sequence
uniqueness, generic palindromic results and initial-consecutive-sequence conjectures.
A correction should preserve historical records and explicitly identify the
scope of any changed claim rather than silently editing expected evidence.

The right publication object, if the statement survives, is a reconstruction
query theorem. It is not another twist-schedule comparison or a numerical gate
speedup. A separate reconstruction-theory repository becomes appropriate only
when the independent audit supports a distinct worthwhile research programme.
No new repository is requested by this checkpoint. Do not let code volume or
an available implementation task determine that decision.

## Boundaries that still govern the quantum project

The theorem receives TRUE cardinalities. It does not authenticate supplied data,
construct a curve, or perform quantum order finding. In particular the previous
large-field generator/arithmetic restrictions are not removed. Kedlaya's actual
order-acquisition Proposition 11 has its own field-extension condition. An
all-field reconstruction theorem is not automatically an all-field implementation
with fewer than 2g complete quantum invocations.

Keep Note 27's closed source-aware comparison: known quadratic splitting and
reuse let the ordinary route execute the same underlying calls as the signed
route. The new result does not reopen that claimed advantage. All classical
competitors receive the same decoder and may bypass group orders altogether.
Retain the preceding stopping, backend and resource-accounting restrictions.

## Verification actually performed

Run `python experiments/all_field_reconstruction_v1/verify.py` for the new
source-hash and exact-report checks. Seven supplied Weil controls recover 489
coefficients and 227 traces; they are not asserted to be curve Jacobians.
The uniform proof is not inferred from finite tests. All four preceding current
verifiers passed unchanged from the mounted Note-27 checkpoint. Historical root
and 164-curve suites were not rerun; full checkout failed on DNS. No native point
counter, quantum circuit, hardware, paid computation or external contact ran.
No unattended work, unrelated merge, repository administration or submission is
authorized. Manuscript preparation remains on hold.
