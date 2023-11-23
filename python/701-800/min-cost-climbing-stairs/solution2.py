class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        length = len(cost)
        dp = [0] * length
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, length):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-2], dp[-1])
    

self = Solution()

cost = [10,15,20]
print(Solution.minCostClimbingStairs(self, cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution.minCostClimbingStairs(self, cost))
