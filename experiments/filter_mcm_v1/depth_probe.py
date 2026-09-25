"""Exact target-only depth closure and one-helper check for a published MCM bank."""
from pathlib import Path
import json
from shift_closure import options
from mcm_smt import odd

ROOT=Path(__file__).resolve().parent

def layers(targets,helpers,B):
    requested=set(targets)|set(helpers);known={1:0};defs={}
    while True:
        prior=sorted(known);new={}
        for a in prior:
            for b in prior:
                for c,s,t,sign in options(a,b,B):
                    if c in requested and c not in known:
                        candidate=(1+max(known[a],known[b]),a,b,s,t,sign)
                        if c not in new or candidate<new[c]:new[c]=candidate
        if not new:break
        for c,x in new.items():known[c]=x[0];defs[c]=x[1:]
    return known,defs

def makecert(ts,hs,B):
    lv,defs=layers(ts,hs,B);values=[1];rows=[]
    for c in sorted(set(ts)|set(hs),key=lambda x:(lv.get(x,999),x)):
        if c not in defs:raise ValueError('unreachable')
        a,b,s,t,sign=defs[c]
        raw=(a<<s)+sign*b
        rows.append(dict(value=c,left=values.index(a),right=values.index(b),left_shift=s,right_shift=t,sign=sign,output_sign=1 if raw>0 else -1));values.append(c)
    return rows

def validate(rows,targets,B):
    vals=[1];depth=[0]
    for r in rows:
        a,b=vals[r['left']],vals[r['right']]
        n=((a<<r['left_shift'])+r['sign']*b)*r['output_sign']
        if n!=r['value']*(1<<r['right_shift']):raise AssertionError('identity')
        if not(0<r['value']<1<<B and r['value']%2):raise AssertionError('domain')
        vals.append(r['value']);depth.append(1+max(depth[r['left']],depth[r['right']]))
    if not set(targets)<=set(vals):raise AssertionError('outputs')
    return max(depth)

def pipeline(rows,targets,D,word=16):
    # ASAP and ALAP schedules of this fixed witness, not global register optimality.
    vals=[1]+[r['value'] for r in rows];asap=[0]
    for r in rows:asap.append(1+max(asap[r['left']],asap[r['right']]))
    stage=[D]*len(vals);stage[0]=0
    for i in range(len(rows),0,-1):
        r=rows[i-1]
        for p in (r['left'],r['right']):
            if p:stage[p]=min(stage[p],stage[i]-1)
    assert all(stage[i]>=asap[i] for i in range(len(vals)))
    widths=[(c*((1<<word)-1)).bit_length() for c in vals]
    end=[stage[i] for i in range(len(vals))]
    for i in range(1,len(vals)):
        for p in (rows[i-1]['left'],rows[i-1]['right']):end[p]=max(end[p],stage[i]-1)
    for c in [1]+list(targets):end[vals.index(c)]=D
    regs=[max(0,end[i]-max(stage[i],1)+1)*widths[i] for i in range(len(vals))]
    return dict(stages=stage,widths=widths,register_bits=sum(regs),per_node_register_bits=regs,scope='One fully pipelined ALAP witness; positive fundamental outputs plus delayed input. No post-shift/sign restoration cost or mapped area. Not a global register optimum.')

def main(output_path=None):
    case=json.loads((ROOT/'published_coefficients.json').read_text())['cases'][-1]
    ts=sorted({odd(c) for row in case['matrix'] for c in row}-{0,1});B=10
    lv,_=layers(ts,[],B);cert0=makecert(ts,[],B);d0=validate(cert0,ts,B)
    candidates=sorted({x[0] for x in options(1,1,B)}-set(ts)-{1})
    successful=[]
    for h in candidates:
        dl,df=layers(ts,[h],B)
        if set(ts)<=set(dl) and max(dl[t] for t in ts)<=2:successful.append(h)
    h=successful[0];cert1=makecert(ts,[h],B);d1=validate(cert1,ts,B)
    # Independent exhaustive data-level evaluation of both complete multiplier banks.
    counts=[]
    for rows in (cert0,cert1):
        for x in range(1<<16):
            values=[x]
            for r in rows:
                n=((values[r['left']]<<r['left_shift'])+r['sign']*values[r['right']])*r['output_sign']
                assert n%(1<<r['right_shift'])==0
                values.append(n>>r['right_shift'])
                assert values[-1]==r['value']*x
        counts.append(1<<16)
    result=dict(targets=ts,B=B,target_only_depths=lv,target_only_certificate=cert0,
        one_helper_candidates=candidates,successful_depth_two_helpers=successful,chosen_helper=h,
        one_helper_certificate=cert1,counts=[len(cert0),len(cert1)],depths=[d0,d1],
        scalar_inputs_exhaustively_checked=counts,
        pipeline=[pipeline(cert0,ts,d0),pipeline(cert1,ts,d1)],
        claim='Bounded-model Pareto witnesses (12,3) and (13,2); no novelty or hardware-speedup claim.')
    Path(output_path or ROOT/'depth_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ['targets','counts','depths','chosen_helper','successful_depth_two_helpers','pipeline']},indent=2))
if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True,help='A new JSON output path; do not overwrite evidence.')
    args=parser.parse_args()
    if Path(args.output).exists():raise SystemExit('Output path already exists.')
    if not __debug__:raise SystemExit('Do not use Python -O or -OO.')
    main(args.output)
