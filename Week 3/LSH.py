import numpy as np
import itertools

array = np.array([[1, 2, 1, 1, 2, 5, 4],
       [2, 3, 4, 2, 3, 2, 2],
       [3, 1, 2, 3, 1, 3, 2],
       [4, 1, 3, 1, 2, 4, 4],
       [5, 2, 5, 1, 1, 5, 1],
       [6, 1, 6, 4, 1, 1, 4]])

b=3
r=2

result = []
for i in itertools.combinations(list(range(0, array.shape[1])), 2):
    identicalBand = 0
    for j in range(0, b):
        identicalRow = 0
        for k in range(0, r):
            if(array[j*r+k,i[0]] == array[j*r+k,i[1]]):
                identicalRow+=1
        if identicalRow==r:
            identicalBand+=1

    result.append((i, identicalBand))

print result

n=24.0
r=[1,2,3,4,6,8,12,24]

for i in r:
    i = float(i)
    s = (1/(n/i))**(1/i)
    FN = (1-(0.5**i))**(n/i)
    FP = 1-(1-(0.2**i))**(n/i)
    print((i,s,FN,FP, FN+FP))