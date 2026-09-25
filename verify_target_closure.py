#!/usr/bin/env python3
"""Verify the versioned target-closure checkpoint in disposable copies.

Python 3.10+ standard library. Stored result files are never overwritten.
This validates exact classical calculations, not quantum advantage.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
EXPERIMENT = Path("experiments/target_closure_v1")
MANIFEST = ROOT / "provenance/target-closure-manifest.json"


def check_files() -> dict:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if data["schema"] != 1:
        raise RuntimeError("Unsupported manifest schema")
    for name, entry in data["files"].items():
        relative = Path(name)
        path = ROOT / relative
        if relative.is_absolute() or ".." in relative.parts:
            raise RuntimeError(f"Unsafe manifest path: {name}")
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(ROOT):
            raise RuntimeError(f"Missing or unsafe file: {name}")
        raw = path.read_bytes()
        if len(raw) != entry["bytes"] or hashlib.sha256(raw).hexdigest() != entry["sha256"]:
            raise RuntimeError(f"Changed checkpoint file: {name}")
    license_data = (ROOT / "LICENSE").read_bytes()
    blob = hashlib.sha1(f"blob {len(license_data)}\0".encode() + license_data).hexdigest()
    if blob != "e17a781bf47c4aadf18b68fc593846a1193b86c1":
        raise RuntimeError("Root license changed")
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("Do not run under -O or -OO")
    manifest = check_files()
    with tempfile.TemporaryDirectory(prefix="qaad-closure-") as directory:
        work = Path(directory)
        for name in manifest["files"]:
            relative = Path(name)
            if not relative.is_relative_to(EXPERIMENT):
                continue
            destination = work / relative.relative_to(EXPERIMENT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, destination)
        for script, expected, extra in (
            ("probe.py", "results.json", []),
            ("neighborhood.py", "neighborhood_results.json", ["--radius", "2"]),
        ):
            output = work / ("generated_" + expected)
            result = subprocess.run(
                [sys.executable, "-B", str(work / script), "--output", str(output), *extra],
                check=True, capture_output=True, text=True, timeout=180,
            )
            if output.read_bytes() != (work / expected).read_bytes():
                raise RuntimeError(f"Deterministic output mismatch: {expected}")
            print(f"Reproduced {expected} byte-for-byte.", flush=True)
    check_files()
    print("All successor checks passed; stored evidence and MIT license unchanged.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        raise SystemExit(f"Verification failed: {error}") from error
