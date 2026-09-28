# Sampling encoding audit 09: compute internal wires; do not guess them

28 September 2026. Parent baseline: `0e02a52f2e52fb5541018e47c5ba4401ca5ea58d`.
Working branch: `research/prx-quantum-phase2`. Manuscript stays on hold.

**Outcome:** an executed source-level diagnostic identifies and removes an
artificial rejection penalty in a naive full-assignment quantum sampler. The
planned native Manthan/CMSGen comparison remains incomplete because installation
inputs could not be transferred. This is neither a synthesis speedup nor a new
technique. It refines the producer in [Note 08](SAMPLING_TO_VERIFIED_LOGIC_08.md)
without abandoning useful sampling or the classical-deployment objective.

## 1. What was and was not acquired

The upstream Manthan commit was pinned to
`8d7ad340436255f9d0a7f6920f54f9422e502a0a`. Its installation script builds native
dependencies from source. A runtime `git ls-remote` attempt failed with exit 128
and `Could not resolve host: github.com`; raw-file/codeload transfer attempts also
failed. The latest successful upstream dependency workflow returned no artifacts
from the artifact-list action. No complete installation or official smoke test
was performed, and no native pipeline phase time can be reported.

GitHub text reads worked. The examined `usb-phy-fixpoint-1.qdimacs` header declares
1631 variables and 4395 clauses. Its X prefix is 1-334 and Y prefix is 335-1630.
The absence of index 1631 from these prefixes is recorded, not silently repaired.
It does not affect the selected definitions below.

The complete benchmark was NOT copied into the runtime or hash-verified there.
The executed fixture transcribes only lines 4-379: the first 376 clauses. Its
origin, normalization, source blob and retained upstream license are in
[provenance](../../experiments/sampling_encoding_v1/PROVENANCE.md). A separate
optional verifier mode can compare against a complete source file when available.
The fixture must not be advertised as the full benchmark.

The filename is not sufficient application provenance. A search found a similarly
named fixed-point benchmark in the Wintersteiger SMT-LIB family, but did not
establish the translation or original signal mapping of this QDIMACS file.
No claim of synthesizing a deployable USB component follows. This instance is
used only for a cheap encoding check, not promoted as the useful target.

## 2. An exact property of the inspected clauses

They define 85 output variables, numbered 502-586, as an acyclic Boolean circuit:
18 AND gates with signed inputs, one OR gate, and 66 XOR gates. The definitions
ultimately depend on 119 original X bits. The largest AND has 25 inputs.
For example, the first three clauses state exactly

$$
z_{502}=x_2\land\neg x_3.
$$

For every assignment to the other variables there is exactly one assignment to
these 85 bits satisfying this prefix D. This follows inductively through the
ordered gate definitions. The checker matches each complete gate's CNF clauses,
not just one direction of an implication; deleting a defining clause is rejected.

Since every satisfying assignment of the full formula F must satisfy D, a prior
that independently chooses every assignment bit uniformly has

$$
p_{\rm raw}=\Pr[F]\leq\Pr[D]=2^{-85}.
$$

This bound uses only the inspected prefix; it is not an exact count of solutions
to F. Nor does it claim that all output bits of F are uniquely defined.

For fixed-round ordinary Grover amplification of this RAW uniform prior,

$$
P_t=\sin^2((2t+1)\theta)\leq(2t+1)^2p_{\rm raw},
\qquad \sin^2\theta=p_{\rm raw}.
$$

Thus achieving success at least 1/2 requires at least 2^41 Grover rounds under
that particular preparation/reflection contract. This excludes oracle/gate cost
and can be an extremely loose necessary bound. It is NOT a lower bound on
quantum synthesis, structured quantum sampling, all amplitude-amplification
strategies, or the native classical tools. It exposes a bad encoding choice.

The prior note specifies a general product-prior producer, not an implemented
circuit for this file. The result here concerns its naive uniform full-variable
specialization, not a bug asserted against every producer covered by Note 08.

## 3. Remove the artificial difficulty on both sides

Write the remaining assignment bits as u and the defined bits as g(u). Instead
of guessing g, compute it reversibly:

$$
A_D|0\rangle=2^{-|u|/2}\sum_u|u,g(u)\rangle.
$$

Use the reflection implemented by A_D and its inverse when amplifying the
remaining condition. Because the extension u -> (u,g(u)) is one-to-one,

$$
p_{\rm structured}=2^{85}p_{\rm raw}.
$$

Conditioning either uniform construction on F gives the SAME uniform law on
full satisfying assignments, when that set is nonempty. This removes only the
known gate-guessing penalty. The remaining acceptance mass may still be small;
its value, useful training coverage and native synthesis costs are unmeasured.

The executed code constructs a straight-line reversible evaluator for this prefix
using 149 X, 132 CX and 129 CCX gates: 410 elementary reversible gates in total,
with at most 23 reusable clean AND-chain scratch bits. Outputs initially contain
zero. An inverse traversal clears the computed wires and restores the input.
These counts cover ONLY the inspected prefix evaluator, not preparation of all
free registers, the full relation oracle, reflection, sampling, training, or
fault-tolerant error correction. They are circuit-description counts, not hardware
execution times. No state-vector simulation of the entire circuit was attempted.

A classical algorithm can evaluate the same circuit. This correction is therefore
not our quantum advantage. Both competitors must be allowed to exploit explicit
definitions, deterministic propagation and uniquely defined functions. Manthan2's
published design already uses unique-function extraction by interpolation [1];
we have not measured whether its particular implementation extracts this prefix.

For nonuniform product weights, deleting the dependent-bit factors can change the
training law. To preserve the original weighted conditional distribution, the
induced weight on u includes the factors evaluated at g(u). Efficient preparation
of that induced law is a separate task, not established here. Do not apply the
uniform 2^85 ratio to arbitrary weighted CMSGen calls.

## 4. Executed checks and their limits

```sh
python experiments/sampling_encoding_v1/verify.py
python experiments/sampling_encoding_v1/verify.py --native
```

The default standard-library checker matches all 376 clauses to complete gate
identities, checks 6320 local truth assignments (larger AND handled by exact
clause-pattern identity), and compares classical and reversible evaluation on
128 fixed-seed basis-input controls. All scratch is clean and uncomputation
restores the initial state. Flipping each defined output individually gives
10,880 rejected negative controls. Four malformed/incomplete-gate controls pass.

The native mode uses the already installed Z3 4.13.3.0 C library. It returned
UNSAT for both mismatch formulas: D and not(gate equations), and vice versa.
These are prefix-equivalence checks, NOT native Manthan/CMSGen, full-instance
synthesis, or independent UNSAT-proof replay. A structural induction gives the
mathematical uniqueness argument; finite input tests alone do not prove it.

The final native checker was run twice and gave identical
[JSON](../../experiments/sampling_encoding_v1/REPORT.json). Default mode passed.
Python -O/-OO, an altered prefix, and an incorrect complete-source file were
rejected. Successful `--source` validation was NOT run. Source SHA256 is
`35ebbf68d01b451ee6e6b2c938f8bf0a500cf32b2f91fcd58cc0aa4aeb346348`;
report SHA256 is
`38280669662211b8bccdba4709644a8bc6d9f4cc96deaa6f8bc1ad0556c145d5`.
Root, earlier sampling and historical scientific suites were not rerun; their
code and reference results remain unchanged. No trained classifier, verified
full program, sample-source ablation or performance improvement is claimed.

## 5. Next decision: measure the remaining opportunity

Keep the sample-to-verified-logic contract, but require a structure-preserving
producer rather than raw guesses of explicit internal wires. Do not use a huge
raw rejection penalty as evidence of a useful discovery bottleneck.

The outstanding experiment remains the instrumented native classical baseline,
with preprocessing and unique extraction enabled, plus original benchmark-signal
provenance. Separate sample acquisition, learning, repair and proof checking.
Permit direct synthesis and task-equivalent classical example sources. A tiny
sampling-time fraction would constrain same-law acquisition gains, while a change
of useful sample law would need a different controlled test.

A working native execution environment is now a concrete operational prerequisite,
not evidence that the underlying research problem is hard. A local terminal
integration was located but not connected; no user machine was accessed. Do not
keep replacing the missing baseline with additional small logic demonstrations.
No new repository or spin-off is justified by this diagnostic.

## Sources inspected

[1] Golia et al., *Engineering an Efficient Boolean Functional Synthesis Engine*,
arXiv:2108.05717 (2021), primary abstract: unique-function extraction and other
classical improvements. https://arxiv.org/abs/2108.05717

[2] Manthan upstream source at the pinned commit: setup script, benchmark header
and selected clauses, repository tree and LICENSE. No native upstream program ran.
https://github.com/meelgroup/manthan/tree/8d7ad340436255f9d0a7f6920f54f9422e502a0a

[3] Source-line membership is attributed through [2]; the verified local objects
are the explicitly transcribed prefix and independent diagnostic, not a full
benchmark import. Existing reversible evaluation, gate recovery and amplification
principles are being applied, not claimed as new techniques or an exhaustive
novelty result. No PDF was analyzed in this checkpoint.
