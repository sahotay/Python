'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def twoSum(num, target):
    map = {}
    for each in range(len(num)):
        if num[each] not in map:
            map[target - num[each]] = each
        else:
            return map[num[each]], each
    return "Not Found"

def main():
    nums = [2, 7, 17, 15]
    target = 9
    print(twoSum(nums, target))

if __name__ == '__main__':
    main()