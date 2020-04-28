def maxScore(s):
    ans,t=0,s.count('1')
    for c in s[:-1]:
        if c=='0':
            t+=1
            ans=max(ans,t)
        else:
            t-=1
            ans=max(ans,t)
    return ans

s = "011101"
print(maxScore(s))