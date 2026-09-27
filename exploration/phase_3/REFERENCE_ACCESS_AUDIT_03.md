# Reference audit 03: use the published electronic problem

28 September 2026. Base: `13e8a7135a2061b826911e4cbad7fff786ba5147`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**Outcome:** public reference data were located, and the proposed matched-input
calibration needs a frozen-core correction. The quantum/classical runtime comparison
is not complete. This is a source and protocol audit, not a new chemistry result.
The [application case](APPLICATION_CASE_02.md) remains the motivation; its dated
access statement and hypothetical lithium-core convention are superseded here.

## 1. The geometry deposit exists

The authors' [Zenodo record](https://zenodo.org/records/22116355), DOI
`10.5281/zenodo.22116355`, was published on 26 August 2026. It supplies
`paper_data.zip` (displayed size 1.4 MB), with listed MD5
`cf3b3c01508a96749a39442850007f32`.
The [archive preview](https://zenodo.org/records/22116355/preview/paper_data.zip?include_deleted=0)
lists, among other entries:

```text
README.md
geometries/parallel/40.xyz
geometries/top/40.xyz
geometries/transition_state/40.xyz
data/energy_barrier_ccsd.txt
data/energy_barrier_dlpno_ccsd-t.txt
data/energy_barrier_afqmc.txt
```

The listing is not an inspection of the member bytes. It supports locating the
calibration, not yet its coordinate hashes, composition, units, or job settings.
This is the static cluster study's deposit; it is not established to contain the
other paper's molecular-potential training set or model weights.

Web access exposed the record and directory listing, but attempts to transfer the
ZIP into the execution environment failed. No archive checksum or member hash has
been verified. A local copy or user upload of the original ZIP is sufficient for
the next access step; no author contact is needed. No suitable Zenodo connector
was found. The displayed rights section did not establish a reusable data license
in this audit. Review the archive and record rights before repository redistribution;
the parent's MIT license does not automatically cover the deposit.

## 2. A substantive correction to the calibration

Vo et al. [1], Supplement S3, specifies frozen C/O 1s orbitals for ph-AFQMC and
identifies the same default for ORCA. The ORCA 6.0 manual [2], Table 7.15, confirms
zero frozen electrons for Li and two each for C and O. Thus the previous proposal
to freeze lithium 1s as well is **not the matched published convention**. Do not
silently transfer that proposal into a resource estimate.

For neutral Li40+C3H4O3, assuming that composition until coordinates are read:

| Quantity | AFQMC/ORCA convention for the calibration | Earlier hypothetical Li/C/O-core convention |
|---|---:|---:|
| Total electrons | 166 | 166 |
| Frozen spatial orbitals | 6 | 46 |
| Correlated electrons | 154 | 74 |
| Full spherical cc-pVTZ spatial basis | 1436 | 1436 |
| Spatial orbitals after core removal, before virtual truncation | 1430 | 1390 |

This is integer bookkeeping, not an active-space adequacy argument. The specific
PySCF CCSD core/virtual settings still need their own input-level confirmation;
do not infer every code's configuration from the ORCA default.

The cc-pVTZ contractions in the inspected PySCF basis source [3] give 30 spherical
functions per Li, C, or O atom and 14 per H. Hence

```text
40*30 + 3*30 + 3*30 + 4*14 = 1436
166 - 2*6 = 154
1436 - 6 = 1430
```

The analogous Li50 calculation gives 1736 functions, matching the paper's stated
basis dimension [1]. The arithmetic was executed locally with exact integers.
No linear-dependency pruning, integral construction, or orbital calculation was run.
For reproduction, Python 3.10+ needs no dependencies:

```python
shells = {"H": (3, 2, 1), "Li": (4, 3, 2, 1),
          "C": (4, 3, 2, 1), "O": (4, 3, 2, 1)}
basis = {s: sum(n * (2*l + 1) for l, n in enumerate(v))
         for s, v in shells.items()}
full = 40*basis["Li"] + 3*basis["C"] + 4*basis["H"] + 3*basis["O"]
print(full, 166 - 2*6, full - 6, 2*(full - 6))
# 1436 154 1430 2860
```

For one untapered second-quantized occupation encoding, the untruncated correlation
space therefore uses 2860 system qubits, before auxiliary registers and error
correction. This is **not a minimum qubit requirement**, a gate estimate, or a
rejection of other encodings, embeddings, or justified orbital compression. Their
approximation error must be included rather than deleting orbitals for convenience.

A related trap appears in Supplement Table S1 [1]: the Li40+EC HCI trial for the
parallel geometry has a small (20e,19o) active space. That is a **trial wavefunction
for the AFQMC calculation**, not the complete correlation space being solved.
Its retained CI percentage is not the initial-state overlap of a proposed quantum
phase-estimation algorithm. Neither a tiny matched quantum problem nor an overlap
bound follows from that table.

## 3. Reference forces are not automatically required

Kundu et al. [4], Methods IV.B, trained the molecular CCSD(T) potential without
force labels. Their datasets use approximately 4500 training/validation
configurations and 3000 unseen test configurations. This is a useful precedent
for an **energy-only reference route**, not proof of its accuracy at the metal
surface and not a lower bound on the number of new quantum references.

Consequently, neither of two shortcuts is justified: treating energy measurements
as if they deliver free force labels, or multiplying the cost by all finite-difference
coordinates and declaring that penalty unavoidable. Energy-only learning and actual
quantum force algorithms [5] are alternatives with different costs. Any learned
energy still needs force/trajectory validation; an energy fit alone does not
establish useful dynamics. Classical active selection must be allowed too.

This keeps the possible quantum contribution offline. The target remains a
classical simulator used on later configurations, not quantum calls at every
simulation step or a list of stationary energies.

## 4. What the comparison still lacks

| Required item | Current status |
|---|---|
| Published calibration coordinates | Listed publicly; not transferred or hash-checked |
| Charge, spin, basis and core convention | Paper-level specification audited; actual input files not replayed |
| Classical benchmark | Appropriate published methods identified; no matched native timings measured |
| Reduced orbital space | CCSD uses FNO truncation [1]; the retained orbital count and error cannot be assumed for our quantum calculation |
| Quantum cost | Hamiltonian coefficients/factorization, preparation overlap, error budget and circuit costs not yet computed |
| Useful simulator | No new reference set, trained model, or deployment benefit established |

The static parallel-to-transition-state pair is a reproducible calibration target,
not yet a test of the fluctuating surface pathway in the dynamics application.
A better finite-cluster energy cannot automatically be transferred to an extended,
solvated or voltage-controlled surface. A public dataset does not remove these
scientific questions.

**Next decision:** obtain the small archive, inspect its README and rights, check
its checksum, hash the relevant geometry/data members, and establish a matched
parallel/transition-state calculation before assigning electronic resource numbers.
Then assess whether the electronic improvement can change a useful prediction
beyond embedding/environment and learned-model errors. Do not launch a training
campaign or a larger quantum simulation based only on the basis count.

## 5. Evidence boundary and sources

No archive was imported; no molecular, electronic, quantum-circuit or performance
calculation was executed. No new verifier or framework was added. The integer
accounting above was executed; root and historical research suites were not rerun.
Their code, reference outputs, the earlier notes and LICENSE are unchanged. Git
checkout failed on DNS; the GitHub connector worked. No outside contact occurred.

Sources checked 28 September 2026; bounded protocol audit, not a novelty review:

[1] E. A. Vo et al., arXiv:2603.22139v1, Methods and Supplement S3/Table S1.
PDF pages 7 and 8 (zero-based) were visually inspected, including the trial-space
table. Earlier main-text figures were also inspected. No timing inferred from plots.
https://arxiv.org/pdf/2603.22139v1

[2] ORCA 6.0 Manual, Section 7.12, Table 7.15. This is the version used in [1],
not a statement about every package or user-specified core convention.
https://www.faccts.de/docs/orca/6.0/manual/contents/detailed/frozencore.html

[3] PySCF `pyscf/gto/basis/cc-pvtz.dat`, Git blob
`d7500e428cf8d0a78c77d00dbf66a43ed073332a`; H/Li/C/O contraction structure inspected.
The file credits the original basis literature. No source implementation imported.
https://github.com/pyscf/pyscf/blob/master/pyscf/gto/basis/cc-pvtz.dat

[4] S. Kundu et al., arXiv:2509.14067v1, Methods IV.A-B. PDF page 4 visually
inspected. Energy-only molecular training is not a surface demonstration.
https://arxiv.org/pdf/2509.14067v1

[5] T. E. O'Brien et al., arXiv:2111.12437v2, *Efficient quantum computation of
molecular forces and other energy gradients*, later Phys. Rev. Research 4, 043210
(2022). Abstract and algorithm organization inspected; no full 62-page audit and
no force-resource estimate for Li40+EC were made.
https://arxiv.org/abs/2111.12437
