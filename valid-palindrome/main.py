class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""
        for ch in s:
            if 97 <= ord(ch) <= 122 or 48 <= ord(ch) <= 57:
                temp += ch

        for i in range(len(temp) // 2):
            if temp[i] == temp[- i - 1]:
                continue
            else:
                return False

        return True


self = Solution()

s = "A man, a plan, a canal: Panama"
print(Solution.isPalindrome(self, s))

s = "0P"
print(Solution.isPalindrome(self, s))

s = " "
print(Solution.isPalindrome(self, s))
