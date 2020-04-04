#!/usr/local/bin/python3
arr_1 = [5,5,7,7]
arr_2 = [5,7,7]


def finderM1(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


print(f"Missing number from 'finderM1' function is: {finderM1(arr_1, arr_2)}")


import collections
def finderM2(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1
print(f"Missing number from 'finderM2' function is: {finderM2(arr_1, arr_2)}")

def finderM3(arr1, arr2):
    result = 0
    # Perform an XOR between the number in the arrays
    for num in arr1+arr2:
        result^=num
    return result
print(f"Missing number from 'finderM3' function is: {finderM3(arr_1, arr_2)}")