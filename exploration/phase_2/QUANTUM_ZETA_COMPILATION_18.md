# Quantum compilation of algebraic counting rules

26 September 2026. Original project; PRX Quantum target; manuscript on hold.
Live base: 8a722797910873557fd6af9dd69e67b04c55a30e.
Condensed source audit and exact small-example checks. No new quantum algorithm,
useful advantage, native point-counting benchmark or resource estimate is claimed.

## Separation

Algebraic-Loop-Certificates has its own project. Its classical certificate work
is not continued here. The original project retains useful circuit-model quantum
advantage, comparable source information and AI assistance on both sides, and
an independently worthwhile consequence. A short explicit specification,
efficient coherent evaluation and short structural answer remain priorities,
not substitutes for a complete comparison. No spinoff files were accessed or changed.

## An established quantum capability with the desired output shape

Kedlaya [1] gives a quantum algorithm polynomial jointly in the genus g and log q
for the zeta numerator of a smooth projective geometrically irreducible curve
over F_q, with explicit curve-input conventions. It constructs finite abelian
Jacobian groups with unique encodings, finds generators probabilistically,
computes group orders quantumly, and reconstructs the numerator classically.
Orders over suitable finite extensions are included; no arbitrary huge point
table or residual truth table is supplied. This is an established theorem, not
this project's discovery. Polynomial arithmetic construction is not a practical
logical gate estimate.

A concrete subclass is the smooth projective completion of y^2=f(x), where f is
squarefree of degree 2g+1 in odd characteristic. Its input has O(g log q) field-
coefficient bits. The general theorem is not extended here to arbitrary
multivariate polynomial systems or arbitrary source programs.

## The short classical output

For N_m=#C(F_(q^m)),

    exp(sum_(m>=1) N_m T^m/m) = P_C(T)/((1-T)(1-qT)),
    P_C(T)=product_(i=1)^(2g)(1-alpha_i T),
    N_m=q^m+1-sum_i alpha_i^m.

The degree-2g integer polynomial therefore supplies a classical recurrence for
all extension-field counts. Newton identities give its initial values. The
coefficient list has O(g^2 log q+g^2) bits by the Weil coefficient bounds; it is
not generally only O(g log q) bits. F_(q^m) is an extension field, not the ring
of integers modulo q^m.

Printing an exact N_m takes Omega(m log q) output bits for large m. Computing it
modulo a supplied integer can instead use recurrence powering polynomial in
log m. No exponential output expansion is hidden. Computing a zeta function is
an independently established computational-algebra task [2-4], but that fact
alone does not establish a broad practical quantum application.

## A complete small reconstruction

For genus two,

    P(T)=1+a1*T+a2*T^2+q*a1*T^3+q^2*T^4.

The quadratic twist has numerator P(-T). Thus, with base Jacobian orders
Jplus=P(1) and Jminus=P(-1),

    a1=(Jplus-Jminus)/(2(q+1)),
    a2=(Jplus+Jminus)/2-1-q^2.

These are elementary consequences of standard zeta/twist identities, not a new
algorithm. For y^2=x^5+x^2+x+1 over F_5, exact classical enumeration gives
Jplus=60 and Jminus=12 and hence P=(1,4,10,20,25). Independent point counts over
fields of sizes 5,25,125,625 are 10,30,130,590, including the point at infinity.
The resulting recurrence gives N_5=3050 and N_6=16110 without further curve
queries; those two counts were not independently enumerated. A test computes
N_(10^12) modulo 1000000007 as 363634812 rather than printing its enormous exact
integer. This is classical reuse of the record, not a quantum execution.

The order enumeration uses the canonical reduced Mumford pairs (u,v): u monic,
deg(v)<deg(u)<=2, and u divides f-v^2. This is existing Jacobian arithmetic [4].
The general quantum algorithm obtains group orders without our tiny exhaustive
enumeration; its group operations and generator preparation must still be priced.

One base group order is insufficient: two F_3 controls have order 8 but different
numerators (1,-1,2,-3,9) and (1,0,-2,0,9), and base point counts 3 and 4. Further
information is genuinely required. The general theorem supplies a reconstruction;
it does not assume that an arbitrary one-number summary determines the curve.

## Classical comparison and usefulness boundary

Fixed-genus Schoof/Pila-type algorithms are polynomial in log q. Small fixed
characteristic supports classical polynomial-time cohomological algorithms as
genus/extension degree grow. Large-characteristic cyclic-cover methods achieve
p^(1/2+o(1)) dependence [3]; Kyng [2] extends a Harvey-style method to general plane
curves, explicitly qualifying that the complete exponents of the complexity
analysis were not worked out in that paper. These are stronger baselines than
point enumeration.

Moreover, for the reductions of ONE integer curve at ALL primes below a bound,
Harvey [5] gives average-polynomial-time classical computation. That workload
must not be compared with independent classical runs when shared computation
is possible. Sutherland [6] gives implemented superelliptic average-polynomial
point-counting techniques; its stated point-count/matrix outputs are not silently
upgraded to arbitrary full zeta numerators.

The surviving theoretical distinction in the inspected sources is JOINT
polynomial quantum dependence on geometric complexity and log q. There is no
unconditional lower bound against all classical algorithms. Genus-two toy cases
are not an asymptotic advantage regime. Special equations, known decompositions,
family preprocessing, and choosing a different adequate output remain legitimate
classical alternatives. Exact computation is not automatically the consumer's
requirement. Listing points or constructing a long code has additional costs.
No coding, cryptographic, or industrial quantum benefit is inferred here.

## Work actually performed

The independent standard-library diagnostic tests all 162 squarefree monic
quintics over F_3 and two explicit F_5 examples: 164 genus-two reconstructions,
32088 candidate reduced pairs, 348 independently enumerated field-point counts,
and 32800 modular recurrence checks against exact recurrence values. The report
regenerated byte-for-byte and the new verifier passed. These are exact algebraic
controls, not a native Sage/Magma run, quantum state simulation, compiled quantum
order finder, or advantage benchmark. No historical/root verifier was rerun.

Companion source SHA256:
06082df7fd5854002cf70a8fea3b4bf073cafc47f72c092a3e40c6e17009dd4f
Exact results SHA256:
25fa0c787a9c63ca24fa9df9cfcc274ba81ac17be401b50e426f302f111494ee
Expanded note SHA256:
aa2ea1cc43b4f8d3101041f30e248e09b76bb5f4db54fee37c989ff34ce321d5
The source, results, expanded derivation and standard-library verifier are supplied
in Quantum_Discovery_Zeta_Compilation_Scout.zip, not represented as committed
code. This scoped repository addition contains only the present note.

## Next research question

Can an explicit high-genus algebraic group interface make this known quantum
capability economical for a worthwhile sparse-in-characteristic counting task,
after reversible group arithmetic, generators, reconstruction and the best
classical methods are charged? Or does another structural output from the same
algebraic machinery offer a better consequence? Neither question is settled.
Do not call the published theorem a new result, reopen the classical spinoff,
revive the manuscript, or invent a workload simply to disable amortization.

## Primary sources and scope

[1] K. S. Kedlaya, Quantum computation of zeta functions of curves,
Computational Complexity 15 (2006), 1-19. arXiv:math/0411623v3.
https://arxiv.org/pdf/math/0411623
Theorem and Sections 3,6-8 inspected in parsed text. Pages 2,13 visually checked;
page-7 screenshot failed. No figure/table performance claim is made.

[2] M. Kyng, Computing zeta functions of algebraic curves using Harvey's trace
formula, Research in Number Theory 8,100 (2022).
https://doi.org/10.1007/s40993-022-00398-7
Full HTML classical-comparison/method text inspected; no native run or tabulated
timing reproduction.

[3] V. Arul et al., Computing zeta functions of cyclic covers in large
characteristic, ANTS XIII (2018), Open Book Series 2 (2019),37-53.
https://arxiv.org/abs/1806.02262
Primary abstract and proceedings metadata inspected; implementation not run.

[4] SageMath reference, Jacobian morphisms in the Picard group.
https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/hyperelliptic_curves/jacobian_morphism.html
Mumford conditions/Cantor arithmetic documentation inspected. No solver code
imported; the small enumeration is independently implemented.

[5] D. Harvey, Counting points on hyperelliptic curves in average polynomial
time, Annals of Mathematics 179 (2014),783-803.
https://annals.math.princeton.edu/2014/179-2/p07
Primary theorem/abstract scope inspected, not an executed implementation.

[6] A. V. Sutherland, Counting points on superelliptic curves in average polynomial
time, ANTS XIV (2020), arXiv:2004.10189, updated 2025.
https://arxiv.org/abs/2004.10189
Primary abstract/version inspected; no new performance claims transferred.
