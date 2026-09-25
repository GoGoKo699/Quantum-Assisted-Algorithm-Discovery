"""Check immutable inputs and regenerate exact results in a disposable directory."""
import argparse,hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def main():
    if not __debug__:raise SystemExit('Do not use Python -O or -OO.')
    p=argparse.ArgumentParser();p.add_argument('--solver',action='store_true');args=p.parse_args()
    expected=json.loads((ROOT/'expected_reports.json').read_text())
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for name,sha in manifest['sha256'].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=sha:
            raise SystemExit('Hash mismatch: '+name)
    with tempfile.TemporaryDirectory(prefix='qad-filter-verify-') as temp:
        d=Path(temp)/'experiment';shutil.copytree(ROOT,d,ignore=shutil.ignore_patterns('__pycache__'))
        generated=Path(temp)/'generated';generated.mkdir()
        def run(script,out,extra=()):
            subprocess.run([sys.executable,str(d/script),'--output',str(generated/out),*extra],check=True,cwd=d,
                           stdout=subprocess.DEVNULL,timeout=120)
            sha=hashlib.sha256((generated/out).read_bytes()).hexdigest()
            target=expected.get(out,hashlib.sha256((ROOT/out).read_bytes()).hexdigest() if (ROOT/out).exists() else None)
            if sha!=target:raise AssertionError('Reproduction mismatch: '+out)
        run('checks.py','checks_results.json')
        run('depth_probe.py','depth_results.json')
        if args.solver:run('checks.py','solver_validation.json',('--solver',))
    print('PASS: hashes, all stored SAT certificates, independent small enumeration, depth obstruction, and both full 16-bit bank evaluations.'
          + (' Native Z3 agrees on all 384 small decisions.' if args.solver else ' Native solver rerun not requested.'))
    print('No newest-solver reproduction, mapped hardware result, or quantum advantage is certified.')

if __name__=='__main__':main()
