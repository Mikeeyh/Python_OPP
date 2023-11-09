"""We can use other class methods and attributes in order to do not repeat the code"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    pass


s = Student('Maraya', 'Kaneva')
p = Person('Mike', 'Biserov')

print(p.first_name)
print(p.last_name)
print(p.get_info())

print(s.first_name)
print(s.last_name)
print(s.get_info())

""" Using super class to add more methods in the other class """


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        if len(first_name) < 2:
            raise ValueError("Name must be at least 2 characters")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person): 
    def __init__(self, first_name, last_name, fac_number):
        super().__init__(first_name, last_name)  # We are using super() if there is only one inheritance
        # Person.__init__(self, first_name, last_name)  # We are using this if there are more than one inheritance
        self.fac_number = fac_number


s = Student('Maraya', 'Kaneva', '123456')
p = Person('Mike', 'Biserov')

print(p.first_name)
print(p.last_name)
print(p.get_full_name())

print(s.first_name)
print(s.last_name)
print(s.get_full_name())
