# Returns all possible arrangements.
from itertools import permutations

items = [1, 2, 3]

print(list(permutations(items, 2)))