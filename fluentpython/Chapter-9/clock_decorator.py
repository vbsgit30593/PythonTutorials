"""
write a decorator to time execution of a function
"""
import time
def clock(func):
    def clocked(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        name = func.__name__
        delta = end - start 
        arglist = ", ".join(repr(arg) for arg in args)
        print(f"{delta:.8f}: {name}({arglist}) -> {result}")
        return result
    return clocked
