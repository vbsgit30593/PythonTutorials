import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print ("__add__ called")
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __bool__(self):
        return bool(abs(self))

    # def __iadd__(self, other):
    #     print ("__iadd__ called")
    #     return Vector(self.x + other.x, self.y + other.y)


point1 = Vector(1, 2)
point2 = Vector(3, 5)

print (point1 + point2)
print (point1 * 10)
print (point1)
print (abs(point1))
point1 += point2
print (point1)