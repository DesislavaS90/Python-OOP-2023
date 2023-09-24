import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero('some hero', 1, 100, 100)
        self.enemy = Hero('some enemy', 1, 50, 50)

    def test_initialisation(self):
        self.assertEqual('some hero', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_if_new_name_is_same_as_current(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual(str(context.exception), 'You cannot fight yourself')

    def test_if_hero_health_when_is_less_than_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_if_enemy_health_when_is_less_than_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), "You cannot fight some enemy. He needs to rest")

    def test_health_and_damage_after_equal_fight(self):
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.health

        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual('Draw', result)

    def test_when_hero_wins_and_parameters_improves(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual('You win', result)

    def test_when_hero_loses_and_parameters_decreases(self):
        self.hero, self.enemy = self.enemy, self.hero
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual('You lose', result)

    def test_str_(self):

        self.assertEqual(
            f"Hero some hero: 1 lvl\n" +
            f"Health: 100\n" +
            f"Damage: 100\n",
            str(self.hero)
        )


if __name__ == '__main__':
    unittest.main()