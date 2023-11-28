from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Mike", "Dog", "sound")

    def test_correct_initialization(self):
        self.assertEqual("Mike", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("wouf!", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_returns_correct_string(self):
        result = self.mammal.make_sound()
        expected_data = "Mike makes sound"
        self.assertEqual(expected_data, result)

    def test_get_kingdom_expect_correct_kingdom_type(self):
        result = self.mammal.get_kingdom()
        expected_data = "animals"
        self.assertEqual(expected_data, result)

    def test_info_method_expect_correct_string(self):
        result = self.mammal.info()
        expected_data = "Mike is of type Dog"
        self.assertEqual(expected_data, result)


if __name__ == '__main__':
    main()
