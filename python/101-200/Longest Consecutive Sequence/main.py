from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(nums)
        curr_seq = 1
        max_seq = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr_seq += 1
            else:
                if nums[i] == nums[i - 1]:
                    continue
                else:
                    max_seq = max(curr_seq, max_seq)
                    curr_seq = 1
        
        return max(curr_seq, max_seq)