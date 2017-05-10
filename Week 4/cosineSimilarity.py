import math
u = [1, 0.25, 0, 0, 0.5, 0]
v = [0.75, 0, 0, 0.2, 0.4, 0]
w = [0, 0.1, 0.75, 0, 0, 1]

def cosineSimilarity(x, y):
    product = 0.0
    length_x = 0.0
    length_y = 0.0
    for i in range(0, len(x)):
        product += x[i]*y[i]
        length_x += x[i]**2
        length_y += y[i]**2

    length = (length_x**0.5) * (length_y**0.5)

    return (product/length)

print(cosineSimilarity([0,0,0,1,1], [1,0,0,1,1]))
print(cosineSimilarity(u, w))
print(cosineSimilarity(v, w))
print(cosineSimilarity(u, v))