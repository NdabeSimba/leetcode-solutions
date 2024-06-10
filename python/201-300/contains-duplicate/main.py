from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()

        for num in nums:
            if num in hashtable:
                return True
            else:
                hashtable.add(num)
        
        return False