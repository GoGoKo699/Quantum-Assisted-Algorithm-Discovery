#!/usr/bin/env python3
"""Audit the user-supplied Zenodo ZIP; no extraction or electronic calculation.

Python 3.10+, standard library. Does not modify the archive or any stored report.
Rounded publication constants are explicitly distinct from archive data. See
exploration/phase_3/ARCHIVE_REPLAY_04.md for interpretation and attribution.
"""
from __future__ import annotations
import argparse
from collections import Counter
import csv
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import stat
import sys
from zipfile import BadZipFile, ZipFile

ARCHIVE_SHA256 = "edc45a55827ed4f07596d7d1e4a5eccc0b736ee77ffe89e40eee7a20a3b28feb"
ARCHIVE_MD5 = "cf3b3c01508a96749a39442850007f32"
GEOMETRY_SHA256 = {
    "parallel": "2238b73e2a7f55f57f4ad9c77b7da9b2e5c8860a48fb3c2f9880401cdba66096",
    "top": "f6cfb8b3344d7732e7f7272d9d8ceab3d16757a4332a4c5d23229802526ede24",
    "transition_state": "292b85657cad91c071c566366e74072cc38ab55b3f08f93e3d7547bc70f25154",
}
# Vo et al., arXiv:2603.22139v1 Table III, not values supplied by the ZIP.
HCI_PARALLEL = {26: F("-18.3"), 28: F("-13.8"), 38: F("-17.8"), 40: F("-21.0")}
PUBLISHED_NPE = {
    "top": {"PBE": "0.13", "ccsd": "0.60", "dlpno_ccsd-t": "0.85", "afqmc": "1.03"},
    "parallel": {"PBE": "0.18", "ccsd": "0.84", "dlpno_ccsd-t": "1.08", "afqmc": "1.62"},
    "energy_barrier": {"PBE": "0.34", "ccsd": "1.17", "dlpno_ccsd-t": "2.54", "afqmc": "1.80"},
}
# Table II barrier values; PBE's rounded limit is an INPUT, not regenerated.
PBE_LIMIT = F("5.6")
PUBLISHED_BARRIERS = {"ccsd": "16.0", "dlpno_ccsd-t": "15.5", "afqmc": "17.4", "wB97X-V": "17.9"}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def number(text: str) -> F:
    require(len(text) <= 100, "Numeric field too long")
    value = Decimal(text)
    require(value.is_finite() and abs(value.adjusted()) <= 100, "Invalid numeric field")
    return F(value)


def display(x: F) -> str:
    with localcontext() as ctx:
        ctx.prec = 40
        return format(Decimal(x.numerator) / Decimal(x.denominator), ".9f")


def xyz(text: str) -> tuple[tuple[str, F, F, F], ...]:
    lines = text.splitlines()
    require(len(lines) >= 3, "Truncated XYZ")
    count = int(lines[0])
    require(0 < count <= 1000, "Invalid XYZ count")
    rows = [line.split() for line in lines[2:] if line.strip()]
    require(len(rows) == count, "XYZ count mismatch")
    require(all(len(r) == 4 and r[0] in {"Li", "C", "H", "O"} for r in rows), "Invalid XYZ row")
    atoms = tuple((r[0], *(number(t) for t in r[1:])) for r in rows)
    require(len(set(a[1:] for a in atoms)) == count, "Coincident nuclei")
    return atoms


def table(text: str) -> dict[int, tuple[F, ...]]:
    result = {}
    for line in text.splitlines():
        if not line.strip():
            continue
        row = line.split()
        require(len(row) in (2, 3), "Invalid energy table width")
        n = number(row[0])
        require(n.denominator == 1 and n > 0 and n % 2 == 0, "Invalid cluster index")
        require(int(n) not in result, "Duplicate cluster index")
        values = tuple(number(t) for t in row[1:])
        require(len(values) != 2 or values[1] >= 0, "Negative reported uncertainty")
        result[int(n)] = values
    require(bool(result), "Empty energy table")
    return result


def csv_table(text: str) -> dict[int, dict[str, F]]:
    reader = csv.DictReader(io.StringIO(text))
    require(reader.fieldnames == ["n Li", "PBE", "PBED3", "PBE0", "PBE0D3", "wB97X-V"], "Unexpected CSV schema")
    result = {}
    for row in reader:
        n = int(row.pop("n Li"))
        require(n > 0 and n % 2 == 0 and n not in result, "Invalid/duplicate CSV index")
        result[n] = {k: number(v) for k, v in row.items()}
    return result


def mad(values: list[F]) -> F:
    require(bool(values), "Empty deviation set")
    mean = sum(values) / len(values)
    return sum(abs(x - mean) for x in values) / len(values)


def self_tests() -> int:
    bad = [lambda: xyz("2\n\nLi 0 0 0\n"),
           lambda: xyz("1\n\nLi nan 0 0\n"),
           lambda: xyz("2\n\nLi 0 0 0\nH 0 0 0\n"),
           lambda: table("2 1\n2 2\n"), lambda: table("3 1\n"),
           lambda: table("2 1 -0.1\n"), lambda: table("2 Infinity\n"),
           lambda: csv_table("n Li,PBE\n2,1\n")]
    for f in bad:
        try:
            f()
        except (ValueError, ArithmeticError):
            continue
        raise ValueError("Malformed-input control accepted")
    require(mad([F(2), F(4), F(6)]) == F(4, 3), "MAD arithmetic control")
    return len(bad)


def audit(path: Path) -> dict:
    require(path.stat().st_size <= 10_000_000, "Archive exceeds audit size limit")
    blob = path.read_bytes()
    require(hashlib.sha256(blob).hexdigest() == ARCHIVE_SHA256, "Archive SHA256 mismatch; not the pinned release")
    require(hashlib.md5(blob).hexdigest() == ARCHIVE_MD5, "Archive MD5 mismatch")
    with ZipFile(io.BytesIO(blob)) as z:
        entries = z.infolist()
        require(len(entries) == 768 and len({e.filename for e in entries}) == 768, "Wrong/duplicate ZIP entries")
        require(sum(e.file_size for e in entries) <= 10_000_000, "Uncompressed data too large")
        for e in entries:
            p = PurePosixPath(e.filename)
            require(not p.is_absolute() and ".." not in p.parts and "\\" not in e.filename and ":" not in e.filename, "Unsafe ZIP path")
            require(not stat.S_ISLNK(e.external_attr >> 16), "ZIP symlink rejected")
            require(not (e.flag_bits & 1), "Encrypted ZIP rejected")
        require(z.testzip() is None, "ZIP CRC failure")
        raw = {e.filename: z.read(e) for e in entries if not e.is_dir()}
    require(len(raw) == 763, "Wrong regular-file count")
    geom_names = sorted(n for n in raw if n.endswith(".xyz"))
    txt_names = sorted(n for n in raw if n.startswith("data/") and n.endswith(".txt"))
    csv_names = sorted(n for n in raw if n.startswith("data/") and n.endswith(".csv"))
    require((len(geom_names), len(txt_names), len(csv_names)) == (732, 27, 3), "Unexpected release inventory")
    require(set(raw) == {"README.md", *geom_names, *txt_names, *csv_names}, "Unexpected non-data member")
    manifest = [[n, len(b), hashlib.sha256(b).hexdigest()] for n, b in sorted(raw.items())]
    manifest_hash = hashlib.sha256(json.dumps(manifest, separators=(",", ":")).encode()).hexdigest()
    groups = {}
    for family in ("parallel", "top", "transition_state"):
        prefix = "geometries/" + family + "/"
        names = [n for n in geom_names if n.startswith(prefix)]
        molecules, shells = set(), {}
        for n in names:
            atoms = xyz(raw[n].decode())
            composition = Counter(a[0] for a in atoms)
            require({s: composition[s] for s in ("C", "H", "O")} == {"C": 3, "H": 4, "O": 3}, "Wrong EC composition")
            stem = PurePosixPath(n).stem
            if stem.isdigit():
                k = int(stem)
                require(composition["Li"] == k, "Geometry filename/composition mismatch")
                molecules.add(tuple(a for a in atoms if a[0] != "Li"))
                shells[k] = {a for a in atoms if a[0] == "Li"}
        require(sorted(shells) == list(range(2, 487, 2)), "Missing numerical cluster geometry")
        require(len(molecules) == 1, "EC moved along cluster-size sequence")
        require(all(shells[n] < shells[n+2] for n in range(2, 485, 2)), "Non-nested cluster sequence")
        selected = prefix + "40.xyz"
        require(hashlib.sha256(raw[selected]).hexdigest() == GEOMETRY_SHA256[family], "Li40 geometry hash mismatch")
        groups[family] = {"files": len(names), "nested_pairs": 242, "distinct_EC_coordinate_sets_in_numerical_sequence": 1, "Li40_sha256": GEOMETRY_SHA256[family]}
    composition40 = Counter(a[0] for a in xyz(raw["geometries/parallel/40.xyz"].decode()))
    atomic_numbers = {"Li": 3, "C": 6, "H": 1, "O": 8}
    shells = {"H": (3, 2, 1), "Li": (4, 3, 2, 1), "C": (4, 3, 2, 1), "O": (4, 3, 2, 1)}
    electrons = sum(composition40[s] * atomic_numbers[s] for s in composition40)
    cores = composition40["C"] + composition40["O"]
    basis = sum(composition40[s] * sum((2*l+1)*count for l, count in enumerate(shells[s])) for s in composition40)
    require((electrons, cores, basis) == (166, 6, 1436), "Matched-convention counting control")
    energies = {n: table(raw[n].decode()) for n in txt_names}
    dfts = {n: csv_table(raw[n].decode()) for n in csv_names}
    npe, strict = {}, {}
    for prop in ("top", "parallel", "energy_barrier"):
        baseline = {n: t[0] for n, t in energies[f"data/{prop}_pbe-def2svp.txt"].items()}
        for method, upper in (("PBE", 100), ("ccsd", 50), ("dlpno_ccsd-t", 40), ("afqmc", 40)):
            values = ({n: t["PBE"] for n, t in dfts[f"data/{prop}_dft.csv"].items()} if method == "PBE"
                      else {n: t[0] for n, t in energies[f"data/{prop}_{method}.txt"].items()})
            if prop == "parallel" and method == "afqmc":
                values = values | HCI_PARALLEL  # separate, attributed overlay; archive is unmodified
            delta = [values[n]-baseline[n] for n in sorted(values) if 10 <= n < upper]
            result = mad(delta)
            require(abs(result-F(PUBLISHED_NPE[prop][method])) < F("0.005"), "Printed Table I NPE not reproduced")
            npe[prop + "/" + method] = display(result)
            if prop == "energy_barrier" and method != "PBE":
                strict[method] = display(mad([values[n]-baseline[n] for n in sorted(values) if 10 < n < upper]))
    dft = dfts["data/energy_barrier_dft.csv"]
    barriers40, corrected, diagnostics = {}, {}, {}
    for method, endpoint in (("ccsd", 50), ("dlpno_ccsd-t", 40), ("afqmc", 40), ("wB97X-V", 100)):
        values = ({n: t[method] for n, t in dft.items()} if method == "wB97X-V" else
                  {n: t[0] for n, t in energies[f"data/energy_barrier_{method}.txt"].items()})
        barriers40[method] = display(values[40])
        value = values[endpoint] + PBE_LIMIT - dft[endpoint]["PBE"]
        require(abs(value-F(PUBLISHED_BARRIERS[method])) < F("0.05"), "Printed Table II barrier not reproduced")
        corrected[method] = {"endpoint_N": endpoint, "from_released_rows": display(value), "published_rounded": PUBLISHED_BARRIERS[method]}
        if method != "wB97X-V":
            shift = values[40] - dft[40]["PBE"]
            indices = [n for n in sorted(values) if n >= 12 and n != 40]
            residuals = {n: dft[n]["PBE"]+shift-values[n] for n in indices}
            worst = max(indices, key=lambda n: abs(residuals[n]))
            diagnostics[method] = {"anchor_N": 40, "other_sizes": len(indices),
                "mean_absolute_residual": display(sum(abs(x) for x in residuals.values())/len(indices)),
                "max_absolute_residual": display(abs(residuals[worst])), "worst_N": worst}
    barriers40["PBE_csv"] = display(dft[40]["PBE"])
    barriers40["PBE_ccpvtz_txt"] = display(energies["data/energy_barrier_pbe-ccpvtz.txt"][40][0])
    selected = {n: hashlib.sha256(raw[n]).hexdigest() for n in sorted(raw) if n == "README.md" or n.startswith("data/energy_barrier_")}
    return {"status": "pass", "archive": {"bytes": len(blob), "md5": ARCHIVE_MD5, "sha256": ARCHIVE_SHA256,
            "zip_entries": 768, "files": 763, "xyz_files": 732, "data_tables": 30,
            "manifest_sha256": manifest_hash}, "geometry_sequences": groups,
            "Li40_convention": {"composition": dict(composition40),
                "charge_assumption": 0, "spin_from_paper": "singlet", "total_electrons": electrons,
                "frozen_core_spatial_orbitals_AFQMC_ORCA": cores, "correlated_electrons": electrons-2*cores,
                "ccpVTZ_spherical_functions": basis, "post_core_spatial_orbitals_before_virtual_truncation": basis-cores},
            "Li40_barriers_kcal_mol": barriers40,
            "reported_AFQMC_Li40_statistical_uncertainty": display(energies["data/energy_barrier_afqmc.txt"][40][1]),
            "Table_II_barrier_replay_with_published_PBE_limit_5_6": corrected,
            "Table_I_NPE_replay_including_N10": npe, "strict_caption_NPE_barrier_excluding_N10": strict,
            "AFQMC_parallel_overlay": {"source": "paper Table III (rounded), NOT ZIP", "archive_N40": display(energies['data/parallel_afqmc.txt'][40][0]), "paper_HCI_N40": "-21.0"},
            "retrospective_single_anchor_PBE_transfer_kcal_mol": diagnostics,
            "selected_member_sha256": selected,
            "scope": "Archive and arithmetic replay only; not chemistry, force-field validation, runtime, or quantum advantage."}


def main() -> None:
    if sys.flags.optimize:
        raise SystemExit("Run without -O or -OO.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    args = parser.parse_args()
    try:
        invalid = self_tests()
        result = audit(args.archive)
        result["malformed_input_controls_rejected"] = invalid
    except (OSError, ValueError, ArithmeticError, BadZipFile, UnicodeError, KeyError) as error:
        raise SystemExit(f"Audit failed: {error}") from error
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
