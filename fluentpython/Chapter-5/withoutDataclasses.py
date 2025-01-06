"""
Write a class for Coordinates.
"""


class Coordinate:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def __str__(self) -> str:
        return f"Coordinate({self.lat}, {self.lon})"

    def __eq__(self, obj) -> bool:
        return self.lat == obj.lat and self.lon == obj.lon

    def __getitem__(self, idx):
        return self.lat if idx == 0 else self.lon

delhi = Coordinate(10.1, 20.2)
current = Coordinate(10.1, 20.2)

print(delhi)
print(current)

print(f"Delhi == current ? {delhi == current}")


print(f"{delhi[0] = }")