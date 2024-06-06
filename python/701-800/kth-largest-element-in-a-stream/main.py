import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        heapq.heapify(self.stream)

        while len(self.stream) > k:
            heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        if len(self.stream) > self.k:
            heapq.heappop(self.stream)

        return self.stream[0]


self = KthLargest(3, [4, 5, 8, 2])
print(KthLargest.add(self, 3))  # return 4
print(KthLargest.add(self, 5))  # return 5
print(KthLargest.add(self, 10))  # return 5
print(KthLargest.add(self, 9))  # return 8
print(KthLargest.add(self, 4))  # return 8
