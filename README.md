# Trie Tree implemented with Python 2.7

```python:test.py
from Trie import *
trie = Trie('users')
with open(trie.make('shogonir', 'repositories.txt'), 'w') as f :
    f.write('\n'.join(['sorts', 'FiveProblems', 'camerobo', 'vimrc']) + '\n\n')
```

If execute this code, "repositories.txt" created at "./users/s/h/o/g/o/n/i/r/".

```
sorts
FiveProblems
camerobo
vimrc
```
