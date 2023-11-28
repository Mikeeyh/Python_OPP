from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    name = "Mike"
    courses = {}

    def setUp(self):
        self.student = Student(self.name, self.courses)

    def test_correct_initialization(self):
        self.assertEqual(self.name, self.student.name)
        self.assertEqual(self.courses, self.student.courses)

    def test_attributes_types(self):
        self.assertIsInstance(self.student.name, str)
        self.assertIsInstance(self.courses, dict)


# class Student:
#     def __init__(self, name: str, courses=None):
#         if courses is None:
#             courses = {}
#         self.name = name
#         self.courses = courses  # {course_name: [notes]}
#
#     def enroll(self, course_name: str, notes, add_course_notes: str = ""):
#         if course_name in self.courses.keys():
#             [self.courses[course_name].append(x) for x in notes]
#             return "Course already added. Notes have been updated."
#
#         if add_course_notes == "Y" or add_course_notes == "":
#             self.courses[course_name] = notes
#             return "Course and course notes have been added."
#
#         self.courses[course_name] = []
#         return "Course has been added."
#
#     def add_notes(self, course_name, notes):
#         if course_name in self.courses.keys():
#             self.courses[course_name].append(notes)
#             return "Notes have been updated"
#         raise Exception("Cannot add notes. Course not found.")
#
#     def leave_course(self, course_name):
#         if course_name in self.courses.keys():
#             self.courses.pop(course_name)
#             return "Course has been removed"
#         raise Exception("Cannot remove course. Course not found.")
