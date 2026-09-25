"""Hash validation and temporary, deterministic regeneration; no expected file changes."""
import argparse, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def main():
    if not __debug__:raise SystemExit('Do not disable assertions.')
    p=argparse.ArgumentParser();p.add_argument('--solver',action='store_true');a=p.parse_args()
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for name,sha in manifest['sha256'].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=sha:raise SystemExit('Hash mismatch: '+name)
    expected=json.loads((ROOT/'expected.json').read_text())
    with tempfile.TemporaryDirectory(prefix='qad-sorting-') as temp:
        dst=Path(temp)/'experiment';shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('__pycache__'))
        out=Path(temp)/'checks.json';command=[sys.executable,str(dst/'checks.py'),'--output',str(out)]
        if a.solver:command.append('--solver')
        subprocess.run(command,cwd=dst,check=True,stdout=subprocess.DEVNULL,timeout=90)
        if json.loads(out.read_text())!=expected['optional_solver' if a.solver else 'default']:
            raise SystemExit('Deterministic reproduction mismatch.')
    print('PASS: hashes, 1211 exact prefix comparisons, 152 enumerated completion decisions, known certificates and recovered-control suffix.'
          + (' Native Z3 agrees on all 152 decisions.' if a.solver else ' Native solver not rerun.'))
    print('No independent large UNSAT proof, new sorting routine, strongest-native-solver reproduction, or quantum advantage certified.')

if __name__=='__main__':main()
