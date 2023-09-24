def vowel_filter(function):
    def wrapper():
        letters = function()
        return [v for v in letters if v in 'a,e,i,o,u']
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())

