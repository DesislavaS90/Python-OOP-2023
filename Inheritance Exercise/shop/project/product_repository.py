from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name):
        p = self.find(product_name)
        if p:
            self.products.remove(p)

    def __repr__(self):
        return '\n'.join([f'{p}: {p.quantity}' for p in self.products])


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
