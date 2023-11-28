from unittest import TestCase, main
from testing.hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Mike", 11, 10.5, 10)

    def test_correct_initialization(self):
        self.assertEqual("Mike", self.hero.username)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(10.5, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_with_yourself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero=Hero("Mike", 11, 10.5, 10))

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_str_representation_expect_correct_output(self):
        expected_string = f"Hero Mike: 11 lvl\nHealth: 10.5\nDamage: 10\n"
        self.assertEqual(expected_string, self.hero.__str__())


if __name__ == '__main__':
    main()

#     def battle(self, enemy_hero):
#         if self.health <= 0:
#             raise ValueError("Your health is lower than or equal to 0. You need to rest")
#
#         if enemy_hero.health <= 0:
#             raise ValueError(f"You cannot fight {enemy_hero.username}. He needs to rest")
#
#         player_damage = self.damage * self.level
#         enemy_hero_damage = enemy_hero.damage * enemy_hero.level
#
#         self.health -= enemy_hero_damage
#         enemy_hero.health -= player_damage
#
#         if self.health <= 0 and enemy_hero.health <= 0:
#             return "Draw"
#
#         if enemy_hero.health <= 0:
#             self.level += 1
#             self.health += 5
#             self.damage += 5
#             return "You win"
#
#         enemy_hero.level += 1
#         enemy_hero.health += 5
#         enemy_hero.damage += 5
#         return "You lose"