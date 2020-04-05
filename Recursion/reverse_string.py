#!/usr/local/bin/python3
def reverse(s):
    # Base Case
    if len(s) <= 1:
        return s
    # Recursion Case
    return (reverse(s[1:]) + s[0])

print(reverse('string'))