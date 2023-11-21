def squares(n):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1


print(list(squares(5)))


def squares(n):
    for i in range(1, n + 1):
        yield i ** 2


print(list(squares(5)))

# Using iterator:

# class squares:
#     def __init__(self, n: int):
#         self.n = n
#         self.start_index = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start_index > self.n:
#             raise StopIteration()
#         result = self.start_index ** 2
#         self.start_index += 1
#         return result
