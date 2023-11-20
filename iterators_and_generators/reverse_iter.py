class reverse_iter:
    def __init__(self, iterable: list):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.iterable[self.index]
        raise StopIteration

# OR:


class reverse_iter:
    def __init__(self, iterable: list):
        self.iterable = iterable
        self.current_index = len(iterable) - 1
        self.end_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index -= 1
        return self.iterable[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
