from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i, val in enumerate(nums):
            nums[i] = -val

        heapq.heapify(nums)
        print(nums)

        for _ in range(1, k):
            heapq.heappop(nums)
        
        return -nums[0]
        
