#!/usr/local/bin/python3

# basic search
arr1 = [1,2,3,5,6]
def lookup(arr, k):
    if k in arr:
        return True
    return False

print(lookup(arr1,11))

# 2nd method
def seq_search(arr, k):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == k:
            found = True
        else:
            pos += 1
    return found

print(lookup(arr1, 5))

# 3rd method

def seq_search_sorted(arr, k):
    '''
    Input array must be sorted
    '''
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == k:
            found = True
        else:
            if arr[pos] > k:
                stopped = True
            else:
                pos += 1
    return found

print(lookup(arr1, 5))