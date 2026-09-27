# A legitimate zeta task and a non-oracle translation bound

27 September 2026. Continuation of Note 24, based on
`af9dc73040c24352ab1b71b0339d3a55b01cfaef` on `research/prx-quantum-phase2`.
Manuscript preparation remains on hold.

**This round resolves two specification gaps:** it fixes a standard mathematical
input/output family for the comparison, and replaces the unspecified cost of a
general controlled Jacobian translation with a conservative asymptotic circuit
construction. It does not establish a useful quantum/classical crossover, a new
quantum algorithm, or publication originality. No physical gate count is reported.

## 1. The task is the local Weil polynomial, not a mandatory order-finding route

Take an odd prime p, a positive genus g, and an explicitly represented monic
squarefree polynomial f in F_p[x] of degree 2g+1. Let C be the smooth projective
curve with affine equation y^2=f(x). The required output is its exact numerator

$$
Z(C,T)=\frac{P_C(T)}{(1-T)(1-pT)},\qquad P_C(T)\in\mathbb Z[T].
$$

This is the established local-zeta problem studied in [1-4], not a workload
introduced solely to frustrate a classical solver. The input class includes
special/easy members. Extra endomorphisms, decompositions, prior data and useful
preprocessing are available to both sides; no promise of classical hardness is
assumed. A particular independently sourced benchmark collection is still missing.

The coefficients occupy O(g^2(1+log p)) bits by the Weil bounds. They determine
all extension counts. If chi(X)=X^(2g) P_C(1/X) and its power sums are S_r, then

$$
\#C(\mathbb F_{p^r})=p^r+1-S_r.
$$

The sums obey the recurrence with characteristic polynomial chi. Newton identities
supply the initial sums; reduction of X^r modulo chi then supports modular queries
in O(g^2 log r) ring operations after this initialization. This is ordinary
classical recurrence evaluation, not new mathematics. Exact answers have size
O(r log p+log g), so this is not a claim of poly(log r) BIT time for writing an
arbitrarily long exact integer. The result is a compact reusable classical object,
but compactness and reuse alone do not imply a quantum advantage.

For the inherited point-sampling and reconstruction route, restrict its direct
large-field implementation to p>=64g^2. This is that route's sufficient condition,
not a new definition of the classical task. The same input is supplied to every
competitor. Classical algorithms may compute P_C directly and never obtain our
intermediate Jacobian orders.

## 2. Which classical algorithms must be allowed?

The following distinctions prevent a false opportunity claim.

| Input regime | Relevant classical route | Consequence for this study |
|---|---|---|
| Fixed/small characteristic, possibly large extension degree and genus | p-adic cohomology, including Kedlaya/Harvey [2] | A huge field p^n is not by itself an exponential quantum opportunity; characteristic and extension degree differ |
| Fixed genus and growing field, with the published characteristic conditions | Schoof-Pila and Abelard-Gaudry-Spaenlehauer [1] | An exponential-in-log(field-size) classical baseline would be wrong here |
| One integral curve, many primes below a bound | Harvey's average-polynomial-time all-primes method [3] | Classical cross-prime reuse must not be replaced with isolated runs |
| Supplied useful algebraic structure | Real-multiplication and other specialized methods [5] | The source structure cannot be hidden from the classical side |
| General variable genus and large characteristic | The minimum of applicable cohomological, torsion, generic-group and specialized methods | A legitimate comparison region, not a hardness theorem or a verified benchmark |

In particular, [1, Theorem 1] has a genus-dependent threshold q_0(g), requires
p >= (log q)^(c g), and explicitly explains that O_g((log q)^(O(g))) hides factors
depending only on g. Do not substitute g=log p into that fixed-genus notation and
turn it into a calibrated uniform runtime curve. Its noncoverage is likewise not
proof of classical difficulty. Its torsion route is a relevant independent
alternative even when a generic group algorithm appears expensive.

Harvey's [2, Theorem 1] gives a concrete different dependence: the Frobenius
matrix to p-adic precision p^k costs

$$
\widetilde O\bigl(p^{1/2} k^{5/2}g^\omega a+k^4g^4a\log p\bigr),
\qquad p>(2k-1)(2g+1),
$$

for a base field F_(p^a). In the prime-field task a=1. Sufficient precision grows
with g; it must not be held fixed when g grows. This is an upper bound for the
stated algorithm, not a classical lower bound. Modern implementations, fast
polynomial arithmetic and other algorithms remain eligible. The published
polynomial-time quantum zeta theorem itself is already Kedlaya's [4].

Generic-group period finding [6] is therefore only ONE branch of the classical
comparison. We have not shown that it dominates the best classical route on a
new useful family. The remaining application question is now explicit rather
than hidden behind the size of a Jacobian.

## 3. General controlled translation: representation and total semantics

Consider a required group call over F_Q, Q=p^n. Write b=ceil(log2 p) and h=n b.
Use a polynomial basis defined by a classically supplied, verified monic
irreducible degree-n polynomial over F_p. Each field element has n canonical
b-bit residues. Establishing p, irreducibility and the curve equation is part of
classical setup, not a free oracle.

Represent a reduced Mumford divisor by degree d<=g, the d coefficients below the
leading one in monic u, and the coefficients of v with deg v<d. Pad each polynomial
to g coefficient slots. Require zeros in unused slots, valid residues, a valid
degree tag, and u dividing f-v^2. The identity has d=0,u=1,v=0. Data width is

$$
W=2g h+\lceil\log_2(g+1)\rceil.
$$

This counts ONE group data register, not its arithmetic workspace or the full
quantum device. A precomputed translation constant K is an arbitrary canonical
reduced divisor, including degrees larger than one.

For the phase-control bit c define the Boolean permutation

$$
F_{c,K}(x)=
\begin{cases}
\operatorname{enc}(D+K),&c=1\text{ and }x=\operatorname{enc}(D)\text{ is valid},\\
x,&\text{otherwise}.
\end{cases}
$$

Its inverse is F_(c,-K). Valid strings stay valid; invalid strings are fixed.
This defines the action on every basis string, not just on a promised input.
Coherent validation is included in the cost. No measurement is used to choose an
exceptional branch. Fresh quadratic twists have the same degree bounds; the
leading coefficient of their defining polynomial need not be one.

## 4. A deliberately conservative, bounded-control-flow construction

We use standard Cantor composition and reduction, including shared support,
doubling, inverses and lower-degree divisors. We do NOT use only the faster
coprime-support formula. The classical group-law contract is documented in [1,7].
The following cost construction is independently specified, not a claim that
Sage or another native implementation is already a reversible circuit.

### Field layer

Schoolbook modular arithmetic in F_p has Boolean multiplication cost O(b^2).
Polynomial-basis multiplication and reduction in F_Q consequently cost O(h^2).
Addition costs O(h). For a nonzero field value z, fixed binary exponentiation
z^(Q-2) computes its inverse with O(h) multiplications and O(h^3) Boolean gates.
The same circuit maps zero to zero since Q>=3. This total convention is used on
inactive/dummy paths; it is not mathematical division by zero on an active path.

Faster multiplication and inversion may improve these exponents. They are not
forbidden to either competitor. This construction supplies a fallback upper
bound, not a claim of optimal arithmetic.

### Polynomial layer and data-dependent degrees

All intermediate polynomials have degree O(g). Arrays of 16g+16 coefficient
slots are sufficient for the simple composition formulas and their Euclidean
intermediates. Degree detection, leading-coefficient selection and shifts are
implemented by Boolean selection networks, not coherent random access.

A polynomial multiplication costs O(g^2 h^2). For division, select and invert the
divisor's leading coefficient once. Use O(g) padded cancellation steps, each with
O(g) field multiplications and a barrel shift of O(g h log(g+1)) Boolean gates.
Inactive steps retain the state. Thus division, including degree selection, costs

$$
\widetilde O(g^2h^2+h^3).
$$

Two extended polynomial gcds implement the general composition. Each has O(g)
Euclidean rounds, padded to a fixed bound; each round uses one division and
O(1) polynomial products for Bezout updates. Composition's remaining products
and exact quotients also have degree O(g).

For reduction, if the current monic u has degree d with g<d<=2g and deg v<d,
then replacing u by the monic version of (f-v^2)/u has degree at most

$$
\max(2g+1-d,d-2)<d.
$$

After reducing -v modulo the new u, at most g such rounds suffice. Normalizations
and validation use O(g) further inversions/divisions in total. Zero-polynomial
Euclidean inputs stop through masks; inactive divisions select harmless dummy
denominators. All branches are padded, and final valid/invalid selection restores
x on invalid inputs. No average-generic-divisor assumption is needed.

It follows that the total Boolean circuit size for either F_(c,K) or F_(c,-K) is

$$
S(g,h)=\widetilde O(g^3h^2+g h^3).
$$

The soft notation hides logarithmic control/array factors. This is a constructive
asymptotic bound; no numerical leading constant or emitted netlist is supplied.
Fast Cantor arithmetic is known [1]; the cubic genus dependence here reflects
padding a simple algorithm, not a lower bound on coherent Jacobian arithmetic.

### Clean reversible implementation

Use an AND/XOR/NOT Boolean circuit of size S. Compute each intermediate in a fresh
wire, XOR-copy its W outputs, then reverse the computation [8]. Each Boolean gate
needs at most two NOT/CNOT/Toffoli gates on this representation, so a clean XOR
oracle has at most 4S+W such gates, up to constant initialization overhead.

The in-place translation uses two clean XOR oracles:

    (x,0) -> (x,F_(c,K)(x))
          -> (F_(c,K)(x),x)          [swap]
          -> (F_(c,K)(x),0)         [XOR F_(c,-K) of first register].

The same c is retained throughout. All temporary wires return to zero. Thus, if
S_+ and S_- are the forward Boolean sizes, a bound is
4(S_+ + S_-) + 5W + O(1) elementary reversible gates. In particular,

$$
\Gamma(g,n,b)=\widetilde O(g^3n^2b^2+g n^3b^3).
$$

The store-all-intermediates construction uses O(S+W) working qubits, as well as
the two W-bit data registers and control. It does NOT achieve O(W) space. Sequential
translations can reuse the clean workspace. Standard time/space tradeoffs may
reduce space, but are not silently substituted for this construction. A Toffoli
has a constant-size Clifford+T realization [9]; fault tolerance, connectivity and
physical scheduling have not been costed.

## 5. What the inherited schedule then costs

Retain Note 21's rank-aware lists, same-register character tuples, recycled
control and first-batch reuse. For fixed total failure probability and O(g) calls,
its full-backend count at extension degree n is
A_n = Otilde(g^3 n b). Multiplying by the ACTUAL size-dependent arithmetic bound,
not a common cost for all n, gives the translation component

$$
\widetilde O\left(g^6b^3\sum_n n^3+g^4b^4\sum_n n^4\right)
 =\widetilde O(g^{10}b^3+g^9b^4),
$$

for O(g) calls with n=O(g), counting multiplicities. The initial order-acquisition
component has A_n^initial=Otilde(g^2 n b), reducing those two genus powers by one
on a branch where the remaining relations can be omitted. Notes 23-24's classical
completion, all failed attempts and the full fallback must still be charged.
Do not report the accepted-branch expression as an unconditional runtime.

For maximum extension O(g), the particular store-all-history workspace is
Otilde(g^5 b^2+g^4 b^3). Neither this loose gate bound nor this space upper bound
establishes a physical requirement, practical viability or an impossibility.
At b=Theta(g) the translation expression becomes Otilde(g^13); this is just an
algebraic specialization, not a speedup theorem over the best classical algorithm.

The full workflow ALSO includes field and twist construction, point sampling,
classical multiple precomputation, factoring/order checks, Fourier rotations and
readout, integer normal forms, classical cofactor completion, zeta reconstruction,
and any failure/fallback budgets. These have not all been combined into a numerical
resource estimate here. The contribution of this section is eliminating the
unpriced GENERAL-TRANSLATION oracle, not relabeling that component as total time.

The endpoint-completed schedule mentioned in Note 22 remains available. The
bounds apply to it as well. The executable arithmetic audit reconstructs the older
Note 21 illustration solely as a regression: genus 10, p=1000003, 665651460 versus
240901313 controlled translations, and 8004 versus 4004 data bits INCLUDING degree
tags. Neither is a hardware width. The squared/cubed extension-weighted monomials
are retained separately without unknown constants; their ratios are not runtime
speedups. This does not revert to the older schedule as the best current one.

## 6. Evidence, contribution and next decision

The unchanged Note 24 verifier passed from its supplied checkpoint. The new
[arithmetic audit](../../experiments/translation_cost_v1/README.md) independently
checks 48 binomial sample bounds by rational convolution, 2080 reduction-degree
bounds, 42 coefficient-lifting precision cases, 4096 integer-logarithm cases, the
two historical count totals and eight malformed controls. These verify arithmetic
used in the construction. They are NOT simulations of Cantor arithmetic, a quantum
translation circuit, phase estimation or a native point counter. The general
soundness argument above is mathematical, not inferred from these finite tests.

A full checkout could not be downloaded in this environment. Live files and refs
were read through GitHub; only the new versioned arithmetic audit and current
navigation were changed. Root historical and 164-curve verifiers were not rerun.
No third-party implementation was imported or modified. The separate classical
spinoff, other branches and historical experiment bytes remain unchanged.

**Research decision:** keep the standard odd-degree local-Weil-polynomial task
as the comparison contract, not as a declared application win. Generic quantum
polynomial time was already known. The two necessary next measurements are now
well specified: native classical cost on independently sourced general curves,
and a much tighter gate/space realization of general arithmetic on the same
parameters. A broad arithmetic compiler or new small-group census is not required.
A bounded audit of a realistic general-translation arithmetic strategy, versus
its actual classical counterpart, is preferable to expanding the loose envelope.
The question is a consequential resource/capability contribution, not another
restatement that the computation is polynomial. Manuscript stays on hold.

Primary references and precise inspection scope are in
[SOURCES.md](../../experiments/translation_cost_v1/SOURCES.md).
