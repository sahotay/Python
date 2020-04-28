'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = values.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
s = Solution()
print(s.romanToInt("MCMXCIV"))

'''
Approach 3: Right-to-Left Pass
Intuition

This approach is a more elegant variant of Approach 1. Just to be clear though, Approach 1 and Approach 2 are probably sufficient for an interview. This approach is still well worth understanding though.

In the "subtraction" cases, such as XC, we've been updating our running sum as follows:

sum += value(C) - value(X)
However, notice that this is mathematically equivalent to the following:

sum += value(C)
sum -= value(X)
Utilizing this means that we can process one symbol each time we go around the main loop. We still need to determine whether or not our current symbol should be added or subtracted by looking at the neighbour though.

In Approach 1, we had to be careful when inspecting the next symbol to not go over the end of the string. This check wasn't difficult to do, but it increased the code complexity a bit, and it turns out we can avoid it with this approach!

Observe the following:

Without looking at the next symbol, we don't know whether or not the left-most symbol should be added or subtracted.
The right-most symbol is always added. It is either by itself, or the additive part of a pair.
So, what we can do is initialise sum to be the value of the right-most (last) symbol. Then, we work backwards through the string, starting from the second-to-last-symbol. We check the symbol after (i + 1) to determine whether the current symbol should be "added" or "subtracted".

last = s.length - 1
total = value(last)
`
for i from last - 1 down to 0:
    if value(s[i]) < value(s[i+1]):
        total -= value(s[i])
    else:
        total += value(s[i])
return sum
Because we're starting at the second-to-last-index, we know that index i + 1 always exists. We no longer need to handle its potential non-existence as a special case, and additionally we're able to (cleanly) use a for loop, as we're always moving along by 1 index at at time, unlike before where it could have been 1 or 2.
'''