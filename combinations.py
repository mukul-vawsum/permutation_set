import itertools

a = [1,2,3,4]
for i in xrange(0,len(a)+1):
   print list(itertools.combinations(a,i))
