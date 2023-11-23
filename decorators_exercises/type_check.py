def type_check(expected_type):
    def decorator(func):
        def wrapper(given_type):
            if not isinstance(given_type, expected_type):
                return "Bad Type"
            return func(given_type)
        return wrapper
    return decorator

    #     def wrapper(*args):
    #         if all(isinstance(arg, expected_type) for arg in args):
    #             return func(*args)
    #         return "Bad Type"
    #     return wrapper
    # return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
