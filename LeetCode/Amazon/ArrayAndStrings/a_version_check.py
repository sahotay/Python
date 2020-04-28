'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

 

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
Example 4:


'''

def compareVersion(version1, version2):
    nums1 = version1.split('.')
    nums2 = version2.split('.')
    n1, n2 = len(nums1), len(nums2)
    
    # compare versions
    for i in range(max(n1, n2)):
        i1 = int(nums1[i]) if i < n1 else 0
        i2 = int(nums2[i]) if i < n2 else 0
        if i1 != i2:
            return 1 if i1 > i2 else -1
    # the versions are equal
    return 0 

version1 = "1.0"
version2 = "1.0.0"
print(compareVersion(version1,version2))