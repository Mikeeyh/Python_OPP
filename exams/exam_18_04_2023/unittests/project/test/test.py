from project.robot import Robot
from unittest import TestCase, main


class TestSRobot(TestCase):
    def setUp(self):
        self.robot = Robot("robot_id", "Military", 100, 2000)

    def test_correct_init(self):
        self.assertEqual("robot_id", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(2000, self.robot.price)
        self.assertListEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_wrong_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Not_a_valid_category"
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_negative_price(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_not_existing_hardware_component(self):
        result = self.robot.upgrade("new_component", 100)
        self.assertEqual(["new_component"], self.robot.hardware_upgrades)
        self.assertEqual(2150, self.robot.price)
        self.assertEqual('Robot robot_id was upgraded with new_component.', result)

    def test_upgrade_with_existing_hardware_component(self):
        self.robot.hardware_upgrades = ["old_component"]
        result = self.robot.upgrade("old_component", 100)
        self.assertEqual("Robot robot_id was not upgraded.", result)

    def test_update_with_not_existing_version_and_enough_capacity(self):
        result = self.robot.update(11.11, 50)
        self.assertEqual(self.robot.software_updates, [11.11])
        self.assertEqual(self.robot.available_capacity, 50)
        self.assertEqual('Robot robot_id was updated to version 11.11.', result)

    def test_update_with_not_existing_version_and_not_enough_capacity(self):
        result = self.robot.update(11.11, 1000)
        self.assertEqual("Robot robot_id was not updated.", result)

    def test_update_with_existing_version_and_enough_capacity(self):
        self.robot.software_updates = [11.11]
        result = self.robot.update(11.11, 20)
        self.assertEqual("Robot robot_id was not updated.", result)

    def test_update_with_lower_version_and_enough_capacity(self):
        self.robot.software_updates = [11.11]
        result = self.robot.update(3.12, 20)
        self.assertEqual("Robot robot_id was not updated.", result)

    def test_gt_if_first_robot_price_is_higher(self):
        robot_2 = Robot('R1', 'Education', 200, 0)
        result = self.robot > robot_2
        self.assertEqual('Robot with ID robot_id is more expensive than Robot with ID R1.', result)

    def test_gt_if_equal_prices(self):
        robot_2 = Robot('R1', 'Education', 200, 2000)
        result = self.robot > robot_2
        self.assertEqual('Robot with ID robot_id costs equal to Robot with ID R1.', result)

    def test_gt_if_first_robot_price_is_lower(self):
        robot_2 = Robot('R1', 'Education', 200, 3000)
        result = self.robot > robot_2
        self.assertEqual('Robot with ID robot_id is cheaper than Robot with ID R1.', result)


if __name__ == '__main__':
    main()
