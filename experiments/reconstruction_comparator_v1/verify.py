#!/usr/bin/env python3
"""Verify immutable local/dependency bytes and regenerate the exact audit report."""
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
    dep = here.parent / 'translation_cost_v1' / 'cost.py'
    raw = dep.read_bytes()
    spec = manifest['dependency']
    if hashlib.sha256(raw).hexdigest() != spec['sha256']:
        raise SystemExit('Changed inherited arithmetic dependency')
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if blob != spec['git_blob']:
        raise SystemExit('Dependency Git blob differs')
    with tempfile.TemporaryDirectory(prefix='matched-reconstruction-') as directory:
        base = Path(directory)
        target = base / 'reconstruction_comparator_v1'
        target.mkdir()
        for name in ('transcripts.py', 'checks.py'):
            shutil.copyfile(here / name, target / name)
        (base / 'translation_cost_v1').mkdir()
        shutil.copyfile(dep, base / 'translation_cost_v1' / 'cost.py')
        result = subprocess.run([sys.executable, str(target / 'checks.py')],
                                capture_output=True, check=True, timeout=60)
        if result.stdout != (here / 'REPORT.json').read_bytes():
            raise SystemExit('Report differs: inspect rather than overwrite evidence.')
    report = json.loads(result.stdout)
    print('Matched reconstruction: source hashes, dependency and exact report passed.')
    print(json.dumps({k: report[k] for k in ('transcript_roundtrips',
          'supplied_polynomial_reconstructions_each_route',
          'independent_determinant_checks', 'homogeneous_cost_checks',
          'malformed_controls')}, sort_keys=True))
    print('No new curve, quantum circuit or native benchmark was executed.')


if __name__ == '__main__':
    main()
