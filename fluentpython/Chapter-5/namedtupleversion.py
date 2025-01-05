from collections import namedtuple
from unicodedata import name

Coordinate = namedtuple("Coordinate", "lat lon")

delhi = Coordinate(10.1, 20.2)
current = Coordinate(10.1, 20.2)

print(delhi)
print(current)

print(f"Delhi == current ? {delhi == current}")


"""
Note that we are unable to provide typehints here.
"""