from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = "WG8"

    def __str__(self) -> str:
        return f"({self.lat}, {self.lon})"


class DemoNT(NamedTuple):
    var1: int
    var2: int = 10
    var3 = 20

obj = Coordinate(10, 20)
print (obj)