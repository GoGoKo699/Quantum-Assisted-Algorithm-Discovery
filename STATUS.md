# Claim ledger

## Latest: complete eleven-bank count/depth screen, 25 September 2026

**Research decision:** retire these eleven small filter-bank arithmetic-count/depth tasks as quantum-advantage candidates. Keep quantum-assisted discovery of useful reusable classical methods as the objective. This is not a rejection of all constant-multiplier synthesis or of the broader direction.

### Established in the stated model

- All eleven published numerical coefficient banks transcribed with pinned provenance; repeated coefficients removed only under free-copy semantics. The source CSV's exact Git blob was checked locally. No upstream solver code imported.
- An exact two-layer normal form using first-layer coefficients 2^s +/- 1 and a monotone helper-coverage recurrence. Eight banks are feasible at depth two; the largest retained antichain has eleven helper sets.
- Exact depth-aware helper search completes the three remaining cases and establishes every nondominated (binary-node count, arithmetic depth) pair under the declared coefficient/shift bounds. All banks attain the established signed-digit lower bound on minimum depth.
- Fifteen explicit Pareto circuits, including (5,4)/(6,3) for the 5x5 Gaussian bank and (25,3) for the largest lowpass bank. These are not claimed as new circuits or records.
- Agreement with independent enumeration on 1,536 small circuit decisions and 972 helper subsets. Exact integer certificate checking plus 384 signed inputs per Pareto circuit, 5,760 network evaluations.
- Full deterministic reports regenerated and checked. The new synthesis screen took about 0.27 seconds in one local Python run; this is not a portable or cross-solver speed comparison.

### Boundaries

Positive odd fundamentals are below 2^B, both shifts are at most B, and copying/signs/constant shifts/fanout/live storage are free. The objective counts binary arithmetic nodes and their longest dependency chain. Exact count optima are bounded-model statements. The signed-digit minimum-depth bound is more general, but does not imply clock-frequency or bit-area optimality.

Subset dominance and eager target production must not be transferred unchanged to bit-area, register, routing or physical-delay objectives. Covering, signed-digit depth bounds, positive closure, reverse search, and generic quantum backtracking are prior tools, not new general theorem claims.

### Not completed or established

- Native execution of current SAT-CMM, RPAG/PAGSuite or jMCM. Interfaces were inspected, but the source/package/runtime access did not support execution here. Independent scripts are not a substitute claimed as an upstream run.
- A surviving unsupplied, independently valuable routine with a documented strong-classical discovery shortfall.
- A complete quantum implementation of the new formulations, practical quantum resource estimates or useful advantage.
- New arithmetic identities, novelty of these recovered routines, physical implementation, measured clock speed, power, area or a deployed performance gain.

## Historical evidence

The guided-search, target-closure, unique-helper and first-filter experiments remain unchanged in their versioned directories, with their manifests and source attribution. Earlier ledger snapshots remain in Git history. Known-identity reconstruction, reversible-operator checks, canonical-parent enumeration and generic-SMT timeouts must not be mistaken for useful quantum advantage. The old raw/guided quantum counts apply only to the old constructions.

The latest turn reran the supplied first-filter default verifier and all new checks. It did not rerun the optional native-Z3 check, remote target-closure verifier, or all historical long benchmarks. Prior results are historical evidence, not newly repeated experiments.
