class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return self.radius * self.radius * self.pi  # we can use self.pi or Circle.pi

    def get_circumference(self):
        return self.radius * 2 * self.pi


circle = Circle(15)
circle.set_radius(11)
print(circle.get_area())
print(circle.get_circumference())
