a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)
print(b)
# [1, 2, 3]
# [1, 2, 3, 4]

a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
# [1, 2, 3, 4]
# [1, 2, 3, 4]

x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x

        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x

        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
