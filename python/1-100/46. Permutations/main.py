from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        result = []

        for p in perms:
            for i in range(len(p) + 1):
                temp_p = p.copy()
                temp_p.insert(i, nums[0])
                result.append(temp_p)

        return result
            