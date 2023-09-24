import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(20.5, 175.5)

    def test_initialisation(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_when_fuel_not_enough(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(50)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_when_fuel_is_enough(self):
        self.vehicle.drive(3)
        self.assertEqual(16.75, self.vehicle.fuel)

    def test_when_fuel_is_more_than_capacity(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(40.5)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_when_fuel_is_enough_for_capacity(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)
        self.assertEqual(10, self.vehicle.fuel)

    def test_str_(self):
        self.assertEqual(
               f"The vehicle has 175.5 " +
               f"horse power with 20.5 fuel left and 1.25 fuel consumption",
               str(self.vehicle)
        )


if __name__ == '__main__':
    unittest.main()


     

