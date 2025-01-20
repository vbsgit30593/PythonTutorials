from curses import meta
from tokenize import Single
import enum
from abc import ABC, abstractmethod


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()

print(obj1 == obj2)
