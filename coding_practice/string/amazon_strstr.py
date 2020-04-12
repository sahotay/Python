#!/usr/local/bin/python3
'''
Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

Example

For s = "CodefightsIsAwesome" and x = "IA", the output should be
strstr(s, x) = -1;
For s = "CodefightsIsAwesome" and x = "IsA", the output should be
strstr(s, x) = 10.
'''
def findFirstSubstringOccurrence(s, x):

    ''' Find the first occurrances of @patt in @text
    '''
    patt = x
    text = s
    if not patt or not text: 
        return -1

    # First build the pattern lookup table
    tbl = [0] * (1 + len(patt))
    i = 1; j = 0
    while i < len(patt):
        if patt[i] == patt[j]:
            i += 1; j += 1; tbl[i] = j
        elif 0 == j:
            i += 1
        else:
            j = tbl[j]
    
    # Search over the query text
    i = 0; j = 0
    while i < len(text):
        if text[i] == patt[j]:
            i += 1; j += 1
            if len(patt) == j:
                assert(text[i - len(patt): i] == patt)
                return i - len(patt)
        elif j == 0:
            i += 1
        else:
            j = tbl[j]

    return -1

# def findFirstSubstringOccurrence(s, x):
#     try:
#         return s.index(x)
#     except:
#         return -1

s = "CodefightsIsAwesome"
x = "ISA"
print(findFirstSubstringOccurrence(s,x))