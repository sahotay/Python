#!/usr/local/bin/python3
def firstNotRepeatingCharacter(str):
    unique = {}
    for char in str:
        if char in unique:
            unique[char] +=1
        else:
            unique[char] = 1
    for k,v in unique.items():
        if v == 1:
            return k
    return "_"

print(firstNotRepeatingCharacter('abacabad'))

def firstNotRepeatingCharacter_v2(str):
    newstr=str.lower()
    for char in newstr:
        if newstr.index(char) == newstr.rindex(char):
            return char
    return '_'
print(firstNotRepeatingCharacter('abaAcbd'))