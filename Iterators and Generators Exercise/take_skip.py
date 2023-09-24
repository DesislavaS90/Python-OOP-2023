class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.count == self.counter:
            raise StopIteration

        return self.counter * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)