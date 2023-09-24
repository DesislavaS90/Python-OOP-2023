from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver('John', 10.0)

    def test_initialisation(self):
        self.assertEqual(self.driver.name, 'John')
        self.assertEqual(self.driver.money_per_mile, 10.0)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_negative_earned_money(self):
        with self.assertRaises(ValueError) as context:
            self.driver.earned_money = -1
        self.assertEqual(str(context.exception), f"{self.driver.name} went bankrupt.")

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer('Razlog', 2000)

        with self.assertRaises(ValueError) as context:
            self.driver.drive_best_cargo_offer()
        self.assertEqual(str(context.exception), f"{self.driver.name} went bankrupt.")

    def test_add_successfully_cargo(self):
        result = self.driver.add_cargo_offer('Sofia', 100)

        self.assertEqual(result, 'Cargo for 100 to Sofia was added as an offer.')
        self.assertEqual(self.driver.available_cargos, {'Sofia': 100})

    def test_add_existing_cargo(self):
        self.driver.available_cargos = {'Sofia': 100}
        with self.assertRaises(Exception) as context:
            self.driver.add_cargo_offer('Sofia', 100)
        self.assertEqual(str(context.exception), "Cargo offer is already added.")

    def test_valid_cargo_best_offer(self):
        self.driver.add_cargo_offer('Sofia', 200)
        self.driver.add_cargo_offer('Plovdiv', 350)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(result, f'{self.driver.name} is driving 350 to Plovdiv.')
        self.assertEqual(self.driver.earned_money, 3480)
        self.assertEqual(self.driver.miles, 350)

    def test_no_available_cargo_offer(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, 'There are no offers available.')

    def test_eat(self):
        self.driver.earned_money = 50
        self.driver.eat(250)
        self.driver.eat(250)
        self.assertEqual(self.driver.earned_money, 10)

    def test_sleep(self):
        self.driver.earned_money = 50
        self.driver.sleep(1000)
        self.driver.sleep(1500)
        self.assertEqual(self.driver.earned_money, 5)

    def test_pump_gas(self):
        self.driver.earned_money = 1100
        self.driver.pump_gas(1500)
        self.driver.pump_gas(1500)
        self.assertEqual(self.driver.earned_money, 100)

    def test_repair_truck(self):
        self.driver.earned_money = 20000
        self.driver.repair_truck(10000)
        self.driver.repair_truck(20000)
        self.assertEqual(self.driver.earned_money, 5000)

    def test_repr_(self):
        self.assertEqual(str(self.driver), 'John has 0 miles behind his back.')


if __name__ == '__main__':
    unittest.main()
