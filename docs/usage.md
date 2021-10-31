# Example Usage

Unshared prefix:
```
$ puristaa a/a b/c
Prefix compression yields '' + ['a/a', 'b/c']
```

Shared prefix:
```
$ puristaa a/a a/b
Prefix compression yields 'a/' + ['a', 'b']
```
