import itertools

array = [[1,1,1,1,0,0,0,0,0,0],
[0,1,0,0,1,0,0,1,0,1],
[0,0,0,0,0,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1],
[1,0,1,1,1,1,1,1,1,1]]

def jaccardDistance(x, y):
    inter = 0
    union = 0
    for i in range(0, len(x)):
        if(x[i]!=0 or y[i]!=0):
            union += 1
            if(x[i]==y[i]):
                inter += 1
    return 1-(float(inter)/float(union))

for i in itertools.combinations(range(0,5), 2):
    print((i, jaccardDistance(array[i[0]], array[i[1]])))