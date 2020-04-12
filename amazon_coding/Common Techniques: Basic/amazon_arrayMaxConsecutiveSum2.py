#!/usr/local/bin/python3
'''
For inputArray = [-2, 2, 5, -11, 6], the output should be
arrayMaxConsecutiveSum2(inputArray) = 7.

The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.
'''
def arrayMaxConsecutiveSum2(inputArray):
    maxsum = inputArray[0]
    l = len(inputArray)
    cumsum = inputArray[0]
    for i in range(1, l):
        cumsum += inputArray[i]
        if inputArray[i] > cumsum:
            cumsum = inputArray[i]
        maxsum = max(maxsum, cumsum)
    return maxsum


inputArray = [-2, 2, 5, -11, 6]
print(arrayMaxConsecutiveSum2(inputArray))