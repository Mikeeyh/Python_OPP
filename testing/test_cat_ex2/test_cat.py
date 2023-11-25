from unittest import TestCase, main
from testing.test_cat_ex2.cat import Cat


class CatTests(TestCase):

    def setUp(self):  # set values again before each test
        self.cat = Cat("Caty")

    def test_correct_initialization(self):
        self.assertEqual("Caty", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_cat_expect_fed_and_sleepy_cat_with_increased_size(self):
        expected_size = 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_eat_when_cat_is_fed_raises_exception(self):
        self.cat.fed = True  # arrange

        with self.assertRaises(Exception) as ex:
            self.cat.eat()  # act

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleeping_cat_when_is_fed_makes_cat_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_sleep_when_cat_is_not_fed_raises_exception(self):
        self.cat.fed = False  # arrange

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()  # act

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
