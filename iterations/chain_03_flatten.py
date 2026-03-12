# Write a Python program to build an iterator from nested iterables, flattening them into a single sequence using itertools.chain.
from itertools import chain

l1 = [[1,2], ['Mumbai', 343, 23.34], ('Hitesh', 1937)]

mylist = list(chain.from_iterable(l1))

for item in mylist:
    print(item)

