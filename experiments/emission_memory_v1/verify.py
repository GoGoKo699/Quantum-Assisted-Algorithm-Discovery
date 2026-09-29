#!/usr/bin/env python3
"""Checks of excitation-limited monitored memory, not a quantum advantage test.

Python 3.10+, NumPy, SciPy. No files written or network access. The general
record and factorial-moment bounds are proved in EMISSION_MEMORY_26.md.
"""
from __future__ import annotations
from itertools import product
from collections import Counter
import json
import math
import sys
import numpy as np
from scipy.linalg import expm

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')

TOL = 8e-10
COUNTS = Counter()


def check(ok: bool, name: str) -> None:
    if not ok:
        raise AssertionError(name)
    COUNTS[name] += 1


def matrices(n: int, q: int, omega: float, coupling: float, kappa: float):
    if not isinstance(n, int) or not isinstance(q, int) or n < 1 or not 0 <= q <= n:
        raise ValueError('Require integers n>=1 and 0<=q<=n.')
    if not all(math.isfinite(x) for x in (omega, coupling, kappa)) or kappa <= 0:
        raise ValueError('Require finite parameters and kappa>0.')
    basis = [x for x in range(1 << n) if x.bit_count() <= q]
    where = {x: i for i, x in enumerate(basis)}
    d = len(basis)
    h = np.zeros((d, d), complex)
    # Subtract the ground configuration's scalar energy from every sector.
    for a, x in enumerate(basis):
        z = [((x >> i) & 1) - .5 for i in range(n)]
        h[a, a] = coupling * sum(z[i]*z[i+1] - .25 for i in range(n-1))
        for i in range(n):
            y = x ^ (1 << i)
            if y in where:
                h[where[y], a] += omega/2
    jumps = []
    for i in range(n):
        j = np.zeros_like(h)
        for a, x in enumerate(basis):
            if x & (1 << i):
                j[where[x ^ (1 << i)], a] = math.sqrt(kappa)
        jumps.append(j)
    number = np.array([x.bit_count() for x in basis], dtype=int)
    rate = sum((j.conj().T@j for j in jumps), np.zeros_like(h))
    check(np.max(abs(rate-kappa*np.diag(number))) < TOL, 'decay_number_identity')
    eff = h-.5j*rate
    ident = np.eye(d)
    no = -1j*(np.kron(ident, eff)-np.kron(eff.conj(), ident))
    gen = no + sum((np.kron(j.conj(), j) for j in jumps), np.zeros_like(no))
    rho = np.zeros(d*d, complex); rho[0] = 1
    trace = np.eye(d).ravel(order='F')
    return basis, h, jumps, eff, gen, no, rho, trace, number


def envelope(n: int, q: int, omega: float, kappa: float, horizon: float):
    if not isinstance(q, int) or not 0 <= q <= n or kappa <= 0 or horizon < 0:
        raise ValueError('Invalid envelope parameters.')
    if not all(math.isfinite(x) for x in (omega, kappa, horizon)):
        raise ValueError('Nonfinite envelope.')
    if q == n:
        return 0.
    value = abs(omega)*horizon/2*math.sqrt((q+1)*(n-q)*math.comb(n,q))*(abs(omega)/kappa)**q
    return min(1., value)


def binary_record(data, delta: float, bins: int):
    if delta <= 0 or bins < 1:
        raise ValueError('Positive bin width/count required.')
    _, _, _, _, gen, no, rho, trace, _ = data
    dark = expm(no*delta); total = expm(gen*delta)
    ops = (dark, total-dark)
    states = [rho]
    for _ in range(bins):
        states = [op @ state for state in states for op in ops]
    probabilities = np.array([(trace @ s).real for s in states])
    check(probabilities.min() >= -TOL and abs(probabilities.sum()-1) < TOL, 'record_normalization')
    return states, probabilities


def moments_and_drift(data, n: int, omega: float, kappa: float):
    basis, h, jumps, eff, gen, no, rho, trace, numbers = data
    dim = len(basis)
    # The decay identity is exact at matrix level, including at the cutoff.
    for r in range(1, min(n, int(max(numbers)))+1):
        f = np.diag([math.comb(int(m),r) if m>=r else 0 for m in numbers]).astype(complex)
        adj = sum((j.conj().T@f@j-.5*(j.conj().T@j@f+f@j.conj().T@j) for j in jumps), np.zeros_like(f))
        check(np.max(abs(adj+kappa*r*f)) < TOL, 'factorial_decay_identity')
    for t in (.25, 1., 3., 6.):
        state = (expm(gen*t) @ rho).reshape(dim,dim,order='F')
        diag = np.real(np.diag(state))
        g = (abs(omega)/kappa*(1-math.exp(-kappa*t/2)))**2
        vals = [1.]
        for r in range(1, n+1):
            f = np.array([math.comb(int(m),r) if m>=r else 0 for m in numbers])
            val = float(f @ diag)
            check(val <= math.comb(n,r)*g**r+TOL and val >= -TOL, 'factorial_transient_envelope')
            vals.append(max(0.,val))
            deriv = float(np.real(f @ np.diag((gen@state.ravel(order='F')).reshape(dim,dim,order='F'))))
            bound = abs(omega)*math.sqrt(r*(n-r+1)*vals[r]*vals[r-1])-kappa*r*vals[r]
            check(deriv <= bound+TOL, 'factorial_drift_inequality')


def main():
    # One four-site chain, two regimes; no size sweep or performance fit.
    n = 4; delta = 2.; bins = 3; horizon = delta*bins
    rows = []
    for omega in (.1, 1.):
        reference = matrices(n,n,omega,1.,1.)
        states, law = binary_record(reference,delta,bins)
        moments_and_drift(reference,n,omega,1.)
        for q in (1,2,3,4):
            data = matrices(n,q,omega,1.,1.)
            trial, approx = binary_record(data,delta,bins)
            basis = data[0]; d = len(basis)
            cq = 0.
            for a,b in zip(states,trial):
                embedded = np.zeros((1<<n,1<<n),complex)
                embedded[np.ix_(basis,basis)] = b.reshape(d,d,order='F')
                diff = a.reshape(1<<n,1<<n,order='F')-embedded
                cq += float(np.abs(np.linalg.eigvalsh((diff+diff.conj().T)/2)).sum())/2
            tv = float(abs(law-approx).sum()/2)
            bound = envelope(n,q,omega,1.,horizon)
            check(tv <= cq+TOL and cq <= bound+TOL, 'record_and_final_state_bound')
            moments_and_drift(data,n,omega,1.)
            # The deleted raising block and its exact norm.
            fullh = reference[1]
            outer = [x for x in range(1<<n) if x.bit_count()==q+1]
            inner = [x for x in basis if x.bit_count()==q]
            exactnorm = abs(omega)/2*math.sqrt((q+1)*(n-q)) if q<n else 0.
            num = float(np.linalg.norm(fullh[np.ix_(outer,inner)],2)) if outer else 0.
            check(abs(num-exactnorm)<TOL, 'excitation_boundary_norm')
            # Exact Kraus rank, not an assumption about reachable states.
            rank = np.linalg.matrix_rank(data[2][0],tol=1e-12)
            expected = sum(math.comb(n-1,r) for r in range(q))
            check(rank==expected, 'jump_rank_formula')
            rows.append({'n':n,'Omega':omega,'V':1.,'kappa':1.,'excitation_cutoff':q,
                         'conditional_vector_dimension':d,'record_TV':tv,
                         'record_plus_final_state_trace_distance':cq,'analytic_record_bound':bound,
                         'full_probability_at_least_one_count':float(1-law[0]),
                         'truncated_probability_at_least_one_count':float(1-approx[0]),
                         'local_jump_rank':int(rank)})
    # All-size algebra is in the proof. These check compressed q=1 spaces only.
    renewal=[]
    for size in (4,7,10):
        data=matrices(size,1,.7,1.2,.9)
        basis,h,jumps,eff,_,_,_,_,_=data
        degs=[int(i>0)+int(i<size-1) for i in range(size)]
        classes=sorted(set(degs)); members=[[i for i in range(size) if degs[i]==g] for g in classes]
        w=np.zeros((size+1,1+len(classes)),complex);w[0,0]=1
        for c,inds in enumerate(members,1):
            for i in inds:w[basis.index(1<<i),c]=1/math.sqrt(len(inds))
        small=w.conj().T@eff@w
        check(np.max(abs(eff@w-w@small))<TOL, 'degree_class_invariance')
        predicted=np.zeros_like(small)
        for c,(g,inds) in enumerate(zip(classes,members),1):
            predicted[c,c]=-1.2*g/2-.9j/2
            predicted[0,c]=predicted[c,0]=.7*math.sqrt(len(inds))/2
        check(np.max(abs(small-predicted))<TOL, 'degree_class_generator')
        ground=np.zeros(size+1,complex);ground[0]=1
        for time in (.2,1.,3.):
            v=expm(-1j*eff*time)@ground
            short=w@(expm(-1j*small*time)@w.conj().T@ground)
            check(np.linalg.norm(v-short)<TOL,'renewal_waiting_state_identity')
            for i,j in enumerate(jumps):
                post=j@v; prob=float(np.vdot(post,post).real)
                check(np.linalg.norm(post[1:])<TOL,'every_jump_resets_vacuum_q1')
                ci=classes.index(degs[i])+1
                predictedprob=.9*abs((w.conj().T@v)[ci])**2/len(members[ci-1])
                check(abs(prob-predictedprob)<TOL,'site_resolved_waiting_density')
        # With one excitation shared over a cut, entanglement does not prevent renewal.
        check(small.shape[0]==3,'three_amplitude_open_chain')
        renewal.append({'n':size,'single_excitation_dimension':size+1,
                        'propagated_amplitudes':int(small.shape[0]),'scope':'single-excitation model, not full-chain accuracy'})
    # Reachable post-first-jump states: same last detector label, different waiting time.
    data=matrices(4,4,1.,1.,1.);basis,h,jumps,eff,*_=data
    g=np.zeros(16,complex);g[0]=1
    postrows=[]
    for t in (.5,1.):
        post=jumps[0]@expm(-1j*eff*t)@g
        density=float(np.vdot(post,post).real);post/=math.sqrt(density)
        neighbor=float(np.vdot(jumps[1]@post,jumps[1]@post).real)
        postrows.append({'first_click_time':t,'first_click_site':0,
                         'first_click_density':density,'post_click_neighbor_intensity':neighbor})
    check(abs(postrows[0]['post_click_neighbor_intensity']-postrows[1]['post_click_neighbor_intensity'])>1e-3,
          'last_click_not_global_renewal')
    # Dimension-free envelope is an analytical budget, not a simulated large system.
    budget=[]
    lam=.01; duration=100.
    for q in (1,2,3,4):
        b=duration/2*math.sqrt((q+1)*lam**(q+1)/math.factorial(q))
        budget.append({'lambda_collective':lam,'kappa_T':duration,'cutoff':q,'uniform_upper_bound':b,
                       'scope':'unexecuted all-size bound; Omega/kappa=sqrt(lambda/n)'})
    # Time dependence matters: later multiple photons are not a forbidden history.
    q1data=matrices(4,1,1.,1.,1.)
    _,q1law=binary_record(q1data,delta,bins)
    check(q1law[-1]>1e-3,'repeated_photons_allowed_in_q1')
    invalid=[lambda:matrices(0,0,1,1,1),lambda:matrices(4,5,1,1,1),
             lambda:matrices(4,1,1,1,0),lambda:matrices(4,1,float('nan'),1,1),
             lambda:envelope(4,-1,1,1,1),lambda:envelope(4,1,1,1,-1)]
    for action in invalid:
        try:action()
        except ValueError:continue
        raise AssertionError('Invalid input accepted')
    print(json.dumps({'status':'pass','scope':'Fixed four-site record laws and reduced-space algebra; not many-body scaling, hardware, or runtime.',
                      'precision':'complex128 diagnostics; universal statements follow from the proof, not interval numerics',
                      'record':'global dark/bright coarsening; three bins of width 2; theorem covers the finer site-count law',
                      'counts':dict(sorted(COUNTS.items())),'cutoff_comparisons':rows,
                      'renewal_controls':renewal,'reachable_post_click_control':postrows,
                      'analytical_regime_budget':budget,'q1_probability_bright_in_each_of_three_bins':float(q1law[-1]),
                      'invalid_inputs_rejected':len(invalid)},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
