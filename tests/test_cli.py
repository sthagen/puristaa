# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import prefix_compression.cli as cli


def test_main_ok_string():
    cli.main("imension is implicit")


def test_main_ok_same_chars_in_string():
    cli.main("a a a a")


def test_main_nok_ints():
    with pytest.raises(TypeError):
        cli.main([1, 2, 3])


def test_main_nok_int():
    with pytest.raises(AttributeError):
        cli.main(42)
