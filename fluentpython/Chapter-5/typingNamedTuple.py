from email.policy import default
from tokenize import Name
from typing import NamedTuple, get_type_hints

# coord = NamedTuple("Coordinate", [("lat", float), ("lon", float)])
Coordinate = NamedTuple("Coordinate", lat=float, lon=float,)

delhi = Coordinate(10.1, 20.2)
current = Coordinate(10.1, 20.2)

print(delhi)
print(current)

print(f"Delhi == current ? {delhi == current}")

print(f"{issubclass(Coordinate, tuple) = }")
print(f"{get_type_hints(Coordinate)}")

"""
We can specify type hints here.
"""