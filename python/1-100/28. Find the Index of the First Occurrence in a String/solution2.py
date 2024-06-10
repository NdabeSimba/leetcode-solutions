# Two pointers

# Time complexity: O(n*m)
# Space complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if all(haystack[i + j] == needle[j] for j in range(len(needle))):
                return i
        return -1
    
self = Solution()
haystack = "sadbutsad" 
needle = "sad"
print(Solution.strStr(self, haystack, needle))

haystack = "leetcode" 
needle = "leeto"
print(Solution.strStr(self, haystack, needle))