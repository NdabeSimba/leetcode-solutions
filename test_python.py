class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle) if needle in haystack else -1


self = Solution()
haystack = "sadbutsad" 
needle = "sad"
print(Solution.strStr(self, haystack, needle))

haystack = "leetcode" 
needle = "leeto"
print(Solution.strStr(self, haystack, needle))