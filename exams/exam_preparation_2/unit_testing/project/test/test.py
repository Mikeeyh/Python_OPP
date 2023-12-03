from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("bmw", "jeep", 150, 2000.5)

    def test_correct_init(self):
        self.assertEqual("bmw", self.car.model)
        self.assertEqual("jeep", self.car.car_type)
        self.assertEqual(150, self.car.mileage)
        self.assertEqual(2000.5, self.car.price)
        self.assertListEqual([], self.car.repairs)

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 90

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_not_possible(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 100.0
            self.car.set_promotional_price(100.0)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.price = 100.0
            self.car.set_promotional_price(101.0)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_successfully(self):
        self.car.price = 100
        self.assertEqual(100, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', self.car.set_promotional_price(50))
        self.assertEqual(50.0, self.car.price)

    def test_need_repair_impossible(self):
        self.car.price = 100
        self.assertEqual(100, self.car.price)
        self.assertEqual([], self.car.repairs)
        self.assertEqual('Repair is impossible!', self.car.need_repair(51, "description"))
        self.assertEqual([], self.car.repairs)

    def test_need_repair_with_success(self):
        self.car.price = 100
        self.assertEqual('Price has been increased due to repair charges.', self.car.need_repair(49, "description"))
        self.assertEqual(["description"], self.car.repairs)
        self.assertEqual(149, self.car.price)

    def test_need_repair_with_success_exact_price(self):
        self.car.price = 100
        self.assertEqual('Price has been increased due to repair charges.', self.car.need_repair(50, "description"))
        self.assertEqual(["description"], self.car.repairs)
        self.assertEqual(150, self.car.price)

    def test_gt_method_types_mismatch(self):
        car2 = SecondHandCar("mercedes", "not_jeep", 170, 1960.5)
        result = car2 > self.car
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_method_with_success(self):
        car2 = SecondHandCar("bmw", "jeep", 170, 1900)
        result = car2 > self.car
        self.assertFalse(result)

    def test_gt_method_with_success_1(self):
        car2 = SecondHandCar("bmw", "jeep", 170, 2500)
        result = car2 > self.car
        self.assertTrue(result)

    def test_string_representation(self):
        self.assertEqual("""Model bmw | Type jeep | Milage 150km\nCurrent price: 2000.50 | Number of Repairs: 0""", str(self.car))


if __name__ == '__main__':
    main()
