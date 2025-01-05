"""Shows a hack of how to use class methods with namedtuple."""
from collections import namedtuple

Coordinates = namedtuple("Coordinates", "lat lon", defaults=[0.0, 0.0])

class MakeCoordinates(Coordinates):
    def doSomething(self):
        print ("In do something")
    
    def __str__(self) -> str:
        return f"({self.lat}, {self.lon})"

obj = MakeCoordinates(10, 20)
print (obj)
