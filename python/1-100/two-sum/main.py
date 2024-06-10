
"""
# nums = [2, 7, 11, 15] and target = 9

First iteration (i = 0, num = 2):
    num (2) is not in hashmap.
    Calculate counterpart: 9 - 2 = 7.
    Store counterpart in hashmap: hashmap = {7: 0}.

Second iteration (i = 1, num = 7):
    num (7) is in hashmap.
    Return the indices: [hashmap[7], 1] which is [0, 1].
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i, num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], i]
            else:
                hashmap[target - num] = i
