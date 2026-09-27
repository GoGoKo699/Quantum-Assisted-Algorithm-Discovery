# Proof audit of sparse Weil reconstruction

This is the executable companion to [Note 29](../../exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md).
The Note-28 theorem survives this internal audit without changing its query set,
field range, or sufficient genus threshold. This is not external peer review,
a formal proof certificate, or an exhaustive priority guarantee.

```sh
python experiments/reconstruction_audit_v1/verify.py
```

Python 3.10 or later, standard library only. The verifier pins the inherited
`all_field_reconstruction_v1/reconstruct.py`, copies it and the audit into a
temporary directory, and regenerates REPORT.json exactly. It never rewrites
reference data. Do not run with `-O` or `-OO`.

The independent fixture is an irreducible degree-64 2-Weil polynomial, not a
newly counted curve. Its construction, real-root bounds, and irreducibility
are verified by exact integer/rational arithmetic and a modulo-7 test. All
45 supplied counts are reconstructed with circulant determinants and compared
to the fingerprint of a separately executed SymPy resultant calculation.
SymPy is not required for replay. Only q, g and the counts reach the inherited
decoder, which recovers 65 coefficients and 30 traces exactly. Four legal
logarithm-centre displacement runs retain the correct output.

The test intentionally records a corrupted count that the decoder does NOT
reject. Exact resultant replay detects that discrepancy. This is consistent
with the theorem's promised-true-input contract and demonstrates why this
routine is not an order-authentication or curve-identification certificate.

The proof audit adds explicit bounds on input size, binary range-reduction
exponents, series length, intermediate rational lengths and operation count.
The finite tests support the implementation; they do not establish the
all-genus theorem by enumeration.

Proposed separation: a classical `Sparse-Weil-Reconstruction` project, with the
present audited theorem as its initial result. No new repository is created
here. The parent quantum-discovery project retains its independent objective.
See [SOURCES.md](SOURCES.md) for attribution and bounded search scope.
