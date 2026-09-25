"""Sanity checks for reusable thermal-flux event records, not a collision solver.

Requires NumPy and SciPy. No quantum dynamics is simulated. The response law
is an explicitly supplied synthetic bounded function. Reported finite-grid
errors are observations, not uniform confidence certificates.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad

C = 4.0 * math.exp(-2.0)


def density(e, theta):
    e = np.asarray(e, dtype=float)
    return e / theta**2 * np.exp(-e/theta)


def envelope(e, low, high):
    e = np.asarray(e, dtype=float)
    optimum_theta = np.clip(e/2.0, low, high)
    return density(e, optimum_theta)


def norm(low, high):
    if not 0 < low <= high:
        raise ValueError('Require 0 < low <= high.')
    return 1.0 + C * math.log(high/low)


def proposal(e, low, high):
    return envelope(e, low, high) / norm(low, high)


def draw_proposal(rng, count, low, high):
    """Exact continuous-distribution construction up to floating-point arithmetic."""
    if count < 1:
        raise ValueError('Positive count required.')
    normalizer = norm(low, high)
    left = 1.0-3.0*math.exp(-2.0)
    middle = C*math.log(high/low)
    sample = []
    proposals = 0
    for _ in range(count):
        pick = rng.random()*normalizer
        if pick < left:
            while True:
                x = rng.gamma(2.0, low)
                proposals += 1
                if x < 2*low:
                    break
        elif pick < left+middle:
            x = 2*low*math.exp(rng.random()*math.log(high/low))
            proposals += 1
        else:
            while True:
                x = rng.gamma(2.0, high)
                proposals += 1
                if x >= 2*high:
                    break
        sample.append(x)
    return np.asarray(sample), proposals


def cdf(e, theta):
    z=e/theta
    return -math.expm1(-z)-z*math.exp(-z)


BANDS=((.7,.8,.45),(4.0,5.0,.65),(20.0,25.0,.30))


def synthetic_response(e):
    ans = np.full_like(e, .05)
    for a,b,weight in BANDS:
        ans += weight*((e>=a)&(e<=b))
    return ans


def exact_mean(theta):
    return .05+sum(w*(cdf(b,theta)-cdf(a,theta)) for a,b,w in BANDS)


def check():
    low,high=.1,10.0
    W=norm(low,high)
    mass=sum(quad(lambda e: float(proposal(e,low,high)),a,b,
                  epsabs=1e-12)[0] for a,b in ((0,2*low),(2*low,2*high),(2*high,np.inf)))
    if abs(mass-1)>1e-10:
        raise AssertionError('Proposal normalization failed.')
    energies=np.geomspace(1e-8,1000,512)
    temps=np.geomspace(low,high,129)
    # Analytic maximizer theta=clip(E/2,low,high) must dominate each test density.
    max_excess=max(float(np.max(density(energies,t)-envelope(energies,low,high))) for t in temps)
    if max_excess>1e-12:
        raise AssertionError('Envelope violated.')
    scaled=np.max(np.abs(proposal(energies*7.3,low*7.3,high*7.3)*7.3-proposal(energies,low,high)))
    if scaled>1e-10:
        raise AssertionError('Energy-unit scaling failed.')
    # Independently verify exact response integrals (piecewise quadrature).
    bounds=[0]+sorted({b for a,c,_ in BANDS for b in (a,c)})+[np.inf]
    integration_error=0.0
    for t in temps[::16]:
        value=sum(quad(lambda e: float(density(e,t)*synthetic_response(np.asarray(e))),
                       a,b,epsabs=1e-11)[0] for a,b in zip(bounds,bounds[1:]))
        integration_error=max(integration_error,abs(value-exact_mean(t)))
    if integration_error>1e-8:
        raise AssertionError('Analytic rate integral failed.')
    rng=np.random.default_rng(20260925)
    es,proposals=draw_proposal(rng,32768,low,high)
    ys=(rng.random(len(es))<synthetic_response(es)).astype(float)
    qs=proposal(es,low,high)
    records=[]
    for m in (1024,8192,32768):
        estimates=[]
        max_weight=0.0
        for t in temps:
            weights=density(es[:m],t)/qs[:m]
            max_weight=max(max_weight,float(weights.max()))
            estimates.append(float(np.mean(weights*ys[:m])))
        truth=np.array([exact_mean(t) for t in temps])
        error=np.abs(np.asarray(estimates)-truth)
        if max_weight>W+1e-10:
            raise AssertionError('Weight bound failed.')
        # A later mixture inherits the simultaneous endpoint errors by linearity.
        mix=(.3*estimates[7]+.7*estimates[114])
        mix_truth=.3*truth[7]+.7*truth[114]
        if abs(mix-mix_truth)>error.max()+1e-12:
            raise AssertionError('Mixture bound failed.')
        records.append(dict(samples=m,test_temperatures=len(temps),
            maximum_grid_error=float(error.max()),
            rms_grid_error=float(np.sqrt(np.mean(error**2))),
            largest_observed_importance_weight=max_weight,
            example_mixture_error=float(abs(mix-mix_truth))))
    eps,delta=.05,.05
    J=math.ceil(16*math.log(high/low)/eps)+1
    bound=math.ceil(10*W/eps**2*math.log(2*J/delta))
    # Check the numerical constants used in the analytic uniform interpolation proof.
    coeff=(math.exp(1/8)-1)+math.exp(1/8)*(C/16+.5)
    if coeff>=1:
        raise AssertionError('Uniform interpolation constant not sufficient.')
    return dict(scope='Synthetic event sampler; no quantum/scattering calculation or advantage.',
        numpy_version=np.__version__,seed=20260925,thermal_scale_range=[low,high],
        normalizer=W,numerical_proposal_mass=mass,
        envelope_grid_excess=max_excess,scale_identity_error=float(scaled),
        exact_integral_check_error=integration_error,
        number_of_draws=32768,proposal_primitive_draws=proposals,
        records=records,illustrative_uniform_bound=dict(epsilon=eps,delta=delta,
            grid_points=J,sufficient_independent_samples=bound,
            observed_errors_are_not_this_certificate=True),
        window_weight_bounds={str(r):1+C*math.log(r) for r in (1,10,100,1000)},
        next_requirement='A justified bounded event estimator and matched microscopic classical/quantum cost.')


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True,type=Path)
    args=p.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite an existing report.')
    result=check()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))
