from time import perf_counter
from typing import Callable
from functools import wraps

def clock(func: Callable) ->Callable:
    """Function to track exec time"""
    # @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper for clock"""
        start = perf_counter()
        result = func(*args, *kwargs)
        end = perf_counter()
        name = func.__name__
        arglist = ', '.join(str(arg) for arg in args)
        delta = end - start
        print(f"{delta}: {name}({arglist}) -> {result!r}")
        return result

    return wrapper

@clock
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

print(add.__name__)
print(add.__doc__)

add(10, 20)