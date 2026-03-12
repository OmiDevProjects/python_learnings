# Returns unique selections of elements where order doesn't matter.
from itertools import combinations

a = [1,2,3]

print(list(combinations(a, 2)))
