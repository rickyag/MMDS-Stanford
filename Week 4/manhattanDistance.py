import itertools

array = [[1,1,1,1,0,0,0,0,0,0],
[0,1,0,0,1,0,0,1,0,1],
[0,0,0,0,0,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1],
[1,0,1,1,1,1,1,1,1,1]]

def manhattanDistance(x, y):
    distance = 0
    for i in range(0, len(x)):
        if(x[i]!=y[i]):
            distance += 1

    return distance

for i in itertools.combinations(range(0, len(array)), 2):
    print((i, manhattanDistance(array[i[0]], array[i[1]])))