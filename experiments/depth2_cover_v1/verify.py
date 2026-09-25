"""Verify sources and regenerate complete deterministic reports in a temporary copy."""
import hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    if not __debug__:raise SystemExit('Do not use Python -O/-OO.')
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for name,wanted in manifest['sha256'].items():
        if digest(ROOT/name)!=wanted:raise SystemExit('Source hash mismatch: '+name)
    expected=json.loads((ROOT/'expected.json').read_text())
    with tempfile.TemporaryDirectory(prefix='qad-depth-screen-') as temp:
        copy=Path(temp)/'experiment';shutil.copytree(ROOT,copy,ignore=shutil.ignore_patterns('__pycache__'))
        for script,key in [('checks.py','checks_sha256'),('run_screen.py','screen_sha256')]:
            output=Path(temp)/(script+'.json')
            subprocess.run([sys.executable,str(copy/script),'--output',str(output)],cwd=copy,
                           stdout=subprocess.DEVNULL,check=True,timeout=90)
            if digest(output)!=expected[key]:raise SystemExit('Reproduction mismatch: '+script)
    print('PASS: source hashes, all eleven bounded-model Pareto fronts, 1536 independent tiny decisions,')
    print('972 portfolio subsets, 15 integer circuit certificates and 5760 signed data-level runs.')
    print('No upstream native solver, mapped hardware result, or quantum advantage is certified.')
if __name__=='__main__':main()
