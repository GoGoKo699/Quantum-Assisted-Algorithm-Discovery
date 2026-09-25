"""Deterministic independent checks; optional native SAT comparison.

No timing or timeout observation is used as a hardness certificate.
"""
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, itertools, json, random
from prefix import reachable, materialize, apply_layers, sorted_word, validate_layers
ROOT=Path(__file__).resolve().parent

def matching_layers(wires):
    if not wires:
        yield (); return
    i=wires[0]
    for tail in matching_layers(wires[1:]):yield tail
    for q,j in enumerate(wires[1:],1):
        remaining=wires[1:q]+wires[q+1:]
        for tail in matching_layers(remaining):yield ((i,j),)+tail

def reference(x,n,layers):
    bits=[(x>>i)&1 for i in range(n)]
    for layer in layers:
        for i,j in layer:bits[i],bits[j]=min(bits[i],bits[j]),max(bits[i],bits[j])
    return sum(v<<i for i,v in enumerate(bits))

def brute_outputs(n,layers):
    return sorted({reference(x,n,layers) for x in range(1<<n)})

def tests(use_solver=False):
    if not __debug__:raise RuntimeError('Assertions must be enabled.')
    cases=0;counts={};decisions=[];sat=0;unsat=0
    if use_solver:
        from completion import Solver,Encoding
    for n in (2,3,4):
        matchings=list(matching_layers(tuple(range(n))));cnt=0
        for length in range(4):
            for net in itertools.product(matchings,repeat=length):
                actual=materialize(reachable(n,net)[0]);expect=brute_outputs(n,net)
                assert actual==expect;cnt+=1
        counts[str(n)]=cnt
        for prefix in [()]+[(layer,) for layer in matchings]:
            states=brute_outputs(n,prefix)
            for depth,symmetric,adjacent in itertools.product((1,2),(False,True),(False,True)):
                allowed=[]
                for t in range(depth):
                    options=[]
                    for layer in matchings:
                        if symmetric and set(layer)!={(n-1-j,n-1-i) for i,j in layer}:continue
                        if adjacent and t==depth-1 and any(j!=i+1 for i,j in layer):continue
                        options.append(layer)
                    allowed.append(options)
                answer=any(all(reference(x,n,suffix)==sorted_word(n,x.bit_count()) for x in states)
                           for suffix in itertools.product(*allowed))
                decisions.append(int(answer));cases+=1
                if use_solver:
                    enc=Encoding(n,depth,symmetric,adjacent);solver=Solver(2000)
                    try:
                        solver.add(enc.header)
                        for x in states:solver.add(enc.example(x))
                        out=solver.check()
                        assert out['status']!='unknown',(n,depth,'unexpected small timeout')
                        assert (out['status']=='sat')==answer,(n,prefix,depth,symmetric,adjacent,out)
                        if answer:
                            suffix=enc.decode(out['model']);validate_layers(n,suffix)
                            assert all(reference(x,n,suffix)==sorted_word(n,x.bit_count()) for x in states)
                            sat+=1
                        else:unsat+=1
                    finally:solver.close()
    reports=[]
    for net in json.loads((ROOT/'networks.json').read_text())['networks']:
        n=net['n'];comp,census=reachable(n,net['layers']);outputs=materialize(comp)
        assert outputs==sorted(sorted_word(n,w) for w in range(n+1))
        rng=random.Random(20260925+n)
        for _ in range(1024):
            x=rng.randrange(1<<n);assert reference(x,n,net['layers'])==sorted_word(n,x.bit_count())
        for x in (0,(1<<n)-1):assert reference(x,n,net['layers'])==x
        reports.append(dict(name=net['name'],n=n,comparators=sum(map(len,net['layers'])),
                            layers=len(net['layers']),census=census,random_input_checks=1024))
    witness=json.loads((ROOT/'observations.json').read_text())['runs']['p18_d11_p6']
    assert witness['status']=='verified_sat'
    net=witness['certificate'];validate_layers(18,net)
    states=materialize(reachable(18,net[:6])[0])
    assert all(reference(x,18,net[6:])==sorted_word(18,x.bit_count()) for x in states)
    witness_count=len(states)
    return dict(prefix_networks_by_width=counts,completion_decisions=cases,
        completion_decision_sha256=hashlib.sha256(bytes(decisions)).hexdigest(),
        published_networks=reports,
        recovered_control=dict(n=18,depth=len(net),comparators=sum(map(len,net)),prefix_states_checked=witness_count),
        optional_solver= dict(sat=sat,unsat=unsat) if use_solver else None,
        scope='Known-network/circuit/encoding validation, not a new network or quantum advantage.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--solver',action='store_true');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise SystemExit('Refusing to overwrite evidence.')
    report=tests(a.solver);a.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps(report,indent=2))
