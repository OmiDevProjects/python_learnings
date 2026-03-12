#TODO: Write a Python program to create an iterator from several iterables in a sequence and display the type and elements of the new iterator.

from itertools import chain

def chainFunc(l1, l2, l3):
    return chain(l1, l2, l3)

# Lists
l1 = [1, 2, 3, 4, 5]
l2 = [10, 12, 13, 15, 16]
l3 = [22, 34, 54, 27, 89]


chain_obj = chainFunc(l1, l2, l3)
print(type(chain_obj))

for item in chain_obj:
    print(item)

# Tuple
l1_t = (1, 2, 3, 4, 5)
l2_t = (10, 12, 13, 15, 16)
l3_t = (22, 34, 54, 27, 89)

chain_obj = chainFunc(l1_t, l2_t, l3_t)
print(type(chain_obj))

for item in chain_obj:
    print(item)