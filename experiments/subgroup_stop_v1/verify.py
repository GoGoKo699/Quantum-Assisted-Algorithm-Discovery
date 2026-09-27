#!/usr/bin/env python3
"""Check hashes and reproduce this successor's exact report in a temporary copy."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def main():
    if not __debug__ or sys.flags.optimize:
        raise SystemExit('Do not run research verification with -O or -OO.')
    here = Path(__file__).resolve().parent
    manifest = json.loads((here / 'MANIFEST.json').read_text())
    for name, digest in manifest['sha256'].items():
        if hashlib.sha256((here / name).read_bytes()).hexdigest() != digest:
            raise SystemExit('Hash mismatch: ' + name)
    with tempfile.TemporaryDirectory(prefix='subgroup-stop-') as directory:
        temp = Path(directory)
        for name in ('subgroup.py', 'checks.py'):
            shutil.copyfile(here / name, temp / name)
        result = subprocess.run([sys.executable, str(temp / 'checks.py')],
                                capture_output=True, check=True, timeout=60)
        if result.stdout != (here / 'REPORT.json').read_bytes():
            raise SystemExit('Deterministic report differs; inspect, do not overwrite.')
    report = json.loads(result.stdout)
    print('Subgroup stopping: hashes and exact independent report passed.')
    print(json.dumps(report['census'], sort_keys=True))


if __name__ == '__main__':
    main()
