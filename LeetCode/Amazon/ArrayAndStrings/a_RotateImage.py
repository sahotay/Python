'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

matrix = [[7,4,1], [8,5,2], [9,6,3]]
def rotateImage_v1(a):
    if not a or a == [[]]:
        return [[]]
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

print(rotateImage_v1(matrix))

"""
The obvious idea would be to transpose the matrix first and then reverse each row. 
This simple approach already demonstrates the best possible time complexity O(N^2).
"""
def rotateImage_v2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0]) 
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
    
    # reverse each row
    for i in range(n):
        matrix[i].reverse()
    return matrix

print(rotateImage_v2(matrix))


"""
Approach 2 : Rotate four rectangles
Intuition

Approach 1 makes two passes through the matrix, though it's possible to make a rotation in one pass.

To figure out how let's check how each element in the angle moves during the rotation.
That gives us an idea to split a given matrix in four rectangles and reduce the initial problem to the rotation of these rectangles.

"""
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = [0] * 4
            row, col = i, j
            # store 4 elements in tmp
            for k in range(4):
                tmp[k] = matrix[row][col]
                row, col = col, n - 1 - row
            # rotate 4 elements   
            for k in range(4):
                matrix[row][col] = tmp[(k - 1) % 4]
                row, col = col, n - 1 - row

"""
Approach 3 : Rotate four rectangles in one single loop
The idea is the same as in the approach 2, but everything is done in one single loop and hence it's a way more elegant (kudos go to @gxldragon).
"""


def rotate_v3(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])        
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp