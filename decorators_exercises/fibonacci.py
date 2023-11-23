def cache(func):
    log = {}

    def wrapper(n):
        if not wrapper.log.get(n):  # checks if the key 'n' is already in the dictionary
            wrapper.log[n] = func(n)  # if not, we add it to the dictionary
        return wrapper.log[n]  # then we return it
    wrapper.log = {}  # in order to have access and print fibonacci.log

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)
