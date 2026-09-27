#!/usr/bin/env python3
"""Pin the audited decoder and regenerate the independent audit in temporary storage."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def main():
    if not __debug__ or sys.flags.optimize:
        raise SystemExit('Do not use -O or -OO for this research verifier.')
    here = Path(__file__).resolve().parent
    manifest = json.loads((here / 'MANIFEST.json').read_text())
    for name, digest in manifest['sha256'].items():
        if hashlib.sha256((here / name).read_bytes()).hexdigest() != digest:
            raise SystemExit('Hash mismatch: ' + name)
    dependency = here.parent / 'all_field_reconstruction_v1' / 'reconstruct.py'
    raw = dependency.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if (hashlib.sha256(raw).hexdigest() != manifest['dependency']['sha256'] or
            blob != manifest['dependency']['git_blob']):
        raise SystemExit('Audited dependency changed')
    with tempfile.TemporaryDirectory(prefix='reconstruction-audit-') as directory:
        root = Path(directory)
        audit = root / 'reconstruction_audit_v1'
        audit.mkdir()
        (root / 'all_field_reconstruction_v1').mkdir()
        for name in ('audit.py', 'CONTROL.json'):
            shutil.copyfile(here / name, audit / name)
        shutil.copyfile(dependency, root / 'all_field_reconstruction_v1' / 'reconstruct.py')
        result = subprocess.run([sys.executable, str(audit / 'audit.py')],
                                capture_output=True, check=True, timeout=120)
        if result.stdout != (here / 'REPORT.json').read_bytes():
            raise SystemExit('Audit report differs; inspect rather than overwriting evidence.')
    print('Reconstruction audit: hashes, irreducibility, all resultants and exact output passed.')
    print('The decoder remains a promised-input routine, not an order-authentication certificate.')


if __name__ == '__main__':
    main()
