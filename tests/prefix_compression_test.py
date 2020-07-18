import pytest

import prefix_compression.cli as cli
import prefix_compression.prefix_compression as pc


def test_main_nok_ints():
    with pytest.raises(TypeError):
        cli.main([1, 2, 3])


def test_prefix_compression_ok_strings():
    assert pc.prefix_compression(["aa", "ab"]) == ('a', ['a', 'b'])


def test_prefix_compression_nok_ints():
    with pytest.raises(TypeError):
        pc.prefix_compression([1, 2, 3])
