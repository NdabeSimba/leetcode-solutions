# Buckets O(n)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        occurences  = {}
        maxOccurence = 1

        # O(n) iterating over nums and put in hash table
        for num in nums:
            if num in occurences:
                occurences[num] = occurences[num] + 1 
                if occurences[num] + 1  > maxOccurence:
                    maxOccurence = occurences[num] + 1
            else:
                occurences[num] = 1

        # O(n) creating buckets list
        buckets = [[] for _ in range(maxOccurence)]

        # O(n) iterating over hash table keys and putting into buckets
        for num in occurences:
            buckets[occurences[num]-1].append(num)
        
        # O(k) iterating over buckets in reverse order and pop k numbers
        res = []
        for i in range(len(buckets)-1,-1,-1):
            if len(res) == k:
                    break
            while(len(buckets[i])) > 0:
                res.append(buckets[i].pop())
                if len(res) == k:
                    break
        return res

        #overall O(n) since n>k