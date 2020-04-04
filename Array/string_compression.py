#!/usr/local/bin/python3
# AAAAABBBBBBBCCaaaa -> A5B7C2a4
def stringCompression(s):
    r = ""
    l = len(s)

    #edge case #1
    if l == 0:
        return ""
    #edge case #2
    if l == 1:
        return (f"{s}+1")
    count = 1
    i = 1
    while i < l:
        if s[i] == s[i-1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
            count = 1
        i += 1
    return (r + s[i-1] + str(count))

print(stringCompression('AABaabbbAAA'))