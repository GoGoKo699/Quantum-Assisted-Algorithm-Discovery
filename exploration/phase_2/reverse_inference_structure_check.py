"""Finite checks of information retained by coarse reverse conditioning.

This is classical exact linear algebra plus Haar-reference sampling, not quantum
execution, a many-body hardness benchmark, or a test of a deployed material.
The Haar reference must NOT be substituted for energy-conserving local dynamics.
Requires NumPy. Existing evidence files are never overwritten.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np


def tv(p: np.ndarray, q: np.ndarray) -> float:
    return float(np.sum(np.abs(p-q))/2)


def haar_isometry(rng: np.random.Generator, d: int, r: int) -> np.ndarray:
    z = rng.normal(size=(d,r)) + 1j*rng.normal(size=(d,r))
    q, rr = np.linalg.qr(z, mode='reduced')
    # Phases do not change QQ^dagger; include the usual correction explicitly.
    diagonal = np.diag(rr)
    phases = np.ones_like(diagonal)
    np.divide(diagonal, np.abs(diagonal), out=phases, where=np.abs(diagonal)>0)
    return q*phases


def haar_exact_mean_tv(d: int, r: int) -> float:
    if not 1 <= r <= d:
        raise ValueError('Require 1 <= r <= d.')
    if r == d:
        return 0.0
    a = r/d
    log_beta = math.lgamma(r)+math.lgamma(d-r)-math.lgamma(d)
    return math.exp(r*math.log(a)+(d-r)*math.log1p(-a)-math.log(r)-log_beta)


def reference_checks() -> list[dict]:
    rng = np.random.default_rng(20260926)
    records=[]
    for d,r in ((64,1),(64,4),(64,16),(64,32),(256,1),(256,4),(256,16),(256,64)):
        distances=[]; chi=[]; norm_error=0.0; orth_error=0.0
        for _ in range(160):
            q=haar_isometry(rng,d,r)
            p=np.sum(np.abs(q)**2,axis=1)/r
            norm_error=max(norm_error,abs(float(p.sum())-1))
            orth_error=max(orth_error,float(np.max(np.abs(q.conj().T@q-np.eye(r)))))
            distances.append(tv(p,np.full(d,1/d)))
            chi.append(float(d*np.sum((p-1/d)**2)))
        expectation=haar_exact_mean_tv(d,r)
        se=float(np.std(distances,ddof=1)/math.sqrt(len(distances)))
        if norm_error>1e-11 or orth_error>1e-11:
            raise AssertionError('Isometry normalization failed.')
        records.append(dict(dimension=d,event_rank=r,event_probability=r/d,
            independently_drawn_subspaces=len(distances),mean_tv=float(np.mean(distances)),
            exact_ensemble_mean_tv=expectation,monte_carlo_standard_error=se,
            mean_chi_squared=float(np.mean(chi)),exact_mean_chi_squared=(d-r)/(r*(d+1)),
            ensemble_mean_tv_upper_bound=.5*math.sqrt((d-r)/(r*(d+1))),
            normalization_error=norm_error,orthogonality_error=orth_error,
            scope='Monte Carlo corroboration, not a confidence-certified assertion about one circuit.'))
    return records


def sector_hamiltonian(n: int, particles: int, interacting: bool):
    states=[x for x in range(1<<n) if x.bit_count()==particles]
    index={x:i for i,x in enumerate(states)}
    occupation=np.array([[(x>>j)&1 for j in range(n)] for x in states],dtype=float)
    h=np.zeros((len(states),len(states)),dtype=float)
    for i,x in enumerate(states):
        h[i,i]=sum((.13*math.cos(.7*j)+.05*(-1)**j)*occupation[i,j] for j in range(n))
        if interacting:
            h[i,i]+=1.1*sum(occupation[i,j]*occupation[i,j+1] for j in range(n-1))
            h[i,i]+=.7*sum(occupation[i,j]*occupation[i,j+2] for j in range(n-2))
        for j in range(n-1):
            if ((x>>j)&1)!=((x>>(j+1))&1):
                other=x^(1<<j)^(1<<(j+1))
                h[index[other],i]+=1+.08*math.sin(j)
    if np.max(abs(h-h.T))>1e-14:
        raise AssertionError('Hamiltonian not real symmetric.')
    return states,occupation,h


def local_relaxation_checks():
    n,particles=10,5
    patch=(3,4,5)
    reports=[]
    for interacting in (False,True):
        states,occ,h=sector_hamiltonian(n,particles,interacting)
        d=len(states); endpoints=np.where(np.all(occ[:,patch]==1,axis=1))[0]
        r=len(endpoints)
        e,v=np.linalg.eigh(h)
        cases=[]
        for t in (0,.5,1,2,4,8):
            u=(v*np.exp(-1j*t*e))@v.T
            w=np.abs(u)**2
            posterior=w[endpoints,:].sum(axis=0)/r
            relaxation=w[:,endpoints].sum(axis=1)/r
            mismatch=tv(posterior,relaxation)
            if mismatch>1e-11 or abs(float(posterior.sum())-1)>1e-11:
                raise AssertionError('Retrodiction/relaxation identity failed.')
            means=posterior@occ
            pair=occ.T@(posterior[:,None]*occ)
            cov=pair-means[:,None]*means[None,:]
            patch_count=occ[:,patch].sum(axis=1).astype(int)
            filled=len(patch)-patch_count
            distribution=np.bincount(filled,weights=posterior,minlength=len(patch)+1)
            m=float(distribution@np.arange(len(distribution)))
            var=float(distribution@((np.arange(len(distribution))-m)**2))
            cases.append(dict(time=t,reverse_forward_tv=mismatch,
                posterior_tv_from_sector_uniform=tv(posterior,np.full(d,1/d)),
                initial_density_conditioned_on_final_patch=means.tolist(),
                net_patch_filling_probabilities=distribution.tolist(),
                net_patch_filling_mean=m,net_patch_filling_variance=var,
                example_left_right_covariance=float(cov[2,6])))
        reports.append(dict(n=n,particles=particles,sector_dimension=d,event_rank=r,
            event_probability=r/d,patch_sites=list(patch),interactions=interacting,
            observations=cases,scope='Both models solved classically; real H has energy conservation and is not a Haar ensemble.'))
    return reports


def controls():
    d,r=16,4
    event=np.zeros(d);event[:r]=1/r
    identity=tv(event,np.full(d,1/d))
    j=np.arange(d)
    fourier=np.exp(2j*np.pi*j[:,None]*j[None,:]/d)/math.sqrt(d)
    posterior=(abs(fourier[:r,:])**2).sum(axis=0)/r
    fourier_error=tv(posterior,np.full(d,1/d))
    if abs(identity-(1-r/d))>1e-12 or fourier_error>1e-12:
        raise AssertionError('Simple controls failed.')
    # Append idle spectators and condition them to zero: evidence becomes
    # arbitrarily rarer while the inference on the original subsystem is unchanged.
    active=np.array([[1,1],[-1,1]],dtype=float)/math.sqrt(2)
    p0=abs(active[0,:])**2
    spectator_checks=[]
    for s in (0,2,6):
        u=np.kron(active,np.eye(1<<s))
        posterior=abs(u[0,:])**2
        active_marginal=posterior.reshape(2,1<<s).sum(axis=1)
        difference=tv(active_marginal,p0)
        if difference>1e-12:raise AssertionError('Spectator marginal changed.')
        spectator_checks.append(dict(idle_spectators=s,evidence=1/len(u),active_tv_change=difference))
    d100=math.comb(100,50);r100=math.comb(80,30)
    return dict(same_evidence_controls=dict(dimension=d,rank=r,evidence=r/d,
        identity_posterior_tv=identity,fourier_posterior_tv=fourier_error),
        idle_spectators=spectator_checks,
        hundred_site_combinatorics=dict(sector_dimension=str(d100),event_rank=str(r100),
            evidence_probability=r100/d100,naive_forward_rejection_mean=d100/r100,
            haar_ensemble_mean_tv_upper_bound=.5*math.sqrt((d100-r100)/(r100*(d100+1))),
            scope='Combinatorics plus Haar-reference bound only; no 100-site simulation or design-time claim.'))


def run():
    return dict(scope='Classical mechanism checks only. No new quantum algorithm, useful advantage, or manuscript.',
                seed=20260926,numpy_version=np.__version__,controls=controls(),
                haar_reference=reference_checks(),local_models=local_relaxation_checks())

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True,type=Path)
    a=p.parse_args()
    if a.output.exists():raise SystemExit('Output already exists.')
    result=run()
    with a.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps({'controls':result['controls'],
                     'haar':[{k:z[k] for k in ['dimension','event_rank','mean_tv','exact_ensemble_mean_tv','monte_carlo_standard_error']} for z in result['haar_reference']],
                     'local_max_reverse_error':max(x['reverse_forward_tv'] for z in result['local_models'] for x in z['observations'])},indent=2))
