#!/usr/local/bin/python3
def reverseWord(s):
    # return ' '.join(reversed(s.split())) ## Method 1
    return ' '.join(s.split()[::-1])

print (reverseWord("This is the best"))

#manual split  (Method 2)

def reverseWordV2(s):
    words = []
    length = len(s)
    spaces = [' ']
    counter = 0
    while counter < length:
        if s[counter] not in spaces:
            word_start = counter
            while counter < length and s[counter] not in spaces:
                counter += 1
            words.append(s[word_start:counter])
        counter += 1
    return ' '.join(reversed(words))
print (reverseWordV2("This is the best"))