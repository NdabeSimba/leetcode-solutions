class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        min_price = 10000

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
        


self = Solution()

prices = [7,1,5,3,6,4]
print(Solution.maxProfit(self, prices))

prices = [7,6,4,3,1]
print(Solution.maxProfit(self, prices))

prices = [2,4,1]
print(Solution.maxProfit(self, prices))