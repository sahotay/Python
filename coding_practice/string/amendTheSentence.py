#!/usr/local/bin/python3
'''
You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.
Example

For s = "CodesignalIsAwesome", the output should be
amendTheSentence(s) = "codesignal is awesome";
For s = "Hello", the output should be
amendTheSentence(s) = "hello".
'''

def amendTheSentence(s):

    sentence = ""
    for i,c in enumerate(s):
        if c.isupper():
            if i!=0:
                sentence+=" "+c.lower()
            else:
                sentence+=c.lower()                  
        else:
            sentence+=c            
    return sentence

s = "CodesignalIsAwesome"
print(amendTheSentence(s))

import re
def amendTheSentence_v2(s):
    return " ".join(re.findall(r"[A-Za-z][a-z]*", s)).lower()
print(amendTheSentence_v2(s))
