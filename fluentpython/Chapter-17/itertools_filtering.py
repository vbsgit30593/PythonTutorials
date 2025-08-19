import itertools
from random import choice

print("# filter")
def vowel(x):
    return x.lower() in 'aeiou'

st = 'Aardvark'
print(f"{st=}")
res = filter(vowel, st) 
print(list(res))

print("# filterfalse")
res = itertools.filterfalse(vowel, st)
print(list(res))

print("# compress")
comp = (vowel(x) for x in st)
res = itertools.compress(st, comp)
print(list(res))

print("# dropwhile")
res = itertools.dropwhile(vowel, st)
print(list(res))

print("# takewhile")
res = itertools.takewhile(vowel, st)
print(list(res))

print("# islice 1")
res = itertools.islice(st, 3)
print(list(res))

print("# islice 2")
res = itertools.islice(st, 3, 5)
print(list(res))

print("# islice 3")
res = itertools.islice(st, 1, 6, 2)
print(list(res))

"""
# filter
st='Aardvark'
['A', 'a', 'a']
# filterfalse
['r', 'd', 'v', 'r', 'k']
# compress
['A', 'a', 'a']
# dropwhile
['r', 'd', 'v', 'a', 'r', 'k']
# takewhile
['A', 'a']
# islice 1
['A', 'a', 'r']
# islice 2
['d', 'v']
# islice 3
['a', 'd', 'a']
"""