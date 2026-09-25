"""Independent incremental SAT encoding of fixed-prefix sorting completion.

Runs the native Z3 backend, not the published MiniSat-based synthesizer.
A query may additionally restrict reflection symmetry and the final layer.
"""
from __future__ import annotations
import json,re,time
from pathlib import Path
from itertools import combinations
from prefix import reachable,materialize,apply_layers,sorted_word
import smt_native as z

class Solver:
    def __init__(self,timeout_ms:int):
        cfg=z.mk_config();self.ctx=z.mk_context(cfg);z.del_config(cfg)
        self.s=z.mk_solver(self.ctx);z.inc_solver(self.ctx,self.s)
        prm=z.mk_params(self.ctx);z.inc_params(self.ctx,prm)
        z.set_uint(self.ctx,prm,z.mk_symbol(self.ctx,b'timeout'),timeout_ms)
        z.set_uint(self.ctx,prm,z.mk_symbol(self.ctx,b'random_seed'),0)
        z.set_params(self.ctx,self.s,prm);z.dec_params(self.ctx,prm)
    def add(self,text):z.from_string(self.ctx,self.s,text.encode())
    def check(self):
        r=z.check(self.ctx,self.s)
        ans={'status':{1:'sat',0:'unknown',-1:'unsat'}[r]}
        if r==1:ans['model']=z.model_string(self.ctx,z.get_model(self.ctx,self.s)).decode()
        if r==0:ans['reason']=z.get_reason(self.ctx,self.s).decode()
        return ans
    def close(self):
        if self.ctx:z.dec_solver(self.ctx,self.s);z.del_context(self.ctx);self.ctx=None

class Encoding:
    def __init__(self,n:int,depth:int,symmetric:bool=True,last_adjacent:bool=True):
        self.n=n;self.depth=depth;self.count=0;self.bytes=0
        self.pairs={t:[(i,j) for i in range(n) for j in range(i+1,n)
             if not (last_adjacent and t==depth-1 and j!=i+1)] for t in range(depth)}
        lines=[]
        for t,pairs in self.pairs.items():
            for i,j in pairs:lines.append(f'(declare-const c_{t}_{i}_{j} Bool)')
            for i in range(n):
                incident=[self.c(t,a,b) for a,b in pairs if i in (a,b)]
                for a,b in combinations(incident,2):lines.append(f'(assert (or (not {a}) (not {b})))')
            if symmetric:
                for i,j in pairs:
                    p=(n-1-j,n-1-i)
                    if (i,j)<p:lines.append(f'(assert (= {self.c(t,i,j)} {self.c(t,*p)}))')
        self.header='\n'.join(lines)+'\n';self.bytes=len(self.header)
    @staticmethod
    def c(t,i,j):return f'c_{t}_{min(i,j)}_{max(i,j)}'
    def example(self,x):
        """Each example describes a Boolean vector reachable after the prefix."""
        k=self.count;self.count+=1;lines=[]
        state=['true' if x>>i&1 else 'false' for i in range(self.n)]
        for t,pairs in self.pairs.items():
            nxt=[]
            for i in range(self.n):
                expr=state[i]
                for a,b in pairs:
                    if i==a:expr=f'(ite {self.c(t,a,b)} (and {state[a]} {state[b]}) {expr})'
                    elif i==b:expr=f'(ite {self.c(t,a,b)} (or {state[a]} {state[b]}) {expr})'
                name=f'v_{k}_{t}_{i}';lines.append(f'(declare-const {name} Bool)')
                lines.append(f'(assert (= {name} {expr}))');nxt.append(name)
            state=nxt
        y=sorted_word(self.n,x.bit_count())
        for i,s in enumerate(state):lines.append(f'(assert {s if y>>i&1 else "(not "+s+")"})')
        text='\n'.join(lines)+'\n';self.bytes+=len(text);return text
    def decode(self,model):
        chosen=set(re.findall(r'(?m)^c_(\d+)_(\d+)_(\d+) -> true$',model))
        return [[[i,j] for i,j in self.pairs[t] if (str(t),str(i),str(j)) in chosen] for t in range(self.depth)]

def run(nw:dict,prefix_depth:int,target_depth:int,timeout_ms:int=4000,
        max_rounds:int=20,batch:int=16,all_patterns:bool=False,
        symmetric:bool=True,last_adjacent:bool=True):
    n=nw['n']
    if not (0 <= prefix_depth < target_depth and prefix_depth <= len(nw['layers'])):
        raise ValueError('Require an existing prefix and a positive suffix depth.')
    if timeout_ms < 1 or max_rounds < 1 or batch < 1:
        raise ValueError('Positive timeout, round budget and batch required.')
    prefix=nw['layers'][:prefix_depth]
    comp,census=reachable(n,prefix);patterns=materialize(comp)
    unsorted=[x for x in patterns if x!=sorted_word(n,x.bit_count())]
    enc=Encoding(n,target_depth-prefix_depth,symmetric,last_adjacent);s=Solver(timeout_ms)
    started=time.perf_counter();s.add(enc.header);used=set();trace=[]
    try:
        initial=unsorted if all_patterns else [unsorted[i] for i in range(0,len(unsorted),max(1,len(unsorted)//batch))][:batch]
        for x in initial:s.add(enc.example(x));used.add(x)
        result=None
        for iteration in range(max_rounds):
            t=time.perf_counter();ans=s.check();solve_sec=time.perf_counter()-t
            record={'round':iteration,'examples':len(used),'status':ans['status'],'solve_seconds':solve_sec}
            if ans['status']!='sat':
                if 'reason' in ans:record['reason']=ans['reason']
                trace.append(record);result=ans['status'];break
            layers=enc.decode(ans['model']);t=time.perf_counter()
            failures=[x for x in unsorted if apply_layers(x,layers)!=sorted_word(n,x.bit_count())]
            record['verification_seconds']=time.perf_counter()-t;record['failures']=len(failures)
            trace.append(record)
            if not failures:result='verified_sat';break
            if any(x in used for x in failures):raise AssertionError('SAT model violates encoded test.')
            for x in failures[:batch]:s.add(enc.example(x));used.add(x)
        if result is None:result='round_budget'
        return dict(network=nw['name'],n=n,prefix_depth=prefix_depth,target_depth=target_depth,
            restrictions={'reflection_symmetric_suffix':symmetric,'adjacent_last_layer':last_adjacent},
            all_patterns=all_patterns,prefix_output_count=len(patterns),unsorted_count=len(unsorted),
            solver_version=z.version().decode(),timeout_ms_per_call=timeout_ms,max_rounds=max_rounds,
            status=result,trace=trace,formula_bytes=enc.bytes,elapsed_seconds=time.perf_counter()-started,
            certificate=prefix+layers if result=='verified_sat' else None,encoded_examples=sorted(used),
            classification='Independent encoding and native backend; not upstream synthesis reproduction; UNKNOWN is not UNSAT.')
    finally:s.close()

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=18);p.add_argument('--prefix',type=int,default=6)
    p.add_argument('--depth',type=int,default=10);p.add_argument('--timeout-ms',type=int,default=4000)
    p.add_argument('--rounds',type=int,default=20);p.add_argument('--all-patterns',action='store_true')
    p.add_argument('--no-symmetry',action='store_true');p.add_argument('--unrestricted-last',action='store_true')
    p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if not __debug__:raise SystemExit('Do not disable assertions.')
    if a.output.exists():raise SystemExit('Refusing to overwrite evidence.')
    networks=json.loads((Path(__file__).with_name('networks.json')).read_text())['networks']
    nw=next(x for x in networks if x['n']==a.n)
    out=run(nw,a.prefix,a.depth,a.timeout_ms,a.rounds,all_patterns=a.all_patterns,
            symmetric=not a.no_symmetry,last_adjacent=not a.unrestricted_last)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='certificate'},indent=2))
