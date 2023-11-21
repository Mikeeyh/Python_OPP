def genrange(start, end):
    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 10)))
print(tuple(genrange(1, 10)))
print(*(genrange(1, 10)), sep=', ')
