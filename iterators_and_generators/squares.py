class squares:
    def __init__(self, n: int):
        self.n = n
        self.start_index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index > self.n:
            raise StopIteration()
        result = self.start_index ** 2
        self.start_index += 1
        return result


print(list(squares(5)))
