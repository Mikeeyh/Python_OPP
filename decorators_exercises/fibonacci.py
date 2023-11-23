def cache(func):
    log = {}

    def wrapper(n):
        # Check if the result is already in the cache
        if n not in log:
            # If not, calculate and store the result
            log[n] = func(n)
        return log

    # Attach the cache to the original function
    func.log = log

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)
