from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float


delhi = Coordinate(10.1, 20.2)
current = Coordinate(10.1, 20.2)

print(delhi)
print(current)

print(f"Delhi == current ? {delhi == current}")

print(f"{issubclass(Coordinate, tuple) = }")


d = {
    Coordinate(10, 20): True,
}
print(d)
