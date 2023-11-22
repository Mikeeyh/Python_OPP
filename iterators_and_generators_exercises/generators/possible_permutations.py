import itertools


def possible_permutations(ls):
    if len(ls) <= 1:
        yield ls
    else:
        for i in range(0, len(ls)):
            for permutation in possible_permutations(ls[:i] + ls[i + 1:]):  # recursion of our function
                yield [ls[i]] + permutation


# def possible_permutations(ls):
#     for permutation in itertools.permutations(ls):
#         yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
