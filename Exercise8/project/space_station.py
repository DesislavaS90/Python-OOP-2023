from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUTS = {"Biologist": Biologist,
                        "Geodesist": Geodesist,
                        "Meteorologist": Meteorologist
                        }
    successful_missions = 0
    not_completed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'

        if astronaut_type not in self.VALID_ASTRONAUTS:
            raise Exception('Astronaut type is not valid!')

        astronaut = self.VALID_ASTRONAUTS[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        planet = Planet(name)
        self.planet_repository.add(planet)
        planet.items.extend(items.split(', '))
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f'Astronaut {name} doesn\'t exist!')

        astronaut = self.astronaut_repository.find_by_name(name)
        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):

        if not self.planet_repository.find_by_name(planet_name):
            raise Exception('Invalid planet name!')

        planet = self.planet_repository.find_by_name(planet_name)
        sorted_astronauts = sorted(list(filter(lambda x: x.oxygen > 30, self.astronaut_repository.astronauts)),
                                   key=lambda o: o.oxygen, reverse=True)[:5]

        if not sorted_astronauts:
            raise Exception('You need at least one astronaut to explore the planet!')

        participated_astronauts = 0

        while True:

            if len(sorted_astronauts) == 0:
                self.not_completed_missions += 1
                return 'Mission is not completed.'

            astronaut = sorted_astronauts.pop(0)
            participated_astronauts += 1
            item = planet.items.pop()

            astronaut.backpack.append(item)
            astronaut.breathe()
            if len(planet.items) == 0:
                self.successful_missions += 1
                return f"Planet: {planet_name} was explored. " \
                       f"{participated_astronauts} astronauts participated in collecting items."

            if astronaut.oxygen <= 0:
                continue
            else:
                sorted_astronauts.insert(0, astronaut)
                participated_astronauts -= 1

    def report(self):

        result = [f"Astronauts' info:"]

        new_line = '\n'

        for a in self.astronaut_repository.astronauts:
            result.extend([f'Name: {a.name}',
                           f'Oxygen: {a.oxygen}',
                           f'Backpack items: {", ".join(a.backpack) if a.backpack else "none"}'])

        return f'{self.successful_missions} successful missions!\n' \
               f'{self.not_completed_missions} missions were not completed!\n' \
               f'{new_line.join(result)}'
