"""
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

# Intuition

# # A small improvement to the above approach can reduce the time complexity of the algorithm to O(2∗∣filtered_S∣+∣S∣+∣T∣), 
# where filtered_S is the string formed from S by removing all the elements not present in TT.

# This complexity reduction is evident when ∣filtered_S∣<<<∣S∣.

# This kind of scenario might happen when length of string TT is way too small than the length of string SS and string SS consists of numerous characters which are not present in TT.

# Algorithm:

# We create a list called filtered_S which has all the characters from string SS along with their indices in SS, but these characters should be present in TT.

#   S = "ABCDDDDDDEEAFFBC" T = "ABC"
#   filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
#   Here (0, 'A') means in string S character A is at index 0.
# We can now follow our sliding window approach on the smaller string filtered_S.

"""

from collections import Counter 
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1    

        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

print(minWindow("ADOBECODEBANC", "ABC"))