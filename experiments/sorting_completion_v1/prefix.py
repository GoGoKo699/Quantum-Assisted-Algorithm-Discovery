"""Exact component-factored Boolean reachability; all arithmetic is finite.

This implements standard prefix-output reduction, not a novel synthesis method.
Wire 0 is the least-significant bit and is the top (minimum) wire.
"""
from __future__ import annotations
from itertools import product
from math import prod

def apply_pair(x: int, i: int, j: int) -> int:
    if ((x >> i) & 1) and not ((x >> j) & 1):
        return x ^ (1 << i) ^ (1 << j)
    return x

def apply_layers(x: int, layers: list) -> int:
    for layer in layers:
        for i,j in layer:
            x=apply_pair(x,i,j)
    return x

def sorted_word(n:int, weight:int) -> int:
    return ((1 << weight)-1) << (n-weight)

def validate_layers(n:int, layers:list) -> None:
    if n<1:raise ValueError('Positive width required.')
    for layer in layers:
        seen=set()
        for i,j in layer:
            if not 0<=i<j<n or i in seen or j in seen:
                raise ValueError('Each layer must be a disjoint forward matching.')
            seen.update((i,j))

def reachable(n:int, layers:list, cap:int=2_000_000):
    """Return independent component sets and an exact size/work census.

    Merging disconnected components forms a Cartesian product before applying
    the connecting comparator. This is exact because no earlier comparator
    crossed the components. General prefixes can still require exponential work.
    """
    validate_layers(n,layers)
    components={i:({i},{0,1<<i}) for i in range(n)}
    owner=list(range(n));peak=2;evaluations=0;by_layer=[1<<n]
    for layer in layers:
        for i,j in layer:
            a,b=owner[i],owner[j]
            if a==b:
                wires,states=components[a]
            else:
                wa,sa=components.pop(a);wb,sb=components.pop(b)
                if len(sa)*len(sb)>cap:raise RuntimeError('Declared exact-enumeration cap reached.')
                wires=wa|wb;states={x|y for x in sa for y in sb}
                for w in wires:owner[w]=a
            peak=max(peak,len(states));evaluations+=len(states)
            components[a]=(wires,{apply_pair(x,i,j) for x in states})
        by_layer.append(prod(len(s) for _,s in components.values()))
    return list(components.values()),dict(by_layer=by_layer,
        peak_component_inputs=peak,comparator_pattern_evaluations=evaluations,
        component_sizes=sorted((len(w),len(s)) for w,s in components.values()))

def materialize(components,cap:int=2_000_000):
    count=prod(len(s) for _,s in components)
    if count>cap:raise RuntimeError('Output materialization cap reached.')
    states={0}
    for _,pool in components:states={x|y for x in states for y in pool}
    if len(states)!=count:raise AssertionError('Disjoint component product failed.')
    return sorted(states)
