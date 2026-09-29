#!/usr/bin/env python3
"""Exact finite controls for an implicit Gaussian graph/access comparison.

Python 3.10+, standard library only. No data files, network, or file writes.
Not a sparsification implementation, quantum circuit, or hardness benchmark.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
import json
import sys

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')

COUNTS: dict[str, int] = {}


def check(ok: bool, name: str) -> None:
    if not ok:
        raise AssertionError(name)
    COUNTS[name] = COUNTS.get(name, 0) + 1


def neighbor(n: int, i: int, k: int) -> int:
    if n < 2 or not 0 <= i < n or not 0 <= k < n-1:
        raise ValueError('Invalid complete-graph adjacency index.')
    return k + int(k >= i)


def weights(points: list[tuple[int, ...]], base: F) -> dict[tuple[int, int], F]:
    if len(points) < 2 or not points[0] or any(len(p) != len(points[0]) for p in points):
        raise ValueError('At least two equal-dimensional nonempty points required.')
    if not F(0) < base < F(1):
        raise ValueError('Gaussian dyadic base must be between zero and one.')
    return {(i,j):base**sum((a-b)**2 for a,b in zip(points[i], points[j]))
            for i,j in combinations(range(len(points)),2)}


def laplacian(n: int, w: dict[tuple[int, int], F]) -> list[list[F]]:
    out = [[F(0) for _ in range(n)] for _ in range(n)]
    for (i,j), value in w.items():
        if not 0 <= i < j < n or value < 0:
            raise ValueError('Invalid edge/weight.')
        out[i][i] += value; out[j][j] += value
        out[i][j] -= value; out[j][i] -= value
    return out


def solve(a: list[list[F]], b: list[F]) -> list[F]:
    n = len(a)
    if n == 0 or len(b) != n or any(len(row) != n for row in a):
        raise ValueError('Invalid square system.')
    rows = [list(map(F,row))+[F(rhs)] for row,rhs in zip(a,b)]
    for col in range(n):
        pivot = next((j for j in range(col,n) if rows[j][col]),None)
        if pivot is None:
            raise ValueError('Singular system.')
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]; rows[col] = [x/scale for x in rows[col]]
        for j in range(n):
            if j != col:
                c = rows[j][col]
                rows[j] = [x-c*y for x,y in zip(rows[j], rows[col])]
    return [row[-1] for row in rows]


def energy(a: list[list[F]], x: list[F]) -> F:
    return sum(x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))


def harmonic(a: list[list[F]], labels: dict[int,F]) -> list[F]:
    n = len(a)
    if not labels or any(not 0 <= i < n for i in labels):
        raise ValueError('Grounding labels required.')
    free = [i for i in range(n) if i not in labels]
    out = [F(labels.get(i,0)) for i in range(n)]
    if free:
        sol = solve([[a[i][j] for j in free] for i in free],
                    [-sum(a[i][j]*v for j,v in labels.items()) for i in free])
        for i,v in zip(free,sol): out[i]=v
    for i in free:
        check(sum(a[i][j]*out[j] for j in range(n)) == 0, 'harmonic_stationarity')
    return out


def main() -> None:
    for n in (4,7):
        for i in range(n):
            got = [neighbor(n,i,k) for k in range(n-1)]
            check(got == [j for j in range(n) if i!=j], 'implicit_adjacency_bijection')
    points = [(0,0),(1,0),(0,1),(1,1)]
    w = weights(points,F(1,2)); n=len(points); m=len(w)
    a=laplacian(n,w); tau=min(w.values()); total_leverage=F(0); levers=[]
    for (i,j),wij in w.items():
        rhs=[F(int(t==i)-int(t==j)) for t in range(n)]
        voltage=solve([row[:-1] for row in a[:-1]], rhs[:-1])+[F(0)]
        resist=voltage[i]-voltage[j]; leverage=wij*resist
        check(F(0)<leverage<=F(2,n)/tau, 'broad_kernel_leverage_bound')
        total_leverage+=leverage; levers.append(str(leverage))
    check(total_leverage==n-1,'leverage_trace_identity')
    # Expectation of m*w_e*b_e*b_e^T under a uniform edge, exactly.
    expected=[[F(0) for _ in range(n)] for _ in range(n)]
    for edge,wij in w.items():
        one=laplacian(n,{edge:m*wij})
        for i in range(n):
            for j in range(n):expected[i][j]+=one[i][j]/m
    check(expected==a,'uniform_edge_unbiased_laplacian')
    epsilon=F(1,5)
    modified={e:value*(1+epsilon if e==(0,1) else 1) for e,value in w.items()}
    ah=laplacian(n,modified)
    f=harmonic(a,{0:F(0),3:F(1)}); g=harmonic(ah,{0:F(0),3:F(1)})
    diff=[x-y for x,y in zip(g,f)]; error=energy(a,diff); reference=energy(a,f)
    check(error>0,'nonzero_harmonic_change_control')
    check(error<=(epsilon/(1-epsilon))**2*reference,'harmonic_energy_bound')
    eta=F(1,32)
    compounded=eta+epsilon+eta*epsilon
    check((1+eta)*(1+epsilon)==1+compounded,'upper_relative_error_composition')
    check((1-eta)*(1-epsilon)>=1-compounded,'lower_relative_error_composition')
    # Finite-bit version of the known bichromatic-cut reduction; not a hard instance.
    aa=[(0,0,0,0,0),(1,1,0,0,0),(1,0,1,1,0)]
    bb=[(1,1,1,0,0),(0,1,1,1,1),(1,0,0,1,1)]
    allpoints=aa+bb; size=len(allpoints); p=(16*size*size-1).bit_length(); r=F(1,2**p)
    allw=weights(allpoints,r)
    cross=sum(v for (i,j),v in allw.items() if i<len(aa)<=j)
    min_dist=min(sum((x-y)**2 for x,y in zip(a,b)) for a in aa for b in bb)
    for k in range(len(aa[0])+1):
        threshold=r**k/2
        if min_dist<=k:
            check(F(2,3)*cross>threshold,'closest_pair_yes_cut_separation')
        else:
            check(cross<=r**k/64 and F(4,3)*cross<threshold,'closest_pair_no_cut_separation')
    max_bits=max(v.denominator.bit_length() for v in allw.values())
    check(max_bits<=p*len(aa[0])+1,'polynomial_weight_precision')
    # Tiny absolute edge mass may still control a boundary-value prediction.
    gap=5
    pts=[(-gap-1,),(-gap,),(0,),(gap,),(gap+1,)]
    ww={e:2*v for e,v in weights(pts,F(1,2)).items()}
    removed={(0,2),(1,2)}
    ar=laplacian(5,ww); cut=laplacian(5,{e:v for e,v in ww.items() if e not in removed})
    labels={0:F(0),1:F(0),3:F(1),4:F(1)}
    original=harmonic(ar,labels); pruned=harmonic(cut,labels)
    deleted_trace=2*sum(ww[e] for e in removed)
    check(original[2]==F(1,2) and pruned[2]==1,'absolute_pruning_prediction_negative_control')
    check(deleted_trace<F(1,1000000),'small_absolute_laplacian_change')
    invalid=[lambda:neighbor(4,4,0),lambda:neighbor(4,1,3),
             lambda:weights([(0,),(1,2)],F(1,2)),lambda:weights(points,F(1)),
             lambda:solve([[F(0)]],[F(1)]),lambda:harmonic(a,{})]
    for fn in invalid:
        try: fn()
        except ValueError:COUNTS['invalid_inputs_rejected']=COUNTS.get('invalid_inputs_rejected',0)+1
        else:raise AssertionError('Invalid control accepted.')
    print(json.dumps({'status':'pass','scope':'Exact finite rational contract controls; no sparsifier, quantum circuit, data workflow or speedup benchmark.',
        'counts':COUNTS,
        'square_graph':{'n':n,'edges':m,'minimum_weight':str(tau),'edge_leverages':levers,
          'label_solution':list(map(str,f)),'perturbed_solution':list(map(str,g)),
          'error_energy':str(error),'energy_bound':str((epsilon/(1-epsilon))**2*reference)},
        'dyadic_reduction_control':{'n':size,'dimension':len(aa[0]),'base_exponent_bits':p,
          'minimum_bichromatic_squared_distance':min_dist,'cut_weight':str(cross),
          'largest_denominator_binary_digits':max_bits,'warning':'Checks the reduction inequalities, not conditional hardness empirically.'},
        'pruning_control':{'center_before':str(original[2]),'center_after':str(pruned[2]),
          'deleted_laplacian_trace':str(deleted_trace),'warning':'Sensitivity control; not evidence that an isolated point requires this accuracy in a real application.'},
        'not_executed':['quantum enumeration','bounded-independence sparsifier','QRAM implementation','matrix concentration sampling','real-data label classification','historical scientific verifiers']},indent=2,sort_keys=True))

if __name__=='__main__':main()
