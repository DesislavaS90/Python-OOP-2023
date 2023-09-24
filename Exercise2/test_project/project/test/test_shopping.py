from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.shop_cart = ShoppingCart('Desi', 500)

    def test_init_(self):
        self.assertEqual(self.shop_cart.shop_name, 'Desi')
        self.assertEqual(self.shop_cart.budget, 500)
        self.assertEqual(self.shop_cart.products, {})

    def test_invalid_shop_name(self):
        with self.assertRaises(ValueError) as context:
            self.shop_cart.shop_name = 'desi123'
        self.assertEqual(str(context.exception), 'Shop must contain only letters and must start with capital letter!')

    def test_valid_shop_name(self):
        result = self.shop_cart.shop_name = 'Ani'
        self.assertEqual(result, self.shop_cart.shop_name)

    def test_expensive_product(self):
        with self.assertRaises(ValueError) as context:
            self.shop_cart.add_to_cart('Juice', 105.00)
        self.assertEqual(str(context.exception), 'Product Juice cost too much!')

    def test_adding_valid_product(self):
        result = self.shop_cart.add_to_cart('Cheese', 50.00)

        self.assertEqual(result, 'Cheese product was successfully added to the cart!')
        self.assertEqual(self.shop_cart.products, {'Cheese': 50.00})

    def test_remove_non_existing_product(self):
        self.shop_cart.products = {'Cheese': 50.00, 'Juice': 10.00}
        with self.assertRaises(ValueError) as context:
            self.shop_cart.remove_from_cart('Pizza')
        self.assertEqual(str(context.exception), 'No product with name Pizza in the cart!')

    def test_remove_valid_product(self):
        self.shop_cart.products = {'Cheese': 50.00, 'Juice': 10.00}
        result = self.shop_cart.remove_from_cart('Cheese')
        self.assertEqual(result, 'Product Cheese was successfully removed from the cart!')
        self.assertEqual(self.shop_cart.products, {'Juice': 10.00})

    def test_adding_new_shop_instance(self):
        self.shop_cart.products = {'Cheese': 50.00}
        new_shop = ShoppingCart('Ani', 600)
        new_shop.products = {'Cake': 80.00}
        new_shop_cart = self.shop_cart.__add__(new_shop)
        self.assertEqual(new_shop.shop_name, 'Ani')
        self.assertEqual(new_shop.budget, 600)
        self.assertEqual(new_shop_cart.products, {'Cheese': 50.00, 'Cake': 80.00})

    def test_buy_products_with_not_enough_budget(self):
        self.shop_cart.budget = 50
        self.shop_cart.products = {'Cheese': 50.00, 'Juice': 10.00}
        with self.assertRaises(ValueError) as context:
            self.shop_cart.buy_products()
        self.assertEqual(str(context.exception), 'Not enough money to buy the products! Over budget with '
                                                 '10.00lv!')

    def test_buy_products_with_enough_budget(self):
        self.shop_cart.products = {'Cheese': 50.00, 'Juice': 10.00}
        self.assertEqual(self.shop_cart.buy_products(), 'Products were successfully bought! Total cost: 60.00lv.')


if __name__ == '__main__':
    unittest.main()