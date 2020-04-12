#!/usr/local/bin/python3

'''
For s = 12 and arr = [1, 2, 3, 7, 5], the output should be
findLongestSubarrayBySum(s, arr) = [2, 4].

The sum of elements from the 2nd position to the 4th position (1-based) is equal to 12: 2 + 3 + 7.

For s = 15 and arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be
findLongestSubarrayBySum(s, arr) = [1, 5].

The sum of elements from the 1st position to the 5th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5.

For s = 15 and arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], the output should be
findLongestSubarrayBySum(s, arr) = [1, 8].

The sum of elements from the 1st position to the 8th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5 + 0 + 0 + 0.
'''
def findLongestSubarrayBySum(s, a):
    total = j = 0
    res = (0,-1)
    for i,v in enumerate(a):
        total += v
        while j<=i and total>s:
            total -= a[j]
            j += 1
        if (total == s) and (res[1]-res[0]<i-j):
            res=(j+1,i+1)
    return res if res[0] else [-1]

s = 12
arr = [1, 2, 3, 7, 5]
print(findLongestSubarrayBySum(s, arr))