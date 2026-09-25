# Publication progress 03: scale-invariant search and a matched classical comparison

25 September 2026. Additive continuation on research/sharing-core-publication.
This document updates, not overwrites, PLAN.md and the previous theorem section.

## What moved

The cyclic grounded-budget formulation can now use finite alphabets of local
prices rather than every integer cap. Exact downward snapping preserves all
local enabling decisions. Mandatory lower-price grounding safely fixes some
caps before compilation. Uniform rescaling leaves label counts unchanged.

A complete indexed predicate now includes reversible constant-division decoding,
price lookup, total-budget checking, grounding, phase marking and uncomputation.
A standard diffusion implementation is also counted. These are component and
iteration-level logical resources, not a measured discovery advantage. The
small public calibration remains classically easy.

The comparison audit found a material modeling distinction: the OOPSLA 2024
5^w treewidth algorithm does not impose acyclic extraction from cyclic support.
Its authors explicitly discuss the more expensive reachability extension. The
2^(O(w^2)) acyclicity-aware bound is the relevant comparison for cyclic support.
This is not a correction of their theorem, and it does not imply our method wins.

## The strengthened candidate statement

Given an explicit e-graph, nonnegative integer costs, and compiled local price
alphabets of total size P and product Q, an exact threshold problem can be
searched quantumly in O(sqrt(Q)*poly(N,P,log K)) time after price-compilation work
A, with polynomial workspace in the compiled representation. Costs of compiling,
storing and reading those alphabets must be included. Mixed-radix indexing
eliminates duplicate numeric labels; it does not create a new quantum search law.

The conditional bound is useful only if A and P are controlled and if Q is a
better remaining representation than those exploited classically. We have not
established those conditions on a difficult useful workload.

## A non-negotiable limitation

An explicit local-price list can be exponential even for a separable graph whose
optimum is immediate. The new proof gives an O(n)-class family with 3^n local
prices and 2^n distinct conditional minima; a direct componentwise algorithm
solves it. The effect survives the particular mandatory-grounding prepass.
Therefore no blanket polynomial-preprocessing or original-input polynomial-space
claim can be made for explicit spectrum compilation. A fail-fast compiler limit
is not a proof that no implementation exists.

## Current publication assessment

Gate 1: advanced the SAME-PROBLEM comparison and made the novelty obligations
more precise. Priority/significance of the combined parameterization is unresolved.
Grounding, sparse cost-set propagation, mandatory inference and amplitude
amplification are not claimed as new general techniques.

Gate 2: the cost-unit pathology is removed; explicit indexing/lookup closes the
previous component gap. The theorem must keep A and P. One Grover iteration is
not one successful discovery, and no physical resources are provided.

Gate 3: unchanged. The public graph is calibration only. No new full native
SmoothE/e-boost or large representative benchmark was executed. Downloads failed;
a graph read through the connector is not a graph processed in an experiment.

## Next decisive step within this branch

Do not open a new application or repeat supplied-identity recovery. Compare this
formulation with structural decomposition and a strong native/parameterized
extractor on the same semantics. Establish either (a) a justified, efficiently
compilable price-diversity regime with an original complete advantage result,
or (b) an implicit representation/search that avoids enumerating all price
thresholds. Cost catalogs cannot be an unpriced preprocessing oracle.

Draft against one central theorem, not a list of previous probes. An original,
consequential theory result need not wait for hardware, but this standard-search
corollary plus calibration is not yet an established publishable advance. No
submission, public novelty announcement, outside contact, or paid work is authorized.
