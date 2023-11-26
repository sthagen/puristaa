# Puristaa

Puristaa (Finnish for compress)

Provide a memory neutral and fast implementation that is clear to understand and works for the use case of extracting a common prefix of a sequence of strings and yielding that prefix and a generator for the compressed strings of the original sequence.

The latter is not yet clear. One simple implementation path is to receive a reference to a sequence, determine min-max, compare min to max by character and break with first index of enumaeration not matching. Finally yield first the prefix, subsequently all strings of the sequence each shortened by the prefix.

Another still open question is, if a composition of functions can be construed, such that the prefix finding algorithm respects a caller provided policy representing the inner structure of the strings.
 An example for an inner structure is a sequence of paths as strings. A path policy would provide a separator that modifies the prefix finding algorithm to backtrack to the previous such separator token.

why? well, imagine the sequence `'bar/baz', 'bar/bazaar'` and a path policy providing the boolean predicate `lambda x: x == '/'` should not yield `'bar/baz', '', 'aar'` but instead `'bar/', 'baz', 'bazaar'`.

[![License](https://git.sr.ht/~sthagen/puristaa/blob/default/docs/badges/license-spdx-mit.svg)](https://git.sr.ht/~sthagen/puristaa/tree/default/item/LICENSE)
[![Country of Origin](https://git.sr.ht/~sthagen/puristaa/blob/default/docs/badges/country-of-origin-name-switzerland-neutral.svg)](https://git.sr.ht/~sthagen/puristaa/tree/default/item/COUNTRY-OF-ORIGIN)
[![Export Classification Control Number (ECCN)](https://git.sr.ht/~sthagen/puristaa/blob/default/docs/badges/export-control-classification-number_eccn-ear99-neutral.svg)](https://git.sr.ht/~sthagen/puristaa/tree/default/item/EXPORT-CONTROL-CLASSIFICATION-NUMBER)
[![Configuration](https://git.sr.ht/~sthagen/puristaa/blob/default/docs/badges/configuration-sbom.svg)](https://git.sr.ht/~sthagen/puristaa/tree/default/item/docs/third-party/README.md)

[![Version](https://git.sr.ht/~sthagen/puristaa/blob/default/docs/badges/latest-release.svg)](https://pypi.python.org/pypi/puristaa/)
[![Downloads](https://git.sr.ht/~sthagen/puristaa/blob/default/docs/badges/downloads-per-month.svg)](https://pepy.tech/project/puristaa)
[![Python](https://git.sr.ht/~sthagen/puristaa/blob/default/docs/badges/python-versions.svg)](https://pypi.python.org/pypi/puristaa/)
[![Maintenance Status](https://git.sr.ht/~sthagen/puristaa/blob/default/docs/badges/commits-per-year.svg)](https://git.sr.ht/~sthagen/puristaa/log)

## Documentation

User and developer [documentation of puristaa](https://codes.dilettant.life/docs/puristaa).

## Bug Tracker

Any feature requests or bug reports shall go to the [todos of puristaa](https://todo.sr.ht/~sthagen/puristaa).

## Primary Source repository

The main source of `puristaa` is on a mountain in central Switzerland.
We use distributed version control (git).
There is no central hub.
Every clone can become a new source for the benefit of all.
The preferred public clones of `puristaa` are:

* [on codeberg](https://codeberg.org/sthagen/puristaa) - a democratic community-driven, non-profit software development platform operated by Codeberg e.V.
* [at sourcehut](https://git.sr.ht/~sthagen/puristaa) - a collection of tools useful for software development.

## Contributions

Please do not submit "pull requests" (I found no way to disable that "feature" on GitHub).
If you like to share small changes under the repositories license please kindly do so by sending a patchset.
You can either send such a patchset per email using [git send-email](https://git-send-email.io) or 
if you are a sourcehut user by selecting "Prepare a patchset" on the summary page of your fork at [sourcehut](https://git.sr.ht/).

## Support

Please kindly submit issues at https://todo.sr.ht/~sthagen/puristaa or write plain text email to ~sthagen/puristaa@lists.sr.ht to submit patches and request support. Thanks.

## Status

Experimental

**Note**: The default branch is `default`.
