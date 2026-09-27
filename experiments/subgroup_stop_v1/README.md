# Subgroup-certified stopping

A focused diagnostic for [Phase-2 note 24](../../exploration/phase_2/SUBGROUP_CERTIFIED_STOPPING_24.md).

The generated subgroup and the ambient group are different objects. `subgroup.py`
checks supplied exact orders, applies the bounded cofactor method to the generated
subgroup, and accepts an ambient cardinality only when its rigorous interval
contains one multiple of the computed subgroup size. No ambient-generation promise
is accepted as a shortcut. The complete proof and cost limitations are in note 24.

Run from any checkout with Python 3.10 or later, standard library only:

```sh
python experiments/subgroup_stop_v1/verify.py
```

The verifier checks the manifest and reproduces `REPORT.json` byte-for-byte in a
temporary copy. It never overwrites expected evidence. Do not use `-O` or `-OO`.
The source uses no external service and receives no coordinate decoder or ambient
size through its group interface. Fixture code separately knows the true direct
product in order to check answers; these groups are not hard discovery inputs.

## Actual scope

The report covers 662 lists, 1,986 exact subgroup completions, 3,310 ambient
interval decisions and 1,236 nonminimal-order rejections, plus targeted malformed,
large-integer, incomplete-list and budget controls. Eleven direct-product fixtures
include all ordered lists of length at most two; one rank-three basis is added.
Intervals include singleton and duplicate tiny-case policies, so aggregate
acceptance counts are not empirical success probabilities. No old curve suite,
root historical verifier, native counter, quantum sampler or hardware was run.

`cap` limits the value `floor(U/E)` used for optional cofactor completion; it is
not a wall-time or whole-workflow budget. Exact primality uses trial division in
this diagnostic; order factorization and all candidate orders are classically
supplied. Neither operation is represented as free or as production-scale
polynomial-bit-time code. The abstract proof allows standard certified prime
factorizations, whose acquisition/checking costs must be charged separately.
Correct finite abelian group operations, valid elements and the rigorous ambient
interval remain trusted premises. Tests are not end-to-end formal verification.

## Provenance

New source, not a transcription of a native solver or the unavailable predecessor
archive. Base branch commit: `4a22c36b249a69bd172fe5c47b988e02c91c52c8`.
The exact-order, primary decomposition and digit-lifting ingredients follow the
mathematical contracts in notes 22-23 and the primary references in note 24.
The predecessor ZIP was located, but its raw-byte materialization failed; it was
not imported or rerun. Historical repository files and licenses remain unchanged.
