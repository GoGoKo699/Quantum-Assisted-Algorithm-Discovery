#!/usr/bin/env python3
"""Verify source hashes and exact arithmetic report without overwriting evidence."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def main():
    if not __debug__ or sys.flags.optimize:
        raise SystemExit('Do not use -O or -OO for research verification.')
    here = Path(__file__).resolve().parent
    manifest = json.loads((here / 'MANIFEST.json').read_text())
    for name, digest in manifest['sha256'].items():
        if hashlib.sha256((here / name).read_bytes()).hexdigest() != digest:
            raise SystemExit('Hash mismatch: ' + name)
    with tempfile.TemporaryDirectory(prefix='translation-cost-') as directory:
        temp = Path(directory)
        for name in ('cost.py', 'checks.py'):
            shutil.copyfile(here / name, temp / name)
        result = subprocess.run([sys.executable, str(temp / 'checks.py')],
                                capture_output=True, check=True, timeout=60)
        if result.stdout != (here / 'REPORT.json').read_bytes():
            raise SystemExit('Exact report differs; inspect, do not overwrite.')
    print('Translation cost audit: source hashes and independent arithmetic passed.')
    print('No native point counter, group-law circuit or quantum device was executed.')


if __name__ == '__main__':
    main()
