class Vector:
    def __init__(self, x : int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __repr__(self):
        return f"Current object: ({self.x}, {self.y})"

    def __len__(self):
        return 10
    
    def __call__(self):
        print ("Called me?")


v1 = Vector(10, 20)
v2 = Vector(30, 40)
v = v1 + v2

print(f"Add result : ({v.x}, {v.y})")
print(v.y)

v = v1 - v2
print(f"Sub result : ({v.x}, {v.y})")

v = v1 * v2
print(f"Mul result : ({v.x}, {v.y})")

print(v)
print (len(v))
v()