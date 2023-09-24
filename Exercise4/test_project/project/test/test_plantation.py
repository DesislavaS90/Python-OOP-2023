import unittest
from project.plantation import Plantation


class TestPlantation(unittest.TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(3)

    def test_init(self):
        self.assertEqual(self.plantation.size, 3)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_invalid_size(self):
        with self.assertRaises(ValueError) as context:
            self.plantation.size = -1
        self.assertEqual(str(context.exception), "Size must be positive number!")

    def test_hire_worker(self):
        result = self.plantation.hire_worker("Ivan")
        self.assertEqual(result, "Ivan successfully hired.")
        self.assertEqual(self.plantation.workers, ["Ivan"])

    def test_hire_worker_already_hired(self):
        self.plantation.hire_worker("Ivan")
        with self.assertRaises(ValueError) as context:
            self.plantation.hire_worker("Ivan")
        self.assertEqual(str(context.exception), "Worker already hired!")

    def test_len_method(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Anna")
        self.plantation.planting("Ivan", "Tomato")
        self.plantation.planting("Anna", "Potato")
        self.plantation.planting("Anna", "Carrot")
        self.assertEqual(len(self.plantation), 3)
        self.assertEqual(self.plantation.plants, {'Ivan': ['Tomato'], 'Anna': ['Potato', 'Carrot']})

    def test_planting_invalid_worker(self):
        with self.assertRaises(ValueError) as context:
            self.plantation.planting("Ivan", "Tomato")
        self.assertEqual(str(context.exception), "Worker with name Ivan is not hired!")

    def test_plantation_is_full(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "Tomato")
        self.plantation.planting("Ivan", "Carrot")
        self.plantation.planting("Ivan", "Potato")
        with self.assertRaises(ValueError) as context:
            self.plantation.planting('Ivan', 'Apple')
        self.assertEqual(str(context.exception), "The plantation is full!")

    def test_planting_existing_worker(self):
        self.plantation.hire_worker('Ivan')
        self.plantation.plants = {'Ivan': ['Tomato', 'Cucumber']}

        result = self.plantation.planting('Ivan', 'Potato')

        self.assertEqual(result, 'Ivan planted Potato.')
        self.assertEqual(self.plantation.plants, {'Ivan': ['Tomato', 'Cucumber', 'Potato']})
        self.assertEqual(len(self.plantation), 3)

    def test_planted_non_existing_worker_in_dict(self):
        self.plantation.hire_worker("Ivan")
        result = self.plantation.planting('Ivan', 'Potato')
        self.assertEqual(result, "Ivan planted it's first Potato.")
        self.assertEqual(self.plantation.plants, {'Ivan': ['Potato']})
        self.assertEqual(len(self.plantation), 1)

    def test_str_method(self):
        self.plantation.workers = ['Ivan', 'Anna']
        self.plantation.plants = {'Ivan': ['Tomato', 'Cucumber'],
                                  'Anna': ['Potato']}
        self.assertEqual(str(self.plantation),
                         f'Plantation size: 3\n'
                         f'Ivan, Anna\n'
                         f'Ivan planted: Tomato, Cucumber\n'
                         f'Anna planted: Potato')

    def test_repr_method(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Anna")
        self.assertEqual(repr(self.plantation),
                         f'Size: 3\n'
                         f'Workers: Ivan, Anna')


if __name__ == '__main__':
    unittest.main()