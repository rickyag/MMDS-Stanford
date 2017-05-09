import numpy as np
array = np.array([[0,1,1,0],
                  [1,0,1,1],
                  [0,1,0,1],
                  [0,0,1,0],
                  [1,0,1,0],
                  [0,1,0,0]])

order = [3,5,0,2,4,1]

result = [0, 0, 0, 0]
for i in order:
    for j in range(0, len(array[i])):
        if(result[j]==0 and array[i][j]==1):
            result[j] = i+1

print(result)
