from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return f"teaching..."
