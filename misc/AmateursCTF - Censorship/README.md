We can't execute code that includes word `flag` or `t`, `e`, `\` char, so printing is out of play. However, all the exceptions that occur are printed so we can use it as stdout here. Notice that flag is stored in `_` var because of `for _ in [flag]:`. The easiest way to make the program to stdout the flag:
```bash
Give code: {}[_]
'flag{this_is_a_fake_flag}'
```
Code attempts to get value of key `_` from empty dict which results in `KeyError` exception that gets us the flag as the key is included in the exception message.

I think it's not the solution that was meant by the author, tricky one 😉

- `main.py` - basic challenge
- `main2.py` -  harder version with different set of forbidden chars, this solution works the same