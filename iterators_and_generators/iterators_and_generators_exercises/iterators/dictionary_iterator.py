class dictionary_iter:
    def __init__(self, given_dict: dict):
        self.given_dict = given_dict
        self.index = 0
        self.keys = list(self.given_dict.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration()
        key = self.keys[self.index]
        value = self.given_dict[key]
        self.index += 1
        if isinstance(key, str):
            key = f'"{key}"'
        if isinstance(value, str):
            value = f'"{value}"'
        return f"({key}, {value})"


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
