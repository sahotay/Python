#!/usr/local/bin/python3
def uniqueChar(s):
    occurance = {}
    for char in s:
        if char in occurance.keys():
            occurance[char] +=1
        else:
            occurance[char] =1
    for k, v in occurance.items():
        if v == 1:
            return k

print(uniqueChar("abbaccfb"))

def uniqueCharV2(s):
    return len(set(s)) == len(s)
print(uniqueCharV2("abbaccfb"))

def uniqueCharV3(s):
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True
print(uniqueCharV3("abbaccfb"))

print(uniqueCharV2("abbaccfb"))