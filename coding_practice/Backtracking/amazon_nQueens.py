#!/usr/local/bin/python3
'''
In chess, queens can move any number of squares vertically, horizontally, or diagonally. The n-queens puzzle is the problem of placing n queens on an n × n chessboard so that no two queens can attack each other.

Given an integer n, print all possible distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the placement of the n queens, where the solutions are arrays that contain permutations of [1, 2, 3, .. n]. The number in the ith position of the results array indicates that the ith column queen is placed in the row with that number. In your solution, the board configurations should be returned in lexicographical order.

Example

For n = 1, the output should be
nQueens(n) = [[1]];

For n = 4, the output should be

  nQueens(n) = [[2, 4, 1, 3],
                [3, 1, 4, 2]]
'''
def nQueens(n):

    s = [[x] for x in range(1,n+1)]
    r = []
    
    def validMoves(sol):
        col = len(sol) + 1
        moves = [x for x in range(1,n+1) if x not in sol]
        for i,x in enumerate(sol):
            s1 = x + (col - (i+1))
            s2 = x - (col - (i+1))
            if s1 in moves:
                moves.remove(s1) 
            if s2 in moves:
                moves.remove(s2)
        return moves
        
    
    while s:
        c = s.pop()
        
        if len(c) == n:
            r.append(c)
        
        for i in validMoves(c):
            # check if spot is valid
            s.append(c+[i])
    
    return r[::-1]