class Solution(object):
    def topKFrequent(self, nums, k):
        di = {}
        result = list()
        for num in nums:
            if num in di:
                di[num] += 1
            else: 
                di[num] = 1

        sort_di = dict(sorted(di.items(), key=lambda x: x[1], reverse=True))
        for i in range(k):
            result.append(list(sort_di.keys())[i])

        return result

# says its not the right answer, i get the same result every time.

self = Solution()

nums = [1,1,1,2,2,3]
k = 2
print(Solution.topKFrequent(self, nums, k))

nums = [4,1,-1,2,-1,2,3]
k = 2
print(Solution.topKFrequent(self, nums, k))