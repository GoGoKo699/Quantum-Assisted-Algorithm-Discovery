"""Regenerate fixed-protocol empirical-policy results in temporary storage."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def main() -> None:
    if not __debug__:
        raise SystemExit('Do not use Python -O/-OO.')
    manifest = json.loads((ROOT/'MANIFEST.json').read_text())
    for name, digest in manifest['sha256'].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != digest:
            raise SystemExit('Source hash mismatch: '+name)
    with tempfile.TemporaryDirectory(prefix='qad-policy-screen-') as temp:
        result, observation = Path(temp)/'result.json', Path(temp)/'observation.json'
        subprocess.run([sys.executable, str(ROOT/'check.py'), '--output', str(result),
                        '--observations', str(observation)], check=True, timeout=120)
        digest = hashlib.sha256(result.read_bytes()).hexdigest()
        if digest != manifest['expected_result_sha256']:
            raise SystemExit('Deterministic result differs. Check the pinned data/software; do not overwrite evidence.')
    from check import data, predict
    from deploy import decide
    x, _, _, _, _ = data()
    tree = json.loads((ROOT/'policy_d4.json').read_text())
    for row in x:
        label, used = decide(tree, lambda q: int(row[q]))
        if label != predict(tree, row[None, :])[0][0] or len(used) > 4 or len(set(used)) != len(used):
            raise AssertionError('Sensor-only policy replay failed.')
    print('PASS: source hashes, exact full-tree controls, four learned-policy budgets, native CART replay,')
    print('nonadaptive comparators, fixed held-out results, and 1797 sensor-callback replays.')
    print('No quantum advantage, Action-BED reproduction, or population-optimality claim is certified.')


if __name__ == '__main__':
    main()
