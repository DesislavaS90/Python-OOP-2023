class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError('Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError('Users under the age of 6 are not allowed!')
        self.__age = value

    def __str__(self):
        new_line = '\n'

        return f"Username: {self.username}, Age: {self.age}\n"\
               f"Liked movies:\n"\
               f"{new_line.join(m.details() for m in self.movies_liked)if self.movies_liked else 'No movies liked.'}\n"\
               f"Owned movies:\n"\
               f"{new_line.join(m.details() for m in self.movies_owned)if self.movies_owned else 'No movies owned.'}"
