def anagram_check_v1(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    return sorted(s1) == sorted(s2)

print(anagram_check_v1('d o g', 'g od'))
print(anagram_check_v1('clint eastwood', 'old west action'))
print(anagram_check_v1('abc', 'zxy'))

def anagram_check_v2(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    #Edge Case check
    if len(s1) != len(s2):
        return False
    
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = -1
    for k in count:
        if count[k] != 0:
            return False
    return True

print(anagram_check_v2('d o g', 'g od'))

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""

from itertools import groupby 
def groupAnagrams(strs):
    temp = lambda strs: sorted(strs)
    res = [list(val) for key, val in groupby(sorted(strs, key = temp), temp)] 
    return str(res)

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))



def groupAnagrams_1(strs):
    result = {}
    for i in strs:
        x = "".join(sorted(i))
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]
    return list(result.values())
print(groupAnagrams_1(strs))