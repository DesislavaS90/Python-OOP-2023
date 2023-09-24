from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    MAXIMUM_SPEED = 140

    def train(self):
        if self.speed + 3 <= Thoroughbred.MAXIMUM_SPEED:
            self.speed += 3
        else:
            self.speed = Thoroughbred.MAXIMUM_SPEED
