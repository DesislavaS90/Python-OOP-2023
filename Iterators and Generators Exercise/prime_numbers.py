def get_primes(data):

    for d in data:
        if d <= 1:
            continue
        for num in range(2, d):
            if d % num == 0:
                break
        else:
            yield d


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
