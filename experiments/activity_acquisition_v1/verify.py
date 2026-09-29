#!/usr/bin/env python3
"""Acquire and validate one source-matched classical activity reduction.

Python 3.10+, NumPy, SciPy. One seven-emitter ring, not a size/parameter survey.
No network or file writes. Complex128 diagnostics, NOT interval certification.
Read CLASSICAL_ACTIVITY_ACQUISITION_29.md for the model, scope and decision.
"""
from __future__ import annotations
import json
import math
import sys
import numpy as np
from scipy import sparse
from scipy.linalg import expm
from scipy.sparse.linalg import LinearOperator, eigs, expm_multiply, splu

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def ring_model(n: int, drive: float, coupling: float, decay: float):
    if not isinstance(n, int) or n < 3 or not all(math.isfinite(x) for x in (drive, coupling, decay)) or decay <= 0:
        raise ValueError("Require n>=3, finite parameters and positive decay.")
    dim = 1 << n
    mask = dim-1
    def rotate(x, k):
        return ((x << k) | (x >> (n-k))) & mask if k else x
    rev = [int(f"{x:0{n}b}"[::-1], 2) for x in range(dim)]
    permutations = np.array([[rotate(x,k) for x in range(dim)] for k in range(n)] +
                            [[rotate(rev[x],k) for x in range(dim)] for k in range(n)])
    orbit = np.full(dim*dim, -1, dtype=int)
    reps, sizes = [], []
    for x in range(dim*dim):
        if orbit[x] >= 0:
            continue
        a,b = x % dim, x // dim
        members = np.unique(permutations[:,a] + dim*permutations[:,b])
        orbit[members] = len(reps)
        reps.append((a,b)); sizes.append(len(members))
    sizes = np.array(sizes)
    count = len(reps)
    pop = np.array([x.bit_count() for x in range(dim)])
    energy = np.array([coupling/4*sum((2*((x>>i)&1)-1)*(2*((x>>((i+1)%n))&1)-1)
                                      for i in range(n)) for x in range(dim)])
    def actions(a,b):
        yield a+dim*b, -1j*(energy[a]-energy[b]) - decay*(pop[a]+pop[b])/2, False
        for i in range(n):
            bit=1<<i
            yield (a^bit)+dim*b, -1j*drive/2, False
            yield a+dim*(b^bit), 1j*drive/2, False
            if a&bit and b&bit:
                yield (a^bit)+dim*(b^bit), decay, True
    # Acquisition: one representative per dihedral orbit, not a supplied eigenbasis.
    rr,cc,vv,jr,jc,jv = [],[],[],[],[],[]
    for col,(a,b) in enumerate(reps):
        for destination,value,jump in actions(a,b):
            row=orbit[destination]; value*=math.sqrt(sizes[col]/sizes[row])
            rr.append(row);cc.append(col);vv.append(value)
            if jump:jr.append(row);jc.append(col);jv.append(value)
    L=sparse.coo_matrix((vv,(rr,cc)),shape=(count,count)).tocsc()
    J=sparse.coo_matrix((jv,(jr,jc)),shape=(count,count)).tocsc()
    L.eliminate_zeros(); J.eliminate_zeros()
    embedding=sparse.coo_matrix((1/np.sqrt(sizes[orbit]),(np.arange(dim*dim),orbit)),
                               shape=(dim*dim,count)).tocsc()
    trace=np.eye(dim).ravel(order='F')@embedding
    initial=np.zeros(count); initial[orbit[0]]=1
    # Independent full-basis generator assembly validates the exact reduction.
    rr,cc,vv,jr,jc,jv = [],[],[],[],[],[]
    for col in range(dim*dim):
        for row,value,jump in actions(col%dim,col//dim):
            rr.append(row);cc.append(col);vv.append(value)
            if jump:jr.append(row);jc.append(col);jv.append(value)
    full=sparse.coo_matrix((vv,(rr,cc)),shape=(dim*dim,dim*dim)).tocsc()
    fullJ=sparse.coo_matrix((jv,(jr,jc)),shape=(dim*dim,dim*dim)).tocsc()
    e0=sparse.linalg.norm(embedding.conj().T@embedding-sparse.eye(count))
    eL=sparse.linalg.norm(full@embedding-embedding@L)/max(1.,sparse.linalg.norm(full))
    eJ=sparse.linalg.norm(fullJ@embedding-embedding@J)/max(1.,sparse.linalg.norm(fullJ))
    require(max(e0,eL,eJ)<2e-12,"Symmetry reduction failed")
    require(np.linalg.norm(trace@L)<1e-9,"Original channel not trace preserving")
    return L,J,np.asarray(trace).ravel(),initial,embedding,(e0,eL,eJ)


def acquire(L,J,trace,initial,embedding,shift=1e-4):
    if shift<=0 or not math.isfinite(shift):
        raise ValueError("Positive finite shift required.")
    size=L.shape[0]
    start=np.cos(np.arange(size)*.37)+1j*np.sin(np.arange(size)*.23)
    factor=splu(L-shift*sparse.eye(size,format="csc"))
    calls={"right":0,"left":0}
    def solve(v, adjoint=False):
        calls["left" if adjoint else "right"]+=1
        return factor.solve(v,trans="H" if adjoint else "N")
    right_inverse=LinearOperator(L.shape,matvec=solve,dtype=complex)
    left_inverse=LinearOperator(L.shape,matvec=lambda v:solve(v,True),dtype=complex)
    w,R=eigs(L,k=2,sigma=shift,OPinv=right_inverse,tol=1e-12,maxiter=5000,v0=start)
    order=np.argsort(-w.real);w=w[order];R=R[:,order]
    wl,left=eigs(L.conj().T,k=2,sigma=shift,OPinv=left_inverse,tol=1e-12,maxiter=5000,v0=start)
    left=left[:,np.argsort(-wl.real)]
    dim=int(math.sqrt(embedding.shape[0]))
    for j in range(2):
        mat=(embedding@R[:,j]).reshape(dim,dim,order='F')
        phase=mat[0,0]
        mat*=np.exp(-1j*np.angle(phase))
        mat=(mat+mat.conj().T)/2
        R[:,j]=embedding.conj().T@mat.ravel(order='F')
        if j==0:
            R[:,j]/=trace@R[:,j]
        else:
            R[:,j]-=R[:,0]*(trace@R[:,j])
            R[:,j]/=np.linalg.norm(R[:,j])
    W=np.linalg.solve(left.conj().T@R,left.conj().T)
    A=W@(L@R); B=W@(J@R); c=W@initial; ell=trace@R
    right=np.linalg.norm(L@R-R@A)
    left_error=np.linalg.norm(W@L-A@W)
    require(right<1e-7 and left_error<1e-7,"Low-mode residual too large")
    require(np.linalg.norm(W@R-np.eye(2))<1e-10,"Dual basis failed")
    require(max(np.max(abs(z.imag)) for z in (A,B,c,ell))<1e-8,"Expected a real contraction model")
    cost={"right_inverse_actions":calls["right"],"left_inverse_actions":calls["left"],
          "factor_L_plus_U_nonzeros":factor.L.nnz+factor.U.nnz,"sparse_factorizations":1}
    return A.real,B.real,c.real,ell.real,R,W,(right,left_error),cost


def reduced(A,B,c,ell,n,kappa,delta,u=1.):
    if delta<=0 or not math.isfinite(delta) or u<0 or not math.isfinite(u):
        raise ValueError("Require finite delta>0 and u>=0.")
    factor=np.expm1(-u/(n*kappa*delta))
    E=expm(delta*(A+factor*B)); F=expm(delta*A)
    z=np.array([ell@E@c,ell@E@F@c,ell@E@E@c])
    return z,float(z[2]-z[0]*z[1])


def direct(L,J,tr,rho,n,kappa,delta):
    Ls=L+np.expm1(-1/(n*kappa*delta))*J
    def prop(G,t,v):
        return expm_multiply(t*G,v,traceA=t*G.diagonal().sum())
    a=prop(Ls,delta,rho); b=prop(Ls,delta,prop(L,delta,rho)); c=prop(Ls,delta,a)
    zc=np.array([tr@a,tr@b,tr@c])
    require(np.max(abs(zc.imag))<1e-10,"Unexpected imaginary probability")
    z=zc.real
    require(np.all(z>=0) and np.all(z<=1),"Invalid Laplace probabilities")
    # Same sparse exponential algorithm at half steps: a consistency check, not an interval proof.
    half=prop(Ls,delta/2,prop(Ls,delta/2,rho))
    discrepancy=float(np.linalg.norm(half-a))
    require(discrepancy<1e-9,"Full versus half-step propagation disagree")
    g=float(z[2]-z[0]*z[1])
    return z,g,discrepancy


def clean(x):
    if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [clean(v) for v in x]
    if isinstance(x,np.ndarray):return clean(x.tolist())
    if isinstance(x,(np.floating,float)):return float(round(float(x),12)) if round(float(x),12)!=0 else 0.0
    if isinstance(x,np.integer):return int(x)
    return x


def main():
    n=7;drive=50.;coupling=250.;kappa=1.
    L,J,tr,rho,embedding,symmetry_errors=ring_model(n,drive,coupling,kappa)
    require(L.shape==(1300,1300),"Unexpected seven-site orbit count")
    A,B,c,ell,R,W,residuals,cost=acquire(L,J,tr,rho,embedding)
    A2,B2,c2,ell2,*_=acquire(L,J,tr,rho,embedding,shift=1e-3)
    # Only a stationary-preparation negative control; NOT the target initial state.
    stationary_c=W@R[:,0]
    rows=[]
    for delta in (1.,4.,16.):
        z,g,prop_error=direct(L,J,tr,rho,n,kappa,delta)
        zr,gr=reduced(A,B,c,ell,n,kappa,delta)
        zs,gs=reduced(A,B,stationary_c.real,ell,n,kappa,delta)
        zalt,galt=reduced(A2,B2,c2,ell2,n,kappa,delta)
        _,zero_tilt=reduced(A,B,c,ell,n,kappa,delta,u=0)
        require(abs(zero_tilt)<1e-9,"Zero-tilt covariance should vanish")
        require(np.max(abs(zalt-zr))<2e-9 and abs(galt-gr)<2e-9,"Sparse acquisition shift check failed")
        require(abs(g-gr)<3.4e-5,"Two-mode covariance does not pass declared diagnostic tolerance")
        require(abs(g-gs)>5e-4,"Initial-state negative control did not discriminate")
        rows.append({"window_kappa_Delta":delta,"full_tilted_Z1_Z2_Z12":z,
                     "full_covariance":g,"acquired_two_mode_Z1_Z2_Z12":zr,
                     "acquired_two_mode_covariance":gr,"absolute_covariance_discrepancy":abs(gr-g),
                     "max_Laplace_probability_discrepancy":float(np.max(abs(z-zr))),
                     "wrong_stationary_start_covariance":gs,
                     "shift_check_max_probability_discrepancy":float(np.max(abs(zalt-zr))),
                     "propagation_half_step_vector_discrepancy":prop_error})
    invalid=[lambda:ring_model(2,1.,1.,1.),lambda:ring_model(3,float('nan'),1.,1.),
             lambda:ring_model(3,1.,1.,0.),lambda:reduced(A,B,c,ell,n,kappa,0.),
             lambda:reduced(A,B,c,ell,n,kappa,1.,u=-1.)]
    for check in invalid:
        try:check()
        except ValueError:continue
        raise AssertionError("Invalid input accepted")
    out={"status":"pass","model":{"n":n,"Omega_over_kappa":drive,"V_over_kappa":coupling,
         "graph":"periodic nearest-neighbor ring","initial":"all ground","u":1},
         "acquisition":{"full_Liouville_dimension":4**n,"symmetry_dimension":L.shape[0],
           "symmetry":"simultaneous dihedral action on bra and ket","generator_nonzeros":L.nnz,
           "reduced_parameters_fitted_or_supplied":False,"sparse_work":cost,"slow_modes_per_side":2,
           "method":"two shift-invert sparse right/left eigensolves, biorthogonal projection; one acquisition reused at all windows",
           "reduced_L":A,"reduced_jump":B,"initial_coefficients":c,"trace_row":ell,
           "slow_relaxation_time":-1/A[1,1],"right_residual_Frobenius":residuals[0],
           "left_residual_Frobenius":residuals[1],"intertwining_checks":symmetry_errors},
         "rows":rows,"invalid_inputs_rejected":len(invalid),
         "validation":"Direct sparse exponential action in the full invariant operator sector; full-basis intertwining; second eigensolver shift; step composition",
         "precision":"complex128, rounded decimals; no interval certificate or worst-case scaling inference",
         "scope":"One source-matched seven-emitter acquisition/validation. No quantum circuit, native upstream solver, trajectory shots, parameter sweep, or timing comparison.",
         "interpretation":"The two-mode model is validated for three scalar contractions/covariance, not a positive full-record instrument or all counting fields."}
    print(json.dumps(clean(out),indent=2,sort_keys=True))

if __name__=='__main__':
    main()
