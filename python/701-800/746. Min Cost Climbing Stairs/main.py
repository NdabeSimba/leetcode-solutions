from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        if n < 3:
            return min(cost)

        for i in range(len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        print(dp)

        return min(dp[n - 1], dp[n - 2])
