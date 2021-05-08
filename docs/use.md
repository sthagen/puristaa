# Example Usage

Unshared prefix:
```
$ prefix-compression a/a b/c
Prefix compression yields '' + ['a/a', 'b/c']
```

Shared prefix:
```
$ prefix-compression a/a a/b
Prefix compression yields 'a/' + ['a', 'b']
```
