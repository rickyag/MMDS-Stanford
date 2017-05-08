import numpy as np
from Graph import Graph

# data = Graph({'y': ['y', 'a'], 'a': ['y', 'm'], 'm': ['m']})
# data = Graph({'y': ['y', 'a'], 'a': ['y', 'm'], 'm': ['a']})
# data = Graph({'a': ['b', 'c'], 'b': ['c'], 'c': ['c']})
data = Graph({'a': ['b', 'c'], 'b': ['c'], 'c':['a']})

n = len(data.vertices())
M = np.zeros((n, n))
for i in xrange(0, M.shape[0]):
    for j in xrange(0, M.shape[1]):
        M[j ,i] = data.get_relative_rank(data.vertices()[i], data.vertices()[j])

iteration = 5
beta = 1
count = 0
r = np.ones((n, )) * 1/float(n)
A = beta * M + (1-beta) * (np.ones((n, n)) * 1/float(n))
while count <= iteration:
    print A
    print r
    r = A.dot(r)
    count += 1

print data.vertices()
# print (r[1], r[2] + 0.575*r[0])
# print (r[1], 0.9*r[2] + 0.475*r[0])
# print (0.95 * r[0], 0.9*r[1] + 0.05*r[2])
# print (0.85 * r[0], r[1] + 0.15*r[2])