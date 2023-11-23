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


# if the decorator should accept some parameters we need 3 functions ---------------------------------------------------


def uppercase(n_letters):
    def decorator(function):
        def wrapper():
            result = function()
            upper_part = result[:n_letters + 1].upper()
            lower_part = result[n_letters:].lower()
            return upper_part + lower_part
        return wrapper
    return decorator


@uppercase(3)
def say_hi():
    return 'hello there'


print(say_hi())  # HELLlo there

# ----------------------------------------------------------------


def repeat(n):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * n
        return wrapper
    return decorator


@repeat(4)
def say(word):
    return word


print(say("Hello"))  # HelloHelloHelloHello
