#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract common prefix from sequence of strings and yield sequence of rest strings.

Implementation uses min-max left matching and a generator.
"""
import sys


def prefix_compression(paths):
    """Return common prefix string and relative paths string sequence."""
    if not paths:  # Early out return empty prefix and empty sequence
        return "", paths
    prefix_guard, first, last = 0, min(paths), max(paths)
    for pos, char in enumerate(first):
        if char != last[pos]:
            prefix_guard = pos
            break
    if not prefix_guard:  # Reduce memory pressure for all different paths
        return "", paths
    return first[:prefix_guard], [a_path[prefix_guard:] for a_path in paths]


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process the files separately per folder."""
    argv = sys.argv[1:] if argv is None else argv

    prefix, rel_paths = prefix_compression(argv)
    if len(rel_paths) > 5:
        folders_disp = f"{prefix}[{', '.join(rel_paths[:3])}, ... {rel_paths[-1]}]"
    else:
        folders_disp = f"{prefix}{rel_paths}"
    print(f"Prefix compression yields {folders_disp}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
