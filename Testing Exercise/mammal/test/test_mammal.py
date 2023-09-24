import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('some name', 'some type', 'some sound')

    def test_initialisation(self):
        self.assertEqual(self.mammal.name, 'some name')
        self.assertEqual(self.mammal.type, 'some type')
        self.assertEqual(self.mammal.sound, 'some sound')

    def test_make_sound(self):
        self.assertEqual('some name makes some sound', self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual('some name is of type some type', self.mammal.info())


if __name__ == '__main__':
    unittest.main()
