from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self):
        self.truck = TruckDriver("BigBoss", 1.4)

    def test_correct_init(self):
        self.assertEqual("BigBoss", self.truck.name)
        self.assertEqual(1.4, self.truck.money_per_mile)
        self.assertDictEqual({}, self.truck.available_cargos)
        self.assertEqual(0, self.truck.earned_money)
        self.assertEqual(0, self.truck.miles)

    def test_earned_money_negative_raises_bankrupt(self):
        with self.assertRaises(ValueError) as ve:
            self.truck.earned_money = -1
        self.assertEqual("BigBoss went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_if_location_exists_raises_error(self):
        self.truck.available_cargos = {"Sofia": 120}
        with self.assertRaises(Exception) as ex:
            self.truck.add_cargo_offer("Sofia", 220)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_if_new_location(self):
        self.truck.available_cargos = {"Sofia": 120}
        result = self.truck.add_cargo_offer("Stara Zagora", 220)
        self.assertEqual("Cargo for 220 to Stara Zagora was added as an offer.", result)
        self.assertEqual({'Sofia': 120, 'Stara Zagora': 220}, self.truck.available_cargos)

    def test_drive_best_cargo_offer_no_location_raises_error(self):
        result = self.truck.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_valid(self):
        self.truck.add_cargo_offer("California", 2000)
        self.truck.add_cargo_offer("Los Angeles", 20000)

        result = self.truck.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.truck.name} is driving 20000 to Los Angeles.")
        self.assertEqual(self.truck.earned_money, 4000)
        self.assertEqual(self.truck.miles, 20000)

    def test_check_for_activities(self):
        self.truck.earned_money = 10000
        miles = 1000
        self.truck.check_for_activities(miles)
        self.assertEqual(10000 - 20 * (miles // 250) - 45 * (miles // 1000) - 500 * (miles // 1500) - 7500 * (miles // 10000), self.truck.earned_money)

    def test_eat(self):
        self.truck.earned_money = 10000
        self.truck.eat(250)
        self.assertEqual(9980, self.truck.earned_money)

    def test_sleep(self):
        self.truck.earned_money = 10000
        self.truck.sleep(1000)
        self.assertEqual(9955, self.truck.earned_money)

    def test_pump_gas(self):
        self.truck.earned_money = 10000
        self.truck.pump_gas(1500)
        self.assertEqual(9500, self.truck.earned_money)

    def test_repair_truck(self):
        self.truck.earned_money = 10000
        self.truck.repair_truck(10000)
        self.assertEqual(2500, self.truck.earned_money)

    def test_repr(self):
        result = self.truck.__str__()
        self.assertEqual("BigBoss has 0 miles behind his back.", result)


if __name__ == '__main__':
    main()
