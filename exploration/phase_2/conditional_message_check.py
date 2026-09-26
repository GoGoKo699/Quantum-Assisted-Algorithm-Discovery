"""Exact checks of a public HMM's posterior and evidence-conditioned generator.

Mathematical transcription, NOT execution of Pluck or a quantum algorithm.
The two-state HMM is classically easy. All probability checks use fractions;
reported decimal conversions are presentation only. Standard library only.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path

# State 0=False, 1=True, matching the pinned programs/hmm.pluck.
PRIOR = (F(1, 2), F(1, 2))
TRANSITION = ((F(2, 5), F(3, 5)), (F(3, 5), F(2, 5)))
TRUE_EMISSION = (F(2, 5), F(9, 10))


def emission(state: int, observed: int) -> F:
    return TRUE_EMISSION[state] if observed else 1 - TRUE_EMISSION[state]


def joint(path: tuple[int, ...], obs: tuple[int, ...]) -> F:
    if len(path) != len(obs) or not path:
        raise ValueError('Nonempty matching sequences required.')
    mass = PRIOR[path[0]] * emission(path[0], obs[0])
    for t in range(1, len(path)):
        mass *= TRANSITION[path[t-1]][path[t]] * emission(path[t], obs[t])
    return mass


def messages(obs: tuple[int, ...]) -> dict:
    if not obs or any(type(x) is not int or x not in (0, 1) for x in obs):
        raise ValueError('Expected a nonempty binary observation tuple.')
    alpha = [[PRIOR[s] * emission(s, obs[0]) for s in (0, 1)]]
    for observed in obs[1:]:
        alpha.append([sum(alpha[-1][s] * TRANSITION[s][v] for s in (0, 1))
                      * emission(v, observed) for v in (0, 1)])
    beta = [[F(1), F(1)] for _ in obs]
    for t in range(len(obs)-2, -1, -1):
        beta[t] = [sum(TRANSITION[s][v] * emission(v, obs[t+1]) * beta[t+1][v]
                       for v in (0, 1)) for s in (0, 1)]
    evidence = sum(alpha[-1])
    initial = [alpha[0][s] * beta[0][s] / evidence for s in (0, 1)]
    conditional = [[[TRANSITION[s][v] * emission(v, obs[t+1]) * beta[t+1][v]
                     / beta[t][s] for v in (0, 1)] for s in (0, 1)]
                   for t in range(len(obs)-1)]
    if sum(initial) != 1 or any(sum(row) != 1 for step in conditional for row in step):
        raise AssertionError('Conditioned generator lost normalization.')
    marginals = [[alpha[t][s] * beta[t][s] / evidence for s in (0, 1)]
                 for t in range(len(obs))]
    if any(sum(row) != 1 for row in marginals):
        raise AssertionError('Smoothing distribution lost normalization.')
    return dict(evidence=evidence, alpha=alpha, beta=beta, initial=initial,
                conditional=conditional, marginals=marginals)


def compiled_probability(path: tuple[int, ...], model: dict) -> F:
    p = model['initial'][path[0]]
    for t in range(len(path)-1):
        p *= model['conditional'][t][path[t]][path[t+1]]
    return p


def run() -> dict:
    histories = sequences = queried_marginals = 0
    for length in range(1, 8):
        for obs in product((0, 1), repeat=length):
            model = messages(obs)
            weights = {path: joint(path, obs) for path in product((0, 1), repeat=length)}
            z = sum(weights.values())
            if z != model['evidence']:
                raise AssertionError('Forward likelihood differs from direct path sum.')
            for path, mass in weights.items():
                if compiled_probability(path, model) != mass / z:
                    raise AssertionError('Compiled conditional generator is incorrect.')
                histories += 1
            for t in range(length):
                direct = sum(mass for path, mass in weights.items() if path[t] == 1) / z
                if direct != model['marginals'][t][1]:
                    raise AssertionError('Smoothing marginal differs from path enumeration.')
                queried_marginals += 1
            sequences += 1

    source = messages((1,)*50)
    p = source['evidence']
    # Coupled histories can still be summarized by two states at every time.
    public = dict(
        source_repository='pluck-lang/Pluck.jl',
        source_commit='2ac3400e24d7fa67d87f3ef43265bda2f311e1bc',
        source_path='programs/hmm.pluck',
        source_blob='644473d86d870fece95850b07bfc88bafb78fd4e',
        transition=[[str(x) for x in row] for row in TRANSITION],
        true_emission=list(map(str, TRUE_EMISSION)),
        observations=50, observation_pattern='all True', hidden_histories=1 << 50,
        exact_evidence=str(p), evidence_decimal=float(p),
        inverse_evidence=1/float(p), inverse_sqrt_evidence=1/math.sqrt(float(p)),
        eleventh_hidden_state_probability=str(source['marginals'][10][1]),
        eleventh_hidden_state_probability_decimal=float(source['marginals'][10][1]),
        filtered_eleventh_probability_decimal=float(source['alpha'][10][1]/sum(source['alpha'][10])),
        forward_transition_terms=4*49, backward_transition_terms=4*49,
        compiled_conditional_transition_entries=4*49,
        note='Counts are elementary recurrence terms, not timings or gate counts. '
             'Input transition probabilities have finite rational descriptions. '
             'No full 50-state-path enumeration or native Pluck run was performed.')

    # Exact Bayesian update cannot be a fixed unitary on arbitrary sqrt-prior states.
    # Same likelihood (1/16,1) acts on priors (1/2,1/2), (4/5,1/5).
    likelihood = (F(1,16), F(1))
    update = []
    for prior in ((F(1,2), F(1,2)), (F(4,5), F(1,5))):
        z = sum(a*b for a,b in zip(prior, likelihood))
        post = [a*b/z for a,b in zip(prior, likelihood)]
        if sum(post) != 1:
            raise AssertionError('Bayes update failed.')
        update.append(dict(prior=list(map(str, prior)), success_probability=str(z),
                           posterior=list(map(str, post))))

    # Data can create a joint dependence even when every individual marginal is unchanged.
    prior_pairs = {x:F(1,4) for x in product((0,1),repeat=2)}
    posterior_pairs = {x:(F(1,2) if sum(x)==1 else F(0)) for x in prior_pairs}
    tv = sum(abs(prior_pairs[x]-posterior_pairs[x]) for x in prior_pairs)/2
    if tv != F(1,2):
        raise AssertionError('Joint-dependence example differs.')
    # Full hidden-history square-root posterior factors through the boundary state;
    # check the associated left/right factorization numerically only as exact
    # probability products, avoiding irrational square-root arithmetic.
    # Given a split at t, P(path,y)=left(prefix)*right(suffix|boundary).
    cuts_checked=0
    for obs in ((1,0,1,1,0,1),(0,)*6):
        for path in product((0,1),repeat=6):
            for cut in range(1,6):
                left=joint(path[:cut],obs[:cut])
                right=F(1)
                for t in range(cut,6):
                    right*=TRANSITION[path[t-1]][path[t]]*emission(path[t],obs[t])
                if left*right != joint(path,obs):
                    raise AssertionError('Boundary factorization failed.')
                cuts_checked+=1
    return dict(
        scope='Exact small-model inference and interface checks. No quantum speedup, learned model, '
              'native Pluck benchmark, or factorial-HMM implementation is established.',
        exhaustive=dict(observation_sequences=sequences,path_probability_comparisons=histories,
                        marginal_comparisons=queried_marginals,
                        boundary_factorizations=cuts_checked, arithmetic='fractions.Fraction'),
        public_hmm=public,
        likelihood_filter=update,
        explaining_away=dict(prior_marginals=['1/2','1/2'],posterior_marginals=['1/2','1/2'],
                             posterior_equal_one_probability='1',independent_approximation_equal_one_probability='1/2',
                             joint_total_variation=str(tv),scope='Elementary two-bit example, classically trivial.'))


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite an existing report.')
    result=run()
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps(result,indent=2,sort_keys=True))
