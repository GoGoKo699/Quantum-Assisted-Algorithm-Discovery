# General-translation cost audit

A standalone arithmetic companion to
[Phase-2 Note 25](../../exploration/phase_2/FAMILY_AND_TRANSLATION_COST_25.md).
The note specifies a standard local-zeta workload and derives a constructive,
conservative bound for canonical controlled Jacobian translation:

$$
\widetilde O(g^3n^2b^2+g n^3b^3),\qquad b=\lceil\log_2 p\rceil.
$$

It includes general-support Cantor composition, bounded reduction, coherent
validation, invalid-encoding behavior and clean uncomputation. This is NOT a
compiled circuit, a numerical Toffoli count, a native arithmetic benchmark or a
new quantum algorithm. The classical comparator can use better arithmetic and
can bypass group orders by computing the Weil polynomial directly.

## Reproduce

```sh
python experiments/translation_cost_v1/verify.py
```

Python 3.10 or later, standard library only. Do not use `-O` or `-OO`. The verifier
checks file hashes and compares a fresh exact report in temporary storage with
the immutable REPORT.json. It does not overwrite expected evidence.

The checks cover 48 sample bounds by independent rational convolution, 2080
polynomial-degree inequalities, 42 sufficient coefficient-lifting precisions,
4096 integer logarithms, eight invalid-input controls and the exact historical
Note 21 totals. These are arithmetic checks, not executions of the group law.
The queried q/p values in `cost.py` are size parameters; that module does not
certify a finite field or construct a curve. Its precision check does not replace
a native Frobenius implementation's own working-precision contract.

## Do not turn the report into a performance claim

The two `formal_*_term` fields multiply translation counts by the monomials in
the asymptotic bound. They intentionally have no fitted constants or physical
units. They are neither gate counts nor measured times. Their exact ratios are
not speedups and do not rank quantum and classical algorithms.

`max_accumulator_bits` includes degree tags for one canonical Mumford data
register. It excludes the second register and store-all-history work space.
`initial_translations` is only the order-acquisition stage. Classical completion,
retries and full fallback cannot be omitted from any end-to-end comparison.

The older 20-call/15-call illustration is reproduced to check the new accounting,
not substituted for the stronger endpoint-completed schedule in the intervening
notes. No historical source/result file is changed. See [SOURCES.md](SOURCES.md)
for publication scope, access limitations and exact provenance.
