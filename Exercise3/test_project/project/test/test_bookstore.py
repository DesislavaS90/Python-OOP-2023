import unittest
from project.bookstore import Bookstore


class TestBookStore(unittest.TestCase):

    def setUp(self):
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertEqual(self.bookstore.books_limit, 10)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_book_limit_equal_zero(self):
        with self.assertRaises(ValueError) as context:
            self.bookstore.books_limit = 0
        self.assertEqual(str(context.exception), "Books limit of 0 is not valid")

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Harry Potter": 4,
            "Lord of the Rings": 3,
            "The Hobbit": 3
        }
        self.assertEqual(len(self.bookstore), 10)

    def test_receive_books_with_not_enough_space_in_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 4, "The Hobbit": 3}

        with self.assertRaises(Exception) as context:
            self.bookstore.receive_book("Lord of the Ring", 11)
        self.assertEqual(str(context.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_new_books_with_enough_space_in_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles = {"Lord of the Rings": 3}

        result = self.bookstore.receive_book("Harry Potter", 4)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"Lord of the Rings": 3, "Harry Potter": 4})
        self.assertEqual(result, '4 copies of Harry Potter are available in the bookstore.')

    def test_receive_existing_books_with_enough_space_in_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles = {"Lord of the Rings": 3, "Harry Potter": 1}

        result = self.bookstore.receive_book("Harry Potter", 3)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles,
                         {"Lord of the Rings": 3, "Harry Potter": 4})
        self.assertEqual(result, '4 copies of Harry Potter are available in the bookstore.')

    def test_sell_non_existing_book(self):
        with self.assertRaises(Exception) as context:
            self.bookstore.sell_book("Lord of the Rings", 2)
        self.assertEqual(str(context.exception), "Book Lord of the Rings doesn't exist!")

    def test_sell_existing_book_with_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Harry Potter": 4,
            "The Hobbit": 3
        }
        with self.assertRaises(Exception) as context:
            self.bookstore.sell_book("Harry Potter", 10)
        self.assertEqual(str(context.exception), "Harry Potter has not enough copies to sell. Left: 4")

    def test_sell_existing_book(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Harry Potter": 4,
            "The Hobbit": 3
        }
        result = self.bookstore.sell_book("Harry Potter", 4)

        self.assertEqual(result, 'Sold 4 copies of Harry Potter')
        self.assertEqual(self.bookstore.total_sold_books, 4)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {
            "Harry Potter": 0, "The Hobbit": 3})

    def test_str_method(self):
        self.bookstore.receive_book("Harry Potter", 4)
        self.bookstore.receive_book("The Hobbit", 3)
        self.bookstore.receive_book("Lord of the Rings", 3)
        self.bookstore.sell_book("Lord of the Rings", 2)
        self.assertEqual(str(self.bookstore),
                         'Total sold books: 2\n'
                         'Current availability: 8\n'
                         ' - Harry Potter: 4 copies\n'
                         ' - The Hobbit: 3 copies\n'
                         ' - Lord of the Rings: 1 copies')


if __name__ == '__main__':
    unittest.main()