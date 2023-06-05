class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c not in hashmap: # open-bracket
                stack.append(c)
            elif not stack or stack[-1] != hashmap[c]: # stack empty or mismatch of end-bracket
                return False
            else:
                stack.pop() # we have end-bracket that matched open-bracket
                
        return not stack
    
self = Solution()

s = "()[]{}"
print(Solution.isValid(self, s))

s = "(]"
print(Solution.isValid(self, s))

s = "([)]"
print(Solution.isValid(self, s))

s = "()[]()(){()()()}()"
print(Solution.isValid(self, s))