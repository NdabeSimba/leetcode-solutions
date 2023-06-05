class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = True
        for i in range(len(str(x))//2):
            if str(x)[i] != str(x)[-i-1]:
                result = False
                break
        return result
    
x = -121
self = Solution()
print(Solution.isPalindrome(self,x))

