def numberOf2sinRange(n):
    s = ""
    for i in range(2,n+1): 
        s+=str(i)
    print(s)
    return(list(s).count('2'))

print(numberOf2sinRange(22))