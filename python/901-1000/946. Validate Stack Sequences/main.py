from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return not stack


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        for num in pushed:
            pushed[i] = num
            while i >= 0 and pushed[i] == popped[j]:
                i -= 1
                j += 1
            i += 1
        return i == 0
