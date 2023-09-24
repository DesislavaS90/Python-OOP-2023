from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    MAXIMUM_SPEED = 120

    def train(self):
        if self.speed + 2 <= Appaloosa.MAXIMUM_SPEED:
            self.speed += 2
        else:
            self.speed = Appaloosa.MAXIMUM_SPEED

