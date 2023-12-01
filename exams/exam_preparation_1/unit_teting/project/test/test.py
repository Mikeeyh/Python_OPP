from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def setUp(self):
        self.trip = Trip(15000, 3, True)

    def test_correct_init(self):
        self.assertEqual(15000, self.trip.budget)
        self.assertEqual(3, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_with_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip = Trip(15000, 0, True)
            self.trip = Trip(15000, -2, True)
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_expected_correct_boolean(self):
        if self.trip.is_family and self.trip.travelers < 2:
            self.trip.is_family = False
            self.assertFalse(self.trip.is_family)
        else:
            self.assertTrue(self.trip.is_family)

    def test_book_a_trip_with_not_existing_destination(self):
        destination = "France"
        result = 'This destination is not in our offers, please choose a new one!'
        self.trip.book_a_trip(destination)
        self.assertEqual(result, self.trip.book_a_trip(destination))

    def test_book_a_trip_with_existing_destination_decrease_price_if_is_family(self):
        self.trip = Trip(20000, 3, True)

        destination = "Brazil"
        total_price = (6200 * 3) * 0.9
        result = 20000 - total_price
        self.trip.book_a_trip(destination)

        self.assertEqual(result, self.trip.budget)

    def test_book_a_trip_with_existing_destination_if_not_family(self):
        self.trip = Trip(20000, 2, False)
        destination = "Brazil"
        total_price = (6200 * 2)
        result = 20000 - total_price
        self.trip.book_a_trip(destination)

        self.assertEqual(result, self.trip.budget)

    def test_book_a_trip_with_not_enough_budget(self):
        self.trip = Trip(20000, 3, True)
        result = 'Your budget is not enough!'

        self.assertEqual(result, self.trip.book_a_trip('New Zealand'))

    def test_book_a_trip_with_enough_budget(self):
        self.trip = Trip(20000, 2, False)
        result = f'Successfully booked destination Brazil! Your budget left is 7600.00'

        self.assertEqual(result, self.trip.book_a_trip("Brazil"))

    def test_booking_status_without_booked_destinations(self):
        result = 'No bookings yet. Budget: 15000.00'
        self.assertEqual(result, self.trip.booking_status())

    def test_booking_status_with_booked_destinations(self):
        self.trip = Trip(1000, 2, False)
        self.trip.booked_destinations_paid_amounts = {'B': 300.00, 'A': 200.00}

        expected_result = """Booked Destination: A
Paid Amount: 200.00
Booked Destination: B
Paid Amount: 300.00
Number of Travelers: 2
Budget Left: 1000.00"""

        actual_result = self.trip.booking_status()
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()
