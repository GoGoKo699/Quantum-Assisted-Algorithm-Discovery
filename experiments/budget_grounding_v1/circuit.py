"""Explicit reversible compute/phase/uncompute marker for binary local caps.

The unitary marks accepted cap vectors. The compact-allocation unranking and
outer amplitude-amplification schedule are NOT counted by this component.
All Boolean gates have fresh targets; the inverse restores every work bit.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import Counter
from itertools import product
from math import inf
from budget import Graph, Node, Grounding

F=-1; T=-2

class BooleanCircuit:
    def __init__(self, inputs):
        self.inputs=inputs;self.gates=[];self.intern={}
    def gate(self, op, a, b=None):
        if op=='not':
            if a<0:return T if a==F else F
            key=(op,a)
        else:
            if a>b:a,b=b,a
            if op=='and':
                if F in (a,b):return F
                if a==T:return b
                if b==T or a==b:return a
            elif op=='or':
                if T in (a,b):return T
                if a==F:return b
                if b==F or a==b:return a
            elif op=='xor':
                if a==b:return F
                if a==F:return b
                if b==F:return a
                if a==T:return self.gate('not',b)
                if b==T:return self.gate('not',a)
            else:raise ValueError(op)
            key=(op,a,b)
        if key not in self.intern:
            self.intern[key]=self.inputs+len(self.gates);self.gates.append(key)
        return self.intern[key]
    def AND(self,a,b):return self.gate('and',a,b)
    def OR(self,a,b):return self.gate('or',a,b)
    def XOR(self,a,b):return self.gate('xor',a,b)
    def NOT(self,a):return self.gate('not',a)
    def all(self,bits):
        out=T
        for x in bits:out=self.AND(out,x)
        return out
    def constant(self,n,w):return tuple(T if (n>>i)&1 else F for i in range(w))
    def mux(self,c,a,b):
        if a==b:return a
        return tuple(self.XOR(y,self.AND(c,self.XOR(x,y))) for x,y in zip(a,b))
    def lt(self,a,b):
        # Build lexicographic comparison from least to most significant bit.
        less=F
        for x,y in zip(a,b):
            less=self.OR(self.AND(self.NOT(x),y),self.AND(self.NOT(self.XOR(x,y)),less))
        return less
    def add(self,a,b):
        carry=F;out=[]
        for x,y in zip(a,b):
            p=self.XOR(x,y);out.append(self.XOR(p,carry))
            carry=self.OR(self.AND(x,y),self.AND(p,carry))
        return tuple(out+[carry])
    def satadd(self,a,b,limit):
        w=len(a);z=self.add(a,b);cut=self.constant(limit,w+1)
        large=self.NOT(self.lt(z,cut))
        return self.mux(large,self.constant(limit,w),z[:w])
    def minimum(self,a,b):return self.mux(self.lt(a,b),a,b)
    @staticmethod
    def val(wires,i):return (i==T) if i<0 else wires[i]
    def simulate(self,bits,output):
        if len(bits)!=self.inputs:raise ValueError('Input width.')
        wires=list(map(bool,bits))+[False]*len(self.gates)
        def apply(k):
            op,*args=self.gates[k];a=self.val(wires,args[0])
            b=self.val(wires,args[1]) if len(args)==2 else False
            value={'and':a and b,'or':a or b,'xor':a != b,'not':not a}[op]
            wires[self.inputs+k]^=value
        for k in range(len(self.gates)):apply(k)
        phase=-1 if self.val(wires,output) else 1
        for k in range(len(self.gates)-1,-1,-1):apply(k)
        if any(wires[self.inputs:]) or wires[:self.inputs]!=list(map(bool,bits)):
            raise AssertionError('Workspace not restored.')
        return phase
    def resources(self):
        n=Counter(g[0] for g in self.gates)
        # AND: Toffoli; OR: 2 CNOT + Toffoli; XOR: 2 CNOT; NOT: CNOT+X.
        return dict(logical_qubits=self.inputs+len(self.gates),cap_input_qubits=self.inputs,
                    clean_work_qubits=len(self.gates),
                    marker_toffoli=2*(n['and']+n['or']),
                    marker_cnot=2*(2*n['or']+2*n['xor']+n['not']),
                    marker_x=2*n['not'],phase_z=1,boolean_gate_counts=dict(sorted(n.items())),
                    exclusions=['allocation unranking','initial Hadamards','outer search and diffusion',
                                'connectivity and physical error correction'])


def compile_marker(g: Graph, total: int):
    if total<0:raise ValueError('Nonnegative threshold.')
    o=Grounding(g);core=o.core;s=len(core.core);w=max(1,(total+1).bit_length())
    c=BooleanCircuit(s*w);caps=[tuple(range(j*w,(j+1)*w)) for j in range(s)]
    zero=c.constant(0,w);unavailable=c.constant(total+1,w)
    charged=zero
    for b in caps:charged=c.satadd(charged,b,total+1)
    valid=c.lt(charged,unavailable)
    built=[F]*s
    for _ in range(s):
        memo={}
        def value(name):
            if name in core.index:
                return c.mux(built[core.index[name]],zero,unavailable)
            if name in memo:return memo[name]
            memo[name]=expand(name)
            return memo[name]
        def expand(name):
            best=unavailable
            for node in core.g.classes[name]:
                cost=c.constant(min(node.cost,total+1),w)
                for child in sorted(set(node.children)):
                    cost=c.satadd(cost,value(child),total+1)
                best=c.minimum(best,cost)
            return best
        prices=[expand(name) for name in core.core]
        built=[c.OR(old,c.NOT(c.lt(cap,price))) for old,cap,price in zip(built,caps,prices)]
    output=c.AND(valid,c.all(built[core.index[r]] for r in core.g.roots))
    return c,output,w,o


def validate_circuits():
    from random import Random
    examples=[('cycle',Graph({'r':(Node('r',0,('A','B')),),
                   'A':(Node('ab',0,('B',)),Node('a0',10)),
                   'B':(Node('ba',0,('A',)),Node('b0',10))},('r',)),10),
       ('private_chain',Graph({'r':(Node('r',1,('p',)),),'p':(Node('p0',2),Node('pq',0,('q',))),
                             'q':(Node('q0',1),)},('r',)),3),
       ('pure_cycle',Graph({'r':(Node('ra',0,('a',)),),'a':(Node('ar',0,('r',)),)},('r',)),2),
       ('zero_root',Graph({'r':(Node('r0',0),)},('r',)),0),
       ('private_alternatives',Graph({'r':(Node('r',0,('v','w')),),
             'v':(Node('v',0,('p',)),),
             'p':(Node('pu',0,('u',)),Node('p0',4)),
             'w':(Node('wu',1,('u',)),Node('w0',3)),
             'u':(Node('u0',2),)},('r',)),4)]
    report=[]
    for name,g,k in examples:
        c,out,w,o=compile_marker(g,k)
        if c.inputs>14:raise AssertionError('Exhaustive marker budget.')
        accepts=0
        for index in range(1<<c.inputs):
            bits=[(index>>i)&1 for i in range(c.inputs)]
            bs=tuple((index>>(j*w))&((1<<w)-1) for j in range(len(o.core.core)))
            expected=sum(bs)<=k and o.close(bs,witness=False)['success']
            got=c.simulate(bits,out)==-1
            if got!=expected:raise AssertionError((name,bs,got,expected))
            accepts+=got
        report.append(dict(name=name,threshold=k,basis_states=1<<c.inputs,accepted=accepts,**c.resources()))
    return report

if __name__=='__main__':
    import argparse,json
    from pathlib import Path
    if not __debug__:raise SystemExit('Do not use -O/-OO.')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():raise SystemExit('Refusing overwrite.')
    r=validate_circuits();args.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2))
