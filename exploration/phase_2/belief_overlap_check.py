"""Coherent return tests as one-sided distribution certificates.

Small dense-state identities only. No general state-preparation compiler,
quantum execution, training, native inference comparison, or advantage claim.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np


def preparation(vector: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    n=len(vector)
    trial=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    trial[:,0]=vector
    q,_=np.linalg.qr(trial)
    q[:,0]*=np.vdot(q[:,0],vector)
    if np.max(abs(q[:,0]-vector))>1e-12 or np.max(abs(q.conj().T@q-np.eye(n)))>1e-12:
        raise AssertionError('Dense preparation control failed.')
    return q


def diagonal_law(vector: np.ndarray, output_size: int) -> np.ndarray:
    return np.sum(abs(vector.reshape(output_size,-1))**2,axis=1)


def tv(p,q):
    return float(np.sum(abs(p-q))/2)


def run() -> dict:
    rng=np.random.default_rng(2026092609)
    count=0; max_circuit_error=0.; max_bound_excess=0.
    for n in (4,8,16):
        for _ in range(32):
            u=rng.normal(size=n)+1j*rng.normal(size=n)
            u/=np.linalg.norm(u)
            v=rng.normal(size=n)+1j*rng.normal(size=n)
            v/=np.linalg.norm(v)
            a=preparation(u,rng); b=preparation(v,rng)
            f=float(abs(np.vdot(v,u))**2)
            observed=float(abs((b.conj().T@a)[0,0])**2)
            max_circuit_error=max(max_circuit_error,abs(f-observed))
            # Compare both complete output labels and a half-size marginal.
            for output_size in (n,n//2):
                delta=tv(diagonal_law(u,output_size),diagonal_law(v,output_size))
                excess=delta-math.sqrt(max(0.,1-f))
                max_bound_excess=max(max_bound_excess,excess)
                if excess>1e-12:raise AssertionError('Measurement distance exceeded pure-state bound.')
                count+=1
    # Different reversible generators, same classical marginal law.
    identity=np.array([1,0,0,1],dtype=complex)/math.sqrt(2)
    complement=np.array([0,1,1,0],dtype=complex)/math.sqrt(2)
    garbage_f=float(abs(np.vdot(identity,complement))**2)
    # Ordering is random tape then output: marginalize first register.
    p=np.sum(abs(identity.reshape(2,2))**2,axis=0)
    q=np.sum(abs(complement.reshape(2,2))**2,axis=0)
    if garbage_f != 0 or tv(p,q)>1e-14:
        raise AssertionError('Same-law different-workspace control failed.')
    plus=np.array([1,1],dtype=complex)/math.sqrt(2)
    minus=np.array([1,-1],dtype=complex)/math.sqrt(2)
    if abs(np.vdot(plus,minus))>1e-14 or tv(abs(plus)**2,abs(minus)**2)>1e-14:
        raise AssertionError('Phase-only negative control failed.')
    # Tight two-point example: TV=t while squared fidelity=1-t^2.
    t=.1
    p=np.array([(1+t)/2,(1-t)/2]);q=p[::-1].copy()
    f=float(np.dot(np.sqrt(p),np.sqrt(q))**2)
    if abs(f-(1-t*t))>1e-12 or abs(tv(p,q)-t)>1e-12:
        raise AssertionError('Tight fidelity-distance example failed.')
    confidence=[]
    for epsilon in (.1,.05):
        delta=.05
        m=math.ceil(math.log(delta)/math.log1p(-epsilon*epsilon))
        if (1-epsilon*epsilon)**m>delta+1e-13:
            raise AssertionError('All-return test false-accept bound failed.')
        confidence.append(dict(tv_tolerance=epsilon,false_accept_probability=delta,
                               all_zero_returns_required=m,
                               exact_upper_bound_on_bad_state_acceptance=(1-epsilon*epsilon)**m))
    return dict(scope='Finite pure-state/measurement identities, not a complete inference or certification advantage.',
      numpy_version=np.__version__,seed=2026092609,
      random_preparation_pairs=96,output_distribution_bound_checks=count,
      maximum_return_probability_error=max_circuit_error,
      maximum_positive_distance_bound_excess=max_bound_excess,
      tight_two_label_example=dict(p=p.tolist(),q=q.tolist(),total_variation=tv(p,q),
                                   squared_fidelity=f,return_failure_probability=1-f),
      workspace_control=dict(generators='g0(z)=z and g1(z)=1-z; retain the uniform input tape.',
                             identical_output_probabilities=['1/2','1/2'],
                             full_state_squared_overlap=0,
                             warning='Low overlap need not mean different output distributions.'),
      phase_control=dict(states='|+> and |->',output_laws_equal=True,squared_overlap=0),
      all_return_certificate=confidence,
      caveats=['Ideal pure coherent preparation with common output labeling and accessible inverse.',
               'Gate synthesis, statistical failures, source/model error, ancillas and postselection preparation costs are separate.',
               'The one-sided certificate can reject good models because it is sensitive to representation.',
               'Classical competitors may use source code, exact probabilities, likelihood ratios or structure, not only samples.'])


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    report=run()
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(report,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps(report,indent=2,sort_keys=True))
