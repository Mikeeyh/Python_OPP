from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self):
        self.t1f = Trip(10000, 1, False)
        self.t2f = Trip(10000, 2, False)
        self.t2t = Trip(10000, 2, True)

    def test_correct_init(self):
        self.assertEqual(10000, self.t2t.budget)
        self.assertEqual(2, self.t2t.travelers)
        self.assertFalse(self.t2f.is_family)
        self.assertEqual({}, self.t2t.booked_destinations_paid_amounts)

    def test_setter_travelers(self):
        with self.assertRaises(ValueError) as ve:
            self.t1f.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_expected_correct_boolean(self):
        self.assertTrue(self.t2t.is_family)

        self.t1f.is_family = True
        self.assertFalse(self.t1f.is_family)

    def test_book_a_trip_with_not_existing_destination(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         self.t2t.book_a_trip("not existing destination"))

    def test_book_a_trip_with_not_enough_budget(self):
        self.assertEqual('Your budget is not enough!', self.t2t.book_a_trip('New Zealand'))

    def test_book_a_trip_no_family_discount(self):
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 9000.00',
                         self.t2f.book_a_trip('Bulgaria'))
        self.assertEqual(9000, self.t2f.budget)
        self.assertEqual({"Bulgaria": 1000}, self.t2f.booked_destinations_paid_amounts)

    def test_book_a_trip_with_family_discount(self):
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 9100.00',
                         self.t2t.book_a_trip('Bulgaria'))
        self.assertEqual(9100, self.t2t.budget)
        self.assertEqual({"Bulgaria": 900}, self.t2t.booked_destinations_paid_amounts)

    def test_booking_status_no_bookings(self):
        self.assertEqual('No bookings yet. Budget: 10000.00', self.t2t.booking_status())

    def test_booking_status_with_bookings(self):
        self.t2f.budget = 100000
        self.t2f.book_a_trip("Brazil")
        self.t2f.book_a_trip("New Zealand")

        result = self.t2f.booking_status()
        expected_result = """Booked Destination: Brazil
Paid Amount: 12400.00
Booked Destination: New Zealand
Paid Amount: 15000.00
Number of Travelers: 2
Budget Left: 72600.00"""

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
