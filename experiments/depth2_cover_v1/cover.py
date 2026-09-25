"""Exact two-layer constant-multiplier synthesis in a declared bounded model.

One node is a normalized shifted sum/difference of two earlier fundamentals.
All fundamentals are positive odd integers below 2**B; shifts are 0..B.
Copies, shifts, signs and unlimited fanout are free; one node costs one.
No general physical-area or timing interpretation is attached to node count.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product


def odd(value: int) -> int:
    value = abs(value)
    return value // (value & -value) if value else 0


@lru_cache(None)
def signed_weight(value: int) -> int:
    """Minimum number of signed powers of two, allowing arbitrary exponents."""
    value = abs(value)
    if value < 2:
        return value
    if value % 2 == 0:
        return signed_weight(value // 2)
    return 1 + min(signed_weight((value-1)//2), signed_weight((value+1)//2))


def operation(a: int, b: int, shift: int, sign: int, B: int):
    raw = (a << shift) + sign*b
    if raw == 0:
        return None
    absolute = abs(raw)
    right = (absolute & -absolute).bit_length()-1
    value = absolute >> right
    if value >= 1 << B or right > B:
        return None
    return value, (a, b, shift, sign, right, 1 if raw > 0 else -1)


def first_layer(B: int) -> tuple[int, ...]:
    if not isinstance(B, int) or not 2 <= B <= 24:
        raise ValueError('Screen supports coefficient bounds B=2..24.')
    return tuple(sorted({1} | {v for s in range(1, B+1)
                              for v in ((1<<s)-1, (1<<s)+1)
                              if v < 1<<B}))


def minimize_masks(masks):
    kept=[]
    for x in sorted(set(masks), key=lambda x:(x.bit_count(),x)):
        if not any(k & x == k for k in kept):
            kept.append(x)
    return tuple(kept)


def make_model(coefficients, B):
    targets=tuple(sorted({odd(t) for t in coefficients}-{0,1}))
    if any(t >= 1<<B for t in targets):
        raise ValueError('Target outside declared coefficient bound.')
    first=first_layer(B)
    mandatory=set(targets).intersection(first)
    helpers=tuple(sorted(set(first)-mandatory-{1}))
    position={h:i for i,h in enumerate(helpers)}
    expressions={t:{} for t in targets if t not in mandatory}
    evaluations=0
    for a,b in product(first, repeat=2):
        mask=(1<<position[a] if a in position else 0) | (1<<position[b] if b in position else 0)
        for s in range(B+1):
            for sign in (-1,1):
                evaluations+=1
                answer=operation(a,b,s,sign,B)
                if answer is None: continue
                value,witness=answer
                if value in expressions:
                    expressions[value].setdefault(mask,witness)
    requirements={t:minimize_masks(mapping) for t,mapping in expressions.items()}
    return dict(B=B,targets=targets,first=first,mandatory=tuple(sorted(mandatory)),
                helpers=helpers,requirements=requirements,witnesses=expressions,
                pair_shift_tests=evaluations)


def exact_cover(requirements):
    """All inclusion-minimal helper portfolios; subset dominance is exact.

    Future coverage depends only on the union of selected helpers. If A is a
    subset of B and both satisfy every processed target, B can be removed:
    A union C is no larger than B union C for any future choice C.
    """
    frontier=(0,);counts=[1];transitions=0
    for t,alternatives in sorted(requirements.items(),key=lambda kv:(len(kv[1]),kv[0])):
        if not alternatives:
            return dict(feasible=False, obstruction=t, portfolios=(),
                        frontier_sizes=counts, union_operations=transitions)
        choices=[]
        for x in frontier:
            for q in alternatives:
                transitions+=1
                choices.append(x|q)
        frontier=minimize_masks(choices)
        counts.append(len(frontier))
    optimum=min(x.bit_count() for x in frontier)
    return dict(feasible=True, minimum_helpers=optimum,
                portfolios=frontier, minimum_portfolios=tuple(x for x in frontier if x.bit_count()==optimum),
                frontier_sizes=counts,union_operations=transitions)


def decode(mask,helpers):
    return [h for i,h in enumerate(helpers) if mask >> i & 1]


def make_certificate(model,mask):
    B=model['B'];selected=set(decode(mask,model['helpers']))
    values=[1];nodes=[]
    def append(value,witness):
        a,b,s,sign,right,out_sign=witness
        if a not in values or b not in values: raise AssertionError('Unavailable operand.')
        nodes.append(dict(value=value,left=values.index(a),right=values.index(b),
                          shift=s,sign=sign,right_shift=right,output_sign=out_sign))
        values.append(value)
    for value in sorted(set(model['mandatory'])|selected):
        witnesses=[answer[1] for s in range(B+1) for sign in (-1,1)
                   if (answer:=operation(1,1,s,sign,B)) is not None and answer[0]==value]
        append(value,min(witnesses))
    for t in model['targets']:
        if t in values: continue
        valid=[w for m,w in model['witnesses'][t].items() if m & mask == m]
        if not valid:raise AssertionError('Portfolio fails an output.')
        append(t,min(valid))
    verify_certificate(nodes, model['targets'],B)
    return nodes


def verify_certificate(nodes,targets,B):
    values=[1];depth=[0]
    for i,r in enumerate(nodes,1):
        if not 0<=r['left']<i or not 0<=r['right']<i:raise AssertionError('Not a DAG.')
        if r['sign'] not in (-1,1) or r['output_sign'] not in (-1,1):raise AssertionError('Invalid sign.')
        if not 0<=r['shift']<=B or not 0<=r['right_shift']<=B:raise AssertionError('Shift bound.')
        value=((values[r['left']]<<r['shift'])+r['sign']*values[r['right']])*r['output_sign']
        if value != r['value']*(1<<r['right_shift']):raise AssertionError('Incorrect integer identity.')
        if not (0<r['value']<1<<B and r['value']%2):raise AssertionError('Fundamental outside domain.')
        values.append(r['value']);depth.append(1+max(depth[r['left']],depth[r['right']]))
    if not set(targets)<=set(values):raise AssertionError('Missing output.')
    if max(depth)>2:raise AssertionError('Depth exceeds two.')
    return dict(nodes=len(nodes),depth=max(depth),fundamentals=values)


def solve_bank(coefficients,B):
    model=make_model(coefficients,B);answer=exact_cover(model['requirements'])
    record={k:model[k] for k in ('B','targets','first','mandatory','helpers','pair_shift_tests')}
    record['requirements']={str(t):[decode(m,model['helpers']) for m in qs]
                            for t,qs in sorted(model['requirements'].items())}
    record['status']='feasible' if answer['feasible'] else 'infeasible'
    record['minimum_signed_weights']={str(t):signed_weight(t) for t in model['targets']}
    record['frontier_sizes']=answer['frontier_sizes'];record['union_operations']=answer['union_operations']
    if not answer['feasible']:
        record['unreachable_targets']=[t for t,qs in model['requirements'].items() if not qs]
    else:
        record['minimum_helpers']=answer['minimum_helpers']
        record['minimum_operations']=len(model['targets'])+answer['minimum_helpers']
        record['minimal_portfolios']=[decode(m,model['helpers']) for m in answer['portfolios']]
        record['minimum_portfolios']=[decode(m,model['helpers']) for m in answer['minimum_portfolios']]
        record['certificate']=make_certificate(model,answer['minimum_portfolios'][0])
    return record
