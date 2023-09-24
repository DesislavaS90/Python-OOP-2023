from project.product import Product


class Drink(Product):
    def __init__(self, name):
        self.name = name
        super().__init__(name, 10)
