"""Regenerate new deterministic reports without modifying stored evidence."""
import hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]


def main():
    if not __debug__:
        raise SystemExit('Do not use Python -O/-OO.')
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for rel,sha in manifest['sha256'].items():
        path=REPO/rel
        if hashlib.sha256(path.read_bytes()).hexdigest()!=sha:
            raise SystemExit('Hash mismatch: '+rel)
    with tempfile.TemporaryDirectory(prefix='qad-price-check-') as d:
        temp=Path(d)
        for name in ('sharing_core_v1','budget_grounding_v1','price_spectrum_v1'):
            shutil.copytree(REPO/'experiments'/name,temp/'experiments'/name,
                            ignore=shutil.ignore_patterns('__pycache__'))
        for script,result in [('checks.py','results.json'),('indexed_circuit.py','circuit_results.json')]:
            target=temp/result
            subprocess.run([sys.executable,str(temp/'experiments/price_spectrum_v1'/script),
                            '--output',str(target)],check=True,stdout=subprocess.DEVNULL,timeout=120)
            if hashlib.sha256(target.read_bytes()).hexdigest()!=manifest['expected_reports'][result]:
                raise SystemExit('Deterministic mismatch: '+result)
    print('PASS: pinned dependencies, 400 graphs, exact budget snapping, mandatory grounding,')
    print('scale invariance, compilation limits, mixed-radix circuits and clean uncomputation.')
    print('No novelty, native large-workload, or useful quantum advantage is certified.')


if __name__=='__main__':main()
