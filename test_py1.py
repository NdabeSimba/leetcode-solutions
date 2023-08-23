class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        temp_ch = s[0]
        temp_list = [e + temp_ch for e in s.split(temp_ch) if e]

        if len(temp_list) == 0:
            return True
        
        temp_word = temp_list.pop()

        print(temp_word)

        while True:
            if temp_word in temp_list:
                if temp_list[0] == temp_word:
                    temp_list.pop()
                else:
                    return False
            else:
                if len(temp_list) == 0:
                    return True
                else:
                    return False
        
        # if temp_list:
        #     print(temp_list)
        #     return False
        # else:
        #     print(temp_list)
        #     return True

self = Solution()

s = "ababab"
print(Solution.repeatedSubstringPattern(self, s))

s = "babbabbabbabbab"
print(Solution.repeatedSubstringPattern(self, s))

s = "aba"
print(Solution.repeatedSubstringPattern(self, s))
