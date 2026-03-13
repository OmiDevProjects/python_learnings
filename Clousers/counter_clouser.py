# Counter Closure


def make_counter():
    num = 0
    def inner():
        nonlocal num
        num += 1
        return num
    return inner

counter = make_counter()

print(counter())
print(counter())
print(counter())
