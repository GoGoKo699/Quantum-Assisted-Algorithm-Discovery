#!/usr/bin/env python3
"""One published seven-emitter slice: acquire, then validate a small tilted model.

NumPy and SciPy. No files written, network access, Monte Carlo, or quantum circuit.
Results are floating-point diagnostics, NOT interval certificates or size scaling.
Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 for reproducible output.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import math
import sys
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment
from scipy.sparse import coo_matrix, eye, kron
from scipy.sparse.linalg import LinearOperator, eigs, expm_multiply, norm, splu

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')

N, OMEGA, V, KAPPA = 7, 50.0, 250.0, 1.0
WINDOWS = (1.0, 5.0, 20.0)
TOL = 3e-8


def require(test: bool, message: str) -> None:
    if not test:
        raise AssertionError(message)


def validate(n: int, omega: float, coupling: float, kappa: float) -> None:
    if not isinstance(n, int) or n < 3:
        raise ValueError('A ring needs at least three sites.')
    if not all(math.isfinite(x) for x in (omega, coupling, kappa)) or kappa <= 0:
        raise ValueError('Require finite coefficients and positive decay.')


def orbit_model(n: int, omega: float, coupling: float, kappa: float):
    """Exact invariant operator space of simultaneous translations/reflections.

Basis vectors are normalized sums of matrix units |a><b| in a dihedral orbit.
This does not project the physical system onto its symmetric Hilbert subspace.
"""
    validate(n, omega, coupling, kappa)
    d = 1 << n
    mask = d - 1
    def rotate(a):
        return ((a << 1) & mask) | (a >> (n - 1))
    def reflect(a):
        return int(f'{a:0{n}b}'[::-1], 2)
    which = -np.ones(d*d, dtype=int)
    reps, sizes = [], []
    for index in range(d*d):
        if which[index] >= 0:
            continue
        a, b = divmod(index, d)
        orbit = set()
        for reflected in (False, True):
            aa, bb = (reflect(a), reflect(b)) if reflected else (a, b)
            for _ in range(n):
                orbit.add(aa*d + bb)
                aa, bb = rotate(aa), rotate(bb)
        which[list(orbit)] = len(reps)
        reps.append((a, b))
        sizes.append(len(orbit))
    sizes = np.array(sizes, dtype=int)
    energy = np.array([coupling/4 * sum(
        (2*((a >> i) & 1)-1) * (2*((a >> ((i+1) % n)) & 1)-1)
        for i in range(n)) for a in range(d)])
    rows, cols, vals, jrows, jcols, jvals = [], [], [], [], [], []
    def append(index, column, value, rr, cc, vv):
        row = which[index]
        rr.append(row); cc.append(column)
        vv.append(value * math.sqrt(sizes[column]/sizes[row]))
    for column, (a, b) in enumerate(reps):
        append(a*d+b, column, -1j*(energy[a]-energy[b])-
               kappa*(a.bit_count()+b.bit_count())/2, rows, cols, vals)
        for i in range(n):
            bit = 1 << i
            append((a ^ bit)*d+b, column, -1j*omega/2, rows, cols, vals)
            append(a*d+(b ^ bit), column, 1j*omega/2, rows, cols, vals)
            if a & bit and b & bit:
                append((a ^ bit)*d+(b ^ bit), column, kappa, jrows, jcols, jvals)
    size = len(reps)
    jump = coo_matrix((jvals, (jrows, jcols)), shape=(size, size)).tocsr()
    generator = coo_matrix((vals, (rows, cols)), shape=(size, size)).tocsr() + jump
    trace = np.array([math.sqrt(s) if a == b else 0
                      for (a, b), s in zip(reps, sizes)], dtype=complex)
    initial = np.zeros(size, dtype=complex)
    initial[which[0]] = 1.0
    embed = coo_matrix((1/np.sqrt(sizes[which]), (np.arange(d*d), which)),
                      shape=(d*d, size)).tocsr()
    return generator, jump, initial, trace, embed


def full_model(n: int, omega: float, coupling: float, kappa: float):
    """Independent Kronecker construction, retaining all 4**n operator entries."""
    validate(n, omega, coupling, kappa)
    x = coo_matrix([[0., 1.], [1., 0.]]).tocsr()
    z = coo_matrix([[-1., 0.], [0., 1.]]).tocsr()
    lower = coo_matrix([[0., 1.], [0., 0.]]).tocsr()
    d = 1 << n
    def local(op, site):
        return kron(kron(eye(1 << (n-site-1)), op), eye(1 << site), format='csr')
    zz = [local(z, i) for i in range(n)]
    h = sum((omega/2 * local(x, i) for i in range(n)), coo_matrix((d,d))).tocsr()
    h += sum((coupling/4 * (zz[i] @ zz[(i+1) % n]) for i in range(n)), coo_matrix((d,d))).tocsr()
    ident = eye(d, format='csr')
    generator = -1j*(kron(h, ident, format='csr')-kron(ident, h.T, format='csr'))
    jump = coo_matrix((d*d, d*d), dtype=complex).tocsr()
    for i in range(n):
        j = math.sqrt(kappa)*local(lower, i)
        rate = j.conj().T @ j
        jump += kron(j, j.conj(), format='csr')
        generator -= .5*(kron(rate, ident, format='csr')+kron(ident, rate.T, format='csr'))
    generator += jump
    initial = np.zeros(d*d, dtype=complex); initial[0] = 1
    trace = np.eye(d).ravel().astype(complex)
    return generator, jump, initial, trace


@dataclass
class Modes:
    eigenvalues: np.ndarray
    right: np.ndarray
    dual: np.ndarray
    diagnostics: dict

    def evolve(self, time: float, vector: np.ndarray) -> np.ndarray:
        return self.right @ (np.exp(time*self.eigenvalues) * (self.dual @ vector))


def acquire_modes(a, shift: float = 1e-4) -> Modes:
    """One sparse factorization shared by right/left shift-invert solves.

Select two eigenvalues closest to a small positive real shift; no claimed
arbitrary-size proof that these are the only slowly decaying modes.
"""
    size = a.shape[0]
    lu = splu((a-shift*eye(size, format='csc')).tocsc())
    solves = {'right': 0, 'left': 0}
    def inverse(x):
        solves['right'] += 1
        return lu.solve(x)
    def inverse_h(x):
        solves['left'] += 1
        return lu.solve(x, trans='H')
    right_inv = LinearOperator(a.shape, matvec=inverse, dtype=complex)
    left_inv = LinearOperator(a.shape, matvec=inverse_h, dtype=complex)
    start = np.arange(1, size+1, dtype=float)
    start /= np.linalg.norm(start)
    vals, right = eigs(a, k=2, sigma=shift, OPinv=right_inv,
                      v0=start, tol=2e-12, maxiter=2000)
    vals_l, left = eigs(a.conj().T, k=2, sigma=shift, OPinv=left_inv,
                      v0=start, tol=2e-12, maxiter=2000)
    matching = linear_sum_assignment(abs(vals[:, None]-vals_l[None, :].conj()))[1]
    left = left[:, matching]
    order = np.argsort(-vals.real)
    vals, right, left = vals[order], right[:, order], left[:, order]
    dual = np.linalg.solve(left.conj().T @ right, left.conj().T)
    residual = max(np.linalg.norm(a@right-right@np.diag(vals)),
                   np.linalg.norm(dual@a-np.diag(vals)@dual))
    require(residual < TOL, 'Eigenpair residual too large for this diagnostic.')
    require(np.linalg.norm(dual@right-np.eye(2)) < TOL, 'Biorthogonality lost.')
    return Modes(vals, right, dual, {
        'sparse_factorizations': 1,
        'LU_stored_nonzeros': int(lu.L.nnz+lu.U.nnz),
        'shift_inverse_solves': solves,
        'residual_below_3e_8': True,
        'note': 'Residual is not a complete nonnormal error or truncation certificate.'})


def moments(generator, jump, initial, trace, delta: float, substeps: int = 1):
    if not math.isfinite(delta) or delta <= 0 or substeps < 1:
        raise ValueError('Positive finite window and step count required.')
    a = generator + math.expm1(-1/(N*KAPPA*delta))*jump
    def evolve(matrix, vector):
        for _ in range(substeps):
            vector = expm_multiply(matrix*(delta/substeps), vector)
        return vector
    unmarked = evolve(a, initial)
    ordinary = evolve(generator, initial)
    final = evolve(a, np.column_stack([unmarked, ordinary]))
    z = np.array([trace@unmarked, trace@final[:,1], trace@final[:,0]])
    require(max(abs(z.imag)) < TOL, 'Complex probability.')
    return z.real


def covariance(z):
    return float(z[2]-z[0]*z[1])


def rounded(z):
    return [round(float(x), 12) for x in np.asarray(z).real]


def error_display(value):
    """Do not present below-display-resolution errors as exact zeros."""
    return "<1e-12" if abs(value) < 1e-12 else round(float(abs(value)), 12)


def main():
    np.random.seed(290929)  # Reproduce internal norm-estimation choices, not physical trajectories.
    l, j, rho, trace, embed = orbit_model(N, OMEGA, V, KAPPA)
    full_l, full_j, full_rho, full_trace = full_model(N, OMEGA, V, KAPPA)
    require(l.shape == (1300,1300), 'Wrong invariant dimension.')
    require(norm(embed.conj().T@embed-eye(1300)) < TOL, 'Orbit basis not isometric.')
    intertwine = norm(full_l@embed-embed@l) / norm(full_l@embed)
    require(intertwine < 1e-12, 'Full and orbit generators disagree.')
    require(norm(full_j@embed-embed@j) < TOL, 'Jump map failed intertwining.')
    require(np.linalg.norm(trace@l) < TOL, 'Trace preservation failed.')
    require(np.linalg.norm(full_trace@embed-trace) < TOL, 'Trace vectors disagree.')
    require(np.linalg.norm(embed@rho-full_rho) < TOL, 'Initial state changed.')
    base = acquire_modes(l)
    base_alt = acquire_modes(l, shift=1e-3)
    r, b = base.right, base.dual
    lsmall, jsmall = np.diag(base.eigenvalues), b@j@r
    left, initial = trace@r, b@rho
    alt_differences = []
    rows = []
    for delta in WINDOWS:
        z = moments(l, j, rho, trace, delta)
        factor = math.expm1(-1/(N*KAPPA*delta))
        reduced = expm(delta*(lsmall+factor*jsmall))
        ordinary = expm(delta*lsmall)
        zp = np.array([left@reduced@initial,
                       left@reduced@ordinary@initial,
                       left@reduced@reduced@initial]).real
        # Re-acquiring at the actual tilt is an optional refinement, not free data.
        tilted = acquire_modes(l+factor*j)
        zt = np.array([trace@tilted.evolve(delta,rho),
                       trace@tilted.evolve(delta,base.evolve(delta,rho)),
                       trace@tilted.evolve(2*delta,rho)]).real
        # Sensitivity check: independent shifted eigensolve, same two-mode method.
        ra, ba = base_alt.right, base_alt.dual
        ka = np.diag(base_alt.eigenvalues)+factor*(ba@j@ra)
        ea, e0a = expm(delta*ka), expm(delta*np.diag(base_alt.eigenvalues))
        la, ca = trace@ra, ba@rho
        za = np.array([la@ea@ca, la@ea@e0a@ca, la@ea@ea@ca]).real
        alt_differences.append(float(max(abs(za-zp))))
        require(max(abs(za-zp)) < TOL, 'Shift sensitivity failed.')
        require(np.all((z >= 0) & (z <= 1)), 'Invalid exact probabilities.')
        require(max(abs(z-zp)) < .001, 'Unexpected failure of fixed-slice reduction.')
        require(abs(covariance(z)-covariance(zp)) < 4e-5, 'Covariance reduction failed.')
        # Wrong stationary replacement, as an explicit changed-initial-state control.
        stationary = r[:,0]/(trace@r[:,0])
        cstat = b@stationary
        zstat = np.array([left@reduced@cstat, left@reduced@ordinary@cstat,
                          left@reduced@reduced@cstat]).real
        rows.append({'kappa_Delta': delta, 'exact_tilted_Z1_Z2_Z12': rounded(z),
                     'exact_tilted_G': round(covariance(z),12),
                     'once_acquired_two_mode_Z1_Z2_Z12': rounded(zp),
                     'once_acquired_two_mode_G': round(covariance(zp),12),
                     'once_acquired_G_absolute_error': error_display(covariance(zp)-covariance(z)),
                     'once_acquired_max_Z_error': error_display(float(max(abs(zp-z)))),
                     'tilt_readjusted_Z1_Z2_Z12': rounded(zt),
                     'tilt_readjusted_G': round(covariance(zt),12),
                     'tilt_readjusted_G_absolute_error': error_display(covariance(zt)-covariance(z)),
                     'tilt_readjusted_max_Z_error': error_display(float(max(abs(zt-z)))),
                     'wrong_stationary_start_G': round(covariance(zstat),12),
                     'tilted_acquisition': tilted.diagnostics})
    # Independent full Liouville-space calculation at the shortest declared window.
    full_a = full_l + math.expm1(-1/(N*KAPPA))*full_j
    z1full = full_trace @ expm_multiply(full_a, full_rho)
    full_discrepancy = float(abs(z1full-rows[0]['exact_tilted_Z1_Z2_Z12'][0]))
    require(full_discrepancy < TOL, 'Independent full-space propagation disagrees.')
    # Distinct exponential-action decomposition, at the central observation window.
    zhalf = moments(l, j, rho, trace, 5., substeps=2)
    half_discrepancy = float(max(abs(zhalf-np.array(rows[1]['exact_tilted_Z1_Z2_Z12']))))
    require(half_discrepancy < TOL, 'Exponential-action subdivision disagrees.')
    require(max(abs(row['wrong_stationary_start_G']-row['exact_tilted_G']) for row in rows)>1e-4,
            'Ground-start negative control did not distinguish stationarity.')
    invalid = [lambda: validate(2,1,1,1), lambda: validate(7,1,1,0),
               lambda: validate(7,float('nan'),1,1), lambda: validate(7,1,float('inf'),1),
               lambda: moments(l,j,rho,trace,0), lambda: moments(l,j,rho,trace,-1)]
    for action in invalid:
        try:
            action()
        except ValueError:
            continue
        raise AssertionError('Invalid input accepted.')
    out = {'status':'pass', 'scope':'One published seven-emitter parameter slice; numerical validation of one scalar, not all-size tractability or record-TV certification.',
           'model':{'n':N,'Omega_over_kappa':OMEGA,'V_over_kappa':V,'kappa':KAPPA,
                    'graph':'uniform periodic ring','initial':'all ground','u':1},
           'original_operator_dimension':4**N, 'exact_invariant_dimension':l.shape[0],
           'invariant_generator_nonzeros':l.nnz,'full_generator_nonzeros':full_l.nnz,
           'once_acquired_slow_eigenvalues_real':rounded(base.eigenvalues),
           'once_acquired_reference':base.diagnostics,
           'additional_validation_shift_acquisition':base_alt.diagnostics,
           'rows':rows,
           'validation':{'exact_group_reduction_intertwining_below_1e_12':True,
                         'full_space_Z1_reference_agrees_below_3e_8':True,
                         'half_step_reference_agrees_below_3e_8':True,
                         'changed_eigensolver_shift_agrees_below_3e_8':True,
                         'initial_transient_not_replaced_by_stationarity':True,
                         'invalid_inputs_rejected':len(invalid)},
           'precision':'complex128; probabilities rounded to 12 decimals. No interval-certified numerical errors or proof of a uniform metastable approximation.',
           'not_executed':['quantum circuit','amplitude estimation','hardware','large-n extrapolation','Monte Carlo trajectories','native upstream implementation','wall-clock comparison']}
    print(json.dumps(out,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
