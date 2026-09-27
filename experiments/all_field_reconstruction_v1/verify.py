#!/usr/bin/env python3
"""Check immutable source hashes and reproduce the supplied-polynomial report."""
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
    manifest = json.loads((here/'MANIFEST.json').read_text())
    for name, digest in manifest['sha256'].items():
        if hashlib.sha256((here/name).read_bytes()).hexdigest() != digest:
            raise SystemExit('Hash mismatch: '+name)
    with tempfile.TemporaryDirectory(prefix='all-field-reconstruction-') as directory:
        temp = Path(directory)
        for name in ('reconstruct.py','checks.py'):
            shutil.copyfile(here/name,temp/name)
        result = subprocess.run([sys.executable,str(temp/'checks.py')],
                                capture_output=True,check=True,timeout=120)
        if result.stdout != (here/'REPORT.json').read_bytes():
            raise SystemExit('Exact report differs; inspect instead of overwriting.')
    report=json.loads(result.stdout)
    fields=('total_recovered_coefficients','total_recovered_traces',
            'independent_determinant_checks','finite_parameter_checks',
            'logarithm_spot_checks','malformed_controls')
    print('All-field reconstruction: source hashes and exact report passed.')
    print(json.dumps({key:report[key] for key in fields},sort_keys=True))
    print('No group-order acquisition, curve-realizability or quantum run is certified.')


if __name__=='__main__':
    main()
