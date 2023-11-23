from functools import wraps


def uppercase(function):
    @wraps(function)
    def wrapper():
        """ From wrapper """
        result = function()
        uppercase_result = result.upper()
        return uppercase_result
    return wrapper


@uppercase
def say_hi():
    """ Saying Hi """
    return 'hello there'


print(say_hi())  # returns HELLO THERE


print(say_hi.__name__)  # wrapper
print(say_hi.__doc__)  # this returns From wrapper

""" 
If we use wraps(), it will return:
say_hi
Saying Hi 
"""

