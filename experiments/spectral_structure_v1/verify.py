#!/usr/bin/env python3
"""Small deterministic checks of model-level spectral identities.

Python 3.10+ and NumPy. Not an NMR fit, a quantum-circuit implementation, or a
performance benchmark. Proofs are in SPECTRAL_MODEL_STRUCTURE_15.md. No file writes.
"""
from __future__ import annotations
import itertools
import json
import math
import sys
import numpy as np

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")

I = np.eye(2, dtype=complex)
PAULI = (np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.diag([1., -1.]).astype(complex))
TOL = 2e-10


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def close(a, b, label: str) -> None:
    require(bool(np.allclose(a, b, atol=TOL, rtol=TOL)), label)


def kron_all(ops):
    out = np.array([[1.]], complex)
    for op in ops:
        out = np.kron(out, op)
    return out


def model(offsets, edges, secular=False):
    n = len(offsets)
    spins = [[kron_all([p / 2 if k == j else I for k in range(n)])
              for p in PAULI] for j in range(n)]
    zero = np.zeros((2**n, 2**n), complex)
    h = sum((d * spins[j][2] for j, d in enumerate(offsets)), zero.copy())
    for i, j, coupling in edges:
        h += coupling * sum((spins[i][a] @ spins[j][a]
                              for a in ([2] if secular else range(3))), zero.copy())
    o = sum((s[0] + 1j * s[1] for s in spins), zero.copy())
    return h, o


def spectral(h, o):
    energies, vectors = np.linalg.eigh(h)
    amplitudes = vectors.conj().T @ o @ vectors
    weights = abs(amplitudes.ravel()) ** 2 / np.vdot(o, o).real
    frequencies = (energies[:, None] - energies[None, :]).ravel()
    close(weights.sum(), 1, "spectral normalization")
    return frequencies, weights


def bins(law, gamma):
    if not math.isfinite(gamma) or gamma <= 0:
        raise ValueError("gamma must be positive and finite")
    frequencies, weights = law
    # Fixed binning plus both overflow bins; not a density quadrature.
    endpoints = np.r_[-np.inf, np.linspace(-20, 20, 801), np.inf]
    cdf = .5 + np.arctan((endpoints[:, None] - frequencies[None, :]) / gamma) / math.pi
    probabilities = np.diff(cdf, axis=0) @ weights
    require(float(probabilities.min()) >= -TOL, "negative bin probability")
    close(probabilities.sum(), 1, "all-frequency bins")
    return probabilities


def tv(a, b):
    return float(np.abs(a - b).sum() / 2)


def main():
    cases = [([0.], []),
             ([-.5, .5], [(0, 1, 1.)]),
             ([-2., .5, 1.5], [(0, 1, .7), (1, 2, 1.3), (0, 2, -.4)]),
             ([0., 0., 0., 0.], [(0, 1, 2.), (1, 2, -1.), (2, 3, 3.), (3, 0, .5)]),
             ([-1., 1., 2., -2.], [(0, 1, 3.), (1, 2, -2.), (2, 3, 1.), (0, 3, .7)])]
    count = {"model_cases": len(cases), "observable_state_checks":len(cases), "moment_checks": 0, "secular_law_checks": 0,
             "cut_bound_checks": 0, "coarse_line_bound_checks": 0, "pair_controls": 0}
    moment_rows = []
    for offsets, edges in cases:
        n = len(offsets)
        h, o = model(offsets, edges)
        law = spectral(h, o)
        # Independent observable-state vectorization identity (pair order -> A,B).
        phi = np.array([1.,0.,0.,1.])/math.sqrt(2)
        raised = np.array([0.,1.,0.,0.])
        pair_state = np.zeros(4**n)
        for chosen in range(n):
            term = np.array([1.])
            for site in range(n):
                term = np.kron(term, raised if site == chosen else phi)
            pair_state += term/math.sqrt(n)
        axes = list(range(0,2*n,2))+list(range(1,2*n,2))
        reordered = pair_state.reshape([2]*(2*n)).transpose(axes).ravel()
        close(reordered, o.ravel()/np.linalg.norm(o), "raising observable preparation")
        sigma2 = sum(d*d for d in offsets) / n
        kappa = sum(j*j*(offsets[i]-offsets[k])**2 for i,k,j in edges) / (2*n)
        target = [1., 0., sigma2, sum(d**3 for d in offsets)/n,
                  sum(d**4 for d in offsets)/n + kappa]
        a = o.copy()
        for order in range(5):
            trace_moment = np.vdot(o, a) / np.vdot(o, o)
            close(trace_moment, target[order], "commutator moment")
            close(np.dot(law[1], law[0]**order), target[order], "spectral moment")
            a = h @ a - a @ h
            count["moment_checks"] += 1
        moment_rows.append({"n": n, "variance": sigma2, "coupling_fourth_moment_term": kappa})
        # Exact secular sampler: a uniformly chosen spin, independent neighbor signs.
        hz, _ = model(offsets, edges, secular=True)
        analytic_frequencies = []
        for i in range(n):
            other = [j for j in range(n) if j != i]
            for signs in itertools.product((-1, 1), repeat=n-1):
                s = dict(zip(other, signs))
                omega = offsets[i]
                for j,k,coupling in edges:
                    if i == j:
                        omega += coupling*s[k]/2
                    elif i == k:
                        omega += coupling*s[j]/2
                analytic_frequencies.append(omega)
        analytic_law = (np.array(analytic_frequencies),
                        np.ones(len(analytic_frequencies))/len(analytic_frequencies))
        cut_h, _ = model(offsets, [])
        diff_e = np.linalg.eigvalsh(h-cut_h)
        diameter = float(diff_e[-1]-diff_e[0])
        close_line = (np.array([0.]), np.array([1.]))
        for gamma in (.25, 1., 3.):
            full = bins(law, gamma)
            close(bins(spectral(hz, o), gamma), bins(analytic_law, gamma), "secular sampler law")
            count["secular_law_checks"] += 1
            bound = min(1., diameter/(2*gamma))
            require(tv(full, bins(spectral(cut_h, o), gamma)) <= bound + TOL, "resolvent TV bound")
            count["cut_bound_checks"] += 1
            bound = min(1., 3*math.sqrt(3)*sigma2/(8*math.pi*gamma**2))
            require(tv(full, bins(close_line, gamma)) <= bound + TOL, "coarse-line bound")
            count["coarse_line_bound_checks"] += 1
    # Exact two-spin solution and its finite-linewidth secular error bound.
    for delta, coupling in ((1.,1.), (5.,1.), (10.,-2.), (0.,1.)):
        h, o = model([-delta/2, delta/2], [(0,1,coupling)])
        radius = math.hypot(delta, coupling)
        inner, outer = (radius-coupling)/2, (radius+coupling)/2
        pair_law = (np.array([-inner,inner,-outer,outer]),
                    np.array([1+coupling/radius]*2+[1-coupling/radius]*2)/4)
        for gamma in (.2, 1.):
            full = bins(spectral(h,o), gamma)
            close(full, bins(pair_law,gamma), "two-spin line law")
            if delta > abs(coupling):
                hz,_ = model([-delta/2,delta/2],[(0,1,coupling)],secular=True)
                bound = abs(coupling)/(2*radius)+(radius-delta)/(2*math.pi*gamma)
                require(tv(full,bins(spectral(hz,o),gamma)) <= bound+TOL, "two-spin weak-coupling bound")
            count["pair_controls"] += 1
    # Two disconnected components: the collective spectrum is a size-weighted mixture.
    ha,oa=model([-.7,.7],[(0,1,1.2)])
    hb,ob=model([.2],[])
    h=np.kron(ha,np.eye(2))+np.kron(np.eye(4),hb)
    o=np.kron(oa,np.eye(2))+np.kron(np.eye(4),ob)
    fa,wa=spectral(ha,oa); fb,wb=spectral(hb,ob)
    close(bins(spectral(h,o),.4),bins((np.r_[fa,fb],np.r_[2*wa/3,wb/3]),.4),"component mixture")
    # General complex H checks the required transpose in the doubled generator.
    h=np.array([[.2, .3+.7j],[.3-.7j,-.4]])
    o=np.array([[0.,1.],[0.,0.]],complex)
    liouvillian=np.kron(h,np.eye(2))-np.kron(np.eye(2),h.T)
    close(liouvillian@o.ravel(),(h@o-o@h).ravel(),"transpose convention")
    wrong=np.kron(h,np.eye(2))-np.kron(np.eye(2),h)
    require(np.linalg.norm((wrong-liouvillian)@o.ravel())>.1,"negative transpose control")
    # A geometric clock gives a truncated Poisson (wrapped Cauchy) kernel.
    clock_cases = []
    phase_grid = np.linspace(-math.pi, math.pi, 8192, endpoint=False)
    for r, length in ((.4, 8), (.8, 16), (.95, 32)):
        j = np.arange(length)
        normalization = math.sqrt((1-r*r)/(1-r**(2*length)))
        amplitudes = normalization*r**j
        m = int(math.log2(length))
        bit_product = np.array([math.prod((r**(2**k) if (v>>k)&1 else 1.) /
                              math.sqrt(1+r**(2**(k+1))) for k in range(m))
                              for v in range(length)])
        close(bit_product, amplitudes, "product geometric clock")
        phase, offset = .371, .217/length
        angles = 2*math.pi*np.arange(length)/length+offset-phase
        amplitude_direct = np.exp(1j*angles[:,None]*j)@amplitudes/math.sqrt(length)
        probability_closed = (1-r*r)/(length*(1-r**(2*length))) * abs(
            (1-(r*np.exp(1j*angles))**length)/(1-r*np.exp(1j*angles)))**2
        close(abs(amplitude_direct)**2, probability_closed, "finite clock measurement")
        close(probability_closed.sum(), 1, "offset measurement normalization")
        theta = phase_grid-phase
        density_infinite = (1-r*r)/(2*math.pi*abs(1-r*np.exp(1j*theta))**2)
        density_finite = density_infinite*abs(1-r**length*np.exp(1j*length*theta))**2/(1-r**(2*length))
        close(density_finite.mean()*2*math.pi, 1, "dithered kernel normalization")
        measured_tv = float(np.abs(density_finite-density_infinite).mean()*math.pi)
        upper = min(1.,r**length/(1-r**length))
        require(measured_tv <= upper+TOL, "geometric truncation bound")
        clock_cases.append({"r":r,"length":length,"truncation_TV_bound":upper})
    # The QPE uniform clock does not automatically give the specified linewidth.
    r, length = .8, 16
    j = np.arange(length)
    amplitude = np.exp(1j*phase_grid[:,None]*j)@np.ones(length)/math.sqrt(length)
    uniform_density = abs(amplitude)**2/(2*math.pi)
    poisson_density = (1-r*r)/(2*math.pi*abs(1-r*np.exp(1j*phase_grid))**2)
    require(np.abs(uniform_density-poisson_density).mean()*math.pi > .05,
            "uniform-clock mismatch negative control")
    # Exact scalar Cauchy tails validate the stated all-center alias upper bound.
    for gamma in (.1,1.):
        support=3.; margin=5*gamma; half_range=support+margin
        for center in (-support,0.,support):
            tail=1-(math.atan((half_range-center)/gamma)-math.atan((-half_range-center)/gamma))/math.pi
            require(tail <= 2*gamma/(math.pi*margin)+TOL,"alias tail bound")
    print(json.dumps({"status":"pass", "scope":"Selected finite matrix identities; no NMR fit, climate model, hardware, or timing experiment.",
                      "arithmetic":"NumPy complex128, tolerance 2e-10; inequalities also proved analytically in the note", **count,
                      "geometric_clock_controls":clock_cases,"uniform_clock_mismatch_detected":True,
                      "alias_controls":6,"component_mixture_checked":True,"complex_transpose_negative_control_checked":True,
                      "moment_rows":moment_rows},indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
