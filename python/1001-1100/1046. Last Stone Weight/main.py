from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, val in enumerate(stones):
            stones[i] = -val

        heapify(stones)

        while stones:
            first = -heappop(stones)
            if not stones:
                return first

            second = -heappop(stones)

            if first > second:
                heappush(stones, -(first - second))
        
        return 0