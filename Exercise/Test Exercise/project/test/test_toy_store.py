from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_initialisation(self):
        self.assertEqual(len(self.store.toy_shelf), 7)

        for l in range(ord('A'), ord('G') + 1):
            self.assertIsNone(self.store.toy_shelf[chr(l)])

    def test_add_toy_to_non_existing_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.add_toy('Z', 'Doll')
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_add_already_existing_toy(self):
        self.store.add_toy('A', 'Doll')
        with self.assertRaises(Exception) as context:
            self.store.add_toy('A', 'Doll')
        self.assertEqual(str(context.exception), "Toy is already in shelf!")

    def test_toy_shelf_is_not_none(self):
        self.store.add_toy('A', 'Doll')
        with self.assertRaises(Exception) as context:
            self.store.add_toy('A', 'Car')
        self.assertEqual(str(context.exception), "Shelf is already taken!")

    def test_add_toy_on_existing_shelf_with_free_space(self):
        self.assertEqual('Toy:Doll placed successfully!', self.store.add_toy('A', 'Doll'))

    def test_remove_shelf_which_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.store.remove_toy('Z', 'Doll')
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_remove_not_existing_toy(self):
        with self.assertRaises(Exception) as context:
            self.store.remove_toy('A', 'Doll')
        self.assertEqual(str(context.exception), "Toy in that shelf doesn't exists!")

    def test_successfully_remove_toy(self):
        self.store.add_toy('B', 'Car')
        self.assertEqual('Remove toy:Car successfully!', self.store.remove_toy('B', 'Car'))
        self.assertIsNone(self.store.toy_shelf['B'])


if __name__ == '__main__':
    unittest.main()