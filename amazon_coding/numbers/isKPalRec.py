#!/usr/local/bin/python3
def isKPalRec(str1, str2, m, n):
	if not m: return n
	if not n: return m 
	if str1[m-1] == str2[n-1]: 
		return isKPalRec(str1, str2, m-1, n-1) 
	res = 1 + min(isKPalRec(str1, str2, m-1, n),
				(isKPalRec(str1, str2, m, n-1)))
    # if res: 
    #     return true 
    # else:
    #     return False
	return res 
# Returns true if str is k palindrome. 
def kpalindrome(string, k): 
	revStr = string[::-1] 
	l = len(string) 

	return (isKPalRec(string, revStr, l, l) <= k * 2) 