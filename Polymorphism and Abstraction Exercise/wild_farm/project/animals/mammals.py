from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    FOOD = [Vegetable, Fruit]
    GAIN = 0.10

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    FOOD = [Meat]
    GAIN = 0.40

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    FOOD = [Vegetable, Meat]
    GAIN = 0.30

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    FOOD = [Meat]
    GAIN = 1.00

    def make_sound(self):
        return 'ROAR!!!'
