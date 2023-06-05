class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x[::-1] == str(x)

x = 111
self = Solution()
print(Solution.isPalindrome(self,x))