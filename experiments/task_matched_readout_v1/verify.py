#!/usr/bin/env python3
"""Exact regression and Gaussian-noise controls, not a sensor experiment.

Python 3.10+, SymPy, NumPy. No network or file writes. The proof and application
scope are in TASK_MATCHED_READOUT_02.md. No random samples or optical circuits.
"""
from __future__ import annotations
import json
import math
import sys
import numpy as np
import sympy as s

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def compression(h: s.Matrix, b: s.Matrix):
    if h.cols != 1 or h.rows % 2 or b.rows != h.rows or b.rank() != b.cols:
        raise ValueError('Need paired real coordinates and independent nuisance columns.')
    r = h - b * (b.T*b).inv() * b.T*h
    info = s.simplify((r.T*r)[0])
    if info <= 0:
        raise ValueError('Target lies in nuisance span.')
    u = s.zeros(h.rows//2, h.rows)
    w = s.zeros(h.rows//2, 1)
    for j in range(h.rows//2):
        pair = r[2*j:2*j+2, 0]
        w[j] = s.sqrt((pair.T*pair)[0])
        if w[j]:
            u[j, 2*j] = pair[0]/w[j]
            u[j, 2*j+1] = pair[1]/w[j]
        else:
            u[j, 2*j] = 1
    require(b.T*r == s.zeros(b.cols,1), 'Residual must remove every nuisance.')
    require(s.simplify((r.T*h)[0]-info) == 0, 'Target gain.')
    require(s.simplify(u.T*w-r) == s.zeros(h.rows,1), 'Single-quadrature synthesis.')
    require(s.simplify(u*u.T) == s.eye(h.rows//2), 'Independent unit readout rows.')
    require(s.simplify((w.T*w)[0]-info) == 0, 'Noise variance preservation.')
    return r, info, u, w


def sq(e: float) -> float:
    return 1/(math.sqrt(e+1)+math.sqrt(e))**2


def noises(e: float, eta_s: float, eta_r: float):
    if not all(math.isfinite(x) for x in (e,eta_s,eta_r)) or e < 0 or not 0 < eta_s <= 1 or not 0 <= eta_r <= 1:
        raise ValueError('Finite nonnegative energy and physical pure-loss efficiencies required.')
    c, sh = e+1, math.sqrt(e*(e+2))
    loss = (1-eta_s)/(2*eta_s)
    bell = (c*(eta_s+eta_r)+2-eta_s-eta_r-2*math.sqrt(eta_s*eta_r)*sh)/(2*eta_s)
    equal_sensor = loss+sq(e/2)/2
    equal_total = loss+sq(e)/2
    # Independent 4D covariance calculation of the two commuting Bell outputs.
    v = np.array([[c,0,sh,0],[0,c,0,-sh],[sh,0,c,0],[0,-sh,0,c]],float)/2
    a = np.diag([math.sqrt(eta_s)]*2+[math.sqrt(eta_r)]*2)
    after = a@v@a+(np.eye(4)-a@a)/2
    readout = np.array([[1,0,-1,0],[0,1,0,1]],float)/math.sqrt(eta_s)
    require(np.allclose(readout@after@readout.T, bell*np.eye(2),atol=2e-12), 'Loss covariance formula.')
    t = math.sqrt(eta_r/eta_s)
    lower = loss+1/(2*c)
    remainder = c*(t-sh/c)**2/2+(1-eta_r)/(2*eta_s)
    require(abs(bell-lower-remainder) < 2e-12, 'Unequal-loss square identity.')
    require(equal_total <= equal_sensor+1e-12 <= lower+2e-12 <= bell+3e-12, 'Task-specific homodyne comparison.')
    return {'squeezed_photons_total_budget':e, 'signal_efficiency':eta_s,
            'reference_efficiency':eta_r, 'Bell_noise_per_coordinate':round(bell,12),
            'homodyne_equal_sensor_photons':round(equal_sensor,12),
            'homodyne_equal_total_budget':round(equal_total,12)}


def main():
    # Rational points on a scattered-light circle; not an experimental waveform.
    h = s.Matrix([1,0,2,0,-1,0,1,0])
    b1 = s.Matrix([0,1,s.Rational(3,5),s.Rational(4,5),1,0,-s.Rational(3,5),s.Rational(4,5)])
    b2 = b1.multiply_elementwise(s.Matrix([j//2-1 for j in range(8)]))
    b = s.Matrix.hstack(b1,b2)
    r, info, u, w = compression(h,b)
    require(info == s.Rational(154,25), 'Exact information control.')
    theta, beta1, beta2 = s.symbols('theta beta1 beta2', real=True)
    mean = h*theta+b*s.Matrix([beta1,beta2])
    require(s.simplify((w.T*u*mean)[0]/info-theta) == 0, 'Unbiased for all nuisance amplitudes.')
    variance = s.symbols('variance', positive=True)
    require(s.simplify((w.T*(variance*s.eye(4))*w)[0]/info**2-variance/info) == 0, 'Exact variance.')
    # Rotating only the local oscillator, without its squeezed axis, is not free.
    c, sh, t = s.symbols('c sh t',real=True,nonzero=True)
    diff = c*(1+t*t)/2-t*sh-c*(t-sh/c)**2/2-1/(2*c)
    require(s.simplify(diff-(c*c-sh*sh-1)/(2*c)) == 0, 'Conditional noise decomposition.')
    rows = [noises(*args) for args in [(0,1,1),(2,1,1),(2,.8,.8),(2,.8,1),(10,.8,1),(10,.8,.5)]]
    # A calibrated linear nuisance projection need not work after a phase drift.
    amp, drift = 10., .01
    bias = amp*math.sin(drift)
    require(bias > .099 and bias <= amp*abs(drift), 'Unpriced-calibration negative control.')
    # One scalar record cannot subsequently estimate both independent quadratures.
    require(u.rank() < u.cols, 'Not an informationally complete record.')
    bad = [lambda: noises(-1,1,1), lambda: noises(1,0,1), lambda: noises(1,1,1.1),
           lambda: noises(float('nan'),1,1), lambda: compression(b1,b),
           lambda: compression(h,s.Matrix.hstack(b1,b1))]
    for case in bad:
        try: case()
        except ValueError: continue
        raise AssertionError('Invalid input accepted.')
    print(json.dumps({'status':'pass',
        'scope':'Exact finite regression identities and analytic Gaussian covariance arithmetic; no waveform fit, unknown-nuisance pilot, device, or performance run.',
        'exact_regression':{'time_modes':4,'nuisance_columns':2,'residual':list(map(str,r)),
                            'squared_residual_norm':str(info),'exact_checks_passed':True},
        'noise_rows':rows,'phase_drift_negative_control':{'amplitude':amp,'radians':drift,'bias':bias},
        'invalid_inputs_rejected':len(bad),
        'limits':'Noise rows assume pure loss, stable known phases and no back-action; sensing and reference squeezed energy are counted. Homodyne is squeezed but unentangled, not classical light.'},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
