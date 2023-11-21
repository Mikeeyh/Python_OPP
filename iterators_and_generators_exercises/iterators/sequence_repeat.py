class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration()
        element = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        self.number -= 1

        return element


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
