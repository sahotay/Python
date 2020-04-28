'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} 
        maximum_length = 0

        # starting the inital point of window to index 0 
        start = 0 

        for end in range(len(s)): 

            # Checking if we have already seen the element or not 
            if s[end] in seen:
                # If we have seen the number, move the start pointer 
                # to position after the last occurrence 
                start = max(start, seen[s[end]] + 1) 

            # Updating the last seen value of the character 
            seen[s[end]] = end 
            maximum_length = max(maximum_length, end-start+1) 
        return maximum_length

def main():
    s = Solution()
    print(f'The length of the longest non-repeating character substring is: {s.lengthOfLongestSubstring("bbbbb")}')
    
if __name__ =='__main__':
    main()