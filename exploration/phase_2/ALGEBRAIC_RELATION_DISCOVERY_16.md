# Compact questions, algebraic relations, useful classical consequences

26 September 2026. Phase 2; PRX Quantum target; manuscript remains on hold.
Live base read: 16e82483bb89779cbfb9df22fb9aa5903f3e44ee.
Documentation-only direction update. No new algorithm, benchmark, gate estimate,
novelty claim, or useful quantum advantage is established.

## Author input and independent assessment

The author proposes starting from demonstrated quantum algebraic capabilities:
a short explicit question, hidden structure, and a short classical answer. The
intended use need not be cryptographic. Treat this as a mechanism-selection
criterion, not an assertion that all number theory is useless outside cryptography
or that all compact hidden-structure problems are quantumly easy.

Shor's algorithms are polynomial-time algorithms for explicit arithmetic inputs,
not merely query separations with a free unknown oracle. Their advantage is over
the best known classical algorithms, not a proved unconditional superpolynomial
lower bound for classical factoring/discrete logarithms. Post-quantum cryptography
supplies schemes designed to resist known quantum attacks; it is not a proof
that every such scheme resists every possible quantum algorithm. NIST has already
standardized ML-KEM, ML-DSA, and SLH-DSA. This cryptographic fact does not identify
our prospective positive application.

## What the successful algebraic examples actually supply

For order finding, the input is (N,a), with gcd(a,N)=1, and the hidden object is
the least positive r with a^r=1 mod N. The evaluated map is t -> a^t mod N.
Repeated squaring evaluates it in work polynomial in the binary lengths of t
and N. No table of its exponentially many possible arguments is loaded.

This is stronger than being given one cheap step of an iterative computation.
A short rule x -> T(x) does not automatically make T^k(x) cheap for a binary-
encoded, enormous k. Writing U^(2^j) in a circuit diagram does not implement it
cheaply. An algebraic representation, such as explicit fixed-size matrices over
a finite field, can supply powers by repeated squaring without enumerating the
orbit. All reversible implementation and precision costs remain charged.

The collisions must also have usable structure. For an abelian hiding function,
f(x)=f(y) exactly when x-y is in a subgroup H. A Fourier measurement supplies
constraints on H, rather than merely identifying one collision. This is standard
hidden-subgroup machinery. Arbitrary symmetries, noisy similarities, graph
isomorphisms, or hidden shifts cannot be declared efficiently solved just by
calling their structure hidden. The group representation and measurement cost
matter as much as the compact output.

## Candidate starting family: relations among existing transformations

Let A_1,...,A_m be explicit, pairwise commuting invertible d-by-d matrices over
an explicitly represented finite field. Define

    Phi(z) = A_1^z_1 ... A_m^z_m,    z in Z^m,
    L = {z : Phi(z)=I}.

Commutativity gives Phi(z+w)=Phi(z)Phi(w), and hence

    Phi(z)=Phi(w) iff z-w is in L.

The input matrices have O(m d^2 log q) bits. Matrix multiplication, equality,
inversion and powering have ordinary explicit implementations. Commutativity
and invertibility can be checked classically. Relevant exponent bounds and
orders must be derived and paid for, not supplied as a free classical oracle.
The image is finite, so L is a full-rank integer lattice. The bound
|image(Phi)|<=|GL(d,q)|<q^(d^2) bounds the bit length of a Hermite-form relation
basis polynomially in the input parameters. The space of exponent tuples may
nevertheless be enormous.

Quantum finite-abelian-group decomposition and relation finding already address
this algebraic core [2]. There is no novelty in the displayed reduction. In
particular, m=1 is order finding; finite-field scalar relations include ordinary
discrete-logarithm instances. Not every family of matrices is therefore hard:
source structure, invariant subspaces, known orders, finite-field algorithms and
other classical decompositions remain competitors.

Why inspect this family? Once a correct complete relation basis is known,
classical integer normal forms can represent exponent-labelled compositions
canonically and decide equivalence by arithmetic modulo L. The original
operations already tell us how to execute a representative. Unlike an arbitrary
low-dimensional black-box function, there is no obligatory residual truth table
to learn. This could support a symbolic simplification or recurrence-analysis
workflow. It does not establish that such a workflow needs this basis, that its
use is cheaper than direct matrix calculation, or that an end-to-end gain occurs.
Finding shortest words or lowest-cost representatives is another optimization
problem, not a free consequence of canonicalization. Verifying individual
relations is not certifying completeness of the lattice.

The candidate question is: which independently worthwhile computation needs
such a compact global relation description, rather than merely a few forward
evaluations, and cannot obtain or bypass it classically at comparable cost?
Do not disguise a discrete-logarithm challenge as a useful application simply
by renaming its variables.

## Established bridge beyond cryptographic tasks

Hallgren's Pell/principal-ideal algorithms and the Eisentrager-Hallgren-Kitaev-
Song unit-group algorithm are existing extensions of algebraic quantum methods
into computational number theory [3,4]. Their cryptographic implications are
not their entire mathematical content. The latter gives complexity polynomial
in field degree and log discriminant in its stated model. These are reference
points for compact structural outputs, not proposed new contributions.

Full output representations and downstream costs must be inspected before using
such results in a new reduction. Algebraic integers or fundamental solutions can
be huge; a compressed or logarithmic output is not the same as printing every
digit. No new Pell output-size or resource theorem is asserted here.

## Next research priority

Prioritize short, source-specified algebraic relation questions with efficient
coherent evaluation and a useful classical consequence. Preserve the earlier
Fourier-coordinate and probability scouts, but do not extend them merely because
their machinery exists. The classical competitor receives the same arithmetic
specification, source code, AI reasoning, preprocessing and reuse.

The next discriminating work is an application/reduction audit: identify which
relation would remove a genuinely costly operation, check that the evaluation
map is implementable without finding that relation first, and compare with
source-aware classical alternatives. We do not require an existing user script;
a new workflow may be legitimate, but its value must be persuasive independently
of either the author's enthusiasm or the desired journal.

## Sources and work scope

[1] P. W. Shor, Polynomial-Time Algorithms for Prime Factorization and Discrete
Logarithms on a Quantum Computer, SIAM J. Comput.26,1484-1509 (1997).
https://arxiv.org/abs/quant-ph/9508027
Parsed full PDF, especially Section 3's explicit reversible repeated-squaring
implementation, inspected. No current gate-count estimate adopted.

[2] K. Cheung and M. Mosca, Decomposing Finite Abelian Groups (2001).
https://arxiv.org/abs/cs/0101004
Full six-page PDF inspected, including Theorem 7, access assumptions and the
relation-map construction. PDF page 4 was also visually checked. The classical
Smith-normal-form stage is prior work, not our contribution.

[3] S. Hallgren, Polynomial-Time Quantum Algorithms for Pell's Equation and the
Principal Ideal Problem, JACM54 (2007), DOI10.1145/1206035.1206039.
https://authors.library.caltech.edu/records/wwa5n-3k633
Institutional abstract inspected, not a full new audit of the algorithm.

[4] K. Eisentrager, S. Hallgren, A. Kitaev and F. Song, A Quantum Algorithm for
Computing the Unit Group of an Arbitrary Degree Number Field, STOC2014.
https://authors.library.caltech.edu/records/hgwzf-ttf17
Author/institution abstract and complexity statement inspected; no implementation.

[5] M. Mosca and A. Ekert, The Hidden Subgroup Problem and Eigenvalue Estimation
on a Quantum Computer (1999). https://arxiv.org/abs/quant-ph/9903071
Primary abstract checked for the established algebraic problem family.

[6] NIST Post-Quantum Cryptography project, current public standards summary.
https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post_Quantum_Cryptography-Standardization
Checked only to distinguish completed standardization from general security
claims. No cryptographic deployment task is proposed.

No new numerical experiment or old verifier was run in this direction-setting
pass. No external contact, submission, paid computation, or unattended work.
Original license, historical results and other branches remain unchanged.
