#!/usr/local/bin/python3
'''
Given an array of integers a and an integer sum, find all of the unique combinations in a that add up to sum.
The same number from a can be used an unlimited number of times in a combination.
Elements in a combination (a1 a2 … ak) must be sorted in non-descending order, while the combinations themselves must be sorted in ascending order.
If there are no possible combinations that add up to sum, the output should be the string "Empty".

Example

For a = [2, 3, 5, 9] and sum = 9, the output should be
combinationSum(a, sum) = "(2 2 2 3)(2 2 5)(3 3 3)(9)".
'''
def combinationSum(a, s):
    arr = sorted(set(a))
    ans = list(comb_recur([], arr, s))
    ans.sort()
    if len(ans) == 0:
        return 'Empty'
    else:
        return '({})'.format(')('.join(' '.join(map(str, row)) for row in ans))

def comb_recur(pref, arr, s):
    for i, val in enumerate(arr):
        if val == s:
            yield pref + [val]
        elif val < s:
            yield from comb_recur(pref + [val], arr[i:], s-val)
        elif val > s:
            break
