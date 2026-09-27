# All-field ordinary-count reconstruction

[Note 28](../../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) proves an
ordinary-count reconstruction statement for g>=32 over every finite field.
With h=g-2, query degrees 1..h together with the even degrees through 2h.
There are h+ceil(h/2)<2g supplied cardinalities. No twist oracle, curve equation,
known factorization or genericity assumption is used by the decoder.

```sh
python experiments/all_field_reconstruction_v1/verify.py
```

Python 3.10 or later, standard library only. The verifier checks file hashes,
copies code to temporary storage and regenerates REPORT.json without overwriting
expected evidence. Do not use -O or -OO.

The decoder combines the published Mobius/Newton machinery with the inherited
endpoint completion and a uniform tail proof. Range-reduced rational logarithms
are essential: the earlier large-field log routine is not silently reused at
small q. All mathematical input promises remain external; consistency checks do
not authenticate supplied group orders or certify curve realizability.

Tests reconstruct seven SUPPLIED Weil polynomials, comparing 489 coefficients
and 227 traces exactly. Higher-degree and repeated-root factors are included;
none is represented as a newly counted curve. The separate factor-order generator
has 36 small companion-determinant checks. Additional tests check the three
uniform proof constants, 4030 finite parameter pairs, 128 Mobius identities,
seven logarithm cases, a residue-rounding control and eleven malformed cases.
The finite checks are not the proof of the all-genus theorem. Decimal is used
only for secondary logarithm spot checks, never by the reconstruction algorithm.

The number 32 is a sufficient genus threshold, not a lower bound. No new uniform
claim for small-field genera 3..31, minimum-query optimality, publication priority,
or quantum/classical runtime advantage is established. Exact ordinary counts
are inputs, not outputs of an executed order-finding routine. The previous
quantum sampler/arithmetic hypotheses do not disappear in characteristic two.

Base commit: 63a617d3302f1ef1df52febe7b8d231c15a2ead6. Existing experiment bytes
and LICENSE are unchanged. All four preceding current verifiers were rerun;
historical root and 164-curve suites were not. See SOURCES.md for the focused
primary-source comparison and its limits. No new repository is required yet.
