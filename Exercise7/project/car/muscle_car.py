from project.car.car import Car


class MuscleCar(Car):

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value not in range(250, 450 + 1):
            raise ValueError(f'Invalid speed limit! Must be between {250} and {450}!')
        self.__speed_limit = value
