"""
This pattern is useful in case of state transitions.
The context changes from one state to another on an action
"""

from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def insert_coin(self, context):
        pass

    @abstractmethod
    def select_item(self, context):
        pass

    @abstractmethod
    def dispense(self, context):
        pass


# Concrete States


class NoCoinState(State):
    def insert_coin(self, context):
        print("Coin Inserted!")
        context.set_state(CoinInsertedState())

    def select_item(self, context):
        print("Please insert a coin first!")

    def dispense(self, context):
        print("Please insert a coin and select a product first!")

class CoinInsertedState(State):
    def insert_coin(self, context):
        print("Coin has already been inserted!")

    def select_item(self, context):
        print("Product selected!")
        context.set_state(DispensingState())

    def dispense(self, context):
        print("Please select a product first.")


class DispensingState(State):
    def insert_coin(self, context):
        print("Coin has already been inserted!")

    def select_item(self, context):
        print("Product has already been selected!")

    def dispense(self, context):
        print("Dispensing product")
        context.set_state(NoCoinState())


class VendingMachine:
    def __init__(self):
        self.state = NoCoinState()

    def set_state(self, state: State):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin(context=self)

    def select_item(self):
        self.state.select_item(context=self)

    def dispense(self):
        self.state.dispense(context=self)


if __name__ == "__main__":
    machine = VendingMachine()

    machine.insert_coin()
    machine.select_item()
    machine.dispense()
    machine.dispense()
    machine.insert_coin()




