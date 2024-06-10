class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

self = Solution()

haystack = "sadbutsad"; needle = "sad"
print(Solution.strStr(self, haystack, needle))

haystack = "leetcode"; needle = "leeto"
print(Solution.strStr(self, haystack, needle))