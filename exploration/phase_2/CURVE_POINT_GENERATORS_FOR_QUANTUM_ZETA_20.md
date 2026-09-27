# Curve points suffice for the generating-set interface

27 September 2026. Phase 2; PRX Quantum target; manuscript remains on hold.
Live base: 29f97c5d8ee7c6ef7d3c6a5bc4bc032bab64863e.
This is a source-led integration argument with exact small checks, not a new
quantum primitive, priority claim, complete gate estimate or useful advantage.
Algebraic-Loop-Certificates was not accessed or changed.

## 1. The setup need not sample the whole Jacobian uniformly

The zeta algorithm needs generators and explicit uniquely encoded group
arithmetic before quantum group-order computation. Kedlaya [1, Section 7]
gives a general large-field construction through prime divisors and an argument
comparing samples with uniform group elements. It is a sufficient route, not
a claim that all implementations must make the samples uniform on the group.

For C:y^2=f(x), squarefree of odd degree 2g+1 over an odd-characteristic field
F_Q, the point O at infinity is rational. Ordinary rational points give group
elements [P-O] with a two-field-element description. Their distribution is
supported on about Q elements of a group of size about Q^g. Despite being far
from uniform on the Jacobian, these samples can generate it efficiently.

Generation from curve points is established by Voloch [3]. The needed explicit
character-sum bound is given in [2]. No novelty is claimed for this general
principle. The present question is whether it removes unnecessary setup from
the specific quantum zeta computation, without hiding another oracle.

## 2. Explicit subgroup-escape bound

For every nontrivial character chi of G=J_C(F_Q), the standard bound is

    |sum_(P in C(F_Q)) chi([P-O])| <= (2g-2) sqrt(Q).

It follows from [2, Theorem 3] with the identity morphism; its hypotheses hold
because the identity cannot factor through a nontrivial unramified cover.
The chosen rational base point and character interpretation are explicit.

Let mu be the uniform AFFINE-point law, N_aff=|C(F_Q)|-1. Removing infinity
adds at most one to the numerator, so

    |E_mu chi| <= beta
    beta <= ((2g-2) sqrt(Q)+1)/(Q-2g sqrt(Q)).

Under Q>=64g^2, the denominator is at least 3Q/4 and numerator at most Q/4.
Hence beta<=1/3. This is a conservative sufficient condition, not the best known
or necessary field-size threshold. Exact point counts are not needed to use it.

For any proper subgroup H of index d>=2, character orthogonality gives

    mu(H) <= 1/d+(1-1/d) beta <= 2/3.

Thus every proper subgroup is escaped with probability at least 1/3. We do not
need to identify the subgroup or perform membership tests during collection.

For m independent samples, failure to generate G implies that some nontrivial
character is one on every sample. Its kernel is proper. Union-bounding over
|G|-1 nontrivial characters gives

    Pr[incomplete generator list] <= (|G|-1)(2/3)^m.

Choose U=(ceil(sqrt(Q))+1)^(2g), a known integer upper bound on |G|, and take the
least m with U*(2/3)^m<=delta. This requires

    m=O(g log Q+log(1/delta))

samples. The list is not necessarily minimal or independent. Its completeness
is probabilistic, not a deterministic certificate for the realized list. A
quantum routine can correctly return a proper subgroup's order if the supplied
list is incomplete; that error must remain in the overall budget.

## 3. An exact classical sampler without counting points first

Choose uniform x in F_Q and an independent fair branch bit. Find the roots of
y^2=f(x). With two roots use the branch bit to select one in a fixed canonical
order. With one root y=0, accept only branch bit zero. With no roots, retry.
Each affine point occupies exactly one of 2Q equally likely slots. The returned
point is uniform, and acceptance is N_aff/(2Q)>=3/8. The expected number of trials
per returned point is therefore at most 8/3.

Horner evaluation and verified finite-field square roots have polynomial cost
in g and log Q, with an explicit field representation. A nonsquare can be found
by uniform trials and Euler testing. No group order, zeta numerator, large data
table or coherent point-sampling oracle is assumed. The source diagnostic
implements Tonelli-Shanks over the small prime fields and checks it against
brute-force roots; it is not a full extension-field library.

Accepting a double root on both branch bits is wrong. For y^2=x^5+x over F3,
that version produces TV error 1/6 in the conditional point distribution.

## 4. Integrating the previous twist schedule

If the original q>=64g^2, every Q=q^n used by the preceding reconstruction meets
this generating-set condition and its trace-rounding condition. Use a F_Q-
nontrivial twist separately at each field, retaining the previous warning that
a base-field twist can become trivial over an even extension.

For t=g+ceil(g/2) order calls, allocate generator failure delta_gen/t per list,
and separately budget the quantum group-order error. A union bound controls
the complete reconstruction; independence between different calls is unnecessary.
The general finite-abelian-group algorithms [5] accept generators and unique
encodings, not a known group cardinality or uniform whole-group preparation.

The resulting algorithm-level pipeline is

    explicit curve
      -> ordinary classical curve-point generator lists
      -> quantum Jacobian cardinality calculations
      -> twist-assisted exact trace reconstruction
      -> classical counting recurrence.

This replaces the directly invoked general generator route for this declared
hyperelliptic subclass; it does not improve the original theorem for all curves,
claim an optimal setup, or supply a new general small-field base-change method.
The previous 16g<sqrt(q) assumption is not inherited by this separate proof.

A conservative parameter-only illustration uses g=10, q=1000003 and 15 order
calls. A total 1/100 generator failure budget requires 359 points per base-field
list and 3426 at extension degree ten, 27536 across the schedule. These are
bounds, not generated large-curve lists or quantum resources. No curve with those
parameters was selected. The count is not optimized using group-rank information.

## 5. The quantum arithmetic is still general Jacobian arithmetic

Degree-one generators do not imply degree-one coherent accumulators. Sums and
precomputed powers become arbitrary reduced divisors with degree up to g.
A Mumford data register needs O(g log Q) bits plus real arithmetic workspace,
exponents and controls. At n=g this can already be O(g^2 log q) data bits.
These are representation bounds, not a total qubit count.

Repeating the original point once for every unit of a binary exponent would
restore an exponential cost. Efficient controlled powering must use general
translations by precomputed powers. We have not compiled their elementary gates.

On valid canonical encodings a fixed translation is a permutation. Fixing invalid
encodings extends it to a total bit-string permutation. An out-of-place reversible
calculation, register swap and inverse uncomputation can implement it in-place;
validity tests and work registers must be counted. This completion was checked
on all labels of a small explicit coefficient encoding, not only group elements.

## 6. Negative controls and actual checks

For y^2=x^5+x^4+x over F3 the affine points are (0,0),(1,0). Their classes generate
four elements, whereas the full Jacobian has eight. More point samples cannot
repair this deficiency. This is outside the large-field condition and consistent
with the established small-field exceptions [3].

For y^2=x^5+x over F3 the Jacobian has order twelve, but point-generator orders
are 2,6,6. Their lcm is six and their product 72: neither is the cardinality.
Powers of (2,1) have reduced degrees 1,2,2,2,1,0, exposing the accumulator issue.
A ten-bit padded coefficient encoding has 12 valid and 1012 invalid labels.
Three translations give 3072 full-label inverse/clean-work checks, with 3036
fixed-invalid-label checks. The ten bits describe DATA only, not the full machine.

All 162 squarefree monic quintics over F3 and two F5 controls were tested against
independent reduced-pair enumeration. There are 36456 exact binary group products,
14336 associativity triples on four fixed curves, and point-generation checks
on 164 curves. Point classes generate the whole group in 125 controls and a
proper subgroup in 39; the largest missing index is five.

Eighty distributions on F2^2 check character/subgroup inequalities and 800 exact
generation probabilities. Uniform sampling of its three nonzero elements has
TV distance 1/4 from group-uniform and failure 3^(1-m) after m samples. Weights
(0,1022,1,1) still have generating support but fail after ten draws with probability
above .98. Mere support generation is not a quantitative sampling guarantee.

The prime-field square-root routine was checked on 265 field elements. The
point sampler was additionally checked on y^2=x^5+x+1 over F257: 280 affine points,
acceptance 140/257. That larger Jacobian was not enumerated or certified. The other
inherited polynomial x^5+x^2+x+1 was initially rejected as singular modulo257;
only a smooth input is eligible for this theorem.

No quantum group-order routine, native Sage/Magma counter, elementary-gate compiler,
hardware run or useful advantage benchmark was executed. The character-sum theorem
is a cited mathematical input, not a conclusion drawn from the finite checks.
The exact report was regenerated. The preceding twist verifier passed unchanged:
344 reconstructions,1298 traces,140 determinant orders,624 doubling identities.
Older root/historical verifiers were not rerun.

## 7. Research decision and provenance

Retain this as a tested integration lemma from existing theory, not an independent
PRX Quantum result. Classical competitors get the same improved setup. All fixed-
genus, small-characteristic, special-family and amortized classical methods from
the earlier audits remain eligible. The novelty and usefulness of an end-to-end
quantum workflow are still unresolved.

The next bottleneck is the implemented group-cardinality algorithm, especially
coherent general Jacobian translations and the number of generators/exponents.
Do not infer a hardware speedup from a polynomial theorem or a simpler sampler.
The current task remains useful quantum advantage, not classical spinoff development.

Companion source SHA256:
c7fcffb104fde382bb8f9f1c7457412ffc487083546dc957b33c8d1f430495e2
Exact results SHA256:
f98ba8501617fe64c36c933aff64a737a4540ae9930a64d20beb3c1c2855eb3b
Expanded proof SHA256:
7e9e4ac5ed1fd508020d44ba764c575742814f289d2a7b362026805a8cdd5626

The source, results, full derivation, unchanged inherited polynomial helpers and
verifier are in Quantum_Discovery_Curve_Generators_Scout.zip in the conversation.
Run `python verify.py` after unpacking. Only this condensed note is committed.
Original MIT notices, historical research and other branches remain unchanged.

## Primary sources and inspection scope

[1] Kedlaya, Quantum computation of zeta functions of curves (2006),
https://arxiv.org/pdf/math/0411623 . Parsed Sections6-7 and generator assumptions.
[2] Farashahi, Fouque, Shparlinski, Tibouchi, Voloch, Indifferentiable deterministic
hashing to elliptic and hyperelliptic curves, Math.Comp.82 (2013),491-512,
DOI10.1090/S0025-5718-2012-02606-8. https://eprint.iacr.org/2010/539.pdf
Parsed primary preprint Section4, Example1, Lemma1, Theorem3 inspected. Published
metadata checked at the authors' institutional record. No new hash construction
or cryptographic use is proposed here.
[3] Voloch, Jacobians of curves over finite fields, RMJM30(2) (2000),755-759,
DOI10.1216/rmjm/1022009294. https://web.ma.utexas.edu/users/voloch/oldpreprint.html
Author's description of point generation and small-field exceptions inspected;
full article retrieval failed. The quantitative proof here relies on inspected [2].
[4] SageMath official documentation, Jacobian morphisms in the Picard group:
https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/hyperelliptic_curves/jacobian_morphism.html
Mumford/Cantor scope checked; no solver code copied or package executed.
[5] Cheung and Mosca, Decomposing Finite Abelian Groups (2001),
https://arxiv.org/abs/cs/0101004 . Established quantum backend; not implemented.

Web PDF screenshots repeatedly failed with Internal Error and container downloads
failed DNS. The key mathematical text was available and read; no visual/table
measurements were made. No outside contact, paid computation or submission.
