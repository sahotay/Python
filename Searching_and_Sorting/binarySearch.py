#!/usr/local/bin/python3
# uses Divide and conquer!
arr = [1,2,3,4,5]
def binarySearch(arr, k):
    first = 0
    last = len(arr) -1
    found = False
    while first <= last and not found:
        mid = (first+last)//2
        if arr[mid] == k:
            found = True
        else:
            if k < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
        

print(binarySearch(arr,9))

def recursiveBinarySearch(arr, k):
    # Base Check
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        # If match found
        if arr[mid]==k:
            return True
        else:
            if k < arr[mid]:
                return recursiveBinarySearch(arr[:mid], k)
            else:
                return recursiveBinarySearch(arr[mid+1:], k)
            

print(recursiveBinarySearch(arr,3))