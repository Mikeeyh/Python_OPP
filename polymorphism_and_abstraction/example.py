class Shape:
    @staticmethod
    def calculate_area():
        return None


class Square(Shape):
    side_length = 2

    def calculate_square_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_triangle_area(self):
        return 0.5 * self.base_length + self.height


class Circle(Shape):  # adding Circle
    def calculate_circle_area(self):
        pass


t = Triangle()
t2 = Triangle()
s = Square()
s2 = Square()

shapes = [t, t2, s, s2]

"""

We should check what type of shape is before calculating the area. 
So we use isinstance method. But if we add other shape (class Circle for example), 
we should add a check for this class in our if-else too.

We can use polymorphism in order to write better code.

"""

for shape in shapes:
    if isinstance(shape, Triangle):
        print(shape.calculate_triangle_area())
    elif isinstance(shape, Square):
        print(shape.calculate_square_area())
    # adding:
    elif isinstance(shape, Circle):
        print(shape.calculate_circle_area())

"""

We will use the same method's name on every shape.
calculate_square_area -> calculate_area, etc.

"""


class Shape:
    @staticmethod
    def calculate_area():
        return None


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length + self.height


class Circle(Shape):  # adding Circle
    def calculate_area(self):
        pass


t = Triangle()
t2 = Triangle()
s = Square()
s2 = Square()

shapes = [t, t2, s, s2]

for shape in shapes:
    print(shape.calculate_area())
