class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"Driving {self.model}")


ford = Car("Ford Focus RS")
nissan = Car("Nissan GT-R")
toyota = Car("Toyota GR86")

print(ford.model)  # Ford Focus RS
print(ford.drive())


cars = {"ford": {"model": "Ford Focus RS"}}
print(cars["ford"]["model"])  # Ford Focus RS
