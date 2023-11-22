def fibonacci():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num


# OR:


def fibonacci():
    current_num, next_num = 0, 1
    while True:
        yield current_num
        current_num, next_num = next_num, current_num + next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
