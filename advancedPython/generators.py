import sys
def infinite():
    result = 1
    while True:
        yield result
        result *= 5

value = infinite()
for _ in range(10):
    print (next(value))