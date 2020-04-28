#!/usr/local/bin/python3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def rotateImage_clockwise(a):
    if not a or a == [[]]:
        return [[]]
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
print(rotateImage_clockwise(a))

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def rotateImage_counter_clockwise(a):
    if not a or a == [[]]:
        return [[]]
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    a.reverse()
    return a
print(rotateImage_counter_clockwise(a))