"""Finite checks of unitary proposal capacity and random-tape reweighting.

This is not an LLM experiment or evidence of quantum advantage. No generative
model is trained and no large circuit is simulated. The many-to-one generator
is explicitly supplied; exact fractions independently check its output law.
Requires NumPy. Reports are created exclusively, never overwritten.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import numpy as np


def paired_proposal(u: np.ndarray) -> np.ndarray:
    n = len(u)
    if not np.allclose(u.conj().T @ u, np.eye(n), atol=1e-12):
        raise ValueError('Expected a unitary matrix.')
    f = np.abs(u.T)**2  # row x, column y
    return (f + f.T)/2


def metropolis(q: np.ndarray, weights: np.ndarray) -> np.ndarray:
    weights = np.asarray(weights, dtype=float)
    if np.any(weights <= 0) or q.shape != (len(weights), len(weights)):
        raise ValueError('This diagnostic requires strictly positive weights.')
    if not np.allclose(q, q.T, atol=1e-12) or not np.allclose(q.sum(axis=1), 1, atol=1e-12):
        raise ValueError('Expected a symmetric stochastic proposal.')
    trans = q * np.minimum(1., weights[None, :] / weights[:, None])
    np.fill_diagonal(trans, 0.)
    np.fill_diagonal(trans, 1. - trans.sum(axis=1))
    return trans


def random_unitary(rng: np.random.Generator, n: int) -> np.ndarray:
    z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    q, r = np.linalg.qr(z)
    phase = np.diag(r)
    phase = phase/np.abs(phase)
    return q * phase


def spectral_gap(trans: np.ndarray, pi: np.ndarray) -> float:
    root = np.sqrt(pi)
    symmetric = root[:,None] * trans / root[None,:]
    if np.max(np.abs(symmetric-symmetric.T)) > 1e-11:
        raise AssertionError('Detailed balance failed.')
    vals = np.linalg.eigvalsh((symmetric+symmetric.T)/2)
    return float(1.-vals[-2])  # ordinary reversible gap, not absolute gap


def run() -> dict:
    rng = np.random.default_rng(2026092604)
    capacity_checks = 0
    greatest_one_step_ratio = 0.
    greatest_gap_ratio = 0.
    for n in (8,16,32):
        for marked in (1,2):
            for _ in range(12):
                q = paired_proposal(random_unitary(rng,n))
                upper = marked/(n-marked)
                incoming = float(q[marked:,:marked].sum()/(n-marked))
                if incoming > upper+1e-12:
                    raise AssertionError('Column-capacity bound violated.')
                weights = np.ones(n)*marked
                weights[:marked] = n-marked  # exactly half target mass in each set
                pi = weights/weights.sum()
                gap = spectral_gap(metropolis(q,weights),pi)
                gap_upper = 2.*marked/(n-marked)
                if gap > gap_upper+1e-11:
                    raise AssertionError('Rayleigh gap bound violated.')
                greatest_one_step_ratio = max(greatest_one_step_ratio,incoming/upper)
                greatest_gap_ratio = max(greatest_gap_ratio,gap/gap_upper)
                capacity_checks += 1
    uniform_example=[]
    for n in (8,16,32,64):
        q = np.ones((n,n))/n
        w = np.ones(n); w[0] = n-1
        gap = spectral_gap(metropolis(q,w),w/w.sum())
        if abs(gap-2/n) > 1e-12:
            raise AssertionError('Uniform-proposal exact gap failed.')
        uniform_example.append(dict(states=n,ordinary_gap=gap,exact_gap=str(Fraction(2,n)),
                                    universal_gap_upper=2/(n-1)))
    # Same initial basis probabilities, different quantum coherence.
    n=16
    plus = np.ones(n)/np.sqrt(n)
    oracle = np.eye(n); oracle[0,0]=-1.
    iterate=(2*np.outer(plus,plus)-np.eye(n)) @ oracle
    coherent=plus.astype(complex)
    mixed=np.eye(n,dtype=complex)/n
    for _ in range(3):
        coherent=iterate@coherent
        mixed=iterate@mixed@iterate.conj().T
    coherent_hit=float(abs(coherent[0])**2)
    mixed_hit=float(mixed[0,0].real)
    expected=float(np.sin(7*np.arcsin(1/np.sqrt(n)))**2)
    if abs(coherent_hit-expected)>1e-12 or abs(mixed_hit-1/n)>1e-12:
        raise AssertionError('Coherent versus mixed-state control failed.')
    # Explicit finite generator: 16 random tapes produce four objects.
    multiplicities=[8,4,2,2]
    generator=np.repeat(np.arange(4),multiplicities)
    scores=np.array([1,3,2,6],dtype=float)
    p0=[Fraction(c,16) for c in multiplicities]
    target_unnorm=[p*int(s) for p,s in zip(p0,scores)]
    target=[p/sum(target_unnorm) for p in target_unnorm]
    wrong_unnorm=[p*p*int(s) for p,s in zip(p0,scores)]
    wrong=[p/sum(wrong_unnorm) for p in wrong_unnorm]
    tv=sum(abs(p-q) for p,q in zip(target,wrong))/2
    max_stationarity=0.; max_output_error=0.
    for _ in range(12):
        q=paired_proposal(random_unitary(rng,16))
        for double_prior in (False,True):
            w=scores[generator]
            if double_prior:
                w=w*np.array([float(p0[int(x)]) for x in generator])
            pi=w/w.sum()
            trans=metropolis(q,w)
            residual=float(np.max(np.abs(pi@trans-pi)))
            max_stationarity=max(max_stationarity,residual)
            marginal=np.bincount(generator,weights=pi,minlength=4)
            expected=np.array([float(p) for p in (wrong if double_prior else target)])
            max_output_error=max(max_output_error,float(np.max(np.abs(marginal-expected))))
    if max_stationarity>1e-12 or max_output_error>1e-12 or tv!=Fraction(2,9):
        raise AssertionError('Lifted-target check failed.')
    return dict(scope='Finite algebra diagnostics only; no LLM, learned proposal, quantum hardware, or speedup.',
        numpy_version=np.__version__,seed=2026092604,
        capacity=dict(random_unitaries=capacity_checks,
                      maximum_incoming_over_bound=greatest_one_step_ratio,
                      maximum_gap_over_bound=greatest_gap_ratio,
                      uniform_proposal_example=uniform_example),
        coherence_control=dict(dimension=n,iterations=3,coherent_success=coherent_hit,
                               incoherent_success=mixed_hit,scope='Known Grover control, not an innovation.'),
        random_tape=dict(tapes=16,objects=4,multiplicities=multiplicities,
                         scores=[int(x) for x in scores],base_law=list(map(str,p0)),
                         correct_output_law=list(map(str,target)),
                         incorrectly_double_weighted_law=list(map(str,wrong)),
                         double_weighting_total_variation=str(tv),
                         proposal_matrices_checked=12,
                         maximum_stationarity_residual=max_stationarity,
                         maximum_marginal_residual=max_output_error))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite an existing report.')
    result=run()
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps(result,indent=2,sort_keys=True))
