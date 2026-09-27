# Ordinary cardinality requests can use the same smaller-field computation

27 September 2026. Base: `bc62cdcad7927475d40c452112d12af1ed40693c` on
`research/prx-quantum-phase2`. Manuscript remains on hold.

**Completed comparison:** after allowing the ordinary route the established
quadratic-extension factorization and reuse of computed orders, it can make
exactly the same underlying group-order calls as the signed route. Note 26's
weighted ratios compare signed computation with an UNSPLIT ordinary backend,
not with every source-aware implementation of the ordinary cardinality requests.

This does not prove that our precise reconstruction theorem is already in the
literature, or that no useful quantum advantage exists for the whole problem.
It closes a specific implementation comparison. No standalone project is opened.

## 1. Predeclared claim tested

The claim under examination is that fresh twists intrinsically reduce the
quantum resources needed to supply the endpoint-completed reconstruction, even
against an ordinary route that sees the same curve equation and may apply known
algebraic preprocessing. The comparison concerns the complete underlying
cardinality computations, not only the labels on abstract requests.

An exact-order call remains an expensive subroutine: its sampler, quantum
arithmetic, verification, repetitions and fallback must all be charged. We do
not assume that any unknown order is available as a free factorization hint.
We ask whether both routes can invoke the SAME actual subroutines.

## 2. The established reduction is already source-accessible

For an odd-characteristic hyperelliptic curve over F_q, put

$$
K_n=\prod_{i=1}^{2g}(1-\alpha_i^n),\qquad
T_n=\prod_{i=1}^{2g}(1+\alpha_i^n).
$$

Here T_n is the order of a fresh nontrivial quadratic twist over F_(q^n), with
Frobenius eigenvalues -alpha_i^n. Factoring each 1-alpha_i^(2n) gives

$$
K_{2n}=K_n T_n.
$$

Sutherland [1, Lemma 3 and the preceding extension-group discussion] explicitly
uses original/twist orders to obtain the quadratic-extension order. The broader
Weil-restriction/Prym decomposition also appears in [2]. The equality of orders
is the only group-theoretic fact this reduction needs; it does not require a
pointwise direct-product decomposition or an efficient splitting map.

The input source supplies the twist equation. For a monic degree-(2g+1)
polynomial f and a nonsquare d in F_(q^n), one model is

$$
y^2=d^{2g+1}f(x/d).
$$

Construct the degree-n field, choose and check d, and construct this equation
classically. This does not require K_n, T_n, the unknown zeta polynomial, or
building the degree-2n field. Both routes pay for the same field/nonsquare setup.
The ordinary route is not denied this construction in our explicit-input model.
A twist over F_q becomes trivial after an even-degree base change; hence the
fresh degree-n twist must not be silently replaced with that base change.

This is a source-aware algorithmic reduction. It is NOT an implementation of a
restricted oracle that allows queries only to K and forbids source access or
twists. Those different oracle models must remain separate in an originality or
minimum-query argument.

## 3. Normalization theorem for the matched schedules

For g>=2 let h=max(1,g-2) and let O_h be the odd integers at most h. Note 26's
ordinary requests are

$$
\mathcal D_h=\{K_r:r\in O_h\}\cup\{K_{2n}:1\le n\le h\}.
$$

Process an original request K_m as follows: if m is odd, submit it to the group
backend. If m=2n, recursively obtain K_n, submit T_n, and multiply the returned
integers. Retain each computed cardinality so that it is never submitted twice.

**Theorem.** The distinct submitted backend calls after this normalization are
exactly

$$
\mathcal S_h=\{K_r:r\in O_h\}\cup\{T_n:1\le n\le h\}.
$$

Proof: every K_(2n) with n<=h is a root request, so its split submits T_n. Every
new K dependency is obtained by halving its predecessor; its odd part is an
odd r<=h already among the anchors. No new twist with index above h is produced,
and every required odd anchor is supplied. Reuse removes all duplicate queries.
There are exactly h scalar products, one per even target, and h+ceil(h/2)
distinct backend calls. This proves equality of the call sets, not merely an
upper bound on their sizes.

The backend calls can be made in any common deterministic dependency-compatible
order. Once their integers are available, all ordinary root values are returned
by the product DAG. In the reconstruction, a subsequent K_(2n)/K_n can also be
simplified back to its already computed T_n. The scalar graph and this
simplification are ordinary classical processing, not a quantum state map.
For n=O(g) all retained orders have O(gn log q) bits; the graph evaluation and
storage are polynomial. For arbitrary binary-encoded enormous n, printing an
order still costs its output bit length; no logarithmic-output-size shortcut is
claimed by the diagnostic planner.

## 4. Consequence for complete backend comparisons

Choose the same actual curve/twist descriptions, numerical parameters, error
allocation, sampler, cardinality routine, order checker and fallback policy for
each common backend call. Couple the randomness by the call identifier. Both
routes then have the same backend computation distribution, including failures
and retries. Any event in which a leaf order is wrong is counted once, even if
its integer is reused in several derived ordinary requests. A union bound over
leaf errors requires no independence assumption.

This is stronger than assuming a cost law depending only on extension degree.
Curves and twists may have different costs; both routes now face the SAME curves
and twists. Shared field construction, precomputed powers and other preprocessing
can likewise be common. No double charging of a reused leaf is necessary.

For the existing genus-ten h=8 example:

| Implementation | Distinct actual order calls | Maximum degree of actual calls |
|---|---:|---:|
| Unsplit ordinary backend in Note 26 | 12 | 16 |
| Ordinary requests after known quadratic descent | 12 | 8 |
| Signed route | 12 | 8 |

Under the identical Note 26 backend configuration, the last two therefore have
the same 152818614 controlled-translation envelope and the same single-accumulator
layout. These counts are inherited arithmetic, not a new compiled execution.
The 265458395/152818614 ratio and the weighted 6.272/12.512 ratios remain correct
for the historical UNSPLIT comparison. They are not savings against the normalized
comparator. The scalar multiplication/reconstruction bookkeeping can differ and
must still be counted; equality of backend work is not a measured equality of
wall times or a claim that every possible implementation is equivalent.

No new quantum primitive is necessary to implement the competitor: it calls the
same established cardinality backend on the same smaller instances. This is not
a counterexample to all quantum zeta algorithms, nor a classical simulation of
quantum order finding. Both compared backends can be quantum. A classical
source-aware point counter can use the same reduction or bypass it altogether.

## 5. Cardinality factorization is NOT quantum-register factorization

Under the usual embedding over F_(Q^2), let A^+ be the original rational subgroup
and A^- the subgroup obtained from the twist. Frobenius acts as +1 on A^+ and
-1 on A^-. Therefore

$$
A^+\cap A^-=A(\mathbb F_Q)[2].
$$

Rational 2-torsion can prevent a direct product. This matters if one tries to
upgrade the numerical equality to a reversible change of representation for an
arbitrary quantum register. No such map is needed for the cardinality reduction,
and none has been supplied here.

A complete finite control is E:y^2=x^3-x over F_5, with nonsquare d=2 and twist
y^2=x^3+x. Direct enumeration over F_5 and F_25=F_5[s]/(s^2-2) gives

$$
|E(\mathbb F_5)|=8,\quad |E^{(2)}(\mathbb F_5)|=4,\quad
|E(\mathbb F_{25})|=32.
$$

The product formula is correct. But the degree-two group has four 2-torsion
points, while the product of the two base-field groups has sixteen. The groups
are consequently not even abstractly isomorphic. Their natural images intersect
in four elements and generate a subgroup of order eight, not thirty-two.
The control enumerates the point sets and the twist embedding, not the full
Jacobian arithmetic or an alleged quantum unitary.

The extended base twist has order 32, while the fresh twist over F_25 has order
20. This also tests the difference between a fresh twist and an extended twist.
This tiny example is an algebraic counterexample to a false register-splitting
inference, not a quantum-advantage workload or a new curve record.

## 6. Evidence and scientific decision

The [standalone diagnostic](../../experiments/descent_baseline_v1/README.md)
normalizes 64 matched schedules and verifies 3136 independent scalar chain
products. It checks every nonempty request subset of degrees 1 through 8 (255
subsets), ten malformed-input controls, and the finite-field example above.
The original, reverse-order and duplicate-root descriptions give the same plan.
No complete quantum circuit or resource compiler is implied by these tests.

All three inherited current verifiers passed unchanged. Their reports were not
regenerated into new reference data. The root historical verifier and 164-curve
suite were not run; full Git checkout still failed on DNS. Only this repository's
active research branch is changed, and all historical experiments and LICENSE
are preserved. No external contact, paid computation, hardware experiment or
unattended work was initiated.

**Decision:** a smaller-field schedule alone does not yet supply a distinct new
quantum resource claim against a source-aware competitor. Do not start a hardware
cost campaign merely to refine the unsplit comparison. Keep the arithmetic and
reconstruction as reusable supporting work, with the refined comparator explicit.
This is not a novelty disproof for Note 26's precise plain-query theorem: closing
an implementation comparison and determining priority of a mathematical
reconstruction result are different tasks.

The next focused question is the plain-query theorem itself: does its nonconsecutive
h+ceil(h/2) reconstruction, under the explicit large-field hypothesis, give a
previously unestablished restricted answer to Kedlaya's fewer-than-2g query question
[3]? It must be assessed in the SAME oracle model, not by confusing a bound on the
largest requested degree with a bound on the number of requests, or by granting
twist access to only one side. The exact conditional theorem exists in Note 26;
its originality and significance are not certified by an incomplete search.
If that theorem is already subsumed, record that result and return to the broader
compact-input search rather than elaborate this schedule again. If it survives,
it may justify a distinct reconstruction-theory line, but no repository split or
publication claim is warranted yet. Manuscript remains on hold.

Primary sources and their inspection limits are in
[SOURCES.md](../../experiments/descent_baseline_v1/SOURCES.md).
