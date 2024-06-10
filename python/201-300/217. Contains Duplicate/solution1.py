# hashmap

class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)
        return False

self = Solution()

nums = [1,2,3,4]
print(Solution.containsDuplicate(self, nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution.containsDuplicate(self, nums))
