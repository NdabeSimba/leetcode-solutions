import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


self = KthLargest(3, [4, 5, 8, 2])
print(KthLargest.add(self, 3))  # return 4
print(KthLargest.add(self, 5))  # return 5
print(KthLargest.add(self, 10))  # return 5
print(KthLargest.add(self, 9))  # return 8
print(KthLargest.add(self, 4))  # return 8
