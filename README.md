# Quantum-Assisted Algorithm Discovery

**Can a circuit-model quantum computer discover a useful reusable classical method
more efficiently than a strong classical discovery process?** The resulting method
should run classically. Compactness and reuse alone do not establish quantum advantage.

**Status: continuing exploration. No useful quantum discovery advantage is established.
Manuscript preparation is on hold.**

## Start here

Read the [project map](PROJECT_MAP.md) for the objective, independent spin-offs,
branch roles, and continuation boundaries. The [active parent work order](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/work_orders/CURRENT.md)
and [phase-2 charter](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/exploration/phase_2/CHARTER.md) govern the ongoing exploration.

The active working branch is `research/prx-quantum-phase2`. This default branch is
the public entry point and retains earlier evidence; it is not a merged copy of
all later research. Sorting, filters, matrix multiplication, and reconstruction
are not mandatory directions for the next step.

## Two independent classical spin-offs

| Project | Work now owned by that project |
|---|---|
| [Algebraic-Loop-Certificates](https://github.com/GoGoKo699/Algebraic-Loop-Certificates) | Classical loop certificates, reusable summaries, and verification integration |
| [Sparse-Weil-Reconstruction](https://github.com/GoGoKo699/Sparse-Weil-Reconstruction) | Exact selected-data reconstruction of Weil polynomials, proof, and decoder |

Both have their own projects and repositories. Their further development belongs
there. They retain value on their own terms, but neither substitutes for the
parent's quantum-discovery objective. The parent keeps provenance and supporting
references rather than a duplicate development agenda.

## What the parent must establish

A candidate needs a useful classical output, a genuine quantum role in obtaining
it, and a complete comparison against strong classical alternatives. Account for
preparation, discovery, certification, extraction, error handling, and later use.
A classical competitor may obtain the same benefit without reproducing the proposed
quantum pipeline. The [charter](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/research/prx-quantum-phase2/exploration/phase_2/CHARTER.md) sets the detailed standard.

## Preserved evidence and reproduction

The [sorting-completion experiment](experiments/sorting_completion_v1/README.md),
[eleven-bank filter screen](experiments/depth2_cover_v1/README.md), and older guided,
target-closure, and filter experiments remain available in their versioned
directories. They are retained checkpoints, not the default next task. Their
scientific claims and limitations are unchanged. The older sections of the
[claim ledger](STATUS.md) and [guided-search design](docs/current-design.md) are
historical records, not competing current work orders.

For the preserved sorting-completion checks, with Python 3.10 or later:

```sh
python experiments/sorting_completion_v1/verify.py
```

The optional native-Z3 check is:

```sh
python experiments/sorting_completion_v1/verify.py --solver
```

See each experiment's README for its verification scope and dependencies. Generated
data belong in temporary paths. Never use Python `-O` or `-OO` for assertion-dependent
checks. Historical timing and timeout observations are not deterministic expectations;
old quantum resource figures apply only to their original constructions.

This organizational update reran no experimental verifier and introduces no new
scientific result. All experiment sources, reports, proof notes, manifests,
third-party notices, and the original [MIT license](LICENSE), Copyright (c) 2026
Ruge Lin, are preserved.
