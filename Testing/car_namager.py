class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car('Mini', 'Cooper', 10, 80)

    def test_initialisation(self):
        self.assertEqual(self.car.make, 'Mini')
        self.assertEqual(self.car.model, 'Cooper')
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 80)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_cannot_be_empty(self):
        with self.assertRaises(Exception) as context:
            Car('', 'Cooper', 10, 80)
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_model_cannot_be_empty(self):
        with self.assertRaises(Exception) as context:
            Car('Mini', '', 10, 80)
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_cannot_be_zero(self):
        with self.assertRaises(Exception) as context:
            Car('Mini', 'Cooper', 0, 80)
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_cannot_be_zero(self):
        with self.assertRaises(Exception) as context:
            Car('Mini', 'Cooper', 10, 0)
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_cannot_be_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_cannot_be_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_valid_refuel(self):
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_amount, 5)

    def test_refuel_over_capacity(self):
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_capacity, self.car.fuel_capacity)

    def test_drive_over_the_fuel_capacity(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(1000)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")

    def test_drive_with_enough_fuel(self):
        self.car.refuel(100)
        self.car.drive(10)
        self.assertEqual(79, self.car.fuel_amount)


if __name__ == '__main__':
    unittest.main()

