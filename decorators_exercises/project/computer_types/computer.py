from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str, processor=None, ram=None, price=0):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.price = price
        self.type = ""

        if not self.manufacturer or not self.manufacturer.strip() or not self.model or not self.model.strip():
            raise ValueError("Manufacturer name cannot be empty")

    def configure_computer(self, processor: str, ram: int):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"


# c = Computer("Asus", "Notebook 14", "Ryzen 5", 16, 1750)
# print(c.manufacturer)
# print(c.model)
# print(c.processor)
# print(c.ram)
# print(c.price)
# print(c.__repr__())
