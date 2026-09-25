"""Exact helper-only bounded-depth search, retaining shifted arithmetic semantics.

No hardware cost except one per binary arithmetic node. Helpers at the final
layer cannot help a required output and are excluded. Targets are saturated
by earliest-layer forward inference; no helper is supplied as a free input.
"""
from itertools import product
from cover import odd, operation


def closure(targets,helpers,B,D):
    requested=set(targets)|set(helpers)
    known={1:0};witness={}
    for layer in range(1,D+1):
        previous=tuple(sorted(known)); new={}
        for a,b in product(previous,repeat=2):
            if max(known[a],known[b])+1>layer:continue
            for shift in range(B+1):
                for sign in (-1,1):
                    answer=operation(a,b,shift,sign,B)
                    if answer is None:continue
                    c,expr=answer
                    if c in requested and c not in known:
                        if c not in new or expr<new[c]:new[c]=expr
        if not new:break
        for c,expr in sorted(new.items()):
            known[c]=layer;witness[c]=expr
    return known,witness


def helper_candidates(targets,helpers,known,B,D):
    forbidden=set(targets)|set(helpers)|{1}
    # A non-output helper at depth D would be dead in a depth-D circuit.
    inputs=tuple(sorted(x for x in known if known[x]<D-1))
    choices=set()
    for a,b in product(inputs,repeat=2):
        for shift in range(B+1):
            for sign in (-1,1):
                answer=operation(a,b,shift,sign,B)
                if answer and answer[0] not in forbidden:
                    choices.add(answer[0])
    return tuple(sorted(choices))


def search(coefficients,B,D,budget):
    targets=tuple(sorted({odd(t) for t in coefficients}-{0,1}))
    if D<0 or budget<0:raise ValueError('Nonnegative depth and helper budgets required.')
    if any(t >= 1<<B for t in targets):raise ValueError('Target outside coefficient domain.')
    seen=set();counts=[0]*(budget+1);proposals=0;witness=None
    def visit(H):
        nonlocal proposals,witness
        if H in seen:return False
        seen.add(H);counts[len(H)]+=1
        known,rules=closure(targets,H,B,D)
        if not set(H)<=set(known):raise AssertionError('Reached an unconstructible helper state.')
        if set(targets)<=set(known):
            witness=(H,known,rules);return True
        if len(H)==budget:return False
        for c in helper_candidates(targets,H,known,B,D):
            proposals+=1
            if visit(tuple(sorted(H+(c,)))):return True
        return False
    feasible=visit(())
    result=dict(feasible=feasible,budget=budget,visited_by_helper_count=counts,
                proposals=proposals)
    if feasible:
        H,known,rules=witness
        vals=[1];nodes=[]
        for c in sorted(set(targets)|set(H),key=lambda c:(known[c],c)):
            a,b,s,sign,right,outsign=rules[c]
            nodes.append(dict(value=c,left=vals.index(a),right=vals.index(b),shift=s,
                              sign=sign,right_shift=right,output_sign=outsign))
            vals.append(c)
        result.update(helpers=list(H),nodes=len(nodes),depth=max((known[t] for t in targets), default=0),certificate=nodes)
    return result
