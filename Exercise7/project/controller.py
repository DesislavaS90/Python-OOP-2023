from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    CAR_TYPES = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = [c for c in self.cars if c.model == model]

        if car:
            raise Exception(f'Car {model} is already created!')

        if car_type in self.CAR_TYPES:
            self.cars.append(self.CAR_TYPES[car_type](model, speed_limit))
            return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):
        driver = [d for d in self.drivers if d.name == driver_name]

        if driver:
            raise Exception(f'Driver {driver_name} is already created!')

        self.drivers.append(Driver(driver_name))
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]

        if race:
            raise Exception(f'Race {race_name} is already created!')

        self.races.append(Race(race_name))
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = [d for d in self.drivers if d.name == driver_name]

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        new_list = reversed(self.cars)

        for c in new_list:
            if c.__class__.__name__ == car_type and not c.is_taken:
                if driver[0].car is not None:
                    old_model = driver[0].car.model
                    driver[0].car.is_taken = False
                    driver[0].car = c
                    c.is_taken = True
                    return f'Driver {driver[0].name} changed his car from {old_model} to {c.model}.'
                else:
                    driver[0].car = c
                    c.is_taken = True
                    return f'Driver {driver[0].name} chose the car {c.model}.'
        else:
            raise Exception(f'Car {car_type} could not be found!')

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = [r for r in self.races if r.name == race_name]
        driver = [d for d in self.drivers if d.name == driver_name]

        if not race:
            raise Exception(f'Race {race_name} could not be found!')
        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')
        if driver[0].car is None:
            raise Exception(f'Driver {driver_name} could not participate in the race!')
        if driver[0] in race[0].drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'

        race[0].drivers.append(driver[0])
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]

        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if len(race[0].drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')

        winners = sorted(race[0].drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]

        winner_list = []

        for w in winners:
            w.number_of_wins += 1
            winner_list.append(f'Driver {w.name} wins the {race_name} race with a speed of {w.car.speed_limit}.')

        return '\n'.join(winner_list)

