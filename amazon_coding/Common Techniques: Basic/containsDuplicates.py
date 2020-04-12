#!/usr/local/bin/python3
'''
Example

For a = [1, 2, 3, 1], the output should be
containsDuplicates(a) = true.

There are two 1s in the given array.

For a = [3, 1], the output should be
containsDuplicates(a) = false.

The given array contains no duplicates
'''
def containsDuplicates(a):
    occurance = set()
    for i in range(len(a)):
        if a[i] in occurance:
            return True
        else:
            occurance.add(a[i])
    return False

def containsDuplicates_v2(a):
    return len(set(a)) != len(a)


a = [1, 2, 3, 1]
a = [3, 3]
a = [-1200000005, -1200000005]
print(containsDuplicates(a))
print(containsDuplicates_v2(a))