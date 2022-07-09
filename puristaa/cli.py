#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract common prefix from sequence of strings and yield sequence of rest strings.

Implementation uses min-max left matching, single character backtracking policy and a list.
"""
import os
import sys
import typing

from puristaa.puristaa import prefix_compression


@typing.no_type_check
def main(argv=None):
    """Test driver for the prefix compression taking the texts from argv and the policy from PC_TOKEN env variable."""
    texts = sys.argv[1:] if argv is None else argv
    if not isinstance(texts, (tuple, list)):
        texts = texts.split()
    token = os.getenv('PC_TOKEN', '')
    prefix, endings = prefix_compression(texts, lambda x: x == token if token else None)
    compressed = f"'{prefix}' + {endings}"
    print(f"Prefix compression{f' with inner structure separator {token}' if token else ''} yields {compressed}")
