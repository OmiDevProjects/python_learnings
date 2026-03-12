# Write a Python program to create an iterator that chains together multiple iterables of different types and then filters out all non-integer elements.
from itertools import chain

def chainFunc(l1, l2, l3):
    return chain(l1, l2, l3)

l1 = [1, 2, 3, 4, 5]
l2 = ['Mumbai', 'Japan', 'Australia']
l3 = ('782', 'Jaipur', 23, 3, 4)

chain_obj = chainFunc(l1, l2, l3)
filter_item = []

for item in chain_obj:
    if type(item) == str:
        filter_item.append(item)

print(filter_item)
