"""QRAM-free indexed price-spectrum marker and one Grover-iteration counts.

Logical all-to-all X/CNOT/Toffoli/H/Z basis. Constant-folded Boolean DAGs use
fresh clean targets. Compilation and classical preprocessing costs are separate.
No physical resources or quantum-over-classical speedup are measured.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from spectrum import PriceSpectrum, Graph, Node
from circuit import BooleanCircuit, F, T


def div_constant(c, bits, divisor):
    """Binary long division by a positive classical constant, least-bit-first."""
    if divisor < 1:
        raise ValueError('Positive divisor required.')
    if divisor == 1:
        return tuple(bits), (F,)
    width = divisor.bit_length()+1
    remainder = c.constant(0,width)
    quotient = [F]*len(bits)
    for j in range(len(bits)-1,-1,-1):
        doubled = (bits[j],)+remainder[:-1]
        ge = c.NOT(c.lt(doubled,c.constant(divisor,width)))
        difference = c.add(doubled,c.constant((1<<width)-divisor,width))[:width]
        remainder = c.mux(ge,difference,doubled)
        quotient[j] = ge
    return tuple(quotient),remainder


def decode_circuit(c, spectra, cost_width):
    index = tuple(range(c.inputs))
    quotient = index
    caps = [None]*len(spectra.alphabets)
    for j in range(len(caps)-1,-1,-1):
        table=spectra.alphabets[j]
        quotient,digit=div_constant(c,quotient,len(table))
        value=c.constant(0,cost_width)
        for k,price in enumerate(table):
            eq=c.all(c.NOT(c.XOR(x,y)) for x,y in zip(digit,c.constant(k,len(digit))))
            value=c.mux(eq,c.constant(price,cost_width),value)
        caps[j]=value
    valid=c.lt(index+(F,),c.constant(spectra.cartesian_size,c.inputs+1))
    return caps,valid


def compile_indexed(spectra):
    if spectra.cartesian_size<2:
        raise ValueError('A zero/one-label domain should be resolved classically.')
    g=spectra.core.g; core=spectra.core; total=spectra.K
    s=len(core.core);w=max(1,(total+1).bit_length())
    c=BooleanCircuit((spectra.cartesian_size-1).bit_length())
    caps,valid=decode_circuit(c,spectra,w)
    decoder_gates=len(c.gates)
    zero=c.constant(0,w);unavailable=c.constant(total+1,w)
    charged=zero
    for b in caps:charged=c.satadd(charged,b,total+1)
    valid=c.AND(valid,c.lt(charged,unavailable))
    built=[F]*s
    for _ in range(s):
        memo={}
        def value(name):
            if name in core.index:
                return c.mux(built[core.index[name]],zero,unavailable)
            if name not in memo:memo[name]=expand(name)
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
    resources=c.resources()
    resources['index_input_qubits']=resources.pop('cap_input_qubits')
    resources['decoder_boolean_gates']=decoder_gates
    resources['phase_z']=int(output>=0)
    q=c.inputs
    diffusion_toffoli=max(0,2*q-5) if q>=3 else 0
    diffusion_scratch=max(0,q-3)
    resources.update(grover_iteration_toffoli=resources['marker_toffoli']+diffusion_toffoli,
        grover_iteration_qubits=q+max(len(c.gates),diffusion_scratch),
        diffusion_toffoli=diffusion_toffoli,
        diffusion_clifford=dict(X=2*q,H=2*q+(2 if q>=3 else 0),
                                Z=int(q==1),CZ=int(q==2)),
        initial_hadamards=q,
        exclusions=['number of search iterations / unknown-success scheduling',
                    'classical spectrum preprocessing','connectivity and physical fault tolerance'])
    return c,output,resources


def evaluate_boolean(c,bits,outputs):
    values=list(map(bool,bits))
    for op,*args in c.gates:
        x=c.val(values,args[0]);y=c.val(values,args[1]) if len(args)==2 else False
        values.append({'and':x and y,'or':x or y,'xor':x!=y,'not':not x}[op])
    return [sum(int(c.val(values,wire))<<j for j,wire in enumerate(bus)) for bus in outputs]


def run():
    division=0
    for width in range(1,8):
        for divisor in range(1,11):
            c=BooleanCircuit(width)
            q,r=div_constant(c,tuple(range(width)),divisor)
            for x in range(1<<width):
                got=evaluate_boolean(c,[(x>>j)&1 for j in range(width)],[q,r])
                if tuple(got)!=divmod(x,divisor):raise AssertionError('Division mismatch.')
                division+=1
    from public_graph import load_graph,remove_direct_self_dependencies
    cases=[('public_calibration',remove_direct_self_dependencies(load_graph()),1205),
      ('positive_cycle',Graph({'r':(Node('r',0,('A','B')),),
       'A':(Node('ab',1,('B',)),Node('al',10)),
       'B':(Node('ba',1,('A',)),Node('bl',10))},('r',)),11),
      ('three_price',Graph({'r':(Node('rp',0,('p','z')),),
       'p':(Node('p0',2),Node('pa',1,('a',)),Node('pb',0,('b',))),
       'z':(Node('za',0,('a',)),Node('zb',0,('b',)),Node('z0',3)),
       'a':(Node('a',1),),'b':(Node('b',2),)},('r',)),4)]
    records=[]
    for name,g,k in cases:
        obj=PriceSpectrum(g,k,propagate=True)
        c,out,res=compile_indexed(obj)
        good=[]
        for rank in range(1<<c.inputs):
            if rank<obj.cartesian_size:
                bs=obj.decode(rank)
                expected=sum(bs)<=k and obj.grounding.close(bs,witness=False)['success']
            else:expected=False
            bits=[(rank>>i)&1 for i in range(c.inputs)]
            phase=c.simulate(bits,out)
            if (phase==-1)!=expected:raise AssertionError('Indexed marker mismatch.')
            if expected:good.append(rank)
        # Reduced index-space amplitude simulation. Marker workspace is clean
        # for every basis state above, so linearity justifies this restriction.
        dim=1<<c.inputs
        amps=[1/math.sqrt(dim)]*dim
        iterations=3
        for _ in range(iterations):
            for j in good:amps[j]=-amps[j]
            mean=sum(amps)/dim
            amps=[2*mean-a for a in amps]
        observed=sum(amps[i]**2 for i in good)
        p=len(good)/dim
        expected=math.sin((2*iterations+1)*math.asin(math.sqrt(p)))**2
        if abs(observed-expected)>1e-10:raise AssertionError('Amplitude mismatch.')
        records.append(dict(name=name,threshold=k,labels=obj.cartesian_size,basis_states=dim,
            accepted=len(good),accepted_indices=good,resources=res,
            reduced_simulation=dict(iterations=iterations,success_probability=round(observed,12),
                                    scope='Index-space simulation plus exhaustive clean-marker checks, not hardware.')))
    return dict(division_cases=division,markers=records)


if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not use -O/-OO.')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise SystemExit('Refusing to overwrite output.')
    report=run()
    a.output.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print(json.dumps(report,indent=2))
