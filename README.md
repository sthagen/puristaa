# puristaa

Puristaa (Finnish for compress)

[License: MIT](https://git.sr.ht/~sthagen/puristaa/tree/default/item/LICENSE)

Provide a memory neutral and fast implementation that is clear to understand and works for the use case of extracting a common prefix of a sequence of strings and yielding that prefix and a generator for the compressed strings of the original sequence.

The latter is not yet clear. One simple implementation path is to receive a reference to a sequence, determine min-max, compare min to max by character and break with first index of enumaeration not matching. Finally yield first the prefix, subsequently all strings of the sequence each shortened by the prefix.

Another still open question is, if a composition of functions can be construed, such that the prefix finding algorithm respects a caller provided policy representing the inner structure of the strings.
 An example for an inner structure is a sequence of paths as strings. A path policy would provide a separator that modifies the prefix finding algorithm to backtrack to the previous such separator token.

why? well, imagine the sequence `'bar/baz', 'bar/bazaar'` and a path policy providing the boolean predicate `lambda x: x == '/'` should not yield `'bar/baz', '', 'aar'` but instead `'bar/', 'baz', 'bazaar'`.

[![version](https://img.shields.io/pypi/v/puristaa.svg?style=flat)](https://pypi.python.org/pypi/puristaa/)
[![downloads](https://img.shields.io/pypi/dm/puristaa.svg?style=flat)](https://pypi.python.org/pypi/puristaa/)
[![wheel](https://img.shields.io/pypi/wheel/puristaa.svg?style=flat)](https://pypi.python.org/pypi/puristaa/)
[![supported-versions](https://img.shields.io/pypi/pyversions/puristaa.svg?style=flat)](https://pypi.python.org/pypi/puristaa/)
[![supported-implementations](https://img.shields.io/pypi/implementation/puristaa.svg?style=flat)](https://pypi.python.org/pypi/puristaa/)

## Documentation

User and developer [documentation of puristaa](https://codes.dilettant.life/docs/puristaa).

## Bug Tracker

Feature requests and bug reports are bested entered in the [todos of puristaa](https://todo.sr.ht/~sthagen/puristaa).

## Primary Source repository

The primary source repository of [puristaa is at sourcehut](https://git.sr.ht/~sthagen/puristaa)
a collection of tools useful for software development.
## Status

Experimental

**Note**: The default branch is `default`.

# Use

## Commandline API
