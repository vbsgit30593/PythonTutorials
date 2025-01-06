## Python dataclass options
* collections.namedtuple
* typing.NamedTuple
* @dataclasses.dataclass

### Key differences
#### first two create immutable instances

```python
d = {
    Coordinate(10, 20): 1000,
    Coordinate(10.1, 20): 2000,
}
print(d)
```

```
{Coordinate(lat=10, lon=20): 1000, Coordinate(lat=10.1, lon=20): 2000}
```

* By default, dataclasses are mutable
  * We can use `frozen=True` in the decorator to make them immutable and hence hashable.
  * dataclass emulates immutability by implementing a `__setattr__` and `__delattr__` and returns a `class.FrozenInstanceError` when a user attempts to set or delete an attr.
  * to make it unhashable, `(frozen=False)` the dataclass sets `__hash__` to False


#### class syntax
* `typing.NamedTuple` and `dataclass` support regular class statement syntax

### Quirks
* Can't have mutable defaults

```python
@dataclass
class Test:
    var1: int = 10
    varlist: list = []

Traceback (most recent call last):
  File "dataclassesQuirks.py", line 4, in <module>
    class Test:
  File "/Users/vaibhavsingh/opt/anaconda3/lib/python3.8/dataclasses.py", line 1019, in dataclass
    return wrap(cls)
  File "/Users/vaibhavsingh/opt/anaconda3/lib/python3.8/dataclasses.py", line 1011, in wrap
    return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
  File "/Users/vaibhavsingh/opt/anaconda3/lib/python3.8/dataclasses.py", line 861, in _process_class
    cls_fields = [_get_field(cls, name, type)
  File "/Users/vaibhavsingh/opt/anaconda3/lib/python3.8/dataclasses.py", line 861, in <listcomp>
    cls_fields = [_get_field(cls, name, type)
  File "/Users/vaibhavsingh/opt/anaconda3/lib/python3.8/dataclasses.py", line 745, in _get_field
    raise ValueError(f'mutable default {type(f.default)} for field '
ValueError: mutable default <class 'list'> for field varlist is not allowed: use default_factory
```

* Solution

```python
@dataclass
class Test:
    var1: int = 10
    varlist: list[str] = dataclasses.field(default_factory=list)
```

`default_factory` can be a function, class or any other Callable which doesn't take any args
* Every instance gets its own list. No sharing!!
`Note that this error pops up only for dict, set and list defaults. So, remember to use factory`

### ClassVar and InitVar
```python
@dataclass
class Test:
    var1: int = 10
    varlist1: ClassVar[set[str]] = set()
    varlist2: list[str] = dataclasses.field(default_factory=list)
```

Here, `varlist1: set = set()` wouldn't work as that makes it an instance variable and they aren't allowed to have mutable defaults.

Similarly, `varlist2: list = []` is not allowed (`varlist2 = []` is fine since that's again a class var).