class Solution:

    def validPalindrome(self, s: str) -> bool:

        def is_palindrome_range(skips, left, right):
            if skips > 1:
                return False

            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    skips += 1
                    check_left = is_palindrome_range(skips, left + 1, right)
                    check_right = is_palindrome_range(skips, left, right - 1)
                    return check_left or check_right

            return True

        return is_palindrome_range(0, 0, len(s) - 1)
