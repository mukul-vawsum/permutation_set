from itertools import permutations
perm = permutations([1, 2, 3], 2)
for i in list(perm):
	print i

# Now this will result in the required output!
# Expected Answer->(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)
