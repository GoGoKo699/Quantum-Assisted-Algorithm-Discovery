# Opening note: discovering a representation rather than optimizing inside one

Status: exploratory question, not an algorithm or novelty claim.

The earlier work largely fixed a representation of candidate programs, retained strong classical simplifications, and asked whether quantum search could accelerate the remaining choices. That yielded useful classical structure but no established useful quantum advantage. Phase 2 should examine whether the representation itself is the quantum-discoverable object.

A concrete question is:

> Can a quantum computer find a compact change of representation that turns a repeatedly needed classical operation into independent smaller operations?

If successful, the quantum output is the transformation and the resulting rule for classical execution. No quantum computer is needed during later uses. This is not yet a specified workload: the task, allowed transformations, and computational saving all remain to be established.

## Minimal three-step story

1. A classically specified operation has a useful structural relation that is not cheaply supplied with the input.
2. A circuit-model quantum procedure reveals that relation at an explicitly affordable total cost.
3. The relation gives a verified classical implementation with a consequential benefit.

All three steps must concern the same inputs, accuracy, and intended use. If the third step does not follow, the output is merely interesting information. If classical algebra finds the relation cheaply, there is no quantum discovery advantage. If the relation is hidden by an artificial encoding, the task is not yet independently useful.

## Immediate adversarial tests

**Explicit description versus oracle.** An oracle lower bound does not prevent an algorithm from inspecting the source circuit or coefficients. A useful explicit-input example must address that freedom.

**Structure detection versus cheap execution.** Detecting a symmetry or low-rank feature does not automatically reduce the execution cost. A full classical method has to be derived, including the cost of the change of representation.

**Discovery access.** Coherent function evaluation must be compiled from what the classical competitor receives. Do not assume a state containing all candidate qualities or a normalized structural witness is already available.

**Classical competitors.** Ordinary linear algebra, randomized probing, symbolic simplification, tensor factorizations, and known decomposition algorithms are potential competitors, not methods to suppress. A task that they solve cheaply is a calibration, not a hard instance.

**Reuse.** The compiled rule must apply to a meaningful collection of later inputs. A short list of precomputed answers does not by itself meet this criterion.

## Companion question

Could a useful classical description instead be expensive to construct because its discovery requires a quantum evolution, while the description's later use is simple? That possibility is distinct from optimizing an arithmetic circuit. It must account for generating the quantum input and for a classical competitor with comparable data access. It remains open for this exploration; no particular physical model or learning architecture is selected.

## Next action

Find one primitive example for which the quantum-specific information and the resulting classical shortcut can both be written down. Search the relevant primary literature before claiming a new mechanism. Prefer a sharp explanation or decisive counterexample to another large implementation. If neither opening route yields such an example, revise the mechanism rather than dress a standard search bound in more notation.
