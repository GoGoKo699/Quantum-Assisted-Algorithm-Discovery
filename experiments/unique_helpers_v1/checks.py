"""Independent finite GF(2) checks and exact useful-transform calibrations."""
from __future__ import annotations
import json
from pathlib import Path
from itertools import combinations
from collections import Counter
from unique_search import Model,canonical,verify_certificate

def xor_all():
    n=4; basis={1,2,4,8}; ground=[v for v in range(1,16) if v not in basis]
    D=len(ground); full=(1<<D)-1
    def elements(mask): return {ground[i] for i in range(D) if mask>>i&1}
    def fixed_closure(mask):
        a=set(basis);missing=elements(mask)
        while missing:
            found={v for v in missing if any(v^x in a for x in a)}
            if not found: break
            a |= found; missing -= found
        return sum(1<<i for i,v in enumerate(ground) if v in a)
    reach=[fixed_closure(m) for m in range(1<<D)]
    # Independent unrestricted full-wire-state extension search.
    states={0};front=[0];edges=0
    while front:
        S=front.pop();a=elements(S)|basis
        for v in {x^y for x,y in combinations(a,2)}-a:
            edges+=1;g=S|(1<<ground.index(v))
            if g not in states: states.add(g);front.append(g)
    assert states=={m for m in range(1<<D) if reach[m]==m}
    min_gate=[min(S.bit_count() for S in states if T&S==T) for T in range(1<<D)]
    pairs=0;feasible_count=0;parent_edges=0;opt=Counter();ordered_total=0
    for T in range(1<<D):
        free=full^T;H=free;fam=[]
        while True:
            pairs+=1
            if H&reach[T|H]==H:fam.append(H)
            if not H:break
            H=(H-1)&free
        fs=set(fam);feasible_count+=len(fam)
        paths={0:1};count=0;optimum=None
        for H in sorted(fam,key=lambda h:(h.bit_count(),h)):
            if H:
                removals=[H^(1<<i) for i in reversed(range(D)) if H>>i&1 and (H^(1<<i)) in fs]
                assert removals
                P=removals[0];parent_edges+=1
                h=elements(H^P).pop();a=elements(reach[T|P])|basis
                assert any(h^x in a for x in a)
                paths[H]=sum(paths[p] for p in removals)
            if reach[T|H]&T==T:
                size=H.bit_count();optimum=size if optimum is None else min(optimum,size)
        assert optimum+T.bit_count()==min_gate[T]
        opt[optimum]+=1;ordered_total+=sum(paths.values())
        # Independent constructive helper-set enumeration; all states kept only as a test oracle.
        visited={0};q=[0]
        while q:
            H=q.pop();a=elements(reach[T|H])|basis
            for h in {x^y for x,y in combinations(a,2)}-a-elements(T):
                G=H|(1<<ground.index(h))
                if G not in visited: visited.add(G);q.append(G)
        assert visited==fs
    return dict(target_families=1<<D,disjoint_target_helper_pairs=pairs,
                feasible_helper_states=feasible_count,canonical_parent_edges=parent_edges,
                unrestricted_wire_states=len(states),wire_extension_edges=edges,
                optimum_helper_histogram=dict(sorted(opt.items())),ordered_histories=ordered_total)

def tensor(a,b):
    return [tuple(x*y for x in ar for y in br) for ar in a for br in b]

def workloads():
    B=[(1,0,-1,0),(0,1,1,0),(0,-1,1,0),(0,-1,0,1)]
    # Four independent row transforms, then four column transforms.
    targets=tensor(B,B)
    helpers=frozenset(canonical(tuple((v[j] if i==r else 0) for i in range(4) for j in range(4))) for r in range(4) for v in B)
    m=Model(16,targets);A,gates=m.closure(helpers,True)
    assert helpers<=A and m.targets<=A and len(gates)==32
    verify_certificate(16,m.targets,gates)
    conv=dict(name='Winograd F(2x2,3x3) input transform B^T tensor B^T',
              inputs=16,required_directions=len(m.targets),supplied_helpers=len(helpers),
              verified_gate_count=len(gates),targets=targets,helpers=sorted(helpers),gates=gates,
              status='known separable construction; no minimum or runtime claim')
    T=[(1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)]
    H=frozenset([(1,1,0,0),(1,-1,0,0),(0,0,1,1),(0,0,1,-1)])
    m=Model(4,T);_,g=m.closure(H,True);verify_certificate(4,m.targets,g)
    # A simple sorting restriction would miss this constructible helper set.
    m2=Model(3,[(1,1,-2)]);H2=frozenset([(1,1,0),(1,1,-1)])
    assert m2.feasible(H2)
    assert not m2.feasible(frozenset([min(H2)]))
    assert m2.parent(H2)==frozenset([(1,1,0)])
    m3=Model(4,[(1,1,1,0),(0,1,-1,1)])
    c,S=m3.census(2,'canonical',True);d,U=m3.census(2,'memoized',True)
    assert S==U and c['goals']==d['goals'] and c['witness']['gate_count']==4
    # Independently compare the Python/C++ integer census through three helpers.
    m4=Model(4,T);p,S=m4.census(3,'canonical',True);m5=Model(4,T);q,U=m5.census(3,'memoized',True)
    assert S==U and p['by_depth']=={0:1,1:16,2:236,3:4064} and not p['goals']
    return dict(winograd_input_2d=conv,wht4_certificate={'helpers':sorted(H),'gates':g,'gate_count':len(g)},
                winograd_output_1d={'canonical':c,'memoized':d},
                python_integer_census_through_three={'canonical':p,'memoized':q},
                helper_sorting_counterexample={'targets':[(1,1,-2)],'helpers':sorted(H2),'only_feasible_parent':sorted(m2.parent(H2))})

if __name__=='__main__':
    import sys
    if sys.flags.optimize: raise RuntimeError('run without -O/-OO')
    result={'xor_exhaustive':xor_all(),'workloads':workloads()}
    dest=Path(sys.argv[1]) if len(sys.argv)>1 else None
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if dest: dest.write_text(text)
    else: print(text,end='')
