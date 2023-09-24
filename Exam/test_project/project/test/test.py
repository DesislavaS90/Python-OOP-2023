from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer('Desi', 20, 100.00)

    def test_init_(self):
        self.assertEqual(self.player.name, 'Desi')
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.points, 100.00)
        self.assertEqual(self.player.wins, [])

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            self.player.name = 'De'
        self.assertEqual(str(context.exception), "Name should be more than 2 symbols!")

    def test_valid_name(self):
        result = self.player.name = 'Anna'
        self.assertEqual(result, self.player.name)

    def test_invalid_age(self):
        with self.assertRaises(ValueError) as context:
            self.player.age = 16
        self.assertEqual(str(context.exception), "Players must be at least 18 years of age!")

    def test_valid_age(self):
        result = self.player.age = 21
        self.assertEqual(result, self.player.age)

    def test_tournament_name_in_list(self):
        self.player.add_new_win('Wimbledon')
        self.assertEqual(self.player.add_new_win('Wimbledon'), "Wimbledon has been already added to the list of wins!")
        self.assertEqual(['Wimbledon'], self.player.wins)

    def test_add_valid_tournament_name(self):
        result = self.player.add_new_win('US Open')
        self.assertEqual(result, ['US Open'])

    def test_it_method_with_other_winner(self):
        new_player = TennisPlayer('Ivo', 25, 150.00)
        result = self.player.__lt__(new_player)
        self.assertEqual(result, 'Ivo is a top seeded player and he/she is better than Desi')

    def test_it_method_with_me_winner(self):
        new_player = TennisPlayer('Ivo', 25, 80.00)
        result = self.player.__lt__(new_player)
        self.assertEqual(result, 'Desi is a better player than Ivo')

    def test_str_method(self):
        self.player.add_new_win('Wimbledon')
        self.player.add_new_win('US Open')

        self.assertEqual(str(self.player),
                         "Tennis Player: Desi\n"
                         "Age: 20\n"
                         "Points: 100.0\n"
                         "Tournaments won: Wimbledon, US Open")


if __name__ == '__main__':
    unittest.main()


