"""Finite algebra checks: normalized quantum proposals for classical target weights.

This does not run an LLM, a quantum device, or a performance benchmark.
Dense small unitaries test identities, not a scalable proposal construction.
Only NumPy is required. Existing reports are never overwritten.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
import numpy as np


def metropolis(proposal: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Target-ratio acceptance, justified only for a symmetric proposal.

    The function intentionally permits asymmetric proposals for negative controls.
    Positive-weight states form the allowed support; zero-weight states are never
    entered from it. A chain should start in the positive-weight support.
    """
    q = np.asarray(proposal, dtype=float)
    w = np.asarray(weights, dtype=float)
    n = len(w)
    if q.shape != (n, n) or np.any(w < 0) or not w.sum() > 0:
        raise ValueError('Invalid dimensions or nonnegative target weights.')
    if np.min(q) < -1e-12 or not np.allclose(q.sum(axis=1), 1, atol=1e-12):
        raise ValueError('Proposal is not row stochastic.')
    t = np.zeros_like(q)
    for x in range(n):
        if w[x] > 0:
            for y in range(n):
                if y != x:
                    t[x, y] = q[x, y] * min(1.0, w[y]/w[x])
        t[x, x] = 1.0-t[x].sum()
    return t


def errors(q: np.ndarray, w: np.ndarray) -> dict:
    pi = w / w.sum()
    t = metropolis(q, w)
    flow = pi[:, None] * t
    return dict(proposal_asymmetry=float(np.max(np.abs(q-q.T))),
                stationarity_residual=float(np.max(np.abs(pi @ t-pi))),
                detailed_balance_residual=float(np.max(np.abs(flow-flow.T))),
                transition=t.tolist())


def run() -> dict:
    rng = np.random.default_rng(20260926)
    largest = dict(unitarity=0., inverse_identity=0., row_normalization=0.,
                   symmetry=0., stationarity=0., detailed_balance=0.)
    tests = 0
    for n in (2, 4, 8):
        for _ in range(16):
            z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
            u, _ = np.linalg.qr(z)
            # Row convention q[x,y] means next y given current x.
            forward = np.abs(u.T)**2
            reverse = np.abs(u.conj())**2
            q = (forward+reverse)/2
            largest['unitarity'] = max(largest['unitarity'],float(np.max(abs(u.conj().T@u-np.eye(n)))))
            largest['inverse_identity'] = max(largest['inverse_identity'],float(np.max(abs(reverse-forward.T))))
            largest['row_normalization'] = max(largest['row_normalization'],float(np.max(abs(q.sum(axis=1)-1))))
            largest['symmetry'] = max(largest['symmetry'],float(np.max(abs(q-q.T))))
            for constrained in (False, True):
                w = np.exp(rng.uniform(-5, 5, n))
                if constrained:
                    w[rng.choice(n, size=n//2, replace=False)] = 0.
                r = errors(q, w)
                largest['stationarity'] = max(largest['stationarity'],r['stationarity_residual'])
                largest['detailed_balance'] = max(largest['detailed_balance'],r['detailed_balance_residual'])
                tests += 1
    if max(largest.values()) > 1e-11:
        raise AssertionError('Forward/inverse proposal identity failed.')

    # A permutation is unitary but its measured transition need not be symmetric.
    cycle = np.zeros((3,3))
    for x in range(3):
        cycle[x,(x+1)%3] = 1.
    w = np.array([1.,2.,4.])
    wrong = errors(cycle,w)
    correct = errors((cycle+cycle.T)/2,w)
    actual_wrong_stationary = np.array([1.,1.,4.])/6
    if not np.allclose(actual_wrong_stationary @ metropolis(cycle,w),actual_wrong_stationary):
        raise AssertionError('Analytic negative-control stationary law failed.')
    if wrong['stationarity_residual'] < .1 or correct['stationarity_residual'] > 1e-12:
        raise AssertionError('Unitarity versus symmetry control failed.')

    # Each U_x is symmetric/involutive, but using a different U_x for each current
    # state x yields the directed cycle again. Thus adaptation is not free.
    state_dependent = np.zeros((3,3))
    for x in range(3):
        swap = np.eye(3)
        y = (x+1)%3
        swap[[x,y]] = swap[[y,x]]
        if not np.array_equal(swap,swap.T):
            raise AssertionError('Involution construction failed.')
        state_dependent[x] = np.abs(swap[:,x])**2
    if not np.array_equal(state_dependent,cycle):
        raise AssertionError('State-dependent negative control failed.')

    # Two-token toy. A/B chosen uniformly. Terminal-valid probabilities .99/.01.
    # Both first-token options remain completable; hard local masking leaves .5/.5.
    valid_given_first = [Fraction(99,100),Fraction(1,100)]
    joint = [Fraction(1,2)*p for p in valid_given_first]
    conditional = [p/sum(joint) for p in joint]
    masked = [Fraction(1,2)]*2
    tv = sum(abs(a-b) for a,b in zip(conditional,masked))/2
    if tv != Fraction(49,100):
        raise AssertionError('Global-conditioning toy failed.')

    return dict(scope='Algebraic controls only: no quantum speedup, LLM execution, training, mixing-time, or hardware claim.',
        seed=20260926,numpy_version=np.__version__,unitaries=48,target_cases=tests,
        maximum_residuals=largest,
        asymmetric_unitary_control=dict(target=[str(Fraction(int(x),7)) for x in w],
            wrong_stationary=['1/6','1/6','2/3'],wrong=wrong,paired=correct),
        state_dependent_control=dict(proposal=state_dependent.tolist(),
            warning='Per-current-state choice invalidates forward/inverse symmetrization in general.'),
        constrained_generation_control=dict(exact_first_token=[str(x) for x in conditional],
            locally_masked_first_token=[str(x) for x in masked],total_variation=str(tv)))


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite an existing observation file.')
    report=run()
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(report,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps(report,indent=2,sort_keys=True))
