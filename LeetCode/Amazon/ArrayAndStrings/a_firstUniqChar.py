
def firstUniqChar(str1):
    unique = {}
    for char in str1:
        if char in unique:
            unique[char] +=1
        else:
            unique[char] = 1
    for k,v in unique.items():
        if v == 1:
            return str1.find(k)
    return -1


import collections
from collections import Counter
def firstUniqChar_v2(s):
    """
    :type s: str
    :rtype: int
    """
    # build hash map : character and how often it appears
    count = collections.Counter(s)
    print(count)
    
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1
print(firstUniqChar_v2('abaAcbd'))