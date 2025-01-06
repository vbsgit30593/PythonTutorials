from dataclasses import InitVar, dataclass
import dataclasses
from typing import ClassVar, InitVar

@dataclass
class Test:
    var1: int = 10
    varlist1: ClassVar[set[str]] = set()
    varlist2: list[str] = dataclasses.field(default_factory=list)
    database: InitVar[str] = None

    def __post_init__(self, database):
        pass

obj = Test()
print(obj)

