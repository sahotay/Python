#!/usr/local/bin/python3
# Dynamic programming Python implementation of LIS problem
# lis returns length of the longest increasing subsequence 
# in arr of size n 
def longestIncreasingSubsequence(sequence): 
	n = len(sequence) 
	# Declare the list (array) for LIS and initialize LIS 
	# values for all indexes 
	lis = [1]*n 
	# Compute optimized LIS values in bottom up manner 
	for i in range (1, n): 
		for j in range(0, i): 
			if sequence[i] > sequence[j] and lis[i]< lis[j] + 1 : 
				lis[i] = lis[j]+1
	# Initialize maximum to 0 to get the maximum of all 
	# LIS 
	maximum = 0
	# Pick maximum of all LIS values 
	for i in range(n): 
		maximum = max(maximum, lis[i]) 

	return maximum

# Driver program to test above function 
sequence = [10, 22, 9, 33, 21, 50, 41, 60] 
print("Length of lis is", longestIncreasingSubsequence(sequence) )
# This code is contributed by Nikhil Kumar Singh 

## method2
def longestIncreasingSubsequence_v2(a):
    from bisect import bisect_left as f
    s = []
    for i in a:
        t = f(s,i)
        if t >= len(s):
            s.append(i)
        else:
            s[t] = i
    return len(s)