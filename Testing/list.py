class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

import unittest


class TestIntegerList(unittest.TestCase):

    def setUp(self) -> None:
        self.integer = IntegerList('cat', 2, 66, 10, '101', 70)

    def test_initialisation(self):
        self.integer.get_data()
        self.assertEqual([2, 66, 10, 70], self.integer.get_data())

    def test_add_valid_element(self):
        self.integer.add(5)
        self.assertEqual([2, 66, 10, 70, 5], self.integer.get_data())

    def test_add_invalid_element(self):
        with self.assertRaises(ValueError) as context:
            self.integer.add('D')
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_valid_index(self):
        self.integer.remove_index(1)
        self.assertEqual([2, 10, 70], self.integer.get_data())

    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.integer.remove_index(10)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_valid_index(self):
        self.integer.get(3)
        self.assertEqual([2, 66, 10, 70], self.integer.get_data())

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.integer.get(8)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_valid_index_element(self):
        self.integer.insert(1, 100)
        self.assertEqual([2, 100, 66, 10, 70], self.integer.get_data())

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.integer.insert(20, 100)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_invalid_element(self):
        with self.assertRaises(ValueError) as context:
            self.integer.insert(1, 'D')
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_the_biggest_int(self):
        self.assertEqual(70, self.integer.get_biggest())

    def test_get_the_element(self):
        self.assertEqual(2, self.integer.get_index(10))


if __name__ == '__main__':
    unittest.main()







