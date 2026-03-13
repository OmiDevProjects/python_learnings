# Power Function

x = 34

def power(num):
    def actual_solve(x):
        return x ** num
    return actual_solve

square = power(2)
cube = power(3)
print(square(3))
print(cube(3))

# print(power(2)(3))
# print(power(3)(3))



# Write a function outer(x) that returns another function inner(y) which returns the sum of x and y.
x = 10
def outer(num):
    def inner(y):
        return num + y
    return inner
another_value = outer(x)
print(another_value(5))