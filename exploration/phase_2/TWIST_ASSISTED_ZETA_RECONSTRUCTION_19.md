# Use twists to reduce the extension degree of the quantum order queries

27 September 2026. Phase 2; PRX Quantum target; manuscript remains on hold.
Live base: 7365b8ead97fbd14bf7861de5b6108336970c739.
This is a candidate reconstruction refinement, not a new quantum primitive,
complete gate-resource estimate, established priority claim or useful advantage.
The separate Algebraic-Loop-Certificates project was not accessed or modified.

## Result and exact scope

For an odd-characteristic hyperelliptic curve of genus g, suppose q >= (2g+1)^2.
Its zeta numerator can be reconstructed from exact Jacobian orders for the curve
and a fresh quadratic twist over F_(q^n), with n<=g. Reusing the identity
K_(2n)=K_n*T_n leaves only g+ceil(g/2) group-order calls: every twist order T_n,
and curve orders K_n for odd n. The largest extension degree is g.

This replaces the particular reconstruction schedule in Section 8 of Kedlaya [1],
which calls degrees 1 through max(18,2g) in its direct large-field case. It does
not improve the theorem's general-curve scope, prove an optimal schedule, or
replace a special low-genus algorithm. For genus two, the established base-field
curve/twist pair already suffices. For genus three and sufficiently large q,
[2] also reconstructs from the base-field pair. Those methods remain preferred
comparators there. Twists and integer reconstruction are prior tools.

## Proof of trace recovery

Write P(T)=prod_i(1-alpha_i*T), with 2g reciprocal Weil roots, |alpha_i|=sqrt(q).
Let S_n=sum_i alpha_i^n. For Q=q^n define the exact group cardinalities

    K_n = prod_i(1-alpha_i^n),
    T_n = prod_i(1+alpha_i^n).

The second is the order of a NONTRIVIAL quadratic twist over F_Q itself. From
reciprocity, K_n=Q^g prod_i(1-alpha_i^(-n)), and similarly with plus signs for T_n.
The convergent logarithm series gives

    A_n := (Q/2) log(T_n/K_n)
         = S_n + sum_(odd k>=3) S_(nk)/(k Q^(k-1)).

Even powers cancel. The Weil bound yields

    |A_n-S_n| <= 2g sqrt(Q)/(3(Q-1)).

When q >= (2g+1)^2 this is less than 1/3 at every n>=1. Computing A_n to absolute
error at most 1/12 therefore permits exact nearest-integer recovery of S_n.
No unknown higher trace has to be obtained first.

With c_0=1, Newton's identity k*c_k=-sum_(i=1)^k c_(k-i)*S_i recovers c_1,...,c_g.
Reciprocity c_(2g-k)=q^(g-k)*c_k supplies the remaining coefficients. Further,
K_(2n)=prod_i(1-alpha_i^(2n))=K_n*T_n. Processing n in increasing order derives
even K_n from earlier data. This uses only an identity of cardinalities, not a
claimed direct-product or subgroup decomposition.

## Certified arithmetic rather than an assumed precision oracle

Set z=(T-K)/(T+K). Then (Q/2)log(T/K)=Q*sum_(j>=0) z^(2j+1)/(2j+1). After m terms,
the numerical remainder is at most

    Q*|z|^(2m+1)/((2m+1)*(1-z^2)).

The implementation uses exact Fraction arithmetic until this is <=1/12, adds
the analytic trace-tail bound with sqrt(Q) conservatively replaced by ceil(sqrt(Q)),
and requires exactly one integer in the resulting interval. It never subtracts
approximate logarithms of enormous integers. Under the field-size condition,
|z| <= tanh(2g*artanh(Q^(-1/2))) < tanh(1), so O(log Q) series terms suffice and
all arithmetic has polynomial bit length. This is not exponentially precise
analog measurement: the quantum subroutine must supply exact binary orders.

The reconstruction is conditional on those orders being correct. It does not
verify that an incomplete generating set spans the whole Jacobian, or mistake
the order of an element or the group exponent for its cardinality. Newton
integrality and regenerated-order checks catch some inconsistencies, not all
possible false input data. Allocate the allowed total quantum failure probability
across the g+ceil(g/2) queries. Reuse needs no independence assumption for a union
bound on errors.

## What parameter has actually improved?

For g=10, the indicated generic schedule has 20 calls, maximum degree 20, and
sum of degrees 210. Direct pairs at degrees 1..10 use 20 calls of maximum degree
10; reuse reduces this to 15 calls with degree sum 80.

These are query-schedule counts, not measured gate or wall-clock improvements.
A field element over F_(q^n) uses about n*log2(q) bits; a Mumford representation
stores O(g) such elements. Lowering n changes a real size parameter of the
reversible group arithmetic. Its complete register/workspace count and time are
not asserted to halve. The cost of constructing fields, nonsquares, generating
sets, canonical arithmetic and quantum order finding remains.

The reconstruction condition is weaker than the directly invoked generating-set
construction in [1], which uses 16g<sqrt(q). Under that stronger condition the new
reconstruction can replace the specified schedule for this hyperelliptic subclass.
We have NOT eliminated the generating-set condition or supplied a new general
small-q base-change algorithm. Other class-group access methods may have different
costs. Odd characteristic and a hyperelliptic twist are substantive restrictions.

## Fresh-twist negative control

A quadratic twist defined over F_q becomes trivial over an even-degree extension.
Its eigenvalues there are (-alpha_i)^n=alpha_i^n, not -alpha_i^n. Reusing that curve
would make the wrong ratio equal to one. One must choose a nonsquare in each F_Q;
this is a classically sampleable and exponentiation-checkable field element.

For y^2=x^5+x^2+x+1 over F_5, the previously checked polynomial is (1,4,10,20,25).
Over F_25 the curve order is 720, the fresh twist order is 512, and the extended
base twist has order 720. The correct S_2=-4 is recovered from 512/720; the wrong
ratio 720/720 falsely returns zero, no matter how accurately its logarithm is
computed.

Treating the original curve over F_25 yields P=(1,4,-10,100,625). Three supplied
orders K_1=720,T_1=512,T_2=413712 suffice for the general schedule. Derive K_2=368640.
The scaled logs are -4.261582337... and 36.046725470..., rounding rigorously to
S_1=-4 and S_2=36. This is a transparent control, not an improvement over the
known two-order genus-two shortcut or a hard workload.

## Classical comparison and independent consequence

All classical postprocessing, including this cancellation, is available to both
sides. Any useful quantum gain must come from economically obtaining the group
orders. Fixed-genus methods, fixed small characteristic, special factorizations
and shared work across primes remain legitimate classical alternatives. A 2025
preprint [3] improves genus-two L-polynomial lifting after its reduction mod p
is already available; that cost is not the full point-counting cost. No native
performance comparison was run.

Exact coefficients have an independent structural use: the Frobenius polynomial
classifies an abelian variety over F_q up to isogeny [4]. For a curve this concerns
its Jacobian, not curve isomorphism; it does not return an explicit isogeny map.
It motivates why an approximate answer near q+1 can be insufficient, but does
not establish a useful quantum-sized workload or a broad industrial consequence.

Our candidate contribution is reducing the algebraic instances submitted to an
established quantum subroutine, rather than faster classical point enumeration.
The priority of this particular general logarithmic reconstruction is unresolved.
No short keyword search establishes novelty, and a factor improvement in one
proof's query schedule is not automatically a PRX Quantum result.

## Work actually performed

The standard-library diagnostic reconstructs 344 known reciprocal Weil polynomials:
164 base changes of prior genuinely enumerated genus-two curves and 180 explicitly
factored Weil-polynomial controls of dimensions up to 12. The latter are not
asserted to be curve Jacobians and have an easy visible factorization. New group
orders were computed classically from the supplied polynomials, not with a quantum
order finder or by independently enumerating all larger-extension Jacobians.

Checks: 1298 exact traces, 140 independent companion-determinant order calculations,
624 degree-doubling identities, and fresh-twist/unsymmetrized-log/input-precision
negative controls. Maximum observed series length was eight; largest exact
rational component used 13325 bits and largest supplied order 4464 bits. These
are arithmetic diagnostics, not qubit counts or a performance forecast.

The new report regenerated byte-for-byte. The previous zeta checkpoint verifier
was run unchanged from a fresh extraction and passed: 164 original records,
348 independently enumerated point counts and 32800 recurrence checks. No older
root verifier, quantum group circuit, native Sage/Magma benchmark or hardware run.

Companion source SHA256:
af7db8595ff08ba63fa46cbfa8a4f96d13a78e4bc9941c8d03d0c13ea1607df2
Exact result SHA256:
c18a9d32099a459487e651e4f7e61eca4ac7421eeaacce20f8a66be30e7b66d2
Full proof, code, prior data, report and verifier are in the conversation archive
Quantum_Discovery_Twist_Reconstruction_Scout.zip. Run `python verify.py` after
unpacking. The condensed note, not that code, is committed in this scoped change.

## Next gate

Determine whether the reconstruction schedule or a sharper variant already exists,
then price an explicit reliable Jacobian group-order interface. Generating sets
and reversible arithmetic may dominate after this reduction. Keep alternative
compact-output algebraic tasks open if those costs or independent usefulness do
not justify further development. Manuscript on hold; no spinoff work, outside
contact, submission, paid computation or unattended work occurred.

## Primary sources and inspection scope

[1] K. S. Kedlaya, Quantum computation of zeta functions of curves, Computational
Complexity 15 (2006), 1-19. https://arxiv.org/pdf/math/0411623
Parsed Sections 7-8, M=max(18,2g) schedule and large-field assumptions; PDF index10
visually checked. No implementation or original resource count reproduced.

[2] A. V. Sutherland, A Generic Approach to Searching for Jacobians, Math. Comp.
78 (2009), 485-507. https://arxiv.org/pdf/0708.3168
Parsed Lemmas3-4 and Section4.1. Twist-assisted low-genus reconstruction is prior
art. Several screenshots failed; no table-derived benchmark claim is used.
Also inspected Kedlaya-Sutherland, https://arxiv.org/pdf/0801.2778.

[3] J. Shi, Lifting L-polynomials of genus 2 curves, arXiv:2508.11028v1 (2025).
https://arxiv.org/html/2508.11028v1
Full HTML method and lifting-input assumptions inspected; no native run.

[4] T. Dupuy, K. S. Kedlaya, D. Roe, C. Vincent, Isogeny Classes of Abelian
Varieties over Finite Fields in the LMFDB. https://arxiv.org/pdf/2003.05380
Primary isogeny/polynomial statement and computational context inspected.
No current database census, new classification or application speedup claimed.
