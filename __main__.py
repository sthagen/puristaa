#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Extract common prefix from sequence of strings and yield sequence of rest strings.

Implementation uses min-max left matching, single character backtracking policy and a list.
"""
import os
import sys


def prefix_compression(texts, policy=None):
    """Return common prefix string abiding policy and compressed texts string list."""
    if not texts:  # Early out return empty prefix and empty sequence
        return "", texts
    prefix_guard, first, last = 0, min(texts), max(texts)
    for pos, char in enumerate(first):
        if char != last[pos]:
            prefix_guard = pos
            if not policy:
                break
            for here in range(prefix_guard, -1, -1):
                if policy(first[here]):
                    prefix_guard = here + 1
                    break
    if not prefix_guard:  # Reduce memory pressure for all different texts
        return "", texts
    return first[:prefix_guard], [text[prefix_guard:] for text in texts]


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Test driver for the prefix compression taking the texts from argv and the policy from PC_TOKEN env variable."""
    texts = sys.argv[1:] if argv is None else argv
    token = os.getenv("PC_TOKEN", "")
    prefix, endings = prefix_compression(texts, lambda x: x == token if token else None)
    compressed = f"{prefix}{endings}"
    print(
        f"Prefix compression{f' with inner structure separator {token}' if token else ''} yields {compressed}"
    )


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
