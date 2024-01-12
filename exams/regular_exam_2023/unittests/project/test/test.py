from project.railway_station import RailwayStation
from unittest import TestCase, main
from collections import deque


class TestRailwayStation(TestCase):
    def test_correct_init(self):
        station = RailwayStation("London")
        self.assertEqual("London", station.name)
        self.assertEqual(deque(), station.arrival_trains)
        self.assertEqual(deque(), station.departure_trains)

    def test_setter_name(self):
        with self.assertRaises(ValueError) as ve:
            RailwayStation("Lon")
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        station = RailwayStation("London")
        station.new_arrival_on_board("Train_France")
        station.new_arrival_on_board("Train_Portsmouth")

        self.assertEqual(deque(["Train_France", "Train_Portsmouth"]), station.arrival_trains)

    def test_train_has_arrived_correct_first_train_check(self):
        station = RailwayStation("London")
        station.new_arrival_on_board("Train_France")
        station.new_arrival_on_board("Train_Portsmouth")

        result_arrived = station.train_has_arrived("Train_France")
        self.assertEqual("Train_France is on the platform and will leave in 5 minutes.", result_arrived)
        self.assertEqual(deque(["Train_Portsmouth"]), station.arrival_trains)
        self.assertEqual(deque(["Train_France"]), station.departure_trains)

    def test_train_has_arrived_not_correct_first_train_check(self):
        station = RailwayStation("London")
        station.new_arrival_on_board("Train_France")
        station.new_arrival_on_board("Train_Portsmouth")

        result_arrived = station.train_has_arrived("Train_Portsmouth")
        self.assertEqual("There are other trains to arrive before Train_Portsmouth.", result_arrived)

    def test_train_has_left_return_true(self):
        station = RailwayStation("TestStation")
        station.new_arrival_on_board("Train_France")
        station.new_arrival_on_board("Train_Portsmouth")

        station.train_has_arrived("Train_France")

        self.assertTrue(station.train_has_left("Train_France"))

    def test_train_has_left_return_false(self):
        station = RailwayStation("TestStation")
        station.new_arrival_on_board("Train_France")
        station.new_arrival_on_board("Train_Portsmouth")

        station.train_has_arrived("Train_France")

        self.assertFalse(station.train_has_left("Train_Portsmouth"))


if __name__ == '__main__':
    main()
