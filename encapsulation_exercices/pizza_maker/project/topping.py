class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

        if self.topping_type == "":
            raise ValueError("The topping type cannot be an empty string")

        if self.weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
