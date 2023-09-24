from itertools import permutations


def possible_permutations(data):

    for d in permutations(data):
        yield list(d)


[print(n) for n in possible_permutations([1, 2, 3])]