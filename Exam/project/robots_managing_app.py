from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_SERVICE_TYPE = {'MainService': MainService, 'SecondaryService': SecondaryService}
    VALID_ROBOT_TYPE = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPE:
            raise Exception('Invalid service type!')
        self.services.append(self.VALID_SERVICE_TYPE[service_type](name))
        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPE:
            raise Exception('Invalid robot type!')
        self.robots.append(self.VALID_ROBOT_TYPE[robot_type](name, kind, price))
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if (robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'SecondaryService')\
                or (robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'MainService'):
            if len(service.robots) < service.capacity:
                self.robots.remove(robot)
                service.robots.append(robot)
                return f'Successfully added {robot_name} to {service_name}.'
            raise Exception('Not enough capacity for this robot!')
        return 'Unsuitable service.'

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception('No such robot in this service!')
        service.robots.remove(robot[0])
        self.robots.append(robot[0])
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]

        for r in service.robots:
            r.eating()
        return f'Robots fed: {len(service.robots)}.'

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        result = sum([r.price for r in service.robots])

        return f'The value of service {service_name} is {result:.2f}.'

    def __str__(self):
        return '\n'.join(s.details() for s in self.services)







