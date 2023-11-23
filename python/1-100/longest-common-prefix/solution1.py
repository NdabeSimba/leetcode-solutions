class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        exam = list(strs[0])
        ans = ''
        for i in range(len(strs)):
            for j in range(len(exam)):
                if exam[j] != strs[i][j]:
                    exam[j] = ""
                else:
                    continue
        for i in range(len(exam)):
            if exam[i] != "":
                ans += exam[i]
            else:
                break
        return ans
    
strs = ["flower","flow","flight"]
self = Solution()
print(Solution.longestCommonPrefix(self, strs))

strs = ["dog","racecar","car"]
self = Solution()
print(Solution.longestCommonPrefix(self, strs))

strs = ["cir","car"]
self = Solution()
print(Solution.longestCommonPrefix(self, strs))