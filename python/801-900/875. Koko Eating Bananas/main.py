from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if sum(ceil(i/mid) for i in piles) <= h:
                right = mid
            else:
                left = mid + 1
        
        return left