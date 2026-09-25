"""Reproduce this versioned experiment without overwriting stored evidence."""
from __future__ import annotations
import hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FILES=('unique_search.py','checks.py','wht_census.cpp','verify.py','README.md','results.json')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check_manifest():
    m=json.loads((ROOT/'MANIFEST.json').read_text())
    if set(m)!=set(FILES):raise RuntimeError('unexpected manifest members')
    for n in FILES:
        p=ROOT/n
        if p.is_symlink() or not p.is_file() or digest(p)!=m[n]:raise RuntimeError('source mismatch: '+n)
def main():
    if sys.flags.optimize:raise RuntimeError('Do not use -O or -OO')
    check_manifest();expected=json.loads((ROOT/'results.json').read_text())
    with tempfile.TemporaryDirectory(prefix='qaad-unique-') as td:
        p=Path(td)
        for n in FILES:shutil.copyfile(ROOT/n,p/n)
        subprocess.run([sys.executable,str(p/'checks.py'),str(p/'checks.json')],check=True,timeout=180)
        checks=json.loads((p/'checks.json').read_text())
        subprocess.run(['g++','-O2','-std=c++17','-Wall','-Wextra','-pedantic',str(p/'wht_census.cpp'),'-o',str(p/'census')],check=True,timeout=90)
        cpp={}
        for name,mode,flag in [('wht_canonical.json','canonical','audit'),('wht_memoized.json','memoized','audit'),('wht_no_cache.json','canonical','no-audit')]:
            run=subprocess.run([str(p/'census'),'4',mode,flag],check=True,capture_output=True,text=True,timeout=180)
            cpp[name]=json.loads(run.stdout)
        result={'checks_sha256':digest(p/'checks.json'),'xor_exhaustive':checks['xor_exhaustive'],
                'winograd_input_transform':{k:checks['workloads']['winograd_input_2d'][k] for k in ('inputs','required_directions','supplied_helpers','verified_gate_count','status')},'cpp':cpp}
        if result!=expected:raise RuntimeError('deterministic results differ')
    check_manifest()
    print('PASS: full exact certificates/hash, exhaustive GF(2), independent integer tests, both censuses, and actual no-cache traversal. No quantum-advantage claim.')
if __name__=='__main__':
    try:main()
    except (OSError,ValueError,KeyError,RuntimeError,subprocess.SubprocessError) as exc:raise SystemExit('Verification failed: '+str(exc))
