class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 0
        for i in range(n):
            n1, n2 = n1 + n2, n1
        
        return n1
        


self = Solution()

n = 2
print(Solution.climbStairs(self, n))

n = 3
print(Solution.climbStairs(self, n))

n = 5
print(Solution.climbStairs(self, n))