# Originality boundary and a rank-aware quantum cardinality cost envelope

27 September 2026. Original project, PRX Quantum target, manuscript on hold.
Live base: 5c6941f02cf99b9180b494a97150107e9b887fc8.
The Algebraic-Loop-Certificates spinoff was not accessed or changed.
This is an integrated assessment, not a new quantum primitive, proven practical
advantage, elementary-gate resource estimate, or native point-counting benchmark.

## 1. A concrete originality question is resolved

Put Q=q^n and c_n=K_n/q^(gn), with the previous exact curve/twist orders K_n,T_n.
Since K_(2n)=K_n*T_n,

    -Q log(c_n)+(Q/2) log(c_(2n))
      = (Q/2) log(K_(2n)/K_n^2)
      = (Q/2) log(T_n/K_n).

This is n times the TWO-TERM truncation of Kedlaya's displayed Mobius inversion
in Section 8 [1]. The highlighted odd-power cancellation is therefore not a new
inversion principle. The previous rounding proof remains valid, but it should
not be given that originality interpretation.

The implementation schedule can still differ: a fresh twist over F_(q^n) supplies
information otherwise represented by a doubled-extension group order. Priority
and significance of that smaller-field schedule remain unresolved. Low-genus
curve/twist reconstruction is already stronger in its stated regimes [2]. A
particular schedule improvement is not automatically a PRX Quantum contribution.

## 2. Rank, not only group size, controls generator acquisition

Let G be a finite abelian group, |G|<=U with U>=2, and suppose

    dim_(F_ell)(G/ell G)<=d

for every prime ell. Independent samples escape every proper subgroup with
probability at least alpha. For B=ceil(log2 U),

    Pr[m samples fail to generate G]
       <= min(1, B*Pr[Binomial(m,alpha)<d]).

For a fixed prime quotient, every sample increases the current span with
conditional probability at least alpha until it is full. Couple this process
to Bernoulli(alpha) progress. The samples generate G iff they span all its
prime quotients: any proper quotient has a prime cyclic quotient. There are
at most B relevant primes. The displayed bound follows without factoring |G|.
For fixed alpha, O(d+log B+log(1/delta)) samples suffice.

For a genus-g Jacobian, d<=2g. Multiplication by ell on a g-dimensional abelian
variety has degree ell^(2g) [3], hence |G/ell G|=|G[ell]|<=ell^(2g), including
characteristic-primary torsion. The same bound applies to subgroups and duals.
The previous large-field point sampler gives alpha>=1/3 when Q>=64g^2.
Thus its list length can be bounded by

    O(g+log(g log Q)+log(1/delta)),

rather than our prior size-only O(g log Q+log(1/delta)) bound. This is an
elementary application of established group facts, not a claimed new general
random-generation theorem. Both classical and quantum algorithms get this bound.

For the previously used parameter illustration g=10,q=1000003, 15 order calls,
and total generating-list failure allowance 1/100, exact binomial tails give:

| Extension n | Prior sufficient list | Rank-aware sufficient list |
|---|---:|---:|
| 1 | 359 | 126 |
| 2 | 700 | 129 |
| 5 | 1722 | 132 |
| 10 | 3426 | 135 |

Total point samples across the twist schedule: 27536 becomes 1977. This is a
parameter bound, not a run on a selected large curve or a runtime improvement.

## 3. Keep one character while measuring all its coordinates

Translations by D_1,...,D_m commute. In the regular representation of their
generated group H, the identity state is a uniform superposition of character
eigenstates. Joint eigenphase estimation returns one uniform character's values
on all generators. This is established hidden-subgroup machinery [4,5].

Retain the SAME group register across the m phase-coordinate measurements.
Reset it only between complete character tuples. For duplicated generator X,
retaining the register gives phase labels 00 or 11, each with probability 1/2.
Resetting it gives all four labels and hence spurious relations with probability
1/2. Finite precision is treated by coupling to ideal character draws and
bounding the probability of any misread label, not by assuming measurements
conditioned on successful implementation remain exactly uniform.

Standard semiclassical Fourier readout [4,6] recycles one phase-control qubit.
A simultaneous bank of m full exponent registers is not necessary for this
translation interface. The group accumulator, general Jacobian arithmetic
workspace and classical feedforward still cost resources. Precomputed powers
are general reduced divisors, not necessarily degree-one curve points.

## 4. Reuse the initial phase observations instead of paying twice

A first batch of c complete character tuples is read at high precision. For
individual generator order r_i<=U, each phase is a rational with denominator
r_i. Continued fractions and lcm of its reduced denominators recover r_i with
high probability; the uniform-character restriction to <D_i> is uniform.
Let R=lcm_i r_i. On the successful recovery event, R is the exponent of H.
The first c tuples are retained as relation samples. Subsequent tuples need
only enough precision to identify a numerator over the known denominator R.

Let K be the kernel of (Z/R)^m -> H, a -> sum_i a_i D_i. The phase labels are
uniform in K^perp. If y_1,...,y_s generate that dual group, form

    Lambda=span_Z{y_1,...,y_s,R e_1,...,R e_m}.

Then |H|=R^m/det(Lambda), computed by integer Hermite normal form. Generator
orders alone are not the group cardinality. Nor does a correct |H| prove H is
the intended Jacobian: point-list completeness is separately budgeted.
Uniform dual samples have escape probability >=1/2 and rank <=2g, so the same
binomial lemma bounds the required s. No prior group order or factorization is
assumed known. Reusing the first c tuples is ordinary reuse of acquired data,
not a new quantum primitive.

## 5. Conservative controlled-translation envelope

For each of t order calls, set eta=1/(100t), U=(ceil(sqrt(Q))+1)^(2g),
B=ceil(log2 U), and d=2g. Select m and s by the exact binomial bounds with
alpha=1/3 and 1/2. Use

    c=ceil(log2(m B/eta)),
    a=2B+ceil(log2(2mc/eta))+4,
    b=B+ceil(log2(2ms/eta))+4.

The initial a-bit phase readings resolve circular error below 1/(4U^2).
The later b-bit readings resolve the known denominator R. Standard phase-tail
bounds [4] justify the stated conservative precisions. Five global 1/100 error
pools cover point generation, numerator coverage, phase reading, dual generation,
and gate approximation. The phase pool is split between the two reading stages.

One controlled power is one translation by a classically precomputed multiple
2^j D_i, not 2^j consecutive additions. Counting each reused tuple once gives

    A_query <= m*c*a + max(0,s-c)*m*b.

For g=10,q=1000003, the resulting comparison is:

| Schedule, using the SAME improved backend | Orders | Max degree | Controlled translations | Peak coefficient-data bits |
|---|---:|---:|---:|---:|
| Published degree range 1..20 | 20 | 20 | 665651460 | 8000 |
| Twist-assisted range with reuse | 15 | 10 | 240901313 | 4000 |

The translation-count ratio is about 2.76. This is NOT a quantum/classical speedup,
wall-clock forecast or Toffoli count. Different extension degrees have different
translation costs. The 4000/8000 bits exclude work registers and degree tags.
No large curve is selected and a 20-bit prime is not itself a quantum-favorable
classical regime. Smaller-genus special algorithms are not displaced by this table.

Write Gamma(g,n,log q) for the full elementary-gate cost of a general controlled
translation. The quantum cost contains sum A_query*Gamma, plus field setup,
classical point sampling and power precomputation, Fourier feedforward/rotation
synthesis, classical order recovery and normal forms, zeta reconstruction and
error correction. The abstract translation count is Otilde(g^5 log q) for this
unoptimized construction. It is not a complete gate-complexity theorem or an
optimal quantum lower bound. A large upper bound proves neither viability nor
nonviability; a better backend might do substantially less work.

## 6. Research verdict

The proposed new cancellation principle does not survive the direct source
comparison. The smaller-field schedule remains a possible implementation
refinement with unresolved priority. The rank-aware and recycled-control
backend makes the cost accounting more realistic, but its standard ingredients
are not a new useful quantum-advantage result by themselves.

Retain the known algebraic capability and this implementation route provisionally.
The next decision needs an independently justified input family, an appropriate
native classical calculation and a bound for the dominant controlled translation.
Do not begin a general-purpose arithmetic compiler merely because it is the next
available coding task. Mathematical usefulness can suffice; an industrial user
is not mandatory, but a meaningful consequence still must be demonstrated.

Classical fixed-genus, small-characteristic, special-decomposition and batched
all-primes methods remain admissible [7,8]. Field size and characteristic are
different parameters. No classical lower bound or useful crossover is asserted.
Original source information, preprocessing and reuse are available to both sides.

## 7. Executed checks and provenance

The new exact diagnostic checks the Mobius identity symbolically; 468 generation
probability inequalities on 36 distributions over nine groups; 255 character
cancellation sums; 39 HNF prefix cardinalities against explicit closures; and
39 repeated prefix calculations with the common denominator reconstructed from
the phase values. The duplicated-generator control and all resource counts are
also checked. SymPy 1.14.0 supplies exact polynomial and HNF arithmetic.

The full report regenerated byte-for-byte, including from a fresh extraction.
The unchanged preceding curve-generator checkpoint verifier passed: 164 small
Jacobians,36456 group products,14336 associativity triples,3072 translation
checks,265 square-root controls,800 generation-probability controls. No root
historical verifier was rerun. No large-field point counter, compiled quantum
phase estimator, group-cardinality device, or hardware experiment was run.

Full derivations, source, results and verifier are in the conversation archive
Quantum_Discovery_Zeta_Feasibility_Assessment.zip. Run `python verify.py` after
unpacking. Only the condensed note and research work order are committed here.
Source SHA256:2243147045001e226fce3544e11b61cd21f42646e8cc042409589bc35fbbcde0
Result SHA256:256519981ea9868b7ed70623d92164ec72d7f50f6782635006a80ea5e6478960

## Primary sources inspected

[1] Kedlaya, Quantum computation of zeta functions of curves (2006), Section8.
https://arxiv.org/pdf/math/0411623 . Exact displayed Mobius expression inspected.
[2] Sutherland, A Generic Approach to Searching for Jacobians (2009), Lemma4.
https://arxiv.org/pdf/0708.3168 . Low-genus curve/twist prior art; no timing copied.
[3] Milne, Abelian Varieties, Theorem7.2, multiplication degree ell^(2g).
https://www.jmilne.org/math/CourseNotes/AV.pdf . PDF page indexed38 visually checked.
[4] Mosca and Ekert, The Hidden Subgroup Problem and Eigenvalue Estimation on a
Quantum Computer (1999), Sections3-5. https://arxiv.org/pdf/quant-ph/9903071
Phase tail, eigenvalue interpretation and recycled control inspected.
[5] Cheung and Mosca, Decomposing Finite Abelian Groups (2001).
https://arxiv.org/pdf/cs/0101004 . Unique encodings and group access retained.
[6] Griffiths and Niu, Semiclassical Fourier Transform for Quantum Computation,
PRL76,3228 (1996). https://arxiv.org/abs/quant-ph/9511007
[7] Kyng, Computing zeta functions of algebraic curves using Harvey's trace
formula (2022). https://doi.org/10.1007/s40993-022-00398-7
[8] Harvey, Counting points on hyperelliptic curves in average polynomial time
(2014). https://annals.math.princeton.edu/2014/179-2/p07
Prior character-sum input from Farashahi et al. remains documented in note20;
it was not rederived or upgraded to a novelty claim here. Cyclic-resultant
abstracts and quantum resource literature were also screened; no exhaustive
priority audit or genus-one-to-high-genus resource transfer is claimed.
