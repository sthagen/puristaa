# python-prefix_compression
Why not explicitly be weak on naming?

Started using linter, style enforcer, type checker, and coverage in tests.

# what does it accomplish or support?

Provide a memory neutral and fast implementation that is clear to understand and works for the use case of extracting a common prefix of a sequence of strings and yielding that prefix and a generator for the compressed strings of the original sequence.

The latter is not yet clear. One simple implementation path is to receive a reference to a sequence, determine min-max, compare min to max by character and break with first index of enumaeration not matching. Finally yield first the prefix, subsequently all strings of the sequence each shortened by the prefix.

Another still open question is, if a composition of functions can be construed, such that the prefix finding algorithm respects a caller provided policy representing the inner structure of the strings.
 An example for an inner structure is a sequence of paths as strings. A path policy would provide a separator that modifies the prefix finding algorithm to backtrack to the previous such separator token.

why? well, imagine the sequence `'bar/baz', 'bar/bazaar'` and a path policy providing the boolean predicate `lambda x: x == '/'` should not yield `'bar/baz', '', 'aar'` but instead `'bar/', 'baz', 'bazaar'`.

Note: the name of the default branch (with special meaning for github and gitlab users) is `default` :wink:.
