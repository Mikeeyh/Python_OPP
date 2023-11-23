def even_numbers(function):
    def wrapper(nums):
        even_nums = [num for num in nums if num % 2 == 0]
        return even_nums
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))

# OR:


def even_numbers(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        even_nums = [num for num in result if num % 2 == 0]
        return even_nums
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


@even_numbers
def get_multiple_numbers(a, b, c):
    return [a, b, c]


print(get_numbers([1, 2, 3, 4, 5]))
print(get_multiple_numbers(1, 2, 3))
