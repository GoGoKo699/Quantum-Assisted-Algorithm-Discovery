"""Exact finite check of conditioning a causal slice before classical completion.

Standard-library algebra/statevector diagnostic only. No LLM, full compiler,
quantum hardware, or performance comparison. The toy has a direct classical
sampler. Files are created exclusively; earlier observations are not changed.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
from pathlib import Path


def predicate(s: int) -> int:
    a, b, c, d = ((s >> j) & 1 for j in range(4))
    return (a & b) ^ (c & d)


def generate(s: int, r: int) -> tuple[int, int]:
    # A deliberately small many-to-one generator. The first returned field
    # determines acceptance; the second depends on BOTH relevant and other bits.
    return predicate(s), ((s & 7) + r) % 5


def normalize(counts):
    total = sum(counts.values())
    if total <= 0:
        raise ValueError('Positive mass required.')
    return {x:F(c,total) for x,c in counts.items()}


def tv(p, q):
    return sum(abs(p.get(x,F(0))-q.get(x,F(0))) for x in set(p)|set(q))/2


def phase_check(s):
    # Compute two ANDs into clean work bits, Z each, then uncompute.
    a,b,c,d = ((s>>j)&1 for j in range(4))
    anc0=anc1=0
    anc0 ^= a & b
    anc1 ^= c & d
    phase = (-1)**(anc0+anc1)
    anc1 ^= c & d
    anc0 ^= a & b
    if anc0 or anc1 or phase != (-1)**predicate(s):
        raise AssertionError('Marker action or clean uncomputation failed.')
    return phase


def run():
    good = [s for s in range(16) if predicate(s)]
    direct = Counter(generate(s,r) for s in range(16) for r in range(16)
                     if generate(s,r)[0])
    exact = normalize(direct)
    # Ordinary Grover action on the four relevant bits, done with exact fractions.
    marked = [F(1,4)*phase_check(s) for s in range(16)]
    mean = sum(marked)/16
    amplitudes = [2*mean-a for a in marked]
    if sum(a*a for a in amplitudes) != 1:
        raise AssertionError('Unitary control did not preserve norm.')
    success = sum(amplitudes[s]**2 for s in good)
    posterior = {s:amplitudes[s]**2/success for s in good}
    if success != F(27,32) or any(p != F(1,6) for p in posterior.values()):
        raise AssertionError('Known amplitude-amplification control failed.')
    late = defaultdict(F)
    for s,p in posterior.items():
        for r in range(16):
            late[generate(s,r)] += p/16
    if tv(exact,late):
        raise AssertionError('Late classical completion changes target law.')
    # The same toy is easy CLASSICALLY: choose which pair is 11, then choose
    # 00, 01 or 10 uniformly for the other pair. Six equally likely core labels.
    classical = Counter()
    for side in range(2):
        for other in (0,1,2):
            s = (3 | (other<<2)) if side==0 else (other | (3<<2))
            classical[s]+=1
    if set(classical)!=set(good) or any(c!=1 for c in classical.values()):
        raise AssertionError('Direct classical sampler mismatch.')
    # Invalid shortcut: first freeze an influential outer random bit, THEN
    # perfectly condition the inner three bits. This changes outer weights.
    ok = lambda outer,inner: inner < (1 if outer==0 else 7)
    joint = normalize(Counter((o,i) for o in range(2) for i in range(8) if ok(o,i)))
    frozen = {(o,i):F(1,2)*F(1,1 if o==0 else 7)
              for o in range(2) for i in range(8) if ok(o,i)}
    correct_outer=[sum(p for (o,i),p in joint.items() if o==j) for j in range(2)]
    wrong_outer=[sum(p for (o,i),p in frozen.items() if o==j) for j in range(2)]
    if correct_outer!=[F(1,8),F(7,8)] or wrong_outer!=[F(1,2),F(1,2)]:
        raise AssertionError('Outer-context posterior control failed.')
    if tv(joint,frozen)!=F(3,8):
        raise AssertionError('Unexpected context-freezing error.')
    def strings(p):
        return {str(k):str(v) for k,v in sorted(p.items())}
    return dict(scope='Exact toy semantics and Grover control; not a new primitive, LLM run or advantage.',
        full_random_bits=8, relevant_random_bits=4, unused_random_bits_deferred=4,
        full_tapes=256, satisfying_full_tapes=sum(direct.values()),
        satisfying_slice_labels=good, prior_acceptance=str(F(len(good),16)),
        one_grover_iteration_success=str(success),
        marker_basis_states_checked=16, clean_workspace_bits=2,
        sliced_vs_full_total_variation=str(tv(exact,late)),
        conditional_output_distribution=strings(exact),
        direct_classical_core_sampler=strings(normalize(classical)),
        influential_context_control=dict(correct_outer=list(map(str,correct_outer)),
            incorrectly_frozen_outer=list(map(str,wrong_outer)),joint_total_variation='3/8'),
        resource_scope='Four search bits plus two marker work bits in the local marker only; no full gate/depth or physical count.')


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    result=run()
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps(result,indent=2,sort_keys=True))
