"""
What's resolved -
Using the Simple Factory, we have actual honored the Single Responsibility
Principle as the SimpleBurgerFactory has the single job of creating burgers

What's not - 
If we look closely into the SimpleBurgerFactory, we are violating the Open
Closed Principle as we need to keep modifying this class
"""

from abc import ABC, abstractmethod
import random

class SimpleBurgerFactory:
    def create_burger(self, btype: str):
        bid = random.randint(1000, 2000)
        match btype:
            case "veg":
                return VegBurger(id=bid)

            case "beef":
                return BeefBurger(id=bid)

            case _:
                raise Exception("Invalid burger type requested")


class Burger(ABC):
    def __init__(self, id: int, addons: list[str] = None):
        self._id = id
        self._addons = addons

    @abstractmethod
    def prepare():
        pass


class VegBurger(Burger):
    def __init__(self, id: int, addons: list[str] = None, specialveg: str = ""):
        super().__init__(id=id, addons=addons)
        self._specialveg = specialveg

    def prepare(self):
        print(f"Preparing veggie burger {self._id}")


class BeefBurger(Burger):
    def __init__(self, id: int, addons: list[str] = None, specialbeef: str = ""):
        super().__init__(id=id, addons=addons)
        self._specialbeef = specialbeef

    def prepare(self):
        print(f"Preparing beef burger {self._id}")

class Restaurent:
    def order_burger(self, btype) -> Burger:
        bf = SimpleBurgerFactory()
        burger = bf.create_burger(btype)
        burger.prepare()

        return burger

if __name__ == "__main__":
    res = Restaurent()
    res.order_burger(btype="veg")
    res.order_burger(btype="beef")
    res.order_burger(btype="chicken")
