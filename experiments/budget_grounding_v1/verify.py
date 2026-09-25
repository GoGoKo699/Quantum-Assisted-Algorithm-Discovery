"""Reproduce exact reports in temporary storage without changing evidence."""
import hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]

def main():
    if not __debug__:raise SystemExit('Do not use Python -O or -OO.')
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for rel,digest in manifest['sha256'].items():
        if hashlib.sha256((REPO/rel).read_bytes()).hexdigest()!=digest:
            raise SystemExit('Hash mismatch: '+rel)
    with tempfile.TemporaryDirectory(prefix='qad-budget-') as td:
        d=Path(td)
        for name in ('sharing_core_v1','budget_grounding_v1'):
            shutil.copytree(REPO/'experiments'/name,d/'experiments'/name,
                            ignore=shutil.ignore_patterns('__pycache__'))
        here=d/'experiments'/'budget_grounding_v1'
        for script,report in [('checks.py','results.json'),('circuit.py','circuit_results.json')]:
            out=d/report
            subprocess.run([sys.executable,str(here/script),'--output',str(out)],check=True,
                           timeout=180,stdout=subprocess.DEVNULL,cwd=here)
            if out.read_bytes()!=(ROOT/report).read_bytes():
                raise SystemExit('Reproduction mismatch: '+report)
    print('PASS: pinned dependencies, 8374 cap assignments, 2000 threshold decisions, 1790 transferred witnesses, 31823 rank roundtrips, 4174 marker basis states, and clean uncomputation.')
    print('No novelty, best-classical separation, native large-workload result, or useful quantum advantage is certified.')

if __name__=='__main__':main()
