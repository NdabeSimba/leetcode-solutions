from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min price
        min_price = prices[0]

        # max profit
        max_profit = 0

        for price in prices:
            if min_price > price:
                min_price = price
            
            max_profit = max(max_profit, price - min_price)
        
        return max_profit