class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b, index = m-1, n-1, m + n - 1

        while b >= 0:
            print(nums1)
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[index] = nums1[a]
                a -= 1
                
            else:
                nums1[index] = nums2[b]
                b -= 1
                
            index -= 1
            
        return nums1


self = Solution()

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
print(Solution.merge(self, nums1, m, nums2, n))

nums1 = [1]
m = 1
nums2 = []
n = 0
print(Solution.merge(self, nums1, m, nums2, n))

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
print(Solution.merge(self, nums1, m, nums2, n))