"""Reproduce exact evidence without changing saved results or earlier checkpoints."""
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]


def normalized(report):
    report=json.loads(json.dumps(report))
    report['branchings']['networkx_checks']=0
    report['branchings']['networkx_disagreements']=[]
    report['library']['networkx_version']=None
    return report


def main():
    if not __debug__:raise SystemExit('Do not use Python -O/-OO.')
    parser=argparse.ArgumentParser();parser.add_argument('--networkx',action='store_true')
    args=parser.parse_args()
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for rel,expected in manifest['sha256'].items():
        if hashlib.sha256((REPO/rel).read_bytes()).hexdigest()!=expected:
            raise SystemExit('Hash mismatch: '+rel)
    with tempfile.TemporaryDirectory(prefix='qad-component-') as d:
        tmp=Path(d)
        for name in ('sharing_core_v1','budget_grounding_v1','price_spectrum_v1','component_branching_v1'):
            shutil.copytree(REPO/'experiments'/name,tmp/'experiments'/name,
                            ignore=shutil.ignore_patterns('__pycache__'))
        output=tmp/'fresh.json'
        command=[sys.executable,str(tmp/'experiments/component_branching_v1/checks.py'),'--output',str(output)]
        if args.networkx:command.append('--networkx')
        subprocess.run(command,check=True,stdout=subprocess.DEVNULL,timeout=180)
        observed=json.loads(output.read_text());expected=json.loads((ROOT/'results.json').read_text())
        if normalized(observed)!=expected:raise SystemExit('Exact regeneration mismatch.')
        if not args.networkx and output.read_bytes()!=(ROOT/'results.json').read_bytes():
            raise SystemExit('Byte-level regeneration mismatch.')
        print('PASS: immutable source hashes; exact SCC admission, active-set optima,')
        print('arborescence enumeration, unary-Steiner equivalence, scale checks and certificates.')
        if args.networkx:
            failures=observed['branchings']['networkx_disagreements']
            count=observed['branchings']['networkx_checks']
            print('NetworkX '+str(observed['library']['networkx_version'])+': '+str(count-len(failures))+'/'+str(count)+' agree.')
            if failures:
                print('WARNING: independent library discrepancies retained; not universal agreement.')
                print(json.dumps(failures,sort_keys=True))
    print('No full native extractor, quantum circuit, novelty or useful quantum advantage is certified.')


if __name__=='__main__':main()
