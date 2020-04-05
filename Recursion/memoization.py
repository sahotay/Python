#!/usr/local/bin/python3
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            return self.memo[args]

def factorial(k):
    if k < 2:
        return 1
    return k * factorial(k - 1)

factorial = Memoize(factorial)
print(factorial(9,8))