def rotateImage(a):
    return list(zip(*a[::-1]))

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotateImage(a))

rotateImage = lambda a: zip(*a[::-1])
print(rotateImage(a))

def rotateImage_1(a):
    if not a or a == [[]]:
        return [[]]
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
print(rotateImage_1(a))