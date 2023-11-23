# Heap O(klog(n))
import heapq


class Solution:
    def topKFrequent(nums, k):
        di = {}
        for num in nums:
            if num in di:
                di[num] += 1
            else: 
                di[num] = 1

        listOfOccurences = []
        for num in di:
            # I use negative values for di because heapq is a min - queue
            listOfOccurences.append((-di[num],num))
        
        # heapify is performed in O(n) time
        heapq.heapify(listOfOccurences)

        res = []
        # push the top k frequent elements to result O(K * log(n))
        for _ in range(k):
            res.append(heapq.heappop(listOfOccurences)[1])
        
        return res
    

nums = [4,1,-1,2,-1,2,3]
k = 2
print(Solution.topKFrequent(nums, k))