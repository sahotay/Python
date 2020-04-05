#!/usr/local/bin/python3
#0,1,1,2,3,5,8,13

def fib_rec(n):
    if n == 0 or n ==1:
        return n
    return(fib_rec(n-1) + fib_rec(n-2))
print(fib_rec(3))

# Dynamic Programming (using memoization)
n = 10
cache = [None] * (n+1)
def fib_dyn(n):
    # Base case
    if n == 0 or n ==1:
        return n
    
    # check cache
    if cache[n] != None:
        return cache[n]

    #keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]

print(fib_dyn(10))

# Iterrative
def fib_iter(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
print(fib_iter(10))