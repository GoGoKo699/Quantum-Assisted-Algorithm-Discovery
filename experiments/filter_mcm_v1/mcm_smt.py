"""Independent bounded exact MCM encoding; not the upstream SAT-MCM solver."""
import json,re,sys
from pathlib import Path

def odd(c):
    c=abs(c)
    if c==0:return 0
    return c//(c&-c)

def instance(targets,k,B):
    if k < 0 or B < 1:
        raise ValueError('Nonnegative node budget and positive coefficient width required.')
    if any(odd(t) >= (1 << B) for t in targets):
        raise ValueError('A target is outside the declared coefficient bound.')
    ts=sorted({odd(t) for t in targets}-{0,1}); W=2*B+2
    num=lambda x:f'(_ bv{x} {W})'
    out=['(set-logic QF_BV)',f'(define-fun v0 () (_ BitVec {W}) {num(1)})']
    def dec(name):out.append(f'(declare-const {name} (_ BitVec {W}))')
    def ass(exp):out.append(f'(assert {exp})')
    for i in range(1,k+1):
        for x in ('v','l','r','s','t'):dec(x+str(i))
        out.append(f'(declare-const sub{i} Bool)')
        for x in ('l','r'):ass(f'(bvult {x}{i} {num(i)})')
        for x in ('s','t'):ass(f'(bvule {x}{i} {num(B)})')
        ass(f'(and (bvuge v{i} {num(1)}) (bvult v{i} {num(1<<B)}) (= (bvand v{i} {num(1)}) {num(1)}))')
        def sel(x):
            a='v0'
            for j in range(1,i):a=f'(ite (= {x}{i} {num(j)}) v{j} {a})'
            return a
        out.append(f'(define-fun a{i} () (_ BitVec {W}) (bvshl {sel("l")} s{i}))')
        out.append(f'(define-fun b{i} () (_ BitVec {W}) {sel("r")})')
        ass(f'(= (bvshl v{i} t{i}) (ite sub{i} (ite (bvuge a{i} b{i}) (bvsub a{i} b{i}) (bvsub b{i} a{i})) (bvadd a{i} b{i})))')
    for t in ts:ass('(or '+' '.join(f'(= v{i} {num(t)})' for i in range(k+1))+')')
    return '\n'.join(out)+'\n'

def parse_model(text):
    return {m[0]: (int(m[1][2:],16) if m[1].startswith('#x') else int(m[1][2:],2) if m[1].startswith('#b') else m[1]=='true') for m in re.findall(r'(?m)^([vlrst]\d+|sub\d+) -> (#x[\da-f]+|#b[01]+|true|false)$',text)}

def certificate(model,k,targets,B):
    m=parse_model(model); vals=[1]; rows=[]
    for i in range(1,k+1):
        l,r,s,t,v=[m[x+str(i)] for x in ('l','r','s','t','v')]; sign=-1 if m['sub'+str(i)] else 1
        assert 0<=l<i and 0<=r<i and 0<=s<=B and 0<=t<=B
        raw=(vals[l]<<s)+sign*vals[r]
        assert abs(raw)==v*(1<<t) and v>0 and v<1<<B and v%2
        rows.append({'value':v,'left':l,'right':r,'left_shift':s,'right_shift':t,'sign':sign,'output_sign':1 if raw>0 else -1});vals.append(v)
    assert {odd(c) for c in targets}-{0,1}<=set(vals)
    return rows

