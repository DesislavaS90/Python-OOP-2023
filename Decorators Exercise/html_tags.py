def tags(data):
    def decorator(func):
        def wrapper(*args):
            return f'<{data}>{func(*args)}</{data}>'
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
