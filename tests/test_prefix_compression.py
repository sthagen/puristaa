# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import prefix_compression.prefix_compression as pc


def test_prefix_compression_ok_string():
    assert pc.prefix_compression(["aa"]) == ("aa", [""])


def test_prefix_compression_ok_strings():
    assert pc.prefix_compression(["aa", "ab"]) == ("a", ["a", "b"])


def test_prefix_compression_ok_disjoint_strings():
    assert pc.prefix_compression(["a", "b"]) == ("", ["a", "b"])


def test_prefix_compression_ok_empty():
    assert pc.prefix_compression([]) == ("", [])


def test_prefix_compression_nok_ints():
    with pytest.raises(TypeError):
        pc.prefix_compression([1, 2, 3])


def test_prefix_compression_nok_floats():
    with pytest.raises(TypeError):
        pc.prefix_compression([0.123, 3.1415])


def test_documentation_example():
    sequence = ["bar/baz", "bar/bazaar"]
    expect = ("bar/", ["baz", "bazaar"])
    assert pc.prefix_compression(sequence, policy=lambda x: x == "/") == expect


def test_documentation_no_policy_example():
    sequence = ["bar/baz", "bar/bazaar"]
    expect = ("bar/baz", ["", "aar"])
    assert pc.prefix_compression(sequence, policy=None) == expect
