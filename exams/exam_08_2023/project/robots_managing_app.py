from typing import List
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(r for r in self.robots if r.name == robot_name)
        service = next(s for s in self.services if s.name == service_name)
        if (service.__class__.__name__ == "SecondaryService" and robot.__class__.__name__ == "FemaleRobot") or (
                service.__class__.__name__ == "MainService" and robot.__class__.__name__ == "MaleRobot"
        ):
            if len(service.robots) >= service.capacity:
                raise Exception("Not enough capacity for this robot!")
            self.robots.remove(robot)
            service.robots.append(robot)
            return f"Successfully added {robot_name} to {service_name}."
        else:
            return "Unsuitable service."

    # def add_robot_to_service(self, robot_name: str, service_name: str):
    #     robot_obj = self._find_obj_by_name(robot_name, self.robots)
    #     service_obj = self._find_obj_by_name(service_name, self.services)
    #     if robot_obj.POSSIBLE_SERVICE != service_obj.__class__.__name__:
    #         return "Unsuitable service."
    #     if len(service_obj.robots) >= service_obj.capacity:
    #         raise Exception("Not enough capacity for this robot!")
    #     self.robots.remove(robot_obj)
    #     service_obj.robots.append(robot_obj)
    #     return f"Successfully added {robot_name} to {service_name}."

    # @staticmethod
    # def _find_obj_by_name(name, collection):  # existing name
    #     return [obj for obj in collection if obj.name == name][0]

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)
        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        number_of_robots_fed = 0

        for robot in service.robots:
            robot.eating()
            number_of_robots_fed += 1
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        total_price = sum(r.price for r in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = [s.details() for s in self.services]
        return "\n".join(result)
