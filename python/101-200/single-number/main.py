from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        u=[]
        for i in nums:
            if i not in u:
                u.append(i)
        for i in u:
            if nums.count(i)==1:
                return i
        return -1