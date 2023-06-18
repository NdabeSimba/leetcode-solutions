from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        return [x for x,_ in Counter(nums).most_common(k)]
    

self = Solution()

nums = [1,1,1,2,2,3]
k = 2
print(Solution.topKFrequent(self, nums, k))

nums = [4,1,-1,2,-1,2,3]
k = 2
print(Solution.topKFrequent(self, nums, k))