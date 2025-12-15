"""
Function overloading within a class.
"""

from functools import singledispatchmethod
from typing import Any


class TestClass:
    @singledispatchmethod
    def func(self, arg: Any):
        raise NotImplementedError(f"Type {type(arg)} not registered!")

    @func.register(str)
    def _(self, arg):
        print("type is str")

    @func.register(int)
    def _(self, arg):
        print("type is int")

    @func.register(list)
    def _(self, arg):
        print("type is list")


obj = TestClass()
obj.func(10)
obj.func("hello")
obj.func([1, 2, 4])
obj.func(10.0)
