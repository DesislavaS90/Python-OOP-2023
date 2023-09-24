from project.product import Product


class Food(Product):
    def __init__(self, name):
        self.name = name
        super().__init__(name, 15)