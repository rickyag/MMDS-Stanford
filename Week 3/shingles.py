import numpy as np
import itertools

def shingles(string, shingleLength):
    return set([string[i:i+shingleLength] for i in range(len(string) - shingleLength + 1) if i < len(string) - shingleLength + 1])

def commonShingles(set1, set2):
    return set.intersection(set1, set2)

def JaccardSimilarity(set1, set2):
    return len(commonShingles(set1, set2))/len(set.union(set1, set2))


set1 = shingles('ABRACADABRA', 2)
set2 = shingles('BRICABRAC', 2)
print(set1, len(set1))

print(set2, len(set2))

print(commonShingles(set1, set2), len(commonShingles(set1, set2)))

print(set.union(set1, set2), len(set.union(set1, set2)))
print(JaccardSimilarity(set1, set2))

array = np.array([[0,1,1,0],
                  [1,0,1,1],
                  [0,1,0,1],
                  [0,0,1,0],
                  [1,0,1,0],
                  [0,1,0,0]])

m, n = array.shape

result = []
for i in itertools.combinations(list(range(0,n)), 2):
    union = 0
    inter = 0
    for j in range(0, m):
        if(array[j,[i[0]]] + array[j,[i[1]]] == 2):
            union+=1
            inter+=1
        elif(array[j,[i[0]]] + array[j,[i[1]]] >= 1):
            union+=1
    result.append((i, inter, union))

print result