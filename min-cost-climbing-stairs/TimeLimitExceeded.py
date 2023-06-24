class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        
        def DP(n):
            if n < 2:
                return cost[n]
            return cost[n] + min(DP(n - 1), DP(n - 2))

        length = len(cost)
        return min(DP(length - 1), DP(length - 2))


self = Solution()

cost = [10,15,20]
print(Solution.minCostClimbingStairs(self, cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution.minCostClimbingStairs(self, cost))
