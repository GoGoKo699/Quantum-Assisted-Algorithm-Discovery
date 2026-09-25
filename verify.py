#!/usr/bin/env python3
"""Check immutable imports and run validations in disposable copies.

Python 3.10+ stdlib; --quick/--full additionally require g++ with C++17.
No results are overwritten. A passed check is not evidence of advantage.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent

def check_imports() -> int:
    manifest = json.loads((ROOT / "provenance/import-manifest.json").read_text())
    files = manifest["files"]
    if len(files) != 18:
        raise RuntimeError("Expected the 18 bootstrap imports")
    for name, entry in files.items():
        path = ROOT / name
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(ROOT):
            raise RuntimeError(f"Unsafe or missing import: {name}")
        data = path.read_bytes()
        if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise RuntimeError(f"Import mismatch: {name}")
    return len(files)

def run(cmd: list[str], timeout: int = 180) -> None:
    subprocess.run(cmd, check=True, timeout=timeout)

def main() -> None:
    if sys.flags.optimize:
        raise SystemExit("Do not run verification under -O or -OO")
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--quick", action="store_true")
    group.add_argument("--full", action="store_true")
    args = parser.parse_args()
    count = check_imports()
    print(f"Verified {count} byte-identical active imports.", flush=True)
    with tempfile.TemporaryDirectory(prefix="qaad-verify-") as temp:
        work = Path(temp) / "guided_search"
        shutil.copytree(ROOT / "experiments/guided_search", work,
                        ignore=shutil.ignore_patterns("__pycache__"))
        before = {n: (work / n).read_bytes() for n in ("reference23.json", "reference23.txt")}
        run([sys.executable, str(work / "make_reference.py")])
        for n, data in before.items():
            if (work / n).read_bytes() != data:
                raise RuntimeError(f"Reference regeneration mismatch: {n}")
        if args.quick or args.full:
            run([sys.executable, str(work / "reproduce.py"),
                 "--full" if args.full else "--quick"], timeout=2400)
        else:
            run([sys.executable, str(work / "guided_core.py"), "--check"])
    check_imports()
    print("Verification passed; stored imports unchanged. No advantage claim.")

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as exc:
        raise SystemExit(f"Verification failed: {exc}") from exc
