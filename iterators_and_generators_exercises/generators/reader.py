def read_next(*args):
    iterators = [iter(arg) for arg in args]

    while True:
        result = []
        for iterator in iterators:
            for it in iterator:
                try:
                    result.append(next(it))
                except StopIteration:
                    # If any iterator is exhausted, stop the generator
                    return

        yield tuple(result)


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
