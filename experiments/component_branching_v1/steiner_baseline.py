"""Classical directed-Steiner terminal-subset DP for the unary e-graph subcase.

A reference implementation of established directed-Steiner dynamic programming,
not a new algorithm and not a current optimized native synthesis package.
All representatives must have at most one distinct child (repeated ports free).
"""
from __future__ import annotations
from math import inf
from branching import Graph, Node


def solve_unary(graph, max_terminals=16):
    g=graph.restrict_reachable();cs=sorted(g.classes);index={c:i+1 for i,c in enumerate(cs)}
    n=len(cs)+1;terminal=[index[c] for c in g.roots]
    if len(terminal)>max_terminals:raise ValueError('Terminal-DP safety limit; not infeasibility.')
    if any(len(set(nd.children))>1 for ns in g.classes.values() for nd in ns):
        raise ValueError('Unary representatives required for this baseline.')
    dist=[[inf]*n for _ in range(n)]
    for i in range(n):dist[i][i]=0
    for v,nodes in g.classes.items():
        for nd in nodes:
            children=set(nd.children)
            u=index[next(iter(children))] if children else 0
            dist[u][index[v]]=min(dist[u][index[v]],nd.cost)
    for k in range(n):
        for i in range(n):
            if dist[i][k]==inf:continue
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    dp=[[inf]*n for _ in range(1<<len(terminal))];dp[0]=[0]*n
    merge_checks=0;path_checks=0
    for mask in range(1,1<<len(terminal)):
        if mask&(mask-1)==0:
            t=terminal[mask.bit_length()-1]
            dp[mask]=[dist[v][t] for v in range(n)]
            continue
        join=[inf]*n;sub=(mask-1)&mask
        while sub:
            other=mask^sub
            if other and sub<other:
                for v in range(n):
                    join[v]=min(join[v],dp[sub][v]+dp[other][v]);merge_checks+=1
            sub=(sub-1)&mask
        for v in range(n):
            dp[mask][v]=min(dist[v][u]+join[u] for u in range(n));path_checks+=n
    value=dp[-1][0]
    return dict(cost=None if value==inf else value,classes=len(cs),terminals=len(terminal),
                dp_entries=(1<<len(terminal))*n,merge_checks=merge_checks,path_checks=path_checks,
                scope='Established terminal-subset reference DP; not a native best-solver performance claim.')
