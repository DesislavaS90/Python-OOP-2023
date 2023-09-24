from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    FOOD = [Meat]
    GAIN = 0.25

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    FOOD = [Vegetable, Fruit, Meat, Seed]
    GAIN = 0.35

    def make_sound(self):
        return 'Cluck'

