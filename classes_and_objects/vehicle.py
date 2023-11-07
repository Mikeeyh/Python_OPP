class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(max_speed=100, mileage=20)
print("Max speed:", car.max_speed)
print("Mileage:", car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)

# or
class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(20, 100)
print("Max speed:", car.max_speed)
print("Mileage:", car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)

