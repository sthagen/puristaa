# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import puristaa.puristaa as pc


def test_prefix_compression_ok_string():
    texts = 'imension is implicit'
    assert pc.prefix_compression(texts) == (texts, [''])


def test_prefix_compression_ok_same_chars_in_string():
    texts = 'a a a a'
    assert pc.prefix_compression(texts) == (texts, [''])


def test_prefix_compression_ok_sequence_string():
    assert pc.prefix_compression(['aa']) == ('aa', [''])


def test_prefix_compression_ok_strings():
    assert pc.prefix_compression(['aa', 'ab']) == ('a', ['a', 'b'])


def test_prefix_compression_ok_disjoint_strings():
    texts = ['a', 'b']
    assert pc.prefix_compression(texts) == ('', texts)


def test_prefix_compression_ok_empty():
    texts = []
    assert pc.prefix_compression(texts) == ('', texts)


def test_prefix_compression_nok_ints():
    message = r"'int' object is not iterable"
    with pytest.raises(TypeError, match=message):
        pc.prefix_compression([1, 2, 3])


def test_prefix_compression_nok_floats():
    message = r"'float' object is not iterable"
    with pytest.raises(TypeError, match=message):
        pc.prefix_compression([0.123, 3.1415])


def test_documentation_ok_example():
    sequence = ['bar/baz', 'bar/bazaar']
    expect = ('bar/', ['baz', 'bazaar'])
    assert pc.prefix_compression(sequence, policy=lambda x: x == '/') == expect


def test_documentation_ok_no_policy_example():
    sequence = ['bar/baz', 'bar/bazaar']
    expect = ('bar/baz', ['', 'aar'])
    assert pc.prefix_compression(sequence, policy=None) == expect


def test_documentation_ok_tuple_no_policy_example():
    sequence = ('bar/baz', 'bar/bazaar')
    expect = ('bar/baz', ['', 'aar'])
    assert pc.prefix_compression(sequence, policy=None) == expect


def test_documentation_nok_set_no_policy_example():
    sequence = {'bar/baz', 'bar/bazaar'}
    message = r"'set' object is not subscriptable"
    with pytest.raises(TypeError, match=message):
        pc.prefix_compression(sequence, policy=None)


def test_documentation_ok_dict_no_policy_example():
    mapping = {0: 'bar/baz', 1: 'bar/bazaar'}
    expect = ('', [{0: 'bar/baz', 1: 'bar/bazaar'}])
    assert pc.prefix_compression(mapping, policy=None) == expect


def test_documentation_nok_class_instance_no_policy_example():
    class Foo:
        pass

    an_object = Foo()
    message = r"'Foo' object is not iterable"
    with pytest.raises(TypeError, match=message):
        pc.prefix_compression(an_object, policy=None)
