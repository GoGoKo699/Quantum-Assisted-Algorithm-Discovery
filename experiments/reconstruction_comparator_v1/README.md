# Matched reconstruction comparator

This focused audit implements [Note 26](../../exploration/phase_2/MATCHED_RECONSTRUCTION_COMPARATOR_26.md).
The fresh-twist schedule and a pruned base-change-only schedule supply exactly
interconvertible cardinality transcripts with the same number of calls. What
changes is the field degree of those calls, not their count.

```sh
python experiments/reconstruction_comparator_v1/verify.py
```

Python 3.10 or later, standard library only. The verifier copies the source and
its pinned `translation_cost_v1/cost.py` dependency to temporary storage, checks
hashes, and reproduces `REPORT.json` exactly. It never overwrites reference data.
Do not run with `-O` or `-OO`.

`transcripts.py` converts the two transcripts using exact multiplication/division
and implements the inherited rational-log, Newton, endpoint and reciprocity
reconstruction. Its input orders are supplied, not discovered or authenticated.
The field-size parameter is not a field/primality certificate. A consistent
transcript and successful coefficient divisions are not end-to-end verification.

`checks.py` compares independently traversed dyadic chains; reconstructs twelve
supplied factored Weil polynomials through both routes; uses independent companion
determinants and retained low-genus controls; checks matched cost identities; and
rejects deliberately malformed transcripts. The factored polynomials are not
claimed to be arbitrary curve Jacobians or difficult discovery instances.

The genus-ten resource row uses the SAME inherited quantum backend and 12-call
error allocation for both schedules. `formal_*` quantities have no physical units
or fitted constants; their ratios are not gate savings, runtime measurements, or
quantum/classical speedups. The single-accumulator width excludes arithmetic
workspace. A cost-asymmetry control deliberately makes twists expensive and
reverses the preference. This is not an optimal scheduling or native solver tool.

Base commit: `8daa8ae16458acd25155179ad2ab35a97f600b40`. No earlier source or result
file is modified. The existing two current verifiers were rerun unchanged; the
historical root and 164-curve suites were not. Source comparison and its limits
are in [SOURCES.md](SOURCES.md). No new repository is needed for this supporting
comparison; it has not established an independent publication contribution.
