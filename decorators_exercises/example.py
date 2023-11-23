def t_decorator(func):
    def wrapper(*arg):
        print("Starting")
        func()
        print("End")
    return wrapper


@t_decorator
def t():
    print("Test")


t()
