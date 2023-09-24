import unittest
from project.robot import Robot

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot('1', 'Military', 100, 10)

    def test_init(self):
        self.assertEqual(self.robot.robot_id, '1')
        self.assertEqual(self.robot.category, 'Military')
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 10)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_invalid_category(self):
        with self.assertRaises(ValueError) as context:
            self.robot.category = 'invalid'
        self.assertEqual(str(context.exception),
                         "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as context:
            self.robot.price = -1
        self.assertEqual(str(context.exception), "Price cannot be negative!")

    def test_existing_hardware(self):
        self.robot.hardware_upgrades = ['Laser']
        result = self.robot.upgrade('Laser', 5)
        self.assertEqual(result, 'Robot 1 was not upgraded.')

    def test_non_existing_hardware(self):
        result = self.robot.upgrade('Laser', 5)
        self.assertEqual(result, 'Robot 1 was upgraded with Laser.')
        self.assertEqual(self.robot.price, 17.5)
        self.assertEqual(self.robot.hardware_upgrades, ['Laser'])

    def test_invalid_update(self):
        self.robot.software_updates = [2.0, 3.0]
        result = self.robot.update(1.65, 105)
        self.assertEqual(result, 'Robot 1 was not updated.')

    def test_valid_update(self):
        self.robot.software_updates = [2.0, 3.0]
        result = self.robot.update(4.65, 40)
        self.assertEqual(result, 'Robot 1 was updated to version 4.65.')
        self.assertEqual(self.robot.software_updates, [2.0, 3.0, 4.65])
        self.assertEqual(self.robot.available_capacity, 60)

    def test_gt_method_with_current_price_bigger(self):
        Robot2 = Robot('2', 'Military', 100, 5)
        result = self.robot > Robot2
        self.assertEqual(result, 'Robot with ID 1 is more expensive than Robot with ID 2.')

    def test_gt_method_with_current_price_equal(self):
        Robot2 = Robot('2', 'Military', 100, 10)
        result = self.robot > Robot2
        self.assertEqual(result, 'Robot with ID 1 costs equal to Robot with ID 2.')

    def test_gt_method_with_current_price_smaller(self):
        Robot2 = Robot('2', 'Military', 100, 20)
        result = self.robot > Robot2
        self.assertEqual(result, 'Robot with ID 1 is cheaper than Robot with ID 2.')


