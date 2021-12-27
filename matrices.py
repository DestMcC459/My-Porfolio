#datastructures

#list comprehension 
combs = []
for x in [2,5,6]: 
    for y in [3,5,7]: 
        if x != y:
            combs.append((x,y))

print(combs)

gon = [3, -2, 2, 7, 9, -1, -3]
print(gon)


matrix = [
    [1, 2, 3, 4],
    [5, 3, 5, 6],
    [9, 10, 8, 12]
]

matrix2 = [
    [2, 4, 7, 0],
    [4, 3, 2, 7],
    [2, 6, 3, 2]
]
print(matrix, matrix2)
import numpy as np
a = np.array([2, 4, 7])
b = np.array([2, 6, 9])
a * b 

