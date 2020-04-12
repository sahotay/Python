#!/usr/local/bin/python3
'''
For n = 4 and k = 2, the output should be

climbingStaircase(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
There are 4 steps in the staircase, and you can jump up 2 or fewer steps at a time. There are 5 potential sequences in which you jump up the stairs either 2 or 1 at a time.
'''

def climbingStaircase(n, k):
    if n < 0: return []
    if n == 0: return [[]]
    ans = []
    for i in range(1, k+1):
        for seq in climbingStaircase(n-i, k):
            ans.append([i] + seq)
    return ans
