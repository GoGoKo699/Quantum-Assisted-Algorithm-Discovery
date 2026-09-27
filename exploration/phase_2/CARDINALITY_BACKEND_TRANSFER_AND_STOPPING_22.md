# Cardinality first: short-run premises and an exact early exit

27 September 2026. PRX Quantum target; manuscript on hold.
Live base: ec32d7e68be6bd3bf8a3aee1610fba3a40922f07.
The classical spinoff was not read or changed. This is a bounded backend audit,
not a new quantum primitive, complete gate estimate or useful advantage claim.

## 1. Preserve the stronger live baseline

The live note21 already provides rank-aware generating-list bounds, correlated
character-phase tuples with a retained group register, recycled control and
reuse of initial order observations. These are inherited capabilities, not new
results of this pass. The local Zeta_Assessment checkpoint additionally provides
endpoint completion, reducing the maximum reconstruction degree to
h=max(1,g-2). We do not compare a new method only with a needlessly large circuit.

## 2. The Regev-style cardinality extension is already published

Ekerå and Gärtner [1, Appendix A.2] explicitly discuss finding an abelian group's
cardinality using short-run dual-lattice samples. For supplied elements D_i,
let Phi(z)=sum_i z_i D_i, L=ker(Phi), and H=<D_i>. Then

    [Z^d:L]=|H|.

Their Lemma4 proves this identity; their postprocessing can recover a sublattice
containing all sufficiently short relations. To obtain the full cardinality by
its determinant, those relations must generate the full kernel and the D_i must
generate the intended group. Their concrete theorem is for modular multiplicative
groups under stated number-theoretic conditions, not all possible Jacobians.
Pilatte [3] proves unconditional correctness of specified modified modular-group
algorithms; this is not a generic short-basis theorem for arbitrary curve points.

The correct transfer obligations are: generating the group, a sufficiently short
COMPLETE relation basis for the same generator ensemble, and efficiently implemented
coherent combinations. Point-subgroup escape in notes20/21 proves only the first.

An exact control uses Z/101Z with generators 1,2,3. Each alone generates the group,
so the proper-subgroup escape probability is one. But

    L={z: z1+2z2+3z3=0 mod101}.

All97 relations in [-8,8]^3 satisfy the integer equality z1+2z2+3z3=0 and have
rank two. The full kernel has rank three and determinant101. Any missing wrap
relation has squared norm at least101^2/14; (7,14,22) has squared norm729 and
wraps by101. The general deliberately-related-generator obstruction is already
in [1,Section2.3]. This is not a counterexample about actual random Jacobian
points, nor about their stronger character-bias bound. It prevents an unsupported
implication from generation to short-basis recovery.

## 3. The high-genus theorem's parameters do not automatically fit our calls

The published introduction of Barbulescu--Bisson [2] states an unconditional
short-run result at g~sqrt(B), with B=g log2(Q), discusses larger g, and explicitly
leaves the smaller-g regime unanalyzed there. The genus-two construction is
separately heuristic. The accessible old nine-page ePrint and the 2026 publisher
version have different scopes; they are not conflated.

Our extension-field calls have Q=q^n but still genus g. Thus

    B_n=g*n*log2(q),
    g/sqrt(B_n)=sqrt(g/(n*log2(q))).

At n=g-2 this ratio is asymptotic to1/sqrt(log2(q)). Under the sufficient setup
q>=64g^2 it tends to zero as g grows. Hence the largest reconstruction calls
are NOT covered by the cited high-genus scaling simply because g itself is large.
An arithmetic diagnostic n log2(q)<=g is not a sharp finite-input theorem cutoff.
No evaluated curve or quantum-resource claim follows from that diagnostic.

A field extension does not turn this into a genus-ng hyperelliptic curve. A Weil
restriction changes the variety and does not automatically retain the input class
or small-element implementation assumptions. This parameter mismatch is a limit
on importing the theorem, not an impossibility result for another algorithm.

Per-run gate count, total work and parallel hardware also remain distinct. The
current published discussion in [2] and the comparison in [6] explicitly motivate
care over these resources; no cryptographic benchmark numbers are transferred here.

## 4. Complete group structure is not always necessary for the requested number

Let N=|G| lie in a rigorous integer interval [L,U]. Exact orders of ANY selected
elements give a divisor

    E=lcm(ord(D1),...,ord(Dk)),  E|N.

Compute a=ceil(L/E), b=floor(U/E). If a=b, return N=aE. If a<b, the answer is
not yet unique. If a>b, the data are inconsistent. No enumeration of the interval
is required. Neither cyclicity nor a complete generating list is needed.

Sutherland [4,Section4] explicitly notes that an exponent and tight bounds may
determine a Jacobian cardinality without its structure. Partial lcms are the
elementary version of that known technique. It is available to both classical
and quantum algorithms and is not a new theorem claimed here.

For Z/6 x Z/2, a certified divisor6 and interval[10,14] determine cardinality12.
The same divisor with interval[10,20] leaves12 and18. Even knowing the full group
exponent need not settle the answer.

Do not use a merely annihilating integer as a divisor. The integer24 kills every
element of Z/6 x Z/2 but does not divide12. Misusing it with interval[10,26] would
return the wrong answer24. Exact candidate orders can be certified by rD=0,
(r/ell)D!=0 for all prime ell dividing r, and verified complete prime factorization
of r. Factoring, certified primality and group operations have real costs. Tiny
trial division in the diagnostic is not a production factoring procedure.

For the Weil interval, write

    A=sum_j binom(2g,2j) Q^j,
    B=sum_j binom(2g,2j+1) Q^j,
    s=isqrt(B^2 Q).

The exact integer interval is [max(1,A-s),A+s]. This avoids floating-point rounding
of (sqrt(Q)+/-1)^(2g). With g/sqrt(Q) small, its width is approximately
4g Q^(g-1/2). E exceeding that width is sufficient, not necessary, for uniqueness.
No large-exponent or random-cyclicity promise is assumed.

## 5. Correct backend-selection rule

First compute justified interval information and cheap available divisors. Within
a predeclared finite acquisition budget, certify returned element orders, update
E and check uniqueness. If successful, return the exact cardinality. Otherwise
use the complete generic backend of note21, or another method with its premises
established. Never infer completeness just because no new orders were observed.

Order information already produced in the generic backend's initial stage can
be used immediately; a separate quantum prepass is not mandatory. Any extra
factorization, verification and arithmetic still count. A speculative short-run
method can propose orders safely if they are independently checked, but this
supplies no unproved expected-runtime or success-frequency guarantee.

For a prepass budget B_pre and fallback budget B_full, the conservative bound is
B_pre+B_full plus verification. This is not a competitive guarantee against the
best algorithm or its actual runtime. The purpose is sound optional early exit,
not hiding a slow failure branch.

The full task is cardinality, not a requirement to produce every relation. On
some groups the remaining ambiguity collapses after little information; on
others the missing noncyclic structure is genuinely needed. Quantum and classical
methods both receive that distinction, plus fast arithmetic, special families,
fixed-genus/small-characteristic methods and permitted shared preprocessing.

## 6. Actual work and research decision

The new standard-library diagnostic checks99 exact abstract-group order
certificates,99 nonminimal-order rejections,3922 interval comparisons,339 unique
exits,99 lcm prefixes and4913 candidate short relations. It revisits the entire
inherited164-curve small family, verifying500 affine-point orders: only7 groups
have a unique cardinality from those orders and their unrefined Weil intervals;
157 remain ambiguous. These small-field cases do not estimate large-field success.
All cardinalities and element orders were obtained by small classical enumeration.
Another144 tests check exact perfect-square Weil endpoints.

The exact report regenerated byte-for-byte. The preceding curve-generator verifier
passed unchanged:164 small Jacobians,36456 group products,14336 associativity
checks and3072 full-encoding translation controls. No native point-counter,
Regev simulator, phase-estimation circuit, elementary-gate counter, hardware,
root historical verifier or useful-advantage benchmark was run.

The expanded note, new code/report/manifest/verifier, unchanged inherited curve
helpers and verification logs are in Quantum_Discovery_Cardinality_Backend_Scout.zip.
Run python verify.py after unpacking. Only this condensed note is committed.

The bounded assessment does NOT justify replacing the generic cardinality backend
wholesale with the recent high-genus short-run theorem. It DOES justify testing
cardinality uniqueness before demanding full decomposition and identifies the
actual missing geometry/parameter premise for the proposed transfer. Next quantify
the residual work after this stopping rule and strong classical methods on an
independently justified family, or prove a quantum resource tradeoff in the actual
required genus/extension regime. Do not build a general arithmetic library merely
because it is an available next task. Manuscript stays on hold.

## Primary sources and inspection scope

[1] Ekerå--Gärtner, Extending Regev's factoring algorithm to compute discrete
logarithms, PQCrypto2024; arXiv:2311.05545v2. Full parsed Section2.3,Lemma4 and
AppendixA.2 inspected. PDF index8 rendered; Appendix screenshot failed.
https://arxiv.org/pdf/2311.05545
[2] Barbulescu--Bisson, Regev's Attack on Hyperelliptic Cryptosystems,
Cryptography10(5),62 (28 August2026), DOI10.3390/cryptography10050062. Indexed
primary publisher abstract, introduction and selected method text inspected.
Direct HTML/XML/PDF and HAL retrieval failed; final Theorem3's full proof was
not audited. The parameter-scope statement uses the explicit published introduction.
https://www.mdpi.com/2410-387X/10/5/62
[3] Pilatte, Unconditional correctness of recent quantum algorithms for factoring
and computing discrete logarithms, Forum Math.Pi (2025), arXiv:2404.16450.
Primary theorem/scope inspected, not a generic Jacobian claim.
https://arxiv.org/abs/2404.16450
[4] Sutherland, A Generic Approach to Searching for Jacobians, Math.Comp.78 (2009),
485-507. Section4 exponent/tight-bound statement inspected; no timings reproduced.
https://arxiv.org/pdf/0708.3168
[5] Cheung--Mosca, Decomposing Finite Abelian Groups (2001). Primary algorithm and
prime-primary alternatives inspected; PDF page5 rendered. No native execution.
https://arxiv.org/pdf/cs/0101004
[6] Ekerå--Gärtner, A high-level comparison of state-of-the-art quantum algorithms
for breaking asymmetric cryptography, arXiv:2405.14381. Primary abstract inspected;
no resource figures transplanted into the Jacobian setting.
https://arxiv.org/abs/2405.14381
