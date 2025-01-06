"""
Note that we are unable to provide typehints here.
"""
from collections import namedtuple
import json


Coordinate = namedtuple("Coordinate", "lat lon")

delhi = Coordinate(10.1, 20.2)
current = Coordinate(10.1, 20.2)

print(delhi)
print(current)

print(f"Delhi == current ? {delhi == current}")

d = {
    Coordinate(10, 20): 1000,
    Coordinate(10.1, 20): 2000,
}
print(d)

print(f"{delhi[0] = }, {current[1] = }")
current = Coordinate(10.1, 20.1)
print(f"{(delhi > current) = }")

asdict = delhi._asdict()
print(json.dumps(asdict)) # good for serialization
