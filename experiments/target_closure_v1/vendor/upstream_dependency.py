"""Selected functions from trylogical/cn122_add55, MIT, Copyright 2026 Sam Karu.

Source: tools/synthesize_cn122_add55.py at commit
34949f9ce50a89a5ad6b47a17f5834ad5a87a2fb; original Git blob
abfeddcf7a19a3722832b2d171bd09f5d9bbbdc9.
This is an explicitly extracted module, NOT a byte-identical whole-file import.
Functions below are transcribed from the source; imports/header are local.
"""
from collections import deque
from typing import Sequence
Vector = tuple[int, ...]


def require(condition: bool, message: str) -> None:
    """Raise an explicit verification error even when Python uses -O."""
    if not condition:
        raise RuntimeError(message)


def basis(dimension: int) -> list[Vector]:
    return [tuple(int(i == j) for i in range(dimension)) for j in range(dimension)]


def add_vectors(a: Vector, b: Vector, sa: int = 1, sb: int = 1) -> Vector:
    return tuple(sa * x + sb * y for x, y in zip(a, b))


def projective(vector: Sequence[int]) -> tuple[Vector, int]:
    """Return (canonical, sign), with vector == sign*canonical."""
    vector = tuple(vector)
    for coefficient in vector:
        if coefficient:
            if coefficient > 0:
                return vector, 1
            return tuple(-x for x in vector), -1
    return vector, 1


def unique_targets(rows: Sequence[Vector], dimension: int) -> list[Vector]:
    basis_set = {projective(vector)[0] for vector in basis(dimension)}
    targets: list[Vector] = []
    for row in rows:
        canonical, _ = projective(row)
        if canonical not in basis_set and canonical not in targets:
            targets.append(canonical)
    return targets


def operation_for_result(
    forms: Sequence[Vector],
    left: int,
    right: int,
    left_sign: int,
    right_sign: int,
    desired: Vector,
    requirement: int,
) -> dict | None:
    raw = add_vectors(forms[left], forms[right], left_sign, right_sign)
    canonical, orientation = projective(raw)
    if canonical != desired:
        return None
    # raw = orientation*desired, so multiplying both operand signs by
    # orientation makes the gate's actual result exactly desired.
    return {
        "requirement": requirement,
        "left": left,
        "left_sign": left_sign * orientation,
        "right": right,
        "right_sign": right_sign * orientation,
    }


def dependency_options(targets: Sequence[Vector]) -> list[list[dict]]:
    forms = basis(9) + list(targets)
    masks = [0] * 9 + [1 << index for index in range(len(targets))]
    options: list[list[dict]] = []
    for target_index, target in enumerate(targets):
        target_options: list[dict] = []
        seen = set()
        for left in range(len(forms)):
            if masks[left] & (1 << target_index):
                continue
            for right in range(left):
                if masks[right] & (1 << target_index):
                    continue
                requirement = masks[left] | masks[right]
                for left_sign in (1, -1):
                    for right_sign in (1, -1):
                        option = operation_for_result(
                            forms, left, right, left_sign, right_sign,
                            target, requirement,
                        )
                        if option is None:
                            continue
                        key = tuple(option.values())
                        if key not in seen:
                            seen.add(key)
                            target_options.append(option)
        options.append(target_options)
    return options


def auxiliary_candidates(targets: Sequence[Vector]) -> dict[Vector, list[dict]]:
    forms = basis(9) + list(targets)
    masks = [0] * 9 + [1 << index for index in range(len(targets))]
    forbidden = {projective(vector)[0] for vector in basis(9)}
    forbidden.update(targets)
    candidates: dict[Vector, list[dict]] = {}
    for left in range(len(forms)):
        for right in range(left):
            requirement = masks[left] | masks[right]
            for left_sign in (1, -1):
                for right_sign in (1, -1):
                    raw = add_vectors(forms[left], forms[right], left_sign, right_sign)
                    candidate, orientation = projective(raw)
                    if not any(candidate) or candidate in forbidden:
                        continue
                    option = {
                        "requirement": requirement,
                        "left": left,
                        "left_sign": left_sign * orientation,
                        "right": right,
                        "right_sign": right_sign * orientation,
                    }
                    if option not in candidates.setdefault(candidate, []):
                        candidates[candidate].append(option)
    return candidates


def options_using_auxiliary(
    targets: Sequence[Vector], auxiliary: Vector
) -> list[list[dict]]:
    forms = basis(9) + list(targets) + [auxiliary]
    auxiliary_ref = len(forms) - 1
    auxiliary_bit = 1 << len(targets)
    masks = [0] * 9 + [1 << index for index in range(len(targets))] + [auxiliary_bit]
    result: list[list[dict]] = [[] for _ in targets]
    for target_index, target in enumerate(targets):
        for other in range(auxiliary_ref):
            if masks[other] & (1 << target_index):
                continue
            requirement = auxiliary_bit | masks[other]
            for auxiliary_sign in (1, -1):
                for other_sign in (1, -1):
                    option = operation_for_result(
                        forms,
                        auxiliary_ref,
                        other,
                        auxiliary_sign,
                        other_sign,
                        target,
                        requirement,
                    )
                    if option is not None and option not in result[target_index]:
                        result[target_index].append(option)
    return result


def reachable_path(options: Sequence[Sequence[dict]], target_count: int) -> list[tuple[int, dict]] | None:
    """Return a topological node/operation path; node target_count is the aux."""
    target_mask = (1 << target_count) - 1
    queue = deque([0])
    predecessor: dict[int, tuple[int, int, dict] | None] = {0: None}
    final_state = None
    while queue:
        state = queue.popleft()
        if state & target_mask == target_mask:
            final_state = state
            break
        for node, node_options in enumerate(options):
            if state & (1 << node):
                continue
            for option in node_options:
                if option["requirement"] & ~state:
                    continue
                next_state = state | (1 << node)
                if next_state not in predecessor:
                    predecessor[next_state] = (state, node, option)
                    queue.append(next_state)
                break
    if final_state is None:
        return None
    path: list[tuple[int, dict]] = []
    while final_state:
        item = predecessor[final_state]
        require(item is not None, "dependency-search predecessor is missing")
        previous, node, option = item
        path.append((node, option))
        final_state = previous
    path.reverse()
    return path
