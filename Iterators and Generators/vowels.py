class vowels:

    def __init__(self, text):
        self.text = text
        self.result = [v for v in self.text if v.lower() in 'a,e,o,i,u,y']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index == len(self.result):
            raise StopIteration

        current_index = self.index
        self.index += 1
        return self.result[current_index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
