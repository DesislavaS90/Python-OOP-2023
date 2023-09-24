def multiply(times):
    def decorator(function):

        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = function(*args, **kwargs)
                return times * result
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))