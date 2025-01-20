class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.veggies = None
    
    def __str__(self):
        return (
            f"Pizza(size = {self.size}, cheese = {self.cheese}, veggies = {self.veggies})"
        )

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_veggies(self):
        self.pizza.veggies = True
        return self

    def build(self):
        return self.pizza

builder = PizzaBuilder()
pizza = (builder.set_size("Large")
        .add_cheese()
        .add_veggies()
        .build())

print(pizza)
