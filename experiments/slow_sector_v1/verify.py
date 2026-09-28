#!/usr/bin/env python3
"""Finite diagnostics for slow-sector spectral reduction, not a quantum benchmark.

Python 3.10+ and NumPy; complex128, no network or file writes. Run with one BLAS
thread for deterministic replay. The all-size statements are proved in Note 18;
small-chain parity checks do not prove absence of degeneracies at arbitrary n.
"""
from __future__ import annotations
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")
TOL = 3e-9
COUNTS: dict[str, int] = {}


def check(ok: bool, label: str) -> None:
    if not ok:
        raise AssertionError(label)
    COUNTS[label] = COUNTS.get(label, 0) + 1


def close(a, b, label: str, tol: float = TOL) -> None:
    err = np.linalg.norm(np.asarray(a) - np.asarray(b))
    check(bool(err <= tol * max(1.0, float(np.linalg.norm(b)))), label)


def comm(a, b):
    return a @ b - b @ a


def spin(n: int, bonds=None):
    dim = 2**n
    h = np.zeros((dim, dim)); v = np.zeros(dim)
    o = np.zeros((dim, dim)); sz = np.zeros(dim); reflection = np.zeros_like(h)
    js = [1.0] * (n - 1) if bonds is None else bonds
    if len(js) != n - 1:
        raise ValueError("Wrong bond count")
    for x in range(dim):
        z = [.5 if not (x >> i) & 1 else -.5 for i in range(n)]
        sz[x] = sum(z)
        v[x] = sum((-1)**(i + 1) * z[i] for i in range(n))
        for i, j in enumerate(js):
            h[x, x] += j * z[i] * z[i + 1]
            if ((x >> i) ^ (x >> (i + 1))) & 1:
                h[x ^ (1 << i) ^ (1 << (i + 1)), x] += j / 2
        for i in range(n):
            if (x >> i) & 1:
                o[x ^ (1 << i), x] = 1
        reflection[int(f'{x:0{n}b}'[::-1], 2), x] = 1
    return h, np.diag(v), o, np.diag(sz), reflection


def blocks(values):
    groups = []
    for i, val in enumerate(values):
        if not groups or abs(val - values[groups[-1][0]]) > 1e-9:
            groups.append([i])
        else:
            groups[-1].append(i)
    return groups


def reduce(h, v):
    e, u = np.linalg.eigh(h)
    gs = blocks(e)
    vt = u.conj().T @ v @ u
    same = np.abs(e[:, None] - e[None, :]) < 1e-9
    inv = np.zeros_like(same, dtype=float)
    np.divide(1.0, e[:, None] - e[None, :], out=inv, where=~same)
    h2 = np.zeros_like(vt, dtype=complex)
    for ix in gs:
        rest = np.array([j for j in range(len(e)) if j not in ix])
        if len(rest):
            a = vt[np.ix_(ix, rest)]
            h2[np.ix_(ix, ix)] = (a / (e[ix[0]] - e[rest])) @ a.conj().T
    return e, u, gs, vt, same, inv, h2


def spectral_bins(h, o, gamma, edges, scale=1.0):
    if not math.isfinite(gamma) or gamma <= 0:
        raise ValueError("Linewidth must be finite and positive")
    e, u = np.linalg.eigh(h)
    weights = np.abs(u.conj().T @ o @ u)**2
    weights /= np.vdot(o, o).real
    freqs = (e[:, None] - e[None, :]) / scale
    cdf = np.array([np.sum(weights * (.5 + np.arctan((x - freqs) / gamma) / np.pi)) for x in edges])
    return np.diff(cdf)


def spin_checks():
    rows = []; bins_rows = []
    for n in (2, 4, 6, 8):
        h, v, o, sz, ref = spin(n)
        e, u, gs, vt, same, inv, h2 = reduce(h, v)
        ot = u.T @ o @ u; szt = u.T @ sz @ u
        close(ref @ h, h @ ref, 'reflection_commutation')
        close(ref @ v @ ref, -v, 'reflection_odd_field')
        close(comm(h, o), np.zeros_like(o), 'collective_conservation')
        v0 = vt * same
        close(v0, np.zeros_like(v0), 'zero_block_field')
        staggered = comm(vt, ot)
        close(same * staggered, np.zeros_like(staggered), 'zero_conserved_overlap')
        for x in (ot, szt, same * np.exp(1j * np.arange(len(e))[:, None] / 7) * np.cos(np.arange(len(e))[None, :] / 9)):
            slow = -(same * comm(vt, inv * comm(vt, x)))
            close(slow, comm(h2, x), 'effective_commutator')
        max_parity_error = 0.0
        for ix in gs:
            rp = u[:, ix].T @ ref @ u[:, ix]
            parity = np.trace(rp).real / len(ix)
            close(abs(parity), 1.0, 'parity_pure_energy_block')
            max_parity_error = max(max_parity_error, float(np.linalg.norm(rp-parity*np.eye(len(ix)))))
            z = szt[np.ix_(ix, ix)]; b = h2[np.ix_(ix, ix)]
            plus = ot[np.ix_(ix, ix)]
            spin_value = (len(ix)-1)/2
            close(z@z + (plus@plus.conj().T+plus.conj().T@plus)/2,
                  spin_value*(spin_value+1)*np.eye(len(ix)), 'single_spin_multiplet')
            zz = z @ z
            design = np.column_stack([np.eye(len(ix)).ravel(), zz.ravel()])
            coeff = np.linalg.lstsq(design, b.ravel(), rcond=None)[0]
            close(b, coeff[0]*np.eye(len(ix)) + coeff[1]*zz, 'quadratic_multiplet_fit')
        top = gs[-1]; s = n / 2
        z = szt[np.ix_(top, top)]
        close(h2[np.ix_(top, top)], (s*s*np.eye(n+1)-z@z)/(n-1), 'max_spin_effective_formula')
        top_weight = float(np.linalg.norm(ot[np.ix_(top, top)])**2 / np.linalg.norm(o)**2)
        close(top_weight, (n+1)*(n+2)/(3*2**n), 'max_spin_response_weight')
        distinct = np.array([np.mean(e[g]) for g in gs]); gap = float(np.min(np.diff(distinct)))
        check(gap <= 1 - math.cos(math.pi/n) + TOL, 'one_magnon_gap_upper_bound')
        rows.append({'n': n, 'energy_blocks_numeric': len(gs), 'smallest_nonzero_energy_difference_over_J': gap,
                     'parity_block_max_residual': max_parity_error,
                     'conserved_staggered_mass_numeric': float(np.linalg.norm(same*staggered)**2/np.linalg.norm(o)**2),
                     'max_spin_response_weight': top_weight})
        if n <= 4:
            for d in ((.01, .005) if n == 2 else (.001, .0005)):
                c = 4.0; gamma = c*d*d; pert = d*n; x = pert/gap
                bound = min(1., 2*x + 2*pert**3/(gap*gap*gamma))
                edges = np.array([-np.inf,-20,-5,-2,-1,-.5,0,.5,1,2,5,20,np.inf])
                full = spectral_bins(h+d*v,o,c,edges,scale=d*d)
                approx = spectral_bins(h2,ot,c,edges)
                tv = float(np.sum(np.abs(full-approx))/2)
                check(x <= .125, 'perturbation_domain')
                check(tv <= bound+TOL, 'binned_response_bound')
                close(full.sum(),1.,'bin_normalization');close(approx.sum(),1.,'bin_normalization')
                bins_rows.append({'n':n,'d_over_J':d,'gamma_over_d2_J':c,'binned_TV':tv,'proved_upper_bound':bound})
    # Reflection symmetry alone does not forbid opposite-parity degeneracies.
    h = np.diag([0.,0.,2.]); ref=np.diag([1.,-1.,1.]); v=np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,0.]])
    close(comm(h,ref),0.,'degenerate_parity_control')
    close(ref@v@ref,-v,'degenerate_parity_control')
    check(np.linalg.norm(v[:2,:2])>1.,'mixed_parity_obstruction_detected')
    h,v,o,_,_ = spin(4,[1.,.7,1.2]); e,u,gs,vt,same,inv,h2=reduce(h,v)
    check(np.linalg.norm(same*comm(vt,u.T@o@u))>.01,'broken_reflection_control')
    return rows,bins_rows


def riccati_checks():
    rows=[]
    for q in (2,3):
        p=2
        b=np.diag([(-1)**j*(1+j/3) for j in range(q)])
        a=np.array([[math.sin((j+1)*(k+2)) for k in range(p)] for j in range(q)],complex)
        c=np.array([[math.cos(j+k+1) for k in range(q)] for j in range(q)])
        perturb=np.block([[np.zeros((p,p)),a.conj().T],[a,c]])
        perturb/=np.linalg.norm(perturb,2)
        a=perturb[p:,:p];c=perturb[p:,p:]
        for lam in (.03,.1):
            e=lam; g=1.;x=e/g
            k=b+lam*c; f=lam*a
            xx=-np.linalg.solve(k,f)
            for _ in range(100):
                new=np.linalg.solve(k,-f+xx@f.conj().T@xx)
                if np.linalg.norm(new-xx)<1e-15:xx=new;break
                xx=new
            close(k@xx+f,xx@f.conj().T@xx,'riccati_identity')
            ev,uu=np.linalg.eigh(np.eye(p)+xx.conj().T@xx)
            norm=(uu*(1/np.sqrt(ev)))@uu.conj().T
            w=np.vstack([np.eye(p),xx])@norm
            big=np.block([[np.zeros((p,p)),f.conj().T],[f,k]])
            eff=w.conj().T@big@w; second=-f.conj().T@np.linalg.solve(b,f)
            close(w.conj().T@w,np.eye(p),'graph_isometry')
            close(big@w,w@eff,'invariant_graph')
            rem=float(np.linalg.norm(eff-second,2))
            check(np.linalg.norm(xx,2)<=2*x+TOL,'graph_size_bound')
            check(np.linalg.norm(xx+np.linalg.solve(b,f),2)<=2*x*x+TOL,'graph_remainder_bound')
            check(rem<=4*e**3/g**2+TOL,'effective_remainder_bound')
            vec=np.array([1.,1j])/np.sqrt(2);initial=np.r_[vec,np.zeros(q)]
            td=math.sqrt(max(0.,1-abs(np.vdot(initial,w@vec))**2))
            check(td<=2*x+TOL,'state_dressing_bound')
            rows.append({'complement_dimension':q,'perturbation_over_gap':x,'effective_norm_error':rem,'norm_error_bound':4*e**3})
    # The general block estimate does not apply after adding an ignored P-D-P term.
    check(abs(.03 - 0.) > 4*.03**3,'ignored_first_order_control')
    return rows


def path_checks():
    for n in (2,4,6,8,12,20):
        lap=np.diag([1]+[2]*(n-2)+[1])-np.diag(np.ones(n-1),1)-np.diag(np.ones(n-1),-1)
        eps=np.array([(-1)**(i+1) for i in range(n)])
        e,u=np.linalg.eigh(lap.astype(float)); rec=np.zeros(n)
        np.divide(1.,e,out=rec,where=e>1e-10)
        val=eps@((u*rec)@u.T)@eps
        close(val,n/2,'path_green_formula')
        flow=np.cumsum(eps)[:-1]
        close(flow@flow,n/2,'path_flow_formula')


def main():
    rows,binned=spin_checks(); graph=riccati_checks();path_checks()
    invalid=0
    for gamma in (0.,-1.,float('nan'),float('inf')):
        try:spectral_bins(np.diag([0.,1.]),np.eye(2),gamma,[-np.inf,np.inf])
        except ValueError:invalid+=1
        else:raise AssertionError('Invalid linewidth accepted')
    print(json.dumps({'status':'pass','scope':'Finite complex128 structural checks, not all-size parity proof, quantum circuit, experiment, or timing.',
        'tolerance':TOL,'counts':COUNTS,'chain_controls':rows,'binned_spectral_controls':binned,
        'general_graph_controls':graph,'invalid_linewidths_rejected':invalid},indent=2,sort_keys=True))

if __name__=='__main__':main()
