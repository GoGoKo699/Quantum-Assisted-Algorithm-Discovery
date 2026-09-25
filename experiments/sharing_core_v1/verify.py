"""Verify pinned evidence and regenerate in temporary storage; never overwrite results."""
import hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def main():
    if not __debug__:raise SystemExit('Do not use Python -O/-OO.')
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for name, sha in manifest['sha256'].items():
        p=ROOT/name
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha:
            raise SystemExit('Hash mismatch: '+name)
    with tempfile.TemporaryDirectory(prefix='qaad-sharing-core-') as td:
        tmp=Path(td);source=tmp/'source';output=tmp/'generated'
        shutil.copytree(ROOT,source,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        env=os.environ.copy();env['PYTHONHASHSEED']='0'
        subprocess.run([sys.executable,str(source/'checks.py'),'--output-dir',str(output)],
                       check=True,timeout=120,stdout=subprocess.DEVNULL,env=env)
        if (output/'results.json').read_bytes()!=(ROOT/'results.json').read_bytes():
            raise SystemExit('Deterministic report differs.')
    print('PASS: source hashes; 2100 seeded structural graphs vs exhaustive choices; acyclic activation and cyclic counterexample; pinned public graph and upstream greedy-core calibration.')
    print('No novelty, full native optimization benchmark, quantum circuit execution, or useful quantum advantage certified.')
if __name__=='__main__':main()
