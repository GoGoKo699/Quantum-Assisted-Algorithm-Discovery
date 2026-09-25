"""Exact finite checks for scale-invariant local-price search.

Seeded structural instances test arithmetic/graph claims, not rewrite semantics.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json, random, sys
from math import comb, inf, log2
from pathlib import Path
from spectrum import PriceSpectrum, SpectrumLimit, Graph, Node, Grounding, SharingCore
from spectrum import scaled, exponential_spectrum, persistent_spectrum
from budget import allocations, exhaustive
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('budget_prior_checks', ROOT.parent/'budget_grounding_v1/checks.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
random_graph = prior.random_graph
from public_graph import load_graph, remove_direct_self_dependencies, verify_source


def demand(ok, message):
    if not ok:
        raise AssertionError(message)


def run():
    rng = random.Random(202609254)
    counts = dict(graphs=0, cyclic_graphs=0, representative_assignments=0,
                  cap_snaps=0, enabling_comparisons=0, forced_snaps=0,
                  threshold_decisions=0, mixed_radix_roundtrips=0,
                  scale_checks=0, infeasible_graphs=0, mandatory_checks=0)
    digest = hashlib.sha256()
    for n in range(1,6):
        for mode in (True,False):
            for _ in range(40):
                g = random_graph(rng, n, mode)
                g = Graph({c:tuple(Node(x.name,x.cost%4,x.children) for x in ns)
                           for c,ns in g.classes.items()},g.roots)
                raw = PriceSpectrum(g,4)
                red = PriceSpectrum(g,4,propagate=True)
                core = raw.core
                exact = exhaustive(g)
                vectors, assignments = prior.all_local_vectors(g,core.core)
                opt = min(map(sum,vectors),default=None)
                demand(opt==exact['cost'], 'Independent optimum mismatch.')
                # Every valid complete representative choice must use declared mandatory classes.
                cs = sorted(core.g.classes)
                for ns in itertools.product(*(core.g.classes[c] for c in cs)):
                    try: _,used=core.g.check({c:x.name for c,x in zip(cs,ns)})
                    except ValueError: continue
                    demand(red.mandatory<=set(used),'Unsound mandatory-class inference.')
                    counts['mandatory_checks'] += 1
                locals_by_mask = [core.local(m)[0] for m in range(1<<len(core.core))]
                for b in allocations(len(core.core),4):
                    snapped = raw.snap(b)
                    demand(sum(snapped)<=sum(b),'Snapping raised price.')
                    for m,vals in enumerate(locals_by_mask):
                        for j,x in enumerate(vals):
                            demand((x<=b[j])==(x<=snapped[j]),'Enabled transition changed.')
                            counts['enabling_comparisons'] += 1
                    before=raw.grounding.close(b,witness=False)
                    after=raw.grounding.close(snapped,witness=False)
                    demand(before['mask']==after['mask'],'Grounding changed after price snap.')
                    expected=any(all(x<=y for x,y in zip(v,b)) for v in vectors)
                    demand(before['success']==expected,'Direct cap semantics mismatch.')
                    if not red.infeasible_lower and all(x>=lo for x,lo in zip(b,red.lower)):
                        forced=red.snap(b)
                        got=red.grounding.close(forced,witness=False)
                        demand(before['mask']==got['mask'],'Forced-grounding changed fixed point.')
                        demand(sum(forced)<=sum(b),'Forced caps raised cost.')
                        counts['forced_snaps'] += 1
                    counts['cap_snaps'] += 1
                for k in range(5):
                    obj = PriceSpectrum(g,k,propagate=True)
                    result = obj.decision()
                    expected = opt is not None and opt<=k
                    demand(result['success']==expected,'Threshold completeness failed.')
                    if expected:
                        value,_=g.check(result['choices'])
                        demand(value==result['cost'] and value<=k,'Invalid reconstructed witness.')
                    counts['threshold_decisions'] += 1
                    digest.update(bytes([expected]))
                for i in range(red.cartesian_size):
                    demand(red.encode(red.decode(i))==i,'Mixed-radix inverse failure.')
                    counts['mixed_radix_roundtrips']+=1
                factor=1000003
                scaled_obj=PriceSpectrum(scaled(g,factor),4*factor,propagate=True)
                demand(tuple(tuple(x*factor for x in v) for v in red.alphabets)==scaled_obj.alphabets,
                       'Cost scaling changed labels.')
                demand(red.cartesian_size==scaled_obj.cartesian_size,'Scale changed domain size.')
                for rank in sorted({0,red.cartesian_size//2,red.cartesian_size-1}):
                    if rank<0 or rank>=red.cartesian_size:continue
                    b=red.decode(rank); bb=scaled_obj.decode(rank)
                    demand(tuple(x*factor for x in b)==bb,'Scaled decoding failed.')
                    demand(red.grounding.close(b,witness=False)['mask']==scaled_obj.grounding.close(bb,witness=False)['mask'],
                           'Scaled construction changed.')
                    counts['scale_checks']+=1
                counts['graphs']+=1
                counts['cyclic_graphs']+=not g.support_acyclic()
                counts['infeasible_graphs']+=opt is None
                counts['representative_assignments']+=assignments
    public=remove_direct_self_dependencies(load_graph())
    brute=exhaustive(public)
    grid=comb(1205+len(SharingCore(public).core),len(SharingCore(public).core))
    reports=[]
    for propagate in (False,True):
        obj=PriceSpectrum(public,1205,propagate=propagate)
        answer=obj.decision()
        demand(answer['success'] and answer['cost']==brute['cost']==1205,'Public optimum changed.')
        hist=obj.cost_histogram()
        reports.append(dict(propagate=propagate, alphabets=[list(v) for v in obj.alphabets],
            cartesian_size=obj.cartesian_size, histogram=hist,compiler=obj.stats,
            forced_classes=[obj.core.core[j] for j in obj.fixed],
            mandatory_classes=sorted(obj.mandatory),certificate=answer))
    examples=[]
    for n in (2,4,8,12):
        g=exponential_spectrum(n)
        k=(1<<n)-1
        obj=PriceSpectrum(g,k)
        j=obj.core.index['root']
        demand(obj.prices[j]==tuple(range(1<<n)),'Exponential spectrum missing values.')
        fast=PriceSpectrum(g,k,propagate=True)
        cert=fast.decision()
        demand(fast.cartesian_size==1 and cert['cost']==n,'Forced example not solved.')
        # Independent graph identity check of the supplied optimum certificate.
        witness={f's{i}':f'input{i}' for i in range(n)}
        witness.update({f'p{i}':f'use{i}' for i in range(n)});witness['root']='join'
        demand(g.check(witness)[0]==n,'Easy-family certificate failed.')
        examples.append(dict(n=n,graph_classes=len(g.classes),core_size=len(obj.core.core),
            local_root_prices=len(obj.prices[j]),compiler=obj.stats,
            after_forced_domain=fast.cartesian_size,after_forced_compiler=fast.stats,
            optimum=n, scope='All n unit-price required roots give the lower bound; no hardness claim.'))
    persistent=[]
    for n in (2,4,6,8):
        g=persistent_spectrum(n);K=3**n-1
        obj=PriceSpectrum(g,K,propagate=True);root_idx=obj.core.index['root']
        demand(not obj.fixed,'Persistent example unexpectedly grounded.')
        demand(obj.prices[root_idx]==tuple(range(3**n)),'Ternary-sum spectrum differs.')
        minima=set()
        for mask in range(1<<n):
            cm=sum(1<<obj.core.index[f'b{i}'] for i in range(n) if mask>>i&1)
            minima.add(obj.core.local(cm)[0][root_idx])
        demand(len(minima)==1<<n,'Conditional breakpoint count differs.')
        witness={'root':'join'}
        witness.update({f'{p}{i}':f'{p}{i}paid' for i in range(n) for p in ('p','q')})
        demand(g.check(witness)[0]==K,'Independent componentwise optimum fails.')
        persistent.append(dict(n=n,classes=len(g.classes),root_price_spectrum=3**n,
            distinct_conditional_minima=len(minima),compiler=obj.stats,cartesian_size=obj.cartesian_size,
            exact_optimum=K,certificate=witness,
            scope='Each component costs min(2*3**i,2*3**i+1); polynomial classical solution.'))
    try:PriceSpectrum(persistent_spectrum(6),3**6-1,max_prices=64,propagate=True)
    except SpectrumLimit:persistent_guard=True
    else:raise AssertionError('Persistent compiler cap silently ignored.')
    try:PriceSpectrum(exponential_spectrum(12),4095,max_prices=64)
    except SpectrumLimit:guard=True
    else:raise AssertionError('Compilation cap silently ignored.')
    repaired=PriceSpectrum(exponential_spectrum(12),4095,max_prices=64,propagate=True)
    demand(repaired.decision()['cost']==12,'Safe preprocessing did not bypass the expensive compiler.')
    # Positive-cost cycle: relaxed closure alone can underprice an acyclic implementation.
    cycle=Graph({'r':(Node('r',0,('A','B')),),
      'A':(Node('AB',1,('B',)),Node('Al',10)),
      'B':(Node('BA',1,('A',)),Node('Bl',10))},('r',))
    demand(exhaustive(cycle)['cost']==11,'Cycle optimum changed.')
    cy=PriceSpectrum(cycle,11,propagate=True)
    demand(cy.decision()['cost']==11,'Positive-cycle cap failed.')
    return dict(finite_checks=counts,outcome_sha256=digest.hexdigest(),
        public=dict(source=verify_source(),cost=1205,old_grid=grid,
                    old_grid_bits=(grid-1).bit_length(),old_grid_log2=round(log2(grid),6),
                    representative_assignments=brute['assignments'],variants=reports,
                    scope='Known easy calibration, no native full-solver or useful advantage result.'),
        exponential_spectra=examples,persistent_spectra=persistent,
        persistent_compiler_guard=persistent_guard,compiler_limit_guard=guard,
        positive_cycle=dict(relaxed_dependency_closed_cost=2,acyclic_optimum=11,
                            budget_certificate=cy.decision()),
        claims_not_established=['novelty','best_classical_separation','large_native_benchmark',
                                'complete_quantum_gate_counts','useful_quantum_advantage'])


if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not use -O/-OO.')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if a.output.exists():raise SystemExit('Refusing to overwrite stored output.')
    report=run()
    a.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report['finite_checks'],sort_keys=True))
