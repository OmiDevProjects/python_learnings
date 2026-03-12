# Write a Python program that generates the running product of elements in an iterable.
from itertools import accumulate
import operator

l1 = [1, 2, 3, 4, 5]

print(list(accumulate(l1, operator.mul)))
print(list(accumulate(l1)))
print(list(accumulate(l1, max)))