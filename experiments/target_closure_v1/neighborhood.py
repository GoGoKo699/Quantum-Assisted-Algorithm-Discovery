#!/usr/bin/env python3
"""Exact screening of a finite, integer-ternary one/two-flip neighborhood.

This is not a complete search of rank-23 algorithms. No global lower bound.
"""
from __future__ import annotations
import argparse
from itertools import product
import json
import hashlib
import sys
from pathlib import Path
from probe import canon, expand_source, require, saturate, synthesize
from vendor.upstream_dependency import basis


def normalize_term(term):
    a,b,c = term
    ca,cb = canon(a),canon(b)
    sa = 1 if ca == a else -1
    sb = 1 if cb == b else -1
    return ca,cb,tuple(sa*sb*x for x in c)


def normalize_scheme(terms):
    return tuple(sorted(normalize_term(tuple(tuple(v) for v in t)) for t in terms))


def neighbors(terms):
    generated = {}
    for f in range(3):
        for i in range(len(terms)):
            a,b,c = (terms[i][(f+j)%3] for j in range(3))
            for j in range(len(terms)):
                if i == j: continue
                aa,d,e = (terms[j][(f+h)%3] for h in range(3))
                if aa == a: sign=1
                elif aa == tuple(-x for x in a): sign=-1
                else: continue
                d = tuple(sign*x for x in d)
                for s in (-1,1):
                    nb = tuple(x+s*y for x,y in zip(b,d))
                    ne = tuple(x-s*y for x,y in zip(e,c))
                    if not any(nb) or not any(ne): continue
                    if any(abs(x)>1 for v in (nb,ne) for x in v): continue
                    ti,tj = [None]*3,[None]*3
                    for h,v in enumerate((a,nb,c)): ti[(f+h)%3]=v
                    for h,v in enumerate((a,d,ne)): tj[(f+h)%3]=v
                    out = list(terms); out[i]=ti; out[j]=tj
                    key = normalize_scheme(out)
                    if key != terms:
                        generated.setdefault(key,{'axis':f,'left':i,'right':j,'direction':s})
    return generated


def verify_tensor(terms):
    # Third factor here has the paper's raw (column,row) coordinate convention.
    for a,b,c in product(range(9),repeat=3):
        expected=int(a%3 == b//3 and c%3 == a//3 and c//3 == b%3)
        actual=sum(t[0][a]*t[1][b]*t[2][c] for t in terms)
        require(actual == expected,'neighbor does not multiply matrices')


def screen(terms):
    info=[]
    for axis in range(3):
        rows=[t[axis] for t in terms]
        targets={canon(v) for v in rows}-set(basis(9))
        require(all(any(v) for v in targets),'zero target unsupported')
        available,_,_=saturate(basis(9),[],targets)
        failure=not targets <= set(available)
        info.append({'directions':len(targets),'floor_impossible':failure,
                     'factor_lower_bound':len(targets)+int(failure)})
    return {'factors':info,'total_lower_bound':sum(x['factor_lower_bound'] for x in info)+14}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--radius',type=int,choices=(1,2),default=2)
    args=parser.parse_args();require(not sys.flags.optimize,'do not use -O or -OO')
    require(not args.output.exists(),'do not overwrite evidence')
    maps,_=expand_source()
    root=normalize_scheme(list(zip(maps['U'],maps['V'],maps['W'])))
    seen={root}; layer={root}; report=[]
    for distance in range(1,args.radius+1):
        next_layer=set()
        for state in sorted(layer):
            next_layer.update(child for child in neighbors(state) if child not in seen)
        states=sorted(next_layer)
        histogram={}
        for terms in states:
            verify_tensor(terms)
            bound=screen(terms)['total_lower_bound']
            histogram[str(bound)]=histogram.get(str(bound),0)+1
        digest=hashlib.sha256(json.dumps(states,separators=(',',':')).encode()).hexdigest()
        report.append({'distance':distance,'states':len(states),'tensor_equations_checked':729*len(states),
                       'lower_bound_histogram':dict(sorted(histogram.items())),
                       'not_excluded_at_54':sum(v for k,v in histogram.items() if int(k)<=54),
                       'canonical_states_sha256':digest})
        seen.update(next_layer);layer=next_layer
    result={'scope':'Fixed oriented integer tensor; one/two legal integer-ternary flips, signs and term permutations canonicalized; not all rank-23 algorithms or basis changes.',
            'root':screen(root),'radius':args.radius,'layers':report,
            'total_nonroot_states':sum(r['states'] for r in report),
            'tensor_equations_checked':sum(r['tensor_equations_checked'] for r in report)}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
