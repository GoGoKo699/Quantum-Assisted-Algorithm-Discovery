"""Rerun the independent native-Z3 screen; timings/models are observations, not fixtures."""
import argparse,json
from pathlib import Path
from mcm_smt import odd,instance,certificate
from smt_native import solve
ROOT=Path(__file__).resolve().parent

def main(output,timeout_ms):
    if output.exists():raise SystemExit('Refusing to overwrite observations.')
    out=[]
    for case in json.loads((ROOT/'published_coefficients.json').read_text())['cases']:
        ts=sorted({x for row in case['matrix'] for x in row})
        B=max(abs(c).bit_length() for c in ts)+1
        d=len({odd(c) for c in ts}-{0,1})
        for k in range(d,d+3):
            result=solve(instance(ts,k,B),timeout_ms)
            result.update(name=case['name'],targets=ts,k=k,B=B)
            if result['status']=='sat':
                result['certificate']=certificate(result['model'],k,ts,B)
            result.pop('model',None)
            out.append(result)
            output.write_text(json.dumps(out,indent=2)+'\n')
            print(case['name'],k,result['status'],result['seconds'],flush=True)
            if result['status']=='sat':break
    return out

if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not use -O/-OO.')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    p.add_argument('--timeout-ms',type=int,default=4000);a=p.parse_args()
    main(a.output,a.timeout_ms)
