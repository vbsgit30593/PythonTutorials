"""
We can specify type hints here.
"""


from tkinter import FLAT
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


print("\n\n# Alternative readable approach #")


class CoordinateAlter(NamedTuple):
    lat: float
    lon: float

delhi = CoordinateAlter(10.1, 20.2)
current = CoordinateAlter(10.1, 20.2)

print(delhi)
print(current)

print(f"Delhi == current ? {delhi == current}")

print(f"{issubclass(CoordinateAlter, NamedTuple) = }")
print(f"{issubclass(CoordinateAlter, tuple) = }")
print(f"{get_type_hints(CoordinateAlter)}")

d = {
    Coordinate(10, 20): 1000,
    Coordinate(10.1, 20): 2000,
}
print(d)