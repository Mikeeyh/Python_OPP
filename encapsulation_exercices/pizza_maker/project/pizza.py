from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}
        self.dough = dough

        if self.name == "":
            raise ValueError("The name cannot be an empty string")

        if self.max_number_of_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

        if self.dough is None:
            raise ValueError("You should add dough to the pizza")

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        for t in self.toppings.keys():
            if t == topping:
                self.toppings[t] += t.weight
        self.toppings[topping] = topping.weight

    def calculate_total_weight(self):
        total_weight = self.dough.weight + sum(self.toppings.values())
        return total_weight
