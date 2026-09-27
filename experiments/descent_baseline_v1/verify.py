#!/usr/bin/env python3
"""Check retained bytes and reproduce the exact focused report in a fresh copy."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def main() -> None:
    if sys.flags.optimize or not __debug__:
        raise SystemExit('Do not use -O or -OO for research verification.')
    here = Path(__file__).resolve().parent
    manifest = json.loads((here / 'MANIFEST.json').read_text())
    for name, digest in manifest['sha256'].items():
        if hashlib.sha256((here / name).read_bytes()).hexdigest() != digest:
            raise SystemExit('Hash mismatch: ' + name)
    with tempfile.TemporaryDirectory(prefix='descent-baseline-') as directory:
        temp = Path(directory)
        for name in ('descent.py', 'checks.py'):
            shutil.copyfile(here / name, temp / name)
        result = subprocess.run([sys.executable, str(temp / 'checks.py')],
                                capture_output=True, check=True, timeout=60)
        if result.stdout != (here / 'REPORT.json').read_bytes():
            raise SystemExit('Report differs: inspect without overwriting expected data.')
    report = json.loads(result.stdout)
    print('Source-aware descent: hashes and exact focused checks passed.')
    print(json.dumps({k: report[k] for k in ('matched_h_values', 'scalar_product_checks',
          'nonempty_request_subsets', 'malformed_controls')}, sort_keys=True))
    print('No quantum circuit or application-scale comparison was executed.')


if __name__ == '__main__':
    main()
