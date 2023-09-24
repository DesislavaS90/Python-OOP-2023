from project.car.car import Car


class SportsCar(Car):

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value not in range(400, 600 + 1):
            raise ValueError(f'Invalid speed limit! Must be between {400} and {600}!')
        self.__speed_limit = value