#!/usr/local/bin/python3
'''
Problem Statement¶
Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'
'''
def stringPermutation(s):
    lists = []
    # Base Case
    if len(s) == 1:
        lists = [s]
    for i, char in enumerate(s):
        for perm in stringPermutation(s[:i] + s[i+1:]):
            lists += [char + perm]
    return lists
    
print(stringPermutation('abc'))