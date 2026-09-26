"""Exact evidence checks, not a native Pluck run or a quantum speed benchmark.

The published task-000 kernel is transcribed mathematically. Only mixture-mask
choices are enumerated; geometric probabilities are summed analytically.
The finite Grover control and independent-noise tests use invented small models.
Python standard library only. Output files are created exclusively.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

TRAIN = ((1,3,0,4), (1,2,11,4), (1,2,3,4), (1,2,0,7))
SOURCE_REF = '4258adf926055f4e2415c33025ad04da0b5e312d'
SOURCE_PATH = 'data/figure5/out/fuzz-datasets/2024-11-13/04-07-50/dataset.json'


def geom(k: int) -> F:
    if type(k) is not int or k < 0:
        return F(0)
    return F(1,5)*F(4,5)**k


def direct_likelihood(y, copy=F(4,5)) -> F:
    if len(y) != 4:
        return F(0)
    out = F(1)
    for j, value in enumerate(y,1):
        out *= copy*int(value==j)+(1-copy)*geom(value)
    return out


def sum_masks(y, copy=F(4,5)) -> F:
    if len(y) != 4:
        return F(0)
    total=F(0)
    for branches in product((0,1),repeat=4):
        mass=F(1)
        for j,(value,is_copy) in enumerate(zip(y,branches),1):
            mass *= copy*int(value==j) if is_copy else (1-copy)*geom(value)
        total+=mass
    return total


def posterior(prior, likelihood):
    weights=[p*l for p,l in zip(prior,likelihood)]
    if sum(weights)<=0:
        raise ValueError('Evidence must have positive total mass.')
    return [w/sum(weights) for w in weights]


def tv(p,q):
    return sum(abs(x-y) for x,y in zip(p,q))/2


def run():
    # Check every 4-list over 0..5 plus all externally supplied training examples.
    checked=0
    for copy in (F(1,5),F(4,5)):
        for y in list(product(range(6),repeat=4))+list(TRAIN):
            if direct_likelihood(y,copy)!=sum_masks(y,copy):
                raise AssertionError('Factorized likelihood differs from exact mask sum.')
            checked+=1
    source_likelihoods=[direct_likelihood(y) for y in TRAIN]
    source_joint=F(1)
    for l in source_likelihoods: source_joint*=l
    # Modifying one source parameter makes TWO illustrative candidates, not the
    # upstream grammar prior or its original synthesis experiment.
    model_likelihoods=[]
    for copy in (F(1,5),F(4,5)):
        joint=F(1)
        for y in TRAIN: joint*=direct_likelihood(y,copy)
        model_likelihoods.append(joint)
    model_posterior=posterior([F(1,2),F(1,2)],model_likelihoods)

    # Joint conditioning over models and latent random choices, represented by
    # amplitudes relative to the common factor 1/sqrt(32).
    counts=(1,3); n=32
    marked=[r<counts[j] for j in range(2) for r in range(16)]
    amplitudes=[F(-1) if m else F(1) for m in marked]
    mean=sum(amplitudes)/n
    amplitudes=[2*mean-a for a in amplitudes]
    if sum(a*a for a in amplitudes)/n != 1:
        raise AssertionError('Grover normalization failed.')
    good_mass=[sum(amplitudes[j*16+r]**2/n for r in range(counts[j])) for j in range(2)]
    success=sum(good_mass)
    answer=[m/success for m in good_mass]
    expected=posterior([F(1,2)]*2,[F(c,16) for c in counts])
    if answer!=expected or success!=F(25,32):
        raise AssertionError('Global amplification altered within-success weights.')
    # Independent nuisance data affect exact-match probability, but not which
    # model explains the signal. Exhaustively check up to 6 extra fair bits.
    nuisance=[]; tapes=0
    for bits in range(7):
        hits=[0,0]
        for j in range(2):
            for r in range(16):
                for noise in range(1<<bits):
                    tapes+=1
                    hits[j]+=int(r<counts[j] and noise==0)
        prob=F(sum(hits),32*(1<<bits))
        post=[F(h,sum(hits)) for h in hits]
        if post!=expected or prob!=F(1,8*(1<<bits)):
            raise AssertionError('Nuisance cancellation identity failed.')
        nuisance.append({'noise_bits':bits,'evidence_probability':str(prob),
                         'model_posterior':list(map(str,post))})
    # Both models have nonzero evidence: giving each a successful trace and
    # keeping their prior masses is not a Bayesian model comparison.
    locally_normalized=[F(1,2),F(1,2)]
    if tv(locally_normalized,expected)!=F(1,4):
        raise AssertionError('Local-normalization negative control failed.')
    return {
      'scope':'Source-derived easy kernel and exact finite diagnostics; no native Pluck, LLM, quantum hardware, or advantage test.',
      'source_calibration':{
        'repository':'pluck-lang/PluckArtifact.jl','ref':SOURCE_REF,'path':SOURCE_PATH,
        'task':'000','dataset_blob':'8dd1275a589e83d9d2df9e95f5ca0de7f4314782',
        'training_examples':[list(y) for y in TRAIN],
        'semantics':'Copy position j with probability 4/5; otherwise independent Geometric(1/5) on nonnegative integers. Same probabilities for caps strictly above observed values. This does not reproduce upstream fuel/timeouts.',
        'exact_likelihoods':list(map(str,source_likelihoods)),
        'likelihood_decimals':[float(x) for x in source_likelihoods],
        'joint_likelihood':str(source_joint),'joint_likelihood_decimal':float(source_joint),
        'factorization_checks':checked,'mixture_masks_per_check':16,
        'variant_comparison':{'scope':'Illustrative restricted two-model family, not the original synthesis grammar.',
            'copy_probabilities':['1/5','4/5'],'equal_prior_posterior':list(map(str,model_posterior)),
            'posterior_decimals':[float(x) for x in model_posterior]}},
      'joint_conditioning':{
        'models':2,'latent_tapes_per_model':16,'accepted_counts':list(counts),
        'prior_evidence':'1/8','one_grover_iteration_success':str(success),
        'posterior':list(map(str,answer)),
        'separately_normalized_model_weights':['1/2','1/2'],
        'separate_normalization_tv':str(tv(locally_normalized,expected))},
      'nuisance_factor':{'full_tapes_checked':tapes,'cases':nuisance,
        'eighty_bit_noise_case':{'evidence_probability':str(F(1,8*(1<<80))),
                               'posterior':list(map(str,expected)),
                               'unnecessary_rejection_cost_multiplier':str(1<<80),
                               'unnecessary_square_root_cost_multiplier':str(1<<40)}}}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists(): raise SystemExit('Refusing to overwrite an existing report.')
    result=run()
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(result,indent=2,sort_keys=True))
