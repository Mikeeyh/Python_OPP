def logged(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"you called {function.__name__}({', '.join([str(el) for el in args])})\nit returned {result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
print(func(4, 4, 4))
