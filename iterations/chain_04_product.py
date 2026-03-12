# Creates all possible combinations between elements of iterables.

from itertools import product

a = [1,2,3]
b = ['mumbai', 'aakash', 72]

combinations = list(product(a, b))
print(combinations)