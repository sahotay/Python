#!/usr/local/bin/python3
'''
Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.
For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.
'''
# https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/


import heapq

def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        """
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

arr= [1, 23, 12, 9, 30, 2, 50]
k = 3
print(findKthLargest(arr, k))
print(arr)
