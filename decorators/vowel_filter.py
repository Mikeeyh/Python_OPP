def vowel_filter(function):
    def wrapper():
        result = function()  # this returns ["a", "b", "c", "d", "e"], the function get_letters
        vowels = [char for char in result if char.lower() in 'aeouyi']
        return vowels  # we called wrapper() in order to return filtrated result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
