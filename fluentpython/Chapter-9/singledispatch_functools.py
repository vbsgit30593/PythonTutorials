"""
Write a bunch of overloaded functions which can take str, int or list and deal accordingly
"""

from functools import singledispatch
from typing import Any


@singledispatch
def func(arg: Any, verbose: bool = True):
    raise NotImplementedError(f"Type {type(arg)} is not implemented")


@func.register(str)
def _(arg, verbose=None):
    print("This is a string dispatch")


@func.register(int)
def _(arg, verbose=None):
    print("This is an int dispatch")


@func.register(list)
def _(arg, verbose=None):
    print("This is a list dispatch")


func("hello")
func([1, 2, 3])
func(10)
func(10.0)
