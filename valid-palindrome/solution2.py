class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


self = Solution()

s = "A man, a plan, a canal: Panama"
print(Solution.isPalindrome(self, s))

s = "0P"
print(Solution.isPalindrome(self, s))

s = " "
print(Solution.isPalindrome(self, s))
