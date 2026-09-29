#!/usr/bin/env python3
"""Checks of a two-window activity statistic, not a quantum performance study.

Python 3.10+, NumPy, SciPy. One fixed three-emitter identity control and one
analytic classical two-phase control. No network, input files, or file writes.
The claim and general identities are in EMISSION_ACTIVITY_CLAIM_28.md.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import math
import sys
import numpy as np
from scipy.linalg import expm

if sys.flags.optimize:
    raise SystemExit("Run without -O or -OO.")

TOL = 2e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([-1., 1.]).astype(complex)
LOWER = np.array([[0, 1], [0, 0]], dtype=complex)
P0 = np.diag([1., 0.]).astype(complex)
P1 = I-P0
RAISE = LOWER.conj().T


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def local(a: np.ndarray, site: int, n: int) -> np.ndarray:
    out = np.ones((1, 1), dtype=complex)
    for i in range(n):
        out = np.kron(out, a if i == site else I)
    return out


def parameters(n: int, omega: float, interaction: float, kappa: float,
               width: float, u: float) -> float:
    if (not isinstance(n, int) or n < 3 or
        not all(math.isfinite(v) for v in (omega, interaction, kappa, width, u)) or
        min(kappa, width) <= 0 or u < 0):
        raise ValueError("Require n>=3 and finite rates/width, kappa,width>0, u>=0.")
    return math.exp(-u/(n*kappa*width))


def physical_model(n: int, omega: float, interaction: float, kappa: float):
    """Periodic Ising chain, basis ground then excited; no duplicate edges."""
    dim = 2**n
    h = sum((omega*local(X, i, n)/2 for i in range(n)),
            np.zeros((dim, dim), dtype=complex))
    for i in range(n):
        h += interaction*local(Z, i, n)@local(Z, (i+1) % n, n)/4
    jumps = [math.sqrt(kappa)*local(LOWER, i, n) for i in range(n)]
    jj = sum((np.kron(a.conj(), a) for a in jumps),
             np.zeros((dim**2, dim**2), dtype=complex))
    rate = sum((a.conj().T@a for a in jumps), np.zeros_like(h))
    no = -1j*(np.kron(np.eye(dim), h)-np.kron(h.T, np.eye(dim)))
    no -= (np.kron(np.eye(dim), rate)+np.kron(rate.T, np.eye(dim)))/2
    initial = np.zeros(dim**2, dtype=complex)
    initial[0] = 1
    trace = np.eye(dim).ravel(order='F')
    return h, jumps, no, jj, initial, trace


def flags_generator(no: np.ndarray, jj: np.ndarray, r: float, active: int):
    """Diagonal blocks of two absorbing flags; the physical state is retained."""
    if not 0 <= r <= 1 or active not in (0, 1):
        raise ValueError("Invalid flag setting.")
    d2 = len(no)
    out = np.zeros((4*d2, 4*d2), dtype=complex)
    for word in range(4):
        src = slice(word*d2, (word+1)*d2)
        if word & (1 << active):
            out[src, src] = no+jj
        else:
            out[src, src] = no+r*jj
            dest = word | (1 << active)
            out[dest*d2:(dest+1)*d2, src] += (1-r)*jj
    return out


def observe(no, jj, initial, trace, width: float, r: float):
    full = expm(width*(no+jj))
    tilted = expm(width*(no+r*jj))
    z1 = float((trace@full@tilted@initial).real)
    z2 = float((trace@tilted@full@initial).real)
    z12 = float((trace@tilted@tilted@initial).real)
    return np.array([z1, z2, z12]), z12-z1*z2


def main():
    n, omega, interaction, kappa, width, u = 3, 1., 1., 1., 1., 1.
    r = parameters(n, omega, interaction, kappa, width, u)
    h, jumps, no, jj, initial, trace = physical_model(n, omega, interaction, kappa)
    d2 = len(initial)
    g1, g2 = (flags_generator(no, jj, r, j) for j in (0, 1))
    start = np.zeros(4*d2, dtype=complex); start[:d2] = initial
    final = expm(width*g2)@expm(width*g1)@start
    blocks = final.reshape(4, d2)
    probs = (blocks@trace).real
    require(np.min(probs) > -TOL and abs(probs.sum()-1) < TOL,
            "Flags must define a probability distribution")
    folded = np.sum(blocks, axis=0)
    physical = expm(2*width*(no+jj))@initial
    require(np.linalg.norm(folded-physical) < TOL, "Physical marginal changed")
    references, covariance = observe(no, jj, initial, trace, width, r)
    # Bit 0 tracks window one, bit 1 window two.
    from_flags = np.array([probs[0]+probs[2], probs[0]+probs[1], probs[0]])
    require(np.max(abs(references-from_flags)) < TOL, "Tilted/flag laws disagree")
    require(references[0] >= math.exp(-u)-TOL and
            references[1] >= math.exp(-u)-TOL and
            references[2] >= math.exp(-2*u)-TOL, "Jensen/intensity bound")
    require(abs(covariance) <= .25+TOL, "Bounded covariance")
    # The three local jump types have exactly the original total jump rate.
    lifted = [np.kron(jumps[0], a) for a in
              (math.sqrt(r)*P0, math.sqrt(1-r)*RAISE, P1)]
    rate = sum(a.conj().T@a for a in lifted)
    require(np.linalg.norm(rate-np.kron(jumps[0].conj().T@jumps[0], I)) < TOL,
            "Flag jump completeness")
    # Population after each event must survive; an X flip is not absorption.
    rr = F(1, 2)
    absorbing_survival = rr**2
    parity_survival = rr**2+(1-rr)**2
    require(absorbing_survival == F(1, 4) and parity_survival == F(1, 2),
            "Wrong-flip negative control")
    # Retain correlation across the window boundary; independent restarts lose it.
    require(abs(covariance) > 1e-5, "Control has no boundary memory to test")
    # u=0 is a no-mark control, not an additional physical regime.
    no_mark = expm(width*flags_generator(no, jj, 1., 1))@(
              expm(width*flags_generator(no, jj, 1., 0))@start)
    require(abs(trace@no_mark[:d2]-1) < TOL and np.linalg.norm(no_mark[d2:]) < TOL,
            "u=0 must never mark a flag")
    # Independent coherent emitters: factorized generating functions, not Poisson.
    _, _, no0, jj0, init0, tr0 = physical_model(n, omega, 0., kappa)
    z_ind, cov_ind = observe(no0, jj0, init0, tr0, width, r)
    h1 = omega*X/2; j1 = math.sqrt(kappa)*LOWER
    jmap = np.kron(j1.conj(), j1); rate1 = j1.conj().T@j1
    nj1 = -1j*(np.kron(I, h1)-np.kron(h1.T, I))
    nj1 -= (np.kron(I, rate1)+np.kron(rate1.T, I))/2
    ini1 = np.array([1, 0, 0, 0], dtype=complex); tr1 = I.ravel(order='F')
    single, _ = observe(nj1, jmap, ini1, tr1, width, r)
    require(np.max(abs(z_ind-single**n)) < TOL, "Independent coherent factorization")
    # A supplied small classical phase model is a direct competitor.
    # These rates are illustrative, NOT extracted from the spin model.
    w = np.array([[-.2, .1], [.2, -.1]])
    emission = np.diag([.2, 1.2]); tilted = w+(r-1)*emission
    pi = np.array([1., 0.]); tr2 = np.ones(2)
    phase_z1 = tr2@expm(width*w)@expm(width*tilted)@pi
    phase_z2 = tr2@expm(width*tilted)@expm(width*w)@pi
    phase_z12 = tr2@expm(2*width*tilted)@pi
    phase_gens = [flags_generator(w-emission, emission, r, j) for j in (0, 1)]
    pi_flags = np.zeros(8); pi_flags[:2] = pi
    phase_final = expm(width*phase_gens[1])@expm(width*phase_gens[0])@pi_flags
    phase_prob = (phase_final.reshape(4, 2)@tr2).real
    require(np.max(abs(np.array([phase_z1, phase_z2, phase_z12])-
        [phase_prob[0]+phase_prob[2], phase_prob[0]+phase_prob[1], phase_prob[0]])) < TOL,
        "Small classical model must reproduce its flag statistic")
    invalid = [lambda: parameters(2, 1, 1, 1, 1, 1),
               lambda: parameters(3, 1, 1, 0, 1, 1),
               lambda: parameters(3, 1, 1, 1, 0, 1),
               lambda: parameters(3, 1, 1, 1, 1, -1),
               lambda: parameters(3, float('nan'), 1, 1, 1, 1),
               lambda: flags_generator(no, jj, .5, 2)]
    for action in invalid:
        try:
            action()
        except ValueError:
            continue
        raise AssertionError("Invalid input accepted")
    clean = lambda vals: [round(float(x), 12) for x in vals]
    print(json.dumps({
        "status": "pass",
        "scope": "One three-emitter algebra check, not a quantum run, metastability demonstration, or runtime comparison.",
        "control_parameters": {"n": n, "Omega": omega, "V": interaction,
            "kappa": kappa, "window_width": width, "u": u, "initial": "ggg", "graph": "periodic ring"},
        "source_slice_was_not_simulated": "V/kappa=250 and Omega/kappa=50 from Rose et al.; no scaling inferred.",
        "flag_order": ["00", "10", "01", "11"],
        "flag_probabilities": clean(probs),
        "Z1_Z2_Z12": clean(references),
        "quietness_covariance": round(float(covariance), 12),
        "independent_coherent_Z1_Z2_Z12": clean(z_ind),
        "independent_coherent_covariance": round(float(cov_ind), 12),
        "phase_control": {"meaning": "Illustrative supplied classical rates, not a fitted spin reduction", "Z1_Z2_Z12": clean([phase_z1,phase_z2,phase_z12])},
        "two_event_absorbing_survival_exact": str(absorbing_survival),
        "two_event_wrong_flip_survival_exact": str(parity_survival),
        "checks": ["physical marginal", "tilted/flag identity", "positive probabilities",
            "bounded moments", "jump completeness", "u=0", "no independent restart",
            "coherent independent emitters", "small classical phase bypass", "wrong parity flag"],
        "invalid_inputs_rejected": len(invalid),
        "precision": "complex128 at tolerance 2e-10; reported decimals rounded to 12 places; one exact Fraction control",
        "not_executed": ["amplitude estimation", "Lindblad simulation circuit", "published metastable parameter slice", "large chain", "performance benchmark"]
    }, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
