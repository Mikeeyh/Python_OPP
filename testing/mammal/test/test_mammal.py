from unittest import TestCase, main
from testing.mammal.project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Mike", "Dog", "wouf!")

    def test_correct_initialization(self):
        self.assertEqual("Mike", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("wouf!", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_returns_correct_string(self):
        expected_data = "Mike makes wouf!"
        self.assertEqual(expected_data, self.mammal.make_sound())

    def test_get_kingdom_expect_correct_kingdom_type(self):
        expected_data = "animals"
        self.assertEqual(expected_data, self.mammal.get_kingdom())

    def test_info_method_expect_correct_string(self):
        expected_data = "Mike is of type Dog"
        self.assertEqual(expected_data, self.mammal.info())


if __name__ == '__main__':
    main()
