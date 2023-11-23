class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        length = len(cost)

        dp = [-1 for _ in range(length + 1)]
        dp[0] = 0

        if length > 1:
            dp[1] = 0

        for i in range(2, length + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[length]


self = Solution()

cost = [10,15,20]
print(Solution.minCostClimbingStairs(self, cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution.minCostClimbingStairs(self, cost))
