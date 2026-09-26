"""Execute a saved question-and-action tree using ONLY a sensor callback.

The callback supplies one binary patch observation. No image label, row index,
other observations, or hidden simulation randomness is passed to the policy.
This is an interface demonstration, not a production image recognizer.
"""
from __future__ import annotations
from collections.abc import Callable
from typing import Any


def decide(tree: dict[str, Any], observe: Callable[[int], bool | int],
           max_queries: int = 4) -> tuple[int, tuple[int, ...]]:
    if max_queries < 0:
        raise ValueError('The query budget must be nonnegative.')
    node = tree
    used: list[int] = []
    while 'query' in node:
        if len(used) == max_queries:
            raise ValueError('Policy exceeds the declared observation budget.')
        q = node['query']
        if type(q) is not int or not 0 <= q < 16:
            raise ValueError('Invalid patch index.')
        bit = observe(q)
        if bit not in (0, 1, False, True):
            raise ValueError('The observation must be binary.')
        used.append(q)
        node = node['yes'] if bit else node['no']
    answer = node.get('label')
    if type(answer) is not int or not 0 <= answer <= 9:
        raise ValueError('Invalid terminal digit label.')
    return answer, tuple(used)
