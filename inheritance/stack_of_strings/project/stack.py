class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        if not isinstance(element, str):
            raise ValueError("Element is not a string, please add only strings")
        self.data.append(element)

    def is_empty(self):
        return len(self.data) == 0
        # return any(self.data)

    def pop(self):
        if not self.is_empty():
            element = self.data.pop()
            return element

    def top(self):
        if not self.is_empty():
            return self.data[-1]

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f'[{", ".join(reversed_data)}]'
