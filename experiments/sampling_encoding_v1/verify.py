#!/usr/bin/env python3
"""Verify a real CNF prefix's deterministic-wire certificate, not a synthesis run.

The optional --source checks the COMPLETE upstream file before comparing the
excerpt. --native independently queries an installed libz3; it does not run
Manthan/CMSGen and produces no independently checked UNSAT proof.
Python 3.10+, standard library; no file writes. No network access.
"""
from __future__ import annotations
import argparse
import collections
import ctypes
import ctypes.util
import hashlib
import itertools
import json
from pathlib import Path
import random
import sys

if sys.flags.optimize:
    raise SystemExit('Run without -O or -OO.')

ROOT = Path(__file__).resolve().parent
BLOB = 'cd6e0043b175df4247368d0e96a8e1020ed603a4'
PREFIX_SHA = '552172c699638e32fbb5126c11d02916160ec71dfec87d1c397431662a545f15'


def require(ok: bool, reason: str) -> None:
    if not ok:
        raise AssertionError(reason)


def parse(data: str) -> dict[int, list[tuple[int, ...]]]:
    groups: dict[int, list[tuple[int, ...]]] = collections.defaultdict(list)
    last = 0
    for line in data.splitlines():
        tokens = [int(t) for t in line.split()]
        if len(tokens) < 2 or tokens[-1] != 0 or 0 in tokens[:-1]:
            raise ValueError('Malformed clause')
        clause = tuple(tokens[:-1])
        if len(set(map(abs, clause))) != len(clause):
            raise ValueError('Repeated or contradictory variable inside clause')
        out = max(map(abs, clause))
        if out < last:
            raise ValueError('Non-topological group ordering')
        last = out
        groups[out].append(clause)
    return dict(groups)


def clause_set(clauses):
    return {tuple(sorted(c)) for c in clauses}


def gate_definition(out: int, clauses: list[tuple[int, ...]]):
    vars_ = sorted({abs(x) for c in clauses for x in c} - {out})
    actual = clause_set(clauses)
    if len(actual) != len(clauses):
        raise ValueError('Repeated gate clause')
    for op, sign in [('and', -1), ('or', 1)]:
        inputs = []
        for c in clauses:
            if len(c) == 2 and sign * out in c:
                lit = next(t for t in c if abs(t) != out)
                inputs.append(lit if op == 'and' else -lit)
        if len(inputs) != len(vars_) or len(set(map(abs, inputs))) != len(inputs):
            continue
        if op == 'and':
            expected = [(a, -out) for a in inputs] + [tuple([-a for a in inputs] + [out])]
        else:
            expected = [(-a, out) for a in inputs] + [tuple(inputs + [-out])]
        if actual == clause_set(expected):
            return op, tuple(inputs)
    if len(vars_) == 2:
        a, b = vars_
        expected = [(-a,-b,-out),(a,b,-out),(-a,b,out),(a,-b,out)]
        if actual == clause_set(expected):
            return 'xor', (a,b)
    raise ValueError(f'Not a complete supported gate definition: {out}')


def literal(lit, assignment):
    value = assignment[abs(lit)]
    return value if lit > 0 else 1-value


def value(op, inputs, assignment):
    vals = [literal(x, assignment) for x in inputs]
    if op == 'and':
        return int(all(vals))
    if op == 'or':
        return int(any(vals))
    return vals[0] ^ vals[1]


def satisfied(clauses, assignment):
    return all(any(literal(x, assignment) for x in c) for c in clauses)


def reversible(gates):
    """Elementary X, CX and CCX list; clean reusable AND-chain scratch."""
    operations = []
    scratch_base = max(gates) + 1
    max_scratch = 0
    for out, (op, inputs) in gates.items():
        if op == 'xor':
            operations.extend([(inputs[0],out),(inputs[1],out)])
            continue
        # OR(l_i) = NOT AND(NOT l_i); out starts at zero for each new wire.
        controls = inputs if op == 'and' else tuple(-x for x in inputs)
        negatives = [abs(x) for x in controls if x < 0]
        operations.extend((x,) for x in negatives)
        controls = tuple(map(abs, controls))
        k = len(controls)
        if k <= 2:
            operations.append(controls+(out,))
        else:
            max_scratch = max(max_scratch, k-2)
            compute = [(controls[0],controls[1],scratch_base)]
            for j in range(2,k-1):
                compute.append((scratch_base+j-2,controls[j],scratch_base+j-1))
            operations.extend(compute)
            operations.append((scratch_base+k-3,controls[-1],out))
            operations.extend(reversed(compute))
        operations.extend((x,) for x in reversed(negatives))
        if op == 'or':
            operations.append((out,))
    return operations, list(range(scratch_base,scratch_base+max_scratch))


def run_permutation(operations, state):
    for operation in operations:
        *controls, target = operation
        if all(state[c] for c in controls):
            state[target] ^= 1


def z3_queries(groups, gates):
    """Two implication checks over the full prefix, native Z3 C API."""
    path = ctypes.util.find_library('z3')
    if not path:
        raise RuntimeError('Native libz3 unavailable')
    z = ctypes.CDLL(path)
    ptr = ctypes.c_void_p
    for name, args, restype in [
        ('Z3_mk_config', [], ptr), ('Z3_del_config',[ptr],None),
        ('Z3_mk_context',[ptr],ptr), ('Z3_del_context',[ptr],None),
        ('Z3_eval_smtlib2_string',[ptr,ctypes.c_char_p],ctypes.c_char_p),
        ('Z3_get_full_version',[],ctypes.c_char_p)]:
        function=getattr(z,name); function.argtypes=args; function.restype=restype
    def lit(n):
        return f'v{n}' if n>0 else f'(not v{-n})'
    clauses = [f'(or {" ".join(lit(x) for x in c)})' for cs in groups.values() for c in cs]
    definitions = [f'(= v{out} ({op} {" ".join(lit(x) for x in ins)}))'
                   for out,(op,ins) in gates.items()]
    vars_ = sorted({abs(x) for cs in groups.values() for c in cs for x in c})
    common = '(set-option :timeout 10000)\n' + ''.join(f'(declare-const v{x} Bool)\n' for x in vars_)
    c = '(and '+' '.join(clauses)+')'
    d = '(and '+' '.join(definitions)+')'
    outcomes=[]
    for left,right in [(c,d),(d,c)]:
        cfg=z.Z3_mk_config(); ctx=z.Z3_mk_context(cfg); z.Z3_del_config(cfg)
        try:
            command=common+f'(assert (and {left} (not {right})))\n(check-sat)\n'
            result=z.Z3_eval_smtlib2_string(ctx,command.encode()).decode().strip()
            require(result=='unsat',f'Native implication check: {result}')
            outcomes.append(result)
        finally:
            z.Z3_del_context(ctx)
    return {'library':path, 'version':z.Z3_get_full_version().decode(),
            'prefix_implies_gate_equalities':outcomes[0],
            'gate_equalities_imply_prefix':outcomes[1],
            'proof_replay':False, 'scope':'prefix equivalence only; not Manthan or full formula'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path)
    parser.add_argument('--native',action='store_true')
    args=parser.parse_args()
    raw=(ROOT/'gate_prefix.cnf').read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PREFIX_SHA,'Pinned prefix hash mismatch')
    complete_source=False
    if args.source:
        full=args.source.read_bytes()
        git=hashlib.sha1(b'blob '+str(len(full)).encode()+b'\0'+full).hexdigest()
        require(git==BLOB,'Complete upstream Git blob mismatch')
        require(full.splitlines()[3:379]==raw.splitlines(),'Source prefix mismatch')
        complete_source=True
    groups=parse(raw.decode())
    gates={out:gate_definition(out,cs) for out,cs in groups.items()}
    require(list(gates)==list(range(502,587)),'Unexpected gate output range')
    roots=sorted({abs(x) for _,ins in gates.values() for x in ins}-set(gates))
    require(max(roots)<=334,'Gate root outside original X prefix')
    local_cases=0
    for out,(op,ins) in gates.items():
        if len(ins)<=11:
            for bits in itertools.product((0,1),repeat=len(ins)):
                inputs=dict(zip(map(abs,ins),bits))
                expected=value(op,ins,inputs)
                for b in (0,1):
                    require(satisfied(groups[out], inputs|{out:b})==(b==expected),'Gate truth table')
                    local_cases+=1
    operations,scratch=reversible(gates)
    counts=collections.Counter({1:0,2:0,3:0})
    counts.update(map(len,operations))
    generator=random.Random(0)
    patterns=[{x:b for x in roots} for b in (0,1)]
    patterns += [{x:generator.randrange(2) for x in roots} for _ in range(126)]
    flips=0
    all_clauses=[c for cs in groups.values() for c in cs]
    for inputs in patterns:
        expected=dict(inputs)
        for out,(op,ins) in gates.items():
            expected[out]=value(op,ins,expected)
        require(satisfied(all_clauses,expected),'Forward evaluator fails prefix')
        init=inputs|{x:0 for x in gates}|{x:0 for x in scratch}
        state=dict(init); run_permutation(operations,state)
        require(all(state[x]==v for x,v in expected.items()),'Reversible evaluator mismatch')
        require(all(state[x]==0 for x in scratch),'Dirty scratch')
        run_permutation(reversed(operations),state)
        require(state==init,'Uncomputation failure')
        for out in gates:
            bad=expected|{out:1-expected[out]}
            require(not satisfied(all_clauses,bad),'Single-wire negative control accepted')
            flips+=1
    malformed=0
    for mutation in [b'1 0 2\n',b'1 -1 0\n',b'1 -2 0\n1 -2 0\n',b'1 -2 0\n']:
        try:
            for out,cs in parse(mutation.decode()).items():
                gate_definition(out,cs)
        except (ValueError,AssertionError):
            malformed+=1
        else:
            raise AssertionError('Malformed/incomplete gate accepted')
    t = 2**41
    require((2*(t-1)+1)**2 < 2**(len(gates)-1) <= (2*t+1)**2,
            'Fixed-Grover half-success integer bound')
    report={
        'status':'pass','scope':'selected upstream gate-prefix identities; not synthesis, sampling performance or useful advantage',
        'source_git_blob':BLOB,'prefix_sha256':PREFIX_SHA,
        'complete_source_checked':complete_source,
        'source_file_lines':[4,379],'clauses':len(all_clauses),
        'defined_bits':len(gates),'input_root_bits':len(roots),
        'gate_types':dict(collections.Counter(op for op,_ in gates.values())),
        'largest_fanin':max(len(ins) for _,ins in gates.values()),
        'local_truth_assignments_checked':local_cases,
        'basis_input_controls':len(patterns),'single_wire_fault_controls':flips,
        'malformed_controls':malformed,
        'forward_reversible_gates':{'X':counts[1],'CX':counts[2],'CCX':counts[3]},
        'clean_scratch_bits':len(scratch),
        'raw_uniform_success_upper_bound':'2^-85',
        'fixed_Grover_rounds_necessary_for_one_half_success':2**41,
        'removed_uniform_conditioning_penalty':'2^85 in probability; not an application speedup',
    }
    if args.native:
        report['native']=z3_queries(groups,gates)
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
