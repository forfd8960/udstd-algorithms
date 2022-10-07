
## Hash Ooperations - put, get

```
In [1]: from hash import Hash

In [2]: h = Hash(0.75, 10)

In [3]: h.put("abc", 1)
Out[3]: True

In [4]: h.put("def", 2)
Out[4]: True

In [5]: v = h.get("abc")

In [6]: v
Out[6]: (<hash.KV at 0x103fac520>, True)

In [7]: v.value
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Input In [7], in <cell line: 1>()
----> 1 v.value

AttributeError: 'tuple' object has no attribute 'value'

In [8]: v[0]
Out[8]: <hash.KV at 0x103fac520>

In [9]: v[1]
Out[9]: True

In [10]: v[0].key
Out[10]: 'abc'

In [11]: v[0].value
Out[11]: 1

In [12]: h.put("abc", 10)
Out[12]: True

In [13]: kv, exist = h.get("abc")

In [14]: exist
Out[14]: True

In [15]: key, value = kv
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [15], in <cell line: 1>()
----> 1 key, value = kv

TypeError: cannot unpack non-iterable KV object

In [16]: key, value = kv.key, kv.value

In [17]: key, value
Out[17]: ('abc', 10)
```

## Hash Ooperations - remove

```
In [1]: from hash import Hash

In [2]: h = Hash(0.75, 10)

In [3]: h.put("abc", 1)
Out[3]: True

In [4]: h.put("def", 2)
Out[4]: True

In [5]: h.put("xyz", 10)
Out[5]: True

In [6]: v, ok = h.get("xyz")

In [7]: v, ok
Out[7]: (<hash.KV at 0x1052bcaf0>, True)

In [8]: v.key, v.value
Out[8]: ('xyz', 10)

In [9]: h.remove("def")
Out[9]: True

In [10]: v1, ok = h.get("def")

In [11]: ok
Out[11]: False

In [12]: v1

In [13]: v1 is None
Out[13]: True
```
