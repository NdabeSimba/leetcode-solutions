class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i, v in enumerate(nums):
            if len(heap) == k:
                heapq.heappushpop(heap, [v, i])
            else:
                heapq.heappush(heap, [v, i])
        
        heap.sort(key=lambda x: x[1])

        print(heap)

        result = []
        for i in heap:
            result.append(i[0])

        return result