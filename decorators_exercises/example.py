from functools import wraps


def t_decorator(func):
    # @wraps(func)
    def wrapper(*arg):
        """ documentations from wrapper """
        print("Starting")
        func()
        print("End")
    return wrapper


@t_decorator
def t():
    """ function documentations """
    print("Test")


t()
print(t.__name__)  # returns the name of the function 'wrapper'
print(t.__doc__) # returns the documentations in wrapper function if there isn't any docs, returns 'None'

"""
If we add @wraps(func) we will receive the functions name 't' 
and functions 't' documentations if any
"""