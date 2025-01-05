from typing import NamedTuple, ClassVar
from dataclasses import InitVar, dataclass, field

class Coordinate(NamedTuple):
    lat : float
    lon : float

    def __str__(self) -> str:
        return f"({self.lat}, {self.lon})"

@dataclass(frozen=True)
class Coordinates:
    lat : float
    lon : float
    check : set[int] = field(default_factory=set)

    def __str__(self) -> str:
        return f"({self.lat}, {self.lon})"

@dataclass
class DemoDataClass:
    var1: int
    var2: int = 10
    var3 = 40
    check2: set[str] = field(default_factory=set)
    classvar: ClassVar[set[str]] = set()
    initvar: InitVar[set] = set({10, 20})
    # check1 : set[str] = set()
    # check2: frozenset[str] = frozenset({"asdsa", "asdas"})

    def __post_init__(self, initvar):
        print (initvar)
