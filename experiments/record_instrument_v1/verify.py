#!/usr/bin/env python3
"""Finite record-instrument diagnostics and one rational dark-event witness.

Python 3.10+, NumPy, SciPy. No network, input files, or output files.
This is not hardware, a trajectory Monte Carlo benchmark, or a large-n claim.
The general instrument bound is proved in RECORD_INSTRUMENT_25.md.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
import json
import math
import sys
import numpy as np
from scipy.linalg import expm

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([-1., 1.]).astype(complex)  # ground, excited order
LOWER = np.array([[0, 1], [0, 0]], dtype=complex)
TOL = 5e-10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def local(op: np.ndarray, site: int, n: int) -> np.ndarray:
    out = np.ones((1, 1), dtype=complex)
    for j in range(n):
        out = np.kron(out, op if j == site else I2)
    return out


def cmatrix(k: np.ndarray) -> np.ndarray:
    return np.kron(k.conj(), k)


def hc(h: np.ndarray) -> np.ndarray:
    ident = np.eye(len(h))
    return -1j * (np.kron(ident, h) - np.kron(h.T, ident))


def model(n: int, drive: float, coupling: float, decay: float):
    if n < 1 or not all(math.isfinite(x) for x in (drive, coupling, decay)) or decay < 0:
        raise ValueError('Invalid finite model.')
    dim = 2**n
    hx = sum(drive * local(X, i, n)/2 for i in range(n))
    hz = sum((coupling * local(Z, i, n) @ local(Z, i+1, n)/4
              for i in range(n-1)), np.zeros((dim, dim), dtype=complex))
    jumps = [math.sqrt(decay) * local(LOWER, i, n) for i in range(n)]
    rate = sum((a.conj().T@a for a in jumps), np.zeros_like(hx))
    nj = hc(hx+hz)-.5*(np.kron(np.eye(dim), rate)+np.kron(rate.T, np.eye(dim)))
    generator = nj + sum((cmatrix(a) for a in jumps), np.zeros_like(nj))
    initial = np.zeros(dim*dim, dtype=complex); initial[0] = 1
    trace = np.eye(dim).ravel(order='F')
    return hx, hz, jumps, nj, generator, initial, trace


def lifted(n: int, cap: int, drive: float, coupling: float, decay: float):
    """Exact number-resolved generator, with cap denoting >=cap, not truncation."""
    if cap < 1:
        raise ValueError('cap must be positive')
    hx,hz,jumps,nj,generator,initial,trace = model(n,drive,coupling,decay)
    records = list(product(range(cap+1), repeat=n)); index = {c:j for j,c in enumerate(records)}
    d2 = len(initial); length=len(records)*d2
    aa = np.kron(np.eye(len(records)), hc(hx))
    bb = np.kron(np.eye(len(records)), hc(hz))
    cc = np.zeros((length,length), dtype=complex)
    damping_nj = nj-hc(hx+hz)
    for cpos,c in enumerate(records):
        src=slice(cpos*d2,(cpos+1)*d2)
        cc[src,src] += damping_nj
        for i,jump in enumerate(jumps):
            nc=list(c);nc[i]=min(cap,nc[i]+1);dstpos=index[tuple(nc)]
            cc[dstpos*d2:(dstpos+1)*d2,src] += cmatrix(jump)
    return aa,bb,cc,records,initial,trace


def damping_step(n: int, cap: int, h: float, decay: float) -> np.ndarray:
    """Analytic local ancilla instrument, including count saturation."""
    if h <= 0 or decay < 0 or not math.isfinite(h+decay):
        raise ValueError('Invalid damping parameters')
    dim=2**n;d2=dim*dim
    rec=list(product(range(cap+1),repeat=n));ind={c:j for j,c in enumerate(rec)}
    ans=np.eye(len(rec)*d2,dtype=complex)
    no=np.diag([1.,math.exp(-decay*h/2)])
    yes=math.sqrt(-math.expm1(-decay*h))*LOWER
    for i in range(n):
        ka=cmatrix(local(no,i,n));kb=cmatrix(local(yes,i,n))
        step=np.zeros_like(ans)
        for r,c in enumerate(rec):
            src=slice(r*d2,(r+1)*d2);nc=list(c);nc[i]=min(cap,nc[i]+1);s=ind[tuple(nc)]
            step[src,src]+=ka;step[s*d2:(s+1)*d2,src]+=kb
        ans=step@ans
    return ans


def instrument_blocks(channel: np.ndarray, d2: int):
    return [channel[i:i+d2,:d2] for i in range(0,len(channel),d2)]


def two_bin_instrument(blocks):
    return [second@first for first in blocks for second in blocks]


def choi(superop: np.ndarray, dim: int):
    return superop.reshape(dim,dim,dim,dim,order='F').transpose(0,2,1,3).reshape(dim*dim,dim*dim)/dim


def probabilities(blocks, initial, trace):
    p=np.array([(trace@b@initial).real for b in blocks])
    require(p.min()>-TOL and abs(p.sum()-1)<TOL,'Record law not normalized')
    return p


def dark_law(generator, nj, initial, trace, width):
    full=expm(generator*width);dark=expm(nj*width)
    d1=(trace@dark@initial).real;d2=(trace@dark@full@initial).real;both=(trace@dark@dark@initial).real
    return np.array([both,d1-both,d2-both,1-d1-d2+both])


def classical_rate(n: int, drive: float, coupling: float, decay: float, dephase: float=0):
    """Population adiabatic-elimination comparator; not valid uniformly in coherence."""
    size=2**n; rate=np.zeros((size,size));nj=np.zeros_like(rate)
    width=decay/2+dephase
    if width<=0:raise ValueError('Rate model needs a coherence decay width')
    for c in range(size):
        bits=[(c>>(n-1-i))&1 for i in range(n)];spins=[b-.5 for b in bits]
        for i in range(n):
            delta=coupling*sum(spins[j] for j in (i-1,i+1) if 0<=j<n)
            w=drive*drive*width/(2*(width*width+delta*delta));other=c^(1<<(n-1-i))
            for a in (rate,nj):a[other,c]+=w;a[c,c]-=w
            if bits[i]:rate[other,c]+=decay;rate[c,c]-=decay;nj[c,c]-=decay
    initial=np.zeros(size);initial[0]=1
    return rate,nj,initial,np.ones(size)


def exact_dark_intervals(time: F, degree: int=128):
    """Rational Taylor enclosure of survival in 2-emitter Omega=V=kappa=1.

The first propagator is no-jump amplitude evolution; the second is the
adiabatically eliminated population model. All returned endpoints are rational.
"""
    # Gaussian integer matrix M=4*(-i H_eff) in gg,ge,eg,ee order.
    real=[[0,0,0,0],[0,-2,0,0],[0,0,-2,0],[0,0,0,-4]]
    imag=[[-1,-2,-2,0],[-2,1,0,-2],[-2,0,1,-2],[0,-2,-2,-1]]
    vr=[1,0,0,0];vi=[0,0,0,0];sr=[F(1),F(0),F(0),F(0)];si=[F(0)]*4
    coef=F(1)
    for j in range(1,degree+1):
        vr,vi=([sum(real[a][b]*vr[b]-imag[a][b]*vi[b] for b in range(4)) for a in range(4)],
               [sum(real[a][b]*vi[b]+imag[a][b]*vr[b] for b in range(4)) for a in range(4)])
        coef*=time/(4*j)
        sr=[sr[a]+coef*vr[a] for a in range(4)];si=[si[a]+coef*vi[a] for a in range(4)]
    norm=sum(x*x+y*y for x,y in zip(sr,si))
    a=F(9,4)*time
    remainder=F(3)**math.ceil(a)*a**(degree+1)/math.factorial(degree+1)
    survival_error=2*remainder+remainder*remainder
    # N0 with upward and downward stimulated rates 1/2; decay only in diagonal.
    q2=[[-2,1,1,0],[1,-4,0,1],[1,0,-4,1],[0,1,1,-6]]
    v=[1,0,0,0];total=[F(1),F(0),F(0),F(0)];coef=F(1)
    for j in range(1,degree+1):
        v=[sum(q2[a][b]*v[b] for b in range(4)) for a in range(4)];coef*=time/(2*j)
        total=[total[a]+coef*v[a] for a in range(4)]
    classical=sum(total);a=4*time
    cerr=F(3)**math.ceil(a)*a**(degree+1)/math.factorial(degree+1)
    return (norm-survival_error,norm+survival_error),(classical-cerr,classical+cerr)


def floor_string(x: F, digits: int=12) -> str:
    scale=10**digits;return str(F((x.numerator*scale)//x.denominator,scale))


def main():
    n=2;drive=coupling=decay=1.;cap=2;width=2.;horizon=4.
    aa,bb,cc,records,initial,trace=lifted(n,cap,drive,coupling,decay)
    d2=len(initial);dim=int(math.sqrt(d2));generator=aa+bb+cc
    exact=instrument_blocks(expm(width*generator),d2);true=two_bin_instrument(exact)
    p=probabilities(true,initial,trace)
    require(abs(np.linalg.norm(choi(np.eye(d2),dim))-1) < TOL,'Choi normalization')
    c2=2*(n-1)*drive*coupling+4*n*drive*decay+4*(n-1)*coupling*decay
    rows=[]
    for r in (16,32,64,128):
        h=width/r
        damp=damping_step(n,cap,h,decay)
        require(np.max(np.abs(damp-expm(cc*h)))<TOL,'Exact damping instrument')
        step=damp@expm(bb*h)@expm(aa*h)
        split=instrument_blocks(np.linalg.matrix_power(step,r),d2);approx=two_bin_instrument(split)
        q=probabilities(approx,initial,trace);tv=float(np.abs(p-q).sum()/2)
        choi_norm=0.
        for target,trial in zip(true,approx):
            jj=choi(target-trial,dim);require(np.max(abs(jj-jj.conj().T))<TOL,'Hermitian Choi difference')
            choi_norm+=float(np.abs(np.linalg.eigvalsh((jj+jj.conj().T)/2)).sum())
        # normalized Choi trace-distance is a lower bound on half diamond;
        # dim times it is a (possibly loose) upper bound.
        choi_lower=choi_norm/2;choi_upper=dim*choi_lower
        theoretical=min(1.,horizon*h*c2/4)
        require(tv<=theoretical+TOL and choi_lower<=theoretical+TOL,'Record error violates analytic bound')
        rows.append({'substeps_per_detector_bin':r,'h':h,'observed_record_TV':tv,
                     'half_diamond_Choi_lower_diagnostic':choi_lower,
                     'half_diamond_Choi_upper_diagnostic':min(1.,choi_upper),
                     'analytic_record_bound':theoretical})
    # The true record retains repeated emissions. 2 means >=2, not discarded data.
    mult=sum(p[a*len(records)+b] for a,c in enumerate(records) for b in range(len(records)) if 2 in c)
    require(mult>0,'Missing repeated photon events')
    hx,hz,j,nj,sysgen,rho,tr=model(n,drive,coupling,decay)
    pq=dark_law(sysgen,nj,rho,tr,width);pc=dark_law(*classical_rate(n,drive,coupling,decay),width)
    _,_,_,nj0,g0,r0,tr0=model(n,drive,0.,decay)
    independent=dark_law(g0,nj0,r0,tr0,width)
    gathered=np.zeros(4)
    for a,c in enumerate(records):
        for b,d in enumerate(records):
            ia=0 if all(x==0 for x in c) else 1;ib=0 if all(x==0 for x in d) else 1
            gathered[2*ia+ib]+=p[a*len(records)+b]
    require(max(abs(gathered-pq))<TOL,'All counts versus dark-event maps')
    # Factorization into independent single-emitter records at V=0.
    _,_,_,nj1,g1,r1,tr1=model(1,drive,0.,decay)
    single=dark_law(g1,nj1,r1,tr1,width)
    require(abs(independent[0]-single[0]**2)<TOL,'Independent renewal factorization')
    q2,c2_interval=exact_dark_intervals(F(2));q4,c4=exact_dark_intervals(F(4))
    q_event=(q2[0]-q4[1],q2[1]-q4[0]);c_event=(c2_interval[0]-c4[1],c2_interval[1]-c4[0])
    certified=q_event[0]-c_event[1]
    require(certified>F(12,100),'Coherent event witness')
    require(abs(float(sum(q_event)/2)-pq[1])<TOL,'Rational quantum witness')
    require(abs(float(sum(c_event)/2)-pc[1])<TOL,'Rational classical witness')
    # The same rate law improves in the separately specified fast-dephasing controls.
    dephasing=[]
    for phi in (4.,20.):
        noise=sum((phi/2*(cmatrix(local(Z,i,n))-np.eye(d2)) for i in range(n)),np.zeros((d2,d2),complex))
        qp=dark_law(sysgen+noise,nj+noise,rho,tr,width);cp=dark_law(*classical_rate(n,drive,coupling,decay,phi),width)
        dephasing.append({'dephasing_coherence_rate':phi,'dark_binary_record_TV':float(abs(qp-cp).sum()/2),
                          'scope':'different model control, not a proof of asymptotic convergence'})
    invalid=[lambda:model(0,1,1,1),lambda:model(2,1,1,-1),lambda:model(2,float('nan'),1,1),
             lambda:lifted(1,0,1,1,1),lambda:damping_step(1,2,0,1),lambda:classical_rate(1,1,1,0)]
    for f in invalid:
        try:f()
        except ValueError:continue
        raise AssertionError('Invalid input was accepted')
    out={'status':'pass','scope':'One 2-emitter exact coarse-record matrix diagnostic and rational dark-event witness. Not many-body hardness, a hardware run, or a timing comparison.',
         'basis':'ground then excited; Sz=diag(-1/2,1/2)','n':n,'Omega':drive,'V':coupling,'kappa':decay,
         'detector_bin_width':width,'detector_bins':2,'per_site_count_labels':['0','1','>=2'],
         'record_words':len(p),'rows':rows,'probability_some_emitter_has_at_least_two_emissions_in_first_bin':float(mult),
         'dark_record_order':['dark-dark','dark-bright','bright-dark','bright-bright'],
         'exact_quantum_dark_record':pq.tolist(),'population_rate_dark_record':pc.tolist(),
         'exact_independent_emitter_dark_record':independent.tolist(),
         'population_rate_dark_record_TV':float(abs(pq-pc).sum()/2),
         'independent_emitter_dark_record_TV':float(abs(pq-independent).sum()/2),
         'certified_dark_then_bright_gap_lower':floor_string(certified),
         'rational_Taylor_degree':128,'dephasing_controls':dephasing,'invalid_inputs_rejected':len(invalid),
         'precision':'complex128 matrix diagnostics at tolerance 5e-10; only Taylor witness is exact Fraction arithmetic'}
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
