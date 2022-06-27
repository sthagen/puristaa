# -*- coding: utf-8 -*-
"""Extract common prefix from sequence of strings and yield sequence of rest strings.

Implementation uses min-max left matching, single character backtracking policy and a list.
"""
import typing


@typing.no_type_check
def prefix_compression(texts, policy=None):
    """Return common prefix string abiding policy and compressed texts string list."""
    if not texts:  # Early out return empty prefix and empty sequence
        return '', texts

    if not isinstance(texts, (list, tuple)):
        texts = [texts]

    prefix_guard, first, last = 0, min(texts), max(texts)
    for pos, char in enumerate(first):
        if char == last[pos]:
            prefix_guard += 1
        else:
            break

    if policy:
        for here in range(prefix_guard - 1, -1, -1):
            if policy(first[here]):
                prefix_guard = here + 1
                break

    if not prefix_guard:  # Reduce memory pressure for all different texts
        return '', texts

    return first[:prefix_guard], [text[prefix_guard:] for text in texts]
