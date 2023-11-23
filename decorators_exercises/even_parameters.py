def even_parameters(function):

    def wrapper(*args):
        if any(not isinstance(el, int) or el % 2 != 0 for el in args):
            return "Please use only even numbers!"
        return function(*args)
    return wrapper

    # def wrapper(*args, **kwargs):
    #     if all(isinstance(arg, int) and arg % 2 == 0 for arg in args):
    #         return function(*args, **kwargs)
    #     else:
    #         return "Please use only even numbers!"
    # return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
