class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            stack = []
            for ch in s:
                if ch == '#' and stack:
                    stack.pop()
                elif ch != '#':
                    stack.append(ch)
            return stack
        
        return backspace(s) == backspace(t)