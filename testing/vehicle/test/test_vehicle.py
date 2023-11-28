from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(1.5, 150.5)

    def test_correct_initialization(self):
        self.assertEqual(1.5, self.vehicle.fuel)
        self.assertEqual(150.5, self.vehicle.horse_power)
        self.assertEqual(1.5, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_attributes_types(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))

    def test_drive_kilometers_without_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_successful(self):
        self.vehicle.drive(1)
        expected_fuel_left = 0.25

        self.assertEqual(expected_fuel_left, self.vehicle.fuel)

    def test_refuel_with_more_fuel_than_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(2)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_successful(self):
        self.vehicle.fuel = 0.5
        self.vehicle.refuel(1)
        expected_data = 1.5
        self.assertEqual(expected_data, self.vehicle.fuel)

    def test_str_representation_returns_correct_result(self):
        expected_data = f"The vehicle has 150.5 " \
                        f"horse power with 1.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected_data, self.vehicle.__str__())


if __name__ == '__main__':
    main()
