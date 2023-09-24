def even_parameters(func):
    def wrapper(*numbers):
        for num in numbers:
            if isinstance(num, int):
                if num % 2 == 0:
                    continue
            return 'Please use only even numbers!'
        return func(*numbers)
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))