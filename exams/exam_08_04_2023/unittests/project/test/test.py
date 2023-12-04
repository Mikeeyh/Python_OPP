from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Mike", 25, 150)

    def test_correct_init(self):
        self.assertEqual("Mike", self.player.name)
        self.assertEqual(25, self.player.age)
        self.assertEqual(150, self.player.points)
        self.assertListEqual([], self.player.wins)

    def test_correct_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Mi"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_correct_age(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_already_added(self):
        self.player.wins = ["WorldCup"]
        self.assertEqual("WorldCup has been already added to the list of wins!", self.player.add_new_win("WorldCup"))
        self.assertEqual(["WorldCup"], self.player.wins)

    def test_add_new_win_successfully(self):
        self.player.wins = []
        self.assertEqual([], self.player.wins)
        self.player.add_new_win("WorldCup")
        self.assertEqual(["WorldCup"], self.player.wins)

    def test_compare_points_1(self):
        player_2 = TennisPlayer("Novak", 29, 200)
        result = self.player.points < player_2.points
        self.assertTrue(result)
        self.assertEqual('Novak is a top seeded player and he/she is better than Mike', self.player.__lt__(player_2))

    def test_compare_points_2(self):
        player_2 = TennisPlayer("Novak", 29, 100)
        result = self.player.points < player_2.points
        self.assertFalse(result)
        self.assertEqual('Mike is a better player than Novak', self.player.__lt__(player_2))

    def test_string_repr_no_wins(self):
        result = "Tennis Player: Mike\nAge: 25\nPoints: 150.0\nTournaments won: "
        self.assertEqual(result, self.player.__str__())

    def test_string_repr_with_wins(self):
        self.player.wins = ["one", "two"]
        result = "Tennis Player: Mike\nAge: 25\nPoints: 150.0\nTournaments won: one, two"
        self.assertEqual(result, self.player.__str__())


if __name__ == '__main__':
    main()
