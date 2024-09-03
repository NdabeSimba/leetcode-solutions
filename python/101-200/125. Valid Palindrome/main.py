class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alpNum(s[left]):
                left += 1
            while left < right and not self.alpNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def alpNum(self, ch):
        return (
            ord("A") <= ord(ch) <= ord("Z")
            or ord("a") <= ord(ch) <= ord("z")
            or ord("0") <= ord(ch) <= ord("9")
        )
