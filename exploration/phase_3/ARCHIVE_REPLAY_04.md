# Archive replay 04: pin the real comparison and test a transfer shortcut

28 September 2026. Base: `e6b88a758b10f5f42b18ad4d8a56d88760316323`.
Active branch: `research/prx-quantum-phase2`. Manuscript remains on hold.

**The archive-access step is complete.** The supplied ZIP matches the recorded
Zenodo digest. This checkpoint inspects the released geometries, reproduces
selected published comparisons, and tests a one-reference transfer shortcut.
It does not compute electronic energies, quantum resources, or a new potential.
The [application](APPLICATION_CASE_02.md) remains a feasibility candidate, not an
established quantum advantage. The old operator candidate stays parked.

## 1. Verified bytes, not a recreated benchmark

Source: Timothy Berkelbach's Zenodo record, DOI `10.5281/zenodo.22116355`,
version 1 dated 26 August 2026 [1]. The original ZIP was supplied in this
conversation. It was read without extraction or execution of archive contents.

| Property | Verified value |
|---|---|
| Bytes | 1,380,526 |
| MD5 | `cf3b3c01508a96749a39442850007f32` |
| SHA256 | `edc45a55827ed4f07596d7d1e4a5eccc0b736ee77ffe89e40eee7a20a3b28feb` |
| Inventory | 768 ZIP entries: 763 files and five directories |
| File types | 732 XYZ geometries, 27 TXT tables, three CSV tables, one README |

CRC, duplicate-entry, path-safety, uncompressed-size and symlink checks pass.
Every geometry was parsed; all numerical filenames agree with their lithium
counts and contain C3H4O3. A digest of the full sorted member manifest is recorded
in the [executed report](../../experiments/reference_archive_v1/REPORT.json).

The archive has no separate license or computation scripts. The record's exposed
rights metadata did not establish a specific data license. This checkpoint does
not redistribute the archive, coordinates, or full tables, and does not apply the
parent MIT license to them. The new checker and derived report are independent.

## 2. What the 732 geometries actually represent

Each of the parallel, top, and transition-state numerical sequences contains
243 nested clusters, with 2,4,...,486 lithium atoms. Within each sequence the
EC coordinates are exactly unchanged. All 242 adjacent pairs per sequence have
strictly nested lithium coordinate sets. There are three additional top/prism
geometries, which are not part of those numerical sequences.

Thus these are **cluster-size convergence data around fixed molecular geometries**,
not 732 independent samples of a reactive trajectory. They are useful calibration
data but do not supply a train/test corpus for the proposed energy/force model.

The Li40 files each have 50 nuclei: Li40+C3H4O3. Their SHA256 values are:

```text
parallel/40.xyz
2238b73e2a7f55f57f4ad9c77b7da9b2e5c8860a48fb3c2f9880401cdba66096
transition_state/40.xyz
292b85657cad91c071c566366e74072cc38ab55b3f08f93e3d7547bc70f25154
top/40.xyz
f6cfb8b3344d7732e7f7272d9d8ceab3d16757a4332a4c5d23229802526ede24
```

The XYZ comment lines are blank: they do not encode charge, spin, cell, units,
basis or frozen orbitals. Neutrality is the chosen paper-level cluster convention;
the paper specifies a spin-restricted ground-state singlet. Coordinates should be
interpreted as angstroms in a subsequent declared calculation, consistent with
the paper's length scale and approximately 1.1-coordinate-unit C-H distances.
That convention is not an explicit unit tag in the ZIP. Atom order is not a
certified reaction-path mapping, and the filename does not verify a stationary
point or Hessian of the isolated finite cluster.

Under the audited C/O-core-only AFQMC/ORCA convention, the verified composition
has 166 total and 154 correlated electrons. Spherical cc-pVTZ counting gives
1436 full spatial functions, 1430 after six core orbitals and before virtual
truncation. See [audit 03](REFERENCE_ACCESS_AUDIT_03.md) for basis attribution.
The earlier 74-electron convention and small HCI trial spaces remain different
problems, not equivalent resource estimates. PySCF's exact frozen-orbital/FNO
settings are not supplied by the archive.

## 3. Reproducing the barrier comparison correctly

The archive README specifies kcal/mol for TXT energy differences; CSV semantics
are matched to the paper's DFT comparison [2]. These are barriers or adsorption
energies, not absolute electronic energies or measured runtimes.

| Method | Released Li40 barrier (kcal/mol) |
|---|---:|
| PBE, CSV series | 8.963901278 |
| PBE, separate cc-pVTZ TXT series | 8.662765223 |
| CCSD | 20.912147401 |
| DLPNO-CCSD(T) | 18.870000000 |
| AFQMC | 20.770000000, with reported statistical uncertainty 1.17 |
| omegaB97X-V | 26.457990880 |

The two PBE series are not bytewise or numerically identical. Package/grid/input
settings cannot be inferred from filenames alone. Do not silently substitute one
for the other in a supposedly exact replay.

Using the CSV PBE series, the paper's **supplied rounded** PBE surface limit 5.6,
and its stated method endpoints reproduces four Table II barrier values:

$$
B_m^{\mathrm{replay}}=B_m(N_m)+5.6-B_{\mathrm{PBE,CSV}}(N_m).
$$

| Method | Endpoint N | Computed replay | Paper, one decimal |
|---|---:|---:|---:|
| CCSD | 50 | 16.006957805 | 16.0 |
| DLPNO-CCSD(T) | 40 | 15.506098722 | 15.5 |
| AFQMC | 40 | 17.406098722 | 17.4 |
| omegaB97X-V | 100 | 17.916873428 | 17.9 |

The three correlated replays also round to the paper's 16.3 mean and 0.8
population standard deviation. That spread is not a certified accuracy bound.
This replay does not independently derive the 5.6 limit, validate the finite-size
transfer, or reproduce every entry of Table II. In particular, raw Li40 numbers
must not be compared with another method's already-corrected surface estimate.

## 4. Two release/analysis distinctions to preserve

**AFQMC trial refinement.** `data/parallel_afqmc.txt` has -26.22 at Li40. It agrees
with the paper's earlier single-determinant result, not its refined HCI-trial
result of approximately -21.0 (Table III). The same issue occurs at N=26,28,38.
The checker leaves the archive unchanged and uses a separately attributed,
rounded Table III overlay only where explicitly stated. This is not new
correlated data or a source repair. The refined result's full precision is absent,
and we do not claim an exact replay of the final parallel-adsorption estimate.

**NPE averaging interval.** All 12 inspected Table I values (PBE, CCSD,
DLPNO-CCSD(T), AFQMC; three observables) reproduce to two decimals using
10 <= N < N_max, the CSV PBE series where relevant, and the attributed HCI
parallel overlay. The caption literally says more than 10; the strict interval
10 < N gives barrier NPEs 1.044607, 2.637415 and 1.860621 for the three correlated
methods, rather than 1.17, 2.54 and 1.80. Both conventions are recorded, not
silently conflated. Agreement under the inclusive lower endpoint is a numerical
reconstruction, not proof of the authors' original analysis code.

NPE is mean absolute scatter of a method difference about its fitted mean.
It is neither an absolute error against physical truth nor held-out model error.
AFQMC statistical noise also contributes. These distinctions prevent assigning
all disagreement to a quantum-removable electronic error.

## 5. A bounded test of one useful-sounding shortcut

We tested the retrospective rule: obtain one accurate correction at Li40, add
that same correction to all other PBE barriers, and avoid further expensive
reference calculations. For each released correlated method m, define

$$
\widehat B_m(N)=B_{\mathrm{PBE,CSV}}(N)
+B_m(40)-B_{\mathrm{PBE,CSV}}(40).
$$

At all other available even N >= 12, the differences from that method's released
values are:

| Target released method | Other sizes | Mean absolute discrepancy | Maximum discrepancy |
|---|---:|---:|---:|
| CCSD | 19 | 1.986552 | 4.213527 |
| DLPNO-CCSD(T) | 14 | 3.428287 | 6.578234 |
| AFQMC | 14 | 3.064380 | 5.485492 |

All values are kcal/mol. This was designed after inspecting the data and is not
a preregistered or blinded test. The targets are approximate electronic methods,
not exact truth; their available N ranges differ. It is not a ranking of the
methods or a learned force-field validation.

The narrow conclusion is that **one Li40 correction does not reproduce the
released method's whole size sequence at uniformly small tolerance**. Merely
making that one correction more precise does not establish its transfer to
other sizes, still less to different molecular configurations. This does not
rule out multiple references, a structured correction, active learning,
embedding, or quantum-assisted potential construction.

This is a diagnostic of an application assumption, not a new theorem or a
standalone result to spin off.

## 6. What is now possible, and what is still missing

The geometry/composition and released scalar comparison are pinned. A new
explicitly configured Hamiltonian calculation can now be constructed from these
coordinates; it must be labeled a new implementation, not an exact job replay.
The archive does not include SCF orbitals, integral tensors/factors, full job
inputs, FNO cutoffs/retained counts, absolute energy outputs, hardware/timing logs,
HCI coefficients, force labels, or model weights. Those quantities cannot be
recovered from a table of energy differences alone.

No native electronic or quantum calculation was run. The system-qubit bookkeeping
is not a gate/runtime estimate; no Hamiltonian normalization or state-overlap
bound has been computed. Missing job details are a reproducibility limitation,
not evidence that classical computation is intrinsically hard.

**Next research decision:** establish an accuracy-versus-total-preparation-cost
case for reusable references, not just a precise Li40 energy. Use the pinned pair
as a calibration. Explicitly budget the finite-size/environment transfer and the
model's error on unseen molecular configurations; test whether the proposed
quantum reference precision would change the required prediction. Permit modern
classical correlated methods, hybrid references and energy-only/active learning.
If a small independent Hamiltonian calculation is warranted, state its core,
basis, truncation and state-preparation choices, and compare at equal required
observable quality. Do not launch a full 1430-orbital resource/training campaign
or claim a new useful simulator just because the geometry file is now available.

No further archive upload is needed. No new repository or spin-off is justified.

## 7. Executed verification

```sh
python experiments/reference_archive_v1/verify.py --archive /path/to/paper_data.zip
```

Python 3.10+, standard library only, no file writes or archive extraction. The
final checker was executed twice and produced identical JSON. Its eight malformed
input controls pass. A modified archive was rejected by SHA256, and both -O/-OO
refusals were checked. All 732 XYZ files and all 30 data tables were parsed.
The report contains selected member hashes plus the full-manifest digest.

Source SHA256: `bc7cc5208cd70624e2896d05338f1799d2ddbfa736d1d4f0071646b95ce80921`.
Report SHA256: `712d36638d4786b7405e5130a6ec4fa094b90822b31cfce2f302e691ebce9c68`.

Fractions are exact through the arithmetic; reported decimals are formatted to
nine places and do not imply new physical precision. This is data/protocol
verification, not electronic-structure or quantum simulation, solver timing,
force-field training, or an experimental battery result. Root/historical suites
were not rerun because their code and fixtures were unchanged. Full Git checkout
failed on DNS; GitHub connector access worked. No outside contact or paid run.

Sources checked 28 September 2026:

[1] https://zenodo.org/records/22116355 . Search-visible primary metadata checked
against the supplied archive. Direct record/API opens failed. No claim of a
specific reusable data license follows from the displayed rights field.

[2] E. A. Vo et al., *Adsorption energies and decomposition barrier heights for
ethylene carbonate on the surface of lithium from cluster-based quantum chemistry*,
arXiv:2603.22139v1. Methods, Eqs. (1)-(3), Tables I-III, Supplement S3/Table S1.
PDF pages 2, 3, 7 and 8 (zero-based) inspected visually.
https://arxiv.org/pdf/2603.22139v1
