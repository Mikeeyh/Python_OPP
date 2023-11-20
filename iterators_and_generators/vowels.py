class vowels:
    def __init__(self, txt):
        self.txt = txt
        self.start_index = 0
        self.end_index = len(self.txt)

    def __iter__(self):
        return self

    def __next__(self):
        vowels_letters = "aeiou"

        while True:
            if self.start_index >= self.end_index:
                raise StopIteration()

            index = self.start_index
            self.start_index += 1
            if self.txt[index].lower() in vowels_letters:
                return self.txt[index]


# OR:


class vowels:
    def __init__(self, txt):
        self.txt = txt
        vowels_letters = "aeiou"
        self.found_vowels = [char for char in self.txt if char.lower() in vowels_letters]
        self.start_index = 0
        self.end_index = len(self.found_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index > self.end_index:
            raise StopIteration()
        index = self.start_index
        self.start_index += 1
        return self.found_vowels[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

